import logging
import string
import weakref

import numpy

from silx.gui.plot import items

from silx.gui.plot.backends.BackendOpenGL import BackendOpenGL
from silx.gui.plot.backends.glutils import GLPlotItem

from silx.gui import _glutils
from silx.gui._glutils import gl, Texture
from silx.gui.plot3d import items as plot3d_items
from silx.gui.plot3d.scene import function, mixins,transform, primitives, utils, viewport, window
from silx.gui.plot3d.scene.cutplane import ColormapMesh3D


logging.basicConfig(level=logging.DEBUG)
_logger = logging.getLogger(__name__)


# Base class for plot3d.scene integration in PlotWidget OpenGL backend

class GLPlotItemPlot3DWrapper(GLPlotItem):
    """Allow to use silx.gui.plot3d.scene within :class:`PlotWidget`

    :param ~silx.gui.plot3d.scene.Base primitive: 3D rendering primitive
    """

    _CONTEXTS = {}  # To map system GL context id to Context objects

    def __init__(self, primitive):
        super().__init__()
        self._backendRef = None

        self._viewport = viewport.Viewport()
        self._viewport.camera.intrinsic = transform.Orthographic(
            near=1000., far=-1000., keepaspect=False)
        self._viewport.camera.extrinsic.position = 0., 0., 0.
        self._viewport.scene.children = [primitive]
        
    def setGLBackend(self, backend):
        """Set the :class:`PlotWidget` OpenGL backend to use.
        
        :param BackendOpenGL backend:
        """
        self._backendRef = None if backend is None else weakref.ref(backend)

    def getGLBackend(self):
        """Returns the :class:`PlotWidget` OpenGL backend in use.
        
        :rtype: Union[BackendOpenGL,None]
        """
        return None if self._backendRef is None else self._backendRef()

    def getScenePrimitive(self):
        """Returns the scene primitive doing the rendering

        :rtype: ~silx.gui.plot3d.scene.Base
        """
        return self._viewport.scene.children[0]

    def _syncViewport(self):
        """Synchronize viewport with current state of the backend"""
        backend = self.getGLBackend()
        if backend is None:
            _logger.error("Cannot synchronize viewport, no backend")
            return

        ox, oy, width, height = backend.getPlotBoundsInPixels()
        # Change from top to bottom reference
        oy = backend.getDevicePixelRatio() * backend.height() - height - oy
        self._viewport.origin = ox, oy
        self._viewport.size = width, height

        plotFrame = backend._plotFrame
        trBounds = plotFrame.transformedDataRanges
        left, right = trBounds[0]
        if plotFrame.isYAxisInverted:
            top, bottom = trBounds[1]
        else:
             bottom, top = trBounds[1]
        self._viewport.camera.intrinsic.size = self._viewport.size
        self._viewport.camera.intrinsic.setClipping(left, right, bottom, top)

    def _getContext(self):
        """Returns context to use for rendering.

        :rtype: Union[~silx.gui.plot3d.scene.window.ContextGL2,None]
        """
        backend = self.getGLBackend()
        if backend is None:
            return None

        glcontext = backend.context()
        if glcontext not in self._CONTEXTS:
            self._CONTEXTS[glcontext] = window.ContextGL2(glcontext)  # New context

        context = self._CONTEXTS[glcontext]
        context.devicePixelRatio = backend.getDevicePixelRatio()
        return context

    # GLPlotItem methods

    def render(self, matrix, isXLog, isYLog):
        if isXLog or isYLog:  # Log axes are not supported
            return

        context = self._getContext()
        if context is None:
            _logger.error("Cannot render, no backend")
            return

        with context as ctx:
            context.cleanGLGarbage() # Get a chance to run deferred delete

            self._syncViewport()
            ctx = viewport.RenderContext(self._viewport, context)
            self._viewport.scene.render(ctx)
            self._viewport.scene.postRender(ctx)

    def discard(self): # TODO here or not needed?
        self._viewport.scene.children = []
        # TODO call self.getGLBackend().context().cleanGLGarbage()
        # TODO make it net

    def pick(self, x, y):
        """Override in subclass"""
        pass


