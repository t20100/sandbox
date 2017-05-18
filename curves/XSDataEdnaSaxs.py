#!/usr/bin/env python

# Taken from EDNA: license: GPL
# See https://github.com/kif/edna
#
# Generated Mon Feb 8 01:23::45 2016 by EDGenerateDS.
#

import os, sys
from xml.dom import minidom
from xml.dom import Node


strEdnaHome = os.environ.get("EDNA_HOME", None)

dictLocation = { \
 "XSDataCommon": "kernel/datamodel", \
}

try:
    from XSDataCommon import XSData
    from XSDataCommon import XSDataArray
    from XSDataCommon import XSDataBoolean
    from XSDataCommon import XSDataDouble
    from XSDataCommon import XSDataString
    from XSDataCommon import XSDataFile
    from XSDataCommon import XSDataInput
    from XSDataCommon import XSDataInteger
    from XSDataCommon import XSDataResult
    from XSDataCommon import XSDataRotation
    from XSDataCommon import XSDataVectorDouble
    from XSDataCommon import XSDataDoubleWithUnit
    from XSDataCommon import XSDataImage
    from XSDataCommon import XSDataLength
    from XSDataCommon import XSDataWavelength
except ImportError as error:
    if strEdnaHome is not None:
        for strXsdName in dictLocation:
            strXsdModule = strXsdName + ".py"
            strRootdir = os.path.dirname(os.path.abspath(os.path.join(strEdnaHome, dictLocation[strXsdName])))
            for strRoot, listDirs, listFiles in os.walk(strRootdir):
                if strXsdModule in listFiles:
                    sys.path.append(strRoot)
    else:
        raise error
from XSDataCommon import XSData
from XSDataCommon import XSDataArray
from XSDataCommon import XSDataBoolean
from XSDataCommon import XSDataDouble
from XSDataCommon import XSDataString
from XSDataCommon import XSDataFile
from XSDataCommon import XSDataInput
from XSDataCommon import XSDataInteger
from XSDataCommon import XSDataResult
from XSDataCommon import XSDataRotation
from XSDataCommon import XSDataVectorDouble
from XSDataCommon import XSDataDoubleWithUnit
from XSDataCommon import XSDataImage
from XSDataCommon import XSDataLength
from XSDataCommon import XSDataWavelength




#
# Support/utility functions.
#

# Compabiltity between Python 2 and 3:
if sys.version.startswith('3'):
    unicode = str
    from io import StringIO
else:
    from StringIO import StringIO


def showIndent(outfile, level):
    for idx in range(level):
        outfile.write(unicode('    '))


def warnEmptyAttribute(_strName, _strTypeName):
    pass
    #if not _strTypeName in ["float", "double", "string", "boolean", "integer"]:
    #    print("Warning! Non-optional attribute %s of type %s is None!" % (_strName, _strTypeName))

class MixedContainer(object):
    # Constants for category:
    CategoryNone = 0
    CategoryText = 1
    CategorySimple = 2
    CategoryComplex = 3
    # Constants for content_type:
    TypeNone = 0
    TypeText = 1
    TypeString = 2
    TypeInteger = 3
    TypeFloat = 4
    TypeDecimal = 5
    TypeDouble = 6
    TypeBoolean = 7
    def __init__(self, category, content_type, name, value):
        self.category = category
        self.content_type = content_type
        self.name = name
        self.value = value
    def getCategory(self):
        return self.category
    def getContenttype(self, content_type):
        return self.content_type
    def getValue(self):
        return self.value
    def getName(self):
        return self.name
    def export(self, outfile, level, name):
        if self.category == MixedContainer.CategoryText:
            outfile.write(self.value)
        elif self.category == MixedContainer.CategorySimple:
            self.exportSimple(outfile, level, name)
        else:     # category == MixedContainer.CategoryComplex
            self.value.export(outfile, level, name)
    def exportSimple(self, outfile, level, name):
        if self.content_type == MixedContainer.TypeString:
            outfile.write(unicode('<%s>%s</%s>' % (self.name, self.value, self.name)))
        elif self.content_type == MixedContainer.TypeInteger or \
                self.content_type == MixedContainer.TypeBoolean:
            outfile.write(unicode('<%s>%d</%s>' % (self.name, self.value, self.name)))
        elif self.content_type == MixedContainer.TypeFloat or \
                self.content_type == MixedContainer.TypeDecimal:
            outfile.write(unicode('<%s>%f</%s>' % (self.name, self.value, self.name)))
        elif self.content_type == MixedContainer.TypeDouble:
            outfile.write(unicode('<%s>%g</%s>' % (self.name, self.value, self.name)))

#
# Data representation classes.
#



class XSDataAutoRg(XSData):
    def __init__(self, isagregated=None, quality=None, lastPointUsed=None, firstPointUsed=None, i0Stdev=None, i0=None, rgStdev=None, rg=None, filename=None):
        XSData.__init__(self, )
        if filename is None:
            self._filename = None
        elif filename.__class__.__name__ == "XSDataFile":
            self._filename = filename
        else:
            strMessage = "ERROR! XSDataAutoRg constructor argument 'filename' is not XSDataFile but %s" % self._filename.__class__.__name__
            raise BaseException(strMessage)
        if rg is None:
            self._rg = None
        elif rg.__class__.__name__ == "XSDataLength":
            self._rg = rg
        else:
            strMessage = "ERROR! XSDataAutoRg constructor argument 'rg' is not XSDataLength but %s" % self._rg.__class__.__name__
            raise BaseException(strMessage)
        if rgStdev is None:
            self._rgStdev = None
        elif rgStdev.__class__.__name__ == "XSDataLength":
            self._rgStdev = rgStdev
        else:
            strMessage = "ERROR! XSDataAutoRg constructor argument 'rgStdev' is not XSDataLength but %s" % self._rgStdev.__class__.__name__
            raise BaseException(strMessage)
        if i0 is None:
            self._i0 = None
        elif i0.__class__.__name__ == "XSDataDouble":
            self._i0 = i0
        else:
            strMessage = "ERROR! XSDataAutoRg constructor argument 'i0' is not XSDataDouble but %s" % self._i0.__class__.__name__
            raise BaseException(strMessage)
        if i0Stdev is None:
            self._i0Stdev = None
        elif i0Stdev.__class__.__name__ == "XSDataDouble":
            self._i0Stdev = i0Stdev
        else:
            strMessage = "ERROR! XSDataAutoRg constructor argument 'i0Stdev' is not XSDataDouble but %s" % self._i0Stdev.__class__.__name__
            raise BaseException(strMessage)
        if firstPointUsed is None:
            self._firstPointUsed = None
        elif firstPointUsed.__class__.__name__ == "XSDataInteger":
            self._firstPointUsed = firstPointUsed
        else:
            strMessage = "ERROR! XSDataAutoRg constructor argument 'firstPointUsed' is not XSDataInteger but %s" % self._firstPointUsed.__class__.__name__
            raise BaseException(strMessage)
        if lastPointUsed is None:
            self._lastPointUsed = None
        elif lastPointUsed.__class__.__name__ == "XSDataInteger":
            self._lastPointUsed = lastPointUsed
        else:
            strMessage = "ERROR! XSDataAutoRg constructor argument 'lastPointUsed' is not XSDataInteger but %s" % self._lastPointUsed.__class__.__name__
            raise BaseException(strMessage)
        if quality is None:
            self._quality = None
        elif quality.__class__.__name__ == "XSDataDouble":
            self._quality = quality
        else:
            strMessage = "ERROR! XSDataAutoRg constructor argument 'quality' is not XSDataDouble but %s" % self._quality.__class__.__name__
            raise BaseException(strMessage)
        if isagregated is None:
            self._isagregated = None
        elif isagregated.__class__.__name__ == "XSDataBoolean":
            self._isagregated = isagregated
        else:
            strMessage = "ERROR! XSDataAutoRg constructor argument 'isagregated' is not XSDataBoolean but %s" % self._isagregated.__class__.__name__
            raise BaseException(strMessage)
    # Methods and properties for the 'filename' attribute
    def getFilename(self): return self._filename
    def setFilename(self, filename):
        if filename is None:
            self._filename = None
        elif filename.__class__.__name__ == "XSDataFile":
            self._filename = filename
        else:
            strMessage = "ERROR! XSDataAutoRg.setFilename argument is not XSDataFile but %s" % filename.__class__.__name__
            raise BaseException(strMessage)
    def delFilename(self): self._filename = None
    filename = property(getFilename, setFilename, delFilename, "Property for filename")
    # Methods and properties for the 'rg' attribute
    def getRg(self): return self._rg
    def setRg(self, rg):
        if rg is None:
            self._rg = None
        elif rg.__class__.__name__ == "XSDataLength":
            self._rg = rg
        else:
            strMessage = "ERROR! XSDataAutoRg.setRg argument is not XSDataLength but %s" % rg.__class__.__name__
            raise BaseException(strMessage)
    def delRg(self): self._rg = None
    rg = property(getRg, setRg, delRg, "Property for rg")
    # Methods and properties for the 'rgStdev' attribute
    def getRgStdev(self): return self._rgStdev
    def setRgStdev(self, rgStdev):
        if rgStdev is None:
            self._rgStdev = None
        elif rgStdev.__class__.__name__ == "XSDataLength":
            self._rgStdev = rgStdev
        else:
            strMessage = "ERROR! XSDataAutoRg.setRgStdev argument is not XSDataLength but %s" % rgStdev.__class__.__name__
            raise BaseException(strMessage)
    def delRgStdev(self): self._rgStdev = None
    rgStdev = property(getRgStdev, setRgStdev, delRgStdev, "Property for rgStdev")
    # Methods and properties for the 'i0' attribute
    def getI0(self): return self._i0
    def setI0(self, i0):
        if i0 is None:
            self._i0 = None
        elif i0.__class__.__name__ == "XSDataDouble":
            self._i0 = i0
        else:
            strMessage = "ERROR! XSDataAutoRg.setI0 argument is not XSDataDouble but %s" % i0.__class__.__name__
            raise BaseException(strMessage)
    def delI0(self): self._i0 = None
    i0 = property(getI0, setI0, delI0, "Property for i0")
    # Methods and properties for the 'i0Stdev' attribute
    def getI0Stdev(self): return self._i0Stdev
    def setI0Stdev(self, i0Stdev):
        if i0Stdev is None:
            self._i0Stdev = None
        elif i0Stdev.__class__.__name__ == "XSDataDouble":
            self._i0Stdev = i0Stdev
        else:
            strMessage = "ERROR! XSDataAutoRg.setI0Stdev argument is not XSDataDouble but %s" % i0Stdev.__class__.__name__
            raise BaseException(strMessage)
    def delI0Stdev(self): self._i0Stdev = None
    i0Stdev = property(getI0Stdev, setI0Stdev, delI0Stdev, "Property for i0Stdev")
    # Methods and properties for the 'firstPointUsed' attribute
    def getFirstPointUsed(self): return self._firstPointUsed
    def setFirstPointUsed(self, firstPointUsed):
        if firstPointUsed is None:
            self._firstPointUsed = None
        elif firstPointUsed.__class__.__name__ == "XSDataInteger":
            self._firstPointUsed = firstPointUsed
        else:
            strMessage = "ERROR! XSDataAutoRg.setFirstPointUsed argument is not XSDataInteger but %s" % firstPointUsed.__class__.__name__
            raise BaseException(strMessage)
    def delFirstPointUsed(self): self._firstPointUsed = None
    firstPointUsed = property(getFirstPointUsed, setFirstPointUsed, delFirstPointUsed, "Property for firstPointUsed")
    # Methods and properties for the 'lastPointUsed' attribute
    def getLastPointUsed(self): return self._lastPointUsed
    def setLastPointUsed(self, lastPointUsed):
        if lastPointUsed is None:
            self._lastPointUsed = None
        elif lastPointUsed.__class__.__name__ == "XSDataInteger":
            self._lastPointUsed = lastPointUsed
        else:
            strMessage = "ERROR! XSDataAutoRg.setLastPointUsed argument is not XSDataInteger but %s" % lastPointUsed.__class__.__name__
            raise BaseException(strMessage)
    def delLastPointUsed(self): self._lastPointUsed = None
    lastPointUsed = property(getLastPointUsed, setLastPointUsed, delLastPointUsed, "Property for lastPointUsed")
    # Methods and properties for the 'quality' attribute
    def getQuality(self): return self._quality
    def setQuality(self, quality):
        if quality is None:
            self._quality = None
        elif quality.__class__.__name__ == "XSDataDouble":
            self._quality = quality
        else:
            strMessage = "ERROR! XSDataAutoRg.setQuality argument is not XSDataDouble but %s" % quality.__class__.__name__
            raise BaseException(strMessage)
    def delQuality(self): self._quality = None
    quality = property(getQuality, setQuality, delQuality, "Property for quality")
    # Methods and properties for the 'isagregated' attribute
    def getIsagregated(self): return self._isagregated
    def setIsagregated(self, isagregated):
        if isagregated is None:
            self._isagregated = None
        elif isagregated.__class__.__name__ == "XSDataBoolean":
            self._isagregated = isagregated
        else:
            strMessage = "ERROR! XSDataAutoRg.setIsagregated argument is not XSDataBoolean but %s" % isagregated.__class__.__name__
            raise BaseException(strMessage)
    def delIsagregated(self): self._isagregated = None
    isagregated = property(getIsagregated, setIsagregated, delIsagregated, "Property for isagregated")
    def export(self, outfile, level, name_='XSDataAutoRg'):
        showIndent(outfile, level)
        outfile.write(unicode('<%s>\n' % name_))
        self.exportChildren(outfile, level + 1, name_)
        showIndent(outfile, level)
        outfile.write(unicode('</%s>\n' % name_))
    def exportChildren(self, outfile, level, name_='XSDataAutoRg'):
        XSData.exportChildren(self, outfile, level, name_)
        if self._filename is not None:
            self.filename.export(outfile, level, name_='filename')
        else:
            warnEmptyAttribute("filename", "XSDataFile")
        if self._rg is not None:
            self.rg.export(outfile, level, name_='rg')
        else:
            warnEmptyAttribute("rg", "XSDataLength")
        if self._rgStdev is not None:
            self.rgStdev.export(outfile, level, name_='rgStdev')
        else:
            warnEmptyAttribute("rgStdev", "XSDataLength")
        if self._i0 is not None:
            self.i0.export(outfile, level, name_='i0')
        else:
            warnEmptyAttribute("i0", "XSDataDouble")
        if self._i0Stdev is not None:
            self.i0Stdev.export(outfile, level, name_='i0Stdev')
        else:
            warnEmptyAttribute("i0Stdev", "XSDataDouble")
        if self._firstPointUsed is not None:
            self.firstPointUsed.export(outfile, level, name_='firstPointUsed')
        else:
            warnEmptyAttribute("firstPointUsed", "XSDataInteger")
        if self._lastPointUsed is not None:
            self.lastPointUsed.export(outfile, level, name_='lastPointUsed')
        else:
            warnEmptyAttribute("lastPointUsed", "XSDataInteger")
        if self._quality is not None:
            self.quality.export(outfile, level, name_='quality')
        else:
            warnEmptyAttribute("quality", "XSDataDouble")
        if self._isagregated is not None:
            self.isagregated.export(outfile, level, name_='isagregated')
        else:
            warnEmptyAttribute("isagregated", "XSDataBoolean")
    def build(self, node_):
        for child_ in node_.childNodes:
            nodeName_ = child_.nodeName.split(':')[-1]
            self.buildChildren(child_, nodeName_)
    def buildChildren(self, child_, nodeName_):
        if child_.nodeType == Node.ELEMENT_NODE and \
            nodeName_ == 'filename':
            obj_ = XSDataFile()
            obj_.build(child_)
            self.setFilename(obj_)
        elif child_.nodeType == Node.ELEMENT_NODE and \
            nodeName_ == 'rg':
            obj_ = XSDataLength()
            obj_.build(child_)
            self.setRg(obj_)
        elif child_.nodeType == Node.ELEMENT_NODE and \
            nodeName_ == 'rgStdev':
            obj_ = XSDataLength()
            obj_.build(child_)
            self.setRgStdev(obj_)
        elif child_.nodeType == Node.ELEMENT_NODE and \
            nodeName_ == 'i0':
            obj_ = XSDataDouble()
            obj_.build(child_)
            self.setI0(obj_)
        elif child_.nodeType == Node.ELEMENT_NODE and \
            nodeName_ == 'i0Stdev':
            obj_ = XSDataDouble()
            obj_.build(child_)
            self.setI0Stdev(obj_)
        elif child_.nodeType == Node.ELEMENT_NODE and \
            nodeName_ == 'firstPointUsed':
            obj_ = XSDataInteger()
            obj_.build(child_)
            self.setFirstPointUsed(obj_)
        elif child_.nodeType == Node.ELEMENT_NODE and \
            nodeName_ == 'lastPointUsed':
            obj_ = XSDataInteger()
            obj_.build(child_)
            self.setLastPointUsed(obj_)
        elif child_.nodeType == Node.ELEMENT_NODE and \
            nodeName_ == 'quality':
            obj_ = XSDataDouble()
            obj_.build(child_)
            self.setQuality(obj_)
        elif child_.nodeType == Node.ELEMENT_NODE and \
            nodeName_ == 'isagregated':
            obj_ = XSDataBoolean()
            obj_.build(child_)
            self.setIsagregated(obj_)
        XSData.buildChildren(self, child_, nodeName_)
    #Method for marshalling an object
    def marshal( self ):
        oStreamString = StringIO()
        oStreamString.write(unicode('<?xml version="1.0" ?>\n'))
        self.export( oStreamString, 0, name_="XSDataAutoRg" )
        oStringXML = oStreamString.getvalue()
        oStreamString.close()
        return oStringXML
    #Only to export the entire XML tree to a file stream on disk
    def exportToFile( self, _outfileName ):
        outfile = open( _outfileName, "w" )
        outfile.write(unicode('<?xml version=\"1.0\" ?>\n'))
        self.export( outfile, 0, name_='XSDataAutoRg' )
        outfile.close()
    #Deprecated method, replaced by exportToFile
    def outputFile( self, _outfileName ):
        print("WARNING: Method outputFile in class XSDataAutoRg is deprecated, please use instead exportToFile!")
        self.exportToFile(_outfileName)
    #Method for making a copy in a new instance
    def copy( self ):
        return XSDataAutoRg.parseString(self.marshal())
    #Static method for parsing a string
    def parseString( _inString ):
        doc = minidom.parseString(_inString)
        rootNode = doc.documentElement
        rootObj = XSDataAutoRg()
        rootObj.build(rootNode)
        # Check that all minOccurs are obeyed by marshalling the created object
        oStreamString = StringIO()
        rootObj.export( oStreamString, 0, name_="XSDataAutoRg" )
        oStreamString.close()
        return rootObj
    parseString = staticmethod( parseString )
    #Static method for parsing a file
    def parseFile( _inFilePath ):
        doc = minidom.parse(_inFilePath)
        rootNode = doc.documentElement
        rootObj = XSDataAutoRg()
        rootObj.build(rootNode)
        return rootObj
    parseFile = staticmethod( parseFile )
# end class XSDataAutoRg


class XSDataBioSaxsExperimentSetup(XSData):
    def __init__(self, normalizationFactor=None, maskFile=None, machineCurrent=None, wavelength=None, beamStopDiode=None, beamCenter_2=None, beamCenter_1=None, pixelSize_2=None, pixelSize_1=None, detectorDistance=None, detector=None):
        XSData.__init__(self, )
        if detector is None:
            self._detector = None
        elif detector.__class__.__name__ == "XSDataString":
            self._detector = detector
        else:
            strMessage = "ERROR! XSDataBioSaxsExperimentSetup constructor argument 'detector' is not XSDataString but %s" % self._detector.__class__.__name__
            raise BaseException(strMessage)
        if detectorDistance is None:
            self._detectorDistance = None
        elif detectorDistance.__class__.__name__ == "XSDataLength":
            self._detectorDistance = detectorDistance
        else:
            strMessage = "ERROR! XSDataBioSaxsExperimentSetup constructor argument 'detectorDistance' is not XSDataLength but %s" % self._detectorDistance.__class__.__name__
            raise BaseException(strMessage)
        if pixelSize_1 is None:
            self._pixelSize_1 = None
        elif pixelSize_1.__class__.__name__ == "XSDataLength":
            self._pixelSize_1 = pixelSize_1
        else:
            strMessage = "ERROR! XSDataBioSaxsExperimentSetup constructor argument 'pixelSize_1' is not XSDataLength but %s" % self._pixelSize_1.__class__.__name__
            raise BaseException(strMessage)
        if pixelSize_2 is None:
            self._pixelSize_2 = None
        elif pixelSize_2.__class__.__name__ == "XSDataLength":
            self._pixelSize_2 = pixelSize_2
        else:
            strMessage = "ERROR! XSDataBioSaxsExperimentSetup constructor argument 'pixelSize_2' is not XSDataLength but %s" % self._pixelSize_2.__class__.__name__
            raise BaseException(strMessage)
        if beamCenter_1 is None:
            self._beamCenter_1 = None
        elif beamCenter_1.__class__.__name__ == "XSDataDouble":
            self._beamCenter_1 = beamCenter_1
        else:
            strMessage = "ERROR! XSDataBioSaxsExperimentSetup constructor argument 'beamCenter_1' is not XSDataDouble but %s" % self._beamCenter_1.__class__.__name__
            raise BaseException(strMessage)
        if beamCenter_2 is None:
            self._beamCenter_2 = None
        elif beamCenter_2.__class__.__name__ == "XSDataDouble":
            self._beamCenter_2 = beamCenter_2
        else:
            strMessage = "ERROR! XSDataBioSaxsExperimentSetup constructor argument 'beamCenter_2' is not XSDataDouble but %s" % self._beamCenter_2.__class__.__name__
            raise BaseException(strMessage)
        if beamStopDiode is None:
            self._beamStopDiode = None
        elif beamStopDiode.__class__.__name__ == "XSDataDouble":
            self._beamStopDiode = beamStopDiode
        else:
            strMessage = "ERROR! XSDataBioSaxsExperimentSetup constructor argument 'beamStopDiode' is not XSDataDouble but %s" % self._beamStopDiode.__class__.__name__
            raise BaseException(strMessage)
        if wavelength is None:
            self._wavelength = None
        elif wavelength.__class__.__name__ == "XSDataWavelength":
            self._wavelength = wavelength
        else:
            strMessage = "ERROR! XSDataBioSaxsExperimentSetup constructor argument 'wavelength' is not XSDataWavelength but %s" % self._wavelength.__class__.__name__
            raise BaseException(strMessage)
        if machineCurrent is None:
            self._machineCurrent = None
        elif machineCurrent.__class__.__name__ == "XSDataDouble":
            self._machineCurrent = machineCurrent
        else:
            strMessage = "ERROR! XSDataBioSaxsExperimentSetup constructor argument 'machineCurrent' is not XSDataDouble but %s" % self._machineCurrent.__class__.__name__
            raise BaseException(strMessage)
        if maskFile is None:
            self._maskFile = None
        elif maskFile.__class__.__name__ == "XSDataImage":
            self._maskFile = maskFile
        else:
            strMessage = "ERROR! XSDataBioSaxsExperimentSetup constructor argument 'maskFile' is not XSDataImage but %s" % self._maskFile.__class__.__name__
            raise BaseException(strMessage)
        if normalizationFactor is None:
            self._normalizationFactor = None
        elif normalizationFactor.__class__.__name__ == "XSDataDouble":
            self._normalizationFactor = normalizationFactor
        else:
            strMessage = "ERROR! XSDataBioSaxsExperimentSetup constructor argument 'normalizationFactor' is not XSDataDouble but %s" % self._normalizationFactor.__class__.__name__
            raise BaseException(strMessage)
    # Methods and properties for the 'detector' attribute
    def getDetector(self): return self._detector
    def setDetector(self, detector):
        if detector is None:
            self._detector = None
        elif detector.__class__.__name__ == "XSDataString":
            self._detector = detector
        else:
            strMessage = "ERROR! XSDataBioSaxsExperimentSetup.setDetector argument is not XSDataString but %s" % detector.__class__.__name__
            raise BaseException(strMessage)
    def delDetector(self): self._detector = None
    detector = property(getDetector, setDetector, delDetector, "Property for detector")
    # Methods and properties for the 'detectorDistance' attribute
    def getDetectorDistance(self): return self._detectorDistance
    def setDetectorDistance(self, detectorDistance):
        if detectorDistance is None:
            self._detectorDistance = None
        elif detectorDistance.__class__.__name__ == "XSDataLength":
            self._detectorDistance = detectorDistance
        else:
            strMessage = "ERROR! XSDataBioSaxsExperimentSetup.setDetectorDistance argument is not XSDataLength but %s" % detectorDistance.__class__.__name__
            raise BaseException(strMessage)
    def delDetectorDistance(self): self._detectorDistance = None
    detectorDistance = property(getDetectorDistance, setDetectorDistance, delDetectorDistance, "Property for detectorDistance")
    # Methods and properties for the 'pixelSize_1' attribute
    def getPixelSize_1(self): return self._pixelSize_1
    def setPixelSize_1(self, pixelSize_1):
        if pixelSize_1 is None:
            self._pixelSize_1 = None
        elif pixelSize_1.__class__.__name__ == "XSDataLength":
            self._pixelSize_1 = pixelSize_1
        else:
            strMessage = "ERROR! XSDataBioSaxsExperimentSetup.setPixelSize_1 argument is not XSDataLength but %s" % pixelSize_1.__class__.__name__
            raise BaseException(strMessage)
    def delPixelSize_1(self): self._pixelSize_1 = None
    pixelSize_1 = property(getPixelSize_1, setPixelSize_1, delPixelSize_1, "Property for pixelSize_1")
    # Methods and properties for the 'pixelSize_2' attribute
    def getPixelSize_2(self): return self._pixelSize_2
    def setPixelSize_2(self, pixelSize_2):
        if pixelSize_2 is None:
            self._pixelSize_2 = None
        elif pixelSize_2.__class__.__name__ == "XSDataLength":
            self._pixelSize_2 = pixelSize_2
        else:
            strMessage = "ERROR! XSDataBioSaxsExperimentSetup.setPixelSize_2 argument is not XSDataLength but %s" % pixelSize_2.__class__.__name__
            raise BaseException(strMessage)
    def delPixelSize_2(self): self._pixelSize_2 = None
    pixelSize_2 = property(getPixelSize_2, setPixelSize_2, delPixelSize_2, "Property for pixelSize_2")
    # Methods and properties for the 'beamCenter_1' attribute
    def getBeamCenter_1(self): return self._beamCenter_1
    def setBeamCenter_1(self, beamCenter_1):
        if beamCenter_1 is None:
            self._beamCenter_1 = None
        elif beamCenter_1.__class__.__name__ == "XSDataDouble":
            self._beamCenter_1 = beamCenter_1
        else:
            strMessage = "ERROR! XSDataBioSaxsExperimentSetup.setBeamCenter_1 argument is not XSDataDouble but %s" % beamCenter_1.__class__.__name__
            raise BaseException(strMessage)
    def delBeamCenter_1(self): self._beamCenter_1 = None
    beamCenter_1 = property(getBeamCenter_1, setBeamCenter_1, delBeamCenter_1, "Property for beamCenter_1")
    # Methods and properties for the 'beamCenter_2' attribute
    def getBeamCenter_2(self): return self._beamCenter_2
    def setBeamCenter_2(self, beamCenter_2):
        if beamCenter_2 is None:
            self._beamCenter_2 = None
        elif beamCenter_2.__class__.__name__ == "XSDataDouble":
            self._beamCenter_2 = beamCenter_2
        else:
            strMessage = "ERROR! XSDataBioSaxsExperimentSetup.setBeamCenter_2 argument is not XSDataDouble but %s" % beamCenter_2.__class__.__name__
            raise BaseException(strMessage)
    def delBeamCenter_2(self): self._beamCenter_2 = None
    beamCenter_2 = property(getBeamCenter_2, setBeamCenter_2, delBeamCenter_2, "Property for beamCenter_2")
    # Methods and properties for the 'beamStopDiode' attribute
    def getBeamStopDiode(self): return self._beamStopDiode
    def setBeamStopDiode(self, beamStopDiode):
        if beamStopDiode is None:
            self._beamStopDiode = None
        elif beamStopDiode.__class__.__name__ == "XSDataDouble":
            self._beamStopDiode = beamStopDiode
        else:
            strMessage = "ERROR! XSDataBioSaxsExperimentSetup.setBeamStopDiode argument is not XSDataDouble but %s" % beamStopDiode.__class__.__name__
            raise BaseException(strMessage)
    def delBeamStopDiode(self): self._beamStopDiode = None
    beamStopDiode = property(getBeamStopDiode, setBeamStopDiode, delBeamStopDiode, "Property for beamStopDiode")
    # Methods and properties for the 'wavelength' attribute
    def getWavelength(self): return self._wavelength
    def setWavelength(self, wavelength):
        if wavelength is None:
            self._wavelength = None
        elif wavelength.__class__.__name__ == "XSDataWavelength":
            self._wavelength = wavelength
        else:
            strMessage = "ERROR! XSDataBioSaxsExperimentSetup.setWavelength argument is not XSDataWavelength but %s" % wavelength.__class__.__name__
            raise BaseException(strMessage)
    def delWavelength(self): self._wavelength = None
    wavelength = property(getWavelength, setWavelength, delWavelength, "Property for wavelength")
    # Methods and properties for the 'machineCurrent' attribute
    def getMachineCurrent(self): return self._machineCurrent
    def setMachineCurrent(self, machineCurrent):
        if machineCurrent is None:
            self._machineCurrent = None
        elif machineCurrent.__class__.__name__ == "XSDataDouble":
            self._machineCurrent = machineCurrent
        else:
            strMessage = "ERROR! XSDataBioSaxsExperimentSetup.setMachineCurrent argument is not XSDataDouble but %s" % machineCurrent.__class__.__name__
            raise BaseException(strMessage)
    def delMachineCurrent(self): self._machineCurrent = None
    machineCurrent = property(getMachineCurrent, setMachineCurrent, delMachineCurrent, "Property for machineCurrent")
    # Methods and properties for the 'maskFile' attribute
    def getMaskFile(self): return self._maskFile
    def setMaskFile(self, maskFile):
        if maskFile is None:
            self._maskFile = None
        elif maskFile.__class__.__name__ == "XSDataImage":
            self._maskFile = maskFile
        else:
            strMessage = "ERROR! XSDataBioSaxsExperimentSetup.setMaskFile argument is not XSDataImage but %s" % maskFile.__class__.__name__
            raise BaseException(strMessage)
    def delMaskFile(self): self._maskFile = None
    maskFile = property(getMaskFile, setMaskFile, delMaskFile, "Property for maskFile")
    # Methods and properties for the 'normalizationFactor' attribute
    def getNormalizationFactor(self): return self._normalizationFactor
    def setNormalizationFactor(self, normalizationFactor):
        if normalizationFactor is None:
            self._normalizationFactor = None
        elif normalizationFactor.__class__.__name__ == "XSDataDouble":
            self._normalizationFactor = normalizationFactor
        else:
            strMessage = "ERROR! XSDataBioSaxsExperimentSetup.setNormalizationFactor argument is not XSDataDouble but %s" % normalizationFactor.__class__.__name__
            raise BaseException(strMessage)
    def delNormalizationFactor(self): self._normalizationFactor = None
    normalizationFactor = property(getNormalizationFactor, setNormalizationFactor, delNormalizationFactor, "Property for normalizationFactor")
    def export(self, outfile, level, name_='XSDataBioSaxsExperimentSetup'):
        showIndent(outfile, level)
        outfile.write(unicode('<%s>\n' % name_))
        self.exportChildren(outfile, level + 1, name_)
        showIndent(outfile, level)
        outfile.write(unicode('</%s>\n' % name_))
    def exportChildren(self, outfile, level, name_='XSDataBioSaxsExperimentSetup'):
        XSData.exportChildren(self, outfile, level, name_)
        if self._detector is not None:
            self.detector.export(outfile, level, name_='detector')
        if self._detectorDistance is not None:
            self.detectorDistance.export(outfile, level, name_='detectorDistance')
        if self._pixelSize_1 is not None:
            self.pixelSize_1.export(outfile, level, name_='pixelSize_1')
        if self._pixelSize_2 is not None:
            self.pixelSize_2.export(outfile, level, name_='pixelSize_2')
        if self._beamCenter_1 is not None:
            self.beamCenter_1.export(outfile, level, name_='beamCenter_1')
        if self._beamCenter_2 is not None:
            self.beamCenter_2.export(outfile, level, name_='beamCenter_2')
        if self._beamStopDiode is not None:
            self.beamStopDiode.export(outfile, level, name_='beamStopDiode')
        if self._wavelength is not None:
            self.wavelength.export(outfile, level, name_='wavelength')
        if self._machineCurrent is not None:
            self.machineCurrent.export(outfile, level, name_='machineCurrent')
        if self._maskFile is not None:
            self.maskFile.export(outfile, level, name_='maskFile')
        if self._normalizationFactor is not None:
            self.normalizationFactor.export(outfile, level, name_='normalizationFactor')
    def build(self, node_):
        for child_ in node_.childNodes:
            nodeName_ = child_.nodeName.split(':')[-1]
            self.buildChildren(child_, nodeName_)
    def buildChildren(self, child_, nodeName_):
        if child_.nodeType == Node.ELEMENT_NODE and \
            nodeName_ == 'detector':
            obj_ = XSDataString()
            obj_.build(child_)
            self.setDetector(obj_)
        elif child_.nodeType == Node.ELEMENT_NODE and \
            nodeName_ == 'detectorDistance':
            obj_ = XSDataLength()
            obj_.build(child_)
            self.setDetectorDistance(obj_)
        elif child_.nodeType == Node.ELEMENT_NODE and \
            nodeName_ == 'pixelSize_1':
            obj_ = XSDataLength()
            obj_.build(child_)
            self.setPixelSize_1(obj_)
        elif child_.nodeType == Node.ELEMENT_NODE and \
            nodeName_ == 'pixelSize_2':
            obj_ = XSDataLength()
            obj_.build(child_)
            self.setPixelSize_2(obj_)
        elif child_.nodeType == Node.ELEMENT_NODE and \
            nodeName_ == 'beamCenter_1':
            obj_ = XSDataDouble()
            obj_.build(child_)
            self.setBeamCenter_1(obj_)
        elif child_.nodeType == Node.ELEMENT_NODE and \
            nodeName_ == 'beamCenter_2':
            obj_ = XSDataDouble()
            obj_.build(child_)
            self.setBeamCenter_2(obj_)
        elif child_.nodeType == Node.ELEMENT_NODE and \
            nodeName_ == 'beamStopDiode':
            obj_ = XSDataDouble()
            obj_.build(child_)
            self.setBeamStopDiode(obj_)
        elif child_.nodeType == Node.ELEMENT_NODE and \
            nodeName_ == 'wavelength':
            obj_ = XSDataWavelength()
            obj_.build(child_)
            self.setWavelength(obj_)
        elif child_.nodeType == Node.ELEMENT_NODE and \
            nodeName_ == 'machineCurrent':
            obj_ = XSDataDouble()
            obj_.build(child_)
            self.setMachineCurrent(obj_)
        elif child_.nodeType == Node.ELEMENT_NODE and \
            nodeName_ == 'maskFile':
            obj_ = XSDataImage()
            obj_.build(child_)
            self.setMaskFile(obj_)
        elif child_.nodeType == Node.ELEMENT_NODE and \
            nodeName_ == 'normalizationFactor':
            obj_ = XSDataDouble()
            obj_.build(child_)
            self.setNormalizationFactor(obj_)
        XSData.buildChildren(self, child_, nodeName_)
    #Method for marshalling an object
    def marshal( self ):
        oStreamString = StringIO()
        oStreamString.write(unicode('<?xml version="1.0" ?>\n'))
        self.export( oStreamString, 0, name_="XSDataBioSaxsExperimentSetup" )
        oStringXML = oStreamString.getvalue()
        oStreamString.close()
        return oStringXML
    #Only to export the entire XML tree to a file stream on disk
    def exportToFile( self, _outfileName ):
        outfile = open( _outfileName, "w" )
        outfile.write(unicode('<?xml version=\"1.0\" ?>\n'))
        self.export( outfile, 0, name_='XSDataBioSaxsExperimentSetup' )
        outfile.close()
    #Deprecated method, replaced by exportToFile
    def outputFile( self, _outfileName ):
        print("WARNING: Method outputFile in class XSDataBioSaxsExperimentSetup is deprecated, please use instead exportToFile!")
        self.exportToFile(_outfileName)
    #Method for making a copy in a new instance
    def copy( self ):
        return XSDataBioSaxsExperimentSetup.parseString(self.marshal())
    #Static method for parsing a string
    def parseString( _inString ):
        doc = minidom.parseString(_inString)
        rootNode = doc.documentElement
        rootObj = XSDataBioSaxsExperimentSetup()
        rootObj.build(rootNode)
        # Check that all minOccurs are obeyed by marshalling the created object
        oStreamString = StringIO()
        rootObj.export( oStreamString, 0, name_="XSDataBioSaxsExperimentSetup" )
        oStreamString.close()
        return rootObj
    parseString = staticmethod( parseString )
    #Static method for parsing a file
    def parseFile( _inFilePath ):
        doc = minidom.parse(_inFilePath)
        rootNode = doc.documentElement
        rootObj = XSDataBioSaxsExperimentSetup()
        rootObj.build(rootNode)
        return rootObj
    parseFile = staticmethod( parseFile )
# end class XSDataBioSaxsExperimentSetup


class XSDataBioSaxsSample(XSData):
    def __init__(self, temperature=None, code=None, comments=None, concentration=None):
        XSData.__init__(self, )
        if concentration is None:
            self._concentration = None
        elif concentration.__class__.__name__ == "XSDataDouble":
            self._concentration = concentration
        else:
            strMessage = "ERROR! XSDataBioSaxsSample constructor argument 'concentration' is not XSDataDouble but %s" % self._concentration.__class__.__name__
            raise BaseException(strMessage)
        if comments is None:
            self._comments = None
        elif comments.__class__.__name__ == "XSDataString":
            self._comments = comments
        else:
            strMessage = "ERROR! XSDataBioSaxsSample constructor argument 'comments' is not XSDataString but %s" % self._comments.__class__.__name__
            raise BaseException(strMessage)
        if code is None:
            self._code = None
        elif code.__class__.__name__ == "XSDataString":
            self._code = code
        else:
            strMessage = "ERROR! XSDataBioSaxsSample constructor argument 'code' is not XSDataString but %s" % self._code.__class__.__name__
            raise BaseException(strMessage)
        if temperature is None:
            self._temperature = None
        elif temperature.__class__.__name__ == "XSDataDouble":
            self._temperature = temperature
        else:
            strMessage = "ERROR! XSDataBioSaxsSample constructor argument 'temperature' is not XSDataDouble but %s" % self._temperature.__class__.__name__
            raise BaseException(strMessage)
    # Methods and properties for the 'concentration' attribute
    def getConcentration(self): return self._concentration
    def setConcentration(self, concentration):
        if concentration is None:
            self._concentration = None
        elif concentration.__class__.__name__ == "XSDataDouble":
            self._concentration = concentration
        else:
            strMessage = "ERROR! XSDataBioSaxsSample.setConcentration argument is not XSDataDouble but %s" % concentration.__class__.__name__
            raise BaseException(strMessage)
    def delConcentration(self): self._concentration = None
    concentration = property(getConcentration, setConcentration, delConcentration, "Property for concentration")
    # Methods and properties for the 'comments' attribute
    def getComments(self): return self._comments
    def setComments(self, comments):
        if comments is None:
            self._comments = None
        elif comments.__class__.__name__ == "XSDataString":
            self._comments = comments
        else:
            strMessage = "ERROR! XSDataBioSaxsSample.setComments argument is not XSDataString but %s" % comments.__class__.__name__
            raise BaseException(strMessage)
    def delComments(self): self._comments = None
    comments = property(getComments, setComments, delComments, "Property for comments")
    # Methods and properties for the 'code' attribute
    def getCode(self): return self._code
    def setCode(self, code):
        if code is None:
            self._code = None
        elif code.__class__.__name__ == "XSDataString":
            self._code = code
        else:
            strMessage = "ERROR! XSDataBioSaxsSample.setCode argument is not XSDataString but %s" % code.__class__.__name__
            raise BaseException(strMessage)
    def delCode(self): self._code = None
    code = property(getCode, setCode, delCode, "Property for code")
    # Methods and properties for the 'temperature' attribute
    def getTemperature(self): return self._temperature
    def setTemperature(self, temperature):
        if temperature is None:
            self._temperature = None
        elif temperature.__class__.__name__ == "XSDataDouble":
            self._temperature = temperature
        else:
            strMessage = "ERROR! XSDataBioSaxsSample.setTemperature argument is not XSDataDouble but %s" % temperature.__class__.__name__
            raise BaseException(strMessage)
    def delTemperature(self): self._temperature = None
    temperature = property(getTemperature, setTemperature, delTemperature, "Property for temperature")
    def export(self, outfile, level, name_='XSDataBioSaxsSample'):
        showIndent(outfile, level)
        outfile.write(unicode('<%s>\n' % name_))
        self.exportChildren(outfile, level + 1, name_)
        showIndent(outfile, level)
        outfile.write(unicode('</%s>\n' % name_))
    def exportChildren(self, outfile, level, name_='XSDataBioSaxsSample'):
        XSData.exportChildren(self, outfile, level, name_)
        if self._concentration is not None:
            self.concentration.export(outfile, level, name_='concentration')
        if self._comments is not None:
            self.comments.export(outfile, level, name_='comments')
        if self._code is not None:
            self.code.export(outfile, level, name_='code')
        if self._temperature is not None:
            self.temperature.export(outfile, level, name_='temperature')
    def build(self, node_):
        for child_ in node_.childNodes:
            nodeName_ = child_.nodeName.split(':')[-1]
            self.buildChildren(child_, nodeName_)
    def buildChildren(self, child_, nodeName_):
        if child_.nodeType == Node.ELEMENT_NODE and \
            nodeName_ == 'concentration':
            obj_ = XSDataDouble()
            obj_.build(child_)
            self.setConcentration(obj_)
        elif child_.nodeType == Node.ELEMENT_NODE and \
            nodeName_ == 'comments':
            obj_ = XSDataString()
            obj_.build(child_)
            self.setComments(obj_)
        elif child_.nodeType == Node.ELEMENT_NODE and \
            nodeName_ == 'code':
            obj_ = XSDataString()
            obj_.build(child_)
            self.setCode(obj_)
        elif child_.nodeType == Node.ELEMENT_NODE and \
            nodeName_ == 'temperature':
            obj_ = XSDataDouble()
            obj_.build(child_)
            self.setTemperature(obj_)
        XSData.buildChildren(self, child_, nodeName_)
    #Method for marshalling an object
    def marshal( self ):
        oStreamString = StringIO()
        oStreamString.write(unicode('<?xml version="1.0" ?>\n'))
        self.export( oStreamString, 0, name_="XSDataBioSaxsSample" )
        oStringXML = oStreamString.getvalue()
        oStreamString.close()
        return oStringXML
    #Only to export the entire XML tree to a file stream on disk
    def exportToFile( self, _outfileName ):
        outfile = open( _outfileName, "w" )
        outfile.write(unicode('<?xml version=\"1.0\" ?>\n'))
        self.export( outfile, 0, name_='XSDataBioSaxsSample' )
        outfile.close()
    #Deprecated method, replaced by exportToFile
    def outputFile( self, _outfileName ):
        print("WARNING: Method outputFile in class XSDataBioSaxsSample is deprecated, please use instead exportToFile!")
        self.exportToFile(_outfileName)
    #Method for making a copy in a new instance
    def copy( self ):
        return XSDataBioSaxsSample.parseString(self.marshal())
    #Static method for parsing a string
    def parseString( _inString ):
        doc = minidom.parseString(_inString)
        rootNode = doc.documentElement
        rootObj = XSDataBioSaxsSample()
        rootObj.build(rootNode)
        # Check that all minOccurs are obeyed by marshalling the created object
        oStreamString = StringIO()
        rootObj.export( oStreamString, 0, name_="XSDataBioSaxsSample" )
        oStreamString.close()
        return rootObj
    parseString = staticmethod( parseString )
    #Static method for parsing a file
    def parseFile( _inFilePath ):
        doc = minidom.parse(_inFilePath)
        rootNode = doc.documentElement
        rootObj = XSDataBioSaxsSample()
        rootObj.build(rootNode)
        return rootObj
    parseFile = staticmethod( parseFile )
# end class XSDataBioSaxsSample


class XSDataConfigGnom(XSData):
    def __init__(self, nextjob=None, rad56=None, coef=None, nreal=None, alpha=None, spot2=None, spot1=None, lw2=None, aw2=None, lh2=None, ah2=None, lw1=None, aw1=None, lh1=None, ah1=None, fwhm2=None, fwhm1=None, idet=None, deviat=None, kernel=None, lzrmax=None, lzrmin=None, rmax=None, rmin=None, jobtyp=None, lkern=None, ploerr=None, evaerr=None, plores=None, plonp=None, iscale=None, output=None, nskip2=None, nskip1=None, input2=None, input1=None, expert=None, forfac=None, printer=None):
        XSData.__init__(self, )
        if printer is None:
            self._printer = []
        elif printer.__class__.__name__ == "list":
            self._printer = printer
        else:
            strMessage = "ERROR! XSDataConfigGnom constructor argument 'printer' is not list but %s" % self._printer.__class__.__name__
            raise BaseException(strMessage)
        if forfac is None:
            self._forfac = None
        elif forfac.__class__.__name__ == "XSDataFile":
            self._forfac = forfac
        else:
            strMessage = "ERROR! XSDataConfigGnom constructor argument 'forfac' is not XSDataFile but %s" % self._forfac.__class__.__name__
            raise BaseException(strMessage)
        if expert is None:
            self._expert = None
        elif expert.__class__.__name__ == "XSDataFile":
            self._expert = expert
        else:
            strMessage = "ERROR! XSDataConfigGnom constructor argument 'expert' is not XSDataFile but %s" % self._expert.__class__.__name__
            raise BaseException(strMessage)
        if input1 is None:
            self._input1 = None
        elif input1.__class__.__name__ == "XSDataFile":
            self._input1 = input1
        else:
            strMessage = "ERROR! XSDataConfigGnom constructor argument 'input1' is not XSDataFile but %s" % self._input1.__class__.__name__
            raise BaseException(strMessage)
        if input2 is None:
            self._input2 = None
        elif input2.__class__.__name__ == "XSDataFile":
            self._input2 = input2
        else:
            strMessage = "ERROR! XSDataConfigGnom constructor argument 'input2' is not XSDataFile but %s" % self._input2.__class__.__name__
            raise BaseException(strMessage)
        if nskip1 is None:
            self._nskip1 = None
        elif nskip1.__class__.__name__ == "XSDataInteger":
            self._nskip1 = nskip1
        else:
            strMessage = "ERROR! XSDataConfigGnom constructor argument 'nskip1' is not XSDataInteger but %s" % self._nskip1.__class__.__name__
            raise BaseException(strMessage)
        if nskip2 is None:
            self._nskip2 = None
        elif nskip2.__class__.__name__ == "XSDataInteger":
            self._nskip2 = nskip2
        else:
            strMessage = "ERROR! XSDataConfigGnom constructor argument 'nskip2' is not XSDataInteger but %s" % self._nskip2.__class__.__name__
            raise BaseException(strMessage)
        if output is None:
            self._output = None
        elif output.__class__.__name__ == "XSDataFile":
            self._output = output
        else:
            strMessage = "ERROR! XSDataConfigGnom constructor argument 'output' is not XSDataFile but %s" % self._output.__class__.__name__
            raise BaseException(strMessage)
        if iscale is None:
            self._iscale = None
        elif iscale.__class__.__name__ == "XSDataInteger":
            self._iscale = iscale
        else:
            strMessage = "ERROR! XSDataConfigGnom constructor argument 'iscale' is not XSDataInteger but %s" % self._iscale.__class__.__name__
            raise BaseException(strMessage)
        if plonp is None:
            self._plonp = None
        elif plonp.__class__.__name__ == "XSDataBoolean":
            self._plonp = plonp
        else:
            strMessage = "ERROR! XSDataConfigGnom constructor argument 'plonp' is not XSDataBoolean but %s" % self._plonp.__class__.__name__
            raise BaseException(strMessage)
        if plores is None:
            self._plores = None
        elif plores.__class__.__name__ == "XSDataBoolean":
            self._plores = plores
        else:
            strMessage = "ERROR! XSDataConfigGnom constructor argument 'plores' is not XSDataBoolean but %s" % self._plores.__class__.__name__
            raise BaseException(strMessage)
        if evaerr is None:
            self._evaerr = None
        elif evaerr.__class__.__name__ == "XSDataBoolean":
            self._evaerr = evaerr
        else:
            strMessage = "ERROR! XSDataConfigGnom constructor argument 'evaerr' is not XSDataBoolean but %s" % self._evaerr.__class__.__name__
            raise BaseException(strMessage)
        if ploerr is None:
            self._ploerr = None
        elif ploerr.__class__.__name__ == "XSDataBoolean":
            self._ploerr = ploerr
        else:
            strMessage = "ERROR! XSDataConfigGnom constructor argument 'ploerr' is not XSDataBoolean but %s" % self._ploerr.__class__.__name__
            raise BaseException(strMessage)
        if lkern is None:
            self._lkern = None
        elif lkern.__class__.__name__ == "XSDataBoolean":
            self._lkern = lkern
        else:
            strMessage = "ERROR! XSDataConfigGnom constructor argument 'lkern' is not XSDataBoolean but %s" % self._lkern.__class__.__name__
            raise BaseException(strMessage)
        if jobtyp is None:
            self._jobtyp = None
        elif jobtyp.__class__.__name__ == "XSDataInteger":
            self._jobtyp = jobtyp
        else:
            strMessage = "ERROR! XSDataConfigGnom constructor argument 'jobtyp' is not XSDataInteger but %s" % self._jobtyp.__class__.__name__
            raise BaseException(strMessage)
        if rmin is None:
            self._rmin = None
        elif rmin.__class__.__name__ == "XSDataDouble":
            self._rmin = rmin
        else:
            strMessage = "ERROR! XSDataConfigGnom constructor argument 'rmin' is not XSDataDouble but %s" % self._rmin.__class__.__name__
            raise BaseException(strMessage)
        if rmax is None:
            self._rmax = None
        elif rmax.__class__.__name__ == "XSDataDouble":
            self._rmax = rmax
        else:
            strMessage = "ERROR! XSDataConfigGnom constructor argument 'rmax' is not XSDataDouble but %s" % self._rmax.__class__.__name__
            raise BaseException(strMessage)
        if lzrmin is None:
            self._lzrmin = None
        elif lzrmin.__class__.__name__ == "XSDataBoolean":
            self._lzrmin = lzrmin
        else:
            strMessage = "ERROR! XSDataConfigGnom constructor argument 'lzrmin' is not XSDataBoolean but %s" % self._lzrmin.__class__.__name__
            raise BaseException(strMessage)
        if lzrmax is None:
            self._lzrmax = None
        elif lzrmax.__class__.__name__ == "XSDataBoolean":
            self._lzrmax = lzrmax
        else:
            strMessage = "ERROR! XSDataConfigGnom constructor argument 'lzrmax' is not XSDataBoolean but %s" % self._lzrmax.__class__.__name__
            raise BaseException(strMessage)
        if kernel is None:
            self._kernel = None
        elif kernel.__class__.__name__ == "XSDataFile":
            self._kernel = kernel
        else:
            strMessage = "ERROR! XSDataConfigGnom constructor argument 'kernel' is not XSDataFile but %s" % self._kernel.__class__.__name__
            raise BaseException(strMessage)
        if deviat is None:
            self._deviat = None
        elif deviat.__class__.__name__ == "XSDataDouble":
            self._deviat = deviat
        else:
            strMessage = "ERROR! XSDataConfigGnom constructor argument 'deviat' is not XSDataDouble but %s" % self._deviat.__class__.__name__
            raise BaseException(strMessage)
        if idet is None:
            self._idet = None
        elif idet.__class__.__name__ == "XSDataInteger":
            self._idet = idet
        else:
            strMessage = "ERROR! XSDataConfigGnom constructor argument 'idet' is not XSDataInteger but %s" % self._idet.__class__.__name__
            raise BaseException(strMessage)
        if fwhm1 is None:
            self._fwhm1 = None
        elif fwhm1.__class__.__name__ == "XSDataDouble":
            self._fwhm1 = fwhm1
        else:
            strMessage = "ERROR! XSDataConfigGnom constructor argument 'fwhm1' is not XSDataDouble but %s" % self._fwhm1.__class__.__name__
            raise BaseException(strMessage)
        if fwhm2 is None:
            self._fwhm2 = None
        elif fwhm2.__class__.__name__ == "XSDataDouble":
            self._fwhm2 = fwhm2
        else:
            strMessage = "ERROR! XSDataConfigGnom constructor argument 'fwhm2' is not XSDataDouble but %s" % self._fwhm2.__class__.__name__
            raise BaseException(strMessage)
        if ah1 is None:
            self._ah1 = None
        elif ah1.__class__.__name__ == "XSDataDouble":
            self._ah1 = ah1
        else:
            strMessage = "ERROR! XSDataConfigGnom constructor argument 'ah1' is not XSDataDouble but %s" % self._ah1.__class__.__name__
            raise BaseException(strMessage)
        if lh1 is None:
            self._lh1 = None
        elif lh1.__class__.__name__ == "XSDataDouble":
            self._lh1 = lh1
        else:
            strMessage = "ERROR! XSDataConfigGnom constructor argument 'lh1' is not XSDataDouble but %s" % self._lh1.__class__.__name__
            raise BaseException(strMessage)
        if aw1 is None:
            self._aw1 = None
        elif aw1.__class__.__name__ == "XSDataDouble":
            self._aw1 = aw1
        else:
            strMessage = "ERROR! XSDataConfigGnom constructor argument 'aw1' is not XSDataDouble but %s" % self._aw1.__class__.__name__
            raise BaseException(strMessage)
        if lw1 is None:
            self._lw1 = None
        elif lw1.__class__.__name__ == "XSDataDouble":
            self._lw1 = lw1
        else:
            strMessage = "ERROR! XSDataConfigGnom constructor argument 'lw1' is not XSDataDouble but %s" % self._lw1.__class__.__name__
            raise BaseException(strMessage)
        if ah2 is None:
            self._ah2 = None
        elif ah2.__class__.__name__ == "XSDataDouble":
            self._ah2 = ah2
        else:
            strMessage = "ERROR! XSDataConfigGnom constructor argument 'ah2' is not XSDataDouble but %s" % self._ah2.__class__.__name__
            raise BaseException(strMessage)
        if lh2 is None:
            self._lh2 = None
        elif lh2.__class__.__name__ == "XSDataDouble":
            self._lh2 = lh2
        else:
            strMessage = "ERROR! XSDataConfigGnom constructor argument 'lh2' is not XSDataDouble but %s" % self._lh2.__class__.__name__
            raise BaseException(strMessage)
        if aw2 is None:
            self._aw2 = None
        elif aw2.__class__.__name__ == "XSDataDouble":
            self._aw2 = aw2
        else:
            strMessage = "ERROR! XSDataConfigGnom constructor argument 'aw2' is not XSDataDouble but %s" % self._aw2.__class__.__name__
            raise BaseException(strMessage)
        if lw2 is None:
            self._lw2 = None
        elif lw2.__class__.__name__ == "XSDataDouble":
            self._lw2 = lw2
        else:
            strMessage = "ERROR! XSDataConfigGnom constructor argument 'lw2' is not XSDataDouble but %s" % self._lw2.__class__.__name__
            raise BaseException(strMessage)
        if spot1 is None:
            self._spot1 = None
        elif spot1.__class__.__name__ == "XSDataFile":
            self._spot1 = spot1
        else:
            strMessage = "ERROR! XSDataConfigGnom constructor argument 'spot1' is not XSDataFile but %s" % self._spot1.__class__.__name__
            raise BaseException(strMessage)
        if spot2 is None:
            self._spot2 = None
        elif spot2.__class__.__name__ == "XSDataFile":
            self._spot2 = spot2
        else:
            strMessage = "ERROR! XSDataConfigGnom constructor argument 'spot2' is not XSDataFile but %s" % self._spot2.__class__.__name__
            raise BaseException(strMessage)
        if alpha is None:
            self._alpha = None
        elif alpha.__class__.__name__ == "XSDataDouble":
            self._alpha = alpha
        else:
            strMessage = "ERROR! XSDataConfigGnom constructor argument 'alpha' is not XSDataDouble but %s" % self._alpha.__class__.__name__
            raise BaseException(strMessage)
        if nreal is None:
            self._nreal = None
        elif nreal.__class__.__name__ == "XSDataInteger":
            self._nreal = nreal
        else:
            strMessage = "ERROR! XSDataConfigGnom constructor argument 'nreal' is not XSDataInteger but %s" % self._nreal.__class__.__name__
            raise BaseException(strMessage)
        if coef is None:
            self._coef = None
        elif coef.__class__.__name__ == "XSDataDouble":
            self._coef = coef
        else:
            strMessage = "ERROR! XSDataConfigGnom constructor argument 'coef' is not XSDataDouble but %s" % self._coef.__class__.__name__
            raise BaseException(strMessage)
        if rad56 is None:
            self._rad56 = None
        elif rad56.__class__.__name__ == "XSDataDouble":
            self._rad56 = rad56
        else:
            strMessage = "ERROR! XSDataConfigGnom constructor argument 'rad56' is not XSDataDouble but %s" % self._rad56.__class__.__name__
            raise BaseException(strMessage)
        if nextjob is None:
            self._nextjob = None
        elif nextjob.__class__.__name__ == "XSDataBoolean":
            self._nextjob = nextjob
        else:
            strMessage = "ERROR! XSDataConfigGnom constructor argument 'nextjob' is not XSDataBoolean but %s" % self._nextjob.__class__.__name__
            raise BaseException(strMessage)
    # Methods and properties for the 'printer' attribute
    def getPrinter(self): return self._printer
    def setPrinter(self, printer):
        if printer is None:
            self._printer = []
        elif printer.__class__.__name__ == "list":
            self._printer = printer
        else:
            strMessage = "ERROR! XSDataConfigGnom.setPrinter argument is not list but %s" % printer.__class__.__name__
            raise BaseException(strMessage)
    def delPrinter(self): self._printer = None
    printer = property(getPrinter, setPrinter, delPrinter, "Property for printer")
    def addPrinter(self, value):
        if value is None:
            strMessage = "ERROR! XSDataConfigGnom.addPrinter argument is None"
            raise BaseException(strMessage)            
        elif value.__class__.__name__ == "XSDataString":
            self._printer.append(value)
        else:
            strMessage = "ERROR! XSDataConfigGnom.addPrinter argument is not XSDataString but %s" % value.__class__.__name__
            raise BaseException(strMessage)
    def insertPrinter(self, index, value):
        if index is None:
            strMessage = "ERROR! XSDataConfigGnom.insertPrinter argument 'index' is None"
            raise BaseException(strMessage)            
        if value is None:
            strMessage = "ERROR! XSDataConfigGnom.insertPrinter argument 'value' is None"
            raise BaseException(strMessage)            
        elif value.__class__.__name__ == "XSDataString":
            self._printer[index] = value
        else:
            strMessage = "ERROR! XSDataConfigGnom.addPrinter argument is not XSDataString but %s" % value.__class__.__name__
            raise BaseException(strMessage)
    # Methods and properties for the 'forfac' attribute
    def getForfac(self): return self._forfac
    def setForfac(self, forfac):
        if forfac is None:
            self._forfac = None
        elif forfac.__class__.__name__ == "XSDataFile":
            self._forfac = forfac
        else:
            strMessage = "ERROR! XSDataConfigGnom.setForfac argument is not XSDataFile but %s" % forfac.__class__.__name__
            raise BaseException(strMessage)
    def delForfac(self): self._forfac = None
    forfac = property(getForfac, setForfac, delForfac, "Property for forfac")
    # Methods and properties for the 'expert' attribute
    def getExpert(self): return self._expert
    def setExpert(self, expert):
        if expert is None:
            self._expert = None
        elif expert.__class__.__name__ == "XSDataFile":
            self._expert = expert
        else:
            strMessage = "ERROR! XSDataConfigGnom.setExpert argument is not XSDataFile but %s" % expert.__class__.__name__
            raise BaseException(strMessage)
    def delExpert(self): self._expert = None
    expert = property(getExpert, setExpert, delExpert, "Property for expert")
    # Methods and properties for the 'input1' attribute
    def getInput1(self): return self._input1
    def setInput1(self, input1):
        if input1 is None:
            self._input1 = None
        elif input1.__class__.__name__ == "XSDataFile":
            self._input1 = input1
        else:
            strMessage = "ERROR! XSDataConfigGnom.setInput1 argument is not XSDataFile but %s" % input1.__class__.__name__
            raise BaseException(strMessage)
    def delInput1(self): self._input1 = None
    input1 = property(getInput1, setInput1, delInput1, "Property for input1")
    # Methods and properties for the 'input2' attribute
    def getInput2(self): return self._input2
    def setInput2(self, input2):
        if input2 is None:
            self._input2 = None
        elif input2.__class__.__name__ == "XSDataFile":
            self._input2 = input2
        else:
            strMessage = "ERROR! XSDataConfigGnom.setInput2 argument is not XSDataFile but %s" % input2.__class__.__name__
            raise BaseException(strMessage)
    def delInput2(self): self._input2 = None
    input2 = property(getInput2, setInput2, delInput2, "Property for input2")
    # Methods and properties for the 'nskip1' attribute
    def getNskip1(self): return self._nskip1
    def setNskip1(self, nskip1):
        if nskip1 is None:
            self._nskip1 = None
        elif nskip1.__class__.__name__ == "XSDataInteger":
            self._nskip1 = nskip1
        else:
            strMessage = "ERROR! XSDataConfigGnom.setNskip1 argument is not XSDataInteger but %s" % nskip1.__class__.__name__
            raise BaseException(strMessage)
    def delNskip1(self): self._nskip1 = None
    nskip1 = property(getNskip1, setNskip1, delNskip1, "Property for nskip1")
    # Methods and properties for the 'nskip2' attribute
    def getNskip2(self): return self._nskip2
    def setNskip2(self, nskip2):
        if nskip2 is None:
            self._nskip2 = None
        elif nskip2.__class__.__name__ == "XSDataInteger":
            self._nskip2 = nskip2
        else:
            strMessage = "ERROR! XSDataConfigGnom.setNskip2 argument is not XSDataInteger but %s" % nskip2.__class__.__name__
            raise BaseException(strMessage)
    def delNskip2(self): self._nskip2 = None
    nskip2 = property(getNskip2, setNskip2, delNskip2, "Property for nskip2")
    # Methods and properties for the 'output' attribute
    def getOutput(self): return self._output
    def setOutput(self, output):
        if output is None:
            self._output = None
        elif output.__class__.__name__ == "XSDataFile":
            self._output = output
        else:
            strMessage = "ERROR! XSDataConfigGnom.setOutput argument is not XSDataFile but %s" % output.__class__.__name__
            raise BaseException(strMessage)
    def delOutput(self): self._output = None
    output = property(getOutput, setOutput, delOutput, "Property for output")
    # Methods and properties for the 'iscale' attribute
    def getIscale(self): return self._iscale
    def setIscale(self, iscale):
        if iscale is None:
            self._iscale = None
        elif iscale.__class__.__name__ == "XSDataInteger":
            self._iscale = iscale
        else:
            strMessage = "ERROR! XSDataConfigGnom.setIscale argument is not XSDataInteger but %s" % iscale.__class__.__name__
            raise BaseException(strMessage)
    def delIscale(self): self._iscale = None
    iscale = property(getIscale, setIscale, delIscale, "Property for iscale")
    # Methods and properties for the 'plonp' attribute
    def getPlonp(self): return self._plonp
    def setPlonp(self, plonp):
        if plonp is None:
            self._plonp = None
        elif plonp.__class__.__name__ == "XSDataBoolean":
            self._plonp = plonp
        else:
            strMessage = "ERROR! XSDataConfigGnom.setPlonp argument is not XSDataBoolean but %s" % plonp.__class__.__name__
            raise BaseException(strMessage)
    def delPlonp(self): self._plonp = None
    plonp = property(getPlonp, setPlonp, delPlonp, "Property for plonp")
    # Methods and properties for the 'plores' attribute
    def getPlores(self): return self._plores
    def setPlores(self, plores):
        if plores is None:
            self._plores = None
        elif plores.__class__.__name__ == "XSDataBoolean":
            self._plores = plores
        else:
            strMessage = "ERROR! XSDataConfigGnom.setPlores argument is not XSDataBoolean but %s" % plores.__class__.__name__
            raise BaseException(strMessage)
    def delPlores(self): self._plores = None
    plores = property(getPlores, setPlores, delPlores, "Property for plores")
    # Methods and properties for the 'evaerr' attribute
    def getEvaerr(self): return self._evaerr
    def setEvaerr(self, evaerr):
        if evaerr is None:
            self._evaerr = None
        elif evaerr.__class__.__name__ == "XSDataBoolean":
            self._evaerr = evaerr
        else:
            strMessage = "ERROR! XSDataConfigGnom.setEvaerr argument is not XSDataBoolean but %s" % evaerr.__class__.__name__
            raise BaseException(strMessage)
    def delEvaerr(self): self._evaerr = None
    evaerr = property(getEvaerr, setEvaerr, delEvaerr, "Property for evaerr")
    # Methods and properties for the 'ploerr' attribute
    def getPloerr(self): return self._ploerr
    def setPloerr(self, ploerr):
        if ploerr is None:
            self._ploerr = None
        elif ploerr.__class__.__name__ == "XSDataBoolean":
            self._ploerr = ploerr
        else:
            strMessage = "ERROR! XSDataConfigGnom.setPloerr argument is not XSDataBoolean but %s" % ploerr.__class__.__name__
            raise BaseException(strMessage)
    def delPloerr(self): self._ploerr = None
    ploerr = property(getPloerr, setPloerr, delPloerr, "Property for ploerr")
    # Methods and properties for the 'lkern' attribute
    def getLkern(self): return self._lkern
    def setLkern(self, lkern):
        if lkern is None:
            self._lkern = None
        elif lkern.__class__.__name__ == "XSDataBoolean":
            self._lkern = lkern
        else:
            strMessage = "ERROR! XSDataConfigGnom.setLkern argument is not XSDataBoolean but %s" % lkern.__class__.__name__
            raise BaseException(strMessage)
    def delLkern(self): self._lkern = None
    lkern = property(getLkern, setLkern, delLkern, "Property for lkern")
    # Methods and properties for the 'jobtyp' attribute
    def getJobtyp(self): return self._jobtyp
    def setJobtyp(self, jobtyp):
        if jobtyp is None:
            self._jobtyp = None
        elif jobtyp.__class__.__name__ == "XSDataInteger":
            self._jobtyp = jobtyp
        else:
            strMessage = "ERROR! XSDataConfigGnom.setJobtyp argument is not XSDataInteger but %s" % jobtyp.__class__.__name__
            raise BaseException(strMessage)
    def delJobtyp(self): self._jobtyp = None
    jobtyp = property(getJobtyp, setJobtyp, delJobtyp, "Property for jobtyp")
    # Methods and properties for the 'rmin' attribute
    def getRmin(self): return self._rmin
    def setRmin(self, rmin):
        if rmin is None:
            self._rmin = None
        elif rmin.__class__.__name__ == "XSDataDouble":
            self._rmin = rmin
        else:
            strMessage = "ERROR! XSDataConfigGnom.setRmin argument is not XSDataDouble but %s" % rmin.__class__.__name__
            raise BaseException(strMessage)
    def delRmin(self): self._rmin = None
    rmin = property(getRmin, setRmin, delRmin, "Property for rmin")
    # Methods and properties for the 'rmax' attribute
    def getRmax(self): return self._rmax
    def setRmax(self, rmax):
        if rmax is None:
            self._rmax = None
        elif rmax.__class__.__name__ == "XSDataDouble":
            self._rmax = rmax
        else:
            strMessage = "ERROR! XSDataConfigGnom.setRmax argument is not XSDataDouble but %s" % rmax.__class__.__name__
            raise BaseException(strMessage)
    def delRmax(self): self._rmax = None
    rmax = property(getRmax, setRmax, delRmax, "Property for rmax")
    # Methods and properties for the 'lzrmin' attribute
    def getLzrmin(self): return self._lzrmin
    def setLzrmin(self, lzrmin):
        if lzrmin is None:
            self._lzrmin = None
        elif lzrmin.__class__.__name__ == "XSDataBoolean":
            self._lzrmin = lzrmin
        else:
            strMessage = "ERROR! XSDataConfigGnom.setLzrmin argument is not XSDataBoolean but %s" % lzrmin.__class__.__name__
            raise BaseException(strMessage)
    def delLzrmin(self): self._lzrmin = None
    lzrmin = property(getLzrmin, setLzrmin, delLzrmin, "Property for lzrmin")
    # Methods and properties for the 'lzrmax' attribute
    def getLzrmax(self): return self._lzrmax
    def setLzrmax(self, lzrmax):
        if lzrmax is None:
            self._lzrmax = None
        elif lzrmax.__class__.__name__ == "XSDataBoolean":
            self._lzrmax = lzrmax
        else:
            strMessage = "ERROR! XSDataConfigGnom.setLzrmax argument is not XSDataBoolean but %s" % lzrmax.__class__.__name__
            raise BaseException(strMessage)
    def delLzrmax(self): self._lzrmax = None
    lzrmax = property(getLzrmax, setLzrmax, delLzrmax, "Property for lzrmax")
    # Methods and properties for the 'kernel' attribute
    def getKernel(self): return self._kernel
    def setKernel(self, kernel):
        if kernel is None:
            self._kernel = None
        elif kernel.__class__.__name__ == "XSDataFile":
            self._kernel = kernel
        else:
            strMessage = "ERROR! XSDataConfigGnom.setKernel argument is not XSDataFile but %s" % kernel.__class__.__name__
            raise BaseException(strMessage)
    def delKernel(self): self._kernel = None
    kernel = property(getKernel, setKernel, delKernel, "Property for kernel")
    # Methods and properties for the 'deviat' attribute
    def getDeviat(self): return self._deviat
    def setDeviat(self, deviat):
        if deviat is None:
            self._deviat = None
        elif deviat.__class__.__name__ == "XSDataDouble":
            self._deviat = deviat
        else:
            strMessage = "ERROR! XSDataConfigGnom.setDeviat argument is not XSDataDouble but %s" % deviat.__class__.__name__
            raise BaseException(strMessage)
    def delDeviat(self): self._deviat = None
    deviat = property(getDeviat, setDeviat, delDeviat, "Property for deviat")
    # Methods and properties for the 'idet' attribute
    def getIdet(self): return self._idet
    def setIdet(self, idet):
        if idet is None:
            self._idet = None
        elif idet.__class__.__name__ == "XSDataInteger":
            self._idet = idet
        else:
            strMessage = "ERROR! XSDataConfigGnom.setIdet argument is not XSDataInteger but %s" % idet.__class__.__name__
            raise BaseException(strMessage)
    def delIdet(self): self._idet = None
    idet = property(getIdet, setIdet, delIdet, "Property for idet")
    # Methods and properties for the 'fwhm1' attribute
    def getFwhm1(self): return self._fwhm1
    def setFwhm1(self, fwhm1):
        if fwhm1 is None:
            self._fwhm1 = None
        elif fwhm1.__class__.__name__ == "XSDataDouble":
            self._fwhm1 = fwhm1
        else:
            strMessage = "ERROR! XSDataConfigGnom.setFwhm1 argument is not XSDataDouble but %s" % fwhm1.__class__.__name__
            raise BaseException(strMessage)
    def delFwhm1(self): self._fwhm1 = None
    fwhm1 = property(getFwhm1, setFwhm1, delFwhm1, "Property for fwhm1")
    # Methods and properties for the 'fwhm2' attribute
    def getFwhm2(self): return self._fwhm2
    def setFwhm2(self, fwhm2):
        if fwhm2 is None:
            self._fwhm2 = None
        elif fwhm2.__class__.__name__ == "XSDataDouble":
            self._fwhm2 = fwhm2
        else:
            strMessage = "ERROR! XSDataConfigGnom.setFwhm2 argument is not XSDataDouble but %s" % fwhm2.__class__.__name__
            raise BaseException(strMessage)
    def delFwhm2(self): self._fwhm2 = None
    fwhm2 = property(getFwhm2, setFwhm2, delFwhm2, "Property for fwhm2")
    # Methods and properties for the 'ah1' attribute
    def getAh1(self): return self._ah1
    def setAh1(self, ah1):
        if ah1 is None:
            self._ah1 = None
        elif ah1.__class__.__name__ == "XSDataDouble":
            self._ah1 = ah1
        else:
            strMessage = "ERROR! XSDataConfigGnom.setAh1 argument is not XSDataDouble but %s" % ah1.__class__.__name__
            raise BaseException(strMessage)
    def delAh1(self): self._ah1 = None
    ah1 = property(getAh1, setAh1, delAh1, "Property for ah1")
    # Methods and properties for the 'lh1' attribute
    def getLh1(self): return self._lh1
    def setLh1(self, lh1):
        if lh1 is None:
            self._lh1 = None
        elif lh1.__class__.__name__ == "XSDataDouble":
            self._lh1 = lh1
        else:
            strMessage = "ERROR! XSDataConfigGnom.setLh1 argument is not XSDataDouble but %s" % lh1.__class__.__name__
            raise BaseException(strMessage)
    def delLh1(self): self._lh1 = None
    lh1 = property(getLh1, setLh1, delLh1, "Property for lh1")
    # Methods and properties for the 'aw1' attribute
    def getAw1(self): return self._aw1
    def setAw1(self, aw1):
        if aw1 is None:
            self._aw1 = None
        elif aw1.__class__.__name__ == "XSDataDouble":
            self._aw1 = aw1
        else:
            strMessage = "ERROR! XSDataConfigGnom.setAw1 argument is not XSDataDouble but %s" % aw1.__class__.__name__
            raise BaseException(strMessage)
    def delAw1(self): self._aw1 = None
    aw1 = property(getAw1, setAw1, delAw1, "Property for aw1")
    # Methods and properties for the 'lw1' attribute
    def getLw1(self): return self._lw1
    def setLw1(self, lw1):
        if lw1 is None:
            self._lw1 = None
        elif lw1.__class__.__name__ == "XSDataDouble":
            self._lw1 = lw1
        else:
            strMessage = "ERROR! XSDataConfigGnom.setLw1 argument is not XSDataDouble but %s" % lw1.__class__.__name__
            raise BaseException(strMessage)
    def delLw1(self): self._lw1 = None
    lw1 = property(getLw1, setLw1, delLw1, "Property for lw1")
    # Methods and properties for the 'ah2' attribute
    def getAh2(self): return self._ah2
    def setAh2(self, ah2):
        if ah2 is None:
            self._ah2 = None
        elif ah2.__class__.__name__ == "XSDataDouble":
            self._ah2 = ah2
        else:
            strMessage = "ERROR! XSDataConfigGnom.setAh2 argument is not XSDataDouble but %s" % ah2.__class__.__name__
            raise BaseException(strMessage)
    def delAh2(self): self._ah2 = None
    ah2 = property(getAh2, setAh2, delAh2, "Property for ah2")
    # Methods and properties for the 'lh2' attribute
    def getLh2(self): return self._lh2
    def setLh2(self, lh2):
        if lh2 is None:
            self._lh2 = None
        elif lh2.__class__.__name__ == "XSDataDouble":
            self._lh2 = lh2
        else:
            strMessage = "ERROR! XSDataConfigGnom.setLh2 argument is not XSDataDouble but %s" % lh2.__class__.__name__
            raise BaseException(strMessage)
    def delLh2(self): self._lh2 = None
    lh2 = property(getLh2, setLh2, delLh2, "Property for lh2")
    # Methods and properties for the 'aw2' attribute
    def getAw2(self): return self._aw2
    def setAw2(self, aw2):
        if aw2 is None:
            self._aw2 = None
        elif aw2.__class__.__name__ == "XSDataDouble":
            self._aw2 = aw2
        else:
            strMessage = "ERROR! XSDataConfigGnom.setAw2 argument is not XSDataDouble but %s" % aw2.__class__.__name__
            raise BaseException(strMessage)
    def delAw2(self): self._aw2 = None
    aw2 = property(getAw2, setAw2, delAw2, "Property for aw2")
    # Methods and properties for the 'lw2' attribute
    def getLw2(self): return self._lw2
    def setLw2(self, lw2):
        if lw2 is None:
            self._lw2 = None
        elif lw2.__class__.__name__ == "XSDataDouble":
            self._lw2 = lw2
        else:
            strMessage = "ERROR! XSDataConfigGnom.setLw2 argument is not XSDataDouble but %s" % lw2.__class__.__name__
            raise BaseException(strMessage)
    def delLw2(self): self._lw2 = None
    lw2 = property(getLw2, setLw2, delLw2, "Property for lw2")
    # Methods and properties for the 'spot1' attribute
    def getSpot1(self): return self._spot1
    def setSpot1(self, spot1):
        if spot1 is None:
            self._spot1 = None
        elif spot1.__class__.__name__ == "XSDataFile":
            self._spot1 = spot1
        else:
            strMessage = "ERROR! XSDataConfigGnom.setSpot1 argument is not XSDataFile but %s" % spot1.__class__.__name__
            raise BaseException(strMessage)
    def delSpot1(self): self._spot1 = None
    spot1 = property(getSpot1, setSpot1, delSpot1, "Property for spot1")
    # Methods and properties for the 'spot2' attribute
    def getSpot2(self): return self._spot2
    def setSpot2(self, spot2):
        if spot2 is None:
            self._spot2 = None
        elif spot2.__class__.__name__ == "XSDataFile":
            self._spot2 = spot2
        else:
            strMessage = "ERROR! XSDataConfigGnom.setSpot2 argument is not XSDataFile but %s" % spot2.__class__.__name__
            raise BaseException(strMessage)
    def delSpot2(self): self._spot2 = None
    spot2 = property(getSpot2, setSpot2, delSpot2, "Property for spot2")
    # Methods and properties for the 'alpha' attribute
    def getAlpha(self): return self._alpha
    def setAlpha(self, alpha):
        if alpha is None:
            self._alpha = None
        elif alpha.__class__.__name__ == "XSDataDouble":
            self._alpha = alpha
        else:
            strMessage = "ERROR! XSDataConfigGnom.setAlpha argument is not XSDataDouble but %s" % alpha.__class__.__name__
            raise BaseException(strMessage)
    def delAlpha(self): self._alpha = None
    alpha = property(getAlpha, setAlpha, delAlpha, "Property for alpha")
    # Methods and properties for the 'nreal' attribute
    def getNreal(self): return self._nreal
    def setNreal(self, nreal):
        if nreal is None:
            self._nreal = None
        elif nreal.__class__.__name__ == "XSDataInteger":
            self._nreal = nreal
        else:
            strMessage = "ERROR! XSDataConfigGnom.setNreal argument is not XSDataInteger but %s" % nreal.__class__.__name__
            raise BaseException(strMessage)
    def delNreal(self): self._nreal = None
    nreal = property(getNreal, setNreal, delNreal, "Property for nreal")
    # Methods and properties for the 'coef' attribute
    def getCoef(self): return self._coef
    def setCoef(self, coef):
        if coef is None:
            self._coef = None
        elif coef.__class__.__name__ == "XSDataDouble":
            self._coef = coef
        else:
            strMessage = "ERROR! XSDataConfigGnom.setCoef argument is not XSDataDouble but %s" % coef.__class__.__name__
            raise BaseException(strMessage)
    def delCoef(self): self._coef = None
    coef = property(getCoef, setCoef, delCoef, "Property for coef")
    # Methods and properties for the 'rad56' attribute
    def getRad56(self): return self._rad56
    def setRad56(self, rad56):
        if rad56 is None:
            self._rad56 = None
        elif rad56.__class__.__name__ == "XSDataDouble":
            self._rad56 = rad56
        else:
            strMessage = "ERROR! XSDataConfigGnom.setRad56 argument is not XSDataDouble but %s" % rad56.__class__.__name__
            raise BaseException(strMessage)
    def delRad56(self): self._rad56 = None
    rad56 = property(getRad56, setRad56, delRad56, "Property for rad56")
    # Methods and properties for the 'nextjob' attribute
    def getNextjob(self): return self._nextjob
    def setNextjob(self, nextjob):
        if nextjob is None:
            self._nextjob = None
        elif nextjob.__class__.__name__ == "XSDataBoolean":
            self._nextjob = nextjob
        else:
            strMessage = "ERROR! XSDataConfigGnom.setNextjob argument is not XSDataBoolean but %s" % nextjob.__class__.__name__
            raise BaseException(strMessage)
    def delNextjob(self): self._nextjob = None
    nextjob = property(getNextjob, setNextjob, delNextjob, "Property for nextjob")
    def export(self, outfile, level, name_='XSDataConfigGnom'):
        showIndent(outfile, level)
        outfile.write(unicode('<%s>\n' % name_))
        self.exportChildren(outfile, level + 1, name_)
        showIndent(outfile, level)
        outfile.write(unicode('</%s>\n' % name_))
    def exportChildren(self, outfile, level, name_='XSDataConfigGnom'):
        XSData.exportChildren(self, outfile, level, name_)
        for printer_ in self.getPrinter():
            printer_.export(outfile, level, name_='printer')
        if self._forfac is not None:
            self.forfac.export(outfile, level, name_='forfac')
        if self._expert is not None:
            self.expert.export(outfile, level, name_='expert')
        if self._input1 is not None:
            self.input1.export(outfile, level, name_='input1')
        else:
            warnEmptyAttribute("input1", "XSDataFile")
        if self._input2 is not None:
            self.input2.export(outfile, level, name_='input2')
        if self._nskip1 is not None:
            self.nskip1.export(outfile, level, name_='nskip1')
        if self._nskip2 is not None:
            self.nskip2.export(outfile, level, name_='nskip2')
        if self._output is not None:
            self.output.export(outfile, level, name_='output')
        if self._iscale is not None:
            self.iscale.export(outfile, level, name_='iscale')
        if self._plonp is not None:
            self.plonp.export(outfile, level, name_='plonp')
        else:
            warnEmptyAttribute("plonp", "XSDataBoolean")
        if self._plores is not None:
            self.plores.export(outfile, level, name_='plores')
        else:
            warnEmptyAttribute("plores", "XSDataBoolean")
        if self._evaerr is not None:
            self.evaerr.export(outfile, level, name_='evaerr')
        if self._ploerr is not None:
            self.ploerr.export(outfile, level, name_='ploerr')
        else:
            warnEmptyAttribute("ploerr", "XSDataBoolean")
        if self._lkern is not None:
            self.lkern.export(outfile, level, name_='lkern')
        if self._jobtyp is not None:
            self.jobtyp.export(outfile, level, name_='jobtyp')
        if self._rmin is not None:
            self.rmin.export(outfile, level, name_='rmin')
        if self._rmax is not None:
            self.rmax.export(outfile, level, name_='rmax')
        if self._lzrmin is not None:
            self.lzrmin.export(outfile, level, name_='lzrmin')
        if self._lzrmax is not None:
            self.lzrmax.export(outfile, level, name_='lzrmax')
        if self._kernel is not None:
            self.kernel.export(outfile, level, name_='kernel')
        if self._deviat is not None:
            self.deviat.export(outfile, level, name_='deviat')
        else:
            warnEmptyAttribute("deviat", "XSDataDouble")
        if self._idet is not None:
            self.idet.export(outfile, level, name_='idet')
        if self._fwhm1 is not None:
            self.fwhm1.export(outfile, level, name_='fwhm1')
        if self._fwhm2 is not None:
            self.fwhm2.export(outfile, level, name_='fwhm2')
        if self._ah1 is not None:
            self.ah1.export(outfile, level, name_='ah1')
        if self._lh1 is not None:
            self.lh1.export(outfile, level, name_='lh1')
        if self._aw1 is not None:
            self.aw1.export(outfile, level, name_='aw1')
        if self._lw1 is not None:
            self.lw1.export(outfile, level, name_='lw1')
        if self._ah2 is not None:
            self.ah2.export(outfile, level, name_='ah2')
        if self._lh2 is not None:
            self.lh2.export(outfile, level, name_='lh2')
        if self._aw2 is not None:
            self.aw2.export(outfile, level, name_='aw2')
        if self._lw2 is not None:
            self.lw2.export(outfile, level, name_='lw2')
        if self._spot1 is not None:
            self.spot1.export(outfile, level, name_='spot1')
        if self._spot2 is not None:
            self.spot2.export(outfile, level, name_='spot2')
        if self._alpha is not None:
            self.alpha.export(outfile, level, name_='alpha')
        else:
            warnEmptyAttribute("alpha", "XSDataDouble")
        if self._nreal is not None:
            self.nreal.export(outfile, level, name_='nreal')
        else:
            warnEmptyAttribute("nreal", "XSDataInteger")
        if self._coef is not None:
            self.coef.export(outfile, level, name_='coef')
        if self._rad56 is not None:
            self.rad56.export(outfile, level, name_='rad56')
        if self._nextjob is not None:
            self.nextjob.export(outfile, level, name_='nextjob')
    def build(self, node_):
        for child_ in node_.childNodes:
            nodeName_ = child_.nodeName.split(':')[-1]
            self.buildChildren(child_, nodeName_)
    def buildChildren(self, child_, nodeName_):
        if child_.nodeType == Node.ELEMENT_NODE and \
            nodeName_ == 'printer':
            obj_ = XSDataString()
            obj_.build(child_)
            self.printer.append(obj_)
        elif child_.nodeType == Node.ELEMENT_NODE and \
            nodeName_ == 'forfac':
            obj_ = XSDataFile()
            obj_.build(child_)
            self.setForfac(obj_)
        elif child_.nodeType == Node.ELEMENT_NODE and \
            nodeName_ == 'expert':
            obj_ = XSDataFile()
            obj_.build(child_)
            self.setExpert(obj_)
        elif child_.nodeType == Node.ELEMENT_NODE and \
            nodeName_ == 'input1':
            obj_ = XSDataFile()
            obj_.build(child_)
            self.setInput1(obj_)
        elif child_.nodeType == Node.ELEMENT_NODE and \
            nodeName_ == 'input2':
            obj_ = XSDataFile()
            obj_.build(child_)
            self.setInput2(obj_)
        elif child_.nodeType == Node.ELEMENT_NODE and \
            nodeName_ == 'nskip1':
            obj_ = XSDataInteger()
            obj_.build(child_)
            self.setNskip1(obj_)
        elif child_.nodeType == Node.ELEMENT_NODE and \
            nodeName_ == 'nskip2':
            obj_ = XSDataInteger()
            obj_.build(child_)
            self.setNskip2(obj_)
        elif child_.nodeType == Node.ELEMENT_NODE and \
            nodeName_ == 'output':
            obj_ = XSDataFile()
            obj_.build(child_)
            self.setOutput(obj_)
        elif child_.nodeType == Node.ELEMENT_NODE and \
            nodeName_ == 'iscale':
            obj_ = XSDataInteger()
            obj_.build(child_)
            self.setIscale(obj_)
        elif child_.nodeType == Node.ELEMENT_NODE and \
            nodeName_ == 'plonp':
            obj_ = XSDataBoolean()
            obj_.build(child_)
            self.setPlonp(obj_)
        elif child_.nodeType == Node.ELEMENT_NODE and \
            nodeName_ == 'plores':
            obj_ = XSDataBoolean()
            obj_.build(child_)
            self.setPlores(obj_)
        elif child_.nodeType == Node.ELEMENT_NODE and \
            nodeName_ == 'evaerr':
            obj_ = XSDataBoolean()
            obj_.build(child_)
            self.setEvaerr(obj_)
        elif child_.nodeType == Node.ELEMENT_NODE and \
            nodeName_ == 'ploerr':
            obj_ = XSDataBoolean()
            obj_.build(child_)
            self.setPloerr(obj_)
        elif child_.nodeType == Node.ELEMENT_NODE and \
            nodeName_ == 'lkern':
            obj_ = XSDataBoolean()
            obj_.build(child_)
            self.setLkern(obj_)
        elif child_.nodeType == Node.ELEMENT_NODE and \
            nodeName_ == 'jobtyp':
            obj_ = XSDataInteger()
            obj_.build(child_)
            self.setJobtyp(obj_)
        elif child_.nodeType == Node.ELEMENT_NODE and \
            nodeName_ == 'rmin':
            obj_ = XSDataDouble()
            obj_.build(child_)
            self.setRmin(obj_)
        elif child_.nodeType == Node.ELEMENT_NODE and \
            nodeName_ == 'rmax':
            obj_ = XSDataDouble()
            obj_.build(child_)
            self.setRmax(obj_)
        elif child_.nodeType == Node.ELEMENT_NODE and \
            nodeName_ == 'lzrmin':
            obj_ = XSDataBoolean()
            obj_.build(child_)
            self.setLzrmin(obj_)
        elif child_.nodeType == Node.ELEMENT_NODE and \
            nodeName_ == 'lzrmax':
            obj_ = XSDataBoolean()
            obj_.build(child_)
            self.setLzrmax(obj_)
        elif child_.nodeType == Node.ELEMENT_NODE and \
            nodeName_ == 'kernel':
            obj_ = XSDataFile()
            obj_.build(child_)
            self.setKernel(obj_)
        elif child_.nodeType == Node.ELEMENT_NODE and \
            nodeName_ == 'deviat':
            obj_ = XSDataDouble()
            obj_.build(child_)
            self.setDeviat(obj_)
        elif child_.nodeType == Node.ELEMENT_NODE and \
            nodeName_ == 'idet':
            obj_ = XSDataInteger()
            obj_.build(child_)
            self.setIdet(obj_)
        elif child_.nodeType == Node.ELEMENT_NODE and \
            nodeName_ == 'fwhm1':
            obj_ = XSDataDouble()
            obj_.build(child_)
            self.setFwhm1(obj_)
        elif child_.nodeType == Node.ELEMENT_NODE and \
            nodeName_ == 'fwhm2':
            obj_ = XSDataDouble()
            obj_.build(child_)
            self.setFwhm2(obj_)
        elif child_.nodeType == Node.ELEMENT_NODE and \
            nodeName_ == 'ah1':
            obj_ = XSDataDouble()
            obj_.build(child_)
            self.setAh1(obj_)
        elif child_.nodeType == Node.ELEMENT_NODE and \
            nodeName_ == 'lh1':
            obj_ = XSDataDouble()
            obj_.build(child_)
            self.setLh1(obj_)
        elif child_.nodeType == Node.ELEMENT_NODE and \
            nodeName_ == 'aw1':
            obj_ = XSDataDouble()
            obj_.build(child_)
            self.setAw1(obj_)
        elif child_.nodeType == Node.ELEMENT_NODE and \
            nodeName_ == 'lw1':
            obj_ = XSDataDouble()
            obj_.build(child_)
            self.setLw1(obj_)
        elif child_.nodeType == Node.ELEMENT_NODE and \
            nodeName_ == 'ah2':
            obj_ = XSDataDouble()
            obj_.build(child_)
            self.setAh2(obj_)
        elif child_.nodeType == Node.ELEMENT_NODE and \
            nodeName_ == 'lh2':
            obj_ = XSDataDouble()
            obj_.build(child_)
            self.setLh2(obj_)
        elif child_.nodeType == Node.ELEMENT_NODE and \
            nodeName_ == 'aw2':
            obj_ = XSDataDouble()
            obj_.build(child_)
            self.setAw2(obj_)
        elif child_.nodeType == Node.ELEMENT_NODE and \
            nodeName_ == 'lw2':
            obj_ = XSDataDouble()
            obj_.build(child_)
            self.setLw2(obj_)
        elif child_.nodeType == Node.ELEMENT_NODE and \
            nodeName_ == 'spot1':
            obj_ = XSDataFile()
            obj_.build(child_)
            self.setSpot1(obj_)
        elif child_.nodeType == Node.ELEMENT_NODE and \
            nodeName_ == 'spot2':
            obj_ = XSDataFile()
            obj_.build(child_)
            self.setSpot2(obj_)
        elif child_.nodeType == Node.ELEMENT_NODE and \
            nodeName_ == 'alpha':
            obj_ = XSDataDouble()
            obj_.build(child_)
            self.setAlpha(obj_)
        elif child_.nodeType == Node.ELEMENT_NODE and \
            nodeName_ == 'nreal':
            obj_ = XSDataInteger()
            obj_.build(child_)
            self.setNreal(obj_)
        elif child_.nodeType == Node.ELEMENT_NODE and \
            nodeName_ == 'coef':
            obj_ = XSDataDouble()
            obj_.build(child_)
            self.setCoef(obj_)
        elif child_.nodeType == Node.ELEMENT_NODE and \
            nodeName_ == 'rad56':
            obj_ = XSDataDouble()
            obj_.build(child_)
            self.setRad56(obj_)
        elif child_.nodeType == Node.ELEMENT_NODE and \
            nodeName_ == 'nextjob':
            obj_ = XSDataBoolean()
            obj_.build(child_)
            self.setNextjob(obj_)
        XSData.buildChildren(self, child_, nodeName_)
    #Method for marshalling an object
    def marshal( self ):
        oStreamString = StringIO()
        oStreamString.write(unicode('<?xml version="1.0" ?>\n'))
        self.export( oStreamString, 0, name_="XSDataConfigGnom" )
        oStringXML = oStreamString.getvalue()
        oStreamString.close()
        return oStringXML
    #Only to export the entire XML tree to a file stream on disk
    def exportToFile( self, _outfileName ):
        outfile = open( _outfileName, "w" )
        outfile.write(unicode('<?xml version=\"1.0\" ?>\n'))
        self.export( outfile, 0, name_='XSDataConfigGnom' )
        outfile.close()
    #Deprecated method, replaced by exportToFile
    def outputFile( self, _outfileName ):
        print("WARNING: Method outputFile in class XSDataConfigGnom is deprecated, please use instead exportToFile!")
        self.exportToFile(_outfileName)
    #Method for making a copy in a new instance
    def copy( self ):
        return XSDataConfigGnom.parseString(self.marshal())
    #Static method for parsing a string
    def parseString( _inString ):
        doc = minidom.parseString(_inString)
        rootNode = doc.documentElement
        rootObj = XSDataConfigGnom()
        rootObj.build(rootNode)
        # Check that all minOccurs are obeyed by marshalling the created object
        oStreamString = StringIO()
        rootObj.export( oStreamString, 0, name_="XSDataConfigGnom" )
        oStreamString.close()
        return rootObj
    parseString = staticmethod( parseString )
    #Static method for parsing a file
    def parseFile( _inFilePath ):
        doc = minidom.parse(_inFilePath)
        rootNode = doc.documentElement
        rootObj = XSDataConfigGnom()
        rootObj.build(rootNode)
        return rootObj
    parseFile = staticmethod( parseFile )
# end class XSDataConfigGnom


class XSDataFileSeries(XSData):
    def __init__(self, files=None):
        XSData.__init__(self, )
        if files is None:
            self._files = []
        elif files.__class__.__name__ == "list":
            self._files = files
        else:
            strMessage = "ERROR! XSDataFileSeries constructor argument 'files' is not list but %s" % self._files.__class__.__name__
            raise BaseException(strMessage)
    # Methods and properties for the 'files' attribute
    def getFiles(self): return self._files
    def setFiles(self, files):
        if files is None:
            self._files = []
        elif files.__class__.__name__ == "list":
            self._files = files
        else:
            strMessage = "ERROR! XSDataFileSeries.setFiles argument is not list but %s" % files.__class__.__name__
            raise BaseException(strMessage)
    def delFiles(self): self._files = None
    files = property(getFiles, setFiles, delFiles, "Property for files")
    def addFiles(self, value):
        if value is None:
            strMessage = "ERROR! XSDataFileSeries.addFiles argument is None"
            raise BaseException(strMessage)            
        elif value.__class__.__name__ == "XSDataFile":
            self._files.append(value)
        else:
            strMessage = "ERROR! XSDataFileSeries.addFiles argument is not XSDataFile but %s" % value.__class__.__name__
            raise BaseException(strMessage)
    def insertFiles(self, index, value):
        if index is None:
            strMessage = "ERROR! XSDataFileSeries.insertFiles argument 'index' is None"
            raise BaseException(strMessage)            
        if value is None:
            strMessage = "ERROR! XSDataFileSeries.insertFiles argument 'value' is None"
            raise BaseException(strMessage)            
        elif value.__class__.__name__ == "XSDataFile":
            self._files[index] = value
        else:
            strMessage = "ERROR! XSDataFileSeries.addFiles argument is not XSDataFile but %s" % value.__class__.__name__
            raise BaseException(strMessage)
    def export(self, outfile, level, name_='XSDataFileSeries'):
        showIndent(outfile, level)
        outfile.write(unicode('<%s>\n' % name_))
        self.exportChildren(outfile, level + 1, name_)
        showIndent(outfile, level)
        outfile.write(unicode('</%s>\n' % name_))
    def exportChildren(self, outfile, level, name_='XSDataFileSeries'):
        XSData.exportChildren(self, outfile, level, name_)
        for files_ in self.getFiles():
            files_.export(outfile, level, name_='files')
        if self.getFiles() == []:
            warnEmptyAttribute("files", "XSDataFile")
    def build(self, node_):
        for child_ in node_.childNodes:
            nodeName_ = child_.nodeName.split(':')[-1]
            self.buildChildren(child_, nodeName_)
    def buildChildren(self, child_, nodeName_):
        if child_.nodeType == Node.ELEMENT_NODE and \
            nodeName_ == 'files':
            obj_ = XSDataFile()
            obj_.build(child_)
            self.files.append(obj_)
        XSData.buildChildren(self, child_, nodeName_)
    #Method for marshalling an object
    def marshal( self ):
        oStreamString = StringIO()
        oStreamString.write(unicode('<?xml version="1.0" ?>\n'))
        self.export( oStreamString, 0, name_="XSDataFileSeries" )
        oStringXML = oStreamString.getvalue()
        oStreamString.close()
        return oStringXML
    #Only to export the entire XML tree to a file stream on disk
    def exportToFile( self, _outfileName ):
        outfile = open( _outfileName, "w" )
        outfile.write(unicode('<?xml version=\"1.0\" ?>\n'))
        self.export( outfile, 0, name_='XSDataFileSeries' )
        outfile.close()
    #Deprecated method, replaced by exportToFile
    def outputFile( self, _outfileName ):
        print("WARNING: Method outputFile in class XSDataFileSeries is deprecated, please use instead exportToFile!")
        self.exportToFile(_outfileName)
    #Method for making a copy in a new instance
    def copy( self ):
        return XSDataFileSeries.parseString(self.marshal())
    #Static method for parsing a string
    def parseString( _inString ):
        doc = minidom.parseString(_inString)
        rootNode = doc.documentElement
        rootObj = XSDataFileSeries()
        rootObj.build(rootNode)
        # Check that all minOccurs are obeyed by marshalling the created object
        oStreamString = StringIO()
        rootObj.export( oStreamString, 0, name_="XSDataFileSeries" )
        oStreamString.close()
        return rootObj
    parseString = staticmethod( parseString )
    #Static method for parsing a file
    def parseFile( _inFilePath ):
        doc = minidom.parse(_inFilePath)
        rootNode = doc.documentElement
        rootObj = XSDataFileSeries()
        rootObj.build(rootNode)
        return rootObj
    parseFile = staticmethod( parseFile )
# end class XSDataFileSeries


class XSDataGnom(XSData):
    def __init__(self, total=None, dmax=None, rgGnom=None, rgGuinier=None, gnomFile=None):
        XSData.__init__(self, )
        if gnomFile is None:
            self._gnomFile = None
        elif gnomFile.__class__.__name__ == "XSDataFile":
            self._gnomFile = gnomFile
        else:
            strMessage = "ERROR! XSDataGnom constructor argument 'gnomFile' is not XSDataFile but %s" % self._gnomFile.__class__.__name__
            raise BaseException(strMessage)
        if rgGuinier is None:
            self._rgGuinier = None
        elif rgGuinier.__class__.__name__ == "XSDataLength":
            self._rgGuinier = rgGuinier
        else:
            strMessage = "ERROR! XSDataGnom constructor argument 'rgGuinier' is not XSDataLength but %s" % self._rgGuinier.__class__.__name__
            raise BaseException(strMessage)
        if rgGnom is None:
            self._rgGnom = None
        elif rgGnom.__class__.__name__ == "XSDataLength":
            self._rgGnom = rgGnom
        else:
            strMessage = "ERROR! XSDataGnom constructor argument 'rgGnom' is not XSDataLength but %s" % self._rgGnom.__class__.__name__
            raise BaseException(strMessage)
        if dmax is None:
            self._dmax = None
        elif dmax.__class__.__name__ == "XSDataLength":
            self._dmax = dmax
        else:
            strMessage = "ERROR! XSDataGnom constructor argument 'dmax' is not XSDataLength but %s" % self._dmax.__class__.__name__
            raise BaseException(strMessage)
        if total is None:
            self._total = None
        elif total.__class__.__name__ == "XSDataDouble":
            self._total = total
        else:
            strMessage = "ERROR! XSDataGnom constructor argument 'total' is not XSDataDouble but %s" % self._total.__class__.__name__
            raise BaseException(strMessage)
    # Methods and properties for the 'gnomFile' attribute
    def getGnomFile(self): return self._gnomFile
    def setGnomFile(self, gnomFile):
        if gnomFile is None:
            self._gnomFile = None
        elif gnomFile.__class__.__name__ == "XSDataFile":
            self._gnomFile = gnomFile
        else:
            strMessage = "ERROR! XSDataGnom.setGnomFile argument is not XSDataFile but %s" % gnomFile.__class__.__name__
            raise BaseException(strMessage)
    def delGnomFile(self): self._gnomFile = None
    gnomFile = property(getGnomFile, setGnomFile, delGnomFile, "Property for gnomFile")
    # Methods and properties for the 'rgGuinier' attribute
    def getRgGuinier(self): return self._rgGuinier
    def setRgGuinier(self, rgGuinier):
        if rgGuinier is None:
            self._rgGuinier = None
        elif rgGuinier.__class__.__name__ == "XSDataLength":
            self._rgGuinier = rgGuinier
        else:
            strMessage = "ERROR! XSDataGnom.setRgGuinier argument is not XSDataLength but %s" % rgGuinier.__class__.__name__
            raise BaseException(strMessage)
    def delRgGuinier(self): self._rgGuinier = None
    rgGuinier = property(getRgGuinier, setRgGuinier, delRgGuinier, "Property for rgGuinier")
    # Methods and properties for the 'rgGnom' attribute
    def getRgGnom(self): return self._rgGnom
    def setRgGnom(self, rgGnom):
        if rgGnom is None:
            self._rgGnom = None
        elif rgGnom.__class__.__name__ == "XSDataLength":
            self._rgGnom = rgGnom
        else:
            strMessage = "ERROR! XSDataGnom.setRgGnom argument is not XSDataLength but %s" % rgGnom.__class__.__name__
            raise BaseException(strMessage)
    def delRgGnom(self): self._rgGnom = None
    rgGnom = property(getRgGnom, setRgGnom, delRgGnom, "Property for rgGnom")
    # Methods and properties for the 'dmax' attribute
    def getDmax(self): return self._dmax
    def setDmax(self, dmax):
        if dmax is None:
            self._dmax = None
        elif dmax.__class__.__name__ == "XSDataLength":
            self._dmax = dmax
        else:
            strMessage = "ERROR! XSDataGnom.setDmax argument is not XSDataLength but %s" % dmax.__class__.__name__
            raise BaseException(strMessage)
    def delDmax(self): self._dmax = None
    dmax = property(getDmax, setDmax, delDmax, "Property for dmax")
    # Methods and properties for the 'total' attribute
    def getTotal(self): return self._total
    def setTotal(self, total):
        if total is None:
            self._total = None
        elif total.__class__.__name__ == "XSDataDouble":
            self._total = total
        else:
            strMessage = "ERROR! XSDataGnom.setTotal argument is not XSDataDouble but %s" % total.__class__.__name__
            raise BaseException(strMessage)
    def delTotal(self): self._total = None
    total = property(getTotal, setTotal, delTotal, "Property for total")
    def export(self, outfile, level, name_='XSDataGnom'):
        showIndent(outfile, level)
        outfile.write(unicode('<%s>\n' % name_))
        self.exportChildren(outfile, level + 1, name_)
        showIndent(outfile, level)
        outfile.write(unicode('</%s>\n' % name_))
    def exportChildren(self, outfile, level, name_='XSDataGnom'):
        XSData.exportChildren(self, outfile, level, name_)
        if self._gnomFile is not None:
            self.gnomFile.export(outfile, level, name_='gnomFile')
        else:
            warnEmptyAttribute("gnomFile", "XSDataFile")
        if self._rgGuinier is not None:
            self.rgGuinier.export(outfile, level, name_='rgGuinier')
        else:
            warnEmptyAttribute("rgGuinier", "XSDataLength")
        if self._rgGnom is not None:
            self.rgGnom.export(outfile, level, name_='rgGnom')
        else:
            warnEmptyAttribute("rgGnom", "XSDataLength")
        if self._dmax is not None:
            self.dmax.export(outfile, level, name_='dmax')
        else:
            warnEmptyAttribute("dmax", "XSDataLength")
        if self._total is not None:
            self.total.export(outfile, level, name_='total')
        else:
            warnEmptyAttribute("total", "XSDataDouble")
    def build(self, node_):
        for child_ in node_.childNodes:
            nodeName_ = child_.nodeName.split(':')[-1]
            self.buildChildren(child_, nodeName_)
    def buildChildren(self, child_, nodeName_):
        if child_.nodeType == Node.ELEMENT_NODE and \
            nodeName_ == 'gnomFile':
            obj_ = XSDataFile()
            obj_.build(child_)
            self.setGnomFile(obj_)
        elif child_.nodeType == Node.ELEMENT_NODE and \
            nodeName_ == 'rgGuinier':
            obj_ = XSDataLength()
            obj_.build(child_)
            self.setRgGuinier(obj_)
        elif child_.nodeType == Node.ELEMENT_NODE and \
            nodeName_ == 'rgGnom':
            obj_ = XSDataLength()
            obj_.build(child_)
            self.setRgGnom(obj_)
        elif child_.nodeType == Node.ELEMENT_NODE and \
            nodeName_ == 'dmax':
            obj_ = XSDataLength()
            obj_.build(child_)
            self.setDmax(obj_)
        elif child_.nodeType == Node.ELEMENT_NODE and \
            nodeName_ == 'total':
            obj_ = XSDataDouble()
            obj_.build(child_)
            self.setTotal(obj_)
        XSData.buildChildren(self, child_, nodeName_)
    #Method for marshalling an object
    def marshal( self ):
        oStreamString = StringIO()
        oStreamString.write(unicode('<?xml version="1.0" ?>\n'))
        self.export( oStreamString, 0, name_="XSDataGnom" )
        oStringXML = oStreamString.getvalue()
        oStreamString.close()
        return oStringXML
    #Only to export the entire XML tree to a file stream on disk
    def exportToFile( self, _outfileName ):
        outfile = open( _outfileName, "w" )
        outfile.write(unicode('<?xml version=\"1.0\" ?>\n'))
        self.export( outfile, 0, name_='XSDataGnom' )
        outfile.close()
    #Deprecated method, replaced by exportToFile
    def outputFile( self, _outfileName ):
        print("WARNING: Method outputFile in class XSDataGnom is deprecated, please use instead exportToFile!")
        self.exportToFile(_outfileName)
    #Method for making a copy in a new instance
    def copy( self ):
        return XSDataGnom.parseString(self.marshal())
    #Static method for parsing a string
    def parseString( _inString ):
        doc = minidom.parseString(_inString)
        rootNode = doc.documentElement
        rootObj = XSDataGnom()
        rootObj.build(rootNode)
        # Check that all minOccurs are obeyed by marshalling the created object
        oStreamString = StringIO()
        rootObj.export( oStreamString, 0, name_="XSDataGnom" )
        oStreamString.close()
        return rootObj
    parseString = staticmethod( parseString )
    #Static method for parsing a file
    def parseFile( _inFilePath ):
        doc = minidom.parse(_inFilePath)
        rootNode = doc.documentElement
        rootObj = XSDataGnom()
        rootObj.build(rootNode)
        return rootObj
    parseFile = staticmethod( parseFile )
# end class XSDataGnom


class XSDataSaxsModel(XSData):
    """3D model with useful metadata"""
    def __init__(self, dmax=None, rg=None, volume=None, chiSqrt=None, rfactor=None, logFile=None, firFile=None, fitFile=None, pdbFile=None, name=None):
        XSData.__init__(self, )
        if name is None:
            self._name = None
        elif name.__class__.__name__ == "XSDataString":
            self._name = name
        else:
            strMessage = "ERROR! XSDataSaxsModel constructor argument 'name' is not XSDataString but %s" % self._name.__class__.__name__
            raise BaseException(strMessage)
        if pdbFile is None:
            self._pdbFile = None
        elif pdbFile.__class__.__name__ == "XSDataFile":
            self._pdbFile = pdbFile
        else:
            strMessage = "ERROR! XSDataSaxsModel constructor argument 'pdbFile' is not XSDataFile but %s" % self._pdbFile.__class__.__name__
            raise BaseException(strMessage)
        if fitFile is None:
            self._fitFile = None
        elif fitFile.__class__.__name__ == "XSDataFile":
            self._fitFile = fitFile
        else:
            strMessage = "ERROR! XSDataSaxsModel constructor argument 'fitFile' is not XSDataFile but %s" % self._fitFile.__class__.__name__
            raise BaseException(strMessage)
        if firFile is None:
            self._firFile = None
        elif firFile.__class__.__name__ == "XSDataFile":
            self._firFile = firFile
        else:
            strMessage = "ERROR! XSDataSaxsModel constructor argument 'firFile' is not XSDataFile but %s" % self._firFile.__class__.__name__
            raise BaseException(strMessage)
        if logFile is None:
            self._logFile = None
        elif logFile.__class__.__name__ == "XSDataFile":
            self._logFile = logFile
        else:
            strMessage = "ERROR! XSDataSaxsModel constructor argument 'logFile' is not XSDataFile but %s" % self._logFile.__class__.__name__
            raise BaseException(strMessage)
        if rfactor is None:
            self._rfactor = None
        elif rfactor.__class__.__name__ == "XSDataDouble":
            self._rfactor = rfactor
        else:
            strMessage = "ERROR! XSDataSaxsModel constructor argument 'rfactor' is not XSDataDouble but %s" % self._rfactor.__class__.__name__
            raise BaseException(strMessage)
        if chiSqrt is None:
            self._chiSqrt = None
        elif chiSqrt.__class__.__name__ == "XSDataDouble":
            self._chiSqrt = chiSqrt
        else:
            strMessage = "ERROR! XSDataSaxsModel constructor argument 'chiSqrt' is not XSDataDouble but %s" % self._chiSqrt.__class__.__name__
            raise BaseException(strMessage)
        if volume is None:
            self._volume = None
        elif volume.__class__.__name__ == "XSDataDouble":
            self._volume = volume
        else:
            strMessage = "ERROR! XSDataSaxsModel constructor argument 'volume' is not XSDataDouble but %s" % self._volume.__class__.__name__
            raise BaseException(strMessage)
        if rg is None:
            self._rg = None
        elif rg.__class__.__name__ == "XSDataDouble":
            self._rg = rg
        else:
            strMessage = "ERROR! XSDataSaxsModel constructor argument 'rg' is not XSDataDouble but %s" % self._rg.__class__.__name__
            raise BaseException(strMessage)
        if dmax is None:
            self._dmax = None
        elif dmax.__class__.__name__ == "XSDataDouble":
            self._dmax = dmax
        else:
            strMessage = "ERROR! XSDataSaxsModel constructor argument 'dmax' is not XSDataDouble but %s" % self._dmax.__class__.__name__
            raise BaseException(strMessage)
    # Methods and properties for the 'name' attribute
    def getName(self): return self._name
    def setName(self, name):
        if name is None:
            self._name = None
        elif name.__class__.__name__ == "XSDataString":
            self._name = name
        else:
            strMessage = "ERROR! XSDataSaxsModel.setName argument is not XSDataString but %s" % name.__class__.__name__
            raise BaseException(strMessage)
    def delName(self): self._name = None
    name = property(getName, setName, delName, "Property for name")
    # Methods and properties for the 'pdbFile' attribute
    def getPdbFile(self): return self._pdbFile
    def setPdbFile(self, pdbFile):
        if pdbFile is None:
            self._pdbFile = None
        elif pdbFile.__class__.__name__ == "XSDataFile":
            self._pdbFile = pdbFile
        else:
            strMessage = "ERROR! XSDataSaxsModel.setPdbFile argument is not XSDataFile but %s" % pdbFile.__class__.__name__
            raise BaseException(strMessage)
    def delPdbFile(self): self._pdbFile = None
    pdbFile = property(getPdbFile, setPdbFile, delPdbFile, "Property for pdbFile")
    # Methods and properties for the 'fitFile' attribute
    def getFitFile(self): return self._fitFile
    def setFitFile(self, fitFile):
        if fitFile is None:
            self._fitFile = None
        elif fitFile.__class__.__name__ == "XSDataFile":
            self._fitFile = fitFile
        else:
            strMessage = "ERROR! XSDataSaxsModel.setFitFile argument is not XSDataFile but %s" % fitFile.__class__.__name__
            raise BaseException(strMessage)
    def delFitFile(self): self._fitFile = None
    fitFile = property(getFitFile, setFitFile, delFitFile, "Property for fitFile")
    # Methods and properties for the 'firFile' attribute
    def getFirFile(self): return self._firFile
    def setFirFile(self, firFile):
        if firFile is None:
            self._firFile = None
        elif firFile.__class__.__name__ == "XSDataFile":
            self._firFile = firFile
        else:
            strMessage = "ERROR! XSDataSaxsModel.setFirFile argument is not XSDataFile but %s" % firFile.__class__.__name__
            raise BaseException(strMessage)
    def delFirFile(self): self._firFile = None
    firFile = property(getFirFile, setFirFile, delFirFile, "Property for firFile")
    # Methods and properties for the 'logFile' attribute
    def getLogFile(self): return self._logFile
    def setLogFile(self, logFile):
        if logFile is None:
            self._logFile = None
        elif logFile.__class__.__name__ == "XSDataFile":
            self._logFile = logFile
        else:
            strMessage = "ERROR! XSDataSaxsModel.setLogFile argument is not XSDataFile but %s" % logFile.__class__.__name__
            raise BaseException(strMessage)
    def delLogFile(self): self._logFile = None
    logFile = property(getLogFile, setLogFile, delLogFile, "Property for logFile")
    # Methods and properties for the 'rfactor' attribute
    def getRfactor(self): return self._rfactor
    def setRfactor(self, rfactor):
        if rfactor is None:
            self._rfactor = None
        elif rfactor.__class__.__name__ == "XSDataDouble":
            self._rfactor = rfactor
        else:
            strMessage = "ERROR! XSDataSaxsModel.setRfactor argument is not XSDataDouble but %s" % rfactor.__class__.__name__
            raise BaseException(strMessage)
    def delRfactor(self): self._rfactor = None
    rfactor = property(getRfactor, setRfactor, delRfactor, "Property for rfactor")
    # Methods and properties for the 'chiSqrt' attribute
    def getChiSqrt(self): return self._chiSqrt
    def setChiSqrt(self, chiSqrt):
        if chiSqrt is None:
            self._chiSqrt = None
        elif chiSqrt.__class__.__name__ == "XSDataDouble":
            self._chiSqrt = chiSqrt
        else:
            strMessage = "ERROR! XSDataSaxsModel.setChiSqrt argument is not XSDataDouble but %s" % chiSqrt.__class__.__name__
            raise BaseException(strMessage)
    def delChiSqrt(self): self._chiSqrt = None
    chiSqrt = property(getChiSqrt, setChiSqrt, delChiSqrt, "Property for chiSqrt")
    # Methods and properties for the 'volume' attribute
    def getVolume(self): return self._volume
    def setVolume(self, volume):
        if volume is None:
            self._volume = None
        elif volume.__class__.__name__ == "XSDataDouble":
            self._volume = volume
        else:
            strMessage = "ERROR! XSDataSaxsModel.setVolume argument is not XSDataDouble but %s" % volume.__class__.__name__
            raise BaseException(strMessage)
    def delVolume(self): self._volume = None
    volume = property(getVolume, setVolume, delVolume, "Property for volume")
    # Methods and properties for the 'rg' attribute
    def getRg(self): return self._rg
    def setRg(self, rg):
        if rg is None:
            self._rg = None
        elif rg.__class__.__name__ == "XSDataDouble":
            self._rg = rg
        else:
            strMessage = "ERROR! XSDataSaxsModel.setRg argument is not XSDataDouble but %s" % rg.__class__.__name__
            raise BaseException(strMessage)
    def delRg(self): self._rg = None
    rg = property(getRg, setRg, delRg, "Property for rg")
    # Methods and properties for the 'dmax' attribute
    def getDmax(self): return self._dmax
    def setDmax(self, dmax):
        if dmax is None:
            self._dmax = None
        elif dmax.__class__.__name__ == "XSDataDouble":
            self._dmax = dmax
        else:
            strMessage = "ERROR! XSDataSaxsModel.setDmax argument is not XSDataDouble but %s" % dmax.__class__.__name__
            raise BaseException(strMessage)
    def delDmax(self): self._dmax = None
    dmax = property(getDmax, setDmax, delDmax, "Property for dmax")
    def export(self, outfile, level, name_='XSDataSaxsModel'):
        showIndent(outfile, level)
        outfile.write(unicode('<%s>\n' % name_))
        self.exportChildren(outfile, level + 1, name_)
        showIndent(outfile, level)
        outfile.write(unicode('</%s>\n' % name_))
    def exportChildren(self, outfile, level, name_='XSDataSaxsModel'):
        XSData.exportChildren(self, outfile, level, name_)
        if self._name is not None:
            self.name.export(outfile, level, name_='name')
        else:
            warnEmptyAttribute("name", "XSDataString")
        if self._pdbFile is not None:
            self.pdbFile.export(outfile, level, name_='pdbFile')
        else:
            warnEmptyAttribute("pdbFile", "XSDataFile")
        if self._fitFile is not None:
            self.fitFile.export(outfile, level, name_='fitFile')
        if self._firFile is not None:
            self.firFile.export(outfile, level, name_='firFile')
        if self._logFile is not None:
            self.logFile.export(outfile, level, name_='logFile')
        if self._rfactor is not None:
            self.rfactor.export(outfile, level, name_='rfactor')
        if self._chiSqrt is not None:
            self.chiSqrt.export(outfile, level, name_='chiSqrt')
        if self._volume is not None:
            self.volume.export(outfile, level, name_='volume')
        if self._rg is not None:
            self.rg.export(outfile, level, name_='rg')
        if self._dmax is not None:
            self.dmax.export(outfile, level, name_='dmax')
    def build(self, node_):
        for child_ in node_.childNodes:
            nodeName_ = child_.nodeName.split(':')[-1]
            self.buildChildren(child_, nodeName_)
    def buildChildren(self, child_, nodeName_):
        if child_.nodeType == Node.ELEMENT_NODE and \
            nodeName_ == 'name':
            obj_ = XSDataString()
            obj_.build(child_)
            self.setName(obj_)
        elif child_.nodeType == Node.ELEMENT_NODE and \
            nodeName_ == 'pdbFile':
            obj_ = XSDataFile()
            obj_.build(child_)
            self.setPdbFile(obj_)
        elif child_.nodeType == Node.ELEMENT_NODE and \
            nodeName_ == 'fitFile':
            obj_ = XSDataFile()
            obj_.build(child_)
            self.setFitFile(obj_)
        elif child_.nodeType == Node.ELEMENT_NODE and \
            nodeName_ == 'firFile':
            obj_ = XSDataFile()
            obj_.build(child_)
            self.setFirFile(obj_)
        elif child_.nodeType == Node.ELEMENT_NODE and \
            nodeName_ == 'logFile':
            obj_ = XSDataFile()
            obj_.build(child_)
            self.setLogFile(obj_)
        elif child_.nodeType == Node.ELEMENT_NODE and \
            nodeName_ == 'rfactor':
            obj_ = XSDataDouble()
            obj_.build(child_)
            self.setRfactor(obj_)
        elif child_.nodeType == Node.ELEMENT_NODE and \
            nodeName_ == 'chiSqrt':
            obj_ = XSDataDouble()
            obj_.build(child_)
            self.setChiSqrt(obj_)
        elif child_.nodeType == Node.ELEMENT_NODE and \
            nodeName_ == 'volume':
            obj_ = XSDataDouble()
            obj_.build(child_)
            self.setVolume(obj_)
        elif child_.nodeType == Node.ELEMENT_NODE and \
            nodeName_ == 'rg':
            obj_ = XSDataDouble()
            obj_.build(child_)
            self.setRg(obj_)
        elif child_.nodeType == Node.ELEMENT_NODE and \
            nodeName_ == 'dmax':
            obj_ = XSDataDouble()
            obj_.build(child_)
            self.setDmax(obj_)
        XSData.buildChildren(self, child_, nodeName_)
    #Method for marshalling an object
    def marshal( self ):
        oStreamString = StringIO()
        oStreamString.write(unicode('<?xml version="1.0" ?>\n'))
        self.export( oStreamString, 0, name_="XSDataSaxsModel" )
        oStringXML = oStreamString.getvalue()
        oStreamString.close()
        return oStringXML
    #Only to export the entire XML tree to a file stream on disk
    def exportToFile( self, _outfileName ):
        outfile = open( _outfileName, "w" )
        outfile.write(unicode('<?xml version=\"1.0\" ?>\n'))
        self.export( outfile, 0, name_='XSDataSaxsModel' )
        outfile.close()
    #Deprecated method, replaced by exportToFile
    def outputFile( self, _outfileName ):
        print("WARNING: Method outputFile in class XSDataSaxsModel is deprecated, please use instead exportToFile!")
        self.exportToFile(_outfileName)
    #Method for making a copy in a new instance
    def copy( self ):
        return XSDataSaxsModel.parseString(self.marshal())
    #Static method for parsing a string
    def parseString( _inString ):
        doc = minidom.parseString(_inString)
        rootNode = doc.documentElement
        rootObj = XSDataSaxsModel()
        rootObj.build(rootNode)
        # Check that all minOccurs are obeyed by marshalling the created object
        oStreamString = StringIO()
        rootObj.export( oStreamString, 0, name_="XSDataSaxsModel" )
        oStreamString.close()
        return rootObj
    parseString = staticmethod( parseString )
    #Static method for parsing a file
    def parseFile( _inFilePath ):
        doc = minidom.parse(_inFilePath)
        rootNode = doc.documentElement
        rootObj = XSDataSaxsModel()
        rootObj.build(rootNode)
        return rootObj
    parseFile = staticmethod( parseFile )
# end class XSDataSaxsModel


class XSDataSaxsSample(XSData):
    """Everything describing the sample"""
    def __init__(self, code=None, comment=None, name=None):
        XSData.__init__(self, )
        if name is None:
            self._name = None
        elif name.__class__.__name__ == "XSDataString":
            self._name = name
        else:
            strMessage = "ERROR! XSDataSaxsSample constructor argument 'name' is not XSDataString but %s" % self._name.__class__.__name__
            raise BaseException(strMessage)
        if comment is None:
            self._comment = None
        elif comment.__class__.__name__ == "XSDataString":
            self._comment = comment
        else:
            strMessage = "ERROR! XSDataSaxsSample constructor argument 'comment' is not XSDataString but %s" % self._comment.__class__.__name__
            raise BaseException(strMessage)
        if code is None:
            self._code = None
        elif code.__class__.__name__ == "XSDataString":
            self._code = code
        else:
            strMessage = "ERROR! XSDataSaxsSample constructor argument 'code' is not XSDataString but %s" % self._code.__class__.__name__
            raise BaseException(strMessage)
    # Methods and properties for the 'name' attribute
    def getName(self): return self._name
    def setName(self, name):
        if name is None:
            self._name = None
        elif name.__class__.__name__ == "XSDataString":
            self._name = name
        else:
            strMessage = "ERROR! XSDataSaxsSample.setName argument is not XSDataString but %s" % name.__class__.__name__
            raise BaseException(strMessage)
    def delName(self): self._name = None
    name = property(getName, setName, delName, "Property for name")
    # Methods and properties for the 'comment' attribute
    def getComment(self): return self._comment
    def setComment(self, comment):
        if comment is None:
            self._comment = None
        elif comment.__class__.__name__ == "XSDataString":
            self._comment = comment
        else:
            strMessage = "ERROR! XSDataSaxsSample.setComment argument is not XSDataString but %s" % comment.__class__.__name__
            raise BaseException(strMessage)
    def delComment(self): self._comment = None
    comment = property(getComment, setComment, delComment, "Property for comment")
    # Methods and properties for the 'code' attribute
    def getCode(self): return self._code
    def setCode(self, code):
        if code is None:
            self._code = None
        elif code.__class__.__name__ == "XSDataString":
            self._code = code
        else:
            strMessage = "ERROR! XSDataSaxsSample.setCode argument is not XSDataString but %s" % code.__class__.__name__
            raise BaseException(strMessage)
    def delCode(self): self._code = None
    code = property(getCode, setCode, delCode, "Property for code")
    def export(self, outfile, level, name_='XSDataSaxsSample'):
        showIndent(outfile, level)
        outfile.write(unicode('<%s>\n' % name_))
        self.exportChildren(outfile, level + 1, name_)
        showIndent(outfile, level)
        outfile.write(unicode('</%s>\n' % name_))
    def exportChildren(self, outfile, level, name_='XSDataSaxsSample'):
        XSData.exportChildren(self, outfile, level, name_)
        if self._name is not None:
            self.name.export(outfile, level, name_='name')
        if self._comment is not None:
            self.comment.export(outfile, level, name_='comment')
        if self._code is not None:
            self.code.export(outfile, level, name_='code')
    def build(self, node_):
        for child_ in node_.childNodes:
            nodeName_ = child_.nodeName.split(':')[-1]
            self.buildChildren(child_, nodeName_)
    def buildChildren(self, child_, nodeName_):
        if child_.nodeType == Node.ELEMENT_NODE and \
            nodeName_ == 'name':
            obj_ = XSDataString()
            obj_.build(child_)
            self.setName(obj_)
        elif child_.nodeType == Node.ELEMENT_NODE and \
            nodeName_ == 'comment':
            obj_ = XSDataString()
            obj_.build(child_)
            self.setComment(obj_)
        elif child_.nodeType == Node.ELEMENT_NODE and \
            nodeName_ == 'code':
            obj_ = XSDataString()
            obj_.build(child_)
            self.setCode(obj_)
        XSData.buildChildren(self, child_, nodeName_)
    #Method for marshalling an object
    def marshal( self ):
        oStreamString = StringIO()
        oStreamString.write(unicode('<?xml version="1.0" ?>\n'))
        self.export( oStreamString, 0, name_="XSDataSaxsSample" )
        oStringXML = oStreamString.getvalue()
        oStreamString.close()
        return oStringXML
    #Only to export the entire XML tree to a file stream on disk
    def exportToFile( self, _outfileName ):
        outfile = open( _outfileName, "w" )
        outfile.write(unicode('<?xml version=\"1.0\" ?>\n'))
        self.export( outfile, 0, name_='XSDataSaxsSample' )
        outfile.close()
    #Deprecated method, replaced by exportToFile
    def outputFile( self, _outfileName ):
        print("WARNING: Method outputFile in class XSDataSaxsSample is deprecated, please use instead exportToFile!")
        self.exportToFile(_outfileName)
    #Method for making a copy in a new instance
    def copy( self ):
        return XSDataSaxsSample.parseString(self.marshal())
    #Static method for parsing a string
    def parseString( _inString ):
        doc = minidom.parseString(_inString)
        rootNode = doc.documentElement
        rootObj = XSDataSaxsSample()
        rootObj.build(rootNode)
        # Check that all minOccurs are obeyed by marshalling the created object
        oStreamString = StringIO()
        rootObj.export( oStreamString, 0, name_="XSDataSaxsSample" )
        oStreamString.close()
        return rootObj
    parseString = staticmethod( parseString )
    #Static method for parsing a file
    def parseFile( _inFilePath ):
        doc = minidom.parse(_inFilePath)
        rootNode = doc.documentElement
        rootObj = XSDataSaxsSample()
        rootObj.build(rootNode)
        return rootObj
    parseFile = staticmethod( parseFile )
# end class XSDataSaxsSample


class XSDataSaxsSeries(XSData):
    """Basical"""
    def __init__(self, concentration=None, curve=None):
        XSData.__init__(self, )
        if curve is None:
            self._curve = None
        elif curve.__class__.__name__ == "XSDataFile":
            self._curve = curve
        else:
            strMessage = "ERROR! XSDataSaxsSeries constructor argument 'curve' is not XSDataFile but %s" % self._curve.__class__.__name__
            raise BaseException(strMessage)
        if concentration is None:
            self._concentration = None
        elif concentration.__class__.__name__ == "XSDataDouble":
            self._concentration = concentration
        else:
            strMessage = "ERROR! XSDataSaxsSeries constructor argument 'concentration' is not XSDataDouble but %s" % self._concentration.__class__.__name__
            raise BaseException(strMessage)
    # Methods and properties for the 'curve' attribute
    def getCurve(self): return self._curve
    def setCurve(self, curve):
        if curve is None:
            self._curve = None
        elif curve.__class__.__name__ == "XSDataFile":
            self._curve = curve
        else:
            strMessage = "ERROR! XSDataSaxsSeries.setCurve argument is not XSDataFile but %s" % curve.__class__.__name__
            raise BaseException(strMessage)
    def delCurve(self): self._curve = None
    curve = property(getCurve, setCurve, delCurve, "Property for curve")
    # Methods and properties for the 'concentration' attribute
    def getConcentration(self): return self._concentration
    def setConcentration(self, concentration):
        if concentration is None:
            self._concentration = None
        elif concentration.__class__.__name__ == "XSDataDouble":
            self._concentration = concentration
        else:
            strMessage = "ERROR! XSDataSaxsSeries.setConcentration argument is not XSDataDouble but %s" % concentration.__class__.__name__
            raise BaseException(strMessage)
    def delConcentration(self): self._concentration = None
    concentration = property(getConcentration, setConcentration, delConcentration, "Property for concentration")
    def export(self, outfile, level, name_='XSDataSaxsSeries'):
        showIndent(outfile, level)
        outfile.write(unicode('<%s>\n' % name_))
        self.exportChildren(outfile, level + 1, name_)
        showIndent(outfile, level)
        outfile.write(unicode('</%s>\n' % name_))
    def exportChildren(self, outfile, level, name_='XSDataSaxsSeries'):
        XSData.exportChildren(self, outfile, level, name_)
        if self._curve is not None:
            self.curve.export(outfile, level, name_='curve')
        else:
            warnEmptyAttribute("curve", "XSDataFile")
        if self._concentration is not None:
            self.concentration.export(outfile, level, name_='concentration')
    def build(self, node_):
        for child_ in node_.childNodes:
            nodeName_ = child_.nodeName.split(':')[-1]
            self.buildChildren(child_, nodeName_)
    def buildChildren(self, child_, nodeName_):
        if child_.nodeType == Node.ELEMENT_NODE and \
            nodeName_ == 'curve':
            obj_ = XSDataFile()
            obj_.build(child_)
            self.setCurve(obj_)
        elif child_.nodeType == Node.ELEMENT_NODE and \
            nodeName_ == 'concentration':
            obj_ = XSDataDouble()
            obj_.build(child_)
            self.setConcentration(obj_)
        XSData.buildChildren(self, child_, nodeName_)
    #Method for marshalling an object
    def marshal( self ):
        oStreamString = StringIO()
        oStreamString.write(unicode('<?xml version="1.0" ?>\n'))
        self.export( oStreamString, 0, name_="XSDataSaxsSeries" )
        oStringXML = oStreamString.getvalue()
        oStreamString.close()
        return oStringXML
    #Only to export the entire XML tree to a file stream on disk
    def exportToFile( self, _outfileName ):
        outfile = open( _outfileName, "w" )
        outfile.write(unicode('<?xml version=\"1.0\" ?>\n'))
        self.export( outfile, 0, name_='XSDataSaxsSeries' )
        outfile.close()
    #Deprecated method, replaced by exportToFile
    def outputFile( self, _outfileName ):
        print("WARNING: Method outputFile in class XSDataSaxsSeries is deprecated, please use instead exportToFile!")
        self.exportToFile(_outfileName)
    #Method for making a copy in a new instance
    def copy( self ):
        return XSDataSaxsSeries.parseString(self.marshal())
    #Static method for parsing a string
    def parseString( _inString ):
        doc = minidom.parseString(_inString)
        rootNode = doc.documentElement
        rootObj = XSDataSaxsSeries()
        rootObj.build(rootNode)
        # Check that all minOccurs are obeyed by marshalling the created object
        oStreamString = StringIO()
        rootObj.export( oStreamString, 0, name_="XSDataSaxsSeries" )
        oStreamString.close()
        return rootObj
    parseString = staticmethod( parseString )
    #Static method for parsing a file
    def parseFile( _inFilePath ):
        doc = minidom.parse(_inFilePath)
        rootNode = doc.documentElement
        rootObj = XSDataSaxsSeries()
        rootObj.build(rootNode)
        return rootObj
    parseFile = staticmethod( parseFile )
# end class XSDataSaxsSeries


class XSDataInputAutoRg(XSDataInput):
    def __init__(self, configuration=None, maxSminRg=None, maxSmaxRg=None, minIntervalLength=None, inputCurve=None, sample=None):
        XSDataInput.__init__(self, configuration)
        if sample is None:
            self._sample = None
        elif sample.__class__.__name__ == "XSDataSaxsSample":
            self._sample = sample
        else:
            strMessage = "ERROR! XSDataInputAutoRg constructor argument 'sample' is not XSDataSaxsSample but %s" % self._sample.__class__.__name__
            raise BaseException(strMessage)
        if inputCurve is None:
            self._inputCurve = []
        elif inputCurve.__class__.__name__ == "list":
            self._inputCurve = inputCurve
        else:
            strMessage = "ERROR! XSDataInputAutoRg constructor argument 'inputCurve' is not list but %s" % self._inputCurve.__class__.__name__
            raise BaseException(strMessage)
        if minIntervalLength is None:
            self._minIntervalLength = None
        elif minIntervalLength.__class__.__name__ == "XSDataInteger":
            self._minIntervalLength = minIntervalLength
        else:
            strMessage = "ERROR! XSDataInputAutoRg constructor argument 'minIntervalLength' is not XSDataInteger but %s" % self._minIntervalLength.__class__.__name__
            raise BaseException(strMessage)
        if maxSmaxRg is None:
            self._maxSmaxRg = None
        elif maxSmaxRg.__class__.__name__ == "XSDataDouble":
            self._maxSmaxRg = maxSmaxRg
        else:
            strMessage = "ERROR! XSDataInputAutoRg constructor argument 'maxSmaxRg' is not XSDataDouble but %s" % self._maxSmaxRg.__class__.__name__
            raise BaseException(strMessage)
        if maxSminRg is None:
            self._maxSminRg = None
        elif maxSminRg.__class__.__name__ == "XSDataDouble":
            self._maxSminRg = maxSminRg
        else:
            strMessage = "ERROR! XSDataInputAutoRg constructor argument 'maxSminRg' is not XSDataDouble but %s" % self._maxSminRg.__class__.__name__
            raise BaseException(strMessage)
    # Methods and properties for the 'sample' attribute
    def getSample(self): return self._sample
    def setSample(self, sample):
        if sample is None:
            self._sample = None
        elif sample.__class__.__name__ == "XSDataSaxsSample":
            self._sample = sample
        else:
            strMessage = "ERROR! XSDataInputAutoRg.setSample argument is not XSDataSaxsSample but %s" % sample.__class__.__name__
            raise BaseException(strMessage)
    def delSample(self): self._sample = None
    sample = property(getSample, setSample, delSample, "Property for sample")
    # Methods and properties for the 'inputCurve' attribute
    def getInputCurve(self): return self._inputCurve
    def setInputCurve(self, inputCurve):
        if inputCurve is None:
            self._inputCurve = []
        elif inputCurve.__class__.__name__ == "list":
            self._inputCurve = inputCurve
        else:
            strMessage = "ERROR! XSDataInputAutoRg.setInputCurve argument is not list but %s" % inputCurve.__class__.__name__
            raise BaseException(strMessage)
    def delInputCurve(self): self._inputCurve = None
    inputCurve = property(getInputCurve, setInputCurve, delInputCurve, "Property for inputCurve")
    def addInputCurve(self, value):
        if value is None:
            strMessage = "ERROR! XSDataInputAutoRg.addInputCurve argument is None"
            raise BaseException(strMessage)            
        elif value.__class__.__name__ == "XSDataFile":
            self._inputCurve.append(value)
        else:
            strMessage = "ERROR! XSDataInputAutoRg.addInputCurve argument is not XSDataFile but %s" % value.__class__.__name__
            raise BaseException(strMessage)
    def insertInputCurve(self, index, value):
        if index is None:
            strMessage = "ERROR! XSDataInputAutoRg.insertInputCurve argument 'index' is None"
            raise BaseException(strMessage)            
        if value is None:
            strMessage = "ERROR! XSDataInputAutoRg.insertInputCurve argument 'value' is None"
            raise BaseException(strMessage)            
        elif value.__class__.__name__ == "XSDataFile":
            self._inputCurve[index] = value
        else:
            strMessage = "ERROR! XSDataInputAutoRg.addInputCurve argument is not XSDataFile but %s" % value.__class__.__name__
            raise BaseException(strMessage)
    # Methods and properties for the 'minIntervalLength' attribute
    def getMinIntervalLength(self): return self._minIntervalLength
    def setMinIntervalLength(self, minIntervalLength):
        if minIntervalLength is None:
            self._minIntervalLength = None
        elif minIntervalLength.__class__.__name__ == "XSDataInteger":
            self._minIntervalLength = minIntervalLength
        else:
            strMessage = "ERROR! XSDataInputAutoRg.setMinIntervalLength argument is not XSDataInteger but %s" % minIntervalLength.__class__.__name__
            raise BaseException(strMessage)
    def delMinIntervalLength(self): self._minIntervalLength = None
    minIntervalLength = property(getMinIntervalLength, setMinIntervalLength, delMinIntervalLength, "Property for minIntervalLength")
    # Methods and properties for the 'maxSmaxRg' attribute
    def getMaxSmaxRg(self): return self._maxSmaxRg
    def setMaxSmaxRg(self, maxSmaxRg):
        if maxSmaxRg is None:
            self._maxSmaxRg = None
        elif maxSmaxRg.__class__.__name__ == "XSDataDouble":
            self._maxSmaxRg = maxSmaxRg
        else:
            strMessage = "ERROR! XSDataInputAutoRg.setMaxSmaxRg argument is not XSDataDouble but %s" % maxSmaxRg.__class__.__name__
            raise BaseException(strMessage)
    def delMaxSmaxRg(self): self._maxSmaxRg = None
    maxSmaxRg = property(getMaxSmaxRg, setMaxSmaxRg, delMaxSmaxRg, "Property for maxSmaxRg")
    # Methods and properties for the 'maxSminRg' attribute
    def getMaxSminRg(self): return self._maxSminRg
    def setMaxSminRg(self, maxSminRg):
        if maxSminRg is None:
            self._maxSminRg = None
        elif maxSminRg.__class__.__name__ == "XSDataDouble":
            self._maxSminRg = maxSminRg
        else:
            strMessage = "ERROR! XSDataInputAutoRg.setMaxSminRg argument is not XSDataDouble but %s" % maxSminRg.__class__.__name__
            raise BaseException(strMessage)
    def delMaxSminRg(self): self._maxSminRg = None
    maxSminRg = property(getMaxSminRg, setMaxSminRg, delMaxSminRg, "Property for maxSminRg")
    def export(self, outfile, level, name_='XSDataInputAutoRg'):
        showIndent(outfile, level)
        outfile.write(unicode('<%s>\n' % name_))
        self.exportChildren(outfile, level + 1, name_)
        showIndent(outfile, level)
        outfile.write(unicode('</%s>\n' % name_))
    def exportChildren(self, outfile, level, name_='XSDataInputAutoRg'):
        XSDataInput.exportChildren(self, outfile, level, name_)
        if self._sample is not None:
            self.sample.export(outfile, level, name_='sample')
        for inputCurve_ in self.getInputCurve():
            inputCurve_.export(outfile, level, name_='inputCurve')
        if self.getInputCurve() == []:
            warnEmptyAttribute("inputCurve", "XSDataFile")
        if self._minIntervalLength is not None:
            self.minIntervalLength.export(outfile, level, name_='minIntervalLength')
        if self._maxSmaxRg is not None:
            self.maxSmaxRg.export(outfile, level, name_='maxSmaxRg')
        if self._maxSminRg is not None:
            self.maxSminRg.export(outfile, level, name_='maxSminRg')
    def build(self, node_):
        for child_ in node_.childNodes:
            nodeName_ = child_.nodeName.split(':')[-1]
            self.buildChildren(child_, nodeName_)
    def buildChildren(self, child_, nodeName_):
        if child_.nodeType == Node.ELEMENT_NODE and \
            nodeName_ == 'sample':
            obj_ = XSDataSaxsSample()
            obj_.build(child_)
            self.setSample(obj_)
        elif child_.nodeType == Node.ELEMENT_NODE and \
            nodeName_ == 'inputCurve':
            obj_ = XSDataFile()
            obj_.build(child_)
            self.inputCurve.append(obj_)
        elif child_.nodeType == Node.ELEMENT_NODE and \
            nodeName_ == 'minIntervalLength':
            obj_ = XSDataInteger()
            obj_.build(child_)
            self.setMinIntervalLength(obj_)
        elif child_.nodeType == Node.ELEMENT_NODE and \
            nodeName_ == 'maxSmaxRg':
            obj_ = XSDataDouble()
            obj_.build(child_)
            self.setMaxSmaxRg(obj_)
        elif child_.nodeType == Node.ELEMENT_NODE and \
            nodeName_ == 'maxSminRg':
            obj_ = XSDataDouble()
            obj_.build(child_)
            self.setMaxSminRg(obj_)
        XSDataInput.buildChildren(self, child_, nodeName_)
    #Method for marshalling an object
    def marshal( self ):
        oStreamString = StringIO()
        oStreamString.write(unicode('<?xml version="1.0" ?>\n'))
        self.export( oStreamString, 0, name_="XSDataInputAutoRg" )
        oStringXML = oStreamString.getvalue()
        oStreamString.close()
        return oStringXML
    #Only to export the entire XML tree to a file stream on disk
    def exportToFile( self, _outfileName ):
        outfile = open( _outfileName, "w" )
        outfile.write(unicode('<?xml version=\"1.0\" ?>\n'))
        self.export( outfile, 0, name_='XSDataInputAutoRg' )
        outfile.close()
    #Deprecated method, replaced by exportToFile
    def outputFile( self, _outfileName ):
        print("WARNING: Method outputFile in class XSDataInputAutoRg is deprecated, please use instead exportToFile!")
        self.exportToFile(_outfileName)
    #Method for making a copy in a new instance
    def copy( self ):
        return XSDataInputAutoRg.parseString(self.marshal())
    #Static method for parsing a string
    def parseString( _inString ):
        doc = minidom.parseString(_inString)
        rootNode = doc.documentElement
        rootObj = XSDataInputAutoRg()
        rootObj.build(rootNode)
        # Check that all minOccurs are obeyed by marshalling the created object
        oStreamString = StringIO()
        rootObj.export( oStreamString, 0, name_="XSDataInputAutoRg" )
        oStreamString.close()
        return rootObj
    parseString = staticmethod( parseString )
    #Static method for parsing a file
    def parseFile( _inFilePath ):
        doc = minidom.parse(_inFilePath)
        rootNode = doc.documentElement
        rootObj = XSDataInputAutoRg()
        rootObj.build(rootNode)
        return rootObj
    parseFile = staticmethod( parseFile )
# end class XSDataInputAutoRg


class XSDataInputAutoSub(XSDataInput):
    """Autosub works by default in sampleCurve directory """
    def __init__(self, configuration=None, subtractedCurve=None, sampleCurve=None, buffers=None):
        XSDataInput.__init__(self, configuration)
        if buffers is None:
            self._buffers = []
        elif buffers.__class__.__name__ == "list":
            self._buffers = buffers
        else:
            strMessage = "ERROR! XSDataInputAutoSub constructor argument 'buffers' is not list but %s" % self._buffers.__class__.__name__
            raise BaseException(strMessage)
        if sampleCurve is None:
            self._sampleCurve = None
        elif sampleCurve.__class__.__name__ == "XSDataFile":
            self._sampleCurve = sampleCurve
        else:
            strMessage = "ERROR! XSDataInputAutoSub constructor argument 'sampleCurve' is not XSDataFile but %s" % self._sampleCurve.__class__.__name__
            raise BaseException(strMessage)
        if subtractedCurve is None:
            self._subtractedCurve = None
        elif subtractedCurve.__class__.__name__ == "XSDataFile":
            self._subtractedCurve = subtractedCurve
        else:
            strMessage = "ERROR! XSDataInputAutoSub constructor argument 'subtractedCurve' is not XSDataFile but %s" % self._subtractedCurve.__class__.__name__
            raise BaseException(strMessage)
    # Methods and properties for the 'buffers' attribute
    def getBuffers(self): return self._buffers
    def setBuffers(self, buffers):
        if buffers is None:
            self._buffers = []
        elif buffers.__class__.__name__ == "list":
            self._buffers = buffers
        else:
            strMessage = "ERROR! XSDataInputAutoSub.setBuffers argument is not list but %s" % buffers.__class__.__name__
            raise BaseException(strMessage)
    def delBuffers(self): self._buffers = None
    buffers = property(getBuffers, setBuffers, delBuffers, "Property for buffers")
    def addBuffers(self, value):
        if value is None:
            strMessage = "ERROR! XSDataInputAutoSub.addBuffers argument is None"
            raise BaseException(strMessage)            
        elif value.__class__.__name__ == "XSDataFile":
            self._buffers.append(value)
        else:
            strMessage = "ERROR! XSDataInputAutoSub.addBuffers argument is not XSDataFile but %s" % value.__class__.__name__
            raise BaseException(strMessage)
    def insertBuffers(self, index, value):
        if index is None:
            strMessage = "ERROR! XSDataInputAutoSub.insertBuffers argument 'index' is None"
            raise BaseException(strMessage)            
        if value is None:
            strMessage = "ERROR! XSDataInputAutoSub.insertBuffers argument 'value' is None"
            raise BaseException(strMessage)            
        elif value.__class__.__name__ == "XSDataFile":
            self._buffers[index] = value
        else:
            strMessage = "ERROR! XSDataInputAutoSub.addBuffers argument is not XSDataFile but %s" % value.__class__.__name__
            raise BaseException(strMessage)
    # Methods and properties for the 'sampleCurve' attribute
    def getSampleCurve(self): return self._sampleCurve
    def setSampleCurve(self, sampleCurve):
        if sampleCurve is None:
            self._sampleCurve = None
        elif sampleCurve.__class__.__name__ == "XSDataFile":
            self._sampleCurve = sampleCurve
        else:
            strMessage = "ERROR! XSDataInputAutoSub.setSampleCurve argument is not XSDataFile but %s" % sampleCurve.__class__.__name__
            raise BaseException(strMessage)
    def delSampleCurve(self): self._sampleCurve = None
    sampleCurve = property(getSampleCurve, setSampleCurve, delSampleCurve, "Property for sampleCurve")
    # Methods and properties for the 'subtractedCurve' attribute
    def getSubtractedCurve(self): return self._subtractedCurve
    def setSubtractedCurve(self, subtractedCurve):
        if subtractedCurve is None:
            self._subtractedCurve = None
        elif subtractedCurve.__class__.__name__ == "XSDataFile":
            self._subtractedCurve = subtractedCurve
        else:
            strMessage = "ERROR! XSDataInputAutoSub.setSubtractedCurve argument is not XSDataFile but %s" % subtractedCurve.__class__.__name__
            raise BaseException(strMessage)
    def delSubtractedCurve(self): self._subtractedCurve = None
    subtractedCurve = property(getSubtractedCurve, setSubtractedCurve, delSubtractedCurve, "Property for subtractedCurve")
    def export(self, outfile, level, name_='XSDataInputAutoSub'):
        showIndent(outfile, level)
        outfile.write(unicode('<%s>\n' % name_))
        self.exportChildren(outfile, level + 1, name_)
        showIndent(outfile, level)
        outfile.write(unicode('</%s>\n' % name_))
    def exportChildren(self, outfile, level, name_='XSDataInputAutoSub'):
        XSDataInput.exportChildren(self, outfile, level, name_)
        for buffers_ in self.getBuffers():
            buffers_.export(outfile, level, name_='buffers')
        if self.getBuffers() == []:
            warnEmptyAttribute("buffers", "XSDataFile")
        if self._sampleCurve is not None:
            self.sampleCurve.export(outfile, level, name_='sampleCurve')
        else:
            warnEmptyAttribute("sampleCurve", "XSDataFile")
        if self._subtractedCurve is not None:
            self.subtractedCurve.export(outfile, level, name_='subtractedCurve')
    def build(self, node_):
        for child_ in node_.childNodes:
            nodeName_ = child_.nodeName.split(':')[-1]
            self.buildChildren(child_, nodeName_)
    def buildChildren(self, child_, nodeName_):
        if child_.nodeType == Node.ELEMENT_NODE and \
            nodeName_ == 'buffers':
            obj_ = XSDataFile()
            obj_.build(child_)
            self.buffers.append(obj_)
        elif child_.nodeType == Node.ELEMENT_NODE and \
            nodeName_ == 'sampleCurve':
            obj_ = XSDataFile()
            obj_.build(child_)
            self.setSampleCurve(obj_)
        elif child_.nodeType == Node.ELEMENT_NODE and \
            nodeName_ == 'subtractedCurve':
            obj_ = XSDataFile()
            obj_.build(child_)
            self.setSubtractedCurve(obj_)
        XSDataInput.buildChildren(self, child_, nodeName_)
    #Method for marshalling an object
    def marshal( self ):
        oStreamString = StringIO()
        oStreamString.write(unicode('<?xml version="1.0" ?>\n'))
        self.export( oStreamString, 0, name_="XSDataInputAutoSub" )
        oStringXML = oStreamString.getvalue()
        oStreamString.close()
        return oStringXML
    #Only to export the entire XML tree to a file stream on disk
    def exportToFile( self, _outfileName ):
        outfile = open( _outfileName, "w" )
        outfile.write(unicode('<?xml version=\"1.0\" ?>\n'))
        self.export( outfile, 0, name_='XSDataInputAutoSub' )
        outfile.close()
    #Deprecated method, replaced by exportToFile
    def outputFile( self, _outfileName ):
        print("WARNING: Method outputFile in class XSDataInputAutoSub is deprecated, please use instead exportToFile!")
        self.exportToFile(_outfileName)
    #Method for making a copy in a new instance
    def copy( self ):
        return XSDataInputAutoSub.parseString(self.marshal())
    #Static method for parsing a string
    def parseString( _inString ):
        doc = minidom.parseString(_inString)
        rootNode = doc.documentElement
        rootObj = XSDataInputAutoSub()
        rootObj.build(rootNode)
        # Check that all minOccurs are obeyed by marshalling the created object
        oStreamString = StringIO()
        rootObj.export( oStreamString, 0, name_="XSDataInputAutoSub" )
        oStreamString.close()
        return rootObj
    parseString = staticmethod( parseString )
    #Static method for parsing a file
    def parseFile( _inFilePath ):
        doc = minidom.parse(_inFilePath)
        rootNode = doc.documentElement
        rootObj = XSDataInputAutoSub()
        rootObj.build(rootNode)
        return rootObj
    parseFile = staticmethod( parseFile )
# end class XSDataInputAutoSub


class XSDataInputDamaver(XSDataInput):
    def __init__(self, configuration=None, automatic=None, symmetry=None, pdbInputFiles=None):
        XSDataInput.__init__(self, configuration)
        if pdbInputFiles is None:
            self._pdbInputFiles = []
        elif pdbInputFiles.__class__.__name__ == "list":
            self._pdbInputFiles = pdbInputFiles
        else:
            strMessage = "ERROR! XSDataInputDamaver constructor argument 'pdbInputFiles' is not list but %s" % self._pdbInputFiles.__class__.__name__
            raise BaseException(strMessage)
        if symmetry is None:
            self._symmetry = None
        elif symmetry.__class__.__name__ == "XSDataString":
            self._symmetry = symmetry
        else:
            strMessage = "ERROR! XSDataInputDamaver constructor argument 'symmetry' is not XSDataString but %s" % self._symmetry.__class__.__name__
            raise BaseException(strMessage)
        if automatic is None:
            self._automatic = None
        elif automatic.__class__.__name__ == "XSDataBoolean":
            self._automatic = automatic
        else:
            strMessage = "ERROR! XSDataInputDamaver constructor argument 'automatic' is not XSDataBoolean but %s" % self._automatic.__class__.__name__
            raise BaseException(strMessage)
    # Methods and properties for the 'pdbInputFiles' attribute
    def getPdbInputFiles(self): return self._pdbInputFiles
    def setPdbInputFiles(self, pdbInputFiles):
        if pdbInputFiles is None:
            self._pdbInputFiles = []
        elif pdbInputFiles.__class__.__name__ == "list":
            self._pdbInputFiles = pdbInputFiles
        else:
            strMessage = "ERROR! XSDataInputDamaver.setPdbInputFiles argument is not list but %s" % pdbInputFiles.__class__.__name__
            raise BaseException(strMessage)
    def delPdbInputFiles(self): self._pdbInputFiles = None
    pdbInputFiles = property(getPdbInputFiles, setPdbInputFiles, delPdbInputFiles, "Property for pdbInputFiles")
    def addPdbInputFiles(self, value):
        if value is None:
            strMessage = "ERROR! XSDataInputDamaver.addPdbInputFiles argument is None"
            raise BaseException(strMessage)            
        elif value.__class__.__name__ == "XSDataFile":
            self._pdbInputFiles.append(value)
        else:
            strMessage = "ERROR! XSDataInputDamaver.addPdbInputFiles argument is not XSDataFile but %s" % value.__class__.__name__
            raise BaseException(strMessage)
    def insertPdbInputFiles(self, index, value):
        if index is None:
            strMessage = "ERROR! XSDataInputDamaver.insertPdbInputFiles argument 'index' is None"
            raise BaseException(strMessage)            
        if value is None:
            strMessage = "ERROR! XSDataInputDamaver.insertPdbInputFiles argument 'value' is None"
            raise BaseException(strMessage)            
        elif value.__class__.__name__ == "XSDataFile":
            self._pdbInputFiles[index] = value
        else:
            strMessage = "ERROR! XSDataInputDamaver.addPdbInputFiles argument is not XSDataFile but %s" % value.__class__.__name__
            raise BaseException(strMessage)
    # Methods and properties for the 'symmetry' attribute
    def getSymmetry(self): return self._symmetry
    def setSymmetry(self, symmetry):
        if symmetry is None:
            self._symmetry = None
        elif symmetry.__class__.__name__ == "XSDataString":
            self._symmetry = symmetry
        else:
            strMessage = "ERROR! XSDataInputDamaver.setSymmetry argument is not XSDataString but %s" % symmetry.__class__.__name__
            raise BaseException(strMessage)
    def delSymmetry(self): self._symmetry = None
    symmetry = property(getSymmetry, setSymmetry, delSymmetry, "Property for symmetry")
    # Methods and properties for the 'automatic' attribute
    def getAutomatic(self): return self._automatic
    def setAutomatic(self, automatic):
        if automatic is None:
            self._automatic = None
        elif automatic.__class__.__name__ == "XSDataBoolean":
            self._automatic = automatic
        else:
            strMessage = "ERROR! XSDataInputDamaver.setAutomatic argument is not XSDataBoolean but %s" % automatic.__class__.__name__
            raise BaseException(strMessage)
    def delAutomatic(self): self._automatic = None
    automatic = property(getAutomatic, setAutomatic, delAutomatic, "Property for automatic")
    def export(self, outfile, level, name_='XSDataInputDamaver'):
        showIndent(outfile, level)
        outfile.write(unicode('<%s>\n' % name_))
        self.exportChildren(outfile, level + 1, name_)
        showIndent(outfile, level)
        outfile.write(unicode('</%s>\n' % name_))
    def exportChildren(self, outfile, level, name_='XSDataInputDamaver'):
        XSDataInput.exportChildren(self, outfile, level, name_)
        for pdbInputFiles_ in self.getPdbInputFiles():
            pdbInputFiles_.export(outfile, level, name_='pdbInputFiles')
        if self.getPdbInputFiles() == []:
            warnEmptyAttribute("pdbInputFiles", "XSDataFile")
        if self._symmetry is not None:
            self.symmetry.export(outfile, level, name_='symmetry')
        if self._automatic is not None:
            self.automatic.export(outfile, level, name_='automatic')
    def build(self, node_):
        for child_ in node_.childNodes:
            nodeName_ = child_.nodeName.split(':')[-1]
            self.buildChildren(child_, nodeName_)
    def buildChildren(self, child_, nodeName_):
        if child_.nodeType == Node.ELEMENT_NODE and \
            nodeName_ == 'pdbInputFiles':
            obj_ = XSDataFile()
            obj_.build(child_)
            self.pdbInputFiles.append(obj_)
        elif child_.nodeType == Node.ELEMENT_NODE and \
            nodeName_ == 'symmetry':
            obj_ = XSDataString()
            obj_.build(child_)
            self.setSymmetry(obj_)
        elif child_.nodeType == Node.ELEMENT_NODE and \
            nodeName_ == 'automatic':
            obj_ = XSDataBoolean()
            obj_.build(child_)
            self.setAutomatic(obj_)
        XSDataInput.buildChildren(self, child_, nodeName_)
    #Method for marshalling an object
    def marshal( self ):
        oStreamString = StringIO()
        oStreamString.write(unicode('<?xml version="1.0" ?>\n'))
        self.export( oStreamString, 0, name_="XSDataInputDamaver" )
        oStringXML = oStreamString.getvalue()
        oStreamString.close()
        return oStringXML
    #Only to export the entire XML tree to a file stream on disk
    def exportToFile( self, _outfileName ):
        outfile = open( _outfileName, "w" )
        outfile.write(unicode('<?xml version=\"1.0\" ?>\n'))
        self.export( outfile, 0, name_='XSDataInputDamaver' )
        outfile.close()
    #Deprecated method, replaced by exportToFile
    def outputFile( self, _outfileName ):
        print("WARNING: Method outputFile in class XSDataInputDamaver is deprecated, please use instead exportToFile!")
        self.exportToFile(_outfileName)
    #Method for making a copy in a new instance
    def copy( self ):
        return XSDataInputDamaver.parseString(self.marshal())
    #Static method for parsing a string
    def parseString( _inString ):
        doc = minidom.parseString(_inString)
        rootNode = doc.documentElement
        rootObj = XSDataInputDamaver()
        rootObj.build(rootNode)
        # Check that all minOccurs are obeyed by marshalling the created object
        oStreamString = StringIO()
        rootObj.export( oStreamString, 0, name_="XSDataInputDamaver" )
        oStreamString.close()
        return rootObj
    parseString = staticmethod( parseString )
    #Static method for parsing a file
    def parseFile( _inFilePath ):
        doc = minidom.parse(_inFilePath)
        rootNode = doc.documentElement
        rootObj = XSDataInputDamaver()
        rootObj.build(rootNode)
        return rootObj
    parseFile = staticmethod( parseFile )
# end class XSDataInputDamaver


class XSDataInputDamfilt(XSDataInput):
    def __init__(self, configuration=None, inputPdbFile=None):
        XSDataInput.__init__(self, configuration)
        if inputPdbFile is None:
            self._inputPdbFile = None
        elif inputPdbFile.__class__.__name__ == "XSDataFile":
            self._inputPdbFile = inputPdbFile
        else:
            strMessage = "ERROR! XSDataInputDamfilt constructor argument 'inputPdbFile' is not XSDataFile but %s" % self._inputPdbFile.__class__.__name__
            raise BaseException(strMessage)
    # Methods and properties for the 'inputPdbFile' attribute
    def getInputPdbFile(self): return self._inputPdbFile
    def setInputPdbFile(self, inputPdbFile):
        if inputPdbFile is None:
            self._inputPdbFile = None
        elif inputPdbFile.__class__.__name__ == "XSDataFile":
            self._inputPdbFile = inputPdbFile
        else:
            strMessage = "ERROR! XSDataInputDamfilt.setInputPdbFile argument is not XSDataFile but %s" % inputPdbFile.__class__.__name__
            raise BaseException(strMessage)
    def delInputPdbFile(self): self._inputPdbFile = None
    inputPdbFile = property(getInputPdbFile, setInputPdbFile, delInputPdbFile, "Property for inputPdbFile")
    def export(self, outfile, level, name_='XSDataInputDamfilt'):
        showIndent(outfile, level)
        outfile.write(unicode('<%s>\n' % name_))
        self.exportChildren(outfile, level + 1, name_)
        showIndent(outfile, level)
        outfile.write(unicode('</%s>\n' % name_))
    def exportChildren(self, outfile, level, name_='XSDataInputDamfilt'):
        XSDataInput.exportChildren(self, outfile, level, name_)
        if self._inputPdbFile is not None:
            self.inputPdbFile.export(outfile, level, name_='inputPdbFile')
        else:
            warnEmptyAttribute("inputPdbFile", "XSDataFile")
    def build(self, node_):
        for child_ in node_.childNodes:
            nodeName_ = child_.nodeName.split(':')[-1]
            self.buildChildren(child_, nodeName_)
    def buildChildren(self, child_, nodeName_):
        if child_.nodeType == Node.ELEMENT_NODE and \
            nodeName_ == 'inputPdbFile':
            obj_ = XSDataFile()
            obj_.build(child_)
            self.setInputPdbFile(obj_)
        XSDataInput.buildChildren(self, child_, nodeName_)
    #Method for marshalling an object
    def marshal( self ):
        oStreamString = StringIO()
        oStreamString.write(unicode('<?xml version="1.0" ?>\n'))
        self.export( oStreamString, 0, name_="XSDataInputDamfilt" )
        oStringXML = oStreamString.getvalue()
        oStreamString.close()
        return oStringXML
    #Only to export the entire XML tree to a file stream on disk
    def exportToFile( self, _outfileName ):
        outfile = open( _outfileName, "w" )
        outfile.write(unicode('<?xml version=\"1.0\" ?>\n'))
        self.export( outfile, 0, name_='XSDataInputDamfilt' )
        outfile.close()
    #Deprecated method, replaced by exportToFile
    def outputFile( self, _outfileName ):
        print("WARNING: Method outputFile in class XSDataInputDamfilt is deprecated, please use instead exportToFile!")
        self.exportToFile(_outfileName)
    #Method for making a copy in a new instance
    def copy( self ):
        return XSDataInputDamfilt.parseString(self.marshal())
    #Static method for parsing a string
    def parseString( _inString ):
        doc = minidom.parseString(_inString)
        rootNode = doc.documentElement
        rootObj = XSDataInputDamfilt()
        rootObj.build(rootNode)
        # Check that all minOccurs are obeyed by marshalling the created object
        oStreamString = StringIO()
        rootObj.export( oStreamString, 0, name_="XSDataInputDamfilt" )
        oStreamString.close()
        return rootObj
    parseString = staticmethod( parseString )
    #Static method for parsing a file
    def parseFile( _inFilePath ):
        doc = minidom.parse(_inFilePath)
        rootNode = doc.documentElement
        rootObj = XSDataInputDamfilt()
        rootObj.build(rootNode)
        return rootObj
    parseFile = staticmethod( parseFile )
# end class XSDataInputDamfilt


class XSDataInputDammif(XSDataInput):
    def __init__(self, configuration=None, order=None, constant=None, chained=None, mode=None, symmetry=None, unit=None, gnomOutputFile=None, expectedParticleShape=None):
        XSDataInput.__init__(self, configuration)
        if expectedParticleShape is None:
            self._expectedParticleShape = None
        elif expectedParticleShape.__class__.__name__ == "XSDataInteger":
            self._expectedParticleShape = expectedParticleShape
        else:
            strMessage = "ERROR! XSDataInputDammif constructor argument 'expectedParticleShape' is not XSDataInteger but %s" % self._expectedParticleShape.__class__.__name__
            raise BaseException(strMessage)
        if gnomOutputFile is None:
            self._gnomOutputFile = None
        elif gnomOutputFile.__class__.__name__ == "XSDataFile":
            self._gnomOutputFile = gnomOutputFile
        else:
            strMessage = "ERROR! XSDataInputDammif constructor argument 'gnomOutputFile' is not XSDataFile but %s" % self._gnomOutputFile.__class__.__name__
            raise BaseException(strMessage)
        if unit is None:
            self._unit = None
        elif unit.__class__.__name__ == "XSDataString":
            self._unit = unit
        else:
            strMessage = "ERROR! XSDataInputDammif constructor argument 'unit' is not XSDataString but %s" % self._unit.__class__.__name__
            raise BaseException(strMessage)
        if symmetry is None:
            self._symmetry = None
        elif symmetry.__class__.__name__ == "XSDataString":
            self._symmetry = symmetry
        else:
            strMessage = "ERROR! XSDataInputDammif constructor argument 'symmetry' is not XSDataString but %s" % self._symmetry.__class__.__name__
            raise BaseException(strMessage)
        if mode is None:
            self._mode = None
        elif mode.__class__.__name__ == "XSDataString":
            self._mode = mode
        else:
            strMessage = "ERROR! XSDataInputDammif constructor argument 'mode' is not XSDataString but %s" % self._mode.__class__.__name__
            raise BaseException(strMessage)
        if chained is None:
            self._chained = None
        elif chained.__class__.__name__ == "XSDataBoolean":
            self._chained = chained
        else:
            strMessage = "ERROR! XSDataInputDammif constructor argument 'chained' is not XSDataBoolean but %s" % self._chained.__class__.__name__
            raise BaseException(strMessage)
        if constant is None:
            self._constant = None
        elif constant.__class__.__name__ == "XSDataDouble":
            self._constant = constant
        else:
            strMessage = "ERROR! XSDataInputDammif constructor argument 'constant' is not XSDataDouble but %s" % self._constant.__class__.__name__
            raise BaseException(strMessage)
        if order is None:
            self._order = None
        elif order.__class__.__name__ == "XSDataInteger":
            self._order = order
        else:
            strMessage = "ERROR! XSDataInputDammif constructor argument 'order' is not XSDataInteger but %s" % self._order.__class__.__name__
            raise BaseException(strMessage)
    # Methods and properties for the 'expectedParticleShape' attribute
    def getExpectedParticleShape(self): return self._expectedParticleShape
    def setExpectedParticleShape(self, expectedParticleShape):
        if expectedParticleShape is None:
            self._expectedParticleShape = None
        elif expectedParticleShape.__class__.__name__ == "XSDataInteger":
            self._expectedParticleShape = expectedParticleShape
        else:
            strMessage = "ERROR! XSDataInputDammif.setExpectedParticleShape argument is not XSDataInteger but %s" % expectedParticleShape.__class__.__name__
            raise BaseException(strMessage)
    def delExpectedParticleShape(self): self._expectedParticleShape = None
    expectedParticleShape = property(getExpectedParticleShape, setExpectedParticleShape, delExpectedParticleShape, "Property for expectedParticleShape")
    # Methods and properties for the 'gnomOutputFile' attribute
    def getGnomOutputFile(self): return self._gnomOutputFile
    def setGnomOutputFile(self, gnomOutputFile):
        if gnomOutputFile is None:
            self._gnomOutputFile = None
        elif gnomOutputFile.__class__.__name__ == "XSDataFile":
            self._gnomOutputFile = gnomOutputFile
        else:
            strMessage = "ERROR! XSDataInputDammif.setGnomOutputFile argument is not XSDataFile but %s" % gnomOutputFile.__class__.__name__
            raise BaseException(strMessage)
    def delGnomOutputFile(self): self._gnomOutputFile = None
    gnomOutputFile = property(getGnomOutputFile, setGnomOutputFile, delGnomOutputFile, "Property for gnomOutputFile")
    # Methods and properties for the 'unit' attribute
    def getUnit(self): return self._unit
    def setUnit(self, unit):
        if unit is None:
            self._unit = None
        elif unit.__class__.__name__ == "XSDataString":
            self._unit = unit
        else:
            strMessage = "ERROR! XSDataInputDammif.setUnit argument is not XSDataString but %s" % unit.__class__.__name__
            raise BaseException(strMessage)
    def delUnit(self): self._unit = None
    unit = property(getUnit, setUnit, delUnit, "Property for unit")
    # Methods and properties for the 'symmetry' attribute
    def getSymmetry(self): return self._symmetry
    def setSymmetry(self, symmetry):
        if symmetry is None:
            self._symmetry = None
        elif symmetry.__class__.__name__ == "XSDataString":
            self._symmetry = symmetry
        else:
            strMessage = "ERROR! XSDataInputDammif.setSymmetry argument is not XSDataString but %s" % symmetry.__class__.__name__
            raise BaseException(strMessage)
    def delSymmetry(self): self._symmetry = None
    symmetry = property(getSymmetry, setSymmetry, delSymmetry, "Property for symmetry")
    # Methods and properties for the 'mode' attribute
    def getMode(self): return self._mode
    def setMode(self, mode):
        if mode is None:
            self._mode = None
        elif mode.__class__.__name__ == "XSDataString":
            self._mode = mode
        else:
            strMessage = "ERROR! XSDataInputDammif.setMode argument is not XSDataString but %s" % mode.__class__.__name__
            raise BaseException(strMessage)
    def delMode(self): self._mode = None
    mode = property(getMode, setMode, delMode, "Property for mode")
    # Methods and properties for the 'chained' attribute
    def getChained(self): return self._chained
    def setChained(self, chained):
        if chained is None:
            self._chained = None
        elif chained.__class__.__name__ == "XSDataBoolean":
            self._chained = chained
        else:
            strMessage = "ERROR! XSDataInputDammif.setChained argument is not XSDataBoolean but %s" % chained.__class__.__name__
            raise BaseException(strMessage)
    def delChained(self): self._chained = None
    chained = property(getChained, setChained, delChained, "Property for chained")
    # Methods and properties for the 'constant' attribute
    def getConstant(self): return self._constant
    def setConstant(self, constant):
        if constant is None:
            self._constant = None
        elif constant.__class__.__name__ == "XSDataDouble":
            self._constant = constant
        else:
            strMessage = "ERROR! XSDataInputDammif.setConstant argument is not XSDataDouble but %s" % constant.__class__.__name__
            raise BaseException(strMessage)
    def delConstant(self): self._constant = None
    constant = property(getConstant, setConstant, delConstant, "Property for constant")
    # Methods and properties for the 'order' attribute
    def getOrder(self): return self._order
    def setOrder(self, order):
        if order is None:
            self._order = None
        elif order.__class__.__name__ == "XSDataInteger":
            self._order = order
        else:
            strMessage = "ERROR! XSDataInputDammif.setOrder argument is not XSDataInteger but %s" % order.__class__.__name__
            raise BaseException(strMessage)
    def delOrder(self): self._order = None
    order = property(getOrder, setOrder, delOrder, "Property for order")
    def export(self, outfile, level, name_='XSDataInputDammif'):
        showIndent(outfile, level)
        outfile.write(unicode('<%s>\n' % name_))
        self.exportChildren(outfile, level + 1, name_)
        showIndent(outfile, level)
        outfile.write(unicode('</%s>\n' % name_))
    def exportChildren(self, outfile, level, name_='XSDataInputDammif'):
        XSDataInput.exportChildren(self, outfile, level, name_)
        if self._expectedParticleShape is not None:
            self.expectedParticleShape.export(outfile, level, name_='expectedParticleShape')
        else:
            warnEmptyAttribute("expectedParticleShape", "XSDataInteger")
        if self._gnomOutputFile is not None:
            self.gnomOutputFile.export(outfile, level, name_='gnomOutputFile')
        else:
            warnEmptyAttribute("gnomOutputFile", "XSDataFile")
        if self._unit is not None:
            self.unit.export(outfile, level, name_='unit')
        if self._symmetry is not None:
            self.symmetry.export(outfile, level, name_='symmetry')
        else:
            warnEmptyAttribute("symmetry", "XSDataString")
        if self._mode is not None:
            self.mode.export(outfile, level, name_='mode')
        if self._chained is not None:
            self.chained.export(outfile, level, name_='chained')
        if self._constant is not None:
            self.constant.export(outfile, level, name_='constant')
        if self._order is not None:
            self.order.export(outfile, level, name_='order')
    def build(self, node_):
        for child_ in node_.childNodes:
            nodeName_ = child_.nodeName.split(':')[-1]
            self.buildChildren(child_, nodeName_)
    def buildChildren(self, child_, nodeName_):
        if child_.nodeType == Node.ELEMENT_NODE and \
            nodeName_ == 'expectedParticleShape':
            obj_ = XSDataInteger()
            obj_.build(child_)
            self.setExpectedParticleShape(obj_)
        elif child_.nodeType == Node.ELEMENT_NODE and \
            nodeName_ == 'gnomOutputFile':
            obj_ = XSDataFile()
            obj_.build(child_)
            self.setGnomOutputFile(obj_)
        elif child_.nodeType == Node.ELEMENT_NODE and \
            nodeName_ == 'unit':
            obj_ = XSDataString()
            obj_.build(child_)
            self.setUnit(obj_)
        elif child_.nodeType == Node.ELEMENT_NODE and \
            nodeName_ == 'symmetry':
            obj_ = XSDataString()
            obj_.build(child_)
            self.setSymmetry(obj_)
        elif child_.nodeType == Node.ELEMENT_NODE and \
            nodeName_ == 'mode':
            obj_ = XSDataString()
            obj_.build(child_)
            self.setMode(obj_)
        elif child_.nodeType == Node.ELEMENT_NODE and \
            nodeName_ == 'chained':
            obj_ = XSDataBoolean()
            obj_.build(child_)
            self.setChained(obj_)
        elif child_.nodeType == Node.ELEMENT_NODE and \
            nodeName_ == 'constant':
            obj_ = XSDataDouble()
            obj_.build(child_)
            self.setConstant(obj_)
        elif child_.nodeType == Node.ELEMENT_NODE and \
            nodeName_ == 'order':
            obj_ = XSDataInteger()
            obj_.build(child_)
            self.setOrder(obj_)
        XSDataInput.buildChildren(self, child_, nodeName_)
    #Method for marshalling an object
    def marshal( self ):
        oStreamString = StringIO()
        oStreamString.write(unicode('<?xml version="1.0" ?>\n'))
        self.export( oStreamString, 0, name_="XSDataInputDammif" )
        oStringXML = oStreamString.getvalue()
        oStreamString.close()
        return oStringXML
    #Only to export the entire XML tree to a file stream on disk
    def exportToFile( self, _outfileName ):
        outfile = open( _outfileName, "w" )
        outfile.write(unicode('<?xml version=\"1.0\" ?>\n'))
        self.export( outfile, 0, name_='XSDataInputDammif' )
        outfile.close()
    #Deprecated method, replaced by exportToFile
    def outputFile( self, _outfileName ):
        print("WARNING: Method outputFile in class XSDataInputDammif is deprecated, please use instead exportToFile!")
        self.exportToFile(_outfileName)
    #Method for making a copy in a new instance
    def copy( self ):
        return XSDataInputDammif.parseString(self.marshal())
    #Static method for parsing a string
    def parseString( _inString ):
        doc = minidom.parseString(_inString)
        rootNode = doc.documentElement
        rootObj = XSDataInputDammif()
        rootObj.build(rootNode)
        # Check that all minOccurs are obeyed by marshalling the created object
        oStreamString = StringIO()
        rootObj.export( oStreamString, 0, name_="XSDataInputDammif" )
        oStreamString.close()
        return rootObj
    parseString = staticmethod( parseString )
    #Static method for parsing a file
    def parseFile( _inFilePath ):
        doc = minidom.parse(_inFilePath)
        rootNode = doc.documentElement
        rootObj = XSDataInputDammif()
        rootObj.build(rootNode)
        return rootObj
    parseFile = staticmethod( parseFile )
# end class XSDataInputDammif


class XSDataInputDammin(XSDataInput):
    """name is the name to be given to the model"""
    def __init__(self, configuration=None, name=None, unit=None, mode=None, symmetry=None, pdbInputFile=None, initialDummyAtomModel=None, gnomOutputFile=None, expectedParticleShape=None):
        XSDataInput.__init__(self, configuration)
        if expectedParticleShape is None:
            self._expectedParticleShape = None
        elif expectedParticleShape.__class__.__name__ == "XSDataInteger":
            self._expectedParticleShape = expectedParticleShape
        else:
            strMessage = "ERROR! XSDataInputDammin constructor argument 'expectedParticleShape' is not XSDataInteger but %s" % self._expectedParticleShape.__class__.__name__
            raise BaseException(strMessage)
        if gnomOutputFile is None:
            self._gnomOutputFile = None
        elif gnomOutputFile.__class__.__name__ == "XSDataFile":
            self._gnomOutputFile = gnomOutputFile
        else:
            strMessage = "ERROR! XSDataInputDammin constructor argument 'gnomOutputFile' is not XSDataFile but %s" % self._gnomOutputFile.__class__.__name__
            raise BaseException(strMessage)
        if initialDummyAtomModel is None:
            self._initialDummyAtomModel = None
        elif initialDummyAtomModel.__class__.__name__ == "XSDataInteger":
            self._initialDummyAtomModel = initialDummyAtomModel
        else:
            strMessage = "ERROR! XSDataInputDammin constructor argument 'initialDummyAtomModel' is not XSDataInteger but %s" % self._initialDummyAtomModel.__class__.__name__
            raise BaseException(strMessage)
        if pdbInputFile is None:
            self._pdbInputFile = None
        elif pdbInputFile.__class__.__name__ == "XSDataFile":
            self._pdbInputFile = pdbInputFile
        else:
            strMessage = "ERROR! XSDataInputDammin constructor argument 'pdbInputFile' is not XSDataFile but %s" % self._pdbInputFile.__class__.__name__
            raise BaseException(strMessage)
        if symmetry is None:
            self._symmetry = None
        elif symmetry.__class__.__name__ == "XSDataString":
            self._symmetry = symmetry
        else:
            strMessage = "ERROR! XSDataInputDammin constructor argument 'symmetry' is not XSDataString but %s" % self._symmetry.__class__.__name__
            raise BaseException(strMessage)
        if mode is None:
            self._mode = None
        elif mode.__class__.__name__ == "XSDataString":
            self._mode = mode
        else:
            strMessage = "ERROR! XSDataInputDammin constructor argument 'mode' is not XSDataString but %s" % self._mode.__class__.__name__
            raise BaseException(strMessage)
        if unit is None:
            self._unit = None
        elif unit.__class__.__name__ == "XSDataString":
            self._unit = unit
        else:
            strMessage = "ERROR! XSDataInputDammin constructor argument 'unit' is not XSDataString but %s" % self._unit.__class__.__name__
            raise BaseException(strMessage)
        if name is None:
            self._name = None
        elif name.__class__.__name__ == "XSDataString":
            self._name = name
        else:
            strMessage = "ERROR! XSDataInputDammin constructor argument 'name' is not XSDataString but %s" % self._name.__class__.__name__
            raise BaseException(strMessage)
    # Methods and properties for the 'expectedParticleShape' attribute
    def getExpectedParticleShape(self): return self._expectedParticleShape
    def setExpectedParticleShape(self, expectedParticleShape):
        if expectedParticleShape is None:
            self._expectedParticleShape = None
        elif expectedParticleShape.__class__.__name__ == "XSDataInteger":
            self._expectedParticleShape = expectedParticleShape
        else:
            strMessage = "ERROR! XSDataInputDammin.setExpectedParticleShape argument is not XSDataInteger but %s" % expectedParticleShape.__class__.__name__
            raise BaseException(strMessage)
    def delExpectedParticleShape(self): self._expectedParticleShape = None
    expectedParticleShape = property(getExpectedParticleShape, setExpectedParticleShape, delExpectedParticleShape, "Property for expectedParticleShape")
    # Methods and properties for the 'gnomOutputFile' attribute
    def getGnomOutputFile(self): return self._gnomOutputFile
    def setGnomOutputFile(self, gnomOutputFile):
        if gnomOutputFile is None:
            self._gnomOutputFile = None
        elif gnomOutputFile.__class__.__name__ == "XSDataFile":
            self._gnomOutputFile = gnomOutputFile
        else:
            strMessage = "ERROR! XSDataInputDammin.setGnomOutputFile argument is not XSDataFile but %s" % gnomOutputFile.__class__.__name__
            raise BaseException(strMessage)
    def delGnomOutputFile(self): self._gnomOutputFile = None
    gnomOutputFile = property(getGnomOutputFile, setGnomOutputFile, delGnomOutputFile, "Property for gnomOutputFile")
    # Methods and properties for the 'initialDummyAtomModel' attribute
    def getInitialDummyAtomModel(self): return self._initialDummyAtomModel
    def setInitialDummyAtomModel(self, initialDummyAtomModel):
        if initialDummyAtomModel is None:
            self._initialDummyAtomModel = None
        elif initialDummyAtomModel.__class__.__name__ == "XSDataInteger":
            self._initialDummyAtomModel = initialDummyAtomModel
        else:
            strMessage = "ERROR! XSDataInputDammin.setInitialDummyAtomModel argument is not XSDataInteger but %s" % initialDummyAtomModel.__class__.__name__
            raise BaseException(strMessage)
    def delInitialDummyAtomModel(self): self._initialDummyAtomModel = None
    initialDummyAtomModel = property(getInitialDummyAtomModel, setInitialDummyAtomModel, delInitialDummyAtomModel, "Property for initialDummyAtomModel")
    # Methods and properties for the 'pdbInputFile' attribute
    def getPdbInputFile(self): return self._pdbInputFile
    def setPdbInputFile(self, pdbInputFile):
        if pdbInputFile is None:
            self._pdbInputFile = None
        elif pdbInputFile.__class__.__name__ == "XSDataFile":
            self._pdbInputFile = pdbInputFile
        else:
            strMessage = "ERROR! XSDataInputDammin.setPdbInputFile argument is not XSDataFile but %s" % pdbInputFile.__class__.__name__
            raise BaseException(strMessage)
    def delPdbInputFile(self): self._pdbInputFile = None
    pdbInputFile = property(getPdbInputFile, setPdbInputFile, delPdbInputFile, "Property for pdbInputFile")
    # Methods and properties for the 'symmetry' attribute
    def getSymmetry(self): return self._symmetry
    def setSymmetry(self, symmetry):
        if symmetry is None:
            self._symmetry = None
        elif symmetry.__class__.__name__ == "XSDataString":
            self._symmetry = symmetry
        else:
            strMessage = "ERROR! XSDataInputDammin.setSymmetry argument is not XSDataString but %s" % symmetry.__class__.__name__
            raise BaseException(strMessage)
    def delSymmetry(self): self._symmetry = None
    symmetry = property(getSymmetry, setSymmetry, delSymmetry, "Property for symmetry")
    # Methods and properties for the 'mode' attribute
    def getMode(self): return self._mode
    def setMode(self, mode):
        if mode is None:
            self._mode = None
        elif mode.__class__.__name__ == "XSDataString":
            self._mode = mode
        else:
            strMessage = "ERROR! XSDataInputDammin.setMode argument is not XSDataString but %s" % mode.__class__.__name__
            raise BaseException(strMessage)
    def delMode(self): self._mode = None
    mode = property(getMode, setMode, delMode, "Property for mode")
    # Methods and properties for the 'unit' attribute
    def getUnit(self): return self._unit
    def setUnit(self, unit):
        if unit is None:
            self._unit = None
        elif unit.__class__.__name__ == "XSDataString":
            self._unit = unit
        else:
            strMessage = "ERROR! XSDataInputDammin.setUnit argument is not XSDataString but %s" % unit.__class__.__name__
            raise BaseException(strMessage)
    def delUnit(self): self._unit = None
    unit = property(getUnit, setUnit, delUnit, "Property for unit")
    # Methods and properties for the 'name' attribute
    def getName(self): return self._name
    def setName(self, name):
        if name is None:
            self._name = None
        elif name.__class__.__name__ == "XSDataString":
            self._name = name
        else:
            strMessage = "ERROR! XSDataInputDammin.setName argument is not XSDataString but %s" % name.__class__.__name__
            raise BaseException(strMessage)
    def delName(self): self._name = None
    name = property(getName, setName, delName, "Property for name")
    def export(self, outfile, level, name_='XSDataInputDammin'):
        showIndent(outfile, level)
        outfile.write(unicode('<%s>\n' % name_))
        self.exportChildren(outfile, level + 1, name_)
        showIndent(outfile, level)
        outfile.write(unicode('</%s>\n' % name_))
    def exportChildren(self, outfile, level, name_='XSDataInputDammin'):
        XSDataInput.exportChildren(self, outfile, level, name_)
        if self._expectedParticleShape is not None:
            self.expectedParticleShape.export(outfile, level, name_='expectedParticleShape')
        else:
            warnEmptyAttribute("expectedParticleShape", "XSDataInteger")
        if self._gnomOutputFile is not None:
            self.gnomOutputFile.export(outfile, level, name_='gnomOutputFile')
        else:
            warnEmptyAttribute("gnomOutputFile", "XSDataFile")
        if self._initialDummyAtomModel is not None:
            self.initialDummyAtomModel.export(outfile, level, name_='initialDummyAtomModel')
        else:
            warnEmptyAttribute("initialDummyAtomModel", "XSDataInteger")
        if self._pdbInputFile is not None:
            self.pdbInputFile.export(outfile, level, name_='pdbInputFile')
        else:
            warnEmptyAttribute("pdbInputFile", "XSDataFile")
        if self._symmetry is not None:
            self.symmetry.export(outfile, level, name_='symmetry')
        else:
            warnEmptyAttribute("symmetry", "XSDataString")
        if self._mode is not None:
            self.mode.export(outfile, level, name_='mode')
        if self._unit is not None:
            self.unit.export(outfile, level, name_='unit')
        if self._name is not None:
            self.name.export(outfile, level, name_='name')
    def build(self, node_):
        for child_ in node_.childNodes:
            nodeName_ = child_.nodeName.split(':')[-1]
            self.buildChildren(child_, nodeName_)
    def buildChildren(self, child_, nodeName_):
        if child_.nodeType == Node.ELEMENT_NODE and \
            nodeName_ == 'expectedParticleShape':
            obj_ = XSDataInteger()
            obj_.build(child_)
            self.setExpectedParticleShape(obj_)
        elif child_.nodeType == Node.ELEMENT_NODE and \
            nodeName_ == 'gnomOutputFile':
            obj_ = XSDataFile()
            obj_.build(child_)
            self.setGnomOutputFile(obj_)
        elif child_.nodeType == Node.ELEMENT_NODE and \
            nodeName_ == 'initialDummyAtomModel':
            obj_ = XSDataInteger()
            obj_.build(child_)
            self.setInitialDummyAtomModel(obj_)
        elif child_.nodeType == Node.ELEMENT_NODE and \
            nodeName_ == 'pdbInputFile':
            obj_ = XSDataFile()
            obj_.build(child_)
            self.setPdbInputFile(obj_)
        elif child_.nodeType == Node.ELEMENT_NODE and \
            nodeName_ == 'symmetry':
            obj_ = XSDataString()
            obj_.build(child_)
            self.setSymmetry(obj_)
        elif child_.nodeType == Node.ELEMENT_NODE and \
            nodeName_ == 'mode':
            obj_ = XSDataString()
            obj_.build(child_)
            self.setMode(obj_)
        elif child_.nodeType == Node.ELEMENT_NODE and \
            nodeName_ == 'unit':
            obj_ = XSDataString()
            obj_.build(child_)
            self.setUnit(obj_)
        elif child_.nodeType == Node.ELEMENT_NODE and \
            nodeName_ == 'name':
            obj_ = XSDataString()
            obj_.build(child_)
            self.setName(obj_)
        XSDataInput.buildChildren(self, child_, nodeName_)
    #Method for marshalling an object
    def marshal( self ):
        oStreamString = StringIO()
        oStreamString.write(unicode('<?xml version="1.0" ?>\n'))
        self.export( oStreamString, 0, name_="XSDataInputDammin" )
        oStringXML = oStreamString.getvalue()
        oStreamString.close()
        return oStringXML
    #Only to export the entire XML tree to a file stream on disk
    def exportToFile( self, _outfileName ):
        outfile = open( _outfileName, "w" )
        outfile.write(unicode('<?xml version=\"1.0\" ?>\n'))
        self.export( outfile, 0, name_='XSDataInputDammin' )
        outfile.close()
    #Deprecated method, replaced by exportToFile
    def outputFile( self, _outfileName ):
        print("WARNING: Method outputFile in class XSDataInputDammin is deprecated, please use instead exportToFile!")
        self.exportToFile(_outfileName)
    #Method for making a copy in a new instance
    def copy( self ):
        return XSDataInputDammin.parseString(self.marshal())
    #Static method for parsing a string
    def parseString( _inString ):
        doc = minidom.parseString(_inString)
        rootNode = doc.documentElement
        rootObj = XSDataInputDammin()
        rootObj.build(rootNode)
        # Check that all minOccurs are obeyed by marshalling the created object
        oStreamString = StringIO()
        rootObj.export( oStreamString, 0, name_="XSDataInputDammin" )
        oStreamString.close()
        return rootObj
    parseString = staticmethod( parseString )
    #Static method for parsing a file
    def parseFile( _inFilePath ):
        doc = minidom.parse(_inFilePath)
        rootNode = doc.documentElement
        rootObj = XSDataInputDammin()
        rootObj.build(rootNode)
        return rootObj
    parseFile = staticmethod( parseFile )
# end class XSDataInputDammin


class XSDataInputDamstart(XSDataInput):
    def __init__(self, configuration=None, inputPdbFile=None):
        XSDataInput.__init__(self, configuration)
        if inputPdbFile is None:
            self._inputPdbFile = None
        elif inputPdbFile.__class__.__name__ == "XSDataFile":
            self._inputPdbFile = inputPdbFile
        else:
            strMessage = "ERROR! XSDataInputDamstart constructor argument 'inputPdbFile' is not XSDataFile but %s" % self._inputPdbFile.__class__.__name__
            raise BaseException(strMessage)
    # Methods and properties for the 'inputPdbFile' attribute
    def getInputPdbFile(self): return self._inputPdbFile
    def setInputPdbFile(self, inputPdbFile):
        if inputPdbFile is None:
            self._inputPdbFile = None
        elif inputPdbFile.__class__.__name__ == "XSDataFile":
            self._inputPdbFile = inputPdbFile
        else:
            strMessage = "ERROR! XSDataInputDamstart.setInputPdbFile argument is not XSDataFile but %s" % inputPdbFile.__class__.__name__
            raise BaseException(strMessage)
    def delInputPdbFile(self): self._inputPdbFile = None
    inputPdbFile = property(getInputPdbFile, setInputPdbFile, delInputPdbFile, "Property for inputPdbFile")
    def export(self, outfile, level, name_='XSDataInputDamstart'):
        showIndent(outfile, level)
        outfile.write(unicode('<%s>\n' % name_))
        self.exportChildren(outfile, level + 1, name_)
        showIndent(outfile, level)
        outfile.write(unicode('</%s>\n' % name_))
    def exportChildren(self, outfile, level, name_='XSDataInputDamstart'):
        XSDataInput.exportChildren(self, outfile, level, name_)
        if self._inputPdbFile is not None:
            self.inputPdbFile.export(outfile, level, name_='inputPdbFile')
        else:
            warnEmptyAttribute("inputPdbFile", "XSDataFile")
    def build(self, node_):
        for child_ in node_.childNodes:
            nodeName_ = child_.nodeName.split(':')[-1]
            self.buildChildren(child_, nodeName_)
    def buildChildren(self, child_, nodeName_):
        if child_.nodeType == Node.ELEMENT_NODE and \
            nodeName_ == 'inputPdbFile':
            obj_ = XSDataFile()
            obj_.build(child_)
            self.setInputPdbFile(obj_)
        XSDataInput.buildChildren(self, child_, nodeName_)
    #Method for marshalling an object
    def marshal( self ):
        oStreamString = StringIO()
        oStreamString.write(unicode('<?xml version="1.0" ?>\n'))
        self.export( oStreamString, 0, name_="XSDataInputDamstart" )
        oStringXML = oStreamString.getvalue()
        oStreamString.close()
        return oStringXML
    #Only to export the entire XML tree to a file stream on disk
    def exportToFile( self, _outfileName ):
        outfile = open( _outfileName, "w" )
        outfile.write(unicode('<?xml version=\"1.0\" ?>\n'))
        self.export( outfile, 0, name_='XSDataInputDamstart' )
        outfile.close()
    #Deprecated method, replaced by exportToFile
    def outputFile( self, _outfileName ):
        print("WARNING: Method outputFile in class XSDataInputDamstart is deprecated, please use instead exportToFile!")
        self.exportToFile(_outfileName)
    #Method for making a copy in a new instance
    def copy( self ):
        return XSDataInputDamstart.parseString(self.marshal())
    #Static method for parsing a string
    def parseString( _inString ):
        doc = minidom.parseString(_inString)
        rootNode = doc.documentElement
        rootObj = XSDataInputDamstart()
        rootObj.build(rootNode)
        # Check that all minOccurs are obeyed by marshalling the created object
        oStreamString = StringIO()
        rootObj.export( oStreamString, 0, name_="XSDataInputDamstart" )
        oStreamString.close()
        return rootObj
    parseString = staticmethod( parseString )
    #Static method for parsing a file
    def parseFile( _inFilePath ):
        doc = minidom.parse(_inFilePath)
        rootNode = doc.documentElement
        rootObj = XSDataInputDamstart()
        rootObj.build(rootNode)
        return rootObj
    parseFile = staticmethod( parseFile )
# end class XSDataInputDamstart


class XSDataInputDatGnom(XSDataInput):
    """Input file can be in 1/nm or 1/A, result will be in the same unit."""
    def __init__(self, configuration=None, output=None, skip=None, rg=None, inputCurve=None):
        XSDataInput.__init__(self, configuration)
        if inputCurve is None:
            self._inputCurve = None
        elif inputCurve.__class__.__name__ == "XSDataFile":
            self._inputCurve = inputCurve
        else:
            strMessage = "ERROR! XSDataInputDatGnom constructor argument 'inputCurve' is not XSDataFile but %s" % self._inputCurve.__class__.__name__
            raise BaseException(strMessage)
        if rg is None:
            self._rg = None
        elif rg.__class__.__name__ == "XSDataLength":
            self._rg = rg
        else:
            strMessage = "ERROR! XSDataInputDatGnom constructor argument 'rg' is not XSDataLength but %s" % self._rg.__class__.__name__
            raise BaseException(strMessage)
        if skip is None:
            self._skip = None
        elif skip.__class__.__name__ == "XSDataInteger":
            self._skip = skip
        else:
            strMessage = "ERROR! XSDataInputDatGnom constructor argument 'skip' is not XSDataInteger but %s" % self._skip.__class__.__name__
            raise BaseException(strMessage)
        if output is None:
            self._output = None
        elif output.__class__.__name__ == "XSDataFile":
            self._output = output
        else:
            strMessage = "ERROR! XSDataInputDatGnom constructor argument 'output' is not XSDataFile but %s" % self._output.__class__.__name__
            raise BaseException(strMessage)
    # Methods and properties for the 'inputCurve' attribute
    def getInputCurve(self): return self._inputCurve
    def setInputCurve(self, inputCurve):
        if inputCurve is None:
            self._inputCurve = None
        elif inputCurve.__class__.__name__ == "XSDataFile":
            self._inputCurve = inputCurve
        else:
            strMessage = "ERROR! XSDataInputDatGnom.setInputCurve argument is not XSDataFile but %s" % inputCurve.__class__.__name__
            raise BaseException(strMessage)
    def delInputCurve(self): self._inputCurve = None
    inputCurve = property(getInputCurve, setInputCurve, delInputCurve, "Property for inputCurve")
    # Methods and properties for the 'rg' attribute
    def getRg(self): return self._rg
    def setRg(self, rg):
        if rg is None:
            self._rg = None
        elif rg.__class__.__name__ == "XSDataLength":
            self._rg = rg
        else:
            strMessage = "ERROR! XSDataInputDatGnom.setRg argument is not XSDataLength but %s" % rg.__class__.__name__
            raise BaseException(strMessage)
    def delRg(self): self._rg = None
    rg = property(getRg, setRg, delRg, "Property for rg")
    # Methods and properties for the 'skip' attribute
    def getSkip(self): return self._skip
    def setSkip(self, skip):
        if skip is None:
            self._skip = None
        elif skip.__class__.__name__ == "XSDataInteger":
            self._skip = skip
        else:
            strMessage = "ERROR! XSDataInputDatGnom.setSkip argument is not XSDataInteger but %s" % skip.__class__.__name__
            raise BaseException(strMessage)
    def delSkip(self): self._skip = None
    skip = property(getSkip, setSkip, delSkip, "Property for skip")
    # Methods and properties for the 'output' attribute
    def getOutput(self): return self._output
    def setOutput(self, output):
        if output is None:
            self._output = None
        elif output.__class__.__name__ == "XSDataFile":
            self._output = output
        else:
            strMessage = "ERROR! XSDataInputDatGnom.setOutput argument is not XSDataFile but %s" % output.__class__.__name__
            raise BaseException(strMessage)
    def delOutput(self): self._output = None
    output = property(getOutput, setOutput, delOutput, "Property for output")
    def export(self, outfile, level, name_='XSDataInputDatGnom'):
        showIndent(outfile, level)
        outfile.write(unicode('<%s>\n' % name_))
        self.exportChildren(outfile, level + 1, name_)
        showIndent(outfile, level)
        outfile.write(unicode('</%s>\n' % name_))
    def exportChildren(self, outfile, level, name_='XSDataInputDatGnom'):
        XSDataInput.exportChildren(self, outfile, level, name_)
        if self._inputCurve is not None:
            self.inputCurve.export(outfile, level, name_='inputCurve')
        else:
            warnEmptyAttribute("inputCurve", "XSDataFile")
        if self._rg is not None:
            self.rg.export(outfile, level, name_='rg')
        if self._skip is not None:
            self.skip.export(outfile, level, name_='skip')
        if self._output is not None:
            self.output.export(outfile, level, name_='output')
    def build(self, node_):
        for child_ in node_.childNodes:
            nodeName_ = child_.nodeName.split(':')[-1]
            self.buildChildren(child_, nodeName_)
    def buildChildren(self, child_, nodeName_):
        if child_.nodeType == Node.ELEMENT_NODE and \
            nodeName_ == 'inputCurve':
            obj_ = XSDataFile()
            obj_.build(child_)
            self.setInputCurve(obj_)
        elif child_.nodeType == Node.ELEMENT_NODE and \
            nodeName_ == 'rg':
            obj_ = XSDataLength()
            obj_.build(child_)
            self.setRg(obj_)
        elif child_.nodeType == Node.ELEMENT_NODE and \
            nodeName_ == 'skip':
            obj_ = XSDataInteger()
            obj_.build(child_)
            self.setSkip(obj_)
        elif child_.nodeType == Node.ELEMENT_NODE and \
            nodeName_ == 'output':
            obj_ = XSDataFile()
            obj_.build(child_)
            self.setOutput(obj_)
        XSDataInput.buildChildren(self, child_, nodeName_)
    #Method for marshalling an object
    def marshal( self ):
        oStreamString = StringIO()
        oStreamString.write(unicode('<?xml version="1.0" ?>\n'))
        self.export( oStreamString, 0, name_="XSDataInputDatGnom" )
        oStringXML = oStreamString.getvalue()
        oStreamString.close()
        return oStringXML
    #Only to export the entire XML tree to a file stream on disk
    def exportToFile( self, _outfileName ):
        outfile = open( _outfileName, "w" )
        outfile.write(unicode('<?xml version=\"1.0\" ?>\n'))
        self.export( outfile, 0, name_='XSDataInputDatGnom' )
        outfile.close()
    #Deprecated method, replaced by exportToFile
    def outputFile( self, _outfileName ):
        print("WARNING: Method outputFile in class XSDataInputDatGnom is deprecated, please use instead exportToFile!")
        self.exportToFile(_outfileName)
    #Method for making a copy in a new instance
    def copy( self ):
        return XSDataInputDatGnom.parseString(self.marshal())
    #Static method for parsing a string
    def parseString( _inString ):
        doc = minidom.parseString(_inString)
        rootNode = doc.documentElement
        rootObj = XSDataInputDatGnom()
        rootObj.build(rootNode)
        # Check that all minOccurs are obeyed by marshalling the created object
        oStreamString = StringIO()
        rootObj.export( oStreamString, 0, name_="XSDataInputDatGnom" )
        oStreamString.close()
        return rootObj
    parseString = staticmethod( parseString )
    #Static method for parsing a file
    def parseFile( _inFilePath ):
        doc = minidom.parse(_inFilePath)
        rootNode = doc.documentElement
        rootObj = XSDataInputDatGnom()
        rootObj.build(rootNode)
        return rootObj
    parseFile = staticmethod( parseFile )
# end class XSDataInputDatGnom


class XSDataInputDatPorod(XSDataInput):
    """Input file can be in 1/nm or 1/A, result will be in the same unit(^3)."""
    def __init__(self, configuration=None, gnomFile=None):
        XSDataInput.__init__(self, configuration)
        if gnomFile is None:
            self._gnomFile = None
        elif gnomFile.__class__.__name__ == "XSDataFile":
            self._gnomFile = gnomFile
        else:
            strMessage = "ERROR! XSDataInputDatPorod constructor argument 'gnomFile' is not XSDataFile but %s" % self._gnomFile.__class__.__name__
            raise BaseException(strMessage)
    # Methods and properties for the 'gnomFile' attribute
    def getGnomFile(self): return self._gnomFile
    def setGnomFile(self, gnomFile):
        if gnomFile is None:
            self._gnomFile = None
        elif gnomFile.__class__.__name__ == "XSDataFile":
            self._gnomFile = gnomFile
        else:
            strMessage = "ERROR! XSDataInputDatPorod.setGnomFile argument is not XSDataFile but %s" % gnomFile.__class__.__name__
            raise BaseException(strMessage)
    def delGnomFile(self): self._gnomFile = None
    gnomFile = property(getGnomFile, setGnomFile, delGnomFile, "Property for gnomFile")
    def export(self, outfile, level, name_='XSDataInputDatPorod'):
        showIndent(outfile, level)
        outfile.write(unicode('<%s>\n' % name_))
        self.exportChildren(outfile, level + 1, name_)
        showIndent(outfile, level)
        outfile.write(unicode('</%s>\n' % name_))
    def exportChildren(self, outfile, level, name_='XSDataInputDatPorod'):
        XSDataInput.exportChildren(self, outfile, level, name_)
        if self._gnomFile is not None:
            self.gnomFile.export(outfile, level, name_='gnomFile')
    def build(self, node_):
        for child_ in node_.childNodes:
            nodeName_ = child_.nodeName.split(':')[-1]
            self.buildChildren(child_, nodeName_)
    def buildChildren(self, child_, nodeName_):
        if child_.nodeType == Node.ELEMENT_NODE and \
            nodeName_ == 'gnomFile':
            obj_ = XSDataFile()
            obj_.build(child_)
            self.setGnomFile(obj_)
        XSDataInput.buildChildren(self, child_, nodeName_)
    #Method for marshalling an object
    def marshal( self ):
        oStreamString = StringIO()
        oStreamString.write(unicode('<?xml version="1.0" ?>\n'))
        self.export( oStreamString, 0, name_="XSDataInputDatPorod" )
        oStringXML = oStreamString.getvalue()
        oStreamString.close()
        return oStringXML
    #Only to export the entire XML tree to a file stream on disk
    def exportToFile( self, _outfileName ):
        outfile = open( _outfileName, "w" )
        outfile.write(unicode('<?xml version=\"1.0\" ?>\n'))
        self.export( outfile, 0, name_='XSDataInputDatPorod' )
        outfile.close()
    #Deprecated method, replaced by exportToFile
    def outputFile( self, _outfileName ):
        print("WARNING: Method outputFile in class XSDataInputDatPorod is deprecated, please use instead exportToFile!")
        self.exportToFile(_outfileName)
    #Method for making a copy in a new instance
    def copy( self ):
        return XSDataInputDatPorod.parseString(self.marshal())
    #Static method for parsing a string
    def parseString( _inString ):
        doc = minidom.parseString(_inString)
        rootNode = doc.documentElement
        rootObj = XSDataInputDatPorod()
        rootObj.build(rootNode)
        # Check that all minOccurs are obeyed by marshalling the created object
        oStreamString = StringIO()
        rootObj.export( oStreamString, 0, name_="XSDataInputDatPorod" )
        oStreamString.close()
        return rootObj
    parseString = staticmethod( parseString )
    #Static method for parsing a file
    def parseFile( _inFilePath ):
        doc = minidom.parse(_inFilePath)
        rootNode = doc.documentElement
        rootObj = XSDataInputDatPorod()
        rootObj.build(rootNode)
        return rootObj
    parseFile = staticmethod( parseFile )
# end class XSDataInputDatPorod


class XSDataInputDataver(XSDataInput):
    """dataver averages two or more curves from files"""
    def __init__(self, configuration=None, outputCurve=None, inputCurve=None):
        XSDataInput.__init__(self, configuration)
        if inputCurve is None:
            self._inputCurve = []
        elif inputCurve.__class__.__name__ == "list":
            self._inputCurve = inputCurve
        else:
            strMessage = "ERROR! XSDataInputDataver constructor argument 'inputCurve' is not list but %s" % self._inputCurve.__class__.__name__
            raise BaseException(strMessage)
        if outputCurve is None:
            self._outputCurve = None
        elif outputCurve.__class__.__name__ == "XSDataFile":
            self._outputCurve = outputCurve
        else:
            strMessage = "ERROR! XSDataInputDataver constructor argument 'outputCurve' is not XSDataFile but %s" % self._outputCurve.__class__.__name__
            raise BaseException(strMessage)
    # Methods and properties for the 'inputCurve' attribute
    def getInputCurve(self): return self._inputCurve
    def setInputCurve(self, inputCurve):
        if inputCurve is None:
            self._inputCurve = []
        elif inputCurve.__class__.__name__ == "list":
            self._inputCurve = inputCurve
        else:
            strMessage = "ERROR! XSDataInputDataver.setInputCurve argument is not list but %s" % inputCurve.__class__.__name__
            raise BaseException(strMessage)
    def delInputCurve(self): self._inputCurve = None
    inputCurve = property(getInputCurve, setInputCurve, delInputCurve, "Property for inputCurve")
    def addInputCurve(self, value):
        if value is None:
            strMessage = "ERROR! XSDataInputDataver.addInputCurve argument is None"
            raise BaseException(strMessage)            
        elif value.__class__.__name__ == "XSDataFile":
            self._inputCurve.append(value)
        else:
            strMessage = "ERROR! XSDataInputDataver.addInputCurve argument is not XSDataFile but %s" % value.__class__.__name__
            raise BaseException(strMessage)
    def insertInputCurve(self, index, value):
        if index is None:
            strMessage = "ERROR! XSDataInputDataver.insertInputCurve argument 'index' is None"
            raise BaseException(strMessage)            
        if value is None:
            strMessage = "ERROR! XSDataInputDataver.insertInputCurve argument 'value' is None"
            raise BaseException(strMessage)            
        elif value.__class__.__name__ == "XSDataFile":
            self._inputCurve[index] = value
        else:
            strMessage = "ERROR! XSDataInputDataver.addInputCurve argument is not XSDataFile but %s" % value.__class__.__name__
            raise BaseException(strMessage)
    # Methods and properties for the 'outputCurve' attribute
    def getOutputCurve(self): return self._outputCurve
    def setOutputCurve(self, outputCurve):
        if outputCurve is None:
            self._outputCurve = None
        elif outputCurve.__class__.__name__ == "XSDataFile":
            self._outputCurve = outputCurve
        else:
            strMessage = "ERROR! XSDataInputDataver.setOutputCurve argument is not XSDataFile but %s" % outputCurve.__class__.__name__
            raise BaseException(strMessage)
    def delOutputCurve(self): self._outputCurve = None
    outputCurve = property(getOutputCurve, setOutputCurve, delOutputCurve, "Property for outputCurve")
    def export(self, outfile, level, name_='XSDataInputDataver'):
        showIndent(outfile, level)
        outfile.write(unicode('<%s>\n' % name_))
        self.exportChildren(outfile, level + 1, name_)
        showIndent(outfile, level)
        outfile.write(unicode('</%s>\n' % name_))
    def exportChildren(self, outfile, level, name_='XSDataInputDataver'):
        XSDataInput.exportChildren(self, outfile, level, name_)
        for inputCurve_ in self.getInputCurve():
            inputCurve_.export(outfile, level, name_='inputCurve')
        if self.getInputCurve() == []:
            warnEmptyAttribute("inputCurve", "XSDataFile")
        if self._outputCurve is not None:
            self.outputCurve.export(outfile, level, name_='outputCurve')
    def build(self, node_):
        for child_ in node_.childNodes:
            nodeName_ = child_.nodeName.split(':')[-1]
            self.buildChildren(child_, nodeName_)
    def buildChildren(self, child_, nodeName_):
        if child_.nodeType == Node.ELEMENT_NODE and \
            nodeName_ == 'inputCurve':
            obj_ = XSDataFile()
            obj_.build(child_)
            self.inputCurve.append(obj_)
        elif child_.nodeType == Node.ELEMENT_NODE and \
            nodeName_ == 'outputCurve':
            obj_ = XSDataFile()
            obj_.build(child_)
            self.setOutputCurve(obj_)
        XSDataInput.buildChildren(self, child_, nodeName_)
    #Method for marshalling an object
    def marshal( self ):
        oStreamString = StringIO()
        oStreamString.write(unicode('<?xml version="1.0" ?>\n'))
        self.export( oStreamString, 0, name_="XSDataInputDataver" )
        oStringXML = oStreamString.getvalue()
        oStreamString.close()
        return oStringXML
    #Only to export the entire XML tree to a file stream on disk
    def exportToFile( self, _outfileName ):
        outfile = open( _outfileName, "w" )
        outfile.write(unicode('<?xml version=\"1.0\" ?>\n'))
        self.export( outfile, 0, name_='XSDataInputDataver' )
        outfile.close()
    #Deprecated method, replaced by exportToFile
    def outputFile( self, _outfileName ):
        print("WARNING: Method outputFile in class XSDataInputDataver is deprecated, please use instead exportToFile!")
        self.exportToFile(_outfileName)
    #Method for making a copy in a new instance
    def copy( self ):
        return XSDataInputDataver.parseString(self.marshal())
    #Static method for parsing a string
    def parseString( _inString ):
        doc = minidom.parseString(_inString)
        rootNode = doc.documentElement
        rootObj = XSDataInputDataver()
        rootObj.build(rootNode)
        # Check that all minOccurs are obeyed by marshalling the created object
        oStreamString = StringIO()
        rootObj.export( oStreamString, 0, name_="XSDataInputDataver" )
        oStreamString.close()
        return rootObj
    parseString = staticmethod( parseString )
    #Static method for parsing a file
    def parseFile( _inFilePath ):
        doc = minidom.parse(_inFilePath)
        rootNode = doc.documentElement
        rootObj = XSDataInputDataver()
        rootObj.build(rootNode)
        return rootObj
    parseFile = staticmethod( parseFile )
# end class XSDataInputDataver


class XSDataInputDatcmp(XSDataInput):
    """datcmp compares two curves from files
	"""
    def __init__(self, configuration=None, inputCurve=None):
        XSDataInput.__init__(self, configuration)
        if inputCurve is None:
            self._inputCurve = []
        elif inputCurve.__class__.__name__ == "list":
            self._inputCurve = inputCurve
        else:
            strMessage = "ERROR! XSDataInputDatcmp constructor argument 'inputCurve' is not list but %s" % self._inputCurve.__class__.__name__
            raise BaseException(strMessage)
    # Methods and properties for the 'inputCurve' attribute
    def getInputCurve(self): return self._inputCurve
    def setInputCurve(self, inputCurve):
        if inputCurve is None:
            self._inputCurve = []
        elif inputCurve.__class__.__name__ == "list":
            self._inputCurve = inputCurve
        else:
            strMessage = "ERROR! XSDataInputDatcmp.setInputCurve argument is not list but %s" % inputCurve.__class__.__name__
            raise BaseException(strMessage)
    def delInputCurve(self): self._inputCurve = None
    inputCurve = property(getInputCurve, setInputCurve, delInputCurve, "Property for inputCurve")
    def addInputCurve(self, value):
        if value is None:
            strMessage = "ERROR! XSDataInputDatcmp.addInputCurve argument is None"
            raise BaseException(strMessage)            
        elif value.__class__.__name__ == "XSDataFile":
            self._inputCurve.append(value)
        else:
            strMessage = "ERROR! XSDataInputDatcmp.addInputCurve argument is not XSDataFile but %s" % value.__class__.__name__
            raise BaseException(strMessage)
    def insertInputCurve(self, index, value):
        if index is None:
            strMessage = "ERROR! XSDataInputDatcmp.insertInputCurve argument 'index' is None"
            raise BaseException(strMessage)            
        if value is None:
            strMessage = "ERROR! XSDataInputDatcmp.insertInputCurve argument 'value' is None"
            raise BaseException(strMessage)            
        elif value.__class__.__name__ == "XSDataFile":
            self._inputCurve[index] = value
        else:
            strMessage = "ERROR! XSDataInputDatcmp.addInputCurve argument is not XSDataFile but %s" % value.__class__.__name__
            raise BaseException(strMessage)
    def export(self, outfile, level, name_='XSDataInputDatcmp'):
        showIndent(outfile, level)
        outfile.write(unicode('<%s>\n' % name_))
        self.exportChildren(outfile, level + 1, name_)
        showIndent(outfile, level)
        outfile.write(unicode('</%s>\n' % name_))
    def exportChildren(self, outfile, level, name_='XSDataInputDatcmp'):
        XSDataInput.exportChildren(self, outfile, level, name_)
        for inputCurve_ in self.getInputCurve():
            inputCurve_.export(outfile, level, name_='inputCurve')
        if self.getInputCurve() == []:
            warnEmptyAttribute("inputCurve", "XSDataFile")
    def build(self, node_):
        for child_ in node_.childNodes:
            nodeName_ = child_.nodeName.split(':')[-1]
            self.buildChildren(child_, nodeName_)
    def buildChildren(self, child_, nodeName_):
        if child_.nodeType == Node.ELEMENT_NODE and \
            nodeName_ == 'inputCurve':
            obj_ = XSDataFile()
            obj_.build(child_)
            self.inputCurve.append(obj_)
        XSDataInput.buildChildren(self, child_, nodeName_)
    #Method for marshalling an object
    def marshal( self ):
        oStreamString = StringIO()
        oStreamString.write(unicode('<?xml version="1.0" ?>\n'))
        self.export( oStreamString, 0, name_="XSDataInputDatcmp" )
        oStringXML = oStreamString.getvalue()
        oStreamString.close()
        return oStringXML
    #Only to export the entire XML tree to a file stream on disk
    def exportToFile( self, _outfileName ):
        outfile = open( _outfileName, "w" )
        outfile.write(unicode('<?xml version=\"1.0\" ?>\n'))
        self.export( outfile, 0, name_='XSDataInputDatcmp' )
        outfile.close()
    #Deprecated method, replaced by exportToFile
    def outputFile( self, _outfileName ):
        print("WARNING: Method outputFile in class XSDataInputDatcmp is deprecated, please use instead exportToFile!")
        self.exportToFile(_outfileName)
    #Method for making a copy in a new instance
    def copy( self ):
        return XSDataInputDatcmp.parseString(self.marshal())
    #Static method for parsing a string
    def parseString( _inString ):
        doc = minidom.parseString(_inString)
        rootNode = doc.documentElement
        rootObj = XSDataInputDatcmp()
        rootObj.build(rootNode)
        # Check that all minOccurs are obeyed by marshalling the created object
        oStreamString = StringIO()
        rootObj.export( oStreamString, 0, name_="XSDataInputDatcmp" )
        oStreamString.close()
        return rootObj
    parseString = staticmethod( parseString )
    #Static method for parsing a file
    def parseFile( _inFilePath ):
        doc = minidom.parse(_inFilePath)
        rootNode = doc.documentElement
        rootObj = XSDataInputDatcmp()
        rootObj.build(rootNode)
        return rootObj
    parseFile = staticmethod( parseFile )
# end class XSDataInputDatcmp


class XSDataInputDatop(XSDataInput):
    """datop makes an operation on curves"""
    def __init__(self, configuration=None, constant=None, operation=None, outputCurve=None, inputCurve=None):
        XSDataInput.__init__(self, configuration)
        if inputCurve is None:
            self._inputCurve = []
        elif inputCurve.__class__.__name__ == "list":
            self._inputCurve = inputCurve
        else:
            strMessage = "ERROR! XSDataInputDatop constructor argument 'inputCurve' is not list but %s" % self._inputCurve.__class__.__name__
            raise BaseException(strMessage)
        if outputCurve is None:
            self._outputCurve = None
        elif outputCurve.__class__.__name__ == "XSDataFile":
            self._outputCurve = outputCurve
        else:
            strMessage = "ERROR! XSDataInputDatop constructor argument 'outputCurve' is not XSDataFile but %s" % self._outputCurve.__class__.__name__
            raise BaseException(strMessage)
        if operation is None:
            self._operation = None
        elif operation.__class__.__name__ == "XSDataString":
            self._operation = operation
        else:
            strMessage = "ERROR! XSDataInputDatop constructor argument 'operation' is not XSDataString but %s" % self._operation.__class__.__name__
            raise BaseException(strMessage)
        if constant is None:
            self._constant = None
        elif constant.__class__.__name__ == "XSDataDouble":
            self._constant = constant
        else:
            strMessage = "ERROR! XSDataInputDatop constructor argument 'constant' is not XSDataDouble but %s" % self._constant.__class__.__name__
            raise BaseException(strMessage)
    # Methods and properties for the 'inputCurve' attribute
    def getInputCurve(self): return self._inputCurve
    def setInputCurve(self, inputCurve):
        if inputCurve is None:
            self._inputCurve = []
        elif inputCurve.__class__.__name__ == "list":
            self._inputCurve = inputCurve
        else:
            strMessage = "ERROR! XSDataInputDatop.setInputCurve argument is not list but %s" % inputCurve.__class__.__name__
            raise BaseException(strMessage)
    def delInputCurve(self): self._inputCurve = None
    inputCurve = property(getInputCurve, setInputCurve, delInputCurve, "Property for inputCurve")
    def addInputCurve(self, value):
        if value is None:
            strMessage = "ERROR! XSDataInputDatop.addInputCurve argument is None"
            raise BaseException(strMessage)            
        elif value.__class__.__name__ == "XSDataFile":
            self._inputCurve.append(value)
        else:
            strMessage = "ERROR! XSDataInputDatop.addInputCurve argument is not XSDataFile but %s" % value.__class__.__name__
            raise BaseException(strMessage)
    def insertInputCurve(self, index, value):
        if index is None:
            strMessage = "ERROR! XSDataInputDatop.insertInputCurve argument 'index' is None"
            raise BaseException(strMessage)            
        if value is None:
            strMessage = "ERROR! XSDataInputDatop.insertInputCurve argument 'value' is None"
            raise BaseException(strMessage)            
        elif value.__class__.__name__ == "XSDataFile":
            self._inputCurve[index] = value
        else:
            strMessage = "ERROR! XSDataInputDatop.addInputCurve argument is not XSDataFile but %s" % value.__class__.__name__
            raise BaseException(strMessage)
    # Methods and properties for the 'outputCurve' attribute
    def getOutputCurve(self): return self._outputCurve
    def setOutputCurve(self, outputCurve):
        if outputCurve is None:
            self._outputCurve = None
        elif outputCurve.__class__.__name__ == "XSDataFile":
            self._outputCurve = outputCurve
        else:
            strMessage = "ERROR! XSDataInputDatop.setOutputCurve argument is not XSDataFile but %s" % outputCurve.__class__.__name__
            raise BaseException(strMessage)
    def delOutputCurve(self): self._outputCurve = None
    outputCurve = property(getOutputCurve, setOutputCurve, delOutputCurve, "Property for outputCurve")
    # Methods and properties for the 'operation' attribute
    def getOperation(self): return self._operation
    def setOperation(self, operation):
        if operation is None:
            self._operation = None
        elif operation.__class__.__name__ == "XSDataString":
            self._operation = operation
        else:
            strMessage = "ERROR! XSDataInputDatop.setOperation argument is not XSDataString but %s" % operation.__class__.__name__
            raise BaseException(strMessage)
    def delOperation(self): self._operation = None
    operation = property(getOperation, setOperation, delOperation, "Property for operation")
    # Methods and properties for the 'constant' attribute
    def getConstant(self): return self._constant
    def setConstant(self, constant):
        if constant is None:
            self._constant = None
        elif constant.__class__.__name__ == "XSDataDouble":
            self._constant = constant
        else:
            strMessage = "ERROR! XSDataInputDatop.setConstant argument is not XSDataDouble but %s" % constant.__class__.__name__
            raise BaseException(strMessage)
    def delConstant(self): self._constant = None
    constant = property(getConstant, setConstant, delConstant, "Property for constant")
    def export(self, outfile, level, name_='XSDataInputDatop'):
        showIndent(outfile, level)
        outfile.write(unicode('<%s>\n' % name_))
        self.exportChildren(outfile, level + 1, name_)
        showIndent(outfile, level)
        outfile.write(unicode('</%s>\n' % name_))
    def exportChildren(self, outfile, level, name_='XSDataInputDatop'):
        XSDataInput.exportChildren(self, outfile, level, name_)
        for inputCurve_ in self.getInputCurve():
            inputCurve_.export(outfile, level, name_='inputCurve')
        if self.getInputCurve() == []:
            warnEmptyAttribute("inputCurve", "XSDataFile")
        if self._outputCurve is not None:
            self.outputCurve.export(outfile, level, name_='outputCurve')
        else:
            warnEmptyAttribute("outputCurve", "XSDataFile")
        if self._operation is not None:
            self.operation.export(outfile, level, name_='operation')
        else:
            warnEmptyAttribute("operation", "XSDataString")
        if self._constant is not None:
            self.constant.export(outfile, level, name_='constant')
    def build(self, node_):
        for child_ in node_.childNodes:
            nodeName_ = child_.nodeName.split(':')[-1]
            self.buildChildren(child_, nodeName_)
    def buildChildren(self, child_, nodeName_):
        if child_.nodeType == Node.ELEMENT_NODE and \
            nodeName_ == 'inputCurve':
            obj_ = XSDataFile()
            obj_.build(child_)
            self.inputCurve.append(obj_)
        elif child_.nodeType == Node.ELEMENT_NODE and \
            nodeName_ == 'outputCurve':
            obj_ = XSDataFile()
            obj_.build(child_)
            self.setOutputCurve(obj_)
        elif child_.nodeType == Node.ELEMENT_NODE and \
            nodeName_ == 'operation':
            obj_ = XSDataString()
            obj_.build(child_)
            self.setOperation(obj_)
        elif child_.nodeType == Node.ELEMENT_NODE and \
            nodeName_ == 'constant':
            obj_ = XSDataDouble()
            obj_.build(child_)
            self.setConstant(obj_)
        XSDataInput.buildChildren(self, child_, nodeName_)
    #Method for marshalling an object
    def marshal( self ):
        oStreamString = StringIO()
        oStreamString.write(unicode('<?xml version="1.0" ?>\n'))
        self.export( oStreamString, 0, name_="XSDataInputDatop" )
        oStringXML = oStreamString.getvalue()
        oStreamString.close()
        return oStringXML
    #Only to export the entire XML tree to a file stream on disk
    def exportToFile( self, _outfileName ):
        outfile = open( _outfileName, "w" )
        outfile.write(unicode('<?xml version=\"1.0\" ?>\n'))
        self.export( outfile, 0, name_='XSDataInputDatop' )
        outfile.close()
    #Deprecated method, replaced by exportToFile
    def outputFile( self, _outfileName ):
        print("WARNING: Method outputFile in class XSDataInputDatop is deprecated, please use instead exportToFile!")
        self.exportToFile(_outfileName)
    #Method for making a copy in a new instance
    def copy( self ):
        return XSDataInputDatop.parseString(self.marshal())
    #Static method for parsing a string
    def parseString( _inString ):
        doc = minidom.parseString(_inString)
        rootNode = doc.documentElement
        rootObj = XSDataInputDatop()
        rootObj.build(rootNode)
        # Check that all minOccurs are obeyed by marshalling the created object
        oStreamString = StringIO()
        rootObj.export( oStreamString, 0, name_="XSDataInputDatop" )
        oStreamString.close()
        return rootObj
    parseString = staticmethod( parseString )
    #Static method for parsing a file
    def parseFile( _inFilePath ):
        doc = minidom.parse(_inFilePath)
        rootNode = doc.documentElement
        rootObj = XSDataInputDatop()
        rootObj.build(rootNode)
        return rootObj
    parseFile = staticmethod( parseFile )
# end class XSDataInputDatop


class XSDataInputGnom(XSDataInput):
    """Input data can be provided either as a list of doubles, as Arrays or as a filename"""
    def __init__(self, configuration=None, mode=None, angularScale=None, experimentalDataFile=None, experimentalDataStdArray=None, experimentalDataStdDev=None, experimentalDataIArray=None, experimentalDataValues=None, experimentalDataQArray=None, experimentalDataQ=None, rMax=None):
        XSDataInput.__init__(self, configuration)
        if rMax is None:
            self._rMax = None
        elif rMax.__class__.__name__ == "XSDataDouble":
            self._rMax = rMax
        else:
            strMessage = "ERROR! XSDataInputGnom constructor argument 'rMax' is not XSDataDouble but %s" % self._rMax.__class__.__name__
            raise BaseException(strMessage)
        if experimentalDataQ is None:
            self._experimentalDataQ = []
        elif experimentalDataQ.__class__.__name__ == "list":
            self._experimentalDataQ = experimentalDataQ
        else:
            strMessage = "ERROR! XSDataInputGnom constructor argument 'experimentalDataQ' is not list but %s" % self._experimentalDataQ.__class__.__name__
            raise BaseException(strMessage)
        if experimentalDataQArray is None:
            self._experimentalDataQArray = None
        elif experimentalDataQArray.__class__.__name__ == "XSDataArray":
            self._experimentalDataQArray = experimentalDataQArray
        else:
            strMessage = "ERROR! XSDataInputGnom constructor argument 'experimentalDataQArray' is not XSDataArray but %s" % self._experimentalDataQArray.__class__.__name__
            raise BaseException(strMessage)
        if experimentalDataValues is None:
            self._experimentalDataValues = []
        elif experimentalDataValues.__class__.__name__ == "list":
            self._experimentalDataValues = experimentalDataValues
        else:
            strMessage = "ERROR! XSDataInputGnom constructor argument 'experimentalDataValues' is not list but %s" % self._experimentalDataValues.__class__.__name__
            raise BaseException(strMessage)
        if experimentalDataIArray is None:
            self._experimentalDataIArray = None
        elif experimentalDataIArray.__class__.__name__ == "XSDataArray":
            self._experimentalDataIArray = experimentalDataIArray
        else:
            strMessage = "ERROR! XSDataInputGnom constructor argument 'experimentalDataIArray' is not XSDataArray but %s" % self._experimentalDataIArray.__class__.__name__
            raise BaseException(strMessage)
        if experimentalDataStdDev is None:
            self._experimentalDataStdDev = []
        elif experimentalDataStdDev.__class__.__name__ == "list":
            self._experimentalDataStdDev = experimentalDataStdDev
        else:
            strMessage = "ERROR! XSDataInputGnom constructor argument 'experimentalDataStdDev' is not list but %s" % self._experimentalDataStdDev.__class__.__name__
            raise BaseException(strMessage)
        if experimentalDataStdArray is None:
            self._experimentalDataStdArray = None
        elif experimentalDataStdArray.__class__.__name__ == "XSDataArray":
            self._experimentalDataStdArray = experimentalDataStdArray
        else:
            strMessage = "ERROR! XSDataInputGnom constructor argument 'experimentalDataStdArray' is not XSDataArray but %s" % self._experimentalDataStdArray.__class__.__name__
            raise BaseException(strMessage)
        if experimentalDataFile is None:
            self._experimentalDataFile = None
        elif experimentalDataFile.__class__.__name__ == "XSDataFile":
            self._experimentalDataFile = experimentalDataFile
        else:
            strMessage = "ERROR! XSDataInputGnom constructor argument 'experimentalDataFile' is not XSDataFile but %s" % self._experimentalDataFile.__class__.__name__
            raise BaseException(strMessage)
        if angularScale is None:
            self._angularScale = None
        elif angularScale.__class__.__name__ == "XSDataInteger":
            self._angularScale = angularScale
        else:
            strMessage = "ERROR! XSDataInputGnom constructor argument 'angularScale' is not XSDataInteger but %s" % self._angularScale.__class__.__name__
            raise BaseException(strMessage)
        if mode is None:
            self._mode = None
        elif mode.__class__.__name__ == "XSDataString":
            self._mode = mode
        else:
            strMessage = "ERROR! XSDataInputGnom constructor argument 'mode' is not XSDataString but %s" % self._mode.__class__.__name__
            raise BaseException(strMessage)
    # Methods and properties for the 'rMax' attribute
    def getRMax(self): return self._rMax
    def setRMax(self, rMax):
        if rMax is None:
            self._rMax = None
        elif rMax.__class__.__name__ == "XSDataDouble":
            self._rMax = rMax
        else:
            strMessage = "ERROR! XSDataInputGnom.setRMax argument is not XSDataDouble but %s" % rMax.__class__.__name__
            raise BaseException(strMessage)
    def delRMax(self): self._rMax = None
    rMax = property(getRMax, setRMax, delRMax, "Property for rMax")
    # Methods and properties for the 'experimentalDataQ' attribute
    def getExperimentalDataQ(self): return self._experimentalDataQ
    def setExperimentalDataQ(self, experimentalDataQ):
        if experimentalDataQ is None:
            self._experimentalDataQ = []
        elif experimentalDataQ.__class__.__name__ == "list":
            self._experimentalDataQ = experimentalDataQ
        else:
            strMessage = "ERROR! XSDataInputGnom.setExperimentalDataQ argument is not list but %s" % experimentalDataQ.__class__.__name__
            raise BaseException(strMessage)
    def delExperimentalDataQ(self): self._experimentalDataQ = None
    experimentalDataQ = property(getExperimentalDataQ, setExperimentalDataQ, delExperimentalDataQ, "Property for experimentalDataQ")
    def addExperimentalDataQ(self, value):
        if value is None:
            strMessage = "ERROR! XSDataInputGnom.addExperimentalDataQ argument is None"
            raise BaseException(strMessage)            
        elif value.__class__.__name__ == "XSDataDouble":
            self._experimentalDataQ.append(value)
        else:
            strMessage = "ERROR! XSDataInputGnom.addExperimentalDataQ argument is not XSDataDouble but %s" % value.__class__.__name__
            raise BaseException(strMessage)
    def insertExperimentalDataQ(self, index, value):
        if index is None:
            strMessage = "ERROR! XSDataInputGnom.insertExperimentalDataQ argument 'index' is None"
            raise BaseException(strMessage)            
        if value is None:
            strMessage = "ERROR! XSDataInputGnom.insertExperimentalDataQ argument 'value' is None"
            raise BaseException(strMessage)            
        elif value.__class__.__name__ == "XSDataDouble":
            self._experimentalDataQ[index] = value
        else:
            strMessage = "ERROR! XSDataInputGnom.addExperimentalDataQ argument is not XSDataDouble but %s" % value.__class__.__name__
            raise BaseException(strMessage)
    # Methods and properties for the 'experimentalDataQArray' attribute
    def getExperimentalDataQArray(self): return self._experimentalDataQArray
    def setExperimentalDataQArray(self, experimentalDataQArray):
        if experimentalDataQArray is None:
            self._experimentalDataQArray = None
        elif experimentalDataQArray.__class__.__name__ == "XSDataArray":
            self._experimentalDataQArray = experimentalDataQArray
        else:
            strMessage = "ERROR! XSDataInputGnom.setExperimentalDataQArray argument is not XSDataArray but %s" % experimentalDataQArray.__class__.__name__
            raise BaseException(strMessage)
    def delExperimentalDataQArray(self): self._experimentalDataQArray = None
    experimentalDataQArray = property(getExperimentalDataQArray, setExperimentalDataQArray, delExperimentalDataQArray, "Property for experimentalDataQArray")
    # Methods and properties for the 'experimentalDataValues' attribute
    def getExperimentalDataValues(self): return self._experimentalDataValues
    def setExperimentalDataValues(self, experimentalDataValues):
        if experimentalDataValues is None:
            self._experimentalDataValues = []
        elif experimentalDataValues.__class__.__name__ == "list":
            self._experimentalDataValues = experimentalDataValues
        else:
            strMessage = "ERROR! XSDataInputGnom.setExperimentalDataValues argument is not list but %s" % experimentalDataValues.__class__.__name__
            raise BaseException(strMessage)
    def delExperimentalDataValues(self): self._experimentalDataValues = None
    experimentalDataValues = property(getExperimentalDataValues, setExperimentalDataValues, delExperimentalDataValues, "Property for experimentalDataValues")
    def addExperimentalDataValues(self, value):
        if value is None:
            strMessage = "ERROR! XSDataInputGnom.addExperimentalDataValues argument is None"
            raise BaseException(strMessage)            
        elif value.__class__.__name__ == "XSDataDouble":
            self._experimentalDataValues.append(value)
        else:
            strMessage = "ERROR! XSDataInputGnom.addExperimentalDataValues argument is not XSDataDouble but %s" % value.__class__.__name__
            raise BaseException(strMessage)
    def insertExperimentalDataValues(self, index, value):
        if index is None:
            strMessage = "ERROR! XSDataInputGnom.insertExperimentalDataValues argument 'index' is None"
            raise BaseException(strMessage)            
        if value is None:
            strMessage = "ERROR! XSDataInputGnom.insertExperimentalDataValues argument 'value' is None"
            raise BaseException(strMessage)            
        elif value.__class__.__name__ == "XSDataDouble":
            self._experimentalDataValues[index] = value
        else:
            strMessage = "ERROR! XSDataInputGnom.addExperimentalDataValues argument is not XSDataDouble but %s" % value.__class__.__name__
            raise BaseException(strMessage)
    # Methods and properties for the 'experimentalDataIArray' attribute
    def getExperimentalDataIArray(self): return self._experimentalDataIArray
    def setExperimentalDataIArray(self, experimentalDataIArray):
        if experimentalDataIArray is None:
            self._experimentalDataIArray = None
        elif experimentalDataIArray.__class__.__name__ == "XSDataArray":
            self._experimentalDataIArray = experimentalDataIArray
        else:
            strMessage = "ERROR! XSDataInputGnom.setExperimentalDataIArray argument is not XSDataArray but %s" % experimentalDataIArray.__class__.__name__
            raise BaseException(strMessage)
    def delExperimentalDataIArray(self): self._experimentalDataIArray = None
    experimentalDataIArray = property(getExperimentalDataIArray, setExperimentalDataIArray, delExperimentalDataIArray, "Property for experimentalDataIArray")
    # Methods and properties for the 'experimentalDataStdDev' attribute
    def getExperimentalDataStdDev(self): return self._experimentalDataStdDev
    def setExperimentalDataStdDev(self, experimentalDataStdDev):
        if experimentalDataStdDev is None:
            self._experimentalDataStdDev = []
        elif experimentalDataStdDev.__class__.__name__ == "list":
            self._experimentalDataStdDev = experimentalDataStdDev
        else:
            strMessage = "ERROR! XSDataInputGnom.setExperimentalDataStdDev argument is not list but %s" % experimentalDataStdDev.__class__.__name__
            raise BaseException(strMessage)
    def delExperimentalDataStdDev(self): self._experimentalDataStdDev = None
    experimentalDataStdDev = property(getExperimentalDataStdDev, setExperimentalDataStdDev, delExperimentalDataStdDev, "Property for experimentalDataStdDev")
    def addExperimentalDataStdDev(self, value):
        if value is None:
            strMessage = "ERROR! XSDataInputGnom.addExperimentalDataStdDev argument is None"
            raise BaseException(strMessage)            
        elif value.__class__.__name__ == "XSDataDouble":
            self._experimentalDataStdDev.append(value)
        else:
            strMessage = "ERROR! XSDataInputGnom.addExperimentalDataStdDev argument is not XSDataDouble but %s" % value.__class__.__name__
            raise BaseException(strMessage)
    def insertExperimentalDataStdDev(self, index, value):
        if index is None:
            strMessage = "ERROR! XSDataInputGnom.insertExperimentalDataStdDev argument 'index' is None"
            raise BaseException(strMessage)            
        if value is None:
            strMessage = "ERROR! XSDataInputGnom.insertExperimentalDataStdDev argument 'value' is None"
            raise BaseException(strMessage)            
        elif value.__class__.__name__ == "XSDataDouble":
            self._experimentalDataStdDev[index] = value
        else:
            strMessage = "ERROR! XSDataInputGnom.addExperimentalDataStdDev argument is not XSDataDouble but %s" % value.__class__.__name__
            raise BaseException(strMessage)
    # Methods and properties for the 'experimentalDataStdArray' attribute
    def getExperimentalDataStdArray(self): return self._experimentalDataStdArray
    def setExperimentalDataStdArray(self, experimentalDataStdArray):
        if experimentalDataStdArray is None:
            self._experimentalDataStdArray = None
        elif experimentalDataStdArray.__class__.__name__ == "XSDataArray":
            self._experimentalDataStdArray = experimentalDataStdArray
        else:
            strMessage = "ERROR! XSDataInputGnom.setExperimentalDataStdArray argument is not XSDataArray but %s" % experimentalDataStdArray.__class__.__name__
            raise BaseException(strMessage)
    def delExperimentalDataStdArray(self): self._experimentalDataStdArray = None
    experimentalDataStdArray = property(getExperimentalDataStdArray, setExperimentalDataStdArray, delExperimentalDataStdArray, "Property for experimentalDataStdArray")
    # Methods and properties for the 'experimentalDataFile' attribute
    def getExperimentalDataFile(self): return self._experimentalDataFile
    def setExperimentalDataFile(self, experimentalDataFile):
        if experimentalDataFile is None:
            self._experimentalDataFile = None
        elif experimentalDataFile.__class__.__name__ == "XSDataFile":
            self._experimentalDataFile = experimentalDataFile
        else:
            strMessage = "ERROR! XSDataInputGnom.setExperimentalDataFile argument is not XSDataFile but %s" % experimentalDataFile.__class__.__name__
            raise BaseException(strMessage)
    def delExperimentalDataFile(self): self._experimentalDataFile = None
    experimentalDataFile = property(getExperimentalDataFile, setExperimentalDataFile, delExperimentalDataFile, "Property for experimentalDataFile")
    # Methods and properties for the 'angularScale' attribute
    def getAngularScale(self): return self._angularScale
    def setAngularScale(self, angularScale):
        if angularScale is None:
            self._angularScale = None
        elif angularScale.__class__.__name__ == "XSDataInteger":
            self._angularScale = angularScale
        else:
            strMessage = "ERROR! XSDataInputGnom.setAngularScale argument is not XSDataInteger but %s" % angularScale.__class__.__name__
            raise BaseException(strMessage)
    def delAngularScale(self): self._angularScale = None
    angularScale = property(getAngularScale, setAngularScale, delAngularScale, "Property for angularScale")
    # Methods and properties for the 'mode' attribute
    def getMode(self): return self._mode
    def setMode(self, mode):
        if mode is None:
            self._mode = None
        elif mode.__class__.__name__ == "XSDataString":
            self._mode = mode
        else:
            strMessage = "ERROR! XSDataInputGnom.setMode argument is not XSDataString but %s" % mode.__class__.__name__
            raise BaseException(strMessage)
    def delMode(self): self._mode = None
    mode = property(getMode, setMode, delMode, "Property for mode")
    def export(self, outfile, level, name_='XSDataInputGnom'):
        showIndent(outfile, level)
        outfile.write(unicode('<%s>\n' % name_))
        self.exportChildren(outfile, level + 1, name_)
        showIndent(outfile, level)
        outfile.write(unicode('</%s>\n' % name_))
    def exportChildren(self, outfile, level, name_='XSDataInputGnom'):
        XSDataInput.exportChildren(self, outfile, level, name_)
        if self._rMax is not None:
            self.rMax.export(outfile, level, name_='rMax')
        else:
            warnEmptyAttribute("rMax", "XSDataDouble")
        for experimentalDataQ_ in self.getExperimentalDataQ():
            experimentalDataQ_.export(outfile, level, name_='experimentalDataQ')
        if self._experimentalDataQArray is not None:
            self.experimentalDataQArray.export(outfile, level, name_='experimentalDataQArray')
        for experimentalDataValues_ in self.getExperimentalDataValues():
            experimentalDataValues_.export(outfile, level, name_='experimentalDataValues')
        if self._experimentalDataIArray is not None:
            self.experimentalDataIArray.export(outfile, level, name_='experimentalDataIArray')
        for experimentalDataStdDev_ in self.getExperimentalDataStdDev():
            experimentalDataStdDev_.export(outfile, level, name_='experimentalDataStdDev')
        if self._experimentalDataStdArray is not None:
            self.experimentalDataStdArray.export(outfile, level, name_='experimentalDataStdArray')
        if self._experimentalDataFile is not None:
            self.experimentalDataFile.export(outfile, level, name_='experimentalDataFile')
        if self._angularScale is not None:
            self.angularScale.export(outfile, level, name_='angularScale')
        if self._mode is not None:
            self.mode.export(outfile, level, name_='mode')
    def build(self, node_):
        for child_ in node_.childNodes:
            nodeName_ = child_.nodeName.split(':')[-1]
            self.buildChildren(child_, nodeName_)
    def buildChildren(self, child_, nodeName_):
        if child_.nodeType == Node.ELEMENT_NODE and \
            nodeName_ == 'rMax':
            obj_ = XSDataDouble()
            obj_.build(child_)
            self.setRMax(obj_)
        elif child_.nodeType == Node.ELEMENT_NODE and \
            nodeName_ == 'experimentalDataQ':
            obj_ = XSDataDouble()
            obj_.build(child_)
            self.experimentalDataQ.append(obj_)
        elif child_.nodeType == Node.ELEMENT_NODE and \
            nodeName_ == 'experimentalDataQArray':
            obj_ = XSDataArray()
            obj_.build(child_)
            self.setExperimentalDataQArray(obj_)
        elif child_.nodeType == Node.ELEMENT_NODE and \
            nodeName_ == 'experimentalDataValues':
            obj_ = XSDataDouble()
            obj_.build(child_)
            self.experimentalDataValues.append(obj_)
        elif child_.nodeType == Node.ELEMENT_NODE and \
            nodeName_ == 'experimentalDataIArray':
            obj_ = XSDataArray()
            obj_.build(child_)
            self.setExperimentalDataIArray(obj_)
        elif child_.nodeType == Node.ELEMENT_NODE and \
            nodeName_ == 'experimentalDataStdDev':
            obj_ = XSDataDouble()
            obj_.build(child_)
            self.experimentalDataStdDev.append(obj_)
        elif child_.nodeType == Node.ELEMENT_NODE and \
            nodeName_ == 'experimentalDataStdArray':
            obj_ = XSDataArray()
            obj_.build(child_)
            self.setExperimentalDataStdArray(obj_)
        elif child_.nodeType == Node.ELEMENT_NODE and \
            nodeName_ == 'experimentalDataFile':
            obj_ = XSDataFile()
            obj_.build(child_)
            self.setExperimentalDataFile(obj_)
        elif child_.nodeType == Node.ELEMENT_NODE and \
            nodeName_ == 'angularScale':
            obj_ = XSDataInteger()
            obj_.build(child_)
            self.setAngularScale(obj_)
        elif child_.nodeType == Node.ELEMENT_NODE and \
            nodeName_ == 'mode':
            obj_ = XSDataString()
            obj_.build(child_)
            self.setMode(obj_)
        XSDataInput.buildChildren(self, child_, nodeName_)
    #Method for marshalling an object
    def marshal( self ):
        oStreamString = StringIO()
        oStreamString.write(unicode('<?xml version="1.0" ?>\n'))
        self.export( oStreamString, 0, name_="XSDataInputGnom" )
        oStringXML = oStreamString.getvalue()
        oStreamString.close()
        return oStringXML
    #Only to export the entire XML tree to a file stream on disk
    def exportToFile( self, _outfileName ):
        outfile = open( _outfileName, "w" )
        outfile.write(unicode('<?xml version=\"1.0\" ?>\n'))
        self.export( outfile, 0, name_='XSDataInputGnom' )
        outfile.close()
    #Deprecated method, replaced by exportToFile
    def outputFile( self, _outfileName ):
        print("WARNING: Method outputFile in class XSDataInputGnom is deprecated, please use instead exportToFile!")
        self.exportToFile(_outfileName)
    #Method for making a copy in a new instance
    def copy( self ):
        return XSDataInputGnom.parseString(self.marshal())
    #Static method for parsing a string
    def parseString( _inString ):
        doc = minidom.parseString(_inString)
        rootNode = doc.documentElement
        rootObj = XSDataInputGnom()
        rootObj.build(rootNode)
        # Check that all minOccurs are obeyed by marshalling the created object
        oStreamString = StringIO()
        rootObj.export( oStreamString, 0, name_="XSDataInputGnom" )
        oStreamString.close()
        return rootObj
    parseString = staticmethod( parseString )
    #Static method for parsing a file
    def parseFile( _inFilePath ):
        doc = minidom.parse(_inFilePath)
        rootNode = doc.documentElement
        rootObj = XSDataInputGnom()
        rootObj.build(rootNode)
        return rootObj
    parseFile = staticmethod( parseFile )
# end class XSDataInputGnom


class XSDataInputSaxsAnalysis(XSDataInput):
    """AutoRg -> Gnom -> Prod pipeline"""
    def __init__(self, configuration=None, graphFormat=None, gnomFile=None, autoRg=None, scatterCurve=None):
        XSDataInput.__init__(self, configuration)
        if scatterCurve is None:
            self._scatterCurve = None
        elif scatterCurve.__class__.__name__ == "XSDataFile":
            self._scatterCurve = scatterCurve
        else:
            strMessage = "ERROR! XSDataInputSaxsAnalysis constructor argument 'scatterCurve' is not XSDataFile but %s" % self._scatterCurve.__class__.__name__
            raise BaseException(strMessage)
        if autoRg is None:
            self._autoRg = None
        elif autoRg.__class__.__name__ == "XSDataAutoRg":
            self._autoRg = autoRg
        else:
            strMessage = "ERROR! XSDataInputSaxsAnalysis constructor argument 'autoRg' is not XSDataAutoRg but %s" % self._autoRg.__class__.__name__
            raise BaseException(strMessage)
        if gnomFile is None:
            self._gnomFile = None
        elif gnomFile.__class__.__name__ == "XSDataFile":
            self._gnomFile = gnomFile
        else:
            strMessage = "ERROR! XSDataInputSaxsAnalysis constructor argument 'gnomFile' is not XSDataFile but %s" % self._gnomFile.__class__.__name__
            raise BaseException(strMessage)
        if graphFormat is None:
            self._graphFormat = None
        elif graphFormat.__class__.__name__ == "XSDataString":
            self._graphFormat = graphFormat
        else:
            strMessage = "ERROR! XSDataInputSaxsAnalysis constructor argument 'graphFormat' is not XSDataString but %s" % self._graphFormat.__class__.__name__
            raise BaseException(strMessage)
    # Methods and properties for the 'scatterCurve' attribute
    def getScatterCurve(self): return self._scatterCurve
    def setScatterCurve(self, scatterCurve):
        if scatterCurve is None:
            self._scatterCurve = None
        elif scatterCurve.__class__.__name__ == "XSDataFile":
            self._scatterCurve = scatterCurve
        else:
            strMessage = "ERROR! XSDataInputSaxsAnalysis.setScatterCurve argument is not XSDataFile but %s" % scatterCurve.__class__.__name__
            raise BaseException(strMessage)
    def delScatterCurve(self): self._scatterCurve = None
    scatterCurve = property(getScatterCurve, setScatterCurve, delScatterCurve, "Property for scatterCurve")
    # Methods and properties for the 'autoRg' attribute
    def getAutoRg(self): return self._autoRg
    def setAutoRg(self, autoRg):
        if autoRg is None:
            self._autoRg = None
        elif autoRg.__class__.__name__ == "XSDataAutoRg":
            self._autoRg = autoRg
        else:
            strMessage = "ERROR! XSDataInputSaxsAnalysis.setAutoRg argument is not XSDataAutoRg but %s" % autoRg.__class__.__name__
            raise BaseException(strMessage)
    def delAutoRg(self): self._autoRg = None
    autoRg = property(getAutoRg, setAutoRg, delAutoRg, "Property for autoRg")
    # Methods and properties for the 'gnomFile' attribute
    def getGnomFile(self): return self._gnomFile
    def setGnomFile(self, gnomFile):
        if gnomFile is None:
            self._gnomFile = None
        elif gnomFile.__class__.__name__ == "XSDataFile":
            self._gnomFile = gnomFile
        else:
            strMessage = "ERROR! XSDataInputSaxsAnalysis.setGnomFile argument is not XSDataFile but %s" % gnomFile.__class__.__name__
            raise BaseException(strMessage)
    def delGnomFile(self): self._gnomFile = None
    gnomFile = property(getGnomFile, setGnomFile, delGnomFile, "Property for gnomFile")
    # Methods and properties for the 'graphFormat' attribute
    def getGraphFormat(self): return self._graphFormat
    def setGraphFormat(self, graphFormat):
        if graphFormat is None:
            self._graphFormat = None
        elif graphFormat.__class__.__name__ == "XSDataString":
            self._graphFormat = graphFormat
        else:
            strMessage = "ERROR! XSDataInputSaxsAnalysis.setGraphFormat argument is not XSDataString but %s" % graphFormat.__class__.__name__
            raise BaseException(strMessage)
    def delGraphFormat(self): self._graphFormat = None
    graphFormat = property(getGraphFormat, setGraphFormat, delGraphFormat, "Property for graphFormat")
    def export(self, outfile, level, name_='XSDataInputSaxsAnalysis'):
        showIndent(outfile, level)
        outfile.write(unicode('<%s>\n' % name_))
        self.exportChildren(outfile, level + 1, name_)
        showIndent(outfile, level)
        outfile.write(unicode('</%s>\n' % name_))
    def exportChildren(self, outfile, level, name_='XSDataInputSaxsAnalysis'):
        XSDataInput.exportChildren(self, outfile, level, name_)
        if self._scatterCurve is not None:
            self.scatterCurve.export(outfile, level, name_='scatterCurve')
        else:
            warnEmptyAttribute("scatterCurve", "XSDataFile")
        if self._autoRg is not None:
            self.autoRg.export(outfile, level, name_='autoRg')
        if self._gnomFile is not None:
            self.gnomFile.export(outfile, level, name_='gnomFile')
        if self._graphFormat is not None:
            self.graphFormat.export(outfile, level, name_='graphFormat')
    def build(self, node_):
        for child_ in node_.childNodes:
            nodeName_ = child_.nodeName.split(':')[-1]
            self.buildChildren(child_, nodeName_)
    def buildChildren(self, child_, nodeName_):
        if child_.nodeType == Node.ELEMENT_NODE and \
            nodeName_ == 'scatterCurve':
            obj_ = XSDataFile()
            obj_.build(child_)
            self.setScatterCurve(obj_)
        elif child_.nodeType == Node.ELEMENT_NODE and \
            nodeName_ == 'autoRg':
            obj_ = XSDataAutoRg()
            obj_.build(child_)
            self.setAutoRg(obj_)
        elif child_.nodeType == Node.ELEMENT_NODE and \
            nodeName_ == 'gnomFile':
            obj_ = XSDataFile()
            obj_.build(child_)
            self.setGnomFile(obj_)
        elif child_.nodeType == Node.ELEMENT_NODE and \
            nodeName_ == 'graphFormat':
            obj_ = XSDataString()
            obj_.build(child_)
            self.setGraphFormat(obj_)
        XSDataInput.buildChildren(self, child_, nodeName_)
    #Method for marshalling an object
    def marshal( self ):
        oStreamString = StringIO()
        oStreamString.write(unicode('<?xml version="1.0" ?>\n'))
        self.export( oStreamString, 0, name_="XSDataInputSaxsAnalysis" )
        oStringXML = oStreamString.getvalue()
        oStreamString.close()
        return oStringXML
    #Only to export the entire XML tree to a file stream on disk
    def exportToFile( self, _outfileName ):
        outfile = open( _outfileName, "w" )
        outfile.write(unicode('<?xml version=\"1.0\" ?>\n'))
        self.export( outfile, 0, name_='XSDataInputSaxsAnalysis' )
        outfile.close()
    #Deprecated method, replaced by exportToFile
    def outputFile( self, _outfileName ):
        print("WARNING: Method outputFile in class XSDataInputSaxsAnalysis is deprecated, please use instead exportToFile!")
        self.exportToFile(_outfileName)
    #Method for making a copy in a new instance
    def copy( self ):
        return XSDataInputSaxsAnalysis.parseString(self.marshal())
    #Static method for parsing a string
    def parseString( _inString ):
        doc = minidom.parseString(_inString)
        rootNode = doc.documentElement
        rootObj = XSDataInputSaxsAnalysis()
        rootObj.build(rootNode)
        # Check that all minOccurs are obeyed by marshalling the created object
        oStreamString = StringIO()
        rootObj.export( oStreamString, 0, name_="XSDataInputSaxsAnalysis" )
        oStreamString.close()
        return rootObj
    parseString = staticmethod( parseString )
    #Static method for parsing a file
    def parseFile( _inFilePath ):
        doc = minidom.parse(_inFilePath)
        rootNode = doc.documentElement
        rootObj = XSDataInputSaxsAnalysis()
        rootObj.build(rootNode)
        return rootObj
    parseFile = staticmethod( parseFile )
# end class XSDataInputSaxsAnalysis


class XSDataInputSaxsAnalysisModeling(XSDataInput):
    """AutoRg -> Gnom -> Prod -> Dammif -> Supcomb -> Damaver -> Damfilt -> Damstart -> Dammin pipeline"""
    def __init__(self, configuration=None, graphFormat=None, gnomFile=None, autoRg=None, scatterCurve=None):
        XSDataInput.__init__(self, configuration)
        if scatterCurve is None:
            self._scatterCurve = None
        elif scatterCurve.__class__.__name__ == "XSDataFile":
            self._scatterCurve = scatterCurve
        else:
            strMessage = "ERROR! XSDataInputSaxsAnalysisModeling constructor argument 'scatterCurve' is not XSDataFile but %s" % self._scatterCurve.__class__.__name__
            raise BaseException(strMessage)
        if autoRg is None:
            self._autoRg = None
        elif autoRg.__class__.__name__ == "XSDataAutoRg":
            self._autoRg = autoRg
        else:
            strMessage = "ERROR! XSDataInputSaxsAnalysisModeling constructor argument 'autoRg' is not XSDataAutoRg but %s" % self._autoRg.__class__.__name__
            raise BaseException(strMessage)
        if gnomFile is None:
            self._gnomFile = None
        elif gnomFile.__class__.__name__ == "XSDataFile":
            self._gnomFile = gnomFile
        else:
            strMessage = "ERROR! XSDataInputSaxsAnalysisModeling constructor argument 'gnomFile' is not XSDataFile but %s" % self._gnomFile.__class__.__name__
            raise BaseException(strMessage)
        if graphFormat is None:
            self._graphFormat = None
        elif graphFormat.__class__.__name__ == "XSDataString":
            self._graphFormat = graphFormat
        else:
            strMessage = "ERROR! XSDataInputSaxsAnalysisModeling constructor argument 'graphFormat' is not XSDataString but %s" % self._graphFormat.__class__.__name__
            raise BaseException(strMessage)
    # Methods and properties for the 'scatterCurve' attribute
    def getScatterCurve(self): return self._scatterCurve
    def setScatterCurve(self, scatterCurve):
        if scatterCurve is None:
            self._scatterCurve = None
        elif scatterCurve.__class__.__name__ == "XSDataFile":
            self._scatterCurve = scatterCurve
        else:
            strMessage = "ERROR! XSDataInputSaxsAnalysisModeling.setScatterCurve argument is not XSDataFile but %s" % scatterCurve.__class__.__name__
            raise BaseException(strMessage)
    def delScatterCurve(self): self._scatterCurve = None
    scatterCurve = property(getScatterCurve, setScatterCurve, delScatterCurve, "Property for scatterCurve")
    # Methods and properties for the 'autoRg' attribute
    def getAutoRg(self): return self._autoRg
    def setAutoRg(self, autoRg):
        if autoRg is None:
            self._autoRg = None
        elif autoRg.__class__.__name__ == "XSDataAutoRg":
            self._autoRg = autoRg
        else:
            strMessage = "ERROR! XSDataInputSaxsAnalysisModeling.setAutoRg argument is not XSDataAutoRg but %s" % autoRg.__class__.__name__
            raise BaseException(strMessage)
    def delAutoRg(self): self._autoRg = None
    autoRg = property(getAutoRg, setAutoRg, delAutoRg, "Property for autoRg")
    # Methods and properties for the 'gnomFile' attribute
    def getGnomFile(self): return self._gnomFile
    def setGnomFile(self, gnomFile):
        if gnomFile is None:
            self._gnomFile = None
        elif gnomFile.__class__.__name__ == "XSDataFile":
            self._gnomFile = gnomFile
        else:
            strMessage = "ERROR! XSDataInputSaxsAnalysisModeling.setGnomFile argument is not XSDataFile but %s" % gnomFile.__class__.__name__
            raise BaseException(strMessage)
    def delGnomFile(self): self._gnomFile = None
    gnomFile = property(getGnomFile, setGnomFile, delGnomFile, "Property for gnomFile")
    # Methods and properties for the 'graphFormat' attribute
    def getGraphFormat(self): return self._graphFormat
    def setGraphFormat(self, graphFormat):
        if graphFormat is None:
            self._graphFormat = None
        elif graphFormat.__class__.__name__ == "XSDataString":
            self._graphFormat = graphFormat
        else:
            strMessage = "ERROR! XSDataInputSaxsAnalysisModeling.setGraphFormat argument is not XSDataString but %s" % graphFormat.__class__.__name__
            raise BaseException(strMessage)
    def delGraphFormat(self): self._graphFormat = None
    graphFormat = property(getGraphFormat, setGraphFormat, delGraphFormat, "Property for graphFormat")
    def export(self, outfile, level, name_='XSDataInputSaxsAnalysisModeling'):
        showIndent(outfile, level)
        outfile.write(unicode('<%s>\n' % name_))
        self.exportChildren(outfile, level + 1, name_)
        showIndent(outfile, level)
        outfile.write(unicode('</%s>\n' % name_))
    def exportChildren(self, outfile, level, name_='XSDataInputSaxsAnalysisModeling'):
        XSDataInput.exportChildren(self, outfile, level, name_)
        if self._scatterCurve is not None:
            self.scatterCurve.export(outfile, level, name_='scatterCurve')
        else:
            warnEmptyAttribute("scatterCurve", "XSDataFile")
        if self._autoRg is not None:
            self.autoRg.export(outfile, level, name_='autoRg')
        if self._gnomFile is not None:
            self.gnomFile.export(outfile, level, name_='gnomFile')
        if self._graphFormat is not None:
            self.graphFormat.export(outfile, level, name_='graphFormat')
    def build(self, node_):
        for child_ in node_.childNodes:
            nodeName_ = child_.nodeName.split(':')[-1]
            self.buildChildren(child_, nodeName_)
    def buildChildren(self, child_, nodeName_):
        if child_.nodeType == Node.ELEMENT_NODE and \
            nodeName_ == 'scatterCurve':
            obj_ = XSDataFile()
            obj_.build(child_)
            self.setScatterCurve(obj_)
        elif child_.nodeType == Node.ELEMENT_NODE and \
            nodeName_ == 'autoRg':
            obj_ = XSDataAutoRg()
            obj_.build(child_)
            self.setAutoRg(obj_)
        elif child_.nodeType == Node.ELEMENT_NODE and \
            nodeName_ == 'gnomFile':
            obj_ = XSDataFile()
            obj_.build(child_)
            self.setGnomFile(obj_)
        elif child_.nodeType == Node.ELEMENT_NODE and \
            nodeName_ == 'graphFormat':
            obj_ = XSDataString()
            obj_.build(child_)
            self.setGraphFormat(obj_)
        XSDataInput.buildChildren(self, child_, nodeName_)
    #Method for marshalling an object
    def marshal( self ):
        oStreamString = StringIO()
        oStreamString.write(unicode('<?xml version="1.0" ?>\n'))
        self.export( oStreamString, 0, name_="XSDataInputSaxsAnalysisModeling" )
        oStringXML = oStreamString.getvalue()
        oStreamString.close()
        return oStringXML
    #Only to export the entire XML tree to a file stream on disk
    def exportToFile( self, _outfileName ):
        outfile = open( _outfileName, "w" )
        outfile.write(unicode('<?xml version=\"1.0\" ?>\n'))
        self.export( outfile, 0, name_='XSDataInputSaxsAnalysisModeling' )
        outfile.close()
    #Deprecated method, replaced by exportToFile
    def outputFile( self, _outfileName ):
        print("WARNING: Method outputFile in class XSDataInputSaxsAnalysisModeling is deprecated, please use instead exportToFile!")
        self.exportToFile(_outfileName)
    #Method for making a copy in a new instance
    def copy( self ):
        return XSDataInputSaxsAnalysisModeling.parseString(self.marshal())
    #Static method for parsing a string
    def parseString( _inString ):
        doc = minidom.parseString(_inString)
        rootNode = doc.documentElement
        rootObj = XSDataInputSaxsAnalysisModeling()
        rootObj.build(rootNode)
        # Check that all minOccurs are obeyed by marshalling the created object
        oStreamString = StringIO()
        rootObj.export( oStreamString, 0, name_="XSDataInputSaxsAnalysisModeling" )
        oStreamString.close()
        return rootObj
    parseString = staticmethod( parseString )
    #Static method for parsing a file
    def parseFile( _inFilePath ):
        doc = minidom.parse(_inFilePath)
        rootNode = doc.documentElement
        rootObj = XSDataInputSaxsAnalysisModeling()
        rootObj.build(rootNode)
        return rootObj
    parseFile = staticmethod( parseFile )
# end class XSDataInputSaxsAnalysisModeling


class XSDataInputSaxsModeling(XSDataInput):
    """Dammif -> Supcomb -> Damaver -> Damfilt -> Damstart -> Dammin pipeline"""
    def __init__(self, configuration=None, graphFormat=None, gnomFile=None):
        XSDataInput.__init__(self, configuration)
        if gnomFile is None:
            self._gnomFile = None
        elif gnomFile.__class__.__name__ == "XSDataFile":
            self._gnomFile = gnomFile
        else:
            strMessage = "ERROR! XSDataInputSaxsModeling constructor argument 'gnomFile' is not XSDataFile but %s" % self._gnomFile.__class__.__name__
            raise BaseException(strMessage)
        if graphFormat is None:
            self._graphFormat = None
        elif graphFormat.__class__.__name__ == "XSDataString":
            self._graphFormat = graphFormat
        else:
            strMessage = "ERROR! XSDataInputSaxsModeling constructor argument 'graphFormat' is not XSDataString but %s" % self._graphFormat.__class__.__name__
            raise BaseException(strMessage)
    # Methods and properties for the 'gnomFile' attribute
    def getGnomFile(self): return self._gnomFile
    def setGnomFile(self, gnomFile):
        if gnomFile is None:
            self._gnomFile = None
        elif gnomFile.__class__.__name__ == "XSDataFile":
            self._gnomFile = gnomFile
        else:
            strMessage = "ERROR! XSDataInputSaxsModeling.setGnomFile argument is not XSDataFile but %s" % gnomFile.__class__.__name__
            raise BaseException(strMessage)
    def delGnomFile(self): self._gnomFile = None
    gnomFile = property(getGnomFile, setGnomFile, delGnomFile, "Property for gnomFile")
    # Methods and properties for the 'graphFormat' attribute
    def getGraphFormat(self): return self._graphFormat
    def setGraphFormat(self, graphFormat):
        if graphFormat is None:
            self._graphFormat = None
        elif graphFormat.__class__.__name__ == "XSDataString":
            self._graphFormat = graphFormat
        else:
            strMessage = "ERROR! XSDataInputSaxsModeling.setGraphFormat argument is not XSDataString but %s" % graphFormat.__class__.__name__
            raise BaseException(strMessage)
    def delGraphFormat(self): self._graphFormat = None
    graphFormat = property(getGraphFormat, setGraphFormat, delGraphFormat, "Property for graphFormat")
    def export(self, outfile, level, name_='XSDataInputSaxsModeling'):
        showIndent(outfile, level)
        outfile.write(unicode('<%s>\n' % name_))
        self.exportChildren(outfile, level + 1, name_)
        showIndent(outfile, level)
        outfile.write(unicode('</%s>\n' % name_))
    def exportChildren(self, outfile, level, name_='XSDataInputSaxsModeling'):
        XSDataInput.exportChildren(self, outfile, level, name_)
        if self._gnomFile is not None:
            self.gnomFile.export(outfile, level, name_='gnomFile')
        else:
            warnEmptyAttribute("gnomFile", "XSDataFile")
        if self._graphFormat is not None:
            self.graphFormat.export(outfile, level, name_='graphFormat')
    def build(self, node_):
        for child_ in node_.childNodes:
            nodeName_ = child_.nodeName.split(':')[-1]
            self.buildChildren(child_, nodeName_)
    def buildChildren(self, child_, nodeName_):
        if child_.nodeType == Node.ELEMENT_NODE and \
            nodeName_ == 'gnomFile':
            obj_ = XSDataFile()
            obj_.build(child_)
            self.setGnomFile(obj_)
        elif child_.nodeType == Node.ELEMENT_NODE and \
            nodeName_ == 'graphFormat':
            obj_ = XSDataString()
            obj_.build(child_)
            self.setGraphFormat(obj_)
        XSDataInput.buildChildren(self, child_, nodeName_)
    #Method for marshalling an object
    def marshal( self ):
        oStreamString = StringIO()
        oStreamString.write(unicode('<?xml version="1.0" ?>\n'))
        self.export( oStreamString, 0, name_="XSDataInputSaxsModeling" )
        oStringXML = oStreamString.getvalue()
        oStreamString.close()
        return oStringXML
    #Only to export the entire XML tree to a file stream on disk
    def exportToFile( self, _outfileName ):
        outfile = open( _outfileName, "w" )
        outfile.write(unicode('<?xml version=\"1.0\" ?>\n'))
        self.export( outfile, 0, name_='XSDataInputSaxsModeling' )
        outfile.close()
    #Deprecated method, replaced by exportToFile
    def outputFile( self, _outfileName ):
        print("WARNING: Method outputFile in class XSDataInputSaxsModeling is deprecated, please use instead exportToFile!")
        self.exportToFile(_outfileName)
    #Method for making a copy in a new instance
    def copy( self ):
        return XSDataInputSaxsModeling.parseString(self.marshal())
    #Static method for parsing a string
    def parseString( _inString ):
        doc = minidom.parseString(_inString)
        rootNode = doc.documentElement
        rootObj = XSDataInputSaxsModeling()
        rootObj.build(rootNode)
        # Check that all minOccurs are obeyed by marshalling the created object
        oStreamString = StringIO()
        rootObj.export( oStreamString, 0, name_="XSDataInputSaxsModeling" )
        oStreamString.close()
        return rootObj
    parseString = staticmethod( parseString )
    #Static method for parsing a file
    def parseFile( _inFilePath ):
        doc = minidom.parse(_inFilePath)
        rootNode = doc.documentElement
        rootObj = XSDataInputSaxsModeling()
        rootObj.build(rootNode)
        return rootObj
    parseFile = staticmethod( parseFile )
# end class XSDataInputSaxsModeling


class XSDataInputSaxsPipeline(XSDataInput):
    """Run ProcessOneFile on each file of a time time serie until autorg """
    def __init__(self, configuration=None, rawImageSize=None, relativeFidelity=None, absoluteFidelity=None, forceReprocess=None, directoryMisc=None, directory2D=None, directory1D=None, experimentSetup=None, sample=None, fileSerie=None):
        XSDataInput.__init__(self, configuration)
        if fileSerie is None:
            self._fileSerie = None
        elif fileSerie.__class__.__name__ == "XSDataFileSeries":
            self._fileSerie = fileSerie
        else:
            strMessage = "ERROR! XSDataInputSaxsPipeline constructor argument 'fileSerie' is not XSDataFileSeries but %s" % self._fileSerie.__class__.__name__
            raise BaseException(strMessage)
        if sample is None:
            self._sample = None
        elif sample.__class__.__name__ == "XSDataBioSaxsSample":
            self._sample = sample
        else:
            strMessage = "ERROR! XSDataInputSaxsPipeline constructor argument 'sample' is not XSDataBioSaxsSample but %s" % self._sample.__class__.__name__
            raise BaseException(strMessage)
        if experimentSetup is None:
            self._experimentSetup = None
        elif experimentSetup.__class__.__name__ == "XSDataBioSaxsExperimentSetup":
            self._experimentSetup = experimentSetup
        else:
            strMessage = "ERROR! XSDataInputSaxsPipeline constructor argument 'experimentSetup' is not XSDataBioSaxsExperimentSetup but %s" % self._experimentSetup.__class__.__name__
            raise BaseException(strMessage)
        if directory1D is None:
            self._directory1D = None
        elif directory1D.__class__.__name__ == "XSDataFile":
            self._directory1D = directory1D
        else:
            strMessage = "ERROR! XSDataInputSaxsPipeline constructor argument 'directory1D' is not XSDataFile but %s" % self._directory1D.__class__.__name__
            raise BaseException(strMessage)
        if directory2D is None:
            self._directory2D = None
        elif directory2D.__class__.__name__ == "XSDataFile":
            self._directory2D = directory2D
        else:
            strMessage = "ERROR! XSDataInputSaxsPipeline constructor argument 'directory2D' is not XSDataFile but %s" % self._directory2D.__class__.__name__
            raise BaseException(strMessage)
        if directoryMisc is None:
            self._directoryMisc = None
        elif directoryMisc.__class__.__name__ == "XSDataFile":
            self._directoryMisc = directoryMisc
        else:
            strMessage = "ERROR! XSDataInputSaxsPipeline constructor argument 'directoryMisc' is not XSDataFile but %s" % self._directoryMisc.__class__.__name__
            raise BaseException(strMessage)
        if forceReprocess is None:
            self._forceReprocess = None
        elif forceReprocess.__class__.__name__ == "XSDataBoolean":
            self._forceReprocess = forceReprocess
        else:
            strMessage = "ERROR! XSDataInputSaxsPipeline constructor argument 'forceReprocess' is not XSDataBoolean but %s" % self._forceReprocess.__class__.__name__
            raise BaseException(strMessage)
        if absoluteFidelity is None:
            self._absoluteFidelity = None
        elif absoluteFidelity.__class__.__name__ == "XSDataDouble":
            self._absoluteFidelity = absoluteFidelity
        else:
            strMessage = "ERROR! XSDataInputSaxsPipeline constructor argument 'absoluteFidelity' is not XSDataDouble but %s" % self._absoluteFidelity.__class__.__name__
            raise BaseException(strMessage)
        if relativeFidelity is None:
            self._relativeFidelity = None
        elif relativeFidelity.__class__.__name__ == "XSDataDouble":
            self._relativeFidelity = relativeFidelity
        else:
            strMessage = "ERROR! XSDataInputSaxsPipeline constructor argument 'relativeFidelity' is not XSDataDouble but %s" % self._relativeFidelity.__class__.__name__
            raise BaseException(strMessage)
        if rawImageSize is None:
            self._rawImageSize = None
        elif rawImageSize.__class__.__name__ == "XSDataInteger":
            self._rawImageSize = rawImageSize
        else:
            strMessage = "ERROR! XSDataInputSaxsPipeline constructor argument 'rawImageSize' is not XSDataInteger but %s" % self._rawImageSize.__class__.__name__
            raise BaseException(strMessage)
    # Methods and properties for the 'fileSerie' attribute
    def getFileSerie(self): return self._fileSerie
    def setFileSerie(self, fileSerie):
        if fileSerie is None:
            self._fileSerie = None
        elif fileSerie.__class__.__name__ == "XSDataFileSeries":
            self._fileSerie = fileSerie
        else:
            strMessage = "ERROR! XSDataInputSaxsPipeline.setFileSerie argument is not XSDataFileSeries but %s" % fileSerie.__class__.__name__
            raise BaseException(strMessage)
    def delFileSerie(self): self._fileSerie = None
    fileSerie = property(getFileSerie, setFileSerie, delFileSerie, "Property for fileSerie")
    # Methods and properties for the 'sample' attribute
    def getSample(self): return self._sample
    def setSample(self, sample):
        if sample is None:
            self._sample = None
        elif sample.__class__.__name__ == "XSDataBioSaxsSample":
            self._sample = sample
        else:
            strMessage = "ERROR! XSDataInputSaxsPipeline.setSample argument is not XSDataBioSaxsSample but %s" % sample.__class__.__name__
            raise BaseException(strMessage)
    def delSample(self): self._sample = None
    sample = property(getSample, setSample, delSample, "Property for sample")
    # Methods and properties for the 'experimentSetup' attribute
    def getExperimentSetup(self): return self._experimentSetup
    def setExperimentSetup(self, experimentSetup):
        if experimentSetup is None:
            self._experimentSetup = None
        elif experimentSetup.__class__.__name__ == "XSDataBioSaxsExperimentSetup":
            self._experimentSetup = experimentSetup
        else:
            strMessage = "ERROR! XSDataInputSaxsPipeline.setExperimentSetup argument is not XSDataBioSaxsExperimentSetup but %s" % experimentSetup.__class__.__name__
            raise BaseException(strMessage)
    def delExperimentSetup(self): self._experimentSetup = None
    experimentSetup = property(getExperimentSetup, setExperimentSetup, delExperimentSetup, "Property for experimentSetup")
    # Methods and properties for the 'directory1D' attribute
    def getDirectory1D(self): return self._directory1D
    def setDirectory1D(self, directory1D):
        if directory1D is None:
            self._directory1D = None
        elif directory1D.__class__.__name__ == "XSDataFile":
            self._directory1D = directory1D
        else:
            strMessage = "ERROR! XSDataInputSaxsPipeline.setDirectory1D argument is not XSDataFile but %s" % directory1D.__class__.__name__
            raise BaseException(strMessage)
    def delDirectory1D(self): self._directory1D = None
    directory1D = property(getDirectory1D, setDirectory1D, delDirectory1D, "Property for directory1D")
    # Methods and properties for the 'directory2D' attribute
    def getDirectory2D(self): return self._directory2D
    def setDirectory2D(self, directory2D):
        if directory2D is None:
            self._directory2D = None
        elif directory2D.__class__.__name__ == "XSDataFile":
            self._directory2D = directory2D
        else:
            strMessage = "ERROR! XSDataInputSaxsPipeline.setDirectory2D argument is not XSDataFile but %s" % directory2D.__class__.__name__
            raise BaseException(strMessage)
    def delDirectory2D(self): self._directory2D = None
    directory2D = property(getDirectory2D, setDirectory2D, delDirectory2D, "Property for directory2D")
    # Methods and properties for the 'directoryMisc' attribute
    def getDirectoryMisc(self): return self._directoryMisc
    def setDirectoryMisc(self, directoryMisc):
        if directoryMisc is None:
            self._directoryMisc = None
        elif directoryMisc.__class__.__name__ == "XSDataFile":
            self._directoryMisc = directoryMisc
        else:
            strMessage = "ERROR! XSDataInputSaxsPipeline.setDirectoryMisc argument is not XSDataFile but %s" % directoryMisc.__class__.__name__
            raise BaseException(strMessage)
    def delDirectoryMisc(self): self._directoryMisc = None
    directoryMisc = property(getDirectoryMisc, setDirectoryMisc, delDirectoryMisc, "Property for directoryMisc")
    # Methods and properties for the 'forceReprocess' attribute
    def getForceReprocess(self): return self._forceReprocess
    def setForceReprocess(self, forceReprocess):
        if forceReprocess is None:
            self._forceReprocess = None
        elif forceReprocess.__class__.__name__ == "XSDataBoolean":
            self._forceReprocess = forceReprocess
        else:
            strMessage = "ERROR! XSDataInputSaxsPipeline.setForceReprocess argument is not XSDataBoolean but %s" % forceReprocess.__class__.__name__
            raise BaseException(strMessage)
    def delForceReprocess(self): self._forceReprocess = None
    forceReprocess = property(getForceReprocess, setForceReprocess, delForceReprocess, "Property for forceReprocess")
    # Methods and properties for the 'absoluteFidelity' attribute
    def getAbsoluteFidelity(self): return self._absoluteFidelity
    def setAbsoluteFidelity(self, absoluteFidelity):
        if absoluteFidelity is None:
            self._absoluteFidelity = None
        elif absoluteFidelity.__class__.__name__ == "XSDataDouble":
            self._absoluteFidelity = absoluteFidelity
        else:
            strMessage = "ERROR! XSDataInputSaxsPipeline.setAbsoluteFidelity argument is not XSDataDouble but %s" % absoluteFidelity.__class__.__name__
            raise BaseException(strMessage)
    def delAbsoluteFidelity(self): self._absoluteFidelity = None
    absoluteFidelity = property(getAbsoluteFidelity, setAbsoluteFidelity, delAbsoluteFidelity, "Property for absoluteFidelity")
    # Methods and properties for the 'relativeFidelity' attribute
    def getRelativeFidelity(self): return self._relativeFidelity
    def setRelativeFidelity(self, relativeFidelity):
        if relativeFidelity is None:
            self._relativeFidelity = None
        elif relativeFidelity.__class__.__name__ == "XSDataDouble":
            self._relativeFidelity = relativeFidelity
        else:
            strMessage = "ERROR! XSDataInputSaxsPipeline.setRelativeFidelity argument is not XSDataDouble but %s" % relativeFidelity.__class__.__name__
            raise BaseException(strMessage)
    def delRelativeFidelity(self): self._relativeFidelity = None
    relativeFidelity = property(getRelativeFidelity, setRelativeFidelity, delRelativeFidelity, "Property for relativeFidelity")
    # Methods and properties for the 'rawImageSize' attribute
    def getRawImageSize(self): return self._rawImageSize
    def setRawImageSize(self, rawImageSize):
        if rawImageSize is None:
            self._rawImageSize = None
        elif rawImageSize.__class__.__name__ == "XSDataInteger":
            self._rawImageSize = rawImageSize
        else:
            strMessage = "ERROR! XSDataInputSaxsPipeline.setRawImageSize argument is not XSDataInteger but %s" % rawImageSize.__class__.__name__
            raise BaseException(strMessage)
    def delRawImageSize(self): self._rawImageSize = None
    rawImageSize = property(getRawImageSize, setRawImageSize, delRawImageSize, "Property for rawImageSize")
    def export(self, outfile, level, name_='XSDataInputSaxsPipeline'):
        showIndent(outfile, level)
        outfile.write(unicode('<%s>\n' % name_))
        self.exportChildren(outfile, level + 1, name_)
        showIndent(outfile, level)
        outfile.write(unicode('</%s>\n' % name_))
    def exportChildren(self, outfile, level, name_='XSDataInputSaxsPipeline'):
        XSDataInput.exportChildren(self, outfile, level, name_)
        if self._fileSerie is not None:
            self.fileSerie.export(outfile, level, name_='fileSerie')
        else:
            warnEmptyAttribute("fileSerie", "XSDataFileSeries")
        if self._sample is not None:
            self.sample.export(outfile, level, name_='sample')
        else:
            warnEmptyAttribute("sample", "XSDataBioSaxsSample")
        if self._experimentSetup is not None:
            self.experimentSetup.export(outfile, level, name_='experimentSetup')
        else:
            warnEmptyAttribute("experimentSetup", "XSDataBioSaxsExperimentSetup")
        if self._directory1D is not None:
            self.directory1D.export(outfile, level, name_='directory1D')
        else:
            warnEmptyAttribute("directory1D", "XSDataFile")
        if self._directory2D is not None:
            self.directory2D.export(outfile, level, name_='directory2D')
        else:
            warnEmptyAttribute("directory2D", "XSDataFile")
        if self._directoryMisc is not None:
            self.directoryMisc.export(outfile, level, name_='directoryMisc')
        else:
            warnEmptyAttribute("directoryMisc", "XSDataFile")
        if self._forceReprocess is not None:
            self.forceReprocess.export(outfile, level, name_='forceReprocess')
        if self._absoluteFidelity is not None:
            self.absoluteFidelity.export(outfile, level, name_='absoluteFidelity')
        if self._relativeFidelity is not None:
            self.relativeFidelity.export(outfile, level, name_='relativeFidelity')
        if self._rawImageSize is not None:
            self.rawImageSize.export(outfile, level, name_='rawImageSize')
    def build(self, node_):
        for child_ in node_.childNodes:
            nodeName_ = child_.nodeName.split(':')[-1]
            self.buildChildren(child_, nodeName_)
    def buildChildren(self, child_, nodeName_):
        if child_.nodeType == Node.ELEMENT_NODE and \
            nodeName_ == 'fileSerie':
            obj_ = XSDataFileSeries()
            obj_.build(child_)
            self.setFileSerie(obj_)
        elif child_.nodeType == Node.ELEMENT_NODE and \
            nodeName_ == 'sample':
            obj_ = XSDataBioSaxsSample()
            obj_.build(child_)
            self.setSample(obj_)
        elif child_.nodeType == Node.ELEMENT_NODE and \
            nodeName_ == 'experimentSetup':
            obj_ = XSDataBioSaxsExperimentSetup()
            obj_.build(child_)
            self.setExperimentSetup(obj_)
        elif child_.nodeType == Node.ELEMENT_NODE and \
            nodeName_ == 'directory1D':
            obj_ = XSDataFile()
            obj_.build(child_)
            self.setDirectory1D(obj_)
        elif child_.nodeType == Node.ELEMENT_NODE and \
            nodeName_ == 'directory2D':
            obj_ = XSDataFile()
            obj_.build(child_)
            self.setDirectory2D(obj_)
        elif child_.nodeType == Node.ELEMENT_NODE and \
            nodeName_ == 'directoryMisc':
            obj_ = XSDataFile()
            obj_.build(child_)
            self.setDirectoryMisc(obj_)
        elif child_.nodeType == Node.ELEMENT_NODE and \
            nodeName_ == 'forceReprocess':
            obj_ = XSDataBoolean()
            obj_.build(child_)
            self.setForceReprocess(obj_)
        elif child_.nodeType == Node.ELEMENT_NODE and \
            nodeName_ == 'absoluteFidelity':
            obj_ = XSDataDouble()
            obj_.build(child_)
            self.setAbsoluteFidelity(obj_)
        elif child_.nodeType == Node.ELEMENT_NODE and \
            nodeName_ == 'relativeFidelity':
            obj_ = XSDataDouble()
            obj_.build(child_)
            self.setRelativeFidelity(obj_)
        elif child_.nodeType == Node.ELEMENT_NODE and \
            nodeName_ == 'rawImageSize':
            obj_ = XSDataInteger()
            obj_.build(child_)
            self.setRawImageSize(obj_)
        XSDataInput.buildChildren(self, child_, nodeName_)
    #Method for marshalling an object
    def marshal( self ):
        oStreamString = StringIO()
        oStreamString.write(unicode('<?xml version="1.0" ?>\n'))
        self.export( oStreamString, 0, name_="XSDataInputSaxsPipeline" )
        oStringXML = oStreamString.getvalue()
        oStreamString.close()
        return oStringXML
    #Only to export the entire XML tree to a file stream on disk
    def exportToFile( self, _outfileName ):
        outfile = open( _outfileName, "w" )
        outfile.write(unicode('<?xml version=\"1.0\" ?>\n'))
        self.export( outfile, 0, name_='XSDataInputSaxsPipeline' )
        outfile.close()
    #Deprecated method, replaced by exportToFile
    def outputFile( self, _outfileName ):
        print("WARNING: Method outputFile in class XSDataInputSaxsPipeline is deprecated, please use instead exportToFile!")
        self.exportToFile(_outfileName)
    #Method for making a copy in a new instance
    def copy( self ):
        return XSDataInputSaxsPipeline.parseString(self.marshal())
    #Static method for parsing a string
    def parseString( _inString ):
        doc = minidom.parseString(_inString)
        rootNode = doc.documentElement
        rootObj = XSDataInputSaxsPipeline()
        rootObj.build(rootNode)
        # Check that all minOccurs are obeyed by marshalling the created object
        oStreamString = StringIO()
        rootObj.export( oStreamString, 0, name_="XSDataInputSaxsPipeline" )
        oStreamString.close()
        return rootObj
    parseString = staticmethod( parseString )
    #Static method for parsing a file
    def parseFile( _inFilePath ):
        doc = minidom.parse(_inFilePath)
        rootNode = doc.documentElement
        rootObj = XSDataInputSaxsPipeline()
        rootObj.build(rootNode)
        return rootObj
    parseFile = staticmethod( parseFile )
# end class XSDataInputSaxsPipeline


class XSDataInputSupcomb(XSDataInput):
    """name is the name to be given to the model"""
    def __init__(self, configuration=None, name=None, backbone=None, enantiomorphs=None, superimposeFile=None, templateFile=None):
        XSDataInput.__init__(self, configuration)
        if templateFile is None:
            self._templateFile = None
        elif templateFile.__class__.__name__ == "XSDataFile":
            self._templateFile = templateFile
        else:
            strMessage = "ERROR! XSDataInputSupcomb constructor argument 'templateFile' is not XSDataFile but %s" % self._templateFile.__class__.__name__
            raise BaseException(strMessage)
        if superimposeFile is None:
            self._superimposeFile = None
        elif superimposeFile.__class__.__name__ == "XSDataFile":
            self._superimposeFile = superimposeFile
        else:
            strMessage = "ERROR! XSDataInputSupcomb constructor argument 'superimposeFile' is not XSDataFile but %s" % self._superimposeFile.__class__.__name__
            raise BaseException(strMessage)
        if enantiomorphs is None:
            self._enantiomorphs = None
        elif enantiomorphs.__class__.__name__ == "XSDataBoolean":
            self._enantiomorphs = enantiomorphs
        else:
            strMessage = "ERROR! XSDataInputSupcomb constructor argument 'enantiomorphs' is not XSDataBoolean but %s" % self._enantiomorphs.__class__.__name__
            raise BaseException(strMessage)
        if backbone is None:
            self._backbone = None
        elif backbone.__class__.__name__ == "XSDataBoolean":
            self._backbone = backbone
        else:
            strMessage = "ERROR! XSDataInputSupcomb constructor argument 'backbone' is not XSDataBoolean but %s" % self._backbone.__class__.__name__
            raise BaseException(strMessage)
        if name is None:
            self._name = None
        elif name.__class__.__name__ == "XSDataString":
            self._name = name
        else:
            strMessage = "ERROR! XSDataInputSupcomb constructor argument 'name' is not XSDataString but %s" % self._name.__class__.__name__
            raise BaseException(strMessage)
    # Methods and properties for the 'templateFile' attribute
    def getTemplateFile(self): return self._templateFile
    def setTemplateFile(self, templateFile):
        if templateFile is None:
            self._templateFile = None
        elif templateFile.__class__.__name__ == "XSDataFile":
            self._templateFile = templateFile
        else:
            strMessage = "ERROR! XSDataInputSupcomb.setTemplateFile argument is not XSDataFile but %s" % templateFile.__class__.__name__
            raise BaseException(strMessage)
    def delTemplateFile(self): self._templateFile = None
    templateFile = property(getTemplateFile, setTemplateFile, delTemplateFile, "Property for templateFile")
    # Methods and properties for the 'superimposeFile' attribute
    def getSuperimposeFile(self): return self._superimposeFile
    def setSuperimposeFile(self, superimposeFile):
        if superimposeFile is None:
            self._superimposeFile = None
        elif superimposeFile.__class__.__name__ == "XSDataFile":
            self._superimposeFile = superimposeFile
        else:
            strMessage = "ERROR! XSDataInputSupcomb.setSuperimposeFile argument is not XSDataFile but %s" % superimposeFile.__class__.__name__
            raise BaseException(strMessage)
    def delSuperimposeFile(self): self._superimposeFile = None
    superimposeFile = property(getSuperimposeFile, setSuperimposeFile, delSuperimposeFile, "Property for superimposeFile")
    # Methods and properties for the 'enantiomorphs' attribute
    def getEnantiomorphs(self): return self._enantiomorphs
    def setEnantiomorphs(self, enantiomorphs):
        if enantiomorphs is None:
            self._enantiomorphs = None
        elif enantiomorphs.__class__.__name__ == "XSDataBoolean":
            self._enantiomorphs = enantiomorphs
        else:
            strMessage = "ERROR! XSDataInputSupcomb.setEnantiomorphs argument is not XSDataBoolean but %s" % enantiomorphs.__class__.__name__
            raise BaseException(strMessage)
    def delEnantiomorphs(self): self._enantiomorphs = None
    enantiomorphs = property(getEnantiomorphs, setEnantiomorphs, delEnantiomorphs, "Property for enantiomorphs")
    # Methods and properties for the 'backbone' attribute
    def getBackbone(self): return self._backbone
    def setBackbone(self, backbone):
        if backbone is None:
            self._backbone = None
        elif backbone.__class__.__name__ == "XSDataBoolean":
            self._backbone = backbone
        else:
            strMessage = "ERROR! XSDataInputSupcomb.setBackbone argument is not XSDataBoolean but %s" % backbone.__class__.__name__
            raise BaseException(strMessage)
    def delBackbone(self): self._backbone = None
    backbone = property(getBackbone, setBackbone, delBackbone, "Property for backbone")
    # Methods and properties for the 'name' attribute
    def getName(self): return self._name
    def setName(self, name):
        if name is None:
            self._name = None
        elif name.__class__.__name__ == "XSDataString":
            self._name = name
        else:
            strMessage = "ERROR! XSDataInputSupcomb.setName argument is not XSDataString but %s" % name.__class__.__name__
            raise BaseException(strMessage)
    def delName(self): self._name = None
    name = property(getName, setName, delName, "Property for name")
    def export(self, outfile, level, name_='XSDataInputSupcomb'):
        showIndent(outfile, level)
        outfile.write(unicode('<%s>\n' % name_))
        self.exportChildren(outfile, level + 1, name_)
        showIndent(outfile, level)
        outfile.write(unicode('</%s>\n' % name_))
    def exportChildren(self, outfile, level, name_='XSDataInputSupcomb'):
        XSDataInput.exportChildren(self, outfile, level, name_)
        if self._templateFile is not None:
            self.templateFile.export(outfile, level, name_='templateFile')
        else:
            warnEmptyAttribute("templateFile", "XSDataFile")
        if self._superimposeFile is not None:
            self.superimposeFile.export(outfile, level, name_='superimposeFile')
        else:
            warnEmptyAttribute("superimposeFile", "XSDataFile")
        if self._enantiomorphs is not None:
            self.enantiomorphs.export(outfile, level, name_='enantiomorphs')
        if self._backbone is not None:
            self.backbone.export(outfile, level, name_='backbone')
        if self._name is not None:
            self.name.export(outfile, level, name_='name')
    def build(self, node_):
        for child_ in node_.childNodes:
            nodeName_ = child_.nodeName.split(':')[-1]
            self.buildChildren(child_, nodeName_)
    def buildChildren(self, child_, nodeName_):
        if child_.nodeType == Node.ELEMENT_NODE and \
            nodeName_ == 'templateFile':
            obj_ = XSDataFile()
            obj_.build(child_)
            self.setTemplateFile(obj_)
        elif child_.nodeType == Node.ELEMENT_NODE and \
            nodeName_ == 'superimposeFile':
            obj_ = XSDataFile()
            obj_.build(child_)
            self.setSuperimposeFile(obj_)
        elif child_.nodeType == Node.ELEMENT_NODE and \
            nodeName_ == 'enantiomorphs':
            obj_ = XSDataBoolean()
            obj_.build(child_)
            self.setEnantiomorphs(obj_)
        elif child_.nodeType == Node.ELEMENT_NODE and \
            nodeName_ == 'backbone':
            obj_ = XSDataBoolean()
            obj_.build(child_)
            self.setBackbone(obj_)
        elif child_.nodeType == Node.ELEMENT_NODE and \
            nodeName_ == 'name':
            obj_ = XSDataString()
            obj_.build(child_)
            self.setName(obj_)
        XSDataInput.buildChildren(self, child_, nodeName_)
    #Method for marshalling an object
    def marshal( self ):
        oStreamString = StringIO()
        oStreamString.write(unicode('<?xml version="1.0" ?>\n'))
        self.export( oStreamString, 0, name_="XSDataInputSupcomb" )
        oStringXML = oStreamString.getvalue()
        oStreamString.close()
        return oStringXML
    #Only to export the entire XML tree to a file stream on disk
    def exportToFile( self, _outfileName ):
        outfile = open( _outfileName, "w" )
        outfile.write(unicode('<?xml version=\"1.0\" ?>\n'))
        self.export( outfile, 0, name_='XSDataInputSupcomb' )
        outfile.close()
    #Deprecated method, replaced by exportToFile
    def outputFile( self, _outfileName ):
        print("WARNING: Method outputFile in class XSDataInputSupcomb is deprecated, please use instead exportToFile!")
        self.exportToFile(_outfileName)
    #Method for making a copy in a new instance
    def copy( self ):
        return XSDataInputSupcomb.parseString(self.marshal())
    #Static method for parsing a string
    def parseString( _inString ):
        doc = minidom.parseString(_inString)
        rootNode = doc.documentElement
        rootObj = XSDataInputSupcomb()
        rootObj.build(rootNode)
        # Check that all minOccurs are obeyed by marshalling the created object
        oStreamString = StringIO()
        rootObj.export( oStreamString, 0, name_="XSDataInputSupcomb" )
        oStreamString.close()
        return rootObj
    parseString = staticmethod( parseString )
    #Static method for parsing a file
    def parseFile( _inFilePath ):
        doc = minidom.parse(_inFilePath)
        rootNode = doc.documentElement
        rootObj = XSDataInputSupcomb()
        rootObj.build(rootNode)
        return rootObj
    parseFile = staticmethod( parseFile )
# end class XSDataInputSupcomb


class XSDataResultAutoRg(XSDataResult):
    def __init__(self, status=None, autoRgOut=None):
        XSDataResult.__init__(self, status)
        if autoRgOut is None:
            self._autoRgOut = []
        elif autoRgOut.__class__.__name__ == "list":
            self._autoRgOut = autoRgOut
        else:
            strMessage = "ERROR! XSDataResultAutoRg constructor argument 'autoRgOut' is not list but %s" % self._autoRgOut.__class__.__name__
            raise BaseException(strMessage)
    # Methods and properties for the 'autoRgOut' attribute
    def getAutoRgOut(self): return self._autoRgOut
    def setAutoRgOut(self, autoRgOut):
        if autoRgOut is None:
            self._autoRgOut = []
        elif autoRgOut.__class__.__name__ == "list":
            self._autoRgOut = autoRgOut
        else:
            strMessage = "ERROR! XSDataResultAutoRg.setAutoRgOut argument is not list but %s" % autoRgOut.__class__.__name__
            raise BaseException(strMessage)
    def delAutoRgOut(self): self._autoRgOut = None
    autoRgOut = property(getAutoRgOut, setAutoRgOut, delAutoRgOut, "Property for autoRgOut")
    def addAutoRgOut(self, value):
        if value is None:
            strMessage = "ERROR! XSDataResultAutoRg.addAutoRgOut argument is None"
            raise BaseException(strMessage)            
        elif value.__class__.__name__ == "XSDataAutoRg":
            self._autoRgOut.append(value)
        else:
            strMessage = "ERROR! XSDataResultAutoRg.addAutoRgOut argument is not XSDataAutoRg but %s" % value.__class__.__name__
            raise BaseException(strMessage)
    def insertAutoRgOut(self, index, value):
        if index is None:
            strMessage = "ERROR! XSDataResultAutoRg.insertAutoRgOut argument 'index' is None"
            raise BaseException(strMessage)            
        if value is None:
            strMessage = "ERROR! XSDataResultAutoRg.insertAutoRgOut argument 'value' is None"
            raise BaseException(strMessage)            
        elif value.__class__.__name__ == "XSDataAutoRg":
            self._autoRgOut[index] = value
        else:
            strMessage = "ERROR! XSDataResultAutoRg.addAutoRgOut argument is not XSDataAutoRg but %s" % value.__class__.__name__
            raise BaseException(strMessage)
    def export(self, outfile, level, name_='XSDataResultAutoRg'):
        showIndent(outfile, level)
        outfile.write(unicode('<%s>\n' % name_))
        self.exportChildren(outfile, level + 1, name_)
        showIndent(outfile, level)
        outfile.write(unicode('</%s>\n' % name_))
    def exportChildren(self, outfile, level, name_='XSDataResultAutoRg'):
        XSDataResult.exportChildren(self, outfile, level, name_)
        for autoRgOut_ in self.getAutoRgOut():
            autoRgOut_.export(outfile, level, name_='autoRgOut')
        if self.getAutoRgOut() == []:
            warnEmptyAttribute("autoRgOut", "XSDataAutoRg")
    def build(self, node_):
        for child_ in node_.childNodes:
            nodeName_ = child_.nodeName.split(':')[-1]
            self.buildChildren(child_, nodeName_)
    def buildChildren(self, child_, nodeName_):
        if child_.nodeType == Node.ELEMENT_NODE and \
            nodeName_ == 'autoRgOut':
            obj_ = XSDataAutoRg()
            obj_.build(child_)
            self.autoRgOut.append(obj_)
        XSDataResult.buildChildren(self, child_, nodeName_)
    #Method for marshalling an object
    def marshal( self ):
        oStreamString = StringIO()
        oStreamString.write(unicode('<?xml version="1.0" ?>\n'))
        self.export( oStreamString, 0, name_="XSDataResultAutoRg" )
        oStringXML = oStreamString.getvalue()
        oStreamString.close()
        return oStringXML
    #Only to export the entire XML tree to a file stream on disk
    def exportToFile( self, _outfileName ):
        outfile = open( _outfileName, "w" )
        outfile.write(unicode('<?xml version=\"1.0\" ?>\n'))
        self.export( outfile, 0, name_='XSDataResultAutoRg' )
        outfile.close()
    #Deprecated method, replaced by exportToFile
    def outputFile( self, _outfileName ):
        print("WARNING: Method outputFile in class XSDataResultAutoRg is deprecated, please use instead exportToFile!")
        self.exportToFile(_outfileName)
    #Method for making a copy in a new instance
    def copy( self ):
        return XSDataResultAutoRg.parseString(self.marshal())
    #Static method for parsing a string
    def parseString( _inString ):
        doc = minidom.parseString(_inString)
        rootNode = doc.documentElement
        rootObj = XSDataResultAutoRg()
        rootObj.build(rootNode)
        # Check that all minOccurs are obeyed by marshalling the created object
        oStreamString = StringIO()
        rootObj.export( oStreamString, 0, name_="XSDataResultAutoRg" )
        oStreamString.close()
        return rootObj
    parseString = staticmethod( parseString )
    #Static method for parsing a file
    def parseFile( _inFilePath ):
        doc = minidom.parse(_inFilePath)
        rootNode = doc.documentElement
        rootObj = XSDataResultAutoRg()
        rootObj.build(rootNode)
        return rootObj
    parseFile = staticmethod( parseFile )
# end class XSDataResultAutoRg


class XSDataResultAutoSub(XSDataResult):
    """Result of AutoSub (EDNA implementation) 	"""
    def __init__(self, status=None, autoRg=None, bestBufferType=None, bestBuffer=None, subtractedCurve=None):
        XSDataResult.__init__(self, status)
        if subtractedCurve is None:
            self._subtractedCurve = None
        elif subtractedCurve.__class__.__name__ == "XSDataFile":
            self._subtractedCurve = subtractedCurve
        else:
            strMessage = "ERROR! XSDataResultAutoSub constructor argument 'subtractedCurve' is not XSDataFile but %s" % self._subtractedCurve.__class__.__name__
            raise BaseException(strMessage)
        if bestBuffer is None:
            self._bestBuffer = None
        elif bestBuffer.__class__.__name__ == "XSDataFile":
            self._bestBuffer = bestBuffer
        else:
            strMessage = "ERROR! XSDataResultAutoSub constructor argument 'bestBuffer' is not XSDataFile but %s" % self._bestBuffer.__class__.__name__
            raise BaseException(strMessage)
        if bestBufferType is None:
            self._bestBufferType = None
        elif bestBufferType.__class__.__name__ == "XSDataString":
            self._bestBufferType = bestBufferType
        else:
            strMessage = "ERROR! XSDataResultAutoSub constructor argument 'bestBufferType' is not XSDataString but %s" % self._bestBufferType.__class__.__name__
            raise BaseException(strMessage)
        if autoRg is None:
            self._autoRg = None
        elif autoRg.__class__.__name__ == "XSDataAutoRg":
            self._autoRg = autoRg
        else:
            strMessage = "ERROR! XSDataResultAutoSub constructor argument 'autoRg' is not XSDataAutoRg but %s" % self._autoRg.__class__.__name__
            raise BaseException(strMessage)
    # Methods and properties for the 'subtractedCurve' attribute
    def getSubtractedCurve(self): return self._subtractedCurve
    def setSubtractedCurve(self, subtractedCurve):
        if subtractedCurve is None:
            self._subtractedCurve = None
        elif subtractedCurve.__class__.__name__ == "XSDataFile":
            self._subtractedCurve = subtractedCurve
        else:
            strMessage = "ERROR! XSDataResultAutoSub.setSubtractedCurve argument is not XSDataFile but %s" % subtractedCurve.__class__.__name__
            raise BaseException(strMessage)
    def delSubtractedCurve(self): self._subtractedCurve = None
    subtractedCurve = property(getSubtractedCurve, setSubtractedCurve, delSubtractedCurve, "Property for subtractedCurve")
    # Methods and properties for the 'bestBuffer' attribute
    def getBestBuffer(self): return self._bestBuffer
    def setBestBuffer(self, bestBuffer):
        if bestBuffer is None:
            self._bestBuffer = None
        elif bestBuffer.__class__.__name__ == "XSDataFile":
            self._bestBuffer = bestBuffer
        else:
            strMessage = "ERROR! XSDataResultAutoSub.setBestBuffer argument is not XSDataFile but %s" % bestBuffer.__class__.__name__
            raise BaseException(strMessage)
    def delBestBuffer(self): self._bestBuffer = None
    bestBuffer = property(getBestBuffer, setBestBuffer, delBestBuffer, "Property for bestBuffer")
    # Methods and properties for the 'bestBufferType' attribute
    def getBestBufferType(self): return self._bestBufferType
    def setBestBufferType(self, bestBufferType):
        if bestBufferType is None:
            self._bestBufferType = None
        elif bestBufferType.__class__.__name__ == "XSDataString":
            self._bestBufferType = bestBufferType
        else:
            strMessage = "ERROR! XSDataResultAutoSub.setBestBufferType argument is not XSDataString but %s" % bestBufferType.__class__.__name__
            raise BaseException(strMessage)
    def delBestBufferType(self): self._bestBufferType = None
    bestBufferType = property(getBestBufferType, setBestBufferType, delBestBufferType, "Property for bestBufferType")
    # Methods and properties for the 'autoRg' attribute
    def getAutoRg(self): return self._autoRg
    def setAutoRg(self, autoRg):
        if autoRg is None:
            self._autoRg = None
        elif autoRg.__class__.__name__ == "XSDataAutoRg":
            self._autoRg = autoRg
        else:
            strMessage = "ERROR! XSDataResultAutoSub.setAutoRg argument is not XSDataAutoRg but %s" % autoRg.__class__.__name__
            raise BaseException(strMessage)
    def delAutoRg(self): self._autoRg = None
    autoRg = property(getAutoRg, setAutoRg, delAutoRg, "Property for autoRg")
    def export(self, outfile, level, name_='XSDataResultAutoSub'):
        showIndent(outfile, level)
        outfile.write(unicode('<%s>\n' % name_))
        self.exportChildren(outfile, level + 1, name_)
        showIndent(outfile, level)
        outfile.write(unicode('</%s>\n' % name_))
    def exportChildren(self, outfile, level, name_='XSDataResultAutoSub'):
        XSDataResult.exportChildren(self, outfile, level, name_)
        if self._subtractedCurve is not None:
            self.subtractedCurve.export(outfile, level, name_='subtractedCurve')
        else:
            warnEmptyAttribute("subtractedCurve", "XSDataFile")
        if self._bestBuffer is not None:
            self.bestBuffer.export(outfile, level, name_='bestBuffer')
        else:
            warnEmptyAttribute("bestBuffer", "XSDataFile")
        if self._bestBufferType is not None:
            self.bestBufferType.export(outfile, level, name_='bestBufferType')
        else:
            warnEmptyAttribute("bestBufferType", "XSDataString")
        if self._autoRg is not None:
            self.autoRg.export(outfile, level, name_='autoRg')
        else:
            warnEmptyAttribute("autoRg", "XSDataAutoRg")
    def build(self, node_):
        for child_ in node_.childNodes:
            nodeName_ = child_.nodeName.split(':')[-1]
            self.buildChildren(child_, nodeName_)
    def buildChildren(self, child_, nodeName_):
        if child_.nodeType == Node.ELEMENT_NODE and \
            nodeName_ == 'subtractedCurve':
            obj_ = XSDataFile()
            obj_.build(child_)
            self.setSubtractedCurve(obj_)
        elif child_.nodeType == Node.ELEMENT_NODE and \
            nodeName_ == 'bestBuffer':
            obj_ = XSDataFile()
            obj_.build(child_)
            self.setBestBuffer(obj_)
        elif child_.nodeType == Node.ELEMENT_NODE and \
            nodeName_ == 'bestBufferType':
            obj_ = XSDataString()
            obj_.build(child_)
            self.setBestBufferType(obj_)
        elif child_.nodeType == Node.ELEMENT_NODE and \
            nodeName_ == 'autoRg':
            obj_ = XSDataAutoRg()
            obj_.build(child_)
            self.setAutoRg(obj_)
        XSDataResult.buildChildren(self, child_, nodeName_)
    #Method for marshalling an object
    def marshal( self ):
        oStreamString = StringIO()
        oStreamString.write(unicode('<?xml version="1.0" ?>\n'))
        self.export( oStreamString, 0, name_="XSDataResultAutoSub" )
        oStringXML = oStreamString.getvalue()
        oStreamString.close()
        return oStringXML
    #Only to export the entire XML tree to a file stream on disk
    def exportToFile( self, _outfileName ):
        outfile = open( _outfileName, "w" )
        outfile.write(unicode('<?xml version=\"1.0\" ?>\n'))
        self.export( outfile, 0, name_='XSDataResultAutoSub' )
        outfile.close()
    #Deprecated method, replaced by exportToFile
    def outputFile( self, _outfileName ):
        print("WARNING: Method outputFile in class XSDataResultAutoSub is deprecated, please use instead exportToFile!")
        self.exportToFile(_outfileName)
    #Method for making a copy in a new instance
    def copy( self ):
        return XSDataResultAutoSub.parseString(self.marshal())
    #Static method for parsing a string
    def parseString( _inString ):
        doc = minidom.parseString(_inString)
        rootNode = doc.documentElement
        rootObj = XSDataResultAutoSub()
        rootObj.build(rootNode)
        # Check that all minOccurs are obeyed by marshalling the created object
        oStreamString = StringIO()
        rootObj.export( oStreamString, 0, name_="XSDataResultAutoSub" )
        oStreamString.close()
        return rootObj
    parseString = staticmethod( parseString )
    #Static method for parsing a file
    def parseFile( _inFilePath ):
        doc = minidom.parse(_inFilePath)
        rootNode = doc.documentElement
        rootObj = XSDataResultAutoSub()
        rootObj.build(rootNode)
        return rootObj
    parseFile = staticmethod( parseFile )
# end class XSDataResultAutoSub


class XSDataResultDamaver(XSDataResult):
    def __init__(self, status=None, damstartModel=None, damfiltModel=None, model=None, damstartPdbFile=None, damfilterPdbFile=None, damaverPdbFile=None, variationNSD=None, meanNSD=None):
        XSDataResult.__init__(self, status)
        if meanNSD is None:
            self._meanNSD = None
        elif meanNSD.__class__.__name__ == "XSDataDouble":
            self._meanNSD = meanNSD
        else:
            strMessage = "ERROR! XSDataResultDamaver constructor argument 'meanNSD' is not XSDataDouble but %s" % self._meanNSD.__class__.__name__
            raise BaseException(strMessage)
        if variationNSD is None:
            self._variationNSD = None
        elif variationNSD.__class__.__name__ == "XSDataDouble":
            self._variationNSD = variationNSD
        else:
            strMessage = "ERROR! XSDataResultDamaver constructor argument 'variationNSD' is not XSDataDouble but %s" % self._variationNSD.__class__.__name__
            raise BaseException(strMessage)
        if damaverPdbFile is None:
            self._damaverPdbFile = None
        elif damaverPdbFile.__class__.__name__ == "XSDataFile":
            self._damaverPdbFile = damaverPdbFile
        else:
            strMessage = "ERROR! XSDataResultDamaver constructor argument 'damaverPdbFile' is not XSDataFile but %s" % self._damaverPdbFile.__class__.__name__
            raise BaseException(strMessage)
        if damfilterPdbFile is None:
            self._damfilterPdbFile = None
        elif damfilterPdbFile.__class__.__name__ == "XSDataFile":
            self._damfilterPdbFile = damfilterPdbFile
        else:
            strMessage = "ERROR! XSDataResultDamaver constructor argument 'damfilterPdbFile' is not XSDataFile but %s" % self._damfilterPdbFile.__class__.__name__
            raise BaseException(strMessage)
        if damstartPdbFile is None:
            self._damstartPdbFile = None
        elif damstartPdbFile.__class__.__name__ == "XSDataFile":
            self._damstartPdbFile = damstartPdbFile
        else:
            strMessage = "ERROR! XSDataResultDamaver constructor argument 'damstartPdbFile' is not XSDataFile but %s" % self._damstartPdbFile.__class__.__name__
            raise BaseException(strMessage)
        if model is None:
            self._model = None
        elif model.__class__.__name__ == "XSDataSaxsModel":
            self._model = model
        else:
            strMessage = "ERROR! XSDataResultDamaver constructor argument 'model' is not XSDataSaxsModel but %s" % self._model.__class__.__name__
            raise BaseException(strMessage)
        if damfiltModel is None:
            self._damfiltModel = None
        elif damfiltModel.__class__.__name__ == "XSDataSaxsModel":
            self._damfiltModel = damfiltModel
        else:
            strMessage = "ERROR! XSDataResultDamaver constructor argument 'damfiltModel' is not XSDataSaxsModel but %s" % self._damfiltModel.__class__.__name__
            raise BaseException(strMessage)
        if damstartModel is None:
            self._damstartModel = None
        elif damstartModel.__class__.__name__ == "XSDataSaxsModel":
            self._damstartModel = damstartModel
        else:
            strMessage = "ERROR! XSDataResultDamaver constructor argument 'damstartModel' is not XSDataSaxsModel but %s" % self._damstartModel.__class__.__name__
            raise BaseException(strMessage)
    # Methods and properties for the 'meanNSD' attribute
    def getMeanNSD(self): return self._meanNSD
    def setMeanNSD(self, meanNSD):
        if meanNSD is None:
            self._meanNSD = None
        elif meanNSD.__class__.__name__ == "XSDataDouble":
            self._meanNSD = meanNSD
        else:
            strMessage = "ERROR! XSDataResultDamaver.setMeanNSD argument is not XSDataDouble but %s" % meanNSD.__class__.__name__
            raise BaseException(strMessage)
    def delMeanNSD(self): self._meanNSD = None
    meanNSD = property(getMeanNSD, setMeanNSD, delMeanNSD, "Property for meanNSD")
    # Methods and properties for the 'variationNSD' attribute
    def getVariationNSD(self): return self._variationNSD
    def setVariationNSD(self, variationNSD):
        if variationNSD is None:
            self._variationNSD = None
        elif variationNSD.__class__.__name__ == "XSDataDouble":
            self._variationNSD = variationNSD
        else:
            strMessage = "ERROR! XSDataResultDamaver.setVariationNSD argument is not XSDataDouble but %s" % variationNSD.__class__.__name__
            raise BaseException(strMessage)
    def delVariationNSD(self): self._variationNSD = None
    variationNSD = property(getVariationNSD, setVariationNSD, delVariationNSD, "Property for variationNSD")
    # Methods and properties for the 'damaverPdbFile' attribute
    def getDamaverPdbFile(self): return self._damaverPdbFile
    def setDamaverPdbFile(self, damaverPdbFile):
        if damaverPdbFile is None:
            self._damaverPdbFile = None
        elif damaverPdbFile.__class__.__name__ == "XSDataFile":
            self._damaverPdbFile = damaverPdbFile
        else:
            strMessage = "ERROR! XSDataResultDamaver.setDamaverPdbFile argument is not XSDataFile but %s" % damaverPdbFile.__class__.__name__
            raise BaseException(strMessage)
    def delDamaverPdbFile(self): self._damaverPdbFile = None
    damaverPdbFile = property(getDamaverPdbFile, setDamaverPdbFile, delDamaverPdbFile, "Property for damaverPdbFile")
    # Methods and properties for the 'damfilterPdbFile' attribute
    def getDamfilterPdbFile(self): return self._damfilterPdbFile
    def setDamfilterPdbFile(self, damfilterPdbFile):
        if damfilterPdbFile is None:
            self._damfilterPdbFile = None
        elif damfilterPdbFile.__class__.__name__ == "XSDataFile":
            self._damfilterPdbFile = damfilterPdbFile
        else:
            strMessage = "ERROR! XSDataResultDamaver.setDamfilterPdbFile argument is not XSDataFile but %s" % damfilterPdbFile.__class__.__name__
            raise BaseException(strMessage)
    def delDamfilterPdbFile(self): self._damfilterPdbFile = None
    damfilterPdbFile = property(getDamfilterPdbFile, setDamfilterPdbFile, delDamfilterPdbFile, "Property for damfilterPdbFile")
    # Methods and properties for the 'damstartPdbFile' attribute
    def getDamstartPdbFile(self): return self._damstartPdbFile
    def setDamstartPdbFile(self, damstartPdbFile):
        if damstartPdbFile is None:
            self._damstartPdbFile = None
        elif damstartPdbFile.__class__.__name__ == "XSDataFile":
            self._damstartPdbFile = damstartPdbFile
        else:
            strMessage = "ERROR! XSDataResultDamaver.setDamstartPdbFile argument is not XSDataFile but %s" % damstartPdbFile.__class__.__name__
            raise BaseException(strMessage)
    def delDamstartPdbFile(self): self._damstartPdbFile = None
    damstartPdbFile = property(getDamstartPdbFile, setDamstartPdbFile, delDamstartPdbFile, "Property for damstartPdbFile")
    # Methods and properties for the 'model' attribute
    def getModel(self): return self._model
    def setModel(self, model):
        if model is None:
            self._model = None
        elif model.__class__.__name__ == "XSDataSaxsModel":
            self._model = model
        else:
            strMessage = "ERROR! XSDataResultDamaver.setModel argument is not XSDataSaxsModel but %s" % model.__class__.__name__
            raise BaseException(strMessage)
    def delModel(self): self._model = None
    model = property(getModel, setModel, delModel, "Property for model")
    # Methods and properties for the 'damfiltModel' attribute
    def getDamfiltModel(self): return self._damfiltModel
    def setDamfiltModel(self, damfiltModel):
        if damfiltModel is None:
            self._damfiltModel = None
        elif damfiltModel.__class__.__name__ == "XSDataSaxsModel":
            self._damfiltModel = damfiltModel
        else:
            strMessage = "ERROR! XSDataResultDamaver.setDamfiltModel argument is not XSDataSaxsModel but %s" % damfiltModel.__class__.__name__
            raise BaseException(strMessage)
    def delDamfiltModel(self): self._damfiltModel = None
    damfiltModel = property(getDamfiltModel, setDamfiltModel, delDamfiltModel, "Property for damfiltModel")
    # Methods and properties for the 'damstartModel' attribute
    def getDamstartModel(self): return self._damstartModel
    def setDamstartModel(self, damstartModel):
        if damstartModel is None:
            self._damstartModel = None
        elif damstartModel.__class__.__name__ == "XSDataSaxsModel":
            self._damstartModel = damstartModel
        else:
            strMessage = "ERROR! XSDataResultDamaver.setDamstartModel argument is not XSDataSaxsModel but %s" % damstartModel.__class__.__name__
            raise BaseException(strMessage)
    def delDamstartModel(self): self._damstartModel = None
    damstartModel = property(getDamstartModel, setDamstartModel, delDamstartModel, "Property for damstartModel")
    def export(self, outfile, level, name_='XSDataResultDamaver'):
        showIndent(outfile, level)
        outfile.write(unicode('<%s>\n' % name_))
        self.exportChildren(outfile, level + 1, name_)
        showIndent(outfile, level)
        outfile.write(unicode('</%s>\n' % name_))
    def exportChildren(self, outfile, level, name_='XSDataResultDamaver'):
        XSDataResult.exportChildren(self, outfile, level, name_)
        if self._meanNSD is not None:
            self.meanNSD.export(outfile, level, name_='meanNSD')
        if self._variationNSD is not None:
            self.variationNSD.export(outfile, level, name_='variationNSD')
        if self._damaverPdbFile is not None:
            self.damaverPdbFile.export(outfile, level, name_='damaverPdbFile')
        if self._damfilterPdbFile is not None:
            self.damfilterPdbFile.export(outfile, level, name_='damfilterPdbFile')
        if self._damstartPdbFile is not None:
            self.damstartPdbFile.export(outfile, level, name_='damstartPdbFile')
        if self._model is not None:
            self.model.export(outfile, level, name_='model')
        if self._damfiltModel is not None:
            self.damfiltModel.export(outfile, level, name_='damfiltModel')
        if self._damstartModel is not None:
            self.damstartModel.export(outfile, level, name_='damstartModel')
    def build(self, node_):
        for child_ in node_.childNodes:
            nodeName_ = child_.nodeName.split(':')[-1]
            self.buildChildren(child_, nodeName_)
    def buildChildren(self, child_, nodeName_):
        if child_.nodeType == Node.ELEMENT_NODE and \
            nodeName_ == 'meanNSD':
            obj_ = XSDataDouble()
            obj_.build(child_)
            self.setMeanNSD(obj_)
        elif child_.nodeType == Node.ELEMENT_NODE and \
            nodeName_ == 'variationNSD':
            obj_ = XSDataDouble()
            obj_.build(child_)
            self.setVariationNSD(obj_)
        elif child_.nodeType == Node.ELEMENT_NODE and \
            nodeName_ == 'damaverPdbFile':
            obj_ = XSDataFile()
            obj_.build(child_)
            self.setDamaverPdbFile(obj_)
        elif child_.nodeType == Node.ELEMENT_NODE and \
            nodeName_ == 'damfilterPdbFile':
            obj_ = XSDataFile()
            obj_.build(child_)
            self.setDamfilterPdbFile(obj_)
        elif child_.nodeType == Node.ELEMENT_NODE and \
            nodeName_ == 'damstartPdbFile':
            obj_ = XSDataFile()
            obj_.build(child_)
            self.setDamstartPdbFile(obj_)
        elif child_.nodeType == Node.ELEMENT_NODE and \
            nodeName_ == 'model':
            obj_ = XSDataSaxsModel()
            obj_.build(child_)
            self.setModel(obj_)
        elif child_.nodeType == Node.ELEMENT_NODE and \
            nodeName_ == 'damfiltModel':
            obj_ = XSDataSaxsModel()
            obj_.build(child_)
            self.setDamfiltModel(obj_)
        elif child_.nodeType == Node.ELEMENT_NODE and \
            nodeName_ == 'damstartModel':
            obj_ = XSDataSaxsModel()
            obj_.build(child_)
            self.setDamstartModel(obj_)
        XSDataResult.buildChildren(self, child_, nodeName_)
    #Method for marshalling an object
    def marshal( self ):
        oStreamString = StringIO()
        oStreamString.write(unicode('<?xml version="1.0" ?>\n'))
        self.export( oStreamString, 0, name_="XSDataResultDamaver" )
        oStringXML = oStreamString.getvalue()
        oStreamString.close()
        return oStringXML
    #Only to export the entire XML tree to a file stream on disk
    def exportToFile( self, _outfileName ):
        outfile = open( _outfileName, "w" )
        outfile.write(unicode('<?xml version=\"1.0\" ?>\n'))
        self.export( outfile, 0, name_='XSDataResultDamaver' )
        outfile.close()
    #Deprecated method, replaced by exportToFile
    def outputFile( self, _outfileName ):
        print("WARNING: Method outputFile in class XSDataResultDamaver is deprecated, please use instead exportToFile!")
        self.exportToFile(_outfileName)
    #Method for making a copy in a new instance
    def copy( self ):
        return XSDataResultDamaver.parseString(self.marshal())
    #Static method for parsing a string
    def parseString( _inString ):
        doc = minidom.parseString(_inString)
        rootNode = doc.documentElement
        rootObj = XSDataResultDamaver()
        rootObj.build(rootNode)
        # Check that all minOccurs are obeyed by marshalling the created object
        oStreamString = StringIO()
        rootObj.export( oStreamString, 0, name_="XSDataResultDamaver" )
        oStreamString.close()
        return rootObj
    parseString = staticmethod( parseString )
    #Static method for parsing a file
    def parseFile( _inFilePath ):
        doc = minidom.parse(_inFilePath)
        rootNode = doc.documentElement
        rootObj = XSDataResultDamaver()
        rootObj.build(rootNode)
        return rootObj
    parseFile = staticmethod( parseFile )
# end class XSDataResultDamaver


class XSDataResultDamfilt(XSDataResult):
    def __init__(self, status=None, model=None, outputPdbFile=None):
        XSDataResult.__init__(self, status)
        if outputPdbFile is None:
            self._outputPdbFile = None
        elif outputPdbFile.__class__.__name__ == "XSDataFile":
            self._outputPdbFile = outputPdbFile
        else:
            strMessage = "ERROR! XSDataResultDamfilt constructor argument 'outputPdbFile' is not XSDataFile but %s" % self._outputPdbFile.__class__.__name__
            raise BaseException(strMessage)
        if model is None:
            self._model = None
        elif model.__class__.__name__ == "XSDataSaxsModel":
            self._model = model
        else:
            strMessage = "ERROR! XSDataResultDamfilt constructor argument 'model' is not XSDataSaxsModel but %s" % self._model.__class__.__name__
            raise BaseException(strMessage)
    # Methods and properties for the 'outputPdbFile' attribute
    def getOutputPdbFile(self): return self._outputPdbFile
    def setOutputPdbFile(self, outputPdbFile):
        if outputPdbFile is None:
            self._outputPdbFile = None
        elif outputPdbFile.__class__.__name__ == "XSDataFile":
            self._outputPdbFile = outputPdbFile
        else:
            strMessage = "ERROR! XSDataResultDamfilt.setOutputPdbFile argument is not XSDataFile but %s" % outputPdbFile.__class__.__name__
            raise BaseException(strMessage)
    def delOutputPdbFile(self): self._outputPdbFile = None
    outputPdbFile = property(getOutputPdbFile, setOutputPdbFile, delOutputPdbFile, "Property for outputPdbFile")
    # Methods and properties for the 'model' attribute
    def getModel(self): return self._model
    def setModel(self, model):
        if model is None:
            self._model = None
        elif model.__class__.__name__ == "XSDataSaxsModel":
            self._model = model
        else:
            strMessage = "ERROR! XSDataResultDamfilt.setModel argument is not XSDataSaxsModel but %s" % model.__class__.__name__
            raise BaseException(strMessage)
    def delModel(self): self._model = None
    model = property(getModel, setModel, delModel, "Property for model")
    def export(self, outfile, level, name_='XSDataResultDamfilt'):
        showIndent(outfile, level)
        outfile.write(unicode('<%s>\n' % name_))
        self.exportChildren(outfile, level + 1, name_)
        showIndent(outfile, level)
        outfile.write(unicode('</%s>\n' % name_))
    def exportChildren(self, outfile, level, name_='XSDataResultDamfilt'):
        XSDataResult.exportChildren(self, outfile, level, name_)
        if self._outputPdbFile is not None:
            self.outputPdbFile.export(outfile, level, name_='outputPdbFile')
        if self._model is not None:
            self.model.export(outfile, level, name_='model')
    def build(self, node_):
        for child_ in node_.childNodes:
            nodeName_ = child_.nodeName.split(':')[-1]
            self.buildChildren(child_, nodeName_)
    def buildChildren(self, child_, nodeName_):
        if child_.nodeType == Node.ELEMENT_NODE and \
            nodeName_ == 'outputPdbFile':
            obj_ = XSDataFile()
            obj_.build(child_)
            self.setOutputPdbFile(obj_)
        elif child_.nodeType == Node.ELEMENT_NODE and \
            nodeName_ == 'model':
            obj_ = XSDataSaxsModel()
            obj_.build(child_)
            self.setModel(obj_)
        XSDataResult.buildChildren(self, child_, nodeName_)
    #Method for marshalling an object
    def marshal( self ):
        oStreamString = StringIO()
        oStreamString.write(unicode('<?xml version="1.0" ?>\n'))
        self.export( oStreamString, 0, name_="XSDataResultDamfilt" )
        oStringXML = oStreamString.getvalue()
        oStreamString.close()
        return oStringXML
    #Only to export the entire XML tree to a file stream on disk
    def exportToFile( self, _outfileName ):
        outfile = open( _outfileName, "w" )
        outfile.write(unicode('<?xml version=\"1.0\" ?>\n'))
        self.export( outfile, 0, name_='XSDataResultDamfilt' )
        outfile.close()
    #Deprecated method, replaced by exportToFile
    def outputFile( self, _outfileName ):
        print("WARNING: Method outputFile in class XSDataResultDamfilt is deprecated, please use instead exportToFile!")
        self.exportToFile(_outfileName)
    #Method for making a copy in a new instance
    def copy( self ):
        return XSDataResultDamfilt.parseString(self.marshal())
    #Static method for parsing a string
    def parseString( _inString ):
        doc = minidom.parseString(_inString)
        rootNode = doc.documentElement
        rootObj = XSDataResultDamfilt()
        rootObj.build(rootNode)
        # Check that all minOccurs are obeyed by marshalling the created object
        oStreamString = StringIO()
        rootObj.export( oStreamString, 0, name_="XSDataResultDamfilt" )
        oStreamString.close()
        return rootObj
    parseString = staticmethod( parseString )
    #Static method for parsing a file
    def parseFile( _inFilePath ):
        doc = minidom.parse(_inFilePath)
        rootNode = doc.documentElement
        rootObj = XSDataResultDamfilt()
        rootObj.build(rootNode)
        return rootObj
    parseFile = staticmethod( parseFile )
# end class XSDataResultDamfilt


class XSDataResultDammif(XSDataResult):
    def __init__(self, status=None, model=None, chiSqrt=None, rfactor=None, pdbSolventFile=None, pdbMoleculeFile=None, logFile=None, fitFile=None):
        XSDataResult.__init__(self, status)
        if fitFile is None:
            self._fitFile = None
        elif fitFile.__class__.__name__ == "XSDataFile":
            self._fitFile = fitFile
        else:
            strMessage = "ERROR! XSDataResultDammif constructor argument 'fitFile' is not XSDataFile but %s" % self._fitFile.__class__.__name__
            raise BaseException(strMessage)
        if logFile is None:
            self._logFile = None
        elif logFile.__class__.__name__ == "XSDataFile":
            self._logFile = logFile
        else:
            strMessage = "ERROR! XSDataResultDammif constructor argument 'logFile' is not XSDataFile but %s" % self._logFile.__class__.__name__
            raise BaseException(strMessage)
        if pdbMoleculeFile is None:
            self._pdbMoleculeFile = None
        elif pdbMoleculeFile.__class__.__name__ == "XSDataFile":
            self._pdbMoleculeFile = pdbMoleculeFile
        else:
            strMessage = "ERROR! XSDataResultDammif constructor argument 'pdbMoleculeFile' is not XSDataFile but %s" % self._pdbMoleculeFile.__class__.__name__
            raise BaseException(strMessage)
        if pdbSolventFile is None:
            self._pdbSolventFile = None
        elif pdbSolventFile.__class__.__name__ == "XSDataFile":
            self._pdbSolventFile = pdbSolventFile
        else:
            strMessage = "ERROR! XSDataResultDammif constructor argument 'pdbSolventFile' is not XSDataFile but %s" % self._pdbSolventFile.__class__.__name__
            raise BaseException(strMessage)
        if rfactor is None:
            self._rfactor = None
        elif rfactor.__class__.__name__ == "XSDataDouble":
            self._rfactor = rfactor
        else:
            strMessage = "ERROR! XSDataResultDammif constructor argument 'rfactor' is not XSDataDouble but %s" % self._rfactor.__class__.__name__
            raise BaseException(strMessage)
        if chiSqrt is None:
            self._chiSqrt = None
        elif chiSqrt.__class__.__name__ == "XSDataDouble":
            self._chiSqrt = chiSqrt
        else:
            strMessage = "ERROR! XSDataResultDammif constructor argument 'chiSqrt' is not XSDataDouble but %s" % self._chiSqrt.__class__.__name__
            raise BaseException(strMessage)
        if model is None:
            self._model = None
        elif model.__class__.__name__ == "XSDataSaxsModel":
            self._model = model
        else:
            strMessage = "ERROR! XSDataResultDammif constructor argument 'model' is not XSDataSaxsModel but %s" % self._model.__class__.__name__
            raise BaseException(strMessage)
    # Methods and properties for the 'fitFile' attribute
    def getFitFile(self): return self._fitFile
    def setFitFile(self, fitFile):
        if fitFile is None:
            self._fitFile = None
        elif fitFile.__class__.__name__ == "XSDataFile":
            self._fitFile = fitFile
        else:
            strMessage = "ERROR! XSDataResultDammif.setFitFile argument is not XSDataFile but %s" % fitFile.__class__.__name__
            raise BaseException(strMessage)
    def delFitFile(self): self._fitFile = None
    fitFile = property(getFitFile, setFitFile, delFitFile, "Property for fitFile")
    # Methods and properties for the 'logFile' attribute
    def getLogFile(self): return self._logFile
    def setLogFile(self, logFile):
        if logFile is None:
            self._logFile = None
        elif logFile.__class__.__name__ == "XSDataFile":
            self._logFile = logFile
        else:
            strMessage = "ERROR! XSDataResultDammif.setLogFile argument is not XSDataFile but %s" % logFile.__class__.__name__
            raise BaseException(strMessage)
    def delLogFile(self): self._logFile = None
    logFile = property(getLogFile, setLogFile, delLogFile, "Property for logFile")
    # Methods and properties for the 'pdbMoleculeFile' attribute
    def getPdbMoleculeFile(self): return self._pdbMoleculeFile
    def setPdbMoleculeFile(self, pdbMoleculeFile):
        if pdbMoleculeFile is None:
            self._pdbMoleculeFile = None
        elif pdbMoleculeFile.__class__.__name__ == "XSDataFile":
            self._pdbMoleculeFile = pdbMoleculeFile
        else:
            strMessage = "ERROR! XSDataResultDammif.setPdbMoleculeFile argument is not XSDataFile but %s" % pdbMoleculeFile.__class__.__name__
            raise BaseException(strMessage)
    def delPdbMoleculeFile(self): self._pdbMoleculeFile = None
    pdbMoleculeFile = property(getPdbMoleculeFile, setPdbMoleculeFile, delPdbMoleculeFile, "Property for pdbMoleculeFile")
    # Methods and properties for the 'pdbSolventFile' attribute
    def getPdbSolventFile(self): return self._pdbSolventFile
    def setPdbSolventFile(self, pdbSolventFile):
        if pdbSolventFile is None:
            self._pdbSolventFile = None
        elif pdbSolventFile.__class__.__name__ == "XSDataFile":
            self._pdbSolventFile = pdbSolventFile
        else:
            strMessage = "ERROR! XSDataResultDammif.setPdbSolventFile argument is not XSDataFile but %s" % pdbSolventFile.__class__.__name__
            raise BaseException(strMessage)
    def delPdbSolventFile(self): self._pdbSolventFile = None
    pdbSolventFile = property(getPdbSolventFile, setPdbSolventFile, delPdbSolventFile, "Property for pdbSolventFile")
    # Methods and properties for the 'rfactor' attribute
    def getRfactor(self): return self._rfactor
    def setRfactor(self, rfactor):
        if rfactor is None:
            self._rfactor = None
        elif rfactor.__class__.__name__ == "XSDataDouble":
            self._rfactor = rfactor
        else:
            strMessage = "ERROR! XSDataResultDammif.setRfactor argument is not XSDataDouble but %s" % rfactor.__class__.__name__
            raise BaseException(strMessage)
    def delRfactor(self): self._rfactor = None
    rfactor = property(getRfactor, setRfactor, delRfactor, "Property for rfactor")
    # Methods and properties for the 'chiSqrt' attribute
    def getChiSqrt(self): return self._chiSqrt
    def setChiSqrt(self, chiSqrt):
        if chiSqrt is None:
            self._chiSqrt = None
        elif chiSqrt.__class__.__name__ == "XSDataDouble":
            self._chiSqrt = chiSqrt
        else:
            strMessage = "ERROR! XSDataResultDammif.setChiSqrt argument is not XSDataDouble but %s" % chiSqrt.__class__.__name__
            raise BaseException(strMessage)
    def delChiSqrt(self): self._chiSqrt = None
    chiSqrt = property(getChiSqrt, setChiSqrt, delChiSqrt, "Property for chiSqrt")
    # Methods and properties for the 'model' attribute
    def getModel(self): return self._model
    def setModel(self, model):
        if model is None:
            self._model = None
        elif model.__class__.__name__ == "XSDataSaxsModel":
            self._model = model
        else:
            strMessage = "ERROR! XSDataResultDammif.setModel argument is not XSDataSaxsModel but %s" % model.__class__.__name__
            raise BaseException(strMessage)
    def delModel(self): self._model = None
    model = property(getModel, setModel, delModel, "Property for model")
    def export(self, outfile, level, name_='XSDataResultDammif'):
        showIndent(outfile, level)
        outfile.write(unicode('<%s>\n' % name_))
        self.exportChildren(outfile, level + 1, name_)
        showIndent(outfile, level)
        outfile.write(unicode('</%s>\n' % name_))
    def exportChildren(self, outfile, level, name_='XSDataResultDammif'):
        XSDataResult.exportChildren(self, outfile, level, name_)
        if self._fitFile is not None:
            self.fitFile.export(outfile, level, name_='fitFile')
        else:
            warnEmptyAttribute("fitFile", "XSDataFile")
        if self._logFile is not None:
            self.logFile.export(outfile, level, name_='logFile')
        else:
            warnEmptyAttribute("logFile", "XSDataFile")
        if self._pdbMoleculeFile is not None:
            self.pdbMoleculeFile.export(outfile, level, name_='pdbMoleculeFile')
        else:
            warnEmptyAttribute("pdbMoleculeFile", "XSDataFile")
        if self._pdbSolventFile is not None:
            self.pdbSolventFile.export(outfile, level, name_='pdbSolventFile')
        else:
            warnEmptyAttribute("pdbSolventFile", "XSDataFile")
        if self._rfactor is not None:
            self.rfactor.export(outfile, level, name_='rfactor')
        if self._chiSqrt is not None:
            self.chiSqrt.export(outfile, level, name_='chiSqrt')
        if self._model is not None:
            self.model.export(outfile, level, name_='model')
        else:
            warnEmptyAttribute("model", "XSDataSaxsModel")
    def build(self, node_):
        for child_ in node_.childNodes:
            nodeName_ = child_.nodeName.split(':')[-1]
            self.buildChildren(child_, nodeName_)
    def buildChildren(self, child_, nodeName_):
        if child_.nodeType == Node.ELEMENT_NODE and \
            nodeName_ == 'fitFile':
            obj_ = XSDataFile()
            obj_.build(child_)
            self.setFitFile(obj_)
        elif child_.nodeType == Node.ELEMENT_NODE and \
            nodeName_ == 'logFile':
            obj_ = XSDataFile()
            obj_.build(child_)
            self.setLogFile(obj_)
        elif child_.nodeType == Node.ELEMENT_NODE and \
            nodeName_ == 'pdbMoleculeFile':
            obj_ = XSDataFile()
            obj_.build(child_)
            self.setPdbMoleculeFile(obj_)
        elif child_.nodeType == Node.ELEMENT_NODE and \
            nodeName_ == 'pdbSolventFile':
            obj_ = XSDataFile()
            obj_.build(child_)
            self.setPdbSolventFile(obj_)
        elif child_.nodeType == Node.ELEMENT_NODE and \
            nodeName_ == 'rfactor':
            obj_ = XSDataDouble()
            obj_.build(child_)
            self.setRfactor(obj_)
        elif child_.nodeType == Node.ELEMENT_NODE and \
            nodeName_ == 'chiSqrt':
            obj_ = XSDataDouble()
            obj_.build(child_)
            self.setChiSqrt(obj_)
        elif child_.nodeType == Node.ELEMENT_NODE and \
            nodeName_ == 'model':
            obj_ = XSDataSaxsModel()
            obj_.build(child_)
            self.setModel(obj_)
        XSDataResult.buildChildren(self, child_, nodeName_)
    #Method for marshalling an object
    def marshal( self ):
        oStreamString = StringIO()
        oStreamString.write(unicode('<?xml version="1.0" ?>\n'))
        self.export( oStreamString, 0, name_="XSDataResultDammif" )
        oStringXML = oStreamString.getvalue()
        oStreamString.close()
        return oStringXML
    #Only to export the entire XML tree to a file stream on disk
    def exportToFile( self, _outfileName ):
        outfile = open( _outfileName, "w" )
        outfile.write(unicode('<?xml version=\"1.0\" ?>\n'))
        self.export( outfile, 0, name_='XSDataResultDammif' )
        outfile.close()
    #Deprecated method, replaced by exportToFile
    def outputFile( self, _outfileName ):
        print("WARNING: Method outputFile in class XSDataResultDammif is deprecated, please use instead exportToFile!")
        self.exportToFile(_outfileName)
    #Method for making a copy in a new instance
    def copy( self ):
        return XSDataResultDammif.parseString(self.marshal())
    #Static method for parsing a string
    def parseString( _inString ):
        doc = minidom.parseString(_inString)
        rootNode = doc.documentElement
        rootObj = XSDataResultDammif()
        rootObj.build(rootNode)
        # Check that all minOccurs are obeyed by marshalling the created object
        oStreamString = StringIO()
        rootObj.export( oStreamString, 0, name_="XSDataResultDammif" )
        oStreamString.close()
        return rootObj
    parseString = staticmethod( parseString )
    #Static method for parsing a file
    def parseFile( _inFilePath ):
        doc = minidom.parse(_inFilePath)
        rootNode = doc.documentElement
        rootObj = XSDataResultDammif()
        rootObj.build(rootNode)
        return rootObj
    parseFile = staticmethod( parseFile )
# end class XSDataResultDammif


class XSDataResultDammin(XSDataResult):
    def __init__(self, status=None, model=None, chiSqrt=None, rfactor=None, pdbSolventFile=None, pdbMoleculeFile=None, logFile=None, fitFile=None):
        XSDataResult.__init__(self, status)
        if fitFile is None:
            self._fitFile = None
        elif fitFile.__class__.__name__ == "XSDataFile":
            self._fitFile = fitFile
        else:
            strMessage = "ERROR! XSDataResultDammin constructor argument 'fitFile' is not XSDataFile but %s" % self._fitFile.__class__.__name__
            raise BaseException(strMessage)
        if logFile is None:
            self._logFile = None
        elif logFile.__class__.__name__ == "XSDataFile":
            self._logFile = logFile
        else:
            strMessage = "ERROR! XSDataResultDammin constructor argument 'logFile' is not XSDataFile but %s" % self._logFile.__class__.__name__
            raise BaseException(strMessage)
        if pdbMoleculeFile is None:
            self._pdbMoleculeFile = None
        elif pdbMoleculeFile.__class__.__name__ == "XSDataFile":
            self._pdbMoleculeFile = pdbMoleculeFile
        else:
            strMessage = "ERROR! XSDataResultDammin constructor argument 'pdbMoleculeFile' is not XSDataFile but %s" % self._pdbMoleculeFile.__class__.__name__
            raise BaseException(strMessage)
        if pdbSolventFile is None:
            self._pdbSolventFile = None
        elif pdbSolventFile.__class__.__name__ == "XSDataFile":
            self._pdbSolventFile = pdbSolventFile
        else:
            strMessage = "ERROR! XSDataResultDammin constructor argument 'pdbSolventFile' is not XSDataFile but %s" % self._pdbSolventFile.__class__.__name__
            raise BaseException(strMessage)
        if rfactor is None:
            self._rfactor = None
        elif rfactor.__class__.__name__ == "XSDataDouble":
            self._rfactor = rfactor
        else:
            strMessage = "ERROR! XSDataResultDammin constructor argument 'rfactor' is not XSDataDouble but %s" % self._rfactor.__class__.__name__
            raise BaseException(strMessage)
        if chiSqrt is None:
            self._chiSqrt = None
        elif chiSqrt.__class__.__name__ == "XSDataDouble":
            self._chiSqrt = chiSqrt
        else:
            strMessage = "ERROR! XSDataResultDammin constructor argument 'chiSqrt' is not XSDataDouble but %s" % self._chiSqrt.__class__.__name__
            raise BaseException(strMessage)
        if model is None:
            self._model = None
        elif model.__class__.__name__ == "XSDataSaxsModel":
            self._model = model
        else:
            strMessage = "ERROR! XSDataResultDammin constructor argument 'model' is not XSDataSaxsModel but %s" % self._model.__class__.__name__
            raise BaseException(strMessage)
    # Methods and properties for the 'fitFile' attribute
    def getFitFile(self): return self._fitFile
    def setFitFile(self, fitFile):
        if fitFile is None:
            self._fitFile = None
        elif fitFile.__class__.__name__ == "XSDataFile":
            self._fitFile = fitFile
        else:
            strMessage = "ERROR! XSDataResultDammin.setFitFile argument is not XSDataFile but %s" % fitFile.__class__.__name__
            raise BaseException(strMessage)
    def delFitFile(self): self._fitFile = None
    fitFile = property(getFitFile, setFitFile, delFitFile, "Property for fitFile")
    # Methods and properties for the 'logFile' attribute
    def getLogFile(self): return self._logFile
    def setLogFile(self, logFile):
        if logFile is None:
            self._logFile = None
        elif logFile.__class__.__name__ == "XSDataFile":
            self._logFile = logFile
        else:
            strMessage = "ERROR! XSDataResultDammin.setLogFile argument is not XSDataFile but %s" % logFile.__class__.__name__
            raise BaseException(strMessage)
    def delLogFile(self): self._logFile = None
    logFile = property(getLogFile, setLogFile, delLogFile, "Property for logFile")
    # Methods and properties for the 'pdbMoleculeFile' attribute
    def getPdbMoleculeFile(self): return self._pdbMoleculeFile
    def setPdbMoleculeFile(self, pdbMoleculeFile):
        if pdbMoleculeFile is None:
            self._pdbMoleculeFile = None
        elif pdbMoleculeFile.__class__.__name__ == "XSDataFile":
            self._pdbMoleculeFile = pdbMoleculeFile
        else:
            strMessage = "ERROR! XSDataResultDammin.setPdbMoleculeFile argument is not XSDataFile but %s" % pdbMoleculeFile.__class__.__name__
            raise BaseException(strMessage)
    def delPdbMoleculeFile(self): self._pdbMoleculeFile = None
    pdbMoleculeFile = property(getPdbMoleculeFile, setPdbMoleculeFile, delPdbMoleculeFile, "Property for pdbMoleculeFile")
    # Methods and properties for the 'pdbSolventFile' attribute
    def getPdbSolventFile(self): return self._pdbSolventFile
    def setPdbSolventFile(self, pdbSolventFile):
        if pdbSolventFile is None:
            self._pdbSolventFile = None
        elif pdbSolventFile.__class__.__name__ == "XSDataFile":
            self._pdbSolventFile = pdbSolventFile
        else:
            strMessage = "ERROR! XSDataResultDammin.setPdbSolventFile argument is not XSDataFile but %s" % pdbSolventFile.__class__.__name__
            raise BaseException(strMessage)
    def delPdbSolventFile(self): self._pdbSolventFile = None
    pdbSolventFile = property(getPdbSolventFile, setPdbSolventFile, delPdbSolventFile, "Property for pdbSolventFile")
    # Methods and properties for the 'rfactor' attribute
    def getRfactor(self): return self._rfactor
    def setRfactor(self, rfactor):
        if rfactor is None:
            self._rfactor = None
        elif rfactor.__class__.__name__ == "XSDataDouble":
            self._rfactor = rfactor
        else:
            strMessage = "ERROR! XSDataResultDammin.setRfactor argument is not XSDataDouble but %s" % rfactor.__class__.__name__
            raise BaseException(strMessage)
    def delRfactor(self): self._rfactor = None
    rfactor = property(getRfactor, setRfactor, delRfactor, "Property for rfactor")
    # Methods and properties for the 'chiSqrt' attribute
    def getChiSqrt(self): return self._chiSqrt
    def setChiSqrt(self, chiSqrt):
        if chiSqrt is None:
            self._chiSqrt = None
        elif chiSqrt.__class__.__name__ == "XSDataDouble":
            self._chiSqrt = chiSqrt
        else:
            strMessage = "ERROR! XSDataResultDammin.setChiSqrt argument is not XSDataDouble but %s" % chiSqrt.__class__.__name__
            raise BaseException(strMessage)
    def delChiSqrt(self): self._chiSqrt = None
    chiSqrt = property(getChiSqrt, setChiSqrt, delChiSqrt, "Property for chiSqrt")
    # Methods and properties for the 'model' attribute
    def getModel(self): return self._model
    def setModel(self, model):
        if model is None:
            self._model = None
        elif model.__class__.__name__ == "XSDataSaxsModel":
            self._model = model
        else:
            strMessage = "ERROR! XSDataResultDammin.setModel argument is not XSDataSaxsModel but %s" % model.__class__.__name__
            raise BaseException(strMessage)
    def delModel(self): self._model = None
    model = property(getModel, setModel, delModel, "Property for model")
    def export(self, outfile, level, name_='XSDataResultDammin'):
        showIndent(outfile, level)
        outfile.write(unicode('<%s>\n' % name_))
        self.exportChildren(outfile, level + 1, name_)
        showIndent(outfile, level)
        outfile.write(unicode('</%s>\n' % name_))
    def exportChildren(self, outfile, level, name_='XSDataResultDammin'):
        XSDataResult.exportChildren(self, outfile, level, name_)
        if self._fitFile is not None:
            self.fitFile.export(outfile, level, name_='fitFile')
        else:
            warnEmptyAttribute("fitFile", "XSDataFile")
        if self._logFile is not None:
            self.logFile.export(outfile, level, name_='logFile')
        else:
            warnEmptyAttribute("logFile", "XSDataFile")
        if self._pdbMoleculeFile is not None:
            self.pdbMoleculeFile.export(outfile, level, name_='pdbMoleculeFile')
        else:
            warnEmptyAttribute("pdbMoleculeFile", "XSDataFile")
        if self._pdbSolventFile is not None:
            self.pdbSolventFile.export(outfile, level, name_='pdbSolventFile')
        else:
            warnEmptyAttribute("pdbSolventFile", "XSDataFile")
        if self._rfactor is not None:
            self.rfactor.export(outfile, level, name_='rfactor')
        if self._chiSqrt is not None:
            self.chiSqrt.export(outfile, level, name_='chiSqrt')
        if self._model is not None:
            self.model.export(outfile, level, name_='model')
        else:
            warnEmptyAttribute("model", "XSDataSaxsModel")
    def build(self, node_):
        for child_ in node_.childNodes:
            nodeName_ = child_.nodeName.split(':')[-1]
            self.buildChildren(child_, nodeName_)
    def buildChildren(self, child_, nodeName_):
        if child_.nodeType == Node.ELEMENT_NODE and \
            nodeName_ == 'fitFile':
            obj_ = XSDataFile()
            obj_.build(child_)
            self.setFitFile(obj_)
        elif child_.nodeType == Node.ELEMENT_NODE and \
            nodeName_ == 'logFile':
            obj_ = XSDataFile()
            obj_.build(child_)
            self.setLogFile(obj_)
        elif child_.nodeType == Node.ELEMENT_NODE and \
            nodeName_ == 'pdbMoleculeFile':
            obj_ = XSDataFile()
            obj_.build(child_)
            self.setPdbMoleculeFile(obj_)
        elif child_.nodeType == Node.ELEMENT_NODE and \
            nodeName_ == 'pdbSolventFile':
            obj_ = XSDataFile()
            obj_.build(child_)
            self.setPdbSolventFile(obj_)
        elif child_.nodeType == Node.ELEMENT_NODE and \
            nodeName_ == 'rfactor':
            obj_ = XSDataDouble()
            obj_.build(child_)
            self.setRfactor(obj_)
        elif child_.nodeType == Node.ELEMENT_NODE and \
            nodeName_ == 'chiSqrt':
            obj_ = XSDataDouble()
            obj_.build(child_)
            self.setChiSqrt(obj_)
        elif child_.nodeType == Node.ELEMENT_NODE and \
            nodeName_ == 'model':
            obj_ = XSDataSaxsModel()
            obj_.build(child_)
            self.setModel(obj_)
        XSDataResult.buildChildren(self, child_, nodeName_)
    #Method for marshalling an object
    def marshal( self ):
        oStreamString = StringIO()
        oStreamString.write(unicode('<?xml version="1.0" ?>\n'))
        self.export( oStreamString, 0, name_="XSDataResultDammin" )
        oStringXML = oStreamString.getvalue()
        oStreamString.close()
        return oStringXML
    #Only to export the entire XML tree to a file stream on disk
    def exportToFile( self, _outfileName ):
        outfile = open( _outfileName, "w" )
        outfile.write(unicode('<?xml version=\"1.0\" ?>\n'))
        self.export( outfile, 0, name_='XSDataResultDammin' )
        outfile.close()
    #Deprecated method, replaced by exportToFile
    def outputFile( self, _outfileName ):
        print("WARNING: Method outputFile in class XSDataResultDammin is deprecated, please use instead exportToFile!")
        self.exportToFile(_outfileName)
    #Method for making a copy in a new instance
    def copy( self ):
        return XSDataResultDammin.parseString(self.marshal())
    #Static method for parsing a string
    def parseString( _inString ):
        doc = minidom.parseString(_inString)
        rootNode = doc.documentElement
        rootObj = XSDataResultDammin()
        rootObj.build(rootNode)
        # Check that all minOccurs are obeyed by marshalling the created object
        oStreamString = StringIO()
        rootObj.export( oStreamString, 0, name_="XSDataResultDammin" )
        oStreamString.close()
        return rootObj
    parseString = staticmethod( parseString )
    #Static method for parsing a file
    def parseFile( _inFilePath ):
        doc = minidom.parse(_inFilePath)
        rootNode = doc.documentElement
        rootObj = XSDataResultDammin()
        rootObj.build(rootNode)
        return rootObj
    parseFile = staticmethod( parseFile )
# end class XSDataResultDammin


class XSDataResultDamstart(XSDataResult):
    def __init__(self, status=None, model=None, outputPdbFile=None):
        XSDataResult.__init__(self, status)
        if outputPdbFile is None:
            self._outputPdbFile = None
        elif outputPdbFile.__class__.__name__ == "XSDataFile":
            self._outputPdbFile = outputPdbFile
        else:
            strMessage = "ERROR! XSDataResultDamstart constructor argument 'outputPdbFile' is not XSDataFile but %s" % self._outputPdbFile.__class__.__name__
            raise BaseException(strMessage)
        if model is None:
            self._model = None
        elif model.__class__.__name__ == "XSDataSaxsModel":
            self._model = model
        else:
            strMessage = "ERROR! XSDataResultDamstart constructor argument 'model' is not XSDataSaxsModel but %s" % self._model.__class__.__name__
            raise BaseException(strMessage)
    # Methods and properties for the 'outputPdbFile' attribute
    def getOutputPdbFile(self): return self._outputPdbFile
    def setOutputPdbFile(self, outputPdbFile):
        if outputPdbFile is None:
            self._outputPdbFile = None
        elif outputPdbFile.__class__.__name__ == "XSDataFile":
            self._outputPdbFile = outputPdbFile
        else:
            strMessage = "ERROR! XSDataResultDamstart.setOutputPdbFile argument is not XSDataFile but %s" % outputPdbFile.__class__.__name__
            raise BaseException(strMessage)
    def delOutputPdbFile(self): self._outputPdbFile = None
    outputPdbFile = property(getOutputPdbFile, setOutputPdbFile, delOutputPdbFile, "Property for outputPdbFile")
    # Methods and properties for the 'model' attribute
    def getModel(self): return self._model
    def setModel(self, model):
        if model is None:
            self._model = None
        elif model.__class__.__name__ == "XSDataSaxsModel":
            self._model = model
        else:
            strMessage = "ERROR! XSDataResultDamstart.setModel argument is not XSDataSaxsModel but %s" % model.__class__.__name__
            raise BaseException(strMessage)
    def delModel(self): self._model = None
    model = property(getModel, setModel, delModel, "Property for model")
    def export(self, outfile, level, name_='XSDataResultDamstart'):
        showIndent(outfile, level)
        outfile.write(unicode('<%s>\n' % name_))
        self.exportChildren(outfile, level + 1, name_)
        showIndent(outfile, level)
        outfile.write(unicode('</%s>\n' % name_))
    def exportChildren(self, outfile, level, name_='XSDataResultDamstart'):
        XSDataResult.exportChildren(self, outfile, level, name_)
        if self._outputPdbFile is not None:
            self.outputPdbFile.export(outfile, level, name_='outputPdbFile')
        if self._model is not None:
            self.model.export(outfile, level, name_='model')
        else:
            warnEmptyAttribute("model", "XSDataSaxsModel")
    def build(self, node_):
        for child_ in node_.childNodes:
            nodeName_ = child_.nodeName.split(':')[-1]
            self.buildChildren(child_, nodeName_)
    def buildChildren(self, child_, nodeName_):
        if child_.nodeType == Node.ELEMENT_NODE and \
            nodeName_ == 'outputPdbFile':
            obj_ = XSDataFile()
            obj_.build(child_)
            self.setOutputPdbFile(obj_)
        elif child_.nodeType == Node.ELEMENT_NODE and \
            nodeName_ == 'model':
            obj_ = XSDataSaxsModel()
            obj_.build(child_)
            self.setModel(obj_)
        XSDataResult.buildChildren(self, child_, nodeName_)
    #Method for marshalling an object
    def marshal( self ):
        oStreamString = StringIO()
        oStreamString.write(unicode('<?xml version="1.0" ?>\n'))
        self.export( oStreamString, 0, name_="XSDataResultDamstart" )
        oStringXML = oStreamString.getvalue()
        oStreamString.close()
        return oStringXML
    #Only to export the entire XML tree to a file stream on disk
    def exportToFile( self, _outfileName ):
        outfile = open( _outfileName, "w" )
        outfile.write(unicode('<?xml version=\"1.0\" ?>\n'))
        self.export( outfile, 0, name_='XSDataResultDamstart' )
        outfile.close()
    #Deprecated method, replaced by exportToFile
    def outputFile( self, _outfileName ):
        print("WARNING: Method outputFile in class XSDataResultDamstart is deprecated, please use instead exportToFile!")
        self.exportToFile(_outfileName)
    #Method for making a copy in a new instance
    def copy( self ):
        return XSDataResultDamstart.parseString(self.marshal())
    #Static method for parsing a string
    def parseString( _inString ):
        doc = minidom.parseString(_inString)
        rootNode = doc.documentElement
        rootObj = XSDataResultDamstart()
        rootObj.build(rootNode)
        # Check that all minOccurs are obeyed by marshalling the created object
        oStreamString = StringIO()
        rootObj.export( oStreamString, 0, name_="XSDataResultDamstart" )
        oStreamString.close()
        return rootObj
    parseString = staticmethod( parseString )
    #Static method for parsing a file
    def parseFile( _inFilePath ):
        doc = minidom.parse(_inFilePath)
        rootNode = doc.documentElement
        rootObj = XSDataResultDamstart()
        rootObj.build(rootNode)
        return rootObj
    parseFile = staticmethod( parseFile )
# end class XSDataResultDamstart


class XSDataResultDatGnom(XSDataResult):
    def __init__(self, status=None, gnom=None):
        XSDataResult.__init__(self, status)
        if gnom is None:
            self._gnom = None
        elif gnom.__class__.__name__ == "XSDataGnom":
            self._gnom = gnom
        else:
            strMessage = "ERROR! XSDataResultDatGnom constructor argument 'gnom' is not XSDataGnom but %s" % self._gnom.__class__.__name__
            raise BaseException(strMessage)
    # Methods and properties for the 'gnom' attribute
    def getGnom(self): return self._gnom
    def setGnom(self, gnom):
        if gnom is None:
            self._gnom = None
        elif gnom.__class__.__name__ == "XSDataGnom":
            self._gnom = gnom
        else:
            strMessage = "ERROR! XSDataResultDatGnom.setGnom argument is not XSDataGnom but %s" % gnom.__class__.__name__
            raise BaseException(strMessage)
    def delGnom(self): self._gnom = None
    gnom = property(getGnom, setGnom, delGnom, "Property for gnom")
    def export(self, outfile, level, name_='XSDataResultDatGnom'):
        showIndent(outfile, level)
        outfile.write(unicode('<%s>\n' % name_))
        self.exportChildren(outfile, level + 1, name_)
        showIndent(outfile, level)
        outfile.write(unicode('</%s>\n' % name_))
    def exportChildren(self, outfile, level, name_='XSDataResultDatGnom'):
        XSDataResult.exportChildren(self, outfile, level, name_)
        if self._gnom is not None:
            self.gnom.export(outfile, level, name_='gnom')
        else:
            warnEmptyAttribute("gnom", "XSDataGnom")
    def build(self, node_):
        for child_ in node_.childNodes:
            nodeName_ = child_.nodeName.split(':')[-1]
            self.buildChildren(child_, nodeName_)
    def buildChildren(self, child_, nodeName_):
        if child_.nodeType == Node.ELEMENT_NODE and \
            nodeName_ == 'gnom':
            obj_ = XSDataGnom()
            obj_.build(child_)
            self.setGnom(obj_)
        XSDataResult.buildChildren(self, child_, nodeName_)
    #Method for marshalling an object
    def marshal( self ):
        oStreamString = StringIO()
        oStreamString.write(unicode('<?xml version="1.0" ?>\n'))
        self.export( oStreamString, 0, name_="XSDataResultDatGnom" )
        oStringXML = oStreamString.getvalue()
        oStreamString.close()
        return oStringXML
    #Only to export the entire XML tree to a file stream on disk
    def exportToFile( self, _outfileName ):
        outfile = open( _outfileName, "w" )
        outfile.write(unicode('<?xml version=\"1.0\" ?>\n'))
        self.export( outfile, 0, name_='XSDataResultDatGnom' )
        outfile.close()
    #Deprecated method, replaced by exportToFile
    def outputFile( self, _outfileName ):
        print("WARNING: Method outputFile in class XSDataResultDatGnom is deprecated, please use instead exportToFile!")
        self.exportToFile(_outfileName)
    #Method for making a copy in a new instance
    def copy( self ):
        return XSDataResultDatGnom.parseString(self.marshal())
    #Static method for parsing a string
    def parseString( _inString ):
        doc = minidom.parseString(_inString)
        rootNode = doc.documentElement
        rootObj = XSDataResultDatGnom()
        rootObj.build(rootNode)
        # Check that all minOccurs are obeyed by marshalling the created object
        oStreamString = StringIO()
        rootObj.export( oStreamString, 0, name_="XSDataResultDatGnom" )
        oStreamString.close()
        return rootObj
    parseString = staticmethod( parseString )
    #Static method for parsing a file
    def parseFile( _inFilePath ):
        doc = minidom.parse(_inFilePath)
        rootNode = doc.documentElement
        rootObj = XSDataResultDatGnom()
        rootObj.build(rootNode)
        return rootObj
    parseFile = staticmethod( parseFile )
# end class XSDataResultDatGnom


class XSDataResultDatPorod(XSDataResult):
    def __init__(self, status=None, volume=None):
        XSDataResult.__init__(self, status)
        if volume is None:
            self._volume = None
        elif volume.__class__.__name__ == "XSDataDoubleWithUnit":
            self._volume = volume
        else:
            strMessage = "ERROR! XSDataResultDatPorod constructor argument 'volume' is not XSDataDoubleWithUnit but %s" % self._volume.__class__.__name__
            raise BaseException(strMessage)
    # Methods and properties for the 'volume' attribute
    def getVolume(self): return self._volume
    def setVolume(self, volume):
        if volume is None:
            self._volume = None
        elif volume.__class__.__name__ == "XSDataDoubleWithUnit":
            self._volume = volume
        else:
            strMessage = "ERROR! XSDataResultDatPorod.setVolume argument is not XSDataDoubleWithUnit but %s" % volume.__class__.__name__
            raise BaseException(strMessage)
    def delVolume(self): self._volume = None
    volume = property(getVolume, setVolume, delVolume, "Property for volume")
    def export(self, outfile, level, name_='XSDataResultDatPorod'):
        showIndent(outfile, level)
        outfile.write(unicode('<%s>\n' % name_))
        self.exportChildren(outfile, level + 1, name_)
        showIndent(outfile, level)
        outfile.write(unicode('</%s>\n' % name_))
    def exportChildren(self, outfile, level, name_='XSDataResultDatPorod'):
        XSDataResult.exportChildren(self, outfile, level, name_)
        if self._volume is not None:
            self.volume.export(outfile, level, name_='volume')
        else:
            warnEmptyAttribute("volume", "XSDataDoubleWithUnit")
    def build(self, node_):
        for child_ in node_.childNodes:
            nodeName_ = child_.nodeName.split(':')[-1]
            self.buildChildren(child_, nodeName_)
    def buildChildren(self, child_, nodeName_):
        if child_.nodeType == Node.ELEMENT_NODE and \
            nodeName_ == 'volume':
            obj_ = XSDataDoubleWithUnit()
            obj_.build(child_)
            self.setVolume(obj_)
        XSDataResult.buildChildren(self, child_, nodeName_)
    #Method for marshalling an object
    def marshal( self ):
        oStreamString = StringIO()
        oStreamString.write(unicode('<?xml version="1.0" ?>\n'))
        self.export( oStreamString, 0, name_="XSDataResultDatPorod" )
        oStringXML = oStreamString.getvalue()
        oStreamString.close()
        return oStringXML
    #Only to export the entire XML tree to a file stream on disk
    def exportToFile( self, _outfileName ):
        outfile = open( _outfileName, "w" )
        outfile.write(unicode('<?xml version=\"1.0\" ?>\n'))
        self.export( outfile, 0, name_='XSDataResultDatPorod' )
        outfile.close()
    #Deprecated method, replaced by exportToFile
    def outputFile( self, _outfileName ):
        print("WARNING: Method outputFile in class XSDataResultDatPorod is deprecated, please use instead exportToFile!")
        self.exportToFile(_outfileName)
    #Method for making a copy in a new instance
    def copy( self ):
        return XSDataResultDatPorod.parseString(self.marshal())
    #Static method for parsing a string
    def parseString( _inString ):
        doc = minidom.parseString(_inString)
        rootNode = doc.documentElement
        rootObj = XSDataResultDatPorod()
        rootObj.build(rootNode)
        # Check that all minOccurs are obeyed by marshalling the created object
        oStreamString = StringIO()
        rootObj.export( oStreamString, 0, name_="XSDataResultDatPorod" )
        oStreamString.close()
        return rootObj
    parseString = staticmethod( parseString )
    #Static method for parsing a file
    def parseFile( _inFilePath ):
        doc = minidom.parse(_inFilePath)
        rootNode = doc.documentElement
        rootObj = XSDataResultDatPorod()
        rootObj.build(rootNode)
        return rootObj
    parseFile = staticmethod( parseFile )
# end class XSDataResultDatPorod


class XSDataResultDataver(XSDataResult):
    """Result of Dataver 	"""
    def __init__(self, status=None, outputCurve=None):
        XSDataResult.__init__(self, status)
        if outputCurve is None:
            self._outputCurve = None
        elif outputCurve.__class__.__name__ == "XSDataFile":
            self._outputCurve = outputCurve
        else:
            strMessage = "ERROR! XSDataResultDataver constructor argument 'outputCurve' is not XSDataFile but %s" % self._outputCurve.__class__.__name__
            raise BaseException(strMessage)
    # Methods and properties for the 'outputCurve' attribute
    def getOutputCurve(self): return self._outputCurve
    def setOutputCurve(self, outputCurve):
        if outputCurve is None:
            self._outputCurve = None
        elif outputCurve.__class__.__name__ == "XSDataFile":
            self._outputCurve = outputCurve
        else:
            strMessage = "ERROR! XSDataResultDataver.setOutputCurve argument is not XSDataFile but %s" % outputCurve.__class__.__name__
            raise BaseException(strMessage)
    def delOutputCurve(self): self._outputCurve = None
    outputCurve = property(getOutputCurve, setOutputCurve, delOutputCurve, "Property for outputCurve")
    def export(self, outfile, level, name_='XSDataResultDataver'):
        showIndent(outfile, level)
        outfile.write(unicode('<%s>\n' % name_))
        self.exportChildren(outfile, level + 1, name_)
        showIndent(outfile, level)
        outfile.write(unicode('</%s>\n' % name_))
    def exportChildren(self, outfile, level, name_='XSDataResultDataver'):
        XSDataResult.exportChildren(self, outfile, level, name_)
        if self._outputCurve is not None:
            self.outputCurve.export(outfile, level, name_='outputCurve')
        else:
            warnEmptyAttribute("outputCurve", "XSDataFile")
    def build(self, node_):
        for child_ in node_.childNodes:
            nodeName_ = child_.nodeName.split(':')[-1]
            self.buildChildren(child_, nodeName_)
    def buildChildren(self, child_, nodeName_):
        if child_.nodeType == Node.ELEMENT_NODE and \
            nodeName_ == 'outputCurve':
            obj_ = XSDataFile()
            obj_.build(child_)
            self.setOutputCurve(obj_)
        XSDataResult.buildChildren(self, child_, nodeName_)
    #Method for marshalling an object
    def marshal( self ):
        oStreamString = StringIO()
        oStreamString.write(unicode('<?xml version="1.0" ?>\n'))
        self.export( oStreamString, 0, name_="XSDataResultDataver" )
        oStringXML = oStreamString.getvalue()
        oStreamString.close()
        return oStringXML
    #Only to export the entire XML tree to a file stream on disk
    def exportToFile( self, _outfileName ):
        outfile = open( _outfileName, "w" )
        outfile.write(unicode('<?xml version=\"1.0\" ?>\n'))
        self.export( outfile, 0, name_='XSDataResultDataver' )
        outfile.close()
    #Deprecated method, replaced by exportToFile
    def outputFile( self, _outfileName ):
        print("WARNING: Method outputFile in class XSDataResultDataver is deprecated, please use instead exportToFile!")
        self.exportToFile(_outfileName)
    #Method for making a copy in a new instance
    def copy( self ):
        return XSDataResultDataver.parseString(self.marshal())
    #Static method for parsing a string
    def parseString( _inString ):
        doc = minidom.parseString(_inString)
        rootNode = doc.documentElement
        rootObj = XSDataResultDataver()
        rootObj.build(rootNode)
        # Check that all minOccurs are obeyed by marshalling the created object
        oStreamString = StringIO()
        rootObj.export( oStreamString, 0, name_="XSDataResultDataver" )
        oStreamString.close()
        return rootObj
    parseString = staticmethod( parseString )
    #Static method for parsing a file
    def parseFile( _inFilePath ):
        doc = minidom.parse(_inFilePath)
        rootNode = doc.documentElement
        rootObj = XSDataResultDataver()
        rootObj.build(rootNode)
        return rootObj
    parseFile = staticmethod( parseFile )
# end class XSDataResultDataver


class XSDataResultDatcmp(XSDataResult):
    """Higher chi-values indicate dis-similarities in the input.

	 Fidelity gives the likelihood of the two data sets being identical.
	"""
    def __init__(self, status=None, fidelity=None, chi=None):
        XSDataResult.__init__(self, status)
        if chi is None:
            self._chi = None
        elif chi.__class__.__name__ == "XSDataDouble":
            self._chi = chi
        else:
            strMessage = "ERROR! XSDataResultDatcmp constructor argument 'chi' is not XSDataDouble but %s" % self._chi.__class__.__name__
            raise BaseException(strMessage)
        if fidelity is None:
            self._fidelity = None
        elif fidelity.__class__.__name__ == "XSDataDouble":
            self._fidelity = fidelity
        else:
            strMessage = "ERROR! XSDataResultDatcmp constructor argument 'fidelity' is not XSDataDouble but %s" % self._fidelity.__class__.__name__
            raise BaseException(strMessage)
    # Methods and properties for the 'chi' attribute
    def getChi(self): return self._chi
    def setChi(self, chi):
        if chi is None:
            self._chi = None
        elif chi.__class__.__name__ == "XSDataDouble":
            self._chi = chi
        else:
            strMessage = "ERROR! XSDataResultDatcmp.setChi argument is not XSDataDouble but %s" % chi.__class__.__name__
            raise BaseException(strMessage)
    def delChi(self): self._chi = None
    chi = property(getChi, setChi, delChi, "Property for chi")
    # Methods and properties for the 'fidelity' attribute
    def getFidelity(self): return self._fidelity
    def setFidelity(self, fidelity):
        if fidelity is None:
            self._fidelity = None
        elif fidelity.__class__.__name__ == "XSDataDouble":
            self._fidelity = fidelity
        else:
            strMessage = "ERROR! XSDataResultDatcmp.setFidelity argument is not XSDataDouble but %s" % fidelity.__class__.__name__
            raise BaseException(strMessage)
    def delFidelity(self): self._fidelity = None
    fidelity = property(getFidelity, setFidelity, delFidelity, "Property for fidelity")
    def export(self, outfile, level, name_='XSDataResultDatcmp'):
        showIndent(outfile, level)
        outfile.write(unicode('<%s>\n' % name_))
        self.exportChildren(outfile, level + 1, name_)
        showIndent(outfile, level)
        outfile.write(unicode('</%s>\n' % name_))
    def exportChildren(self, outfile, level, name_='XSDataResultDatcmp'):
        XSDataResult.exportChildren(self, outfile, level, name_)
        if self._chi is not None:
            self.chi.export(outfile, level, name_='chi')
        else:
            warnEmptyAttribute("chi", "XSDataDouble")
        if self._fidelity is not None:
            self.fidelity.export(outfile, level, name_='fidelity')
        else:
            warnEmptyAttribute("fidelity", "XSDataDouble")
    def build(self, node_):
        for child_ in node_.childNodes:
            nodeName_ = child_.nodeName.split(':')[-1]
            self.buildChildren(child_, nodeName_)
    def buildChildren(self, child_, nodeName_):
        if child_.nodeType == Node.ELEMENT_NODE and \
            nodeName_ == 'chi':
            obj_ = XSDataDouble()
            obj_.build(child_)
            self.setChi(obj_)
        elif child_.nodeType == Node.ELEMENT_NODE and \
            nodeName_ == 'fidelity':
            obj_ = XSDataDouble()
            obj_.build(child_)
            self.setFidelity(obj_)
        XSDataResult.buildChildren(self, child_, nodeName_)
    #Method for marshalling an object
    def marshal( self ):
        oStreamString = StringIO()
        oStreamString.write(unicode('<?xml version="1.0" ?>\n'))
        self.export( oStreamString, 0, name_="XSDataResultDatcmp" )
        oStringXML = oStreamString.getvalue()
        oStreamString.close()
        return oStringXML
    #Only to export the entire XML tree to a file stream on disk
    def exportToFile( self, _outfileName ):
        outfile = open( _outfileName, "w" )
        outfile.write(unicode('<?xml version=\"1.0\" ?>\n'))
        self.export( outfile, 0, name_='XSDataResultDatcmp' )
        outfile.close()
    #Deprecated method, replaced by exportToFile
    def outputFile( self, _outfileName ):
        print("WARNING: Method outputFile in class XSDataResultDatcmp is deprecated, please use instead exportToFile!")
        self.exportToFile(_outfileName)
    #Method for making a copy in a new instance
    def copy( self ):
        return XSDataResultDatcmp.parseString(self.marshal())
    #Static method for parsing a string
    def parseString( _inString ):
        doc = minidom.parseString(_inString)
        rootNode = doc.documentElement
        rootObj = XSDataResultDatcmp()
        rootObj.build(rootNode)
        # Check that all minOccurs are obeyed by marshalling the created object
        oStreamString = StringIO()
        rootObj.export( oStreamString, 0, name_="XSDataResultDatcmp" )
        oStreamString.close()
        return rootObj
    parseString = staticmethod( parseString )
    #Static method for parsing a file
    def parseFile( _inFilePath ):
        doc = minidom.parse(_inFilePath)
        rootNode = doc.documentElement
        rootObj = XSDataResultDatcmp()
        rootObj.build(rootNode)
        return rootObj
    parseFile = staticmethod( parseFile )
# end class XSDataResultDatcmp


class XSDataResultDatop(XSDataResult):
    """Result of Datop 	"""
    def __init__(self, status=None, outputCurve=None):
        XSDataResult.__init__(self, status)
        if outputCurve is None:
            self._outputCurve = None
        elif outputCurve.__class__.__name__ == "XSDataFile":
            self._outputCurve = outputCurve
        else:
            strMessage = "ERROR! XSDataResultDatop constructor argument 'outputCurve' is not XSDataFile but %s" % self._outputCurve.__class__.__name__
            raise BaseException(strMessage)
    # Methods and properties for the 'outputCurve' attribute
    def getOutputCurve(self): return self._outputCurve
    def setOutputCurve(self, outputCurve):
        if outputCurve is None:
            self._outputCurve = None
        elif outputCurve.__class__.__name__ == "XSDataFile":
            self._outputCurve = outputCurve
        else:
            strMessage = "ERROR! XSDataResultDatop.setOutputCurve argument is not XSDataFile but %s" % outputCurve.__class__.__name__
            raise BaseException(strMessage)
    def delOutputCurve(self): self._outputCurve = None
    outputCurve = property(getOutputCurve, setOutputCurve, delOutputCurve, "Property for outputCurve")
    def export(self, outfile, level, name_='XSDataResultDatop'):
        showIndent(outfile, level)
        outfile.write(unicode('<%s>\n' % name_))
        self.exportChildren(outfile, level + 1, name_)
        showIndent(outfile, level)
        outfile.write(unicode('</%s>\n' % name_))
    def exportChildren(self, outfile, level, name_='XSDataResultDatop'):
        XSDataResult.exportChildren(self, outfile, level, name_)
        if self._outputCurve is not None:
            self.outputCurve.export(outfile, level, name_='outputCurve')
        else:
            warnEmptyAttribute("outputCurve", "XSDataFile")
    def build(self, node_):
        for child_ in node_.childNodes:
            nodeName_ = child_.nodeName.split(':')[-1]
            self.buildChildren(child_, nodeName_)
    def buildChildren(self, child_, nodeName_):
        if child_.nodeType == Node.ELEMENT_NODE and \
            nodeName_ == 'outputCurve':
            obj_ = XSDataFile()
            obj_.build(child_)
            self.setOutputCurve(obj_)
        XSDataResult.buildChildren(self, child_, nodeName_)
    #Method for marshalling an object
    def marshal( self ):
        oStreamString = StringIO()
        oStreamString.write(unicode('<?xml version="1.0" ?>\n'))
        self.export( oStreamString, 0, name_="XSDataResultDatop" )
        oStringXML = oStreamString.getvalue()
        oStreamString.close()
        return oStringXML
    #Only to export the entire XML tree to a file stream on disk
    def exportToFile( self, _outfileName ):
        outfile = open( _outfileName, "w" )
        outfile.write(unicode('<?xml version=\"1.0\" ?>\n'))
        self.export( outfile, 0, name_='XSDataResultDatop' )
        outfile.close()
    #Deprecated method, replaced by exportToFile
    def outputFile( self, _outfileName ):
        print("WARNING: Method outputFile in class XSDataResultDatop is deprecated, please use instead exportToFile!")
        self.exportToFile(_outfileName)
    #Method for making a copy in a new instance
    def copy( self ):
        return XSDataResultDatop.parseString(self.marshal())
    #Static method for parsing a string
    def parseString( _inString ):
        doc = minidom.parseString(_inString)
        rootNode = doc.documentElement
        rootObj = XSDataResultDatop()
        rootObj.build(rootNode)
        # Check that all minOccurs are obeyed by marshalling the created object
        oStreamString = StringIO()
        rootObj.export( oStreamString, 0, name_="XSDataResultDatop" )
        oStreamString.close()
        return rootObj
    parseString = staticmethod( parseString )
    #Static method for parsing a file
    def parseFile( _inFilePath ):
        doc = minidom.parse(_inFilePath)
        rootNode = doc.documentElement
        rootObj = XSDataResultDatop()
        rootObj.build(rootNode)
        return rootObj
    parseFile = staticmethod( parseFile )
# end class XSDataResultDatop


class XSDataResultGnom(XSDataResult):
    def __init__(self, status=None, radiusOfGyration=None, radiusOfCrossSection=None, arrayErr=None, arrayPr=None, arrayR=None, distributionErr=None, distributionPr=None, distributionR=None, scatteringFitIArray=None, scatteringFitQArray=None, scatteringFitValues=None, scatteringFitQ=None, output=None, fitQuality=None):
        XSDataResult.__init__(self, status)
        if fitQuality is None:
            self._fitQuality = None
        elif fitQuality.__class__.__name__ == "XSDataDouble":
            self._fitQuality = fitQuality
        else:
            strMessage = "ERROR! XSDataResultGnom constructor argument 'fitQuality' is not XSDataDouble but %s" % self._fitQuality.__class__.__name__
            raise BaseException(strMessage)
        if output is None:
            self._output = None
        elif output.__class__.__name__ == "XSDataFile":
            self._output = output
        else:
            strMessage = "ERROR! XSDataResultGnom constructor argument 'output' is not XSDataFile but %s" % self._output.__class__.__name__
            raise BaseException(strMessage)
        if scatteringFitQ is None:
            self._scatteringFitQ = []
        elif scatteringFitQ.__class__.__name__ == "list":
            self._scatteringFitQ = scatteringFitQ
        else:
            strMessage = "ERROR! XSDataResultGnom constructor argument 'scatteringFitQ' is not list but %s" % self._scatteringFitQ.__class__.__name__
            raise BaseException(strMessage)
        if scatteringFitValues is None:
            self._scatteringFitValues = []
        elif scatteringFitValues.__class__.__name__ == "list":
            self._scatteringFitValues = scatteringFitValues
        else:
            strMessage = "ERROR! XSDataResultGnom constructor argument 'scatteringFitValues' is not list but %s" % self._scatteringFitValues.__class__.__name__
            raise BaseException(strMessage)
        if scatteringFitQArray is None:
            self._scatteringFitQArray = None
        elif scatteringFitQArray.__class__.__name__ == "XSDataArray":
            self._scatteringFitQArray = scatteringFitQArray
        else:
            strMessage = "ERROR! XSDataResultGnom constructor argument 'scatteringFitQArray' is not XSDataArray but %s" % self._scatteringFitQArray.__class__.__name__
            raise BaseException(strMessage)
        if scatteringFitIArray is None:
            self._scatteringFitIArray = None
        elif scatteringFitIArray.__class__.__name__ == "XSDataArray":
            self._scatteringFitIArray = scatteringFitIArray
        else:
            strMessage = "ERROR! XSDataResultGnom constructor argument 'scatteringFitIArray' is not XSDataArray but %s" % self._scatteringFitIArray.__class__.__name__
            raise BaseException(strMessage)
        if distributionR is None:
            self._distributionR = []
        elif distributionR.__class__.__name__ == "list":
            self._distributionR = distributionR
        else:
            strMessage = "ERROR! XSDataResultGnom constructor argument 'distributionR' is not list but %s" % self._distributionR.__class__.__name__
            raise BaseException(strMessage)
        if distributionPr is None:
            self._distributionPr = []
        elif distributionPr.__class__.__name__ == "list":
            self._distributionPr = distributionPr
        else:
            strMessage = "ERROR! XSDataResultGnom constructor argument 'distributionPr' is not list but %s" % self._distributionPr.__class__.__name__
            raise BaseException(strMessage)
        if distributionErr is None:
            self._distributionErr = []
        elif distributionErr.__class__.__name__ == "list":
            self._distributionErr = distributionErr
        else:
            strMessage = "ERROR! XSDataResultGnom constructor argument 'distributionErr' is not list but %s" % self._distributionErr.__class__.__name__
            raise BaseException(strMessage)
        if arrayR is None:
            self._arrayR = None
        elif arrayR.__class__.__name__ == "XSDataArray":
            self._arrayR = arrayR
        else:
            strMessage = "ERROR! XSDataResultGnom constructor argument 'arrayR' is not XSDataArray but %s" % self._arrayR.__class__.__name__
            raise BaseException(strMessage)
        if arrayPr is None:
            self._arrayPr = None
        elif arrayPr.__class__.__name__ == "XSDataArray":
            self._arrayPr = arrayPr
        else:
            strMessage = "ERROR! XSDataResultGnom constructor argument 'arrayPr' is not XSDataArray but %s" % self._arrayPr.__class__.__name__
            raise BaseException(strMessage)
        if arrayErr is None:
            self._arrayErr = None
        elif arrayErr.__class__.__name__ == "XSDataArray":
            self._arrayErr = arrayErr
        else:
            strMessage = "ERROR! XSDataResultGnom constructor argument 'arrayErr' is not XSDataArray but %s" % self._arrayErr.__class__.__name__
            raise BaseException(strMessage)
        if radiusOfCrossSection is None:
            self._radiusOfCrossSection = None
        elif radiusOfCrossSection.__class__.__name__ == "XSDataDouble":
            self._radiusOfCrossSection = radiusOfCrossSection
        else:
            strMessage = "ERROR! XSDataResultGnom constructor argument 'radiusOfCrossSection' is not XSDataDouble but %s" % self._radiusOfCrossSection.__class__.__name__
            raise BaseException(strMessage)
        if radiusOfGyration is None:
            self._radiusOfGyration = None
        elif radiusOfGyration.__class__.__name__ == "XSDataDouble":
            self._radiusOfGyration = radiusOfGyration
        else:
            strMessage = "ERROR! XSDataResultGnom constructor argument 'radiusOfGyration' is not XSDataDouble but %s" % self._radiusOfGyration.__class__.__name__
            raise BaseException(strMessage)
    # Methods and properties for the 'fitQuality' attribute
    def getFitQuality(self): return self._fitQuality
    def setFitQuality(self, fitQuality):
        if fitQuality is None:
            self._fitQuality = None
        elif fitQuality.__class__.__name__ == "XSDataDouble":
            self._fitQuality = fitQuality
        else:
            strMessage = "ERROR! XSDataResultGnom.setFitQuality argument is not XSDataDouble but %s" % fitQuality.__class__.__name__
            raise BaseException(strMessage)
    def delFitQuality(self): self._fitQuality = None
    fitQuality = property(getFitQuality, setFitQuality, delFitQuality, "Property for fitQuality")
    # Methods and properties for the 'output' attribute
    def getOutput(self): return self._output
    def setOutput(self, output):
        if output is None:
            self._output = None
        elif output.__class__.__name__ == "XSDataFile":
            self._output = output
        else:
            strMessage = "ERROR! XSDataResultGnom.setOutput argument is not XSDataFile but %s" % output.__class__.__name__
            raise BaseException(strMessage)
    def delOutput(self): self._output = None
    output = property(getOutput, setOutput, delOutput, "Property for output")
    # Methods and properties for the 'scatteringFitQ' attribute
    def getScatteringFitQ(self): return self._scatteringFitQ
    def setScatteringFitQ(self, scatteringFitQ):
        if scatteringFitQ is None:
            self._scatteringFitQ = []
        elif scatteringFitQ.__class__.__name__ == "list":
            self._scatteringFitQ = scatteringFitQ
        else:
            strMessage = "ERROR! XSDataResultGnom.setScatteringFitQ argument is not list but %s" % scatteringFitQ.__class__.__name__
            raise BaseException(strMessage)
    def delScatteringFitQ(self): self._scatteringFitQ = None
    scatteringFitQ = property(getScatteringFitQ, setScatteringFitQ, delScatteringFitQ, "Property for scatteringFitQ")
    def addScatteringFitQ(self, value):
        if value is None:
            strMessage = "ERROR! XSDataResultGnom.addScatteringFitQ argument is None"
            raise BaseException(strMessage)            
        elif value.__class__.__name__ == "XSDataDouble":
            self._scatteringFitQ.append(value)
        else:
            strMessage = "ERROR! XSDataResultGnom.addScatteringFitQ argument is not XSDataDouble but %s" % value.__class__.__name__
            raise BaseException(strMessage)
    def insertScatteringFitQ(self, index, value):
        if index is None:
            strMessage = "ERROR! XSDataResultGnom.insertScatteringFitQ argument 'index' is None"
            raise BaseException(strMessage)            
        if value is None:
            strMessage = "ERROR! XSDataResultGnom.insertScatteringFitQ argument 'value' is None"
            raise BaseException(strMessage)            
        elif value.__class__.__name__ == "XSDataDouble":
            self._scatteringFitQ[index] = value
        else:
            strMessage = "ERROR! XSDataResultGnom.addScatteringFitQ argument is not XSDataDouble but %s" % value.__class__.__name__
            raise BaseException(strMessage)
    # Methods and properties for the 'scatteringFitValues' attribute
    def getScatteringFitValues(self): return self._scatteringFitValues
    def setScatteringFitValues(self, scatteringFitValues):
        if scatteringFitValues is None:
            self._scatteringFitValues = []
        elif scatteringFitValues.__class__.__name__ == "list":
            self._scatteringFitValues = scatteringFitValues
        else:
            strMessage = "ERROR! XSDataResultGnom.setScatteringFitValues argument is not list but %s" % scatteringFitValues.__class__.__name__
            raise BaseException(strMessage)
    def delScatteringFitValues(self): self._scatteringFitValues = None
    scatteringFitValues = property(getScatteringFitValues, setScatteringFitValues, delScatteringFitValues, "Property for scatteringFitValues")
    def addScatteringFitValues(self, value):
        if value is None:
            strMessage = "ERROR! XSDataResultGnom.addScatteringFitValues argument is None"
            raise BaseException(strMessage)            
        elif value.__class__.__name__ == "XSDataDouble":
            self._scatteringFitValues.append(value)
        else:
            strMessage = "ERROR! XSDataResultGnom.addScatteringFitValues argument is not XSDataDouble but %s" % value.__class__.__name__
            raise BaseException(strMessage)
    def insertScatteringFitValues(self, index, value):
        if index is None:
            strMessage = "ERROR! XSDataResultGnom.insertScatteringFitValues argument 'index' is None"
            raise BaseException(strMessage)            
        if value is None:
            strMessage = "ERROR! XSDataResultGnom.insertScatteringFitValues argument 'value' is None"
            raise BaseException(strMessage)            
        elif value.__class__.__name__ == "XSDataDouble":
            self._scatteringFitValues[index] = value
        else:
            strMessage = "ERROR! XSDataResultGnom.addScatteringFitValues argument is not XSDataDouble but %s" % value.__class__.__name__
            raise BaseException(strMessage)
    # Methods and properties for the 'scatteringFitQArray' attribute
    def getScatteringFitQArray(self): return self._scatteringFitQArray
    def setScatteringFitQArray(self, scatteringFitQArray):
        if scatteringFitQArray is None:
            self._scatteringFitQArray = None
        elif scatteringFitQArray.__class__.__name__ == "XSDataArray":
            self._scatteringFitQArray = scatteringFitQArray
        else:
            strMessage = "ERROR! XSDataResultGnom.setScatteringFitQArray argument is not XSDataArray but %s" % scatteringFitQArray.__class__.__name__
            raise BaseException(strMessage)
    def delScatteringFitQArray(self): self._scatteringFitQArray = None
    scatteringFitQArray = property(getScatteringFitQArray, setScatteringFitQArray, delScatteringFitQArray, "Property for scatteringFitQArray")
    # Methods and properties for the 'scatteringFitIArray' attribute
    def getScatteringFitIArray(self): return self._scatteringFitIArray
    def setScatteringFitIArray(self, scatteringFitIArray):
        if scatteringFitIArray is None:
            self._scatteringFitIArray = None
        elif scatteringFitIArray.__class__.__name__ == "XSDataArray":
            self._scatteringFitIArray = scatteringFitIArray
        else:
            strMessage = "ERROR! XSDataResultGnom.setScatteringFitIArray argument is not XSDataArray but %s" % scatteringFitIArray.__class__.__name__
            raise BaseException(strMessage)
    def delScatteringFitIArray(self): self._scatteringFitIArray = None
    scatteringFitIArray = property(getScatteringFitIArray, setScatteringFitIArray, delScatteringFitIArray, "Property for scatteringFitIArray")
    # Methods and properties for the 'distributionR' attribute
    def getDistributionR(self): return self._distributionR
    def setDistributionR(self, distributionR):
        if distributionR is None:
            self._distributionR = []
        elif distributionR.__class__.__name__ == "list":
            self._distributionR = distributionR
        else:
            strMessage = "ERROR! XSDataResultGnom.setDistributionR argument is not list but %s" % distributionR.__class__.__name__
            raise BaseException(strMessage)
    def delDistributionR(self): self._distributionR = None
    distributionR = property(getDistributionR, setDistributionR, delDistributionR, "Property for distributionR")
    def addDistributionR(self, value):
        if value is None:
            strMessage = "ERROR! XSDataResultGnom.addDistributionR argument is None"
            raise BaseException(strMessage)            
        elif value.__class__.__name__ == "XSDataDouble":
            self._distributionR.append(value)
        else:
            strMessage = "ERROR! XSDataResultGnom.addDistributionR argument is not XSDataDouble but %s" % value.__class__.__name__
            raise BaseException(strMessage)
    def insertDistributionR(self, index, value):
        if index is None:
            strMessage = "ERROR! XSDataResultGnom.insertDistributionR argument 'index' is None"
            raise BaseException(strMessage)            
        if value is None:
            strMessage = "ERROR! XSDataResultGnom.insertDistributionR argument 'value' is None"
            raise BaseException(strMessage)            
        elif value.__class__.__name__ == "XSDataDouble":
            self._distributionR[index] = value
        else:
            strMessage = "ERROR! XSDataResultGnom.addDistributionR argument is not XSDataDouble but %s" % value.__class__.__name__
            raise BaseException(strMessage)
    # Methods and properties for the 'distributionPr' attribute
    def getDistributionPr(self): return self._distributionPr
    def setDistributionPr(self, distributionPr):
        if distributionPr is None:
            self._distributionPr = []
        elif distributionPr.__class__.__name__ == "list":
            self._distributionPr = distributionPr
        else:
            strMessage = "ERROR! XSDataResultGnom.setDistributionPr argument is not list but %s" % distributionPr.__class__.__name__
            raise BaseException(strMessage)
    def delDistributionPr(self): self._distributionPr = None
    distributionPr = property(getDistributionPr, setDistributionPr, delDistributionPr, "Property for distributionPr")
    def addDistributionPr(self, value):
        if value is None:
            strMessage = "ERROR! XSDataResultGnom.addDistributionPr argument is None"
            raise BaseException(strMessage)            
        elif value.__class__.__name__ == "XSDataDouble":
            self._distributionPr.append(value)
        else:
            strMessage = "ERROR! XSDataResultGnom.addDistributionPr argument is not XSDataDouble but %s" % value.__class__.__name__
            raise BaseException(strMessage)
    def insertDistributionPr(self, index, value):
        if index is None:
            strMessage = "ERROR! XSDataResultGnom.insertDistributionPr argument 'index' is None"
            raise BaseException(strMessage)            
        if value is None:
            strMessage = "ERROR! XSDataResultGnom.insertDistributionPr argument 'value' is None"
            raise BaseException(strMessage)            
        elif value.__class__.__name__ == "XSDataDouble":
            self._distributionPr[index] = value
        else:
            strMessage = "ERROR! XSDataResultGnom.addDistributionPr argument is not XSDataDouble but %s" % value.__class__.__name__
            raise BaseException(strMessage)
    # Methods and properties for the 'distributionErr' attribute
    def getDistributionErr(self): return self._distributionErr
    def setDistributionErr(self, distributionErr):
        if distributionErr is None:
            self._distributionErr = []
        elif distributionErr.__class__.__name__ == "list":
            self._distributionErr = distributionErr
        else:
            strMessage = "ERROR! XSDataResultGnom.setDistributionErr argument is not list but %s" % distributionErr.__class__.__name__
            raise BaseException(strMessage)
    def delDistributionErr(self): self._distributionErr = None
    distributionErr = property(getDistributionErr, setDistributionErr, delDistributionErr, "Property for distributionErr")
    def addDistributionErr(self, value):
        if value is None:
            strMessage = "ERROR! XSDataResultGnom.addDistributionErr argument is None"
            raise BaseException(strMessage)            
        elif value.__class__.__name__ == "XSDataDouble":
            self._distributionErr.append(value)
        else:
            strMessage = "ERROR! XSDataResultGnom.addDistributionErr argument is not XSDataDouble but %s" % value.__class__.__name__
            raise BaseException(strMessage)
    def insertDistributionErr(self, index, value):
        if index is None:
            strMessage = "ERROR! XSDataResultGnom.insertDistributionErr argument 'index' is None"
            raise BaseException(strMessage)            
        if value is None:
            strMessage = "ERROR! XSDataResultGnom.insertDistributionErr argument 'value' is None"
            raise BaseException(strMessage)            
        elif value.__class__.__name__ == "XSDataDouble":
            self._distributionErr[index] = value
        else:
            strMessage = "ERROR! XSDataResultGnom.addDistributionErr argument is not XSDataDouble but %s" % value.__class__.__name__
            raise BaseException(strMessage)
    # Methods and properties for the 'arrayR' attribute
    def getArrayR(self): return self._arrayR
    def setArrayR(self, arrayR):
        if arrayR is None:
            self._arrayR = None
        elif arrayR.__class__.__name__ == "XSDataArray":
            self._arrayR = arrayR
        else:
            strMessage = "ERROR! XSDataResultGnom.setArrayR argument is not XSDataArray but %s" % arrayR.__class__.__name__
            raise BaseException(strMessage)
    def delArrayR(self): self._arrayR = None
    arrayR = property(getArrayR, setArrayR, delArrayR, "Property for arrayR")
    # Methods and properties for the 'arrayPr' attribute
    def getArrayPr(self): return self._arrayPr
    def setArrayPr(self, arrayPr):
        if arrayPr is None:
            self._arrayPr = None
        elif arrayPr.__class__.__name__ == "XSDataArray":
            self._arrayPr = arrayPr
        else:
            strMessage = "ERROR! XSDataResultGnom.setArrayPr argument is not XSDataArray but %s" % arrayPr.__class__.__name__
            raise BaseException(strMessage)
    def delArrayPr(self): self._arrayPr = None
    arrayPr = property(getArrayPr, setArrayPr, delArrayPr, "Property for arrayPr")
    # Methods and properties for the 'arrayErr' attribute
    def getArrayErr(self): return self._arrayErr
    def setArrayErr(self, arrayErr):
        if arrayErr is None:
            self._arrayErr = None
        elif arrayErr.__class__.__name__ == "XSDataArray":
            self._arrayErr = arrayErr
        else:
            strMessage = "ERROR! XSDataResultGnom.setArrayErr argument is not XSDataArray but %s" % arrayErr.__class__.__name__
            raise BaseException(strMessage)
    def delArrayErr(self): self._arrayErr = None
    arrayErr = property(getArrayErr, setArrayErr, delArrayErr, "Property for arrayErr")
    # Methods and properties for the 'radiusOfCrossSection' attribute
    def getRadiusOfCrossSection(self): return self._radiusOfCrossSection
    def setRadiusOfCrossSection(self, radiusOfCrossSection):
        if radiusOfCrossSection is None:
            self._radiusOfCrossSection = None
        elif radiusOfCrossSection.__class__.__name__ == "XSDataDouble":
            self._radiusOfCrossSection = radiusOfCrossSection
        else:
            strMessage = "ERROR! XSDataResultGnom.setRadiusOfCrossSection argument is not XSDataDouble but %s" % radiusOfCrossSection.__class__.__name__
            raise BaseException(strMessage)
    def delRadiusOfCrossSection(self): self._radiusOfCrossSection = None
    radiusOfCrossSection = property(getRadiusOfCrossSection, setRadiusOfCrossSection, delRadiusOfCrossSection, "Property for radiusOfCrossSection")
    # Methods and properties for the 'radiusOfGyration' attribute
    def getRadiusOfGyration(self): return self._radiusOfGyration
    def setRadiusOfGyration(self, radiusOfGyration):
        if radiusOfGyration is None:
            self._radiusOfGyration = None
        elif radiusOfGyration.__class__.__name__ == "XSDataDouble":
            self._radiusOfGyration = radiusOfGyration
        else:
            strMessage = "ERROR! XSDataResultGnom.setRadiusOfGyration argument is not XSDataDouble but %s" % radiusOfGyration.__class__.__name__
            raise BaseException(strMessage)
    def delRadiusOfGyration(self): self._radiusOfGyration = None
    radiusOfGyration = property(getRadiusOfGyration, setRadiusOfGyration, delRadiusOfGyration, "Property for radiusOfGyration")
    def export(self, outfile, level, name_='XSDataResultGnom'):
        showIndent(outfile, level)
        outfile.write(unicode('<%s>\n' % name_))
        self.exportChildren(outfile, level + 1, name_)
        showIndent(outfile, level)
        outfile.write(unicode('</%s>\n' % name_))
    def exportChildren(self, outfile, level, name_='XSDataResultGnom'):
        XSDataResult.exportChildren(self, outfile, level, name_)
        if self._fitQuality is not None:
            self.fitQuality.export(outfile, level, name_='fitQuality')
        else:
            warnEmptyAttribute("fitQuality", "XSDataDouble")
        if self._output is not None:
            self.output.export(outfile, level, name_='output')
        else:
            warnEmptyAttribute("output", "XSDataFile")
        for scatteringFitQ_ in self.getScatteringFitQ():
            scatteringFitQ_.export(outfile, level, name_='scatteringFitQ')
        for scatteringFitValues_ in self.getScatteringFitValues():
            scatteringFitValues_.export(outfile, level, name_='scatteringFitValues')
        if self._scatteringFitQArray is not None:
            self.scatteringFitQArray.export(outfile, level, name_='scatteringFitQArray')
        if self._scatteringFitIArray is not None:
            self.scatteringFitIArray.export(outfile, level, name_='scatteringFitIArray')
        for distributionR_ in self.getDistributionR():
            distributionR_.export(outfile, level, name_='distributionR')
        for distributionPr_ in self.getDistributionPr():
            distributionPr_.export(outfile, level, name_='distributionPr')
        for distributionErr_ in self.getDistributionErr():
            distributionErr_.export(outfile, level, name_='distributionErr')
        if self._arrayR is not None:
            self.arrayR.export(outfile, level, name_='arrayR')
        if self._arrayPr is not None:
            self.arrayPr.export(outfile, level, name_='arrayPr')
        if self._arrayErr is not None:
            self.arrayErr.export(outfile, level, name_='arrayErr')
        if self._radiusOfCrossSection is not None:
            self.radiusOfCrossSection.export(outfile, level, name_='radiusOfCrossSection')
        else:
            warnEmptyAttribute("radiusOfCrossSection", "XSDataDouble")
        if self._radiusOfGyration is not None:
            self.radiusOfGyration.export(outfile, level, name_='radiusOfGyration')
        else:
            warnEmptyAttribute("radiusOfGyration", "XSDataDouble")
    def build(self, node_):
        for child_ in node_.childNodes:
            nodeName_ = child_.nodeName.split(':')[-1]
            self.buildChildren(child_, nodeName_)
    def buildChildren(self, child_, nodeName_):
        if child_.nodeType == Node.ELEMENT_NODE and \
            nodeName_ == 'fitQuality':
            obj_ = XSDataDouble()
            obj_.build(child_)
            self.setFitQuality(obj_)
        elif child_.nodeType == Node.ELEMENT_NODE and \
            nodeName_ == 'output':
            obj_ = XSDataFile()
            obj_.build(child_)
            self.setOutput(obj_)
        elif child_.nodeType == Node.ELEMENT_NODE and \
            nodeName_ == 'scatteringFitQ':
            obj_ = XSDataDouble()
            obj_.build(child_)
            self.scatteringFitQ.append(obj_)
        elif child_.nodeType == Node.ELEMENT_NODE and \
            nodeName_ == 'scatteringFitValues':
            obj_ = XSDataDouble()
            obj_.build(child_)
            self.scatteringFitValues.append(obj_)
        elif child_.nodeType == Node.ELEMENT_NODE and \
            nodeName_ == 'scatteringFitQArray':
            obj_ = XSDataArray()
            obj_.build(child_)
            self.setScatteringFitQArray(obj_)
        elif child_.nodeType == Node.ELEMENT_NODE and \
            nodeName_ == 'scatteringFitIArray':
            obj_ = XSDataArray()
            obj_.build(child_)
            self.setScatteringFitIArray(obj_)
        elif child_.nodeType == Node.ELEMENT_NODE and \
            nodeName_ == 'distributionR':
            obj_ = XSDataDouble()
            obj_.build(child_)
            self.distributionR.append(obj_)
        elif child_.nodeType == Node.ELEMENT_NODE and \
            nodeName_ == 'distributionPr':
            obj_ = XSDataDouble()
            obj_.build(child_)
            self.distributionPr.append(obj_)
        elif child_.nodeType == Node.ELEMENT_NODE and \
            nodeName_ == 'distributionErr':
            obj_ = XSDataDouble()
            obj_.build(child_)
            self.distributionErr.append(obj_)
        elif child_.nodeType == Node.ELEMENT_NODE and \
            nodeName_ == 'arrayR':
            obj_ = XSDataArray()
            obj_.build(child_)
            self.setArrayR(obj_)
        elif child_.nodeType == Node.ELEMENT_NODE and \
            nodeName_ == 'arrayPr':
            obj_ = XSDataArray()
            obj_.build(child_)
            self.setArrayPr(obj_)
        elif child_.nodeType == Node.ELEMENT_NODE and \
            nodeName_ == 'arrayErr':
            obj_ = XSDataArray()
            obj_.build(child_)
            self.setArrayErr(obj_)
        elif child_.nodeType == Node.ELEMENT_NODE and \
            nodeName_ == 'radiusOfCrossSection':
            obj_ = XSDataDouble()
            obj_.build(child_)
            self.setRadiusOfCrossSection(obj_)
        elif child_.nodeType == Node.ELEMENT_NODE and \
            nodeName_ == 'radiusOfGyration':
            obj_ = XSDataDouble()
            obj_.build(child_)
            self.setRadiusOfGyration(obj_)
        XSDataResult.buildChildren(self, child_, nodeName_)
    #Method for marshalling an object
    def marshal( self ):
        oStreamString = StringIO()
        oStreamString.write(unicode('<?xml version="1.0" ?>\n'))
        self.export( oStreamString, 0, name_="XSDataResultGnom" )
        oStringXML = oStreamString.getvalue()
        oStreamString.close()
        return oStringXML
    #Only to export the entire XML tree to a file stream on disk
    def exportToFile( self, _outfileName ):
        outfile = open( _outfileName, "w" )
        outfile.write(unicode('<?xml version=\"1.0\" ?>\n'))
        self.export( outfile, 0, name_='XSDataResultGnom' )
        outfile.close()
    #Deprecated method, replaced by exportToFile
    def outputFile( self, _outfileName ):
        print("WARNING: Method outputFile in class XSDataResultGnom is deprecated, please use instead exportToFile!")
        self.exportToFile(_outfileName)
    #Method for making a copy in a new instance
    def copy( self ):
        return XSDataResultGnom.parseString(self.marshal())
    #Static method for parsing a string
    def parseString( _inString ):
        doc = minidom.parseString(_inString)
        rootNode = doc.documentElement
        rootObj = XSDataResultGnom()
        rootObj.build(rootNode)
        # Check that all minOccurs are obeyed by marshalling the created object
        oStreamString = StringIO()
        rootObj.export( oStreamString, 0, name_="XSDataResultGnom" )
        oStreamString.close()
        return rootObj
    parseString = staticmethod( parseString )
    #Static method for parsing a file
    def parseFile( _inFilePath ):
        doc = minidom.parse(_inFilePath)
        rootNode = doc.documentElement
        rootObj = XSDataResultGnom()
        rootObj.build(rootNode)
        return rootObj
    parseFile = staticmethod( parseFile )
# end class XSDataResultGnom


class XSDataResultSaxsAnalysis(XSDataResult):
    """AutoRg -> Gnom -> Porod pipeline"""
    def __init__(self, status=None, densityPlot=None, kratkyPlot=None, guinierPlot=None, scatterPlot=None, volume=None, gnom=None, autoRg=None):
        XSDataResult.__init__(self, status)
        if autoRg is None:
            self._autoRg = None
        elif autoRg.__class__.__name__ == "XSDataAutoRg":
            self._autoRg = autoRg
        else:
            strMessage = "ERROR! XSDataResultSaxsAnalysis constructor argument 'autoRg' is not XSDataAutoRg but %s" % self._autoRg.__class__.__name__
            raise BaseException(strMessage)
        if gnom is None:
            self._gnom = None
        elif gnom.__class__.__name__ == "XSDataGnom":
            self._gnom = gnom
        else:
            strMessage = "ERROR! XSDataResultSaxsAnalysis constructor argument 'gnom' is not XSDataGnom but %s" % self._gnom.__class__.__name__
            raise BaseException(strMessage)
        if volume is None:
            self._volume = None
        elif volume.__class__.__name__ == "XSDataDoubleWithUnit":
            self._volume = volume
        else:
            strMessage = "ERROR! XSDataResultSaxsAnalysis constructor argument 'volume' is not XSDataDoubleWithUnit but %s" % self._volume.__class__.__name__
            raise BaseException(strMessage)
        if scatterPlot is None:
            self._scatterPlot = None
        elif scatterPlot.__class__.__name__ == "XSDataFile":
            self._scatterPlot = scatterPlot
        else:
            strMessage = "ERROR! XSDataResultSaxsAnalysis constructor argument 'scatterPlot' is not XSDataFile but %s" % self._scatterPlot.__class__.__name__
            raise BaseException(strMessage)
        if guinierPlot is None:
            self._guinierPlot = None
        elif guinierPlot.__class__.__name__ == "XSDataFile":
            self._guinierPlot = guinierPlot
        else:
            strMessage = "ERROR! XSDataResultSaxsAnalysis constructor argument 'guinierPlot' is not XSDataFile but %s" % self._guinierPlot.__class__.__name__
            raise BaseException(strMessage)
        if kratkyPlot is None:
            self._kratkyPlot = None
        elif kratkyPlot.__class__.__name__ == "XSDataFile":
            self._kratkyPlot = kratkyPlot
        else:
            strMessage = "ERROR! XSDataResultSaxsAnalysis constructor argument 'kratkyPlot' is not XSDataFile but %s" % self._kratkyPlot.__class__.__name__
            raise BaseException(strMessage)
        if densityPlot is None:
            self._densityPlot = None
        elif densityPlot.__class__.__name__ == "XSDataFile":
            self._densityPlot = densityPlot
        else:
            strMessage = "ERROR! XSDataResultSaxsAnalysis constructor argument 'densityPlot' is not XSDataFile but %s" % self._densityPlot.__class__.__name__
            raise BaseException(strMessage)
    # Methods and properties for the 'autoRg' attribute
    def getAutoRg(self): return self._autoRg
    def setAutoRg(self, autoRg):
        if autoRg is None:
            self._autoRg = None
        elif autoRg.__class__.__name__ == "XSDataAutoRg":
            self._autoRg = autoRg
        else:
            strMessage = "ERROR! XSDataResultSaxsAnalysis.setAutoRg argument is not XSDataAutoRg but %s" % autoRg.__class__.__name__
            raise BaseException(strMessage)
    def delAutoRg(self): self._autoRg = None
    autoRg = property(getAutoRg, setAutoRg, delAutoRg, "Property for autoRg")
    # Methods and properties for the 'gnom' attribute
    def getGnom(self): return self._gnom
    def setGnom(self, gnom):
        if gnom is None:
            self._gnom = None
        elif gnom.__class__.__name__ == "XSDataGnom":
            self._gnom = gnom
        else:
            strMessage = "ERROR! XSDataResultSaxsAnalysis.setGnom argument is not XSDataGnom but %s" % gnom.__class__.__name__
            raise BaseException(strMessage)
    def delGnom(self): self._gnom = None
    gnom = property(getGnom, setGnom, delGnom, "Property for gnom")
    # Methods and properties for the 'volume' attribute
    def getVolume(self): return self._volume
    def setVolume(self, volume):
        if volume is None:
            self._volume = None
        elif volume.__class__.__name__ == "XSDataDoubleWithUnit":
            self._volume = volume
        else:
            strMessage = "ERROR! XSDataResultSaxsAnalysis.setVolume argument is not XSDataDoubleWithUnit but %s" % volume.__class__.__name__
            raise BaseException(strMessage)
    def delVolume(self): self._volume = None
    volume = property(getVolume, setVolume, delVolume, "Property for volume")
    # Methods and properties for the 'scatterPlot' attribute
    def getScatterPlot(self): return self._scatterPlot
    def setScatterPlot(self, scatterPlot):
        if scatterPlot is None:
            self._scatterPlot = None
        elif scatterPlot.__class__.__name__ == "XSDataFile":
            self._scatterPlot = scatterPlot
        else:
            strMessage = "ERROR! XSDataResultSaxsAnalysis.setScatterPlot argument is not XSDataFile but %s" % scatterPlot.__class__.__name__
            raise BaseException(strMessage)
    def delScatterPlot(self): self._scatterPlot = None
    scatterPlot = property(getScatterPlot, setScatterPlot, delScatterPlot, "Property for scatterPlot")
    # Methods and properties for the 'guinierPlot' attribute
    def getGuinierPlot(self): return self._guinierPlot
    def setGuinierPlot(self, guinierPlot):
        if guinierPlot is None:
            self._guinierPlot = None
        elif guinierPlot.__class__.__name__ == "XSDataFile":
            self._guinierPlot = guinierPlot
        else:
            strMessage = "ERROR! XSDataResultSaxsAnalysis.setGuinierPlot argument is not XSDataFile but %s" % guinierPlot.__class__.__name__
            raise BaseException(strMessage)
    def delGuinierPlot(self): self._guinierPlot = None
    guinierPlot = property(getGuinierPlot, setGuinierPlot, delGuinierPlot, "Property for guinierPlot")
    # Methods and properties for the 'kratkyPlot' attribute
    def getKratkyPlot(self): return self._kratkyPlot
    def setKratkyPlot(self, kratkyPlot):
        if kratkyPlot is None:
            self._kratkyPlot = None
        elif kratkyPlot.__class__.__name__ == "XSDataFile":
            self._kratkyPlot = kratkyPlot
        else:
            strMessage = "ERROR! XSDataResultSaxsAnalysis.setKratkyPlot argument is not XSDataFile but %s" % kratkyPlot.__class__.__name__
            raise BaseException(strMessage)
    def delKratkyPlot(self): self._kratkyPlot = None
    kratkyPlot = property(getKratkyPlot, setKratkyPlot, delKratkyPlot, "Property for kratkyPlot")
    # Methods and properties for the 'densityPlot' attribute
    def getDensityPlot(self): return self._densityPlot
    def setDensityPlot(self, densityPlot):
        if densityPlot is None:
            self._densityPlot = None
        elif densityPlot.__class__.__name__ == "XSDataFile":
            self._densityPlot = densityPlot
        else:
            strMessage = "ERROR! XSDataResultSaxsAnalysis.setDensityPlot argument is not XSDataFile but %s" % densityPlot.__class__.__name__
            raise BaseException(strMessage)
    def delDensityPlot(self): self._densityPlot = None
    densityPlot = property(getDensityPlot, setDensityPlot, delDensityPlot, "Property for densityPlot")
    def export(self, outfile, level, name_='XSDataResultSaxsAnalysis'):
        showIndent(outfile, level)
        outfile.write(unicode('<%s>\n' % name_))
        self.exportChildren(outfile, level + 1, name_)
        showIndent(outfile, level)
        outfile.write(unicode('</%s>\n' % name_))
    def exportChildren(self, outfile, level, name_='XSDataResultSaxsAnalysis'):
        XSDataResult.exportChildren(self, outfile, level, name_)
        if self._autoRg is not None:
            self.autoRg.export(outfile, level, name_='autoRg')
        else:
            warnEmptyAttribute("autoRg", "XSDataAutoRg")
        if self._gnom is not None:
            self.gnom.export(outfile, level, name_='gnom')
        else:
            warnEmptyAttribute("gnom", "XSDataGnom")
        if self._volume is not None:
            self.volume.export(outfile, level, name_='volume')
        else:
            warnEmptyAttribute("volume", "XSDataDoubleWithUnit")
        if self._scatterPlot is not None:
            self.scatterPlot.export(outfile, level, name_='scatterPlot')
        if self._guinierPlot is not None:
            self.guinierPlot.export(outfile, level, name_='guinierPlot')
        if self._kratkyPlot is not None:
            self.kratkyPlot.export(outfile, level, name_='kratkyPlot')
        if self._densityPlot is not None:
            self.densityPlot.export(outfile, level, name_='densityPlot')
    def build(self, node_):
        for child_ in node_.childNodes:
            nodeName_ = child_.nodeName.split(':')[-1]
            self.buildChildren(child_, nodeName_)
    def buildChildren(self, child_, nodeName_):
        if child_.nodeType == Node.ELEMENT_NODE and \
            nodeName_ == 'autoRg':
            obj_ = XSDataAutoRg()
            obj_.build(child_)
            self.setAutoRg(obj_)
        elif child_.nodeType == Node.ELEMENT_NODE and \
            nodeName_ == 'gnom':
            obj_ = XSDataGnom()
            obj_.build(child_)
            self.setGnom(obj_)
        elif child_.nodeType == Node.ELEMENT_NODE and \
            nodeName_ == 'volume':
            obj_ = XSDataDoubleWithUnit()
            obj_.build(child_)
            self.setVolume(obj_)
        elif child_.nodeType == Node.ELEMENT_NODE and \
            nodeName_ == 'scatterPlot':
            obj_ = XSDataFile()
            obj_.build(child_)
            self.setScatterPlot(obj_)
        elif child_.nodeType == Node.ELEMENT_NODE and \
            nodeName_ == 'guinierPlot':
            obj_ = XSDataFile()
            obj_.build(child_)
            self.setGuinierPlot(obj_)
        elif child_.nodeType == Node.ELEMENT_NODE and \
            nodeName_ == 'kratkyPlot':
            obj_ = XSDataFile()
            obj_.build(child_)
            self.setKratkyPlot(obj_)
        elif child_.nodeType == Node.ELEMENT_NODE and \
            nodeName_ == 'densityPlot':
            obj_ = XSDataFile()
            obj_.build(child_)
            self.setDensityPlot(obj_)
        XSDataResult.buildChildren(self, child_, nodeName_)
    #Method for marshalling an object
    def marshal( self ):
        oStreamString = StringIO()
        oStreamString.write(unicode('<?xml version="1.0" ?>\n'))
        self.export( oStreamString, 0, name_="XSDataResultSaxsAnalysis" )
        oStringXML = oStreamString.getvalue()
        oStreamString.close()
        return oStringXML
    #Only to export the entire XML tree to a file stream on disk
    def exportToFile( self, _outfileName ):
        outfile = open( _outfileName, "w" )
        outfile.write(unicode('<?xml version=\"1.0\" ?>\n'))
        self.export( outfile, 0, name_='XSDataResultSaxsAnalysis' )
        outfile.close()
    #Deprecated method, replaced by exportToFile
    def outputFile( self, _outfileName ):
        print("WARNING: Method outputFile in class XSDataResultSaxsAnalysis is deprecated, please use instead exportToFile!")
        self.exportToFile(_outfileName)
    #Method for making a copy in a new instance
    def copy( self ):
        return XSDataResultSaxsAnalysis.parseString(self.marshal())
    #Static method for parsing a string
    def parseString( _inString ):
        doc = minidom.parseString(_inString)
        rootNode = doc.documentElement
        rootObj = XSDataResultSaxsAnalysis()
        rootObj.build(rootNode)
        # Check that all minOccurs are obeyed by marshalling the created object
        oStreamString = StringIO()
        rootObj.export( oStreamString, 0, name_="XSDataResultSaxsAnalysis" )
        oStreamString.close()
        return rootObj
    parseString = staticmethod( parseString )
    #Static method for parsing a file
    def parseFile( _inFilePath ):
        doc = minidom.parse(_inFilePath)
        rootNode = doc.documentElement
        rootObj = XSDataResultSaxsAnalysis()
        rootObj.build(rootNode)
        return rootObj
    parseFile = staticmethod( parseFile )
# end class XSDataResultSaxsAnalysis


class XSDataResultSaxsAnalysisModeling(XSDataResult):
    """AutoRg -> Gnom -> Prod -> Dammif -> Supcomb -> Damaver -> Damfilt -> Damstart -> Dammin pipeline"""
    def __init__(self, status=None, pdbSolventFile=None, pdbMoleculeFile=None, logFile=None, fitFile=None, nsdPlot=None, chiRfactorPlot=None, damminModel=None, damstartModel=None, damfiltModel=None, damaverModel=None, dammifModels=None, densityPlot=None, kratkyPlot=None, guinierPlot=None, scatterPlot=None, volume=None, gnom=None, autoRg=None):
        XSDataResult.__init__(self, status)
        if autoRg is None:
            self._autoRg = None
        elif autoRg.__class__.__name__ == "XSDataAutoRg":
            self._autoRg = autoRg
        else:
            strMessage = "ERROR! XSDataResultSaxsAnalysisModeling constructor argument 'autoRg' is not XSDataAutoRg but %s" % self._autoRg.__class__.__name__
            raise BaseException(strMessage)
        if gnom is None:
            self._gnom = None
        elif gnom.__class__.__name__ == "XSDataGnom":
            self._gnom = gnom
        else:
            strMessage = "ERROR! XSDataResultSaxsAnalysisModeling constructor argument 'gnom' is not XSDataGnom but %s" % self._gnom.__class__.__name__
            raise BaseException(strMessage)
        if volume is None:
            self._volume = None
        elif volume.__class__.__name__ == "XSDataDoubleWithUnit":
            self._volume = volume
        else:
            strMessage = "ERROR! XSDataResultSaxsAnalysisModeling constructor argument 'volume' is not XSDataDoubleWithUnit but %s" % self._volume.__class__.__name__
            raise BaseException(strMessage)
        if scatterPlot is None:
            self._scatterPlot = None
        elif scatterPlot.__class__.__name__ == "XSDataFile":
            self._scatterPlot = scatterPlot
        else:
            strMessage = "ERROR! XSDataResultSaxsAnalysisModeling constructor argument 'scatterPlot' is not XSDataFile but %s" % self._scatterPlot.__class__.__name__
            raise BaseException(strMessage)
        if guinierPlot is None:
            self._guinierPlot = None
        elif guinierPlot.__class__.__name__ == "XSDataFile":
            self._guinierPlot = guinierPlot
        else:
            strMessage = "ERROR! XSDataResultSaxsAnalysisModeling constructor argument 'guinierPlot' is not XSDataFile but %s" % self._guinierPlot.__class__.__name__
            raise BaseException(strMessage)
        if kratkyPlot is None:
            self._kratkyPlot = None
        elif kratkyPlot.__class__.__name__ == "XSDataFile":
            self._kratkyPlot = kratkyPlot
        else:
            strMessage = "ERROR! XSDataResultSaxsAnalysisModeling constructor argument 'kratkyPlot' is not XSDataFile but %s" % self._kratkyPlot.__class__.__name__
            raise BaseException(strMessage)
        if densityPlot is None:
            self._densityPlot = None
        elif densityPlot.__class__.__name__ == "XSDataFile":
            self._densityPlot = densityPlot
        else:
            strMessage = "ERROR! XSDataResultSaxsAnalysisModeling constructor argument 'densityPlot' is not XSDataFile but %s" % self._densityPlot.__class__.__name__
            raise BaseException(strMessage)
        if dammifModels is None:
            self._dammifModels = []
        elif dammifModels.__class__.__name__ == "list":
            self._dammifModels = dammifModels
        else:
            strMessage = "ERROR! XSDataResultSaxsAnalysisModeling constructor argument 'dammifModels' is not list but %s" % self._dammifModels.__class__.__name__
            raise BaseException(strMessage)
        if damaverModel is None:
            self._damaverModel = None
        elif damaverModel.__class__.__name__ == "XSDataSaxsModel":
            self._damaverModel = damaverModel
        else:
            strMessage = "ERROR! XSDataResultSaxsAnalysisModeling constructor argument 'damaverModel' is not XSDataSaxsModel but %s" % self._damaverModel.__class__.__name__
            raise BaseException(strMessage)
        if damfiltModel is None:
            self._damfiltModel = None
        elif damfiltModel.__class__.__name__ == "XSDataSaxsModel":
            self._damfiltModel = damfiltModel
        else:
            strMessage = "ERROR! XSDataResultSaxsAnalysisModeling constructor argument 'damfiltModel' is not XSDataSaxsModel but %s" % self._damfiltModel.__class__.__name__
            raise BaseException(strMessage)
        if damstartModel is None:
            self._damstartModel = None
        elif damstartModel.__class__.__name__ == "XSDataSaxsModel":
            self._damstartModel = damstartModel
        else:
            strMessage = "ERROR! XSDataResultSaxsAnalysisModeling constructor argument 'damstartModel' is not XSDataSaxsModel but %s" % self._damstartModel.__class__.__name__
            raise BaseException(strMessage)
        if damminModel is None:
            self._damminModel = None
        elif damminModel.__class__.__name__ == "XSDataSaxsModel":
            self._damminModel = damminModel
        else:
            strMessage = "ERROR! XSDataResultSaxsAnalysisModeling constructor argument 'damminModel' is not XSDataSaxsModel but %s" % self._damminModel.__class__.__name__
            raise BaseException(strMessage)
        if chiRfactorPlot is None:
            self._chiRfactorPlot = None
        elif chiRfactorPlot.__class__.__name__ == "XSDataFile":
            self._chiRfactorPlot = chiRfactorPlot
        else:
            strMessage = "ERROR! XSDataResultSaxsAnalysisModeling constructor argument 'chiRfactorPlot' is not XSDataFile but %s" % self._chiRfactorPlot.__class__.__name__
            raise BaseException(strMessage)
        if nsdPlot is None:
            self._nsdPlot = None
        elif nsdPlot.__class__.__name__ == "XSDataFile":
            self._nsdPlot = nsdPlot
        else:
            strMessage = "ERROR! XSDataResultSaxsAnalysisModeling constructor argument 'nsdPlot' is not XSDataFile but %s" % self._nsdPlot.__class__.__name__
            raise BaseException(strMessage)
        if fitFile is None:
            self._fitFile = None
        elif fitFile.__class__.__name__ == "XSDataFile":
            self._fitFile = fitFile
        else:
            strMessage = "ERROR! XSDataResultSaxsAnalysisModeling constructor argument 'fitFile' is not XSDataFile but %s" % self._fitFile.__class__.__name__
            raise BaseException(strMessage)
        if logFile is None:
            self._logFile = None
        elif logFile.__class__.__name__ == "XSDataFile":
            self._logFile = logFile
        else:
            strMessage = "ERROR! XSDataResultSaxsAnalysisModeling constructor argument 'logFile' is not XSDataFile but %s" % self._logFile.__class__.__name__
            raise BaseException(strMessage)
        if pdbMoleculeFile is None:
            self._pdbMoleculeFile = None
        elif pdbMoleculeFile.__class__.__name__ == "XSDataFile":
            self._pdbMoleculeFile = pdbMoleculeFile
        else:
            strMessage = "ERROR! XSDataResultSaxsAnalysisModeling constructor argument 'pdbMoleculeFile' is not XSDataFile but %s" % self._pdbMoleculeFile.__class__.__name__
            raise BaseException(strMessage)
        if pdbSolventFile is None:
            self._pdbSolventFile = None
        elif pdbSolventFile.__class__.__name__ == "XSDataFile":
            self._pdbSolventFile = pdbSolventFile
        else:
            strMessage = "ERROR! XSDataResultSaxsAnalysisModeling constructor argument 'pdbSolventFile' is not XSDataFile but %s" % self._pdbSolventFile.__class__.__name__
            raise BaseException(strMessage)
    # Methods and properties for the 'autoRg' attribute
    def getAutoRg(self): return self._autoRg
    def setAutoRg(self, autoRg):
        if autoRg is None:
            self._autoRg = None
        elif autoRg.__class__.__name__ == "XSDataAutoRg":
            self._autoRg = autoRg
        else:
            strMessage = "ERROR! XSDataResultSaxsAnalysisModeling.setAutoRg argument is not XSDataAutoRg but %s" % autoRg.__class__.__name__
            raise BaseException(strMessage)
    def delAutoRg(self): self._autoRg = None
    autoRg = property(getAutoRg, setAutoRg, delAutoRg, "Property for autoRg")
    # Methods and properties for the 'gnom' attribute
    def getGnom(self): return self._gnom
    def setGnom(self, gnom):
        if gnom is None:
            self._gnom = None
        elif gnom.__class__.__name__ == "XSDataGnom":
            self._gnom = gnom
        else:
            strMessage = "ERROR! XSDataResultSaxsAnalysisModeling.setGnom argument is not XSDataGnom but %s" % gnom.__class__.__name__
            raise BaseException(strMessage)
    def delGnom(self): self._gnom = None
    gnom = property(getGnom, setGnom, delGnom, "Property for gnom")
    # Methods and properties for the 'volume' attribute
    def getVolume(self): return self._volume
    def setVolume(self, volume):
        if volume is None:
            self._volume = None
        elif volume.__class__.__name__ == "XSDataDoubleWithUnit":
            self._volume = volume
        else:
            strMessage = "ERROR! XSDataResultSaxsAnalysisModeling.setVolume argument is not XSDataDoubleWithUnit but %s" % volume.__class__.__name__
            raise BaseException(strMessage)
    def delVolume(self): self._volume = None
    volume = property(getVolume, setVolume, delVolume, "Property for volume")
    # Methods and properties for the 'scatterPlot' attribute
    def getScatterPlot(self): return self._scatterPlot
    def setScatterPlot(self, scatterPlot):
        if scatterPlot is None:
            self._scatterPlot = None
        elif scatterPlot.__class__.__name__ == "XSDataFile":
            self._scatterPlot = scatterPlot
        else:
            strMessage = "ERROR! XSDataResultSaxsAnalysisModeling.setScatterPlot argument is not XSDataFile but %s" % scatterPlot.__class__.__name__
            raise BaseException(strMessage)
    def delScatterPlot(self): self._scatterPlot = None
    scatterPlot = property(getScatterPlot, setScatterPlot, delScatterPlot, "Property for scatterPlot")
    # Methods and properties for the 'guinierPlot' attribute
    def getGuinierPlot(self): return self._guinierPlot
    def setGuinierPlot(self, guinierPlot):
        if guinierPlot is None:
            self._guinierPlot = None
        elif guinierPlot.__class__.__name__ == "XSDataFile":
            self._guinierPlot = guinierPlot
        else:
            strMessage = "ERROR! XSDataResultSaxsAnalysisModeling.setGuinierPlot argument is not XSDataFile but %s" % guinierPlot.__class__.__name__
            raise BaseException(strMessage)
    def delGuinierPlot(self): self._guinierPlot = None
    guinierPlot = property(getGuinierPlot, setGuinierPlot, delGuinierPlot, "Property for guinierPlot")
    # Methods and properties for the 'kratkyPlot' attribute
    def getKratkyPlot(self): return self._kratkyPlot
    def setKratkyPlot(self, kratkyPlot):
        if kratkyPlot is None:
            self._kratkyPlot = None
        elif kratkyPlot.__class__.__name__ == "XSDataFile":
            self._kratkyPlot = kratkyPlot
        else:
            strMessage = "ERROR! XSDataResultSaxsAnalysisModeling.setKratkyPlot argument is not XSDataFile but %s" % kratkyPlot.__class__.__name__
            raise BaseException(strMessage)
    def delKratkyPlot(self): self._kratkyPlot = None
    kratkyPlot = property(getKratkyPlot, setKratkyPlot, delKratkyPlot, "Property for kratkyPlot")
    # Methods and properties for the 'densityPlot' attribute
    def getDensityPlot(self): return self._densityPlot
    def setDensityPlot(self, densityPlot):
        if densityPlot is None:
            self._densityPlot = None
        elif densityPlot.__class__.__name__ == "XSDataFile":
            self._densityPlot = densityPlot
        else:
            strMessage = "ERROR! XSDataResultSaxsAnalysisModeling.setDensityPlot argument is not XSDataFile but %s" % densityPlot.__class__.__name__
            raise BaseException(strMessage)
    def delDensityPlot(self): self._densityPlot = None
    densityPlot = property(getDensityPlot, setDensityPlot, delDensityPlot, "Property for densityPlot")
    # Methods and properties for the 'dammifModels' attribute
    def getDammifModels(self): return self._dammifModels
    def setDammifModels(self, dammifModels):
        if dammifModels is None:
            self._dammifModels = []
        elif dammifModels.__class__.__name__ == "list":
            self._dammifModels = dammifModels
        else:
            strMessage = "ERROR! XSDataResultSaxsAnalysisModeling.setDammifModels argument is not list but %s" % dammifModels.__class__.__name__
            raise BaseException(strMessage)
    def delDammifModels(self): self._dammifModels = None
    dammifModels = property(getDammifModels, setDammifModels, delDammifModels, "Property for dammifModels")
    def addDammifModels(self, value):
        if value is None:
            strMessage = "ERROR! XSDataResultSaxsAnalysisModeling.addDammifModels argument is None"
            raise BaseException(strMessage)            
        elif value.__class__.__name__ == "XSDataSaxsModel":
            self._dammifModels.append(value)
        else:
            strMessage = "ERROR! XSDataResultSaxsAnalysisModeling.addDammifModels argument is not XSDataSaxsModel but %s" % value.__class__.__name__
            raise BaseException(strMessage)
    def insertDammifModels(self, index, value):
        if index is None:
            strMessage = "ERROR! XSDataResultSaxsAnalysisModeling.insertDammifModels argument 'index' is None"
            raise BaseException(strMessage)            
        if value is None:
            strMessage = "ERROR! XSDataResultSaxsAnalysisModeling.insertDammifModels argument 'value' is None"
            raise BaseException(strMessage)            
        elif value.__class__.__name__ == "XSDataSaxsModel":
            self._dammifModels[index] = value
        else:
            strMessage = "ERROR! XSDataResultSaxsAnalysisModeling.addDammifModels argument is not XSDataSaxsModel but %s" % value.__class__.__name__
            raise BaseException(strMessage)
    # Methods and properties for the 'damaverModel' attribute
    def getDamaverModel(self): return self._damaverModel
    def setDamaverModel(self, damaverModel):
        if damaverModel is None:
            self._damaverModel = None
        elif damaverModel.__class__.__name__ == "XSDataSaxsModel":
            self._damaverModel = damaverModel
        else:
            strMessage = "ERROR! XSDataResultSaxsAnalysisModeling.setDamaverModel argument is not XSDataSaxsModel but %s" % damaverModel.__class__.__name__
            raise BaseException(strMessage)
    def delDamaverModel(self): self._damaverModel = None
    damaverModel = property(getDamaverModel, setDamaverModel, delDamaverModel, "Property for damaverModel")
    # Methods and properties for the 'damfiltModel' attribute
    def getDamfiltModel(self): return self._damfiltModel
    def setDamfiltModel(self, damfiltModel):
        if damfiltModel is None:
            self._damfiltModel = None
        elif damfiltModel.__class__.__name__ == "XSDataSaxsModel":
            self._damfiltModel = damfiltModel
        else:
            strMessage = "ERROR! XSDataResultSaxsAnalysisModeling.setDamfiltModel argument is not XSDataSaxsModel but %s" % damfiltModel.__class__.__name__
            raise BaseException(strMessage)
    def delDamfiltModel(self): self._damfiltModel = None
    damfiltModel = property(getDamfiltModel, setDamfiltModel, delDamfiltModel, "Property for damfiltModel")
    # Methods and properties for the 'damstartModel' attribute
    def getDamstartModel(self): return self._damstartModel
    def setDamstartModel(self, damstartModel):
        if damstartModel is None:
            self._damstartModel = None
        elif damstartModel.__class__.__name__ == "XSDataSaxsModel":
            self._damstartModel = damstartModel
        else:
            strMessage = "ERROR! XSDataResultSaxsAnalysisModeling.setDamstartModel argument is not XSDataSaxsModel but %s" % damstartModel.__class__.__name__
            raise BaseException(strMessage)
    def delDamstartModel(self): self._damstartModel = None
    damstartModel = property(getDamstartModel, setDamstartModel, delDamstartModel, "Property for damstartModel")
    # Methods and properties for the 'damminModel' attribute
    def getDamminModel(self): return self._damminModel
    def setDamminModel(self, damminModel):
        if damminModel is None:
            self._damminModel = None
        elif damminModel.__class__.__name__ == "XSDataSaxsModel":
            self._damminModel = damminModel
        else:
            strMessage = "ERROR! XSDataResultSaxsAnalysisModeling.setDamminModel argument is not XSDataSaxsModel but %s" % damminModel.__class__.__name__
            raise BaseException(strMessage)
    def delDamminModel(self): self._damminModel = None
    damminModel = property(getDamminModel, setDamminModel, delDamminModel, "Property for damminModel")
    # Methods and properties for the 'chiRfactorPlot' attribute
    def getChiRfactorPlot(self): return self._chiRfactorPlot
    def setChiRfactorPlot(self, chiRfactorPlot):
        if chiRfactorPlot is None:
            self._chiRfactorPlot = None
        elif chiRfactorPlot.__class__.__name__ == "XSDataFile":
            self._chiRfactorPlot = chiRfactorPlot
        else:
            strMessage = "ERROR! XSDataResultSaxsAnalysisModeling.setChiRfactorPlot argument is not XSDataFile but %s" % chiRfactorPlot.__class__.__name__
            raise BaseException(strMessage)
    def delChiRfactorPlot(self): self._chiRfactorPlot = None
    chiRfactorPlot = property(getChiRfactorPlot, setChiRfactorPlot, delChiRfactorPlot, "Property for chiRfactorPlot")
    # Methods and properties for the 'nsdPlot' attribute
    def getNsdPlot(self): return self._nsdPlot
    def setNsdPlot(self, nsdPlot):
        if nsdPlot is None:
            self._nsdPlot = None
        elif nsdPlot.__class__.__name__ == "XSDataFile":
            self._nsdPlot = nsdPlot
        else:
            strMessage = "ERROR! XSDataResultSaxsAnalysisModeling.setNsdPlot argument is not XSDataFile but %s" % nsdPlot.__class__.__name__
            raise BaseException(strMessage)
    def delNsdPlot(self): self._nsdPlot = None
    nsdPlot = property(getNsdPlot, setNsdPlot, delNsdPlot, "Property for nsdPlot")
    # Methods and properties for the 'fitFile' attribute
    def getFitFile(self): return self._fitFile
    def setFitFile(self, fitFile):
        if fitFile is None:
            self._fitFile = None
        elif fitFile.__class__.__name__ == "XSDataFile":
            self._fitFile = fitFile
        else:
            strMessage = "ERROR! XSDataResultSaxsAnalysisModeling.setFitFile argument is not XSDataFile but %s" % fitFile.__class__.__name__
            raise BaseException(strMessage)
    def delFitFile(self): self._fitFile = None
    fitFile = property(getFitFile, setFitFile, delFitFile, "Property for fitFile")
    # Methods and properties for the 'logFile' attribute
    def getLogFile(self): return self._logFile
    def setLogFile(self, logFile):
        if logFile is None:
            self._logFile = None
        elif logFile.__class__.__name__ == "XSDataFile":
            self._logFile = logFile
        else:
            strMessage = "ERROR! XSDataResultSaxsAnalysisModeling.setLogFile argument is not XSDataFile but %s" % logFile.__class__.__name__
            raise BaseException(strMessage)
    def delLogFile(self): self._logFile = None
    logFile = property(getLogFile, setLogFile, delLogFile, "Property for logFile")
    # Methods and properties for the 'pdbMoleculeFile' attribute
    def getPdbMoleculeFile(self): return self._pdbMoleculeFile
    def setPdbMoleculeFile(self, pdbMoleculeFile):
        if pdbMoleculeFile is None:
            self._pdbMoleculeFile = None
        elif pdbMoleculeFile.__class__.__name__ == "XSDataFile":
            self._pdbMoleculeFile = pdbMoleculeFile
        else:
            strMessage = "ERROR! XSDataResultSaxsAnalysisModeling.setPdbMoleculeFile argument is not XSDataFile but %s" % pdbMoleculeFile.__class__.__name__
            raise BaseException(strMessage)
    def delPdbMoleculeFile(self): self._pdbMoleculeFile = None
    pdbMoleculeFile = property(getPdbMoleculeFile, setPdbMoleculeFile, delPdbMoleculeFile, "Property for pdbMoleculeFile")
    # Methods and properties for the 'pdbSolventFile' attribute
    def getPdbSolventFile(self): return self._pdbSolventFile
    def setPdbSolventFile(self, pdbSolventFile):
        if pdbSolventFile is None:
            self._pdbSolventFile = None
        elif pdbSolventFile.__class__.__name__ == "XSDataFile":
            self._pdbSolventFile = pdbSolventFile
        else:
            strMessage = "ERROR! XSDataResultSaxsAnalysisModeling.setPdbSolventFile argument is not XSDataFile but %s" % pdbSolventFile.__class__.__name__
            raise BaseException(strMessage)
    def delPdbSolventFile(self): self._pdbSolventFile = None
    pdbSolventFile = property(getPdbSolventFile, setPdbSolventFile, delPdbSolventFile, "Property for pdbSolventFile")
    def export(self, outfile, level, name_='XSDataResultSaxsAnalysisModeling'):
        showIndent(outfile, level)
        outfile.write(unicode('<%s>\n' % name_))
        self.exportChildren(outfile, level + 1, name_)
        showIndent(outfile, level)
        outfile.write(unicode('</%s>\n' % name_))
    def exportChildren(self, outfile, level, name_='XSDataResultSaxsAnalysisModeling'):
        XSDataResult.exportChildren(self, outfile, level, name_)
        if self._autoRg is not None:
            self.autoRg.export(outfile, level, name_='autoRg')
        else:
            warnEmptyAttribute("autoRg", "XSDataAutoRg")
        if self._gnom is not None:
            self.gnom.export(outfile, level, name_='gnom')
        else:
            warnEmptyAttribute("gnom", "XSDataGnom")
        if self._volume is not None:
            self.volume.export(outfile, level, name_='volume')
        else:
            warnEmptyAttribute("volume", "XSDataDoubleWithUnit")
        if self._scatterPlot is not None:
            self.scatterPlot.export(outfile, level, name_='scatterPlot')
        if self._guinierPlot is not None:
            self.guinierPlot.export(outfile, level, name_='guinierPlot')
        if self._kratkyPlot is not None:
            self.kratkyPlot.export(outfile, level, name_='kratkyPlot')
        if self._densityPlot is not None:
            self.densityPlot.export(outfile, level, name_='densityPlot')
        for dammifModels_ in self.getDammifModels():
            dammifModels_.export(outfile, level, name_='dammifModels')
        if self._damaverModel is not None:
            self.damaverModel.export(outfile, level, name_='damaverModel')
        if self._damfiltModel is not None:
            self.damfiltModel.export(outfile, level, name_='damfiltModel')
        if self._damstartModel is not None:
            self.damstartModel.export(outfile, level, name_='damstartModel')
        if self._damminModel is not None:
            self.damminModel.export(outfile, level, name_='damminModel')
        if self._chiRfactorPlot is not None:
            self.chiRfactorPlot.export(outfile, level, name_='chiRfactorPlot')
        else:
            warnEmptyAttribute("chiRfactorPlot", "XSDataFile")
        if self._nsdPlot is not None:
            self.nsdPlot.export(outfile, level, name_='nsdPlot')
        else:
            warnEmptyAttribute("nsdPlot", "XSDataFile")
        if self._fitFile is not None:
            self.fitFile.export(outfile, level, name_='fitFile')
        else:
            warnEmptyAttribute("fitFile", "XSDataFile")
        if self._logFile is not None:
            self.logFile.export(outfile, level, name_='logFile')
        else:
            warnEmptyAttribute("logFile", "XSDataFile")
        if self._pdbMoleculeFile is not None:
            self.pdbMoleculeFile.export(outfile, level, name_='pdbMoleculeFile')
        else:
            warnEmptyAttribute("pdbMoleculeFile", "XSDataFile")
        if self._pdbSolventFile is not None:
            self.pdbSolventFile.export(outfile, level, name_='pdbSolventFile')
        else:
            warnEmptyAttribute("pdbSolventFile", "XSDataFile")
    def build(self, node_):
        for child_ in node_.childNodes:
            nodeName_ = child_.nodeName.split(':')[-1]
            self.buildChildren(child_, nodeName_)
    def buildChildren(self, child_, nodeName_):
        if child_.nodeType == Node.ELEMENT_NODE and \
            nodeName_ == 'autoRg':
            obj_ = XSDataAutoRg()
            obj_.build(child_)
            self.setAutoRg(obj_)
        elif child_.nodeType == Node.ELEMENT_NODE and \
            nodeName_ == 'gnom':
            obj_ = XSDataGnom()
            obj_.build(child_)
            self.setGnom(obj_)
        elif child_.nodeType == Node.ELEMENT_NODE and \
            nodeName_ == 'volume':
            obj_ = XSDataDoubleWithUnit()
            obj_.build(child_)
            self.setVolume(obj_)
        elif child_.nodeType == Node.ELEMENT_NODE and \
            nodeName_ == 'scatterPlot':
            obj_ = XSDataFile()
            obj_.build(child_)
            self.setScatterPlot(obj_)
        elif child_.nodeType == Node.ELEMENT_NODE and \
            nodeName_ == 'guinierPlot':
            obj_ = XSDataFile()
            obj_.build(child_)
            self.setGuinierPlot(obj_)
        elif child_.nodeType == Node.ELEMENT_NODE and \
            nodeName_ == 'kratkyPlot':
            obj_ = XSDataFile()
            obj_.build(child_)
            self.setKratkyPlot(obj_)
        elif child_.nodeType == Node.ELEMENT_NODE and \
            nodeName_ == 'densityPlot':
            obj_ = XSDataFile()
            obj_.build(child_)
            self.setDensityPlot(obj_)
        elif child_.nodeType == Node.ELEMENT_NODE and \
            nodeName_ == 'dammifModels':
            obj_ = XSDataSaxsModel()
            obj_.build(child_)
            self.dammifModels.append(obj_)
        elif child_.nodeType == Node.ELEMENT_NODE and \
            nodeName_ == 'damaverModel':
            obj_ = XSDataSaxsModel()
            obj_.build(child_)
            self.setDamaverModel(obj_)
        elif child_.nodeType == Node.ELEMENT_NODE and \
            nodeName_ == 'damfiltModel':
            obj_ = XSDataSaxsModel()
            obj_.build(child_)
            self.setDamfiltModel(obj_)
        elif child_.nodeType == Node.ELEMENT_NODE and \
            nodeName_ == 'damstartModel':
            obj_ = XSDataSaxsModel()
            obj_.build(child_)
            self.setDamstartModel(obj_)
        elif child_.nodeType == Node.ELEMENT_NODE and \
            nodeName_ == 'damminModel':
            obj_ = XSDataSaxsModel()
            obj_.build(child_)
            self.setDamminModel(obj_)
        elif child_.nodeType == Node.ELEMENT_NODE and \
            nodeName_ == 'chiRfactorPlot':
            obj_ = XSDataFile()
            obj_.build(child_)
            self.setChiRfactorPlot(obj_)
        elif child_.nodeType == Node.ELEMENT_NODE and \
            nodeName_ == 'nsdPlot':
            obj_ = XSDataFile()
            obj_.build(child_)
            self.setNsdPlot(obj_)
        elif child_.nodeType == Node.ELEMENT_NODE and \
            nodeName_ == 'fitFile':
            obj_ = XSDataFile()
            obj_.build(child_)
            self.setFitFile(obj_)
        elif child_.nodeType == Node.ELEMENT_NODE and \
            nodeName_ == 'logFile':
            obj_ = XSDataFile()
            obj_.build(child_)
            self.setLogFile(obj_)
        elif child_.nodeType == Node.ELEMENT_NODE and \
            nodeName_ == 'pdbMoleculeFile':
            obj_ = XSDataFile()
            obj_.build(child_)
            self.setPdbMoleculeFile(obj_)
        elif child_.nodeType == Node.ELEMENT_NODE and \
            nodeName_ == 'pdbSolventFile':
            obj_ = XSDataFile()
            obj_.build(child_)
            self.setPdbSolventFile(obj_)
        XSDataResult.buildChildren(self, child_, nodeName_)
    #Method for marshalling an object
    def marshal( self ):
        oStreamString = StringIO()
        oStreamString.write(unicode('<?xml version="1.0" ?>\n'))
        self.export( oStreamString, 0, name_="XSDataResultSaxsAnalysisModeling" )
        oStringXML = oStreamString.getvalue()
        oStreamString.close()
        return oStringXML
    #Only to export the entire XML tree to a file stream on disk
    def exportToFile( self, _outfileName ):
        outfile = open( _outfileName, "w" )
        outfile.write(unicode('<?xml version=\"1.0\" ?>\n'))
        self.export( outfile, 0, name_='XSDataResultSaxsAnalysisModeling' )
        outfile.close()
    #Deprecated method, replaced by exportToFile
    def outputFile( self, _outfileName ):
        print("WARNING: Method outputFile in class XSDataResultSaxsAnalysisModeling is deprecated, please use instead exportToFile!")
        self.exportToFile(_outfileName)
    #Method for making a copy in a new instance
    def copy( self ):
        return XSDataResultSaxsAnalysisModeling.parseString(self.marshal())
    #Static method for parsing a string
    def parseString( _inString ):
        doc = minidom.parseString(_inString)
        rootNode = doc.documentElement
        rootObj = XSDataResultSaxsAnalysisModeling()
        rootObj.build(rootNode)
        # Check that all minOccurs are obeyed by marshalling the created object
        oStreamString = StringIO()
        rootObj.export( oStreamString, 0, name_="XSDataResultSaxsAnalysisModeling" )
        oStreamString.close()
        return rootObj
    parseString = staticmethod( parseString )
    #Static method for parsing a file
    def parseFile( _inFilePath ):
        doc = minidom.parse(_inFilePath)
        rootNode = doc.documentElement
        rootObj = XSDataResultSaxsAnalysisModeling()
        rootObj.build(rootNode)
        return rootObj
    parseFile = staticmethod( parseFile )
# end class XSDataResultSaxsAnalysisModeling


class XSDataResultSaxsModeling(XSDataResult):
    """Dammif -> Supcomb -> Damaver -> Damfilt -> Damstart -> Dammin pipeline"""
    def __init__(self, status=None, nsdPlot=None, chiRfactorPlot=None, pdbSolventFile=None, pdbMoleculeFile=None, logFile=None, fitFile=None, damminModel=None, damstartModel=None, damfiltModel=None, damaverModel=None, dammifModels=None):
        XSDataResult.__init__(self, status)
        if dammifModels is None:
            self._dammifModels = []
        elif dammifModels.__class__.__name__ == "list":
            self._dammifModels = dammifModels
        else:
            strMessage = "ERROR! XSDataResultSaxsModeling constructor argument 'dammifModels' is not list but %s" % self._dammifModels.__class__.__name__
            raise BaseException(strMessage)
        if damaverModel is None:
            self._damaverModel = None
        elif damaverModel.__class__.__name__ == "XSDataSaxsModel":
            self._damaverModel = damaverModel
        else:
            strMessage = "ERROR! XSDataResultSaxsModeling constructor argument 'damaverModel' is not XSDataSaxsModel but %s" % self._damaverModel.__class__.__name__
            raise BaseException(strMessage)
        if damfiltModel is None:
            self._damfiltModel = None
        elif damfiltModel.__class__.__name__ == "XSDataSaxsModel":
            self._damfiltModel = damfiltModel
        else:
            strMessage = "ERROR! XSDataResultSaxsModeling constructor argument 'damfiltModel' is not XSDataSaxsModel but %s" % self._damfiltModel.__class__.__name__
            raise BaseException(strMessage)
        if damstartModel is None:
            self._damstartModel = None
        elif damstartModel.__class__.__name__ == "XSDataSaxsModel":
            self._damstartModel = damstartModel
        else:
            strMessage = "ERROR! XSDataResultSaxsModeling constructor argument 'damstartModel' is not XSDataSaxsModel but %s" % self._damstartModel.__class__.__name__
            raise BaseException(strMessage)
        if damminModel is None:
            self._damminModel = None
        elif damminModel.__class__.__name__ == "XSDataSaxsModel":
            self._damminModel = damminModel
        else:
            strMessage = "ERROR! XSDataResultSaxsModeling constructor argument 'damminModel' is not XSDataSaxsModel but %s" % self._damminModel.__class__.__name__
            raise BaseException(strMessage)
        if fitFile is None:
            self._fitFile = None
        elif fitFile.__class__.__name__ == "XSDataFile":
            self._fitFile = fitFile
        else:
            strMessage = "ERROR! XSDataResultSaxsModeling constructor argument 'fitFile' is not XSDataFile but %s" % self._fitFile.__class__.__name__
            raise BaseException(strMessage)
        if logFile is None:
            self._logFile = None
        elif logFile.__class__.__name__ == "XSDataFile":
            self._logFile = logFile
        else:
            strMessage = "ERROR! XSDataResultSaxsModeling constructor argument 'logFile' is not XSDataFile but %s" % self._logFile.__class__.__name__
            raise BaseException(strMessage)
        if pdbMoleculeFile is None:
            self._pdbMoleculeFile = None
        elif pdbMoleculeFile.__class__.__name__ == "XSDataFile":
            self._pdbMoleculeFile = pdbMoleculeFile
        else:
            strMessage = "ERROR! XSDataResultSaxsModeling constructor argument 'pdbMoleculeFile' is not XSDataFile but %s" % self._pdbMoleculeFile.__class__.__name__
            raise BaseException(strMessage)
        if pdbSolventFile is None:
            self._pdbSolventFile = None
        elif pdbSolventFile.__class__.__name__ == "XSDataFile":
            self._pdbSolventFile = pdbSolventFile
        else:
            strMessage = "ERROR! XSDataResultSaxsModeling constructor argument 'pdbSolventFile' is not XSDataFile but %s" % self._pdbSolventFile.__class__.__name__
            raise BaseException(strMessage)
        if chiRfactorPlot is None:
            self._chiRfactorPlot = None
        elif chiRfactorPlot.__class__.__name__ == "XSDataFile":
            self._chiRfactorPlot = chiRfactorPlot
        else:
            strMessage = "ERROR! XSDataResultSaxsModeling constructor argument 'chiRfactorPlot' is not XSDataFile but %s" % self._chiRfactorPlot.__class__.__name__
            raise BaseException(strMessage)
        if nsdPlot is None:
            self._nsdPlot = None
        elif nsdPlot.__class__.__name__ == "XSDataFile":
            self._nsdPlot = nsdPlot
        else:
            strMessage = "ERROR! XSDataResultSaxsModeling constructor argument 'nsdPlot' is not XSDataFile but %s" % self._nsdPlot.__class__.__name__
            raise BaseException(strMessage)
    # Methods and properties for the 'dammifModels' attribute
    def getDammifModels(self): return self._dammifModels
    def setDammifModels(self, dammifModels):
        if dammifModels is None:
            self._dammifModels = []
        elif dammifModels.__class__.__name__ == "list":
            self._dammifModels = dammifModels
        else:
            strMessage = "ERROR! XSDataResultSaxsModeling.setDammifModels argument is not list but %s" % dammifModels.__class__.__name__
            raise BaseException(strMessage)
    def delDammifModels(self): self._dammifModels = None
    dammifModels = property(getDammifModels, setDammifModels, delDammifModels, "Property for dammifModels")
    def addDammifModels(self, value):
        if value is None:
            strMessage = "ERROR! XSDataResultSaxsModeling.addDammifModels argument is None"
            raise BaseException(strMessage)            
        elif value.__class__.__name__ == "XSDataSaxsModel":
            self._dammifModels.append(value)
        else:
            strMessage = "ERROR! XSDataResultSaxsModeling.addDammifModels argument is not XSDataSaxsModel but %s" % value.__class__.__name__
            raise BaseException(strMessage)
    def insertDammifModels(self, index, value):
        if index is None:
            strMessage = "ERROR! XSDataResultSaxsModeling.insertDammifModels argument 'index' is None"
            raise BaseException(strMessage)            
        if value is None:
            strMessage = "ERROR! XSDataResultSaxsModeling.insertDammifModels argument 'value' is None"
            raise BaseException(strMessage)            
        elif value.__class__.__name__ == "XSDataSaxsModel":
            self._dammifModels[index] = value
        else:
            strMessage = "ERROR! XSDataResultSaxsModeling.addDammifModels argument is not XSDataSaxsModel but %s" % value.__class__.__name__
            raise BaseException(strMessage)
    # Methods and properties for the 'damaverModel' attribute
    def getDamaverModel(self): return self._damaverModel
    def setDamaverModel(self, damaverModel):
        if damaverModel is None:
            self._damaverModel = None
        elif damaverModel.__class__.__name__ == "XSDataSaxsModel":
            self._damaverModel = damaverModel
        else:
            strMessage = "ERROR! XSDataResultSaxsModeling.setDamaverModel argument is not XSDataSaxsModel but %s" % damaverModel.__class__.__name__
            raise BaseException(strMessage)
    def delDamaverModel(self): self._damaverModel = None
    damaverModel = property(getDamaverModel, setDamaverModel, delDamaverModel, "Property for damaverModel")
    # Methods and properties for the 'damfiltModel' attribute
    def getDamfiltModel(self): return self._damfiltModel
    def setDamfiltModel(self, damfiltModel):
        if damfiltModel is None:
            self._damfiltModel = None
        elif damfiltModel.__class__.__name__ == "XSDataSaxsModel":
            self._damfiltModel = damfiltModel
        else:
            strMessage = "ERROR! XSDataResultSaxsModeling.setDamfiltModel argument is not XSDataSaxsModel but %s" % damfiltModel.__class__.__name__
            raise BaseException(strMessage)
    def delDamfiltModel(self): self._damfiltModel = None
    damfiltModel = property(getDamfiltModel, setDamfiltModel, delDamfiltModel, "Property for damfiltModel")
    # Methods and properties for the 'damstartModel' attribute
    def getDamstartModel(self): return self._damstartModel
    def setDamstartModel(self, damstartModel):
        if damstartModel is None:
            self._damstartModel = None
        elif damstartModel.__class__.__name__ == "XSDataSaxsModel":
            self._damstartModel = damstartModel
        else:
            strMessage = "ERROR! XSDataResultSaxsModeling.setDamstartModel argument is not XSDataSaxsModel but %s" % damstartModel.__class__.__name__
            raise BaseException(strMessage)
    def delDamstartModel(self): self._damstartModel = None
    damstartModel = property(getDamstartModel, setDamstartModel, delDamstartModel, "Property for damstartModel")
    # Methods and properties for the 'damminModel' attribute
    def getDamminModel(self): return self._damminModel
    def setDamminModel(self, damminModel):
        if damminModel is None:
            self._damminModel = None
        elif damminModel.__class__.__name__ == "XSDataSaxsModel":
            self._damminModel = damminModel
        else:
            strMessage = "ERROR! XSDataResultSaxsModeling.setDamminModel argument is not XSDataSaxsModel but %s" % damminModel.__class__.__name__
            raise BaseException(strMessage)
    def delDamminModel(self): self._damminModel = None
    damminModel = property(getDamminModel, setDamminModel, delDamminModel, "Property for damminModel")
    # Methods and properties for the 'fitFile' attribute
    def getFitFile(self): return self._fitFile
    def setFitFile(self, fitFile):
        if fitFile is None:
            self._fitFile = None
        elif fitFile.__class__.__name__ == "XSDataFile":
            self._fitFile = fitFile
        else:
            strMessage = "ERROR! XSDataResultSaxsModeling.setFitFile argument is not XSDataFile but %s" % fitFile.__class__.__name__
            raise BaseException(strMessage)
    def delFitFile(self): self._fitFile = None
    fitFile = property(getFitFile, setFitFile, delFitFile, "Property for fitFile")
    # Methods and properties for the 'logFile' attribute
    def getLogFile(self): return self._logFile
    def setLogFile(self, logFile):
        if logFile is None:
            self._logFile = None
        elif logFile.__class__.__name__ == "XSDataFile":
            self._logFile = logFile
        else:
            strMessage = "ERROR! XSDataResultSaxsModeling.setLogFile argument is not XSDataFile but %s" % logFile.__class__.__name__
            raise BaseException(strMessage)
    def delLogFile(self): self._logFile = None
    logFile = property(getLogFile, setLogFile, delLogFile, "Property for logFile")
    # Methods and properties for the 'pdbMoleculeFile' attribute
    def getPdbMoleculeFile(self): return self._pdbMoleculeFile
    def setPdbMoleculeFile(self, pdbMoleculeFile):
        if pdbMoleculeFile is None:
            self._pdbMoleculeFile = None
        elif pdbMoleculeFile.__class__.__name__ == "XSDataFile":
            self._pdbMoleculeFile = pdbMoleculeFile
        else:
            strMessage = "ERROR! XSDataResultSaxsModeling.setPdbMoleculeFile argument is not XSDataFile but %s" % pdbMoleculeFile.__class__.__name__
            raise BaseException(strMessage)
    def delPdbMoleculeFile(self): self._pdbMoleculeFile = None
    pdbMoleculeFile = property(getPdbMoleculeFile, setPdbMoleculeFile, delPdbMoleculeFile, "Property for pdbMoleculeFile")
    # Methods and properties for the 'pdbSolventFile' attribute
    def getPdbSolventFile(self): return self._pdbSolventFile
    def setPdbSolventFile(self, pdbSolventFile):
        if pdbSolventFile is None:
            self._pdbSolventFile = None
        elif pdbSolventFile.__class__.__name__ == "XSDataFile":
            self._pdbSolventFile = pdbSolventFile
        else:
            strMessage = "ERROR! XSDataResultSaxsModeling.setPdbSolventFile argument is not XSDataFile but %s" % pdbSolventFile.__class__.__name__
            raise BaseException(strMessage)
    def delPdbSolventFile(self): self._pdbSolventFile = None
    pdbSolventFile = property(getPdbSolventFile, setPdbSolventFile, delPdbSolventFile, "Property for pdbSolventFile")
    # Methods and properties for the 'chiRfactorPlot' attribute
    def getChiRfactorPlot(self): return self._chiRfactorPlot
    def setChiRfactorPlot(self, chiRfactorPlot):
        if chiRfactorPlot is None:
            self._chiRfactorPlot = None
        elif chiRfactorPlot.__class__.__name__ == "XSDataFile":
            self._chiRfactorPlot = chiRfactorPlot
        else:
            strMessage = "ERROR! XSDataResultSaxsModeling.setChiRfactorPlot argument is not XSDataFile but %s" % chiRfactorPlot.__class__.__name__
            raise BaseException(strMessage)
    def delChiRfactorPlot(self): self._chiRfactorPlot = None
    chiRfactorPlot = property(getChiRfactorPlot, setChiRfactorPlot, delChiRfactorPlot, "Property for chiRfactorPlot")
    # Methods and properties for the 'nsdPlot' attribute
    def getNsdPlot(self): return self._nsdPlot
    def setNsdPlot(self, nsdPlot):
        if nsdPlot is None:
            self._nsdPlot = None
        elif nsdPlot.__class__.__name__ == "XSDataFile":
            self._nsdPlot = nsdPlot
        else:
            strMessage = "ERROR! XSDataResultSaxsModeling.setNsdPlot argument is not XSDataFile but %s" % nsdPlot.__class__.__name__
            raise BaseException(strMessage)
    def delNsdPlot(self): self._nsdPlot = None
    nsdPlot = property(getNsdPlot, setNsdPlot, delNsdPlot, "Property for nsdPlot")
    def export(self, outfile, level, name_='XSDataResultSaxsModeling'):
        showIndent(outfile, level)
        outfile.write(unicode('<%s>\n' % name_))
        self.exportChildren(outfile, level + 1, name_)
        showIndent(outfile, level)
        outfile.write(unicode('</%s>\n' % name_))
    def exportChildren(self, outfile, level, name_='XSDataResultSaxsModeling'):
        XSDataResult.exportChildren(self, outfile, level, name_)
        for dammifModels_ in self.getDammifModels():
            dammifModels_.export(outfile, level, name_='dammifModels')
        if self._damaverModel is not None:
            self.damaverModel.export(outfile, level, name_='damaverModel')
        if self._damfiltModel is not None:
            self.damfiltModel.export(outfile, level, name_='damfiltModel')
        if self._damstartModel is not None:
            self.damstartModel.export(outfile, level, name_='damstartModel')
        if self._damminModel is not None:
            self.damminModel.export(outfile, level, name_='damminModel')
        if self._fitFile is not None:
            self.fitFile.export(outfile, level, name_='fitFile')
        if self._logFile is not None:
            self.logFile.export(outfile, level, name_='logFile')
        if self._pdbMoleculeFile is not None:
            self.pdbMoleculeFile.export(outfile, level, name_='pdbMoleculeFile')
        if self._pdbSolventFile is not None:
            self.pdbSolventFile.export(outfile, level, name_='pdbSolventFile')
        if self._chiRfactorPlot is not None:
            self.chiRfactorPlot.export(outfile, level, name_='chiRfactorPlot')
        else:
            warnEmptyAttribute("chiRfactorPlot", "XSDataFile")
        if self._nsdPlot is not None:
            self.nsdPlot.export(outfile, level, name_='nsdPlot')
        else:
            warnEmptyAttribute("nsdPlot", "XSDataFile")
    def build(self, node_):
        for child_ in node_.childNodes:
            nodeName_ = child_.nodeName.split(':')[-1]
            self.buildChildren(child_, nodeName_)
    def buildChildren(self, child_, nodeName_):
        if child_.nodeType == Node.ELEMENT_NODE and \
            nodeName_ == 'dammifModels':
            obj_ = XSDataSaxsModel()
            obj_.build(child_)
            self.dammifModels.append(obj_)
        elif child_.nodeType == Node.ELEMENT_NODE and \
            nodeName_ == 'damaverModel':
            obj_ = XSDataSaxsModel()
            obj_.build(child_)
            self.setDamaverModel(obj_)
        elif child_.nodeType == Node.ELEMENT_NODE and \
            nodeName_ == 'damfiltModel':
            obj_ = XSDataSaxsModel()
            obj_.build(child_)
            self.setDamfiltModel(obj_)
        elif child_.nodeType == Node.ELEMENT_NODE and \
            nodeName_ == 'damstartModel':
            obj_ = XSDataSaxsModel()
            obj_.build(child_)
            self.setDamstartModel(obj_)
        elif child_.nodeType == Node.ELEMENT_NODE and \
            nodeName_ == 'damminModel':
            obj_ = XSDataSaxsModel()
            obj_.build(child_)
            self.setDamminModel(obj_)
        elif child_.nodeType == Node.ELEMENT_NODE and \
            nodeName_ == 'fitFile':
            obj_ = XSDataFile()
            obj_.build(child_)
            self.setFitFile(obj_)
        elif child_.nodeType == Node.ELEMENT_NODE and \
            nodeName_ == 'logFile':
            obj_ = XSDataFile()
            obj_.build(child_)
            self.setLogFile(obj_)
        elif child_.nodeType == Node.ELEMENT_NODE and \
            nodeName_ == 'pdbMoleculeFile':
            obj_ = XSDataFile()
            obj_.build(child_)
            self.setPdbMoleculeFile(obj_)
        elif child_.nodeType == Node.ELEMENT_NODE and \
            nodeName_ == 'pdbSolventFile':
            obj_ = XSDataFile()
            obj_.build(child_)
            self.setPdbSolventFile(obj_)
        elif child_.nodeType == Node.ELEMENT_NODE and \
            nodeName_ == 'chiRfactorPlot':
            obj_ = XSDataFile()
            obj_.build(child_)
            self.setChiRfactorPlot(obj_)
        elif child_.nodeType == Node.ELEMENT_NODE and \
            nodeName_ == 'nsdPlot':
            obj_ = XSDataFile()
            obj_.build(child_)
            self.setNsdPlot(obj_)
        XSDataResult.buildChildren(self, child_, nodeName_)
    #Method for marshalling an object
    def marshal( self ):
        oStreamString = StringIO()
        oStreamString.write(unicode('<?xml version="1.0" ?>\n'))
        self.export( oStreamString, 0, name_="XSDataResultSaxsModeling" )
        oStringXML = oStreamString.getvalue()
        oStreamString.close()
        return oStringXML
    #Only to export the entire XML tree to a file stream on disk
    def exportToFile( self, _outfileName ):
        outfile = open( _outfileName, "w" )
        outfile.write(unicode('<?xml version=\"1.0\" ?>\n'))
        self.export( outfile, 0, name_='XSDataResultSaxsModeling' )
        outfile.close()
    #Deprecated method, replaced by exportToFile
    def outputFile( self, _outfileName ):
        print("WARNING: Method outputFile in class XSDataResultSaxsModeling is deprecated, please use instead exportToFile!")
        self.exportToFile(_outfileName)
    #Method for making a copy in a new instance
    def copy( self ):
        return XSDataResultSaxsModeling.parseString(self.marshal())
    #Static method for parsing a string
    def parseString( _inString ):
        doc = minidom.parseString(_inString)
        rootNode = doc.documentElement
        rootObj = XSDataResultSaxsModeling()
        rootObj.build(rootNode)
        # Check that all minOccurs are obeyed by marshalling the created object
        oStreamString = StringIO()
        rootObj.export( oStreamString, 0, name_="XSDataResultSaxsModeling" )
        oStreamString.close()
        return rootObj
    parseString = staticmethod( parseString )
    #Static method for parsing a file
    def parseFile( _inFilePath ):
        doc = minidom.parse(_inFilePath)
        rootNode = doc.documentElement
        rootObj = XSDataResultSaxsModeling()
        rootObj.build(rootNode)
        return rootObj
    parseFile = staticmethod( parseFile )
# end class XSDataResultSaxsModeling


class XSDataResultSaxsPipeline(XSDataResult):
    def __init__(self, status=None, autoRgOut=None):
        XSDataResult.__init__(self, status)
        if autoRgOut is None:
            self._autoRgOut = []
        elif autoRgOut.__class__.__name__ == "list":
            self._autoRgOut = autoRgOut
        else:
            strMessage = "ERROR! XSDataResultSaxsPipeline constructor argument 'autoRgOut' is not list but %s" % self._autoRgOut.__class__.__name__
            raise BaseException(strMessage)
    # Methods and properties for the 'autoRgOut' attribute
    def getAutoRgOut(self): return self._autoRgOut
    def setAutoRgOut(self, autoRgOut):
        if autoRgOut is None:
            self._autoRgOut = []
        elif autoRgOut.__class__.__name__ == "list":
            self._autoRgOut = autoRgOut
        else:
            strMessage = "ERROR! XSDataResultSaxsPipeline.setAutoRgOut argument is not list but %s" % autoRgOut.__class__.__name__
            raise BaseException(strMessage)
    def delAutoRgOut(self): self._autoRgOut = None
    autoRgOut = property(getAutoRgOut, setAutoRgOut, delAutoRgOut, "Property for autoRgOut")
    def addAutoRgOut(self, value):
        if value is None:
            strMessage = "ERROR! XSDataResultSaxsPipeline.addAutoRgOut argument is None"
            raise BaseException(strMessage)            
        elif value.__class__.__name__ == "XSDataAutoRg":
            self._autoRgOut.append(value)
        else:
            strMessage = "ERROR! XSDataResultSaxsPipeline.addAutoRgOut argument is not XSDataAutoRg but %s" % value.__class__.__name__
            raise BaseException(strMessage)
    def insertAutoRgOut(self, index, value):
        if index is None:
            strMessage = "ERROR! XSDataResultSaxsPipeline.insertAutoRgOut argument 'index' is None"
            raise BaseException(strMessage)            
        if value is None:
            strMessage = "ERROR! XSDataResultSaxsPipeline.insertAutoRgOut argument 'value' is None"
            raise BaseException(strMessage)            
        elif value.__class__.__name__ == "XSDataAutoRg":
            self._autoRgOut[index] = value
        else:
            strMessage = "ERROR! XSDataResultSaxsPipeline.addAutoRgOut argument is not XSDataAutoRg but %s" % value.__class__.__name__
            raise BaseException(strMessage)
    def export(self, outfile, level, name_='XSDataResultSaxsPipeline'):
        showIndent(outfile, level)
        outfile.write(unicode('<%s>\n' % name_))
        self.exportChildren(outfile, level + 1, name_)
        showIndent(outfile, level)
        outfile.write(unicode('</%s>\n' % name_))
    def exportChildren(self, outfile, level, name_='XSDataResultSaxsPipeline'):
        XSDataResult.exportChildren(self, outfile, level, name_)
        for autoRgOut_ in self.getAutoRgOut():
            autoRgOut_.export(outfile, level, name_='autoRgOut')
        if self.getAutoRgOut() == []:
            warnEmptyAttribute("autoRgOut", "XSDataAutoRg")
    def build(self, node_):
        for child_ in node_.childNodes:
            nodeName_ = child_.nodeName.split(':')[-1]
            self.buildChildren(child_, nodeName_)
    def buildChildren(self, child_, nodeName_):
        if child_.nodeType == Node.ELEMENT_NODE and \
            nodeName_ == 'autoRgOut':
            obj_ = XSDataAutoRg()
            obj_.build(child_)
            self.autoRgOut.append(obj_)
        XSDataResult.buildChildren(self, child_, nodeName_)
    #Method for marshalling an object
    def marshal( self ):
        oStreamString = StringIO()
        oStreamString.write(unicode('<?xml version="1.0" ?>\n'))
        self.export( oStreamString, 0, name_="XSDataResultSaxsPipeline" )
        oStringXML = oStreamString.getvalue()
        oStreamString.close()
        return oStringXML
    #Only to export the entire XML tree to a file stream on disk
    def exportToFile( self, _outfileName ):
        outfile = open( _outfileName, "w" )
        outfile.write(unicode('<?xml version=\"1.0\" ?>\n'))
        self.export( outfile, 0, name_='XSDataResultSaxsPipeline' )
        outfile.close()
    #Deprecated method, replaced by exportToFile
    def outputFile( self, _outfileName ):
        print("WARNING: Method outputFile in class XSDataResultSaxsPipeline is deprecated, please use instead exportToFile!")
        self.exportToFile(_outfileName)
    #Method for making a copy in a new instance
    def copy( self ):
        return XSDataResultSaxsPipeline.parseString(self.marshal())
    #Static method for parsing a string
    def parseString( _inString ):
        doc = minidom.parseString(_inString)
        rootNode = doc.documentElement
        rootObj = XSDataResultSaxsPipeline()
        rootObj.build(rootNode)
        # Check that all minOccurs are obeyed by marshalling the created object
        oStreamString = StringIO()
        rootObj.export( oStreamString, 0, name_="XSDataResultSaxsPipeline" )
        oStreamString.close()
        return rootObj
    parseString = staticmethod( parseString )
    #Static method for parsing a file
    def parseFile( _inFilePath ):
        doc = minidom.parse(_inFilePath)
        rootNode = doc.documentElement
        rootObj = XSDataResultSaxsPipeline()
        rootObj.build(rootNode)
        return rootObj
    parseFile = staticmethod( parseFile )
# end class XSDataResultSaxsPipeline


class XSDataResultSupcomb(XSDataResult):
    """model is new unified container for the saxs model"""
    def __init__(self, status=None, model=None, NSD=None, trns=None, rot=None, outputFilename=None):
        XSDataResult.__init__(self, status)
        if outputFilename is None:
            self._outputFilename = None
        elif outputFilename.__class__.__name__ == "XSDataFile":
            self._outputFilename = outputFilename
        else:
            strMessage = "ERROR! XSDataResultSupcomb constructor argument 'outputFilename' is not XSDataFile but %s" % self._outputFilename.__class__.__name__
            raise BaseException(strMessage)
        if rot is None:
            self._rot = None
        elif rot.__class__.__name__ == "XSDataRotation":
            self._rot = rot
        else:
            strMessage = "ERROR! XSDataResultSupcomb constructor argument 'rot' is not XSDataRotation but %s" % self._rot.__class__.__name__
            raise BaseException(strMessage)
        if trns is None:
            self._trns = None
        elif trns.__class__.__name__ == "XSDataVectorDouble":
            self._trns = trns
        else:
            strMessage = "ERROR! XSDataResultSupcomb constructor argument 'trns' is not XSDataVectorDouble but %s" % self._trns.__class__.__name__
            raise BaseException(strMessage)
        if NSD is None:
            self._NSD = None
        elif NSD.__class__.__name__ == "XSDataDouble":
            self._NSD = NSD
        else:
            strMessage = "ERROR! XSDataResultSupcomb constructor argument 'NSD' is not XSDataDouble but %s" % self._NSD.__class__.__name__
            raise BaseException(strMessage)
        if model is None:
            self._model = None
        elif model.__class__.__name__ == "XSDataSaxsModel":
            self._model = model
        else:
            strMessage = "ERROR! XSDataResultSupcomb constructor argument 'model' is not XSDataSaxsModel but %s" % self._model.__class__.__name__
            raise BaseException(strMessage)
    # Methods and properties for the 'outputFilename' attribute
    def getOutputFilename(self): return self._outputFilename
    def setOutputFilename(self, outputFilename):
        if outputFilename is None:
            self._outputFilename = None
        elif outputFilename.__class__.__name__ == "XSDataFile":
            self._outputFilename = outputFilename
        else:
            strMessage = "ERROR! XSDataResultSupcomb.setOutputFilename argument is not XSDataFile but %s" % outputFilename.__class__.__name__
            raise BaseException(strMessage)
    def delOutputFilename(self): self._outputFilename = None
    outputFilename = property(getOutputFilename, setOutputFilename, delOutputFilename, "Property for outputFilename")
    # Methods and properties for the 'rot' attribute
    def getRot(self): return self._rot
    def setRot(self, rot):
        if rot is None:
            self._rot = None
        elif rot.__class__.__name__ == "XSDataRotation":
            self._rot = rot
        else:
            strMessage = "ERROR! XSDataResultSupcomb.setRot argument is not XSDataRotation but %s" % rot.__class__.__name__
            raise BaseException(strMessage)
    def delRot(self): self._rot = None
    rot = property(getRot, setRot, delRot, "Property for rot")
    # Methods and properties for the 'trns' attribute
    def getTrns(self): return self._trns
    def setTrns(self, trns):
        if trns is None:
            self._trns = None
        elif trns.__class__.__name__ == "XSDataVectorDouble":
            self._trns = trns
        else:
            strMessage = "ERROR! XSDataResultSupcomb.setTrns argument is not XSDataVectorDouble but %s" % trns.__class__.__name__
            raise BaseException(strMessage)
    def delTrns(self): self._trns = None
    trns = property(getTrns, setTrns, delTrns, "Property for trns")
    # Methods and properties for the 'NSD' attribute
    def getNSD(self): return self._NSD
    def setNSD(self, NSD):
        if NSD is None:
            self._NSD = None
        elif NSD.__class__.__name__ == "XSDataDouble":
            self._NSD = NSD
        else:
            strMessage = "ERROR! XSDataResultSupcomb.setNSD argument is not XSDataDouble but %s" % NSD.__class__.__name__
            raise BaseException(strMessage)
    def delNSD(self): self._NSD = None
    NSD = property(getNSD, setNSD, delNSD, "Property for NSD")
    # Methods and properties for the 'model' attribute
    def getModel(self): return self._model
    def setModel(self, model):
        if model is None:
            self._model = None
        elif model.__class__.__name__ == "XSDataSaxsModel":
            self._model = model
        else:
            strMessage = "ERROR! XSDataResultSupcomb.setModel argument is not XSDataSaxsModel but %s" % model.__class__.__name__
            raise BaseException(strMessage)
    def delModel(self): self._model = None
    model = property(getModel, setModel, delModel, "Property for model")
    def export(self, outfile, level, name_='XSDataResultSupcomb'):
        showIndent(outfile, level)
        outfile.write(unicode('<%s>\n' % name_))
        self.exportChildren(outfile, level + 1, name_)
        showIndent(outfile, level)
        outfile.write(unicode('</%s>\n' % name_))
    def exportChildren(self, outfile, level, name_='XSDataResultSupcomb'):
        XSDataResult.exportChildren(self, outfile, level, name_)
        if self._outputFilename is not None:
            self.outputFilename.export(outfile, level, name_='outputFilename')
        else:
            warnEmptyAttribute("outputFilename", "XSDataFile")
        if self._rot is not None:
            self.rot.export(outfile, level, name_='rot')
        else:
            warnEmptyAttribute("rot", "XSDataRotation")
        if self._trns is not None:
            self.trns.export(outfile, level, name_='trns')
        else:
            warnEmptyAttribute("trns", "XSDataVectorDouble")
        if self._NSD is not None:
            self.NSD.export(outfile, level, name_='NSD')
        else:
            warnEmptyAttribute("NSD", "XSDataDouble")
        if self._model is not None:
            self.model.export(outfile, level, name_='model')
    def build(self, node_):
        for child_ in node_.childNodes:
            nodeName_ = child_.nodeName.split(':')[-1]
            self.buildChildren(child_, nodeName_)
    def buildChildren(self, child_, nodeName_):
        if child_.nodeType == Node.ELEMENT_NODE and \
            nodeName_ == 'outputFilename':
            obj_ = XSDataFile()
            obj_.build(child_)
            self.setOutputFilename(obj_)
        elif child_.nodeType == Node.ELEMENT_NODE and \
            nodeName_ == 'rot':
            obj_ = XSDataRotation()
            obj_.build(child_)
            self.setRot(obj_)
        elif child_.nodeType == Node.ELEMENT_NODE and \
            nodeName_ == 'trns':
            obj_ = XSDataVectorDouble()
            obj_.build(child_)
            self.setTrns(obj_)
        elif child_.nodeType == Node.ELEMENT_NODE and \
            nodeName_ == 'NSD':
            obj_ = XSDataDouble()
            obj_.build(child_)
            self.setNSD(obj_)
        elif child_.nodeType == Node.ELEMENT_NODE and \
            nodeName_ == 'model':
            obj_ = XSDataSaxsModel()
            obj_.build(child_)
            self.setModel(obj_)
        XSDataResult.buildChildren(self, child_, nodeName_)
    #Method for marshalling an object
    def marshal( self ):
        oStreamString = StringIO()
        oStreamString.write(unicode('<?xml version="1.0" ?>\n'))
        self.export( oStreamString, 0, name_="XSDataResultSupcomb" )
        oStringXML = oStreamString.getvalue()
        oStreamString.close()
        return oStringXML
    #Only to export the entire XML tree to a file stream on disk
    def exportToFile( self, _outfileName ):
        outfile = open( _outfileName, "w" )
        outfile.write(unicode('<?xml version=\"1.0\" ?>\n'))
        self.export( outfile, 0, name_='XSDataResultSupcomb' )
        outfile.close()
    #Deprecated method, replaced by exportToFile
    def outputFile( self, _outfileName ):
        print("WARNING: Method outputFile in class XSDataResultSupcomb is deprecated, please use instead exportToFile!")
        self.exportToFile(_outfileName)
    #Method for making a copy in a new instance
    def copy( self ):
        return XSDataResultSupcomb.parseString(self.marshal())
    #Static method for parsing a string
    def parseString( _inString ):
        doc = minidom.parseString(_inString)
        rootNode = doc.documentElement
        rootObj = XSDataResultSupcomb()
        rootObj.build(rootNode)
        # Check that all minOccurs are obeyed by marshalling the created object
        oStreamString = StringIO()
        rootObj.export( oStreamString, 0, name_="XSDataResultSupcomb" )
        oStreamString.close()
        return rootObj
    parseString = staticmethod( parseString )
    #Static method for parsing a file
    def parseFile( _inFilePath ):
        doc = minidom.parse(_inFilePath)
        rootNode = doc.documentElement
        rootObj = XSDataResultSupcomb()
        rootObj.build(rootNode)
        return rootObj
    parseFile = staticmethod( parseFile )
# end class XSDataResultSupcomb



# End of data representation classes.