class PlotItemPlot3DWrapperMixIn:
    """Ease usage of GLPlotItemPlot3DWrapper in PlotWidget Items.

    This class MUST come before Item in the method resolution order.
    
    :param GLPlotItemPlot3DWrapper renderer:
    """

    def __init__(self, renderer):
        assert isinstance(renderer, GLPlotItemPlot3DWrapper)
        self._backendRenderer = renderer

    def getScenePrimitive(self):
        """Returns associated renderer.

        :rtype: GLPlotItemPlot3DWrapper
        """
        return self._backendRenderer.getScenePrimitive()

    def _setPlot(self, plot):
        """Overrides to keep a reference to the backend in use."""
        assert plot is None or isinstance(plot._backend, BackendOpenGL)
        self._backendRenderer.setGLBackend(plot._backend)
        super()._setPlot(plot)

    def _update(self, backend):
        """Overrides update strategy"""
        if backend != self._backendRenderer.getGLBackend():
            self._backendRenderer.setGLBackend(backend)
        self._dirty = False  # Reset dirty flag

    def _addBackendRenderer(self, backend):
        """Overrides backend renderer creation"""
        _logger.error("This should never be called!")
        return self._backendRenderer

    def _removeBackendRenderer(self, backend):
        """Overrides backend render removal"""
        if self._backendRenderer.getGLBackend() is backend:
            # TODO check if OK
            backend.remove(self._backendRenderer)
        self._backendRenderer.setGLBackend(None)

    def _getBounds(self):
        """Overrides bounds computation to use that of plot3d.

        Log scale axes are not supported.
        """
        plot = self.getPlot()
        if plot is not None and (
                plot.getXAxis().getScale() != items.Axis.LINEAR or
                plot.getYAxis().getScale() != items.Axis.LINEAR):
            return None  # No display with log scale for now

        image = self.getScenePrimitive()
        bounds = image.bounds(transformed=True, dataBounds=True)
        if bounds is None:
            return None
        else:
            return bounds[0, 0], bounds[1, 0], bounds[0, 1], bounds[1, 1]


# plot3d-based Image PlotWidget item replacement

class GLImageBackendItem(GLPlotItemPlot3DWrapper):
    """PlotWidget OpenGL backend data image primitive using plot3d.scene."""

    def __init__(self, image):
        image.transforms = [transform.Translate(), transform.Scale()] + image.transforms
        super().__init__(image)

    def pick(self, x, y):
        image = self.getScenePrimitive()
        origin = image.transforms[0].translation[:2]
        scale = image.transforms[1].scale[:2]
        shape = image.getData(copy=False).shape

        # Get image extent
        xmin, ymin = origin
        xmax = xmin + scale[0] * shape[1]
        if xmin > xmax:
            xmin, xmax = xmax, xmin
        ymax = ymin + scale[1] * shape[0]
        if ymin > ymax:
            ymin, ymax = ymax, ymin

        # Get indices
        if xmin <= x <= xmax and ymin <= y <= ymax:
            col = int((x - origin[0]) / scale[0])
            row = int((y - origin[1]) / scale[1])
            return (row,), (col,)
        else:
            return None


class GLImage(PlotItemPlot3DWrapperMixIn,
              items.ImageBase,
              plot3d_items.ColormapMixIn,
              plot3d_items.InterpolationMixIn):
    """Data image PlotWidget item based on plot3d.scene"""

    def __init__(self):
        items.ImageBase.__init__(self)
        plot3d_items.ColormapMixIn.__init__(self)
        plot3d_items.InterpolationMixIn.__init__(self)
        image = self._initPrimitive()
        PlotItemPlot3DWrapperMixIn.__init__(self, GLImageBackendItem(image))

        # Connect scene primitive to mix-in class
        plot3d_items.InterpolationMixIn._setPrimitive(self, image)
        plot3d_items.ColormapMixIn._setSceneColormap(self, image.colormap)
        self._glsync()

    def _initPrimitive(self):
        return primitives.ImageData(
            data=numpy.zeros((0, 0), dtype=numpy.float32))

    def _glsync(self):
        """Perform synchronisation that is not performed by mixin"""
        image = self.getScenePrimitive()
        image.alpha = self.getAlpha()
        translate, scale = image.transforms
        translate.tx, translate.ty = self.getOrigin()
        scale.sx, scale.sy = self.getScale()

    def _updated(self, event=None, checkVisibility: bool=True):
        if event in (items.ItemChangedType.ALPHA,
                     items.ItemChangedType.POSITION,
                     items.ItemChangedType.SCALE):
            self._glsync()
        return super()._updated(event=event, checkVisibility=checkVisibility)

    def getRgbaImageData(self, copy: bool=True):  # TODO remove?
        """Get the displayed RGB(A) image

        :returns: Array of uint8 of shape (height, width, 4)
        :rtype: numpy.ndarray
        """
        return self.getColormap().applyToData(self)

    def getData(self, copy: bool=True):
        """Returns the image data
        
        :param bool copy: True (Default) to get a copy,
                          False to use internal representation (do not modify!)
        """
        return self.getScenePrimitive().getData(copy=copy)

    def setData(self, data, copy: bool=True):
        """"Set the image data

        :param numpy.ndarray data: Data array with 2 dimensions (h, w)
        :param bool copy: True (Default) to make a copy,
                          False to use as is (do not modify!)
        """
        data = numpy.array(data, copy=copy)
        assert data.ndim == 2
        if data.dtype.kind == 'b':
            _logger.warning(
                'Converting boolean image to int8 to plot it.')
            data = numpy.array(data, copy=False, dtype=numpy.int8)
        elif numpy.iscomplexobj(data):
            _logger.warning(
                'Converting complex image to absolute value to plot it.')
            data = numpy.absolute(data)
        # TODO cast to valid type (u)int8|16 or float32

        self.getScenePrimitive().setData(data, copy=False)
        self._setColormappedData(self.getData(copy=False), copy=False)

        # TODO hackish data range implementation
        if self.isVisible():
            plot = self.getPlot()
            if plot is not None:
                plot._invalidateDataRange()

        self._updated(items.ItemChangedType.DATA)


class ColormapTexturedMesh3D(primitives.Geometry, mixins.DataTextureMixIn):
    """A 3D mesh with color from a 3D texture, no lighting."""

    _shaders = ("""
    attribute vec3 position;
    attribute vec3 texcoord;

    uniform mat4 matrix;
    uniform mat4 transformMat;

    varying vec4 vCameraPosition;
    varying vec3 vTexCoord;

    void main(void)
    {
        vCameraPosition = transformMat * vec4(position, 1.0);
        vTexCoord = texcoord;
        gl_Position = matrix * vec4(position, 1.0);
    }
    """,
                string.Template("""
    varying vec4 vCameraPosition;
    varying vec3 vTexCoord;
    uniform sampler3D data;
    uniform float alpha;

    $colormapDecl
    $sceneDecl

    void main(void)
    {
        $scenePreCall(vCameraPosition);

        float value = texture3D(data, vTexCoord).r;
        gl_FragColor = $colormapCall(value);
        gl_FragColor.a *= alpha;

        $scenePostCall(vCameraPosition);
    }
    """))

    def __init__(self, position, texcoord, data, copy=True,
                 mode='triangles', indices=None, colormap=None):
        assert mode in self._TRIANGLE_MODES

        self._alpha = 1.
        self._colormap = colormap or function.Colormap()  # Default colormap
        self._colormap.addListener(self._cmapChanged)

        mixins.DataTextureMixIn.__init__(self, ndim=3, data=data, copy=copy)
        primitives.Geometry.__init__(
            self, mode, indices, position=position, texcoord=texcoord)

    def setData(self, data, copy=True):
        super().setData(data, copy)

    @property
    def alpha(self):
        """Transparency of the plane, float in [0, 1]"""
        return self._alpha

    @alpha.setter
    def alpha(self, alpha):
        self._alpha = float(alpha)
        self.notify()

    @property
    def colormap(self):
        """The colormap used by this primitive"""
        return self._colormap

    def _cmapChanged(self, source, *args, **kwargs):
        """Broadcast colormap changes"""
        self.notify(*args, **kwargs)

    def prepareGL2(self, ctx):
        mixins.DataTextureMixIn.prepareGL2(self, ctx)
        primitives.Geometry.prepareGL2(self, ctx)

    def renderGL2(self, ctx):
        fragment = self._shaders[1].substitute(
            sceneDecl=ctx.fragDecl,
            scenePreCall=ctx.fragCallPre,
            scenePostCall=ctx.fragCallPost,
            colormapDecl=self.colormap.decl,
            colormapCall=self.colormap.call
            )
        program = ctx.glCtx.prog(self._shaders[0], fragment)
        program.use()

        self.colormap.setupProgram(ctx, program)

        program.setUniformMatrix('matrix', ctx.objectToNDC.matrix)
        program.setUniformMatrix('transformMat',
                                 ctx.objectToCamera.matrix,
                                 safe=True)
        gl.glUniform1f(program.uniforms['alpha'], self._alpha)
        gl.glUniform1i(program.uniforms['data'], self.texture.texUnit)

        ctx.setupProgram(program)

        with self.texture:
            self._draw(program)


class GLImageStack(GLImage):
    """Data image PlotWidget item based on plot3d.scene"""
    # TODO origin and scale taking 3 values

    def __init__(self):
        GLImage.__init__(self)
        self.__index = 0
        self.__axis = 0

    def _initPrimitive(self):
        return ColormapTexturedMesh3D(
            position=numpy.zeros((4, 3), dtype=numpy.float32),
            texcoord=numpy.zeros((4, 3), dtype=numpy.float32),
            data=numpy.zeros((0, 0, 0), dtype=numpy.float32),
            copy=False,
            mode='triangle_strip')

    def __updatePrimitive(self):
        """Update the vertices and tex coords"""
        mesh = self.getScenePrimitive()
        shape = mesh.getData(copy=False).shape
        axis = self.getSliceAxis()

        unitsquare = numpy.array(
            [(0., 0., 0.), (0., 1., 0.), (1., 0., 0.), (1., 1., 0.)],
            dtype=numpy.float32)

        size = list(reversed(shape))
        size.pop(2 - axis)
        vertices = unitsquare[:, :2] * size
        mesh.setAttribute('position', vertices, copy=False)

        texcoord = numpy.array(unitsquare, copy=True)
        texcoord[:, -1] = (self.getSliceIndex() + 0.5) / shape[axis]
        texcoord = numpy.roll(texcoord, axis=1, shift=-axis)
        mesh.setAttribute('texcoord', texcoord, copy=False)

    def _updated(self, event=None, checkVisibility: bool=True):
        if event == items.ItemChangedType.DATA:
            self.__updatePrimitive()
            self._setColormappedData(self.getData(copy=False), copy=False)
        return super()._updated(event=event, checkVisibility=checkVisibility)

    def _invalidateDataRange(self):
        """Invalidate PlotWidget data range if needed"""
        # TODO hackish data range implementation
        if self.isVisible():
            plot = self.getPlot()
            if plot is not None:
                plot._invalidateDataRange()

    def getRgbaImageData(self, copy: bool=True):
        """Get the displayed RGB(A) image

        :returns: Array of uint8 of shape (height, width, 4)
        :rtype: numpy.ndarray
        """
        return self.getColormap().applyToData(self)

    def getData(self, copy: bool=True):
        """Returns the image data
        
        :param bool copy: True (Default) to get a copy,
                          False to use internal representation (do not modify!)
        """
        slicing = [slice(None)] * 3
        slicing[self.getSliceAxis()] = self.getSliceIndex()
        return numpy.array(
            self.getStackData(copy=False)[tuple(slicing)], copy=copy)

    def setData(self, data, copy: bool=True):
        data = numpy.array(data, copy=False)
        if data.ndim == 2:  # Make it a 3D stack
            data.shape = (1,) + data.shape
        self.setStackData(data, copy)

    def getStackData(self, copy: bool=True):
        """Returns the image stack data
        
        :param bool copy: True (Default) to get a copy,
                          False to use internal representation (do not modify!)
        """
        return self.getScenePrimitive().getData(copy=copy)

    def setStackData(self, data, copy: bool=True):
        """"Set the image stack data

        :param numpy.ndarray data:
            Data array with 3 dimensions (depth, height, width)
        :param bool copy: True (Default) to make a copy,
                          False to use as is (do not modify!)
        """
        data = numpy.array(data, copy=copy)
        assert data.ndim == 3
        if data.dtype.kind == 'b':
            _logger.warning(
                'Converting boolean image to int8 to plot it.')
            data = numpy.array(data, copy=False, dtype=numpy.int8)
        elif numpy.iscomplexobj(data):
            _logger.warning(
                'Converting complex image to absolute value to plot it.')
            data = numpy.absolute(data)
        # TODO cast to valid type (u)int8|16 or float32

        previousShape = self.getStackData(copy=False).shape
        self.getScenePrimitive().setData(data, copy=False)

        if previousShape != data.shape:
            self._invalidateDataRange()
        self._updated(items.ItemChangedType.DATA)

    def __validSliceIndex(self, index: int, axis: int) -> int:
        """Returns a valid slice index for given axis and current data.
        """
        length = self.getStackData(copy=False).shape[axis]
        if index < 0:  # Handle negative index
            index += length
        index = numpy.clip(index, 0, length-1)
        return index

    def setSlice(self, index: int, axis: int) -> None:
        """Set both the slice index and dimension index at once.

        :param int index: Slice index
        :param int axis: Dimension index to slice
        """
        assert 0 <= axis <= 2
        index = self.__validSliceIndex(index, axis)
        if index != self.__index or axis != self.__axis:
            self.__index = index
            if axis != self.__axis:
                self.__axis = axis
                self._invalidateDataRange()
            self._updated(items.ItemChangedType.DATA)

    def getSliceIndex(self) -> int:
        """Returns slice index.

        :rtype: int
        """
        return self.__index

    def setSliceIndex(self, index: int) -> None:
        """Set the slice index.

        Negative index are converted to positive ones.
        Index is clipped to the stack shape.
        
        :param int index: The index of the slice.
        """
        index = self.__validSliceIndex(index, self.getSliceAxis())
        if index != self.__index:
            self.__index = index
            self._updated(items.ItemChangedType.DATA)

    def getSliceAxis(self) -> int:
        """Returns slice dimension index in [0, 2].

        :rtype: int
        """
        return self.__axis

    def setSliceAxis(self, axis: int) -> None:
        """Set the slice dimension index in [0, 2].

        :param int index: The index of the slice.
        """
        assert 0 <= axis <= 2
        if axis != self.__axis:
            self.__axis = axis
            self._invalidateDataRange()
            self._updated(items.ItemChangedType.DATA)


class DataTexture(Texture):
    """Texture keeping a CPU memory copy of the data"""

    def __init__(self, internalFormat, data, format_=None, texUnit=0,
                 minFilter=None, magFilter=None, wrap=None):
        self.__data = numpy.array(data, copy=False)

        super().__init__(
            internalFormat, self.__data, format_, None, texUnit,
            minFilter, magFilter, wrap)

    def getData(self, copy=True):
        """Returns the image data
        
        :param bool copy: True (Default) to get a copy,
                          False to use internal representation (do not modify!)
        """
        return numpy.array(self.__data, copy=copy)

    def update(self, format_, data, offset=(0, 0, 0), copy=True):
        data = numpy.array(data, copy=False)
        oz, oy, oz = offset
        depth, height, width = data.shape
        self.__data[oz:oz+depth, oy:oy+height, ox:ox+width] = data

        super().update(format_, data, offset, copy)


class ColormapTexturedMesh3D(primitives.Geometry):
    """A 3D mesh with color from a 3D texture, no lighting."""

    _shaders = ("""
    attribute vec3 position;
    attribute vec3 texcoord;

    uniform mat4 matrix;
    uniform mat4 transformMat;

    varying vec4 vCameraPosition;
    varying vec3 vTexCoord;

    void main(void)
    {
        vCameraPosition = transformMat * vec4(position, 1.0);
        vTexCoord = texcoord;
        gl_Position = matrix * vec4(position, 1.0);
    }
    """,
                string.Template("""
    varying vec4 vCameraPosition;
    varying vec3 vTexCoord;
    uniform sampler3D data;
    uniform float alpha;

    $colormapDecl
    $sceneDecl

    void main(void)
    {
        $scenePreCall(vCameraPosition);

        float value = texture3D(data, vTexCoord).r;
        gl_FragColor = $colormapCall(value);
        gl_FragColor.a *= alpha;

        $scenePostCall(vCameraPosition);
    }
    """))

    def __init__(self, position, texcoord, texture,
                 mode='triangles', indices=None, colormap=None):
        assert mode in self._TRIANGLE_MODES
        assert texture is None or isinstance(texture, Texture)

        self._alpha = 1.
        self._colormap = colormap or function.Colormap()  # Default colormap
        self._colormap.addListener(self._cmapChanged)

        self._texturesToDiscard = []
        self._texture = texture

        super().__init__(mode, indices, position=position, texcoord=texcoord)

    @property
    def texture(self):
        """Texture storing the data"""
        return self._texture

    @texture.setter
    def texture(self, texture):
        if self._texture is not None:
            self._texturesToDiscard.append(self._texture)

        self._texture = texture

    @property
    def alpha(self):
        """Transparency of the plane, float in [0, 1]"""
        return self._alpha

    @alpha.setter
    def alpha(self, alpha):
        self._alpha = float(alpha)
        self.notify()

    @property
    def colormap(self):
        """The colormap used by this primitive"""
        return self._colormap

    def _cmapChanged(self, source, *args, **kwargs):
        """Broadcast colormap changes"""
        self.notify(*args, **kwargs)

    def getData(self, copy: bool=True):
        """Returns the image data
        
        :param bool copy: True (Default) to get a copy,
                          False to use internal representation (do not modify!)
        """
        return self.texture.getData(copy=copy)

    def prepareGL2(self, ctx):
        while self._texturesToDiscard:
            self._texturesToDiscard.pop(0).discard()
        
        if self.texture is not None:
            self.texture.prepare()

        super().prepareGL2(ctx)

    def renderGL2(self, ctx):
        if self.texture is None:
            return

        fragment = self._shaders[1].substitute(
            sceneDecl=ctx.fragDecl,
            scenePreCall=ctx.fragCallPre,
            scenePostCall=ctx.fragCallPost,
            colormapDecl=self.colormap.decl,
            colormapCall=self.colormap.call
            )
        program = ctx.glCtx.prog(self._shaders[0], fragment)
        program.use()

        self.colormap.setupProgram(ctx, program)

        program.setUniformMatrix('matrix', ctx.objectToNDC.matrix)
        program.setUniformMatrix('transformMat',
                                 ctx.objectToCamera.matrix,
                                 safe=True)
        gl.glUniform1f(program.uniforms['alpha'], self._alpha)
        gl.glUniform1i(program.uniforms['data'], self.texture.texUnit)

        ctx.setupProgram(program)

        with self.texture:
            self._draw(program)


class GLImageStack(GLImage):
    """Data image PlotWidget item based on plot3d.scene"""
    # TODO origin and scale taking 3 values

    def __init__(self):
        GLImage.__init__(self)
        self.__index = 0
        self.__axis = 0
        self.__texture = None

    def _initPrimitive(self):
        return ColormapTexturedMesh3D(
            position=numpy.zeros((4, 3), dtype=numpy.float32),
            texcoord=numpy.zeros((4, 3), dtype=numpy.float32),
            texture=None,
            mode='triangle_strip')

    def __updatePrimitive(self):
        """Update the vertices and tex coords"""
        if self.__texture is None:
            return
        shape = self.__texture.getData(copy=False).shape
        axis = self.getSliceAxis()
        mesh = self.getScenePrimitive()

        unitsquare = numpy.array(
            [(0., 0., 0.), (0., 1., 0.), (1., 0., 0.), (1., 1., 0.)],
            dtype=numpy.float32)

        size = list(reversed(shape))
        size.pop(2 - axis)
        vertices = unitsquare[:, :2] * size
        mesh.setAttribute('position', vertices, copy=False)

        texcoord = numpy.array(unitsquare, copy=True)
        texcoord[:, -1] = (self.getSliceIndex() + 0.5) / shape[axis]
        texcoord = numpy.roll(texcoord, axis=1, shift=-axis)
        mesh.setAttribute('texcoord', texcoord, copy=False)

    def _updated(self, event=None, checkVisibility: bool=True):
        if event == items.ItemChangedType.DATA:
            self.__updatePrimitive()
            self._setColormappedData(self.getData(copy=False), copy=False)
        return super()._updated(event=event, checkVisibility=checkVisibility)

    def _invalidateDataRange(self):
        """Invalidate PlotWidget data range if needed"""
        # TODO hackish data range implementation
        if self.isVisible():
            plot = self.getPlot()
            if plot is not None:
                plot._invalidateDataRange()

    def getRgbaImageData(self, copy: bool=True):
        """Get the displayed RGB(A) image

        :returns: Array of uint8 of shape (height, width, 4)
        :rtype: numpy.ndarray
        """
        return self.getColormap().applyToData(self)

    def getData(self, copy: bool=True):
        """Returns the image data
        
        :param bool copy: True (Default) to get a copy,
                          False to use internal representation (do not modify!)
        """
        slicing = [slice(None)] * 3
        slicing[self.getSliceAxis()] = self.getSliceIndex()
        return numpy.array(
            self.getStackData(copy=False)[tuple(slicing)], copy=copy)

    def setData(self, data, copy: bool=True):
        data = numpy.array(data, copy=False)
        if data.ndim == 2:  # Make it a 3D stack
            data.shape = (1,) + data.shape
        self.setStackData(data, copy)

    def getStackData(self, copy: bool=True):
        """Returns the image stack data
        
        :param bool copy: True (Default) to get a copy,
                          False to use internal representation (do not modify!)
        """
        if self.__texture is None:
            return numpy.zeros((0, 0, 0), dtype=numpy.float32)
        else:
            return self.__texture.getData(copy=copy)

    def setStackData(self, data, copy: bool=True):
        """"Set the image stack data

        :param numpy.ndarray data:
            Data array with 3 dimensions (depth, height, width)
        :param bool copy: True (Default) to make a copy,
                          False to use as is (do not modify!)
        """
        data = numpy.array(data, copy=copy)
        assert data.ndim == 3
        if data.dtype.kind == 'b':
            _logger.warning(
                'Converting boolean image to int8 to plot it.')
            data = numpy.array(data, copy=False, dtype=numpy.int8)
        elif numpy.iscomplexobj(data):
            _logger.warning(
                'Converting complex image to absolute value to plot it.')
            data = numpy.absolute(data)
        # TODO cast to valid type (u)int8|16 or float32

        if self.__texture is None:  # First call during __init__
            filter_ = gl.GL_LINEAR
        else:
            filter_ = self.texture.magFilter

        self.setDataTexture(DataTexture(
            internalFormat=gl.GL_R32F,
            data=data,
            format_=gl.GL_RED,
            minFilter=filter_,
            magFilter=filter_,
            wrap=gl.GL_CLAMP_TO_EDGE))

    def getDataTexture(self):
        return self.__texture

    def setDataTexture(self, texture):
        previousShape = self.getStackData(copy=False).shape

        self.__texture = texture
        self.getScenePrimitive().texture = self.__texture

        if previousShape != self.__texture.shape:
            self._invalidateDataRange()
        self._updated(items.ItemChangedType.DATA)

    def __validSliceIndex(self, index: int, axis: int) -> int:
        """Returns a valid slice index for given axis and current data.
        """
        length = self.getStackData(copy=False).shape[axis]
        if index < 0:  # Handle negative index
            index += length
        index = numpy.clip(index, 0, length-1)
        return index

    def setSlice(self, index: int, axis: int) -> None:
        """Set both the slice index and dimension index at once.

        :param int index: Slice index
        :param int axis: Dimension index to slice
        """
        assert 0 <= axis <= 2
        index = self.__validSliceIndex(index, axis)
        if index != self.__index or axis != self.__axis:
            self.__index = index
            if axis != self.__axis:
                self.__axis = axis
                self._invalidateDataRange()
            self._updated(items.ItemChangedType.DATA)

    def getSliceIndex(self) -> int:
        """Returns slice index.

        :rtype: int
        """
        return self.__index

    def setSliceIndex(self, index: int) -> None:
        """Set the slice index.

        Negative index are converted to positive ones.
        Index is clipped to the stack shape.
        
        :param int index: The index of the slice.
        """
        index = self.__validSliceIndex(index, self.getSliceAxis())
        if index != self.__index:
            self.__index = index
            self._updated(items.ItemChangedType.DATA)

    def getSliceAxis(self) -> int:
        """Returns slice dimension index in [0, 2].

        :rtype: int
        """
        return self.__axis

    def setSliceAxis(self, axis: int) -> None:
        """Set the slice dimension index in [0, 2].

        :param int index: The index of the slice.
        """
        assert 0 <= axis <= 2
        if axis != self.__axis:
            self.__axis = axis
            self._invalidateDataRange()
            self._updated(items.ItemChangedType.DATA)


if __name__ == '__main__':
    from silx.gui import qt
    from silx.gui.plot import Plot2D

    qt.QApplication.setAttribute(qt.Qt.AA_ShareOpenGLContexts, True)
    qt.QApplication.setAttribute(qt.Qt.AA_EnableHighDpiScaling, True)
    
    app = qt.QApplication([])

    if 0:
        plot = Plot2D(backend='gl')
        image = GLImage()
        image.setName('image')
        image.setColormap(plot.getDefaultColormap())
        image.getColormap().setName('viridis')
        #image.setOrigin((2., 1.))
        #image.setScale((0.5, 1.))
        #image.setData(numpy.random.random((8000, 8000)).astype(numpy.float32))
        image.setData(numpy.arange(200).reshape(20, 10).astype(numpy.float32))
        plot.addItem(image)
        plot.setActiveImage(image.getName())
        plot.resetZoom()
        plot.show()

    shape = 1024*4, 512, 512
    #shape = 2, 3, 4
    data = numpy.random.random(numpy.prod(shape)).astype(numpy.float32).reshape(shape)

    texture = DataTexture(
        internalFormat=gl.GL_R32F,
        data=data,
        format_=gl.GL_RED,
        minFilter=gl.GL_LINEAR,
        magFilter=gl.GL_LINEAR,
        wrap=gl.GL_CLAMP_TO_EDGE)

    plots = []
    for axis in range(3):
        plot = Plot2D(backend='gl')
        plot.setGraphTitle('Plot %d' % axis)
        image = GLImageStack()
        image.setName('stack')
        image.setColormap(plot.getDefaultColormap())
        image.getColormap().setName('viridis')
        image.getColormap().setVRange(0, numpy.prod(shape))
        image.setDataTexture(texture)
        image.setSliceAxis(axis)
        plot.addItem(image)
        plot.setActiveImage(image.getName())
        plot.resetZoom()
        plot.show()
        plots.append(plot)

    def update():
        for plot in plots:
            image = plot.getActiveImage()
            assert isinstance(image, GLImageStack)
            maxindex = image.getStackData(copy=False).shape[image.getSliceAxis()]
            index = (image.getSliceIndex() + 1) % maxindex
            image.setSliceIndex((image.getSliceIndex() + 1) % maxindex)

    timer = qt.QTimer()
    timer.timeout.connect(update)
    timer.start(100)
    
    app.exec_()
