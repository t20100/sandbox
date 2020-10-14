#!/usr/bin/env python

# Taken from EDNA: license: GPL
# See https://github.com/kif/edna
#
# Generated Mon Jan 12 03:27::06 2015 by EDGenerateDS.
#

import os, sys
from xml.dom import minidom
from xml.dom import Node


strEdnaHome = os.environ.get("EDNA_HOME", None)

dictLocation = {
    "XSDataCommon": "kernel/datamodel",
    "XSDataEdnaSaxs": "ednaSaxs/datamodel",
}


try:
    from XSDataCommon import XSData
    from XSDataCommon import XSDataArray
    from XSDataCommon import XSDataBoolean
    from XSDataCommon import XSDataDouble
    from XSDataCommon import XSDataFile
    from XSDataCommon import XSDataInput
    from XSDataCommon import XSDataInteger
    from XSDataCommon import XSDataResult
    from XSDataCommon import XSDataString
    from XSDataEdnaSaxs import XSDataAutoRg
    from XSDataEdnaSaxs import XSDataGnom
    from XSDataEdnaSaxs import XSDataSaxsModel
    from XSDataCommon import XSDataDoubleWithUnit
    from XSDataCommon import XSDataImage
    from XSDataCommon import XSDataLength
    from XSDataCommon import XSDataTime
    from XSDataCommon import XSDataWavelength
except ImportError as error:
    if strEdnaHome is not None:
        for strXsdName in dictLocation:
            strXsdModule = strXsdName + ".py"
            strRootdir = os.path.dirname(
                os.path.abspath(os.path.join(strEdnaHome, dictLocation[strXsdName]))
            )
            for strRoot, listDirs, listFiles in os.walk(strRootdir):
                if strXsdModule in listFiles:
                    sys.path.append(strRoot)
    else:
        raise error
from XSDataCommon import XSData
from XSDataCommon import XSDataArray
from XSDataCommon import XSDataBoolean
from XSDataCommon import XSDataDouble
from XSDataCommon import XSDataFile
from XSDataCommon import XSDataInput
from XSDataCommon import XSDataInteger
from XSDataCommon import XSDataResult
from XSDataCommon import XSDataString
from XSDataEdnaSaxs import XSDataAutoRg
from XSDataEdnaSaxs import XSDataGnom
from XSDataEdnaSaxs import XSDataSaxsModel
from XSDataCommon import XSDataDoubleWithUnit
from XSDataCommon import XSDataImage
from XSDataCommon import XSDataLength
from XSDataCommon import XSDataTime
from XSDataCommon import XSDataWavelength


#
# Support/utility functions.
#

# Compabiltity between Python 2 and 3:
if sys.version.startswith("3"):
    unicode = str
    from io import StringIO
else:
    from StringIO import StringIO


def showIndent(outfile, level):
    for idx in range(level):
        outfile.write(unicode("    "))


def warnEmptyAttribute(_strName, _strTypeName):
    pass
    # if not _strTypeName in ["float", "double", "string", "boolean", "integer"]:
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
        else:  # category == MixedContainer.CategoryComplex
            self.value.export(outfile, level, name)

    def exportSimple(self, outfile, level, name):
        if self.content_type == MixedContainer.TypeString:
            outfile.write(unicode("<%s>%s</%s>" % (self.name, self.value, self.name)))
        elif (
            self.content_type == MixedContainer.TypeInteger
            or self.content_type == MixedContainer.TypeBoolean
        ):
            outfile.write(unicode("<%s>%d</%s>" % (self.name, self.value, self.name)))
        elif (
            self.content_type == MixedContainer.TypeFloat
            or self.content_type == MixedContainer.TypeDecimal
        ):
            outfile.write(unicode("<%s>%f</%s>" % (self.name, self.value, self.name)))
        elif self.content_type == MixedContainer.TypeDouble:
            outfile.write(unicode("<%s>%g</%s>" % (self.name, self.value, self.name)))


#
# Data representation classes.
#


class XSDataResultBioSaxsISPyBHPLCv1_0(object):
    def __init__(self, dataInputBioSaxs=None):
        if dataInputBioSaxs is None:
            self._dataInputBioSaxs = None
        elif dataInputBioSaxs.__class__.__name__ == "XSDataInputBioSaxsISPyBv1_0":
            self._dataInputBioSaxs = dataInputBioSaxs
        else:
            strMessage = (
                "ERROR! XSDataResultBioSaxsISPyBHPLCv1_0 constructor argument 'dataInputBioSaxs' is not XSDataInputBioSaxsISPyBv1_0 but %s"
                % self._dataInputBioSaxs.__class__.__name__
            )
            raise BaseException(strMessage)

    # Methods and properties for the 'dataInputBioSaxs' attribute
    def getDataInputBioSaxs(self):
        return self._dataInputBioSaxs

    def setDataInputBioSaxs(self, dataInputBioSaxs):
        if dataInputBioSaxs is None:
            self._dataInputBioSaxs = None
        elif dataInputBioSaxs.__class__.__name__ == "XSDataInputBioSaxsISPyBv1_0":
            self._dataInputBioSaxs = dataInputBioSaxs
        else:
            strMessage = (
                "ERROR! XSDataResultBioSaxsISPyBHPLCv1_0.setDataInputBioSaxs argument is not XSDataInputBioSaxsISPyBv1_0 but %s"
                % dataInputBioSaxs.__class__.__name__
            )
            raise BaseException(strMessage)

    def delDataInputBioSaxs(self):
        self._dataInputBioSaxs = None

    dataInputBioSaxs = property(
        getDataInputBioSaxs,
        setDataInputBioSaxs,
        delDataInputBioSaxs,
        "Property for dataInputBioSaxs",
    )

    def export(self, outfile, level, name_="XSDataResultBioSaxsISPyBHPLCv1_0"):
        showIndent(outfile, level)
        outfile.write(unicode("<%s>\n" % name_))
        self.exportChildren(outfile, level + 1, name_)
        showIndent(outfile, level)
        outfile.write(unicode("</%s>\n" % name_))

    def exportChildren(self, outfile, level, name_="XSDataResultBioSaxsISPyBHPLCv1_0"):
        pass
        if self._dataInputBioSaxs is not None:
            self.dataInputBioSaxs.export(outfile, level, name_="dataInputBioSaxs")
        else:
            warnEmptyAttribute("dataInputBioSaxs", "XSDataInputBioSaxsISPyBv1_0")

    def build(self, node_):
        for child_ in node_.childNodes:
            nodeName_ = child_.nodeName.split(":")[-1]
            self.buildChildren(child_, nodeName_)

    def buildChildren(self, child_, nodeName_):
        if child_.nodeType == Node.ELEMENT_NODE and nodeName_ == "dataInputBioSaxs":
            obj_ = XSDataInputBioSaxsISPyBv1_0()
            obj_.build(child_)
            self.setDataInputBioSaxs(obj_)

    # Method for marshalling an object
    def marshal(self):
        oStreamString = StringIO()
        oStreamString.write(unicode('<?xml version="1.0" ?>\n'))
        self.export(oStreamString, 0, name_="XSDataResultBioSaxsISPyBHPLCv1_0")
        oStringXML = oStreamString.getvalue()
        oStreamString.close()
        return oStringXML

    # Only to export the entire XML tree to a file stream on disk
    def exportToFile(self, _outfileName):
        outfile = open(_outfileName, "w")
        outfile.write(unicode('<?xml version="1.0" ?>\n'))
        self.export(outfile, 0, name_="XSDataResultBioSaxsISPyBHPLCv1_0")
        outfile.close()

    # Deprecated method, replaced by exportToFile
    def outputFile(self, _outfileName):
        print(
            "WARNING: Method outputFile in class XSDataResultBioSaxsISPyBHPLCv1_0 is deprecated, please use instead exportToFile!"
        )
        self.exportToFile(_outfileName)

    # Method for making a copy in a new instance
    def copy(self):
        return XSDataResultBioSaxsISPyBHPLCv1_0.parseString(self.marshal())

    # Static method for parsing a string
    def parseString(_inString):
        doc = minidom.parseString(_inString)
        rootNode = doc.documentElement
        rootObj = XSDataResultBioSaxsISPyBHPLCv1_0()
        rootObj.build(rootNode)
        # Check that all minOccurs are obeyed by marshalling the created object
        oStreamString = StringIO()
        rootObj.export(oStreamString, 0, name_="XSDataResultBioSaxsISPyBHPLCv1_0")
        oStreamString.close()
        return rootObj

    parseString = staticmethod(parseString)
    # Static method for parsing a file
    def parseFile(_inFilePath):
        doc = minidom.parse(_inFilePath)
        rootNode = doc.documentElement
        rootObj = XSDataResultBioSaxsISPyBHPLCv1_0()
        rootObj.build(rootNode)
        return rootObj

    parseFile = staticmethod(parseFile)


# end class XSDataResultBioSaxsISPyBHPLCv1_0


class XSDataBioSaxsExperimentSetup(XSData):
    def __init__(
        self,
        timeOfFrame=None,
        frameMax=None,
        frameNumber=None,
        exposureTime=None,
        exposureTemperature=None,
        storageTemperature=None,
        normalizationFactor=None,
        maskFile=None,
        machineCurrent=None,
        wavelength=None,
        beamStopDiode=None,
        beamCenter_2=None,
        beamCenter_1=None,
        pixelSize_2=None,
        pixelSize_1=None,
        detectorDistance=None,
        detector=None,
    ):
        XSData.__init__(
            self,
        )
        if detector is None:
            self._detector = None
        elif detector.__class__.__name__ == "XSDataString":
            self._detector = detector
        else:
            strMessage = (
                "ERROR! XSDataBioSaxsExperimentSetup constructor argument 'detector' is not XSDataString but %s"
                % self._detector.__class__.__name__
            )
            raise BaseException(strMessage)
        if detectorDistance is None:
            self._detectorDistance = None
        elif detectorDistance.__class__.__name__ == "XSDataLength":
            self._detectorDistance = detectorDistance
        else:
            strMessage = (
                "ERROR! XSDataBioSaxsExperimentSetup constructor argument 'detectorDistance' is not XSDataLength but %s"
                % self._detectorDistance.__class__.__name__
            )
            raise BaseException(strMessage)
        if pixelSize_1 is None:
            self._pixelSize_1 = None
        elif pixelSize_1.__class__.__name__ == "XSDataLength":
            self._pixelSize_1 = pixelSize_1
        else:
            strMessage = (
                "ERROR! XSDataBioSaxsExperimentSetup constructor argument 'pixelSize_1' is not XSDataLength but %s"
                % self._pixelSize_1.__class__.__name__
            )
            raise BaseException(strMessage)
        if pixelSize_2 is None:
            self._pixelSize_2 = None
        elif pixelSize_2.__class__.__name__ == "XSDataLength":
            self._pixelSize_2 = pixelSize_2
        else:
            strMessage = (
                "ERROR! XSDataBioSaxsExperimentSetup constructor argument 'pixelSize_2' is not XSDataLength but %s"
                % self._pixelSize_2.__class__.__name__
            )
            raise BaseException(strMessage)
        if beamCenter_1 is None:
            self._beamCenter_1 = None
        elif beamCenter_1.__class__.__name__ == "XSDataDouble":
            self._beamCenter_1 = beamCenter_1
        else:
            strMessage = (
                "ERROR! XSDataBioSaxsExperimentSetup constructor argument 'beamCenter_1' is not XSDataDouble but %s"
                % self._beamCenter_1.__class__.__name__
            )
            raise BaseException(strMessage)
        if beamCenter_2 is None:
            self._beamCenter_2 = None
        elif beamCenter_2.__class__.__name__ == "XSDataDouble":
            self._beamCenter_2 = beamCenter_2
        else:
            strMessage = (
                "ERROR! XSDataBioSaxsExperimentSetup constructor argument 'beamCenter_2' is not XSDataDouble but %s"
                % self._beamCenter_2.__class__.__name__
            )
            raise BaseException(strMessage)
        if beamStopDiode is None:
            self._beamStopDiode = None
        elif beamStopDiode.__class__.__name__ == "XSDataDouble":
            self._beamStopDiode = beamStopDiode
        else:
            strMessage = (
                "ERROR! XSDataBioSaxsExperimentSetup constructor argument 'beamStopDiode' is not XSDataDouble but %s"
                % self._beamStopDiode.__class__.__name__
            )
            raise BaseException(strMessage)
        if wavelength is None:
            self._wavelength = None
        elif wavelength.__class__.__name__ == "XSDataWavelength":
            self._wavelength = wavelength
        else:
            strMessage = (
                "ERROR! XSDataBioSaxsExperimentSetup constructor argument 'wavelength' is not XSDataWavelength but %s"
                % self._wavelength.__class__.__name__
            )
            raise BaseException(strMessage)
        if machineCurrent is None:
            self._machineCurrent = None
        elif machineCurrent.__class__.__name__ == "XSDataDouble":
            self._machineCurrent = machineCurrent
        else:
            strMessage = (
                "ERROR! XSDataBioSaxsExperimentSetup constructor argument 'machineCurrent' is not XSDataDouble but %s"
                % self._machineCurrent.__class__.__name__
            )
            raise BaseException(strMessage)
        if maskFile is None:
            self._maskFile = None
        elif maskFile.__class__.__name__ == "XSDataImage":
            self._maskFile = maskFile
        else:
            strMessage = (
                "ERROR! XSDataBioSaxsExperimentSetup constructor argument 'maskFile' is not XSDataImage but %s"
                % self._maskFile.__class__.__name__
            )
            raise BaseException(strMessage)
        if normalizationFactor is None:
            self._normalizationFactor = None
        elif normalizationFactor.__class__.__name__ == "XSDataDouble":
            self._normalizationFactor = normalizationFactor
        else:
            strMessage = (
                "ERROR! XSDataBioSaxsExperimentSetup constructor argument 'normalizationFactor' is not XSDataDouble but %s"
                % self._normalizationFactor.__class__.__name__
            )
            raise BaseException(strMessage)
        if storageTemperature is None:
            self._storageTemperature = None
        elif storageTemperature.__class__.__name__ == "XSDataDouble":
            self._storageTemperature = storageTemperature
        else:
            strMessage = (
                "ERROR! XSDataBioSaxsExperimentSetup constructor argument 'storageTemperature' is not XSDataDouble but %s"
                % self._storageTemperature.__class__.__name__
            )
            raise BaseException(strMessage)
        if exposureTemperature is None:
            self._exposureTemperature = None
        elif exposureTemperature.__class__.__name__ == "XSDataDouble":
            self._exposureTemperature = exposureTemperature
        else:
            strMessage = (
                "ERROR! XSDataBioSaxsExperimentSetup constructor argument 'exposureTemperature' is not XSDataDouble but %s"
                % self._exposureTemperature.__class__.__name__
            )
            raise BaseException(strMessage)
        if exposureTime is None:
            self._exposureTime = None
        elif exposureTime.__class__.__name__ == "XSDataTime":
            self._exposureTime = exposureTime
        else:
            strMessage = (
                "ERROR! XSDataBioSaxsExperimentSetup constructor argument 'exposureTime' is not XSDataTime but %s"
                % self._exposureTime.__class__.__name__
            )
            raise BaseException(strMessage)
        if frameNumber is None:
            self._frameNumber = None
        elif frameNumber.__class__.__name__ == "XSDataInteger":
            self._frameNumber = frameNumber
        else:
            strMessage = (
                "ERROR! XSDataBioSaxsExperimentSetup constructor argument 'frameNumber' is not XSDataInteger but %s"
                % self._frameNumber.__class__.__name__
            )
            raise BaseException(strMessage)
        if frameMax is None:
            self._frameMax = None
        elif frameMax.__class__.__name__ == "XSDataInteger":
            self._frameMax = frameMax
        else:
            strMessage = (
                "ERROR! XSDataBioSaxsExperimentSetup constructor argument 'frameMax' is not XSDataInteger but %s"
                % self._frameMax.__class__.__name__
            )
            raise BaseException(strMessage)
        if timeOfFrame is None:
            self._timeOfFrame = None
        elif timeOfFrame.__class__.__name__ == "XSDataTime":
            self._timeOfFrame = timeOfFrame
        else:
            strMessage = (
                "ERROR! XSDataBioSaxsExperimentSetup constructor argument 'timeOfFrame' is not XSDataTime but %s"
                % self._timeOfFrame.__class__.__name__
            )
            raise BaseException(strMessage)

    # Methods and properties for the 'detector' attribute
    def getDetector(self):
        return self._detector

    def setDetector(self, detector):
        if detector is None:
            self._detector = None
        elif detector.__class__.__name__ == "XSDataString":
            self._detector = detector
        else:
            strMessage = (
                "ERROR! XSDataBioSaxsExperimentSetup.setDetector argument is not XSDataString but %s"
                % detector.__class__.__name__
            )
            raise BaseException(strMessage)

    def delDetector(self):
        self._detector = None

    detector = property(getDetector, setDetector, delDetector, "Property for detector")
    # Methods and properties for the 'detectorDistance' attribute
    def getDetectorDistance(self):
        return self._detectorDistance

    def setDetectorDistance(self, detectorDistance):
        if detectorDistance is None:
            self._detectorDistance = None
        elif detectorDistance.__class__.__name__ == "XSDataLength":
            self._detectorDistance = detectorDistance
        else:
            strMessage = (
                "ERROR! XSDataBioSaxsExperimentSetup.setDetectorDistance argument is not XSDataLength but %s"
                % detectorDistance.__class__.__name__
            )
            raise BaseException(strMessage)

    def delDetectorDistance(self):
        self._detectorDistance = None

    detectorDistance = property(
        getDetectorDistance,
        setDetectorDistance,
        delDetectorDistance,
        "Property for detectorDistance",
    )
    # Methods and properties for the 'pixelSize_1' attribute
    def getPixelSize_1(self):
        return self._pixelSize_1

    def setPixelSize_1(self, pixelSize_1):
        if pixelSize_1 is None:
            self._pixelSize_1 = None
        elif pixelSize_1.__class__.__name__ == "XSDataLength":
            self._pixelSize_1 = pixelSize_1
        else:
            strMessage = (
                "ERROR! XSDataBioSaxsExperimentSetup.setPixelSize_1 argument is not XSDataLength but %s"
                % pixelSize_1.__class__.__name__
            )
            raise BaseException(strMessage)

    def delPixelSize_1(self):
        self._pixelSize_1 = None

    pixelSize_1 = property(
        getPixelSize_1, setPixelSize_1, delPixelSize_1, "Property for pixelSize_1"
    )
    # Methods and properties for the 'pixelSize_2' attribute
    def getPixelSize_2(self):
        return self._pixelSize_2

    def setPixelSize_2(self, pixelSize_2):
        if pixelSize_2 is None:
            self._pixelSize_2 = None
        elif pixelSize_2.__class__.__name__ == "XSDataLength":
            self._pixelSize_2 = pixelSize_2
        else:
            strMessage = (
                "ERROR! XSDataBioSaxsExperimentSetup.setPixelSize_2 argument is not XSDataLength but %s"
                % pixelSize_2.__class__.__name__
            )
            raise BaseException(strMessage)

    def delPixelSize_2(self):
        self._pixelSize_2 = None

    pixelSize_2 = property(
        getPixelSize_2, setPixelSize_2, delPixelSize_2, "Property for pixelSize_2"
    )
    # Methods and properties for the 'beamCenter_1' attribute
    def getBeamCenter_1(self):
        return self._beamCenter_1

    def setBeamCenter_1(self, beamCenter_1):
        if beamCenter_1 is None:
            self._beamCenter_1 = None
        elif beamCenter_1.__class__.__name__ == "XSDataDouble":
            self._beamCenter_1 = beamCenter_1
        else:
            strMessage = (
                "ERROR! XSDataBioSaxsExperimentSetup.setBeamCenter_1 argument is not XSDataDouble but %s"
                % beamCenter_1.__class__.__name__
            )
            raise BaseException(strMessage)

    def delBeamCenter_1(self):
        self._beamCenter_1 = None

    beamCenter_1 = property(
        getBeamCenter_1, setBeamCenter_1, delBeamCenter_1, "Property for beamCenter_1"
    )
    # Methods and properties for the 'beamCenter_2' attribute
    def getBeamCenter_2(self):
        return self._beamCenter_2

    def setBeamCenter_2(self, beamCenter_2):
        if beamCenter_2 is None:
            self._beamCenter_2 = None
        elif beamCenter_2.__class__.__name__ == "XSDataDouble":
            self._beamCenter_2 = beamCenter_2
        else:
            strMessage = (
                "ERROR! XSDataBioSaxsExperimentSetup.setBeamCenter_2 argument is not XSDataDouble but %s"
                % beamCenter_2.__class__.__name__
            )
            raise BaseException(strMessage)

    def delBeamCenter_2(self):
        self._beamCenter_2 = None

    beamCenter_2 = property(
        getBeamCenter_2, setBeamCenter_2, delBeamCenter_2, "Property for beamCenter_2"
    )
    # Methods and properties for the 'beamStopDiode' attribute
    def getBeamStopDiode(self):
        return self._beamStopDiode

    def setBeamStopDiode(self, beamStopDiode):
        if beamStopDiode is None:
            self._beamStopDiode = None
        elif beamStopDiode.__class__.__name__ == "XSDataDouble":
            self._beamStopDiode = beamStopDiode
        else:
            strMessage = (
                "ERROR! XSDataBioSaxsExperimentSetup.setBeamStopDiode argument is not XSDataDouble but %s"
                % beamStopDiode.__class__.__name__
            )
            raise BaseException(strMessage)

    def delBeamStopDiode(self):
        self._beamStopDiode = None

    beamStopDiode = property(
        getBeamStopDiode,
        setBeamStopDiode,
        delBeamStopDiode,
        "Property for beamStopDiode",
    )
    # Methods and properties for the 'wavelength' attribute
    def getWavelength(self):
        return self._wavelength

    def setWavelength(self, wavelength):
        if wavelength is None:
            self._wavelength = None
        elif wavelength.__class__.__name__ == "XSDataWavelength":
            self._wavelength = wavelength
        else:
            strMessage = (
                "ERROR! XSDataBioSaxsExperimentSetup.setWavelength argument is not XSDataWavelength but %s"
                % wavelength.__class__.__name__
            )
            raise BaseException(strMessage)

    def delWavelength(self):
        self._wavelength = None

    wavelength = property(
        getWavelength, setWavelength, delWavelength, "Property for wavelength"
    )
    # Methods and properties for the 'machineCurrent' attribute
    def getMachineCurrent(self):
        return self._machineCurrent

    def setMachineCurrent(self, machineCurrent):
        if machineCurrent is None:
            self._machineCurrent = None
        elif machineCurrent.__class__.__name__ == "XSDataDouble":
            self._machineCurrent = machineCurrent
        else:
            strMessage = (
                "ERROR! XSDataBioSaxsExperimentSetup.setMachineCurrent argument is not XSDataDouble but %s"
                % machineCurrent.__class__.__name__
            )
            raise BaseException(strMessage)

    def delMachineCurrent(self):
        self._machineCurrent = None

    machineCurrent = property(
        getMachineCurrent,
        setMachineCurrent,
        delMachineCurrent,
        "Property for machineCurrent",
    )
    # Methods and properties for the 'maskFile' attribute
    def getMaskFile(self):
        return self._maskFile

    def setMaskFile(self, maskFile):
        if maskFile is None:
            self._maskFile = None
        elif maskFile.__class__.__name__ == "XSDataImage":
            self._maskFile = maskFile
        else:
            strMessage = (
                "ERROR! XSDataBioSaxsExperimentSetup.setMaskFile argument is not XSDataImage but %s"
                % maskFile.__class__.__name__
            )
            raise BaseException(strMessage)

    def delMaskFile(self):
        self._maskFile = None

    maskFile = property(getMaskFile, setMaskFile, delMaskFile, "Property for maskFile")
    # Methods and properties for the 'normalizationFactor' attribute
    def getNormalizationFactor(self):
        return self._normalizationFactor

    def setNormalizationFactor(self, normalizationFactor):
        if normalizationFactor is None:
            self._normalizationFactor = None
        elif normalizationFactor.__class__.__name__ == "XSDataDouble":
            self._normalizationFactor = normalizationFactor
        else:
            strMessage = (
                "ERROR! XSDataBioSaxsExperimentSetup.setNormalizationFactor argument is not XSDataDouble but %s"
                % normalizationFactor.__class__.__name__
            )
            raise BaseException(strMessage)

    def delNormalizationFactor(self):
        self._normalizationFactor = None

    normalizationFactor = property(
        getNormalizationFactor,
        setNormalizationFactor,
        delNormalizationFactor,
        "Property for normalizationFactor",
    )
    # Methods and properties for the 'storageTemperature' attribute
    def getStorageTemperature(self):
        return self._storageTemperature

    def setStorageTemperature(self, storageTemperature):
        if storageTemperature is None:
            self._storageTemperature = None
        elif storageTemperature.__class__.__name__ == "XSDataDouble":
            self._storageTemperature = storageTemperature
        else:
            strMessage = (
                "ERROR! XSDataBioSaxsExperimentSetup.setStorageTemperature argument is not XSDataDouble but %s"
                % storageTemperature.__class__.__name__
            )
            raise BaseException(strMessage)

    def delStorageTemperature(self):
        self._storageTemperature = None

    storageTemperature = property(
        getStorageTemperature,
        setStorageTemperature,
        delStorageTemperature,
        "Property for storageTemperature",
    )
    # Methods and properties for the 'exposureTemperature' attribute
    def getExposureTemperature(self):
        return self._exposureTemperature

    def setExposureTemperature(self, exposureTemperature):
        if exposureTemperature is None:
            self._exposureTemperature = None
        elif exposureTemperature.__class__.__name__ == "XSDataDouble":
            self._exposureTemperature = exposureTemperature
        else:
            strMessage = (
                "ERROR! XSDataBioSaxsExperimentSetup.setExposureTemperature argument is not XSDataDouble but %s"
                % exposureTemperature.__class__.__name__
            )
            raise BaseException(strMessage)

    def delExposureTemperature(self):
        self._exposureTemperature = None

    exposureTemperature = property(
        getExposureTemperature,
        setExposureTemperature,
        delExposureTemperature,
        "Property for exposureTemperature",
    )
    # Methods and properties for the 'exposureTime' attribute
    def getExposureTime(self):
        return self._exposureTime

    def setExposureTime(self, exposureTime):
        if exposureTime is None:
            self._exposureTime = None
        elif exposureTime.__class__.__name__ == "XSDataTime":
            self._exposureTime = exposureTime
        else:
            strMessage = (
                "ERROR! XSDataBioSaxsExperimentSetup.setExposureTime argument is not XSDataTime but %s"
                % exposureTime.__class__.__name__
            )
            raise BaseException(strMessage)

    def delExposureTime(self):
        self._exposureTime = None

    exposureTime = property(
        getExposureTime, setExposureTime, delExposureTime, "Property for exposureTime"
    )
    # Methods and properties for the 'frameNumber' attribute
    def getFrameNumber(self):
        return self._frameNumber

    def setFrameNumber(self, frameNumber):
        if frameNumber is None:
            self._frameNumber = None
        elif frameNumber.__class__.__name__ == "XSDataInteger":
            self._frameNumber = frameNumber
        else:
            strMessage = (
                "ERROR! XSDataBioSaxsExperimentSetup.setFrameNumber argument is not XSDataInteger but %s"
                % frameNumber.__class__.__name__
            )
            raise BaseException(strMessage)

    def delFrameNumber(self):
        self._frameNumber = None

    frameNumber = property(
        getFrameNumber, setFrameNumber, delFrameNumber, "Property for frameNumber"
    )
    # Methods and properties for the 'frameMax' attribute
    def getFrameMax(self):
        return self._frameMax

    def setFrameMax(self, frameMax):
        if frameMax is None:
            self._frameMax = None
        elif frameMax.__class__.__name__ == "XSDataInteger":
            self._frameMax = frameMax
        else:
            strMessage = (
                "ERROR! XSDataBioSaxsExperimentSetup.setFrameMax argument is not XSDataInteger but %s"
                % frameMax.__class__.__name__
            )
            raise BaseException(strMessage)

    def delFrameMax(self):
        self._frameMax = None

    frameMax = property(getFrameMax, setFrameMax, delFrameMax, "Property for frameMax")
    # Methods and properties for the 'timeOfFrame' attribute
    def getTimeOfFrame(self):
        return self._timeOfFrame

    def setTimeOfFrame(self, timeOfFrame):
        if timeOfFrame is None:
            self._timeOfFrame = None
        elif timeOfFrame.__class__.__name__ == "XSDataTime":
            self._timeOfFrame = timeOfFrame
        else:
            strMessage = (
                "ERROR! XSDataBioSaxsExperimentSetup.setTimeOfFrame argument is not XSDataTime but %s"
                % timeOfFrame.__class__.__name__
            )
            raise BaseException(strMessage)

    def delTimeOfFrame(self):
        self._timeOfFrame = None

    timeOfFrame = property(
        getTimeOfFrame, setTimeOfFrame, delTimeOfFrame, "Property for timeOfFrame"
    )

    def export(self, outfile, level, name_="XSDataBioSaxsExperimentSetup"):
        showIndent(outfile, level)
        outfile.write(unicode("<%s>\n" % name_))
        self.exportChildren(outfile, level + 1, name_)
        showIndent(outfile, level)
        outfile.write(unicode("</%s>\n" % name_))

    def exportChildren(self, outfile, level, name_="XSDataBioSaxsExperimentSetup"):
        XSData.exportChildren(self, outfile, level, name_)
        if self._detector is not None:
            self.detector.export(outfile, level, name_="detector")
        if self._detectorDistance is not None:
            self.detectorDistance.export(outfile, level, name_="detectorDistance")
        if self._pixelSize_1 is not None:
            self.pixelSize_1.export(outfile, level, name_="pixelSize_1")
        if self._pixelSize_2 is not None:
            self.pixelSize_2.export(outfile, level, name_="pixelSize_2")
        if self._beamCenter_1 is not None:
            self.beamCenter_1.export(outfile, level, name_="beamCenter_1")
        if self._beamCenter_2 is not None:
            self.beamCenter_2.export(outfile, level, name_="beamCenter_2")
        if self._beamStopDiode is not None:
            self.beamStopDiode.export(outfile, level, name_="beamStopDiode")
        if self._wavelength is not None:
            self.wavelength.export(outfile, level, name_="wavelength")
        if self._machineCurrent is not None:
            self.machineCurrent.export(outfile, level, name_="machineCurrent")
        if self._maskFile is not None:
            self.maskFile.export(outfile, level, name_="maskFile")
        if self._normalizationFactor is not None:
            self.normalizationFactor.export(outfile, level, name_="normalizationFactor")
        if self._storageTemperature is not None:
            self.storageTemperature.export(outfile, level, name_="storageTemperature")
        if self._exposureTemperature is not None:
            self.exposureTemperature.export(outfile, level, name_="exposureTemperature")
        if self._exposureTime is not None:
            self.exposureTime.export(outfile, level, name_="exposureTime")
        if self._frameNumber is not None:
            self.frameNumber.export(outfile, level, name_="frameNumber")
        if self._frameMax is not None:
            self.frameMax.export(outfile, level, name_="frameMax")
        if self._timeOfFrame is not None:
            self.timeOfFrame.export(outfile, level, name_="timeOfFrame")

    def build(self, node_):
        for child_ in node_.childNodes:
            nodeName_ = child_.nodeName.split(":")[-1]
            self.buildChildren(child_, nodeName_)

    def buildChildren(self, child_, nodeName_):
        if child_.nodeType == Node.ELEMENT_NODE and nodeName_ == "detector":
            obj_ = XSDataString()
            obj_.build(child_)
            self.setDetector(obj_)
        elif child_.nodeType == Node.ELEMENT_NODE and nodeName_ == "detectorDistance":
            obj_ = XSDataLength()
            obj_.build(child_)
            self.setDetectorDistance(obj_)
        elif child_.nodeType == Node.ELEMENT_NODE and nodeName_ == "pixelSize_1":
            obj_ = XSDataLength()
            obj_.build(child_)
            self.setPixelSize_1(obj_)
        elif child_.nodeType == Node.ELEMENT_NODE and nodeName_ == "pixelSize_2":
            obj_ = XSDataLength()
            obj_.build(child_)
            self.setPixelSize_2(obj_)
        elif child_.nodeType == Node.ELEMENT_NODE and nodeName_ == "beamCenter_1":
            obj_ = XSDataDouble()
            obj_.build(child_)
            self.setBeamCenter_1(obj_)
        elif child_.nodeType == Node.ELEMENT_NODE and nodeName_ == "beamCenter_2":
            obj_ = XSDataDouble()
            obj_.build(child_)
            self.setBeamCenter_2(obj_)
        elif child_.nodeType == Node.ELEMENT_NODE and nodeName_ == "beamStopDiode":
            obj_ = XSDataDouble()
            obj_.build(child_)
            self.setBeamStopDiode(obj_)
        elif child_.nodeType == Node.ELEMENT_NODE and nodeName_ == "wavelength":
            obj_ = XSDataWavelength()
            obj_.build(child_)
            self.setWavelength(obj_)
        elif child_.nodeType == Node.ELEMENT_NODE and nodeName_ == "machineCurrent":
            obj_ = XSDataDouble()
            obj_.build(child_)
            self.setMachineCurrent(obj_)
        elif child_.nodeType == Node.ELEMENT_NODE and nodeName_ == "maskFile":
            obj_ = XSDataImage()
            obj_.build(child_)
            self.setMaskFile(obj_)
        elif (
            child_.nodeType == Node.ELEMENT_NODE and nodeName_ == "normalizationFactor"
        ):
            obj_ = XSDataDouble()
            obj_.build(child_)
            self.setNormalizationFactor(obj_)
        elif child_.nodeType == Node.ELEMENT_NODE and nodeName_ == "storageTemperature":
            obj_ = XSDataDouble()
            obj_.build(child_)
            self.setStorageTemperature(obj_)
        elif (
            child_.nodeType == Node.ELEMENT_NODE and nodeName_ == "exposureTemperature"
        ):
            obj_ = XSDataDouble()
            obj_.build(child_)
            self.setExposureTemperature(obj_)
        elif child_.nodeType == Node.ELEMENT_NODE and nodeName_ == "exposureTime":
            obj_ = XSDataTime()
            obj_.build(child_)
            self.setExposureTime(obj_)
        elif child_.nodeType == Node.ELEMENT_NODE and nodeName_ == "frameNumber":
            obj_ = XSDataInteger()
            obj_.build(child_)
            self.setFrameNumber(obj_)
        elif child_.nodeType == Node.ELEMENT_NODE and nodeName_ == "frameMax":
            obj_ = XSDataInteger()
            obj_.build(child_)
            self.setFrameMax(obj_)
        elif child_.nodeType == Node.ELEMENT_NODE and nodeName_ == "timeOfFrame":
            obj_ = XSDataTime()
            obj_.build(child_)
            self.setTimeOfFrame(obj_)
        XSData.buildChildren(self, child_, nodeName_)

    # Method for marshalling an object
    def marshal(self):
        oStreamString = StringIO()
        oStreamString.write(unicode('<?xml version="1.0" ?>\n'))
        self.export(oStreamString, 0, name_="XSDataBioSaxsExperimentSetup")
        oStringXML = oStreamString.getvalue()
        oStreamString.close()
        return oStringXML

    # Only to export the entire XML tree to a file stream on disk
    def exportToFile(self, _outfileName):
        outfile = open(_outfileName, "w")
        outfile.write(unicode('<?xml version="1.0" ?>\n'))
        self.export(outfile, 0, name_="XSDataBioSaxsExperimentSetup")
        outfile.close()

    # Deprecated method, replaced by exportToFile
    def outputFile(self, _outfileName):
        print(
            "WARNING: Method outputFile in class XSDataBioSaxsExperimentSetup is deprecated, please use instead exportToFile!"
        )
        self.exportToFile(_outfileName)

    # Method for making a copy in a new instance
    def copy(self):
        return XSDataBioSaxsExperimentSetup.parseString(self.marshal())

    # Static method for parsing a string
    def parseString(_inString):
        doc = minidom.parseString(_inString)
        rootNode = doc.documentElement
        rootObj = XSDataBioSaxsExperimentSetup()
        rootObj.build(rootNode)
        # Check that all minOccurs are obeyed by marshalling the created object
        oStreamString = StringIO()
        rootObj.export(oStreamString, 0, name_="XSDataBioSaxsExperimentSetup")
        oStreamString.close()
        return rootObj

    parseString = staticmethod(parseString)
    # Static method for parsing a file
    def parseFile(_inFilePath):
        doc = minidom.parse(_inFilePath)
        rootNode = doc.documentElement
        rootObj = XSDataBioSaxsExperimentSetup()
        rootObj.build(rootNode)
        return rootObj

    parseFile = staticmethod(parseFile)


# end class XSDataBioSaxsExperimentSetup


class XSDataBioSaxsSample(XSData):
    def __init__(
        self,
        ispybURL=None,
        ispybDestination=None,
        collectionOrder=None,
        measurementID=None,
        passwd=None,
        login=None,
        code=None,
        comments=None,
        concentration=None,
    ):
        XSData.__init__(
            self,
        )
        if concentration is None:
            self._concentration = None
        elif concentration.__class__.__name__ == "XSDataDouble":
            self._concentration = concentration
        else:
            strMessage = (
                "ERROR! XSDataBioSaxsSample constructor argument 'concentration' is not XSDataDouble but %s"
                % self._concentration.__class__.__name__
            )
            raise BaseException(strMessage)
        if comments is None:
            self._comments = None
        elif comments.__class__.__name__ == "XSDataString":
            self._comments = comments
        else:
            strMessage = (
                "ERROR! XSDataBioSaxsSample constructor argument 'comments' is not XSDataString but %s"
                % self._comments.__class__.__name__
            )
            raise BaseException(strMessage)
        if code is None:
            self._code = None
        elif code.__class__.__name__ == "XSDataString":
            self._code = code
        else:
            strMessage = (
                "ERROR! XSDataBioSaxsSample constructor argument 'code' is not XSDataString but %s"
                % self._code.__class__.__name__
            )
            raise BaseException(strMessage)
        if login is None:
            self._login = None
        elif login.__class__.__name__ == "XSDataString":
            self._login = login
        else:
            strMessage = (
                "ERROR! XSDataBioSaxsSample constructor argument 'login' is not XSDataString but %s"
                % self._login.__class__.__name__
            )
            raise BaseException(strMessage)
        if passwd is None:
            self._passwd = None
        elif passwd.__class__.__name__ == "XSDataString":
            self._passwd = passwd
        else:
            strMessage = (
                "ERROR! XSDataBioSaxsSample constructor argument 'passwd' is not XSDataString but %s"
                % self._passwd.__class__.__name__
            )
            raise BaseException(strMessage)
        if measurementID is None:
            self._measurementID = None
        elif measurementID.__class__.__name__ == "XSDataInteger":
            self._measurementID = measurementID
        else:
            strMessage = (
                "ERROR! XSDataBioSaxsSample constructor argument 'measurementID' is not XSDataInteger but %s"
                % self._measurementID.__class__.__name__
            )
            raise BaseException(strMessage)
        if collectionOrder is None:
            self._collectionOrder = None
        elif collectionOrder.__class__.__name__ == "XSDataInteger":
            self._collectionOrder = collectionOrder
        else:
            strMessage = (
                "ERROR! XSDataBioSaxsSample constructor argument 'collectionOrder' is not XSDataInteger but %s"
                % self._collectionOrder.__class__.__name__
            )
            raise BaseException(strMessage)
        if ispybDestination is None:
            self._ispybDestination = None
        elif ispybDestination.__class__.__name__ == "XSDataFile":
            self._ispybDestination = ispybDestination
        else:
            strMessage = (
                "ERROR! XSDataBioSaxsSample constructor argument 'ispybDestination' is not XSDataFile but %s"
                % self._ispybDestination.__class__.__name__
            )
            raise BaseException(strMessage)
        if ispybURL is None:
            self._ispybURL = None
        elif ispybURL.__class__.__name__ == "XSDataString":
            self._ispybURL = ispybURL
        else:
            strMessage = (
                "ERROR! XSDataBioSaxsSample constructor argument 'ispybURL' is not XSDataString but %s"
                % self._ispybURL.__class__.__name__
            )
            raise BaseException(strMessage)

    # Methods and properties for the 'concentration' attribute
    def getConcentration(self):
        return self._concentration

    def setConcentration(self, concentration):
        if concentration is None:
            self._concentration = None
        elif concentration.__class__.__name__ == "XSDataDouble":
            self._concentration = concentration
        else:
            strMessage = (
                "ERROR! XSDataBioSaxsSample.setConcentration argument is not XSDataDouble but %s"
                % concentration.__class__.__name__
            )
            raise BaseException(strMessage)

    def delConcentration(self):
        self._concentration = None

    concentration = property(
        getConcentration,
        setConcentration,
        delConcentration,
        "Property for concentration",
    )
    # Methods and properties for the 'comments' attribute
    def getComments(self):
        return self._comments

    def setComments(self, comments):
        if comments is None:
            self._comments = None
        elif comments.__class__.__name__ == "XSDataString":
            self._comments = comments
        else:
            strMessage = (
                "ERROR! XSDataBioSaxsSample.setComments argument is not XSDataString but %s"
                % comments.__class__.__name__
            )
            raise BaseException(strMessage)

    def delComments(self):
        self._comments = None

    comments = property(getComments, setComments, delComments, "Property for comments")
    # Methods and properties for the 'code' attribute
    def getCode(self):
        return self._code

    def setCode(self, code):
        if code is None:
            self._code = None
        elif code.__class__.__name__ == "XSDataString":
            self._code = code
        else:
            strMessage = (
                "ERROR! XSDataBioSaxsSample.setCode argument is not XSDataString but %s"
                % code.__class__.__name__
            )
            raise BaseException(strMessage)

    def delCode(self):
        self._code = None

    code = property(getCode, setCode, delCode, "Property for code")
    # Methods and properties for the 'login' attribute
    def getLogin(self):
        return self._login

    def setLogin(self, login):
        if login is None:
            self._login = None
        elif login.__class__.__name__ == "XSDataString":
            self._login = login
        else:
            strMessage = (
                "ERROR! XSDataBioSaxsSample.setLogin argument is not XSDataString but %s"
                % login.__class__.__name__
            )
            raise BaseException(strMessage)

    def delLogin(self):
        self._login = None

    login = property(getLogin, setLogin, delLogin, "Property for login")
    # Methods and properties for the 'passwd' attribute
    def getPasswd(self):
        return self._passwd

    def setPasswd(self, passwd):
        if passwd is None:
            self._passwd = None
        elif passwd.__class__.__name__ == "XSDataString":
            self._passwd = passwd
        else:
            strMessage = (
                "ERROR! XSDataBioSaxsSample.setPasswd argument is not XSDataString but %s"
                % passwd.__class__.__name__
            )
            raise BaseException(strMessage)

    def delPasswd(self):
        self._passwd = None

    passwd = property(getPasswd, setPasswd, delPasswd, "Property for passwd")
    # Methods and properties for the 'measurementID' attribute
    def getMeasurementID(self):
        return self._measurementID

    def setMeasurementID(self, measurementID):
        if measurementID is None:
            self._measurementID = None
        elif measurementID.__class__.__name__ == "XSDataInteger":
            self._measurementID = measurementID
        else:
            strMessage = (
                "ERROR! XSDataBioSaxsSample.setMeasurementID argument is not XSDataInteger but %s"
                % measurementID.__class__.__name__
            )
            raise BaseException(strMessage)

    def delMeasurementID(self):
        self._measurementID = None

    measurementID = property(
        getMeasurementID,
        setMeasurementID,
        delMeasurementID,
        "Property for measurementID",
    )
    # Methods and properties for the 'collectionOrder' attribute
    def getCollectionOrder(self):
        return self._collectionOrder

    def setCollectionOrder(self, collectionOrder):
        if collectionOrder is None:
            self._collectionOrder = None
        elif collectionOrder.__class__.__name__ == "XSDataInteger":
            self._collectionOrder = collectionOrder
        else:
            strMessage = (
                "ERROR! XSDataBioSaxsSample.setCollectionOrder argument is not XSDataInteger but %s"
                % collectionOrder.__class__.__name__
            )
            raise BaseException(strMessage)

    def delCollectionOrder(self):
        self._collectionOrder = None

    collectionOrder = property(
        getCollectionOrder,
        setCollectionOrder,
        delCollectionOrder,
        "Property for collectionOrder",
    )
    # Methods and properties for the 'ispybDestination' attribute
    def getIspybDestination(self):
        return self._ispybDestination

    def setIspybDestination(self, ispybDestination):
        if ispybDestination is None:
            self._ispybDestination = None
        elif ispybDestination.__class__.__name__ == "XSDataFile":
            self._ispybDestination = ispybDestination
        else:
            strMessage = (
                "ERROR! XSDataBioSaxsSample.setIspybDestination argument is not XSDataFile but %s"
                % ispybDestination.__class__.__name__
            )
            raise BaseException(strMessage)

    def delIspybDestination(self):
        self._ispybDestination = None

    ispybDestination = property(
        getIspybDestination,
        setIspybDestination,
        delIspybDestination,
        "Property for ispybDestination",
    )
    # Methods and properties for the 'ispybURL' attribute
    def getIspybURL(self):
        return self._ispybURL

    def setIspybURL(self, ispybURL):
        if ispybURL is None:
            self._ispybURL = None
        elif ispybURL.__class__.__name__ == "XSDataString":
            self._ispybURL = ispybURL
        else:
            strMessage = (
                "ERROR! XSDataBioSaxsSample.setIspybURL argument is not XSDataString but %s"
                % ispybURL.__class__.__name__
            )
            raise BaseException(strMessage)

    def delIspybURL(self):
        self._ispybURL = None

    ispybURL = property(getIspybURL, setIspybURL, delIspybURL, "Property for ispybURL")

    def export(self, outfile, level, name_="XSDataBioSaxsSample"):
        showIndent(outfile, level)
        outfile.write(unicode("<%s>\n" % name_))
        self.exportChildren(outfile, level + 1, name_)
        showIndent(outfile, level)
        outfile.write(unicode("</%s>\n" % name_))

    def exportChildren(self, outfile, level, name_="XSDataBioSaxsSample"):
        XSData.exportChildren(self, outfile, level, name_)
        if self._concentration is not None:
            self.concentration.export(outfile, level, name_="concentration")
        if self._comments is not None:
            self.comments.export(outfile, level, name_="comments")
        if self._code is not None:
            self.code.export(outfile, level, name_="code")
        if self._login is not None:
            self.login.export(outfile, level, name_="login")
        if self._passwd is not None:
            self.passwd.export(outfile, level, name_="passwd")
        if self._measurementID is not None:
            self.measurementID.export(outfile, level, name_="measurementID")
        if self._collectionOrder is not None:
            self.collectionOrder.export(outfile, level, name_="collectionOrder")
        if self._ispybDestination is not None:
            self.ispybDestination.export(outfile, level, name_="ispybDestination")
        if self._ispybURL is not None:
            self.ispybURL.export(outfile, level, name_="ispybURL")

    def build(self, node_):
        for child_ in node_.childNodes:
            nodeName_ = child_.nodeName.split(":")[-1]
            self.buildChildren(child_, nodeName_)

    def buildChildren(self, child_, nodeName_):
        if child_.nodeType == Node.ELEMENT_NODE and nodeName_ == "concentration":
            obj_ = XSDataDouble()
            obj_.build(child_)
            self.setConcentration(obj_)
        elif child_.nodeType == Node.ELEMENT_NODE and nodeName_ == "comments":
            obj_ = XSDataString()
            obj_.build(child_)
            self.setComments(obj_)
        elif child_.nodeType == Node.ELEMENT_NODE and nodeName_ == "code":
            obj_ = XSDataString()
            obj_.build(child_)
            self.setCode(obj_)
        elif child_.nodeType == Node.ELEMENT_NODE and nodeName_ == "login":
            obj_ = XSDataString()
            obj_.build(child_)
            self.setLogin(obj_)
        elif child_.nodeType == Node.ELEMENT_NODE and nodeName_ == "passwd":
            obj_ = XSDataString()
            obj_.build(child_)
            self.setPasswd(obj_)
        elif child_.nodeType == Node.ELEMENT_NODE and nodeName_ == "measurementID":
            obj_ = XSDataInteger()
            obj_.build(child_)
            self.setMeasurementID(obj_)
        elif child_.nodeType == Node.ELEMENT_NODE and nodeName_ == "collectionOrder":
            obj_ = XSDataInteger()
            obj_.build(child_)
            self.setCollectionOrder(obj_)
        elif child_.nodeType == Node.ELEMENT_NODE and nodeName_ == "ispybDestination":
            obj_ = XSDataFile()
            obj_.build(child_)
            self.setIspybDestination(obj_)
        elif child_.nodeType == Node.ELEMENT_NODE and nodeName_ == "ispybURL":
            obj_ = XSDataString()
            obj_.build(child_)
            self.setIspybURL(obj_)
        XSData.buildChildren(self, child_, nodeName_)

    # Method for marshalling an object
    def marshal(self):
        oStreamString = StringIO()
        oStreamString.write(unicode('<?xml version="1.0" ?>\n'))
        self.export(oStreamString, 0, name_="XSDataBioSaxsSample")
        oStringXML = oStreamString.getvalue()
        oStreamString.close()
        return oStringXML

    # Only to export the entire XML tree to a file stream on disk
    def exportToFile(self, _outfileName):
        outfile = open(_outfileName, "w")
        outfile.write(unicode('<?xml version="1.0" ?>\n'))
        self.export(outfile, 0, name_="XSDataBioSaxsSample")
        outfile.close()

    # Deprecated method, replaced by exportToFile
    def outputFile(self, _outfileName):
        print(
            "WARNING: Method outputFile in class XSDataBioSaxsSample is deprecated, please use instead exportToFile!"
        )
        self.exportToFile(_outfileName)

    # Method for making a copy in a new instance
    def copy(self):
        return XSDataBioSaxsSample.parseString(self.marshal())

    # Static method for parsing a string
    def parseString(_inString):
        doc = minidom.parseString(_inString)
        rootNode = doc.documentElement
        rootObj = XSDataBioSaxsSample()
        rootObj.build(rootNode)
        # Check that all minOccurs are obeyed by marshalling the created object
        oStreamString = StringIO()
        rootObj.export(oStreamString, 0, name_="XSDataBioSaxsSample")
        oStreamString.close()
        return rootObj

    parseString = staticmethod(parseString)
    # Static method for parsing a file
    def parseFile(_inFilePath):
        doc = minidom.parse(_inFilePath)
        rootNode = doc.documentElement
        rootObj = XSDataBioSaxsSample()
        rootObj.build(rootNode)
        return rootObj

    parseFile = staticmethod(parseFile)


# end class XSDataBioSaxsSample


class XSDataFileSeries(XSData):
    def __init__(self, files=None):
        XSData.__init__(
            self,
        )
        if files is None:
            self._files = []
        elif files.__class__.__name__ == "list":
            self._files = files
        else:
            strMessage = (
                "ERROR! XSDataFileSeries constructor argument 'files' is not list but %s"
                % self._files.__class__.__name__
            )
            raise BaseException(strMessage)

    # Methods and properties for the 'files' attribute
    def getFiles(self):
        return self._files

    def setFiles(self, files):
        if files is None:
            self._files = []
        elif files.__class__.__name__ == "list":
            self._files = files
        else:
            strMessage = (
                "ERROR! XSDataFileSeries.setFiles argument is not list but %s"
                % files.__class__.__name__
            )
            raise BaseException(strMessage)

    def delFiles(self):
        self._files = None

    files = property(getFiles, setFiles, delFiles, "Property for files")

    def addFiles(self, value):
        if value is None:
            strMessage = "ERROR! XSDataFileSeries.addFiles argument is None"
            raise BaseException(strMessage)
        elif value.__class__.__name__ == "XSDataFile":
            self._files.append(value)
        else:
            strMessage = (
                "ERROR! XSDataFileSeries.addFiles argument is not XSDataFile but %s"
                % value.__class__.__name__
            )
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
            strMessage = (
                "ERROR! XSDataFileSeries.addFiles argument is not XSDataFile but %s"
                % value.__class__.__name__
            )
            raise BaseException(strMessage)

    def export(self, outfile, level, name_="XSDataFileSeries"):
        showIndent(outfile, level)
        outfile.write(unicode("<%s>\n" % name_))
        self.exportChildren(outfile, level + 1, name_)
        showIndent(outfile, level)
        outfile.write(unicode("</%s>\n" % name_))

    def exportChildren(self, outfile, level, name_="XSDataFileSeries"):
        XSData.exportChildren(self, outfile, level, name_)
        for files_ in self.getFiles():
            files_.export(outfile, level, name_="files")
        if self.getFiles() == []:
            warnEmptyAttribute("files", "XSDataFile")

    def build(self, node_):
        for child_ in node_.childNodes:
            nodeName_ = child_.nodeName.split(":")[-1]
            self.buildChildren(child_, nodeName_)

    def buildChildren(self, child_, nodeName_):
        if child_.nodeType == Node.ELEMENT_NODE and nodeName_ == "files":
            obj_ = XSDataFile()
            obj_.build(child_)
            self.files.append(obj_)
        XSData.buildChildren(self, child_, nodeName_)

    # Method for marshalling an object
    def marshal(self):
        oStreamString = StringIO()
        oStreamString.write(unicode('<?xml version="1.0" ?>\n'))
        self.export(oStreamString, 0, name_="XSDataFileSeries")
        oStringXML = oStreamString.getvalue()
        oStreamString.close()
        return oStringXML

    # Only to export the entire XML tree to a file stream on disk
    def exportToFile(self, _outfileName):
        outfile = open(_outfileName, "w")
        outfile.write(unicode('<?xml version="1.0" ?>\n'))
        self.export(outfile, 0, name_="XSDataFileSeries")
        outfile.close()

    # Deprecated method, replaced by exportToFile
    def outputFile(self, _outfileName):
        print(
            "WARNING: Method outputFile in class XSDataFileSeries is deprecated, please use instead exportToFile!"
        )
        self.exportToFile(_outfileName)

    # Method for making a copy in a new instance
    def copy(self):
        return XSDataFileSeries.parseString(self.marshal())

    # Static method for parsing a string
    def parseString(_inString):
        doc = minidom.parseString(_inString)
        rootNode = doc.documentElement
        rootObj = XSDataFileSeries()
        rootObj.build(rootNode)
        # Check that all minOccurs are obeyed by marshalling the created object
        oStreamString = StringIO()
        rootObj.export(oStreamString, 0, name_="XSDataFileSeries")
        oStreamString.close()
        return rootObj

    parseString = staticmethod(parseString)
    # Static method for parsing a file
    def parseFile(_inFilePath):
        doc = minidom.parse(_inFilePath)
        rootNode = doc.documentElement
        rootObj = XSDataFileSeries()
        rootObj.build(rootNode)
        return rootObj

    parseFile = staticmethod(parseFile)


# end class XSDataFileSeries


class XSDataRamboTainer(XSData):
    def __init__(self, dmass=None, dqr=None, dvc=None, mass=None, qr=None, vc=None):
        XSData.__init__(
            self,
        )
        if vc is None:
            self._vc = None
        elif vc.__class__.__name__ == "XSDataDouble":
            self._vc = vc
        else:
            strMessage = (
                "ERROR! XSDataRamboTainer constructor argument 'vc' is not XSDataDouble but %s"
                % self._vc.__class__.__name__
            )
            raise BaseException(strMessage)
        if qr is None:
            self._qr = None
        elif qr.__class__.__name__ == "XSDataDouble":
            self._qr = qr
        else:
            strMessage = (
                "ERROR! XSDataRamboTainer constructor argument 'qr' is not XSDataDouble but %s"
                % self._qr.__class__.__name__
            )
            raise BaseException(strMessage)
        if mass is None:
            self._mass = None
        elif mass.__class__.__name__ == "XSDataDouble":
            self._mass = mass
        else:
            strMessage = (
                "ERROR! XSDataRamboTainer constructor argument 'mass' is not XSDataDouble but %s"
                % self._mass.__class__.__name__
            )
            raise BaseException(strMessage)
        if dvc is None:
            self._dvc = None
        elif dvc.__class__.__name__ == "XSDataDouble":
            self._dvc = dvc
        else:
            strMessage = (
                "ERROR! XSDataRamboTainer constructor argument 'dvc' is not XSDataDouble but %s"
                % self._dvc.__class__.__name__
            )
            raise BaseException(strMessage)
        if dqr is None:
            self._dqr = None
        elif dqr.__class__.__name__ == "XSDataDouble":
            self._dqr = dqr
        else:
            strMessage = (
                "ERROR! XSDataRamboTainer constructor argument 'dqr' is not XSDataDouble but %s"
                % self._dqr.__class__.__name__
            )
            raise BaseException(strMessage)
        if dmass is None:
            self._dmass = None
        elif dmass.__class__.__name__ == "XSDataDouble":
            self._dmass = dmass
        else:
            strMessage = (
                "ERROR! XSDataRamboTainer constructor argument 'dmass' is not XSDataDouble but %s"
                % self._dmass.__class__.__name__
            )
            raise BaseException(strMessage)

    # Methods and properties for the 'vc' attribute
    def getVc(self):
        return self._vc

    def setVc(self, vc):
        if vc is None:
            self._vc = None
        elif vc.__class__.__name__ == "XSDataDouble":
            self._vc = vc
        else:
            strMessage = (
                "ERROR! XSDataRamboTainer.setVc argument is not XSDataDouble but %s"
                % vc.__class__.__name__
            )
            raise BaseException(strMessage)

    def delVc(self):
        self._vc = None

    vc = property(getVc, setVc, delVc, "Property for vc")
    # Methods and properties for the 'qr' attribute
    def getQr(self):
        return self._qr

    def setQr(self, qr):
        if qr is None:
            self._qr = None
        elif qr.__class__.__name__ == "XSDataDouble":
            self._qr = qr
        else:
            strMessage = (
                "ERROR! XSDataRamboTainer.setQr argument is not XSDataDouble but %s"
                % qr.__class__.__name__
            )
            raise BaseException(strMessage)

    def delQr(self):
        self._qr = None

    qr = property(getQr, setQr, delQr, "Property for qr")
    # Methods and properties for the 'mass' attribute
    def getMass(self):
        return self._mass

    def setMass(self, mass):
        if mass is None:
            self._mass = None
        elif mass.__class__.__name__ == "XSDataDouble":
            self._mass = mass
        else:
            strMessage = (
                "ERROR! XSDataRamboTainer.setMass argument is not XSDataDouble but %s"
                % mass.__class__.__name__
            )
            raise BaseException(strMessage)

    def delMass(self):
        self._mass = None

    mass = property(getMass, setMass, delMass, "Property for mass")
    # Methods and properties for the 'dvc' attribute
    def getDvc(self):
        return self._dvc

    def setDvc(self, dvc):
        if dvc is None:
            self._dvc = None
        elif dvc.__class__.__name__ == "XSDataDouble":
            self._dvc = dvc
        else:
            strMessage = (
                "ERROR! XSDataRamboTainer.setDvc argument is not XSDataDouble but %s"
                % dvc.__class__.__name__
            )
            raise BaseException(strMessage)

    def delDvc(self):
        self._dvc = None

    dvc = property(getDvc, setDvc, delDvc, "Property for dvc")
    # Methods and properties for the 'dqr' attribute
    def getDqr(self):
        return self._dqr

    def setDqr(self, dqr):
        if dqr is None:
            self._dqr = None
        elif dqr.__class__.__name__ == "XSDataDouble":
            self._dqr = dqr
        else:
            strMessage = (
                "ERROR! XSDataRamboTainer.setDqr argument is not XSDataDouble but %s"
                % dqr.__class__.__name__
            )
            raise BaseException(strMessage)

    def delDqr(self):
        self._dqr = None

    dqr = property(getDqr, setDqr, delDqr, "Property for dqr")
    # Methods and properties for the 'dmass' attribute
    def getDmass(self):
        return self._dmass

    def setDmass(self, dmass):
        if dmass is None:
            self._dmass = None
        elif dmass.__class__.__name__ == "XSDataDouble":
            self._dmass = dmass
        else:
            strMessage = (
                "ERROR! XSDataRamboTainer.setDmass argument is not XSDataDouble but %s"
                % dmass.__class__.__name__
            )
            raise BaseException(strMessage)

    def delDmass(self):
        self._dmass = None

    dmass = property(getDmass, setDmass, delDmass, "Property for dmass")

    def export(self, outfile, level, name_="XSDataRamboTainer"):
        showIndent(outfile, level)
        outfile.write(unicode("<%s>\n" % name_))
        self.exportChildren(outfile, level + 1, name_)
        showIndent(outfile, level)
        outfile.write(unicode("</%s>\n" % name_))

    def exportChildren(self, outfile, level, name_="XSDataRamboTainer"):
        XSData.exportChildren(self, outfile, level, name_)
        if self._vc is not None:
            self.vc.export(outfile, level, name_="vc")
        if self._qr is not None:
            self.qr.export(outfile, level, name_="qr")
        if self._mass is not None:
            self.mass.export(outfile, level, name_="mass")
        if self._dvc is not None:
            self.dvc.export(outfile, level, name_="dvc")
        if self._dqr is not None:
            self.dqr.export(outfile, level, name_="dqr")
        if self._dmass is not None:
            self.dmass.export(outfile, level, name_="dmass")

    def build(self, node_):
        for child_ in node_.childNodes:
            nodeName_ = child_.nodeName.split(":")[-1]
            self.buildChildren(child_, nodeName_)

    def buildChildren(self, child_, nodeName_):
        if child_.nodeType == Node.ELEMENT_NODE and nodeName_ == "vc":
            obj_ = XSDataDouble()
            obj_.build(child_)
            self.setVc(obj_)
        elif child_.nodeType == Node.ELEMENT_NODE and nodeName_ == "qr":
            obj_ = XSDataDouble()
            obj_.build(child_)
            self.setQr(obj_)
        elif child_.nodeType == Node.ELEMENT_NODE and nodeName_ == "mass":
            obj_ = XSDataDouble()
            obj_.build(child_)
            self.setMass(obj_)
        elif child_.nodeType == Node.ELEMENT_NODE and nodeName_ == "dvc":
            obj_ = XSDataDouble()
            obj_.build(child_)
            self.setDvc(obj_)
        elif child_.nodeType == Node.ELEMENT_NODE and nodeName_ == "dqr":
            obj_ = XSDataDouble()
            obj_.build(child_)
            self.setDqr(obj_)
        elif child_.nodeType == Node.ELEMENT_NODE and nodeName_ == "dmass":
            obj_ = XSDataDouble()
            obj_.build(child_)
            self.setDmass(obj_)
        XSData.buildChildren(self, child_, nodeName_)

    # Method for marshalling an object
    def marshal(self):
        oStreamString = StringIO()
        oStreamString.write(unicode('<?xml version="1.0" ?>\n'))
        self.export(oStreamString, 0, name_="XSDataRamboTainer")
        oStringXML = oStreamString.getvalue()
        oStreamString.close()
        return oStringXML

    # Only to export the entire XML tree to a file stream on disk
    def exportToFile(self, _outfileName):
        outfile = open(_outfileName, "w")
        outfile.write(unicode('<?xml version="1.0" ?>\n'))
        self.export(outfile, 0, name_="XSDataRamboTainer")
        outfile.close()

    # Deprecated method, replaced by exportToFile
    def outputFile(self, _outfileName):
        print(
            "WARNING: Method outputFile in class XSDataRamboTainer is deprecated, please use instead exportToFile!"
        )
        self.exportToFile(_outfileName)

    # Method for making a copy in a new instance
    def copy(self):
        return XSDataRamboTainer.parseString(self.marshal())

    # Static method for parsing a string
    def parseString(_inString):
        doc = minidom.parseString(_inString)
        rootNode = doc.documentElement
        rootObj = XSDataRamboTainer()
        rootObj.build(rootNode)
        # Check that all minOccurs are obeyed by marshalling the created object
        oStreamString = StringIO()
        rootObj.export(oStreamString, 0, name_="XSDataRamboTainer")
        oStreamString.close()
        return rootObj

    parseString = staticmethod(parseString)
    # Static method for parsing a file
    def parseFile(_inFilePath):
        doc = minidom.parse(_inFilePath)
        rootNode = doc.documentElement
        rootObj = XSDataRamboTainer()
        rootObj.build(rootNode)
        return rootObj

    parseFile = staticmethod(parseFile)


# end class XSDataRamboTainer


class XSDataInputBioSaxsAsciiExportv1_0(XSDataInput):
    def __init__(
        self,
        configuration=None,
        experimentSetup=None,
        sample=None,
        integratedCurve=None,
        integratedImage=None,
    ):
        XSDataInput.__init__(self, configuration)
        if integratedImage is None:
            self._integratedImage = None
        elif integratedImage.__class__.__name__ == "XSDataImage":
            self._integratedImage = integratedImage
        else:
            strMessage = (
                "ERROR! XSDataInputBioSaxsAsciiExportv1_0 constructor argument 'integratedImage' is not XSDataImage but %s"
                % self._integratedImage.__class__.__name__
            )
            raise BaseException(strMessage)
        if integratedCurve is None:
            self._integratedCurve = None
        elif integratedCurve.__class__.__name__ == "XSDataFile":
            self._integratedCurve = integratedCurve
        else:
            strMessage = (
                "ERROR! XSDataInputBioSaxsAsciiExportv1_0 constructor argument 'integratedCurve' is not XSDataFile but %s"
                % self._integratedCurve.__class__.__name__
            )
            raise BaseException(strMessage)
        if sample is None:
            self._sample = None
        elif sample.__class__.__name__ == "XSDataBioSaxsSample":
            self._sample = sample
        else:
            strMessage = (
                "ERROR! XSDataInputBioSaxsAsciiExportv1_0 constructor argument 'sample' is not XSDataBioSaxsSample but %s"
                % self._sample.__class__.__name__
            )
            raise BaseException(strMessage)
        if experimentSetup is None:
            self._experimentSetup = None
        elif experimentSetup.__class__.__name__ == "XSDataBioSaxsExperimentSetup":
            self._experimentSetup = experimentSetup
        else:
            strMessage = (
                "ERROR! XSDataInputBioSaxsAsciiExportv1_0 constructor argument 'experimentSetup' is not XSDataBioSaxsExperimentSetup but %s"
                % self._experimentSetup.__class__.__name__
            )
            raise BaseException(strMessage)

    # Methods and properties for the 'integratedImage' attribute
    def getIntegratedImage(self):
        return self._integratedImage

    def setIntegratedImage(self, integratedImage):
        if integratedImage is None:
            self._integratedImage = None
        elif integratedImage.__class__.__name__ == "XSDataImage":
            self._integratedImage = integratedImage
        else:
            strMessage = (
                "ERROR! XSDataInputBioSaxsAsciiExportv1_0.setIntegratedImage argument is not XSDataImage but %s"
                % integratedImage.__class__.__name__
            )
            raise BaseException(strMessage)

    def delIntegratedImage(self):
        self._integratedImage = None

    integratedImage = property(
        getIntegratedImage,
        setIntegratedImage,
        delIntegratedImage,
        "Property for integratedImage",
    )
    # Methods and properties for the 'integratedCurve' attribute
    def getIntegratedCurve(self):
        return self._integratedCurve

    def setIntegratedCurve(self, integratedCurve):
        if integratedCurve is None:
            self._integratedCurve = None
        elif integratedCurve.__class__.__name__ == "XSDataFile":
            self._integratedCurve = integratedCurve
        else:
            strMessage = (
                "ERROR! XSDataInputBioSaxsAsciiExportv1_0.setIntegratedCurve argument is not XSDataFile but %s"
                % integratedCurve.__class__.__name__
            )
            raise BaseException(strMessage)

    def delIntegratedCurve(self):
        self._integratedCurve = None

    integratedCurve = property(
        getIntegratedCurve,
        setIntegratedCurve,
        delIntegratedCurve,
        "Property for integratedCurve",
    )
    # Methods and properties for the 'sample' attribute
    def getSample(self):
        return self._sample

    def setSample(self, sample):
        if sample is None:
            self._sample = None
        elif sample.__class__.__name__ == "XSDataBioSaxsSample":
            self._sample = sample
        else:
            strMessage = (
                "ERROR! XSDataInputBioSaxsAsciiExportv1_0.setSample argument is not XSDataBioSaxsSample but %s"
                % sample.__class__.__name__
            )
            raise BaseException(strMessage)

    def delSample(self):
        self._sample = None

    sample = property(getSample, setSample, delSample, "Property for sample")
    # Methods and properties for the 'experimentSetup' attribute
    def getExperimentSetup(self):
        return self._experimentSetup

    def setExperimentSetup(self, experimentSetup):
        if experimentSetup is None:
            self._experimentSetup = None
        elif experimentSetup.__class__.__name__ == "XSDataBioSaxsExperimentSetup":
            self._experimentSetup = experimentSetup
        else:
            strMessage = (
                "ERROR! XSDataInputBioSaxsAsciiExportv1_0.setExperimentSetup argument is not XSDataBioSaxsExperimentSetup but %s"
                % experimentSetup.__class__.__name__
            )
            raise BaseException(strMessage)

    def delExperimentSetup(self):
        self._experimentSetup = None

    experimentSetup = property(
        getExperimentSetup,
        setExperimentSetup,
        delExperimentSetup,
        "Property for experimentSetup",
    )

    def export(self, outfile, level, name_="XSDataInputBioSaxsAsciiExportv1_0"):
        showIndent(outfile, level)
        outfile.write(unicode("<%s>\n" % name_))
        self.exportChildren(outfile, level + 1, name_)
        showIndent(outfile, level)
        outfile.write(unicode("</%s>\n" % name_))

    def exportChildren(self, outfile, level, name_="XSDataInputBioSaxsAsciiExportv1_0"):
        XSDataInput.exportChildren(self, outfile, level, name_)
        if self._integratedImage is not None:
            self.integratedImage.export(outfile, level, name_="integratedImage")
        else:
            warnEmptyAttribute("integratedImage", "XSDataImage")
        if self._integratedCurve is not None:
            self.integratedCurve.export(outfile, level, name_="integratedCurve")
        else:
            warnEmptyAttribute("integratedCurve", "XSDataFile")
        if self._sample is not None:
            self.sample.export(outfile, level, name_="sample")
        if self._experimentSetup is not None:
            self.experimentSetup.export(outfile, level, name_="experimentSetup")

    def build(self, node_):
        for child_ in node_.childNodes:
            nodeName_ = child_.nodeName.split(":")[-1]
            self.buildChildren(child_, nodeName_)

    def buildChildren(self, child_, nodeName_):
        if child_.nodeType == Node.ELEMENT_NODE and nodeName_ == "integratedImage":
            obj_ = XSDataImage()
            obj_.build(child_)
            self.setIntegratedImage(obj_)
        elif child_.nodeType == Node.ELEMENT_NODE and nodeName_ == "integratedCurve":
            obj_ = XSDataFile()
            obj_.build(child_)
            self.setIntegratedCurve(obj_)
        elif child_.nodeType == Node.ELEMENT_NODE and nodeName_ == "sample":
            obj_ = XSDataBioSaxsSample()
            obj_.build(child_)
            self.setSample(obj_)
        elif child_.nodeType == Node.ELEMENT_NODE and nodeName_ == "experimentSetup":
            obj_ = XSDataBioSaxsExperimentSetup()
            obj_.build(child_)
            self.setExperimentSetup(obj_)
        XSDataInput.buildChildren(self, child_, nodeName_)

    # Method for marshalling an object
    def marshal(self):
        oStreamString = StringIO()
        oStreamString.write(unicode('<?xml version="1.0" ?>\n'))
        self.export(oStreamString, 0, name_="XSDataInputBioSaxsAsciiExportv1_0")
        oStringXML = oStreamString.getvalue()
        oStreamString.close()
        return oStringXML

    # Only to export the entire XML tree to a file stream on disk
    def exportToFile(self, _outfileName):
        outfile = open(_outfileName, "w")
        outfile.write(unicode('<?xml version="1.0" ?>\n'))
        self.export(outfile, 0, name_="XSDataInputBioSaxsAsciiExportv1_0")
        outfile.close()

    # Deprecated method, replaced by exportToFile
    def outputFile(self, _outfileName):
        print(
            "WARNING: Method outputFile in class XSDataInputBioSaxsAsciiExportv1_0 is deprecated, please use instead exportToFile!"
        )
        self.exportToFile(_outfileName)

    # Method for making a copy in a new instance
    def copy(self):
        return XSDataInputBioSaxsAsciiExportv1_0.parseString(self.marshal())

    # Static method for parsing a string
    def parseString(_inString):
        doc = minidom.parseString(_inString)
        rootNode = doc.documentElement
        rootObj = XSDataInputBioSaxsAsciiExportv1_0()
        rootObj.build(rootNode)
        # Check that all minOccurs are obeyed by marshalling the created object
        oStreamString = StringIO()
        rootObj.export(oStreamString, 0, name_="XSDataInputBioSaxsAsciiExportv1_0")
        oStreamString.close()
        return rootObj

    parseString = staticmethod(parseString)
    # Static method for parsing a file
    def parseFile(_inFilePath):
        doc = minidom.parse(_inFilePath)
        rootNode = doc.documentElement
        rootObj = XSDataInputBioSaxsAsciiExportv1_0()
        rootObj.build(rootNode)
        return rootObj

    parseFile = staticmethod(parseFile)


# end class XSDataInputBioSaxsAsciiExportv1_0


class XSDataInputBioSaxsAzimutIntv1_0(XSDataInput):
    def __init__(
        self,
        configuration=None,
        experimentSetup=None,
        sample=None,
        correctedImage=None,
        integratedCurve=None,
        integratedImage=None,
        normalizedImageSize=None,
        normalizedImage=None,
    ):
        XSDataInput.__init__(self, configuration)
        if normalizedImage is None:
            self._normalizedImage = None
        elif normalizedImage.__class__.__name__ == "XSDataImage":
            self._normalizedImage = normalizedImage
        else:
            strMessage = (
                "ERROR! XSDataInputBioSaxsAzimutIntv1_0 constructor argument 'normalizedImage' is not XSDataImage but %s"
                % self._normalizedImage.__class__.__name__
            )
            raise BaseException(strMessage)
        if normalizedImageSize is None:
            self._normalizedImageSize = None
        elif normalizedImageSize.__class__.__name__ == "XSDataInteger":
            self._normalizedImageSize = normalizedImageSize
        else:
            strMessage = (
                "ERROR! XSDataInputBioSaxsAzimutIntv1_0 constructor argument 'normalizedImageSize' is not XSDataInteger but %s"
                % self._normalizedImageSize.__class__.__name__
            )
            raise BaseException(strMessage)
        if integratedImage is None:
            self._integratedImage = None
        elif integratedImage.__class__.__name__ == "XSDataImage":
            self._integratedImage = integratedImage
        else:
            strMessage = (
                "ERROR! XSDataInputBioSaxsAzimutIntv1_0 constructor argument 'integratedImage' is not XSDataImage but %s"
                % self._integratedImage.__class__.__name__
            )
            raise BaseException(strMessage)
        if integratedCurve is None:
            self._integratedCurve = None
        elif integratedCurve.__class__.__name__ == "XSDataFile":
            self._integratedCurve = integratedCurve
        else:
            strMessage = (
                "ERROR! XSDataInputBioSaxsAzimutIntv1_0 constructor argument 'integratedCurve' is not XSDataFile but %s"
                % self._integratedCurve.__class__.__name__
            )
            raise BaseException(strMessage)
        if correctedImage is None:
            self._correctedImage = None
        elif correctedImage.__class__.__name__ == "XSDataImage":
            self._correctedImage = correctedImage
        else:
            strMessage = (
                "ERROR! XSDataInputBioSaxsAzimutIntv1_0 constructor argument 'correctedImage' is not XSDataImage but %s"
                % self._correctedImage.__class__.__name__
            )
            raise BaseException(strMessage)
        if sample is None:
            self._sample = None
        elif sample.__class__.__name__ == "XSDataBioSaxsSample":
            self._sample = sample
        else:
            strMessage = (
                "ERROR! XSDataInputBioSaxsAzimutIntv1_0 constructor argument 'sample' is not XSDataBioSaxsSample but %s"
                % self._sample.__class__.__name__
            )
            raise BaseException(strMessage)
        if experimentSetup is None:
            self._experimentSetup = None
        elif experimentSetup.__class__.__name__ == "XSDataBioSaxsExperimentSetup":
            self._experimentSetup = experimentSetup
        else:
            strMessage = (
                "ERROR! XSDataInputBioSaxsAzimutIntv1_0 constructor argument 'experimentSetup' is not XSDataBioSaxsExperimentSetup but %s"
                % self._experimentSetup.__class__.__name__
            )
            raise BaseException(strMessage)

    # Methods and properties for the 'normalizedImage' attribute
    def getNormalizedImage(self):
        return self._normalizedImage

    def setNormalizedImage(self, normalizedImage):
        if normalizedImage is None:
            self._normalizedImage = None
        elif normalizedImage.__class__.__name__ == "XSDataImage":
            self._normalizedImage = normalizedImage
        else:
            strMessage = (
                "ERROR! XSDataInputBioSaxsAzimutIntv1_0.setNormalizedImage argument is not XSDataImage but %s"
                % normalizedImage.__class__.__name__
            )
            raise BaseException(strMessage)

    def delNormalizedImage(self):
        self._normalizedImage = None

    normalizedImage = property(
        getNormalizedImage,
        setNormalizedImage,
        delNormalizedImage,
        "Property for normalizedImage",
    )
    # Methods and properties for the 'normalizedImageSize' attribute
    def getNormalizedImageSize(self):
        return self._normalizedImageSize

    def setNormalizedImageSize(self, normalizedImageSize):
        if normalizedImageSize is None:
            self._normalizedImageSize = None
        elif normalizedImageSize.__class__.__name__ == "XSDataInteger":
            self._normalizedImageSize = normalizedImageSize
        else:
            strMessage = (
                "ERROR! XSDataInputBioSaxsAzimutIntv1_0.setNormalizedImageSize argument is not XSDataInteger but %s"
                % normalizedImageSize.__class__.__name__
            )
            raise BaseException(strMessage)

    def delNormalizedImageSize(self):
        self._normalizedImageSize = None

    normalizedImageSize = property(
        getNormalizedImageSize,
        setNormalizedImageSize,
        delNormalizedImageSize,
        "Property for normalizedImageSize",
    )
    # Methods and properties for the 'integratedImage' attribute
    def getIntegratedImage(self):
        return self._integratedImage

    def setIntegratedImage(self, integratedImage):
        if integratedImage is None:
            self._integratedImage = None
        elif integratedImage.__class__.__name__ == "XSDataImage":
            self._integratedImage = integratedImage
        else:
            strMessage = (
                "ERROR! XSDataInputBioSaxsAzimutIntv1_0.setIntegratedImage argument is not XSDataImage but %s"
                % integratedImage.__class__.__name__
            )
            raise BaseException(strMessage)

    def delIntegratedImage(self):
        self._integratedImage = None

    integratedImage = property(
        getIntegratedImage,
        setIntegratedImage,
        delIntegratedImage,
        "Property for integratedImage",
    )
    # Methods and properties for the 'integratedCurve' attribute
    def getIntegratedCurve(self):
        return self._integratedCurve

    def setIntegratedCurve(self, integratedCurve):
        if integratedCurve is None:
            self._integratedCurve = None
        elif integratedCurve.__class__.__name__ == "XSDataFile":
            self._integratedCurve = integratedCurve
        else:
            strMessage = (
                "ERROR! XSDataInputBioSaxsAzimutIntv1_0.setIntegratedCurve argument is not XSDataFile but %s"
                % integratedCurve.__class__.__name__
            )
            raise BaseException(strMessage)

    def delIntegratedCurve(self):
        self._integratedCurve = None

    integratedCurve = property(
        getIntegratedCurve,
        setIntegratedCurve,
        delIntegratedCurve,
        "Property for integratedCurve",
    )
    # Methods and properties for the 'correctedImage' attribute
    def getCorrectedImage(self):
        return self._correctedImage

    def setCorrectedImage(self, correctedImage):
        if correctedImage is None:
            self._correctedImage = None
        elif correctedImage.__class__.__name__ == "XSDataImage":
            self._correctedImage = correctedImage
        else:
            strMessage = (
                "ERROR! XSDataInputBioSaxsAzimutIntv1_0.setCorrectedImage argument is not XSDataImage but %s"
                % correctedImage.__class__.__name__
            )
            raise BaseException(strMessage)

    def delCorrectedImage(self):
        self._correctedImage = None

    correctedImage = property(
        getCorrectedImage,
        setCorrectedImage,
        delCorrectedImage,
        "Property for correctedImage",
    )
    # Methods and properties for the 'sample' attribute
    def getSample(self):
        return self._sample

    def setSample(self, sample):
        if sample is None:
            self._sample = None
        elif sample.__class__.__name__ == "XSDataBioSaxsSample":
            self._sample = sample
        else:
            strMessage = (
                "ERROR! XSDataInputBioSaxsAzimutIntv1_0.setSample argument is not XSDataBioSaxsSample but %s"
                % sample.__class__.__name__
            )
            raise BaseException(strMessage)

    def delSample(self):
        self._sample = None

    sample = property(getSample, setSample, delSample, "Property for sample")
    # Methods and properties for the 'experimentSetup' attribute
    def getExperimentSetup(self):
        return self._experimentSetup

    def setExperimentSetup(self, experimentSetup):
        if experimentSetup is None:
            self._experimentSetup = None
        elif experimentSetup.__class__.__name__ == "XSDataBioSaxsExperimentSetup":
            self._experimentSetup = experimentSetup
        else:
            strMessage = (
                "ERROR! XSDataInputBioSaxsAzimutIntv1_0.setExperimentSetup argument is not XSDataBioSaxsExperimentSetup but %s"
                % experimentSetup.__class__.__name__
            )
            raise BaseException(strMessage)

    def delExperimentSetup(self):
        self._experimentSetup = None

    experimentSetup = property(
        getExperimentSetup,
        setExperimentSetup,
        delExperimentSetup,
        "Property for experimentSetup",
    )

    def export(self, outfile, level, name_="XSDataInputBioSaxsAzimutIntv1_0"):
        showIndent(outfile, level)
        outfile.write(unicode("<%s>\n" % name_))
        self.exportChildren(outfile, level + 1, name_)
        showIndent(outfile, level)
        outfile.write(unicode("</%s>\n" % name_))

    def exportChildren(self, outfile, level, name_="XSDataInputBioSaxsAzimutIntv1_0"):
        XSDataInput.exportChildren(self, outfile, level, name_)
        if self._normalizedImage is not None:
            self.normalizedImage.export(outfile, level, name_="normalizedImage")
        else:
            warnEmptyAttribute("normalizedImage", "XSDataImage")
        if self._normalizedImageSize is not None:
            self.normalizedImageSize.export(outfile, level, name_="normalizedImageSize")
        if self._integratedImage is not None:
            self.integratedImage.export(outfile, level, name_="integratedImage")
        if self._integratedCurve is not None:
            self.integratedCurve.export(outfile, level, name_="integratedCurve")
        else:
            warnEmptyAttribute("integratedCurve", "XSDataFile")
        if self._correctedImage is not None:
            self.correctedImage.export(outfile, level, name_="correctedImage")
        if self._sample is not None:
            self.sample.export(outfile, level, name_="sample")
        else:
            warnEmptyAttribute("sample", "XSDataBioSaxsSample")
        if self._experimentSetup is not None:
            self.experimentSetup.export(outfile, level, name_="experimentSetup")
        else:
            warnEmptyAttribute("experimentSetup", "XSDataBioSaxsExperimentSetup")

    def build(self, node_):
        for child_ in node_.childNodes:
            nodeName_ = child_.nodeName.split(":")[-1]
            self.buildChildren(child_, nodeName_)

    def buildChildren(self, child_, nodeName_):
        if child_.nodeType == Node.ELEMENT_NODE and nodeName_ == "normalizedImage":
            obj_ = XSDataImage()
            obj_.build(child_)
            self.setNormalizedImage(obj_)
        elif (
            child_.nodeType == Node.ELEMENT_NODE and nodeName_ == "normalizedImageSize"
        ):
            obj_ = XSDataInteger()
            obj_.build(child_)
            self.setNormalizedImageSize(obj_)
        elif child_.nodeType == Node.ELEMENT_NODE and nodeName_ == "integratedImage":
            obj_ = XSDataImage()
            obj_.build(child_)
            self.setIntegratedImage(obj_)
        elif child_.nodeType == Node.ELEMENT_NODE and nodeName_ == "integratedCurve":
            obj_ = XSDataFile()
            obj_.build(child_)
            self.setIntegratedCurve(obj_)
        elif child_.nodeType == Node.ELEMENT_NODE and nodeName_ == "correctedImage":
            obj_ = XSDataImage()
            obj_.build(child_)
            self.setCorrectedImage(obj_)
        elif child_.nodeType == Node.ELEMENT_NODE and nodeName_ == "sample":
            obj_ = XSDataBioSaxsSample()
            obj_.build(child_)
            self.setSample(obj_)
        elif child_.nodeType == Node.ELEMENT_NODE and nodeName_ == "experimentSetup":
            obj_ = XSDataBioSaxsExperimentSetup()
            obj_.build(child_)
            self.setExperimentSetup(obj_)
        XSDataInput.buildChildren(self, child_, nodeName_)

    # Method for marshalling an object
    def marshal(self):
        oStreamString = StringIO()
        oStreamString.write(unicode('<?xml version="1.0" ?>\n'))
        self.export(oStreamString, 0, name_="XSDataInputBioSaxsAzimutIntv1_0")
        oStringXML = oStreamString.getvalue()
        oStreamString.close()
        return oStringXML

    # Only to export the entire XML tree to a file stream on disk
    def exportToFile(self, _outfileName):
        outfile = open(_outfileName, "w")
        outfile.write(unicode('<?xml version="1.0" ?>\n'))
        self.export(outfile, 0, name_="XSDataInputBioSaxsAzimutIntv1_0")
        outfile.close()

    # Deprecated method, replaced by exportToFile
    def outputFile(self, _outfileName):
        print(
            "WARNING: Method outputFile in class XSDataInputBioSaxsAzimutIntv1_0 is deprecated, please use instead exportToFile!"
        )
        self.exportToFile(_outfileName)

    # Method for making a copy in a new instance
    def copy(self):
        return XSDataInputBioSaxsAzimutIntv1_0.parseString(self.marshal())

    # Static method for parsing a string
    def parseString(_inString):
        doc = minidom.parseString(_inString)
        rootNode = doc.documentElement
        rootObj = XSDataInputBioSaxsAzimutIntv1_0()
        rootObj.build(rootNode)
        # Check that all minOccurs are obeyed by marshalling the created object
        oStreamString = StringIO()
        rootObj.export(oStreamString, 0, name_="XSDataInputBioSaxsAzimutIntv1_0")
        oStreamString.close()
        return rootObj

    parseString = staticmethod(parseString)
    # Static method for parsing a file
    def parseFile(_inFilePath):
        doc = minidom.parse(_inFilePath)
        rootNode = doc.documentElement
        rootObj = XSDataInputBioSaxsAzimutIntv1_0()
        rootObj.build(rootNode)
        return rootObj

    parseFile = staticmethod(parseFile)


# end class XSDataInputBioSaxsAzimutIntv1_0


class XSDataInputBioSaxsISPyBHPLCv1_0(XSDataInput):
    def __init__(
        self,
        configuration=None,
        experimentId=None,
        endFrame=None,
        startFrame=None,
        dataInputBioSaxs=None,
    ):
        XSDataInput.__init__(self, configuration)
        if dataInputBioSaxs is None:
            self._dataInputBioSaxs = None
        elif dataInputBioSaxs.__class__.__name__ == "XSDataInputBioSaxsISPyBv1_0":
            self._dataInputBioSaxs = dataInputBioSaxs
        else:
            strMessage = (
                "ERROR! XSDataInputBioSaxsISPyBHPLCv1_0 constructor argument 'dataInputBioSaxs' is not XSDataInputBioSaxsISPyBv1_0 but %s"
                % self._dataInputBioSaxs.__class__.__name__
            )
            raise BaseException(strMessage)
        if startFrame is None:
            self._startFrame = None
        elif startFrame.__class__.__name__ == "XSDataString":
            self._startFrame = startFrame
        else:
            strMessage = (
                "ERROR! XSDataInputBioSaxsISPyBHPLCv1_0 constructor argument 'startFrame' is not XSDataString but %s"
                % self._startFrame.__class__.__name__
            )
            raise BaseException(strMessage)
        if endFrame is None:
            self._endFrame = None
        elif endFrame.__class__.__name__ == "XSDataString":
            self._endFrame = endFrame
        else:
            strMessage = (
                "ERROR! XSDataInputBioSaxsISPyBHPLCv1_0 constructor argument 'endFrame' is not XSDataString but %s"
                % self._endFrame.__class__.__name__
            )
            raise BaseException(strMessage)
        if experimentId is None:
            self._experimentId = None
        elif experimentId.__class__.__name__ == "XSDataInteger":
            self._experimentId = experimentId
        else:
            strMessage = (
                "ERROR! XSDataInputBioSaxsISPyBHPLCv1_0 constructor argument 'experimentId' is not XSDataInteger but %s"
                % self._experimentId.__class__.__name__
            )
            raise BaseException(strMessage)

    # Methods and properties for the 'dataInputBioSaxs' attribute
    def getDataInputBioSaxs(self):
        return self._dataInputBioSaxs

    def setDataInputBioSaxs(self, dataInputBioSaxs):
        if dataInputBioSaxs is None:
            self._dataInputBioSaxs = None
        elif dataInputBioSaxs.__class__.__name__ == "XSDataInputBioSaxsISPyBv1_0":
            self._dataInputBioSaxs = dataInputBioSaxs
        else:
            strMessage = (
                "ERROR! XSDataInputBioSaxsISPyBHPLCv1_0.setDataInputBioSaxs argument is not XSDataInputBioSaxsISPyBv1_0 but %s"
                % dataInputBioSaxs.__class__.__name__
            )
            raise BaseException(strMessage)

    def delDataInputBioSaxs(self):
        self._dataInputBioSaxs = None

    dataInputBioSaxs = property(
        getDataInputBioSaxs,
        setDataInputBioSaxs,
        delDataInputBioSaxs,
        "Property for dataInputBioSaxs",
    )
    # Methods and properties for the 'startFrame' attribute
    def getStartFrame(self):
        return self._startFrame

    def setStartFrame(self, startFrame):
        if startFrame is None:
            self._startFrame = None
        elif startFrame.__class__.__name__ == "XSDataString":
            self._startFrame = startFrame
        else:
            strMessage = (
                "ERROR! XSDataInputBioSaxsISPyBHPLCv1_0.setStartFrame argument is not XSDataString but %s"
                % startFrame.__class__.__name__
            )
            raise BaseException(strMessage)

    def delStartFrame(self):
        self._startFrame = None

    startFrame = property(
        getStartFrame, setStartFrame, delStartFrame, "Property for startFrame"
    )
    # Methods and properties for the 'endFrame' attribute
    def getEndFrame(self):
        return self._endFrame

    def setEndFrame(self, endFrame):
        if endFrame is None:
            self._endFrame = None
        elif endFrame.__class__.__name__ == "XSDataString":
            self._endFrame = endFrame
        else:
            strMessage = (
                "ERROR! XSDataInputBioSaxsISPyBHPLCv1_0.setEndFrame argument is not XSDataString but %s"
                % endFrame.__class__.__name__
            )
            raise BaseException(strMessage)

    def delEndFrame(self):
        self._endFrame = None

    endFrame = property(getEndFrame, setEndFrame, delEndFrame, "Property for endFrame")
    # Methods and properties for the 'experimentId' attribute
    def getExperimentId(self):
        return self._experimentId

    def setExperimentId(self, experimentId):
        if experimentId is None:
            self._experimentId = None
        elif experimentId.__class__.__name__ == "XSDataInteger":
            self._experimentId = experimentId
        else:
            strMessage = (
                "ERROR! XSDataInputBioSaxsISPyBHPLCv1_0.setExperimentId argument is not XSDataInteger but %s"
                % experimentId.__class__.__name__
            )
            raise BaseException(strMessage)

    def delExperimentId(self):
        self._experimentId = None

    experimentId = property(
        getExperimentId, setExperimentId, delExperimentId, "Property for experimentId"
    )

    def export(self, outfile, level, name_="XSDataInputBioSaxsISPyBHPLCv1_0"):
        showIndent(outfile, level)
        outfile.write(unicode("<%s>\n" % name_))
        self.exportChildren(outfile, level + 1, name_)
        showIndent(outfile, level)
        outfile.write(unicode("</%s>\n" % name_))

    def exportChildren(self, outfile, level, name_="XSDataInputBioSaxsISPyBHPLCv1_0"):
        XSDataInput.exportChildren(self, outfile, level, name_)
        if self._dataInputBioSaxs is not None:
            self.dataInputBioSaxs.export(outfile, level, name_="dataInputBioSaxs")
        else:
            warnEmptyAttribute("dataInputBioSaxs", "XSDataInputBioSaxsISPyBv1_0")
        if self._startFrame is not None:
            self.startFrame.export(outfile, level, name_="startFrame")
        else:
            warnEmptyAttribute("startFrame", "XSDataString")
        if self._endFrame is not None:
            self.endFrame.export(outfile, level, name_="endFrame")
        else:
            warnEmptyAttribute("endFrame", "XSDataString")
        if self._experimentId is not None:
            self.experimentId.export(outfile, level, name_="experimentId")
        else:
            warnEmptyAttribute("experimentId", "XSDataInteger")

    def build(self, node_):
        for child_ in node_.childNodes:
            nodeName_ = child_.nodeName.split(":")[-1]
            self.buildChildren(child_, nodeName_)

    def buildChildren(self, child_, nodeName_):
        if child_.nodeType == Node.ELEMENT_NODE and nodeName_ == "dataInputBioSaxs":
            obj_ = XSDataInputBioSaxsISPyBv1_0()
            obj_.build(child_)
            self.setDataInputBioSaxs(obj_)
        elif child_.nodeType == Node.ELEMENT_NODE and nodeName_ == "startFrame":
            obj_ = XSDataString()
            obj_.build(child_)
            self.setStartFrame(obj_)
        elif child_.nodeType == Node.ELEMENT_NODE and nodeName_ == "endFrame":
            obj_ = XSDataString()
            obj_.build(child_)
            self.setEndFrame(obj_)
        elif child_.nodeType == Node.ELEMENT_NODE and nodeName_ == "experimentId":
            obj_ = XSDataInteger()
            obj_.build(child_)
            self.setExperimentId(obj_)
        XSDataInput.buildChildren(self, child_, nodeName_)

    # Method for marshalling an object
    def marshal(self):
        oStreamString = StringIO()
        oStreamString.write(unicode('<?xml version="1.0" ?>\n'))
        self.export(oStreamString, 0, name_="XSDataInputBioSaxsISPyBHPLCv1_0")
        oStringXML = oStreamString.getvalue()
        oStreamString.close()
        return oStringXML

    # Only to export the entire XML tree to a file stream on disk
    def exportToFile(self, _outfileName):
        outfile = open(_outfileName, "w")
        outfile.write(unicode('<?xml version="1.0" ?>\n'))
        self.export(outfile, 0, name_="XSDataInputBioSaxsISPyBHPLCv1_0")
        outfile.close()

    # Deprecated method, replaced by exportToFile
    def outputFile(self, _outfileName):
        print(
            "WARNING: Method outputFile in class XSDataInputBioSaxsISPyBHPLCv1_0 is deprecated, please use instead exportToFile!"
        )
        self.exportToFile(_outfileName)

    # Method for making a copy in a new instance
    def copy(self):
        return XSDataInputBioSaxsISPyBHPLCv1_0.parseString(self.marshal())

    # Static method for parsing a string
    def parseString(_inString):
        doc = minidom.parseString(_inString)
        rootNode = doc.documentElement
        rootObj = XSDataInputBioSaxsISPyBHPLCv1_0()
        rootObj.build(rootNode)
        # Check that all minOccurs are obeyed by marshalling the created object
        oStreamString = StringIO()
        rootObj.export(oStreamString, 0, name_="XSDataInputBioSaxsISPyBHPLCv1_0")
        oStreamString.close()
        return rootObj

    parseString = staticmethod(parseString)
    # Static method for parsing a file
    def parseFile(_inFilePath):
        doc = minidom.parse(_inFilePath)
        rootNode = doc.documentElement
        rootObj = XSDataInputBioSaxsISPyBHPLCv1_0()
        rootObj.build(rootNode)
        return rootObj

    parseFile = staticmethod(parseFile)


# end class XSDataInputBioSaxsISPyBHPLCv1_0


class XSDataInputBioSaxsISPyBModellingv1_0(XSDataInput):
    """Input class for populating ISPyB"""

    def __init__(
        self,
        configuration=None,
        nsdPlot=None,
        chiRfactorPlot=None,
        pdbSolventFile=None,
        pdbMoleculeFile=None,
        logFile=None,
        fitFile=None,
        damminModel=None,
        damstartModel=None,
        damfiltModel=None,
        damaverModel=None,
        dammifModels=None,
        sample=None,
    ):
        XSDataInput.__init__(self, configuration)
        if sample is None:
            self._sample = None
        elif sample.__class__.__name__ == "XSDataBioSaxsSample":
            self._sample = sample
        else:
            strMessage = (
                "ERROR! XSDataInputBioSaxsISPyBModellingv1_0 constructor argument 'sample' is not XSDataBioSaxsSample but %s"
                % self._sample.__class__.__name__
            )
            raise BaseException(strMessage)
        if dammifModels is None:
            self._dammifModels = []
        elif dammifModels.__class__.__name__ == "list":
            self._dammifModels = dammifModels
        else:
            strMessage = (
                "ERROR! XSDataInputBioSaxsISPyBModellingv1_0 constructor argument 'dammifModels' is not list but %s"
                % self._dammifModels.__class__.__name__
            )
            raise BaseException(strMessage)
        if damaverModel is None:
            self._damaverModel = None
        elif damaverModel.__class__.__name__ == "XSDataSaxsModel":
            self._damaverModel = damaverModel
        else:
            strMessage = (
                "ERROR! XSDataInputBioSaxsISPyBModellingv1_0 constructor argument 'damaverModel' is not XSDataSaxsModel but %s"
                % self._damaverModel.__class__.__name__
            )
            raise BaseException(strMessage)
        if damfiltModel is None:
            self._damfiltModel = None
        elif damfiltModel.__class__.__name__ == "XSDataSaxsModel":
            self._damfiltModel = damfiltModel
        else:
            strMessage = (
                "ERROR! XSDataInputBioSaxsISPyBModellingv1_0 constructor argument 'damfiltModel' is not XSDataSaxsModel but %s"
                % self._damfiltModel.__class__.__name__
            )
            raise BaseException(strMessage)
        if damstartModel is None:
            self._damstartModel = None
        elif damstartModel.__class__.__name__ == "XSDataSaxsModel":
            self._damstartModel = damstartModel
        else:
            strMessage = (
                "ERROR! XSDataInputBioSaxsISPyBModellingv1_0 constructor argument 'damstartModel' is not XSDataSaxsModel but %s"
                % self._damstartModel.__class__.__name__
            )
            raise BaseException(strMessage)
        if damminModel is None:
            self._damminModel = None
        elif damminModel.__class__.__name__ == "XSDataSaxsModel":
            self._damminModel = damminModel
        else:
            strMessage = (
                "ERROR! XSDataInputBioSaxsISPyBModellingv1_0 constructor argument 'damminModel' is not XSDataSaxsModel but %s"
                % self._damminModel.__class__.__name__
            )
            raise BaseException(strMessage)
        if fitFile is None:
            self._fitFile = None
        elif fitFile.__class__.__name__ == "XSDataFile":
            self._fitFile = fitFile
        else:
            strMessage = (
                "ERROR! XSDataInputBioSaxsISPyBModellingv1_0 constructor argument 'fitFile' is not XSDataFile but %s"
                % self._fitFile.__class__.__name__
            )
            raise BaseException(strMessage)
        if logFile is None:
            self._logFile = None
        elif logFile.__class__.__name__ == "XSDataFile":
            self._logFile = logFile
        else:
            strMessage = (
                "ERROR! XSDataInputBioSaxsISPyBModellingv1_0 constructor argument 'logFile' is not XSDataFile but %s"
                % self._logFile.__class__.__name__
            )
            raise BaseException(strMessage)
        if pdbMoleculeFile is None:
            self._pdbMoleculeFile = None
        elif pdbMoleculeFile.__class__.__name__ == "XSDataFile":
            self._pdbMoleculeFile = pdbMoleculeFile
        else:
            strMessage = (
                "ERROR! XSDataInputBioSaxsISPyBModellingv1_0 constructor argument 'pdbMoleculeFile' is not XSDataFile but %s"
                % self._pdbMoleculeFile.__class__.__name__
            )
            raise BaseException(strMessage)
        if pdbSolventFile is None:
            self._pdbSolventFile = None
        elif pdbSolventFile.__class__.__name__ == "XSDataFile":
            self._pdbSolventFile = pdbSolventFile
        else:
            strMessage = (
                "ERROR! XSDataInputBioSaxsISPyBModellingv1_0 constructor argument 'pdbSolventFile' is not XSDataFile but %s"
                % self._pdbSolventFile.__class__.__name__
            )
            raise BaseException(strMessage)
        if chiRfactorPlot is None:
            self._chiRfactorPlot = None
        elif chiRfactorPlot.__class__.__name__ == "XSDataFile":
            self._chiRfactorPlot = chiRfactorPlot
        else:
            strMessage = (
                "ERROR! XSDataInputBioSaxsISPyBModellingv1_0 constructor argument 'chiRfactorPlot' is not XSDataFile but %s"
                % self._chiRfactorPlot.__class__.__name__
            )
            raise BaseException(strMessage)
        if nsdPlot is None:
            self._nsdPlot = None
        elif nsdPlot.__class__.__name__ == "XSDataFile":
            self._nsdPlot = nsdPlot
        else:
            strMessage = (
                "ERROR! XSDataInputBioSaxsISPyBModellingv1_0 constructor argument 'nsdPlot' is not XSDataFile but %s"
                % self._nsdPlot.__class__.__name__
            )
            raise BaseException(strMessage)

    # Methods and properties for the 'sample' attribute
    def getSample(self):
        return self._sample

    def setSample(self, sample):
        if sample is None:
            self._sample = None
        elif sample.__class__.__name__ == "XSDataBioSaxsSample":
            self._sample = sample
        else:
            strMessage = (
                "ERROR! XSDataInputBioSaxsISPyBModellingv1_0.setSample argument is not XSDataBioSaxsSample but %s"
                % sample.__class__.__name__
            )
            raise BaseException(strMessage)

    def delSample(self):
        self._sample = None

    sample = property(getSample, setSample, delSample, "Property for sample")
    # Methods and properties for the 'dammifModels' attribute
    def getDammifModels(self):
        return self._dammifModels

    def setDammifModels(self, dammifModels):
        if dammifModels is None:
            self._dammifModels = []
        elif dammifModels.__class__.__name__ == "list":
            self._dammifModels = dammifModels
        else:
            strMessage = (
                "ERROR! XSDataInputBioSaxsISPyBModellingv1_0.setDammifModels argument is not list but %s"
                % dammifModels.__class__.__name__
            )
            raise BaseException(strMessage)

    def delDammifModels(self):
        self._dammifModels = None

    dammifModels = property(
        getDammifModels, setDammifModels, delDammifModels, "Property for dammifModels"
    )

    def addDammifModels(self, value):
        if value is None:
            strMessage = "ERROR! XSDataInputBioSaxsISPyBModellingv1_0.addDammifModels argument is None"
            raise BaseException(strMessage)
        elif value.__class__.__name__ == "XSDataSaxsModel":
            self._dammifModels.append(value)
        else:
            strMessage = (
                "ERROR! XSDataInputBioSaxsISPyBModellingv1_0.addDammifModels argument is not XSDataSaxsModel but %s"
                % value.__class__.__name__
            )
            raise BaseException(strMessage)

    def insertDammifModels(self, index, value):
        if index is None:
            strMessage = "ERROR! XSDataInputBioSaxsISPyBModellingv1_0.insertDammifModels argument 'index' is None"
            raise BaseException(strMessage)
        if value is None:
            strMessage = "ERROR! XSDataInputBioSaxsISPyBModellingv1_0.insertDammifModels argument 'value' is None"
            raise BaseException(strMessage)
        elif value.__class__.__name__ == "XSDataSaxsModel":
            self._dammifModels[index] = value
        else:
            strMessage = (
                "ERROR! XSDataInputBioSaxsISPyBModellingv1_0.addDammifModels argument is not XSDataSaxsModel but %s"
                % value.__class__.__name__
            )
            raise BaseException(strMessage)

    # Methods and properties for the 'damaverModel' attribute
    def getDamaverModel(self):
        return self._damaverModel

    def setDamaverModel(self, damaverModel):
        if damaverModel is None:
            self._damaverModel = None
        elif damaverModel.__class__.__name__ == "XSDataSaxsModel":
            self._damaverModel = damaverModel
        else:
            strMessage = (
                "ERROR! XSDataInputBioSaxsISPyBModellingv1_0.setDamaverModel argument is not XSDataSaxsModel but %s"
                % damaverModel.__class__.__name__
            )
            raise BaseException(strMessage)

    def delDamaverModel(self):
        self._damaverModel = None

    damaverModel = property(
        getDamaverModel, setDamaverModel, delDamaverModel, "Property for damaverModel"
    )
    # Methods and properties for the 'damfiltModel' attribute
    def getDamfiltModel(self):
        return self._damfiltModel

    def setDamfiltModel(self, damfiltModel):
        if damfiltModel is None:
            self._damfiltModel = None
        elif damfiltModel.__class__.__name__ == "XSDataSaxsModel":
            self._damfiltModel = damfiltModel
        else:
            strMessage = (
                "ERROR! XSDataInputBioSaxsISPyBModellingv1_0.setDamfiltModel argument is not XSDataSaxsModel but %s"
                % damfiltModel.__class__.__name__
            )
            raise BaseException(strMessage)

    def delDamfiltModel(self):
        self._damfiltModel = None

    damfiltModel = property(
        getDamfiltModel, setDamfiltModel, delDamfiltModel, "Property for damfiltModel"
    )
    # Methods and properties for the 'damstartModel' attribute
    def getDamstartModel(self):
        return self._damstartModel

    def setDamstartModel(self, damstartModel):
        if damstartModel is None:
            self._damstartModel = None
        elif damstartModel.__class__.__name__ == "XSDataSaxsModel":
            self._damstartModel = damstartModel
        else:
            strMessage = (
                "ERROR! XSDataInputBioSaxsISPyBModellingv1_0.setDamstartModel argument is not XSDataSaxsModel but %s"
                % damstartModel.__class__.__name__
            )
            raise BaseException(strMessage)

    def delDamstartModel(self):
        self._damstartModel = None

    damstartModel = property(
        getDamstartModel,
        setDamstartModel,
        delDamstartModel,
        "Property for damstartModel",
    )
    # Methods and properties for the 'damminModel' attribute
    def getDamminModel(self):
        return self._damminModel

    def setDamminModel(self, damminModel):
        if damminModel is None:
            self._damminModel = None
        elif damminModel.__class__.__name__ == "XSDataSaxsModel":
            self._damminModel = damminModel
        else:
            strMessage = (
                "ERROR! XSDataInputBioSaxsISPyBModellingv1_0.setDamminModel argument is not XSDataSaxsModel but %s"
                % damminModel.__class__.__name__
            )
            raise BaseException(strMessage)

    def delDamminModel(self):
        self._damminModel = None

    damminModel = property(
        getDamminModel, setDamminModel, delDamminModel, "Property for damminModel"
    )
    # Methods and properties for the 'fitFile' attribute
    def getFitFile(self):
        return self._fitFile

    def setFitFile(self, fitFile):
        if fitFile is None:
            self._fitFile = None
        elif fitFile.__class__.__name__ == "XSDataFile":
            self._fitFile = fitFile
        else:
            strMessage = (
                "ERROR! XSDataInputBioSaxsISPyBModellingv1_0.setFitFile argument is not XSDataFile but %s"
                % fitFile.__class__.__name__
            )
            raise BaseException(strMessage)

    def delFitFile(self):
        self._fitFile = None

    fitFile = property(getFitFile, setFitFile, delFitFile, "Property for fitFile")
    # Methods and properties for the 'logFile' attribute
    def getLogFile(self):
        return self._logFile

    def setLogFile(self, logFile):
        if logFile is None:
            self._logFile = None
        elif logFile.__class__.__name__ == "XSDataFile":
            self._logFile = logFile
        else:
            strMessage = (
                "ERROR! XSDataInputBioSaxsISPyBModellingv1_0.setLogFile argument is not XSDataFile but %s"
                % logFile.__class__.__name__
            )
            raise BaseException(strMessage)

    def delLogFile(self):
        self._logFile = None

    logFile = property(getLogFile, setLogFile, delLogFile, "Property for logFile")
    # Methods and properties for the 'pdbMoleculeFile' attribute
    def getPdbMoleculeFile(self):
        return self._pdbMoleculeFile

    def setPdbMoleculeFile(self, pdbMoleculeFile):
        if pdbMoleculeFile is None:
            self._pdbMoleculeFile = None
        elif pdbMoleculeFile.__class__.__name__ == "XSDataFile":
            self._pdbMoleculeFile = pdbMoleculeFile
        else:
            strMessage = (
                "ERROR! XSDataInputBioSaxsISPyBModellingv1_0.setPdbMoleculeFile argument is not XSDataFile but %s"
                % pdbMoleculeFile.__class__.__name__
            )
            raise BaseException(strMessage)

    def delPdbMoleculeFile(self):
        self._pdbMoleculeFile = None

    pdbMoleculeFile = property(
        getPdbMoleculeFile,
        setPdbMoleculeFile,
        delPdbMoleculeFile,
        "Property for pdbMoleculeFile",
    )
    # Methods and properties for the 'pdbSolventFile' attribute
    def getPdbSolventFile(self):
        return self._pdbSolventFile

    def setPdbSolventFile(self, pdbSolventFile):
        if pdbSolventFile is None:
            self._pdbSolventFile = None
        elif pdbSolventFile.__class__.__name__ == "XSDataFile":
            self._pdbSolventFile = pdbSolventFile
        else:
            strMessage = (
                "ERROR! XSDataInputBioSaxsISPyBModellingv1_0.setPdbSolventFile argument is not XSDataFile but %s"
                % pdbSolventFile.__class__.__name__
            )
            raise BaseException(strMessage)

    def delPdbSolventFile(self):
        self._pdbSolventFile = None

    pdbSolventFile = property(
        getPdbSolventFile,
        setPdbSolventFile,
        delPdbSolventFile,
        "Property for pdbSolventFile",
    )
    # Methods and properties for the 'chiRfactorPlot' attribute
    def getChiRfactorPlot(self):
        return self._chiRfactorPlot

    def setChiRfactorPlot(self, chiRfactorPlot):
        if chiRfactorPlot is None:
            self._chiRfactorPlot = None
        elif chiRfactorPlot.__class__.__name__ == "XSDataFile":
            self._chiRfactorPlot = chiRfactorPlot
        else:
            strMessage = (
                "ERROR! XSDataInputBioSaxsISPyBModellingv1_0.setChiRfactorPlot argument is not XSDataFile but %s"
                % chiRfactorPlot.__class__.__name__
            )
            raise BaseException(strMessage)

    def delChiRfactorPlot(self):
        self._chiRfactorPlot = None

    chiRfactorPlot = property(
        getChiRfactorPlot,
        setChiRfactorPlot,
        delChiRfactorPlot,
        "Property for chiRfactorPlot",
    )
    # Methods and properties for the 'nsdPlot' attribute
    def getNsdPlot(self):
        return self._nsdPlot

    def setNsdPlot(self, nsdPlot):
        if nsdPlot is None:
            self._nsdPlot = None
        elif nsdPlot.__class__.__name__ == "XSDataFile":
            self._nsdPlot = nsdPlot
        else:
            strMessage = (
                "ERROR! XSDataInputBioSaxsISPyBModellingv1_0.setNsdPlot argument is not XSDataFile but %s"
                % nsdPlot.__class__.__name__
            )
            raise BaseException(strMessage)

    def delNsdPlot(self):
        self._nsdPlot = None

    nsdPlot = property(getNsdPlot, setNsdPlot, delNsdPlot, "Property for nsdPlot")

    def export(self, outfile, level, name_="XSDataInputBioSaxsISPyBModellingv1_0"):
        showIndent(outfile, level)
        outfile.write(unicode("<%s>\n" % name_))
        self.exportChildren(outfile, level + 1, name_)
        showIndent(outfile, level)
        outfile.write(unicode("</%s>\n" % name_))

    def exportChildren(
        self, outfile, level, name_="XSDataInputBioSaxsISPyBModellingv1_0"
    ):
        XSDataInput.exportChildren(self, outfile, level, name_)
        if self._sample is not None:
            self.sample.export(outfile, level, name_="sample")
        else:
            warnEmptyAttribute("sample", "XSDataBioSaxsSample")
        for dammifModels_ in self.getDammifModels():
            dammifModels_.export(outfile, level, name_="dammifModels")
        if self._damaverModel is not None:
            self.damaverModel.export(outfile, level, name_="damaverModel")
        if self._damfiltModel is not None:
            self.damfiltModel.export(outfile, level, name_="damfiltModel")
        if self._damstartModel is not None:
            self.damstartModel.export(outfile, level, name_="damstartModel")
        if self._damminModel is not None:
            self.damminModel.export(outfile, level, name_="damminModel")
        if self._fitFile is not None:
            self.fitFile.export(outfile, level, name_="fitFile")
        if self._logFile is not None:
            self.logFile.export(outfile, level, name_="logFile")
        if self._pdbMoleculeFile is not None:
            self.pdbMoleculeFile.export(outfile, level, name_="pdbMoleculeFile")
        if self._pdbSolventFile is not None:
            self.pdbSolventFile.export(outfile, level, name_="pdbSolventFile")
        if self._chiRfactorPlot is not None:
            self.chiRfactorPlot.export(outfile, level, name_="chiRfactorPlot")
        if self._nsdPlot is not None:
            self.nsdPlot.export(outfile, level, name_="nsdPlot")

    def build(self, node_):
        for child_ in node_.childNodes:
            nodeName_ = child_.nodeName.split(":")[-1]
            self.buildChildren(child_, nodeName_)

    def buildChildren(self, child_, nodeName_):
        if child_.nodeType == Node.ELEMENT_NODE and nodeName_ == "sample":
            obj_ = XSDataBioSaxsSample()
            obj_.build(child_)
            self.setSample(obj_)
        elif child_.nodeType == Node.ELEMENT_NODE and nodeName_ == "dammifModels":
            obj_ = XSDataSaxsModel()
            obj_.build(child_)
            self.dammifModels.append(obj_)
        elif child_.nodeType == Node.ELEMENT_NODE and nodeName_ == "damaverModel":
            obj_ = XSDataSaxsModel()
            obj_.build(child_)
            self.setDamaverModel(obj_)
        elif child_.nodeType == Node.ELEMENT_NODE and nodeName_ == "damfiltModel":
            obj_ = XSDataSaxsModel()
            obj_.build(child_)
            self.setDamfiltModel(obj_)
        elif child_.nodeType == Node.ELEMENT_NODE and nodeName_ == "damstartModel":
            obj_ = XSDataSaxsModel()
            obj_.build(child_)
            self.setDamstartModel(obj_)
        elif child_.nodeType == Node.ELEMENT_NODE and nodeName_ == "damminModel":
            obj_ = XSDataSaxsModel()
            obj_.build(child_)
            self.setDamminModel(obj_)
        elif child_.nodeType == Node.ELEMENT_NODE and nodeName_ == "fitFile":
            obj_ = XSDataFile()
            obj_.build(child_)
            self.setFitFile(obj_)
        elif child_.nodeType == Node.ELEMENT_NODE and nodeName_ == "logFile":
            obj_ = XSDataFile()
            obj_.build(child_)
            self.setLogFile(obj_)
        elif child_.nodeType == Node.ELEMENT_NODE and nodeName_ == "pdbMoleculeFile":
            obj_ = XSDataFile()
            obj_.build(child_)
            self.setPdbMoleculeFile(obj_)
        elif child_.nodeType == Node.ELEMENT_NODE and nodeName_ == "pdbSolventFile":
            obj_ = XSDataFile()
            obj_.build(child_)
            self.setPdbSolventFile(obj_)
        elif child_.nodeType == Node.ELEMENT_NODE and nodeName_ == "chiRfactorPlot":
            obj_ = XSDataFile()
            obj_.build(child_)
            self.setChiRfactorPlot(obj_)
        elif child_.nodeType == Node.ELEMENT_NODE and nodeName_ == "nsdPlot":
            obj_ = XSDataFile()
            obj_.build(child_)
            self.setNsdPlot(obj_)
        XSDataInput.buildChildren(self, child_, nodeName_)

    # Method for marshalling an object
    def marshal(self):
        oStreamString = StringIO()
        oStreamString.write(unicode('<?xml version="1.0" ?>\n'))
        self.export(oStreamString, 0, name_="XSDataInputBioSaxsISPyBModellingv1_0")
        oStringXML = oStreamString.getvalue()
        oStreamString.close()
        return oStringXML

    # Only to export the entire XML tree to a file stream on disk
    def exportToFile(self, _outfileName):
        outfile = open(_outfileName, "w")
        outfile.write(unicode('<?xml version="1.0" ?>\n'))
        self.export(outfile, 0, name_="XSDataInputBioSaxsISPyBModellingv1_0")
        outfile.close()

    # Deprecated method, replaced by exportToFile
    def outputFile(self, _outfileName):
        print(
            "WARNING: Method outputFile in class XSDataInputBioSaxsISPyBModellingv1_0 is deprecated, please use instead exportToFile!"
        )
        self.exportToFile(_outfileName)

    # Method for making a copy in a new instance
    def copy(self):
        return XSDataInputBioSaxsISPyBModellingv1_0.parseString(self.marshal())

    # Static method for parsing a string
    def parseString(_inString):
        doc = minidom.parseString(_inString)
        rootNode = doc.documentElement
        rootObj = XSDataInputBioSaxsISPyBModellingv1_0()
        rootObj.build(rootNode)
        # Check that all minOccurs are obeyed by marshalling the created object
        oStreamString = StringIO()
        rootObj.export(oStreamString, 0, name_="XSDataInputBioSaxsISPyBModellingv1_0")
        oStreamString.close()
        return rootObj

    parseString = staticmethod(parseString)
    # Static method for parsing a file
    def parseFile(_inFilePath):
        doc = minidom.parse(_inFilePath)
        rootNode = doc.documentElement
        rootObj = XSDataInputBioSaxsISPyBModellingv1_0()
        rootObj.build(rootNode)
        return rootObj

    parseFile = staticmethod(parseFile)


# end class XSDataInputBioSaxsISPyBModellingv1_0


class XSDataInputBioSaxsISPyB_HPLCv1_0(XSDataInput):
    """Input class for populating ISPyB"""

    def __init__(
        self,
        configuration=None,
        hplcPlot=None,
        jsonFile=None,
        hdf5File=None,
        sample=None,
    ):
        XSDataInput.__init__(self, configuration)
        if sample is None:
            self._sample = None
        elif sample.__class__.__name__ == "XSDataBioSaxsSample":
            self._sample = sample
        else:
            strMessage = (
                "ERROR! XSDataInputBioSaxsISPyB_HPLCv1_0 constructor argument 'sample' is not XSDataBioSaxsSample but %s"
                % self._sample.__class__.__name__
            )
            raise BaseException(strMessage)
        if hdf5File is None:
            self._hdf5File = None
        elif hdf5File.__class__.__name__ == "XSDataFile":
            self._hdf5File = hdf5File
        else:
            strMessage = (
                "ERROR! XSDataInputBioSaxsISPyB_HPLCv1_0 constructor argument 'hdf5File' is not XSDataFile but %s"
                % self._hdf5File.__class__.__name__
            )
            raise BaseException(strMessage)
        if jsonFile is None:
            self._jsonFile = None
        elif jsonFile.__class__.__name__ == "XSDataFile":
            self._jsonFile = jsonFile
        else:
            strMessage = (
                "ERROR! XSDataInputBioSaxsISPyB_HPLCv1_0 constructor argument 'jsonFile' is not XSDataFile but %s"
                % self._jsonFile.__class__.__name__
            )
            raise BaseException(strMessage)
        if hplcPlot is None:
            self._hplcPlot = None
        elif hplcPlot.__class__.__name__ == "XSDataFile":
            self._hplcPlot = hplcPlot
        else:
            strMessage = (
                "ERROR! XSDataInputBioSaxsISPyB_HPLCv1_0 constructor argument 'hplcPlot' is not XSDataFile but %s"
                % self._hplcPlot.__class__.__name__
            )
            raise BaseException(strMessage)

    # Methods and properties for the 'sample' attribute
    def getSample(self):
        return self._sample

    def setSample(self, sample):
        if sample is None:
            self._sample = None
        elif sample.__class__.__name__ == "XSDataBioSaxsSample":
            self._sample = sample
        else:
            strMessage = (
                "ERROR! XSDataInputBioSaxsISPyB_HPLCv1_0.setSample argument is not XSDataBioSaxsSample but %s"
                % sample.__class__.__name__
            )
            raise BaseException(strMessage)

    def delSample(self):
        self._sample = None

    sample = property(getSample, setSample, delSample, "Property for sample")
    # Methods and properties for the 'hdf5File' attribute
    def getHdf5File(self):
        return self._hdf5File

    def setHdf5File(self, hdf5File):
        if hdf5File is None:
            self._hdf5File = None
        elif hdf5File.__class__.__name__ == "XSDataFile":
            self._hdf5File = hdf5File
        else:
            strMessage = (
                "ERROR! XSDataInputBioSaxsISPyB_HPLCv1_0.setHdf5File argument is not XSDataFile but %s"
                % hdf5File.__class__.__name__
            )
            raise BaseException(strMessage)

    def delHdf5File(self):
        self._hdf5File = None

    hdf5File = property(getHdf5File, setHdf5File, delHdf5File, "Property for hdf5File")
    # Methods and properties for the 'jsonFile' attribute
    def getJsonFile(self):
        return self._jsonFile

    def setJsonFile(self, jsonFile):
        if jsonFile is None:
            self._jsonFile = None
        elif jsonFile.__class__.__name__ == "XSDataFile":
            self._jsonFile = jsonFile
        else:
            strMessage = (
                "ERROR! XSDataInputBioSaxsISPyB_HPLCv1_0.setJsonFile argument is not XSDataFile but %s"
                % jsonFile.__class__.__name__
            )
            raise BaseException(strMessage)

    def delJsonFile(self):
        self._jsonFile = None

    jsonFile = property(getJsonFile, setJsonFile, delJsonFile, "Property for jsonFile")
    # Methods and properties for the 'hplcPlot' attribute
    def getHplcPlot(self):
        return self._hplcPlot

    def setHplcPlot(self, hplcPlot):
        if hplcPlot is None:
            self._hplcPlot = None
        elif hplcPlot.__class__.__name__ == "XSDataFile":
            self._hplcPlot = hplcPlot
        else:
            strMessage = (
                "ERROR! XSDataInputBioSaxsISPyB_HPLCv1_0.setHplcPlot argument is not XSDataFile but %s"
                % hplcPlot.__class__.__name__
            )
            raise BaseException(strMessage)

    def delHplcPlot(self):
        self._hplcPlot = None

    hplcPlot = property(getHplcPlot, setHplcPlot, delHplcPlot, "Property for hplcPlot")

    def export(self, outfile, level, name_="XSDataInputBioSaxsISPyB_HPLCv1_0"):
        showIndent(outfile, level)
        outfile.write(unicode("<%s>\n" % name_))
        self.exportChildren(outfile, level + 1, name_)
        showIndent(outfile, level)
        outfile.write(unicode("</%s>\n" % name_))

    def exportChildren(self, outfile, level, name_="XSDataInputBioSaxsISPyB_HPLCv1_0"):
        XSDataInput.exportChildren(self, outfile, level, name_)
        if self._sample is not None:
            self.sample.export(outfile, level, name_="sample")
        else:
            warnEmptyAttribute("sample", "XSDataBioSaxsSample")
        if self._hdf5File is not None:
            self.hdf5File.export(outfile, level, name_="hdf5File")
        if self._jsonFile is not None:
            self.jsonFile.export(outfile, level, name_="jsonFile")
        if self._hplcPlot is not None:
            self.hplcPlot.export(outfile, level, name_="hplcPlot")

    def build(self, node_):
        for child_ in node_.childNodes:
            nodeName_ = child_.nodeName.split(":")[-1]
            self.buildChildren(child_, nodeName_)

    def buildChildren(self, child_, nodeName_):
        if child_.nodeType == Node.ELEMENT_NODE and nodeName_ == "sample":
            obj_ = XSDataBioSaxsSample()
            obj_.build(child_)
            self.setSample(obj_)
        elif child_.nodeType == Node.ELEMENT_NODE and nodeName_ == "hdf5File":
            obj_ = XSDataFile()
            obj_.build(child_)
            self.setHdf5File(obj_)
        elif child_.nodeType == Node.ELEMENT_NODE and nodeName_ == "jsonFile":
            obj_ = XSDataFile()
            obj_.build(child_)
            self.setJsonFile(obj_)
        elif child_.nodeType == Node.ELEMENT_NODE and nodeName_ == "hplcPlot":
            obj_ = XSDataFile()
            obj_.build(child_)
            self.setHplcPlot(obj_)
        XSDataInput.buildChildren(self, child_, nodeName_)

    # Method for marshalling an object
    def marshal(self):
        oStreamString = StringIO()
        oStreamString.write(unicode('<?xml version="1.0" ?>\n'))
        self.export(oStreamString, 0, name_="XSDataInputBioSaxsISPyB_HPLCv1_0")
        oStringXML = oStreamString.getvalue()
        oStreamString.close()
        return oStringXML

    # Only to export the entire XML tree to a file stream on disk
    def exportToFile(self, _outfileName):
        outfile = open(_outfileName, "w")
        outfile.write(unicode('<?xml version="1.0" ?>\n'))
        self.export(outfile, 0, name_="XSDataInputBioSaxsISPyB_HPLCv1_0")
        outfile.close()

    # Deprecated method, replaced by exportToFile
    def outputFile(self, _outfileName):
        print(
            "WARNING: Method outputFile in class XSDataInputBioSaxsISPyB_HPLCv1_0 is deprecated, please use instead exportToFile!"
        )
        self.exportToFile(_outfileName)

    # Method for making a copy in a new instance
    def copy(self):
        return XSDataInputBioSaxsISPyB_HPLCv1_0.parseString(self.marshal())

    # Static method for parsing a string
    def parseString(_inString):
        doc = minidom.parseString(_inString)
        rootNode = doc.documentElement
        rootObj = XSDataInputBioSaxsISPyB_HPLCv1_0()
        rootObj.build(rootNode)
        # Check that all minOccurs are obeyed by marshalling the created object
        oStreamString = StringIO()
        rootObj.export(oStreamString, 0, name_="XSDataInputBioSaxsISPyB_HPLCv1_0")
        oStreamString.close()
        return rootObj

    parseString = staticmethod(parseString)
    # Static method for parsing a file
    def parseFile(_inFilePath):
        doc = minidom.parse(_inFilePath)
        rootNode = doc.documentElement
        rootObj = XSDataInputBioSaxsISPyB_HPLCv1_0()
        rootObj.build(rootNode)
        return rootObj

    parseFile = staticmethod(parseFile)


# end class XSDataInputBioSaxsISPyB_HPLCv1_0


class XSDataInputBioSaxsISPyBv1_0(XSDataInput):
    """Input class for populating ISPyB"""

    def __init__(
        self,
        configuration=None,
        densityPlot=None,
        kratkyPlot=None,
        guinierPlot=None,
        scatterPlot=None,
        averageSample=None,
        bestBuffer=None,
        subtractedFilePath=None,
        sampleFrames=None,
        bufferFrames=None,
        averageFilePath=None,
        discardedFrames=None,
        averagedFrames=None,
        curves=None,
        frameMerged=None,
        frameAverage=None,
        volume=None,
        gnom=None,
        autoRg=None,
        sample=None,
    ):
        XSDataInput.__init__(self, configuration)
        if sample is None:
            self._sample = None
        elif sample.__class__.__name__ == "XSDataBioSaxsSample":
            self._sample = sample
        else:
            strMessage = (
                "ERROR! XSDataInputBioSaxsISPyBv1_0 constructor argument 'sample' is not XSDataBioSaxsSample but %s"
                % self._sample.__class__.__name__
            )
            raise BaseException(strMessage)
        if autoRg is None:
            self._autoRg = None
        elif autoRg.__class__.__name__ == "XSDataAutoRg":
            self._autoRg = autoRg
        else:
            strMessage = (
                "ERROR! XSDataInputBioSaxsISPyBv1_0 constructor argument 'autoRg' is not XSDataAutoRg but %s"
                % self._autoRg.__class__.__name__
            )
            raise BaseException(strMessage)
        if gnom is None:
            self._gnom = None
        elif gnom.__class__.__name__ == "XSDataGnom":
            self._gnom = gnom
        else:
            strMessage = (
                "ERROR! XSDataInputBioSaxsISPyBv1_0 constructor argument 'gnom' is not XSDataGnom but %s"
                % self._gnom.__class__.__name__
            )
            raise BaseException(strMessage)
        if volume is None:
            self._volume = None
        elif volume.__class__.__name__ == "XSDataDoubleWithUnit":
            self._volume = volume
        else:
            strMessage = (
                "ERROR! XSDataInputBioSaxsISPyBv1_0 constructor argument 'volume' is not XSDataDoubleWithUnit but %s"
                % self._volume.__class__.__name__
            )
            raise BaseException(strMessage)
        if frameAverage is None:
            self._frameAverage = None
        elif frameAverage.__class__.__name__ == "XSDataInteger":
            self._frameAverage = frameAverage
        else:
            strMessage = (
                "ERROR! XSDataInputBioSaxsISPyBv1_0 constructor argument 'frameAverage' is not XSDataInteger but %s"
                % self._frameAverage.__class__.__name__
            )
            raise BaseException(strMessage)
        if frameMerged is None:
            self._frameMerged = None
        elif frameMerged.__class__.__name__ == "XSDataInteger":
            self._frameMerged = frameMerged
        else:
            strMessage = (
                "ERROR! XSDataInputBioSaxsISPyBv1_0 constructor argument 'frameMerged' is not XSDataInteger but %s"
                % self._frameMerged.__class__.__name__
            )
            raise BaseException(strMessage)
        if curves is None:
            self._curves = []
        elif curves.__class__.__name__ == "list":
            self._curves = curves
        else:
            strMessage = (
                "ERROR! XSDataInputBioSaxsISPyBv1_0 constructor argument 'curves' is not list but %s"
                % self._curves.__class__.__name__
            )
            raise BaseException(strMessage)
        if averagedFrames is None:
            self._averagedFrames = []
        elif averagedFrames.__class__.__name__ == "list":
            self._averagedFrames = averagedFrames
        else:
            strMessage = (
                "ERROR! XSDataInputBioSaxsISPyBv1_0 constructor argument 'averagedFrames' is not list but %s"
                % self._averagedFrames.__class__.__name__
            )
            raise BaseException(strMessage)
        if discardedFrames is None:
            self._discardedFrames = []
        elif discardedFrames.__class__.__name__ == "list":
            self._discardedFrames = discardedFrames
        else:
            strMessage = (
                "ERROR! XSDataInputBioSaxsISPyBv1_0 constructor argument 'discardedFrames' is not list but %s"
                % self._discardedFrames.__class__.__name__
            )
            raise BaseException(strMessage)
        if averageFilePath is None:
            self._averageFilePath = None
        elif averageFilePath.__class__.__name__ == "XSDataFile":
            self._averageFilePath = averageFilePath
        else:
            strMessage = (
                "ERROR! XSDataInputBioSaxsISPyBv1_0 constructor argument 'averageFilePath' is not XSDataFile but %s"
                % self._averageFilePath.__class__.__name__
            )
            raise BaseException(strMessage)
        if bufferFrames is None:
            self._bufferFrames = []
        elif bufferFrames.__class__.__name__ == "list":
            self._bufferFrames = bufferFrames
        else:
            strMessage = (
                "ERROR! XSDataInputBioSaxsISPyBv1_0 constructor argument 'bufferFrames' is not list but %s"
                % self._bufferFrames.__class__.__name__
            )
            raise BaseException(strMessage)
        if sampleFrames is None:
            self._sampleFrames = []
        elif sampleFrames.__class__.__name__ == "list":
            self._sampleFrames = sampleFrames
        else:
            strMessage = (
                "ERROR! XSDataInputBioSaxsISPyBv1_0 constructor argument 'sampleFrames' is not list but %s"
                % self._sampleFrames.__class__.__name__
            )
            raise BaseException(strMessage)
        if subtractedFilePath is None:
            self._subtractedFilePath = None
        elif subtractedFilePath.__class__.__name__ == "XSDataFile":
            self._subtractedFilePath = subtractedFilePath
        else:
            strMessage = (
                "ERROR! XSDataInputBioSaxsISPyBv1_0 constructor argument 'subtractedFilePath' is not XSDataFile but %s"
                % self._subtractedFilePath.__class__.__name__
            )
            raise BaseException(strMessage)
        if bestBuffer is None:
            self._bestBuffer = None
        elif bestBuffer.__class__.__name__ == "XSDataFile":
            self._bestBuffer = bestBuffer
        else:
            strMessage = (
                "ERROR! XSDataInputBioSaxsISPyBv1_0 constructor argument 'bestBuffer' is not XSDataFile but %s"
                % self._bestBuffer.__class__.__name__
            )
            raise BaseException(strMessage)
        if averageSample is None:
            self._averageSample = None
        elif averageSample.__class__.__name__ == "XSDataFile":
            self._averageSample = averageSample
        else:
            strMessage = (
                "ERROR! XSDataInputBioSaxsISPyBv1_0 constructor argument 'averageSample' is not XSDataFile but %s"
                % self._averageSample.__class__.__name__
            )
            raise BaseException(strMessage)
        if scatterPlot is None:
            self._scatterPlot = None
        elif scatterPlot.__class__.__name__ == "XSDataFile":
            self._scatterPlot = scatterPlot
        else:
            strMessage = (
                "ERROR! XSDataInputBioSaxsISPyBv1_0 constructor argument 'scatterPlot' is not XSDataFile but %s"
                % self._scatterPlot.__class__.__name__
            )
            raise BaseException(strMessage)
        if guinierPlot is None:
            self._guinierPlot = None
        elif guinierPlot.__class__.__name__ == "XSDataFile":
            self._guinierPlot = guinierPlot
        else:
            strMessage = (
                "ERROR! XSDataInputBioSaxsISPyBv1_0 constructor argument 'guinierPlot' is not XSDataFile but %s"
                % self._guinierPlot.__class__.__name__
            )
            raise BaseException(strMessage)
        if kratkyPlot is None:
            self._kratkyPlot = None
        elif kratkyPlot.__class__.__name__ == "XSDataFile":
            self._kratkyPlot = kratkyPlot
        else:
            strMessage = (
                "ERROR! XSDataInputBioSaxsISPyBv1_0 constructor argument 'kratkyPlot' is not XSDataFile but %s"
                % self._kratkyPlot.__class__.__name__
            )
            raise BaseException(strMessage)
        if densityPlot is None:
            self._densityPlot = None
        elif densityPlot.__class__.__name__ == "XSDataFile":
            self._densityPlot = densityPlot
        else:
            strMessage = (
                "ERROR! XSDataInputBioSaxsISPyBv1_0 constructor argument 'densityPlot' is not XSDataFile but %s"
                % self._densityPlot.__class__.__name__
            )
            raise BaseException(strMessage)

    # Methods and properties for the 'sample' attribute
    def getSample(self):
        return self._sample

    def setSample(self, sample):
        if sample is None:
            self._sample = None
        elif sample.__class__.__name__ == "XSDataBioSaxsSample":
            self._sample = sample
        else:
            strMessage = (
                "ERROR! XSDataInputBioSaxsISPyBv1_0.setSample argument is not XSDataBioSaxsSample but %s"
                % sample.__class__.__name__
            )
            raise BaseException(strMessage)

    def delSample(self):
        self._sample = None

    sample = property(getSample, setSample, delSample, "Property for sample")
    # Methods and properties for the 'autoRg' attribute
    def getAutoRg(self):
        return self._autoRg

    def setAutoRg(self, autoRg):
        if autoRg is None:
            self._autoRg = None
        elif autoRg.__class__.__name__ == "XSDataAutoRg":
            self._autoRg = autoRg
        else:
            strMessage = (
                "ERROR! XSDataInputBioSaxsISPyBv1_0.setAutoRg argument is not XSDataAutoRg but %s"
                % autoRg.__class__.__name__
            )
            raise BaseException(strMessage)

    def delAutoRg(self):
        self._autoRg = None

    autoRg = property(getAutoRg, setAutoRg, delAutoRg, "Property for autoRg")
    # Methods and properties for the 'gnom' attribute
    def getGnom(self):
        return self._gnom

    def setGnom(self, gnom):
        if gnom is None:
            self._gnom = None
        elif gnom.__class__.__name__ == "XSDataGnom":
            self._gnom = gnom
        else:
            strMessage = (
                "ERROR! XSDataInputBioSaxsISPyBv1_0.setGnom argument is not XSDataGnom but %s"
                % gnom.__class__.__name__
            )
            raise BaseException(strMessage)

    def delGnom(self):
        self._gnom = None

    gnom = property(getGnom, setGnom, delGnom, "Property for gnom")
    # Methods and properties for the 'volume' attribute
    def getVolume(self):
        return self._volume

    def setVolume(self, volume):
        if volume is None:
            self._volume = None
        elif volume.__class__.__name__ == "XSDataDoubleWithUnit":
            self._volume = volume
        else:
            strMessage = (
                "ERROR! XSDataInputBioSaxsISPyBv1_0.setVolume argument is not XSDataDoubleWithUnit but %s"
                % volume.__class__.__name__
            )
            raise BaseException(strMessage)

    def delVolume(self):
        self._volume = None

    volume = property(getVolume, setVolume, delVolume, "Property for volume")
    # Methods and properties for the 'frameAverage' attribute
    def getFrameAverage(self):
        return self._frameAverage

    def setFrameAverage(self, frameAverage):
        if frameAverage is None:
            self._frameAverage = None
        elif frameAverage.__class__.__name__ == "XSDataInteger":
            self._frameAverage = frameAverage
        else:
            strMessage = (
                "ERROR! XSDataInputBioSaxsISPyBv1_0.setFrameAverage argument is not XSDataInteger but %s"
                % frameAverage.__class__.__name__
            )
            raise BaseException(strMessage)

    def delFrameAverage(self):
        self._frameAverage = None

    frameAverage = property(
        getFrameAverage, setFrameAverage, delFrameAverage, "Property for frameAverage"
    )
    # Methods and properties for the 'frameMerged' attribute
    def getFrameMerged(self):
        return self._frameMerged

    def setFrameMerged(self, frameMerged):
        if frameMerged is None:
            self._frameMerged = None
        elif frameMerged.__class__.__name__ == "XSDataInteger":
            self._frameMerged = frameMerged
        else:
            strMessage = (
                "ERROR! XSDataInputBioSaxsISPyBv1_0.setFrameMerged argument is not XSDataInteger but %s"
                % frameMerged.__class__.__name__
            )
            raise BaseException(strMessage)

    def delFrameMerged(self):
        self._frameMerged = None

    frameMerged = property(
        getFrameMerged, setFrameMerged, delFrameMerged, "Property for frameMerged"
    )
    # Methods and properties for the 'curves' attribute
    def getCurves(self):
        return self._curves

    def setCurves(self, curves):
        if curves is None:
            self._curves = []
        elif curves.__class__.__name__ == "list":
            self._curves = curves
        else:
            strMessage = (
                "ERROR! XSDataInputBioSaxsISPyBv1_0.setCurves argument is not list but %s"
                % curves.__class__.__name__
            )
            raise BaseException(strMessage)

    def delCurves(self):
        self._curves = None

    curves = property(getCurves, setCurves, delCurves, "Property for curves")

    def addCurves(self, value):
        if value is None:
            strMessage = "ERROR! XSDataInputBioSaxsISPyBv1_0.addCurves argument is None"
            raise BaseException(strMessage)
        elif value.__class__.__name__ == "XSDataFile":
            self._curves.append(value)
        else:
            strMessage = (
                "ERROR! XSDataInputBioSaxsISPyBv1_0.addCurves argument is not XSDataFile but %s"
                % value.__class__.__name__
            )
            raise BaseException(strMessage)

    def insertCurves(self, index, value):
        if index is None:
            strMessage = "ERROR! XSDataInputBioSaxsISPyBv1_0.insertCurves argument 'index' is None"
            raise BaseException(strMessage)
        if value is None:
            strMessage = "ERROR! XSDataInputBioSaxsISPyBv1_0.insertCurves argument 'value' is None"
            raise BaseException(strMessage)
        elif value.__class__.__name__ == "XSDataFile":
            self._curves[index] = value
        else:
            strMessage = (
                "ERROR! XSDataInputBioSaxsISPyBv1_0.addCurves argument is not XSDataFile but %s"
                % value.__class__.__name__
            )
            raise BaseException(strMessage)

    # Methods and properties for the 'averagedFrames' attribute
    def getAveragedFrames(self):
        return self._averagedFrames

    def setAveragedFrames(self, averagedFrames):
        if averagedFrames is None:
            self._averagedFrames = []
        elif averagedFrames.__class__.__name__ == "list":
            self._averagedFrames = averagedFrames
        else:
            strMessage = (
                "ERROR! XSDataInputBioSaxsISPyBv1_0.setAveragedFrames argument is not list but %s"
                % averagedFrames.__class__.__name__
            )
            raise BaseException(strMessage)

    def delAveragedFrames(self):
        self._averagedFrames = None

    averagedFrames = property(
        getAveragedFrames,
        setAveragedFrames,
        delAveragedFrames,
        "Property for averagedFrames",
    )

    def addAveragedFrames(self, value):
        if value is None:
            strMessage = (
                "ERROR! XSDataInputBioSaxsISPyBv1_0.addAveragedFrames argument is None"
            )
            raise BaseException(strMessage)
        elif value.__class__.__name__ == "XSDataFile":
            self._averagedFrames.append(value)
        else:
            strMessage = (
                "ERROR! XSDataInputBioSaxsISPyBv1_0.addAveragedFrames argument is not XSDataFile but %s"
                % value.__class__.__name__
            )
            raise BaseException(strMessage)

    def insertAveragedFrames(self, index, value):
        if index is None:
            strMessage = "ERROR! XSDataInputBioSaxsISPyBv1_0.insertAveragedFrames argument 'index' is None"
            raise BaseException(strMessage)
        if value is None:
            strMessage = "ERROR! XSDataInputBioSaxsISPyBv1_0.insertAveragedFrames argument 'value' is None"
            raise BaseException(strMessage)
        elif value.__class__.__name__ == "XSDataFile":
            self._averagedFrames[index] = value
        else:
            strMessage = (
                "ERROR! XSDataInputBioSaxsISPyBv1_0.addAveragedFrames argument is not XSDataFile but %s"
                % value.__class__.__name__
            )
            raise BaseException(strMessage)

    # Methods and properties for the 'discardedFrames' attribute
    def getDiscardedFrames(self):
        return self._discardedFrames

    def setDiscardedFrames(self, discardedFrames):
        if discardedFrames is None:
            self._discardedFrames = []
        elif discardedFrames.__class__.__name__ == "list":
            self._discardedFrames = discardedFrames
        else:
            strMessage = (
                "ERROR! XSDataInputBioSaxsISPyBv1_0.setDiscardedFrames argument is not list but %s"
                % discardedFrames.__class__.__name__
            )
            raise BaseException(strMessage)

    def delDiscardedFrames(self):
        self._discardedFrames = None

    discardedFrames = property(
        getDiscardedFrames,
        setDiscardedFrames,
        delDiscardedFrames,
        "Property for discardedFrames",
    )

    def addDiscardedFrames(self, value):
        if value is None:
            strMessage = (
                "ERROR! XSDataInputBioSaxsISPyBv1_0.addDiscardedFrames argument is None"
            )
            raise BaseException(strMessage)
        elif value.__class__.__name__ == "XSDataFile":
            self._discardedFrames.append(value)
        else:
            strMessage = (
                "ERROR! XSDataInputBioSaxsISPyBv1_0.addDiscardedFrames argument is not XSDataFile but %s"
                % value.__class__.__name__
            )
            raise BaseException(strMessage)

    def insertDiscardedFrames(self, index, value):
        if index is None:
            strMessage = "ERROR! XSDataInputBioSaxsISPyBv1_0.insertDiscardedFrames argument 'index' is None"
            raise BaseException(strMessage)
        if value is None:
            strMessage = "ERROR! XSDataInputBioSaxsISPyBv1_0.insertDiscardedFrames argument 'value' is None"
            raise BaseException(strMessage)
        elif value.__class__.__name__ == "XSDataFile":
            self._discardedFrames[index] = value
        else:
            strMessage = (
                "ERROR! XSDataInputBioSaxsISPyBv1_0.addDiscardedFrames argument is not XSDataFile but %s"
                % value.__class__.__name__
            )
            raise BaseException(strMessage)

    # Methods and properties for the 'averageFilePath' attribute
    def getAverageFilePath(self):
        return self._averageFilePath

    def setAverageFilePath(self, averageFilePath):
        if averageFilePath is None:
            self._averageFilePath = None
        elif averageFilePath.__class__.__name__ == "XSDataFile":
            self._averageFilePath = averageFilePath
        else:
            strMessage = (
                "ERROR! XSDataInputBioSaxsISPyBv1_0.setAverageFilePath argument is not XSDataFile but %s"
                % averageFilePath.__class__.__name__
            )
            raise BaseException(strMessage)

    def delAverageFilePath(self):
        self._averageFilePath = None

    averageFilePath = property(
        getAverageFilePath,
        setAverageFilePath,
        delAverageFilePath,
        "Property for averageFilePath",
    )
    # Methods and properties for the 'bufferFrames' attribute
    def getBufferFrames(self):
        return self._bufferFrames

    def setBufferFrames(self, bufferFrames):
        if bufferFrames is None:
            self._bufferFrames = []
        elif bufferFrames.__class__.__name__ == "list":
            self._bufferFrames = bufferFrames
        else:
            strMessage = (
                "ERROR! XSDataInputBioSaxsISPyBv1_0.setBufferFrames argument is not list but %s"
                % bufferFrames.__class__.__name__
            )
            raise BaseException(strMessage)

    def delBufferFrames(self):
        self._bufferFrames = None

    bufferFrames = property(
        getBufferFrames, setBufferFrames, delBufferFrames, "Property for bufferFrames"
    )

    def addBufferFrames(self, value):
        if value is None:
            strMessage = (
                "ERROR! XSDataInputBioSaxsISPyBv1_0.addBufferFrames argument is None"
            )
            raise BaseException(strMessage)
        elif value.__class__.__name__ == "XSDataFile":
            self._bufferFrames.append(value)
        else:
            strMessage = (
                "ERROR! XSDataInputBioSaxsISPyBv1_0.addBufferFrames argument is not XSDataFile but %s"
                % value.__class__.__name__
            )
            raise BaseException(strMessage)

    def insertBufferFrames(self, index, value):
        if index is None:
            strMessage = "ERROR! XSDataInputBioSaxsISPyBv1_0.insertBufferFrames argument 'index' is None"
            raise BaseException(strMessage)
        if value is None:
            strMessage = "ERROR! XSDataInputBioSaxsISPyBv1_0.insertBufferFrames argument 'value' is None"
            raise BaseException(strMessage)
        elif value.__class__.__name__ == "XSDataFile":
            self._bufferFrames[index] = value
        else:
            strMessage = (
                "ERROR! XSDataInputBioSaxsISPyBv1_0.addBufferFrames argument is not XSDataFile but %s"
                % value.__class__.__name__
            )
            raise BaseException(strMessage)

    # Methods and properties for the 'sampleFrames' attribute
    def getSampleFrames(self):
        return self._sampleFrames

    def setSampleFrames(self, sampleFrames):
        if sampleFrames is None:
            self._sampleFrames = []
        elif sampleFrames.__class__.__name__ == "list":
            self._sampleFrames = sampleFrames
        else:
            strMessage = (
                "ERROR! XSDataInputBioSaxsISPyBv1_0.setSampleFrames argument is not list but %s"
                % sampleFrames.__class__.__name__
            )
            raise BaseException(strMessage)

    def delSampleFrames(self):
        self._sampleFrames = None

    sampleFrames = property(
        getSampleFrames, setSampleFrames, delSampleFrames, "Property for sampleFrames"
    )

    def addSampleFrames(self, value):
        if value is None:
            strMessage = (
                "ERROR! XSDataInputBioSaxsISPyBv1_0.addSampleFrames argument is None"
            )
            raise BaseException(strMessage)
        elif value.__class__.__name__ == "XSDataFile":
            self._sampleFrames.append(value)
        else:
            strMessage = (
                "ERROR! XSDataInputBioSaxsISPyBv1_0.addSampleFrames argument is not XSDataFile but %s"
                % value.__class__.__name__
            )
            raise BaseException(strMessage)

    def insertSampleFrames(self, index, value):
        if index is None:
            strMessage = "ERROR! XSDataInputBioSaxsISPyBv1_0.insertSampleFrames argument 'index' is None"
            raise BaseException(strMessage)
        if value is None:
            strMessage = "ERROR! XSDataInputBioSaxsISPyBv1_0.insertSampleFrames argument 'value' is None"
            raise BaseException(strMessage)
        elif value.__class__.__name__ == "XSDataFile":
            self._sampleFrames[index] = value
        else:
            strMessage = (
                "ERROR! XSDataInputBioSaxsISPyBv1_0.addSampleFrames argument is not XSDataFile but %s"
                % value.__class__.__name__
            )
            raise BaseException(strMessage)

    # Methods and properties for the 'subtractedFilePath' attribute
    def getSubtractedFilePath(self):
        return self._subtractedFilePath

    def setSubtractedFilePath(self, subtractedFilePath):
        if subtractedFilePath is None:
            self._subtractedFilePath = None
        elif subtractedFilePath.__class__.__name__ == "XSDataFile":
            self._subtractedFilePath = subtractedFilePath
        else:
            strMessage = (
                "ERROR! XSDataInputBioSaxsISPyBv1_0.setSubtractedFilePath argument is not XSDataFile but %s"
                % subtractedFilePath.__class__.__name__
            )
            raise BaseException(strMessage)

    def delSubtractedFilePath(self):
        self._subtractedFilePath = None

    subtractedFilePath = property(
        getSubtractedFilePath,
        setSubtractedFilePath,
        delSubtractedFilePath,
        "Property for subtractedFilePath",
    )
    # Methods and properties for the 'bestBuffer' attribute
    def getBestBuffer(self):
        return self._bestBuffer

    def setBestBuffer(self, bestBuffer):
        if bestBuffer is None:
            self._bestBuffer = None
        elif bestBuffer.__class__.__name__ == "XSDataFile":
            self._bestBuffer = bestBuffer
        else:
            strMessage = (
                "ERROR! XSDataInputBioSaxsISPyBv1_0.setBestBuffer argument is not XSDataFile but %s"
                % bestBuffer.__class__.__name__
            )
            raise BaseException(strMessage)

    def delBestBuffer(self):
        self._bestBuffer = None

    bestBuffer = property(
        getBestBuffer, setBestBuffer, delBestBuffer, "Property for bestBuffer"
    )
    # Methods and properties for the 'averageSample' attribute
    def getAverageSample(self):
        return self._averageSample

    def setAverageSample(self, averageSample):
        if averageSample is None:
            self._averageSample = None
        elif averageSample.__class__.__name__ == "XSDataFile":
            self._averageSample = averageSample
        else:
            strMessage = (
                "ERROR! XSDataInputBioSaxsISPyBv1_0.setAverageSample argument is not XSDataFile but %s"
                % averageSample.__class__.__name__
            )
            raise BaseException(strMessage)

    def delAverageSample(self):
        self._averageSample = None

    averageSample = property(
        getAverageSample,
        setAverageSample,
        delAverageSample,
        "Property for averageSample",
    )
    # Methods and properties for the 'scatterPlot' attribute
    def getScatterPlot(self):
        return self._scatterPlot

    def setScatterPlot(self, scatterPlot):
        if scatterPlot is None:
            self._scatterPlot = None
        elif scatterPlot.__class__.__name__ == "XSDataFile":
            self._scatterPlot = scatterPlot
        else:
            strMessage = (
                "ERROR! XSDataInputBioSaxsISPyBv1_0.setScatterPlot argument is not XSDataFile but %s"
                % scatterPlot.__class__.__name__
            )
            raise BaseException(strMessage)

    def delScatterPlot(self):
        self._scatterPlot = None

    scatterPlot = property(
        getScatterPlot, setScatterPlot, delScatterPlot, "Property for scatterPlot"
    )
    # Methods and properties for the 'guinierPlot' attribute
    def getGuinierPlot(self):
        return self._guinierPlot

    def setGuinierPlot(self, guinierPlot):
        if guinierPlot is None:
            self._guinierPlot = None
        elif guinierPlot.__class__.__name__ == "XSDataFile":
            self._guinierPlot = guinierPlot
        else:
            strMessage = (
                "ERROR! XSDataInputBioSaxsISPyBv1_0.setGuinierPlot argument is not XSDataFile but %s"
                % guinierPlot.__class__.__name__
            )
            raise BaseException(strMessage)

    def delGuinierPlot(self):
        self._guinierPlot = None

    guinierPlot = property(
        getGuinierPlot, setGuinierPlot, delGuinierPlot, "Property for guinierPlot"
    )
    # Methods and properties for the 'kratkyPlot' attribute
    def getKratkyPlot(self):
        return self._kratkyPlot

    def setKratkyPlot(self, kratkyPlot):
        if kratkyPlot is None:
            self._kratkyPlot = None
        elif kratkyPlot.__class__.__name__ == "XSDataFile":
            self._kratkyPlot = kratkyPlot
        else:
            strMessage = (
                "ERROR! XSDataInputBioSaxsISPyBv1_0.setKratkyPlot argument is not XSDataFile but %s"
                % kratkyPlot.__class__.__name__
            )
            raise BaseException(strMessage)

    def delKratkyPlot(self):
        self._kratkyPlot = None

    kratkyPlot = property(
        getKratkyPlot, setKratkyPlot, delKratkyPlot, "Property for kratkyPlot"
    )
    # Methods and properties for the 'densityPlot' attribute
    def getDensityPlot(self):
        return self._densityPlot

    def setDensityPlot(self, densityPlot):
        if densityPlot is None:
            self._densityPlot = None
        elif densityPlot.__class__.__name__ == "XSDataFile":
            self._densityPlot = densityPlot
        else:
            strMessage = (
                "ERROR! XSDataInputBioSaxsISPyBv1_0.setDensityPlot argument is not XSDataFile but %s"
                % densityPlot.__class__.__name__
            )
            raise BaseException(strMessage)

    def delDensityPlot(self):
        self._densityPlot = None

    densityPlot = property(
        getDensityPlot, setDensityPlot, delDensityPlot, "Property for densityPlot"
    )

    def export(self, outfile, level, name_="XSDataInputBioSaxsISPyBv1_0"):
        showIndent(outfile, level)
        outfile.write(unicode("<%s>\n" % name_))
        self.exportChildren(outfile, level + 1, name_)
        showIndent(outfile, level)
        outfile.write(unicode("</%s>\n" % name_))

    def exportChildren(self, outfile, level, name_="XSDataInputBioSaxsISPyBv1_0"):
        XSDataInput.exportChildren(self, outfile, level, name_)
        if self._sample is not None:
            self.sample.export(outfile, level, name_="sample")
        else:
            warnEmptyAttribute("sample", "XSDataBioSaxsSample")
        if self._autoRg is not None:
            self.autoRg.export(outfile, level, name_="autoRg")
        if self._gnom is not None:
            self.gnom.export(outfile, level, name_="gnom")
        if self._volume is not None:
            self.volume.export(outfile, level, name_="volume")
        if self._frameAverage is not None:
            self.frameAverage.export(outfile, level, name_="frameAverage")
        if self._frameMerged is not None:
            self.frameMerged.export(outfile, level, name_="frameMerged")
        for curves_ in self.getCurves():
            curves_.export(outfile, level, name_="curves")
        for averagedFrames_ in self.getAveragedFrames():
            averagedFrames_.export(outfile, level, name_="averagedFrames")
        for discardedFrames_ in self.getDiscardedFrames():
            discardedFrames_.export(outfile, level, name_="discardedFrames")
        if self._averageFilePath is not None:
            self.averageFilePath.export(outfile, level, name_="averageFilePath")
        else:
            warnEmptyAttribute("averageFilePath", "XSDataFile")
        for bufferFrames_ in self.getBufferFrames():
            bufferFrames_.export(outfile, level, name_="bufferFrames")
        for sampleFrames_ in self.getSampleFrames():
            sampleFrames_.export(outfile, level, name_="sampleFrames")
        if self._subtractedFilePath is not None:
            self.subtractedFilePath.export(outfile, level, name_="subtractedFilePath")
        if self._bestBuffer is not None:
            self.bestBuffer.export(outfile, level, name_="bestBuffer")
        if self._averageSample is not None:
            self.averageSample.export(outfile, level, name_="averageSample")
        if self._scatterPlot is not None:
            self.scatterPlot.export(outfile, level, name_="scatterPlot")
        if self._guinierPlot is not None:
            self.guinierPlot.export(outfile, level, name_="guinierPlot")
        if self._kratkyPlot is not None:
            self.kratkyPlot.export(outfile, level, name_="kratkyPlot")
        if self._densityPlot is not None:
            self.densityPlot.export(outfile, level, name_="densityPlot")

    def build(self, node_):
        for child_ in node_.childNodes:
            nodeName_ = child_.nodeName.split(":")[-1]
            self.buildChildren(child_, nodeName_)

    def buildChildren(self, child_, nodeName_):
        if child_.nodeType == Node.ELEMENT_NODE and nodeName_ == "sample":
            obj_ = XSDataBioSaxsSample()
            obj_.build(child_)
            self.setSample(obj_)
        elif child_.nodeType == Node.ELEMENT_NODE and nodeName_ == "autoRg":
            obj_ = XSDataAutoRg()
            obj_.build(child_)
            self.setAutoRg(obj_)
        elif child_.nodeType == Node.ELEMENT_NODE and nodeName_ == "gnom":
            obj_ = XSDataGnom()
            obj_.build(child_)
            self.setGnom(obj_)
        elif child_.nodeType == Node.ELEMENT_NODE and nodeName_ == "volume":
            obj_ = XSDataDoubleWithUnit()
            obj_.build(child_)
            self.setVolume(obj_)
        elif child_.nodeType == Node.ELEMENT_NODE and nodeName_ == "frameAverage":
            obj_ = XSDataInteger()
            obj_.build(child_)
            self.setFrameAverage(obj_)
        elif child_.nodeType == Node.ELEMENT_NODE and nodeName_ == "frameMerged":
            obj_ = XSDataInteger()
            obj_.build(child_)
            self.setFrameMerged(obj_)
        elif child_.nodeType == Node.ELEMENT_NODE and nodeName_ == "curves":
            obj_ = XSDataFile()
            obj_.build(child_)
            self.curves.append(obj_)
        elif child_.nodeType == Node.ELEMENT_NODE and nodeName_ == "averagedFrames":
            obj_ = XSDataFile()
            obj_.build(child_)
            self.averagedFrames.append(obj_)
        elif child_.nodeType == Node.ELEMENT_NODE and nodeName_ == "discardedFrames":
            obj_ = XSDataFile()
            obj_.build(child_)
            self.discardedFrames.append(obj_)
        elif child_.nodeType == Node.ELEMENT_NODE and nodeName_ == "averageFilePath":
            obj_ = XSDataFile()
            obj_.build(child_)
            self.setAverageFilePath(obj_)
        elif child_.nodeType == Node.ELEMENT_NODE and nodeName_ == "bufferFrames":
            obj_ = XSDataFile()
            obj_.build(child_)
            self.bufferFrames.append(obj_)
        elif child_.nodeType == Node.ELEMENT_NODE and nodeName_ == "sampleFrames":
            obj_ = XSDataFile()
            obj_.build(child_)
            self.sampleFrames.append(obj_)
        elif child_.nodeType == Node.ELEMENT_NODE and nodeName_ == "subtractedFilePath":
            obj_ = XSDataFile()
            obj_.build(child_)
            self.setSubtractedFilePath(obj_)
        elif child_.nodeType == Node.ELEMENT_NODE and nodeName_ == "bestBuffer":
            obj_ = XSDataFile()
            obj_.build(child_)
            self.setBestBuffer(obj_)
        elif child_.nodeType == Node.ELEMENT_NODE and nodeName_ == "averageSample":
            obj_ = XSDataFile()
            obj_.build(child_)
            self.setAverageSample(obj_)
        elif child_.nodeType == Node.ELEMENT_NODE and nodeName_ == "scatterPlot":
            obj_ = XSDataFile()
            obj_.build(child_)
            self.setScatterPlot(obj_)
        elif child_.nodeType == Node.ELEMENT_NODE and nodeName_ == "guinierPlot":
            obj_ = XSDataFile()
            obj_.build(child_)
            self.setGuinierPlot(obj_)
        elif child_.nodeType == Node.ELEMENT_NODE and nodeName_ == "kratkyPlot":
            obj_ = XSDataFile()
            obj_.build(child_)
            self.setKratkyPlot(obj_)
        elif child_.nodeType == Node.ELEMENT_NODE and nodeName_ == "densityPlot":
            obj_ = XSDataFile()
            obj_.build(child_)
            self.setDensityPlot(obj_)
        XSDataInput.buildChildren(self, child_, nodeName_)

    # Method for marshalling an object
    def marshal(self):
        oStreamString = StringIO()
        oStreamString.write(unicode('<?xml version="1.0" ?>\n'))
        self.export(oStreamString, 0, name_="XSDataInputBioSaxsISPyBv1_0")
        oStringXML = oStreamString.getvalue()
        oStreamString.close()
        return oStringXML

    # Only to export the entire XML tree to a file stream on disk
    def exportToFile(self, _outfileName):
        outfile = open(_outfileName, "w")
        outfile.write(unicode('<?xml version="1.0" ?>\n'))
        self.export(outfile, 0, name_="XSDataInputBioSaxsISPyBv1_0")
        outfile.close()

    # Deprecated method, replaced by exportToFile
    def outputFile(self, _outfileName):
        print(
            "WARNING: Method outputFile in class XSDataInputBioSaxsISPyBv1_0 is deprecated, please use instead exportToFile!"
        )
        self.exportToFile(_outfileName)

    # Method for making a copy in a new instance
    def copy(self):
        return XSDataInputBioSaxsISPyBv1_0.parseString(self.marshal())

    # Static method for parsing a string
    def parseString(_inString):
        doc = minidom.parseString(_inString)
        rootNode = doc.documentElement
        rootObj = XSDataInputBioSaxsISPyBv1_0()
        rootObj.build(rootNode)
        # Check that all minOccurs are obeyed by marshalling the created object
        oStreamString = StringIO()
        rootObj.export(oStreamString, 0, name_="XSDataInputBioSaxsISPyBv1_0")
        oStreamString.close()
        return rootObj

    parseString = staticmethod(parseString)
    # Static method for parsing a file
    def parseFile(_inFilePath):
        doc = minidom.parse(_inFilePath)
        rootNode = doc.documentElement
        rootObj = XSDataInputBioSaxsISPyBv1_0()
        rootObj.build(rootNode)
        return rootObj

    parseFile = staticmethod(parseFile)


# end class XSDataInputBioSaxsISPyBv1_0


class XSDataInputBioSaxsNormalizev1_0(XSDataInput):
    def __init__(
        self,
        configuration=None,
        experimentSetup=None,
        sample=None,
        rawImageSize=None,
        normalizedImage=None,
        logFile=None,
        rawImage=None,
    ):
        XSDataInput.__init__(self, configuration)
        if rawImage is None:
            self._rawImage = None
        elif rawImage.__class__.__name__ == "XSDataImage":
            self._rawImage = rawImage
        else:
            strMessage = (
                "ERROR! XSDataInputBioSaxsNormalizev1_0 constructor argument 'rawImage' is not XSDataImage but %s"
                % self._rawImage.__class__.__name__
            )
            raise BaseException(strMessage)
        if logFile is None:
            self._logFile = None
        elif logFile.__class__.__name__ == "XSDataFile":
            self._logFile = logFile
        else:
            strMessage = (
                "ERROR! XSDataInputBioSaxsNormalizev1_0 constructor argument 'logFile' is not XSDataFile but %s"
                % self._logFile.__class__.__name__
            )
            raise BaseException(strMessage)
        if normalizedImage is None:
            self._normalizedImage = None
        elif normalizedImage.__class__.__name__ == "XSDataImage":
            self._normalizedImage = normalizedImage
        else:
            strMessage = (
                "ERROR! XSDataInputBioSaxsNormalizev1_0 constructor argument 'normalizedImage' is not XSDataImage but %s"
                % self._normalizedImage.__class__.__name__
            )
            raise BaseException(strMessage)
        if rawImageSize is None:
            self._rawImageSize = None
        elif rawImageSize.__class__.__name__ == "XSDataInteger":
            self._rawImageSize = rawImageSize
        else:
            strMessage = (
                "ERROR! XSDataInputBioSaxsNormalizev1_0 constructor argument 'rawImageSize' is not XSDataInteger but %s"
                % self._rawImageSize.__class__.__name__
            )
            raise BaseException(strMessage)
        if sample is None:
            self._sample = None
        elif sample.__class__.__name__ == "XSDataBioSaxsSample":
            self._sample = sample
        else:
            strMessage = (
                "ERROR! XSDataInputBioSaxsNormalizev1_0 constructor argument 'sample' is not XSDataBioSaxsSample but %s"
                % self._sample.__class__.__name__
            )
            raise BaseException(strMessage)
        if experimentSetup is None:
            self._experimentSetup = None
        elif experimentSetup.__class__.__name__ == "XSDataBioSaxsExperimentSetup":
            self._experimentSetup = experimentSetup
        else:
            strMessage = (
                "ERROR! XSDataInputBioSaxsNormalizev1_0 constructor argument 'experimentSetup' is not XSDataBioSaxsExperimentSetup but %s"
                % self._experimentSetup.__class__.__name__
            )
            raise BaseException(strMessage)

    # Methods and properties for the 'rawImage' attribute
    def getRawImage(self):
        return self._rawImage

    def setRawImage(self, rawImage):
        if rawImage is None:
            self._rawImage = None
        elif rawImage.__class__.__name__ == "XSDataImage":
            self._rawImage = rawImage
        else:
            strMessage = (
                "ERROR! XSDataInputBioSaxsNormalizev1_0.setRawImage argument is not XSDataImage but %s"
                % rawImage.__class__.__name__
            )
            raise BaseException(strMessage)

    def delRawImage(self):
        self._rawImage = None

    rawImage = property(getRawImage, setRawImage, delRawImage, "Property for rawImage")
    # Methods and properties for the 'logFile' attribute
    def getLogFile(self):
        return self._logFile

    def setLogFile(self, logFile):
        if logFile is None:
            self._logFile = None
        elif logFile.__class__.__name__ == "XSDataFile":
            self._logFile = logFile
        else:
            strMessage = (
                "ERROR! XSDataInputBioSaxsNormalizev1_0.setLogFile argument is not XSDataFile but %s"
                % logFile.__class__.__name__
            )
            raise BaseException(strMessage)

    def delLogFile(self):
        self._logFile = None

    logFile = property(getLogFile, setLogFile, delLogFile, "Property for logFile")
    # Methods and properties for the 'normalizedImage' attribute
    def getNormalizedImage(self):
        return self._normalizedImage

    def setNormalizedImage(self, normalizedImage):
        if normalizedImage is None:
            self._normalizedImage = None
        elif normalizedImage.__class__.__name__ == "XSDataImage":
            self._normalizedImage = normalizedImage
        else:
            strMessage = (
                "ERROR! XSDataInputBioSaxsNormalizev1_0.setNormalizedImage argument is not XSDataImage but %s"
                % normalizedImage.__class__.__name__
            )
            raise BaseException(strMessage)

    def delNormalizedImage(self):
        self._normalizedImage = None

    normalizedImage = property(
        getNormalizedImage,
        setNormalizedImage,
        delNormalizedImage,
        "Property for normalizedImage",
    )
    # Methods and properties for the 'rawImageSize' attribute
    def getRawImageSize(self):
        return self._rawImageSize

    def setRawImageSize(self, rawImageSize):
        if rawImageSize is None:
            self._rawImageSize = None
        elif rawImageSize.__class__.__name__ == "XSDataInteger":
            self._rawImageSize = rawImageSize
        else:
            strMessage = (
                "ERROR! XSDataInputBioSaxsNormalizev1_0.setRawImageSize argument is not XSDataInteger but %s"
                % rawImageSize.__class__.__name__
            )
            raise BaseException(strMessage)

    def delRawImageSize(self):
        self._rawImageSize = None

    rawImageSize = property(
        getRawImageSize, setRawImageSize, delRawImageSize, "Property for rawImageSize"
    )
    # Methods and properties for the 'sample' attribute
    def getSample(self):
        return self._sample

    def setSample(self, sample):
        if sample is None:
            self._sample = None
        elif sample.__class__.__name__ == "XSDataBioSaxsSample":
            self._sample = sample
        else:
            strMessage = (
                "ERROR! XSDataInputBioSaxsNormalizev1_0.setSample argument is not XSDataBioSaxsSample but %s"
                % sample.__class__.__name__
            )
            raise BaseException(strMessage)

    def delSample(self):
        self._sample = None

    sample = property(getSample, setSample, delSample, "Property for sample")
    # Methods and properties for the 'experimentSetup' attribute
    def getExperimentSetup(self):
        return self._experimentSetup

    def setExperimentSetup(self, experimentSetup):
        if experimentSetup is None:
            self._experimentSetup = None
        elif experimentSetup.__class__.__name__ == "XSDataBioSaxsExperimentSetup":
            self._experimentSetup = experimentSetup
        else:
            strMessage = (
                "ERROR! XSDataInputBioSaxsNormalizev1_0.setExperimentSetup argument is not XSDataBioSaxsExperimentSetup but %s"
                % experimentSetup.__class__.__name__
            )
            raise BaseException(strMessage)

    def delExperimentSetup(self):
        self._experimentSetup = None

    experimentSetup = property(
        getExperimentSetup,
        setExperimentSetup,
        delExperimentSetup,
        "Property for experimentSetup",
    )

    def export(self, outfile, level, name_="XSDataInputBioSaxsNormalizev1_0"):
        showIndent(outfile, level)
        outfile.write(unicode("<%s>\n" % name_))
        self.exportChildren(outfile, level + 1, name_)
        showIndent(outfile, level)
        outfile.write(unicode("</%s>\n" % name_))

    def exportChildren(self, outfile, level, name_="XSDataInputBioSaxsNormalizev1_0"):
        XSDataInput.exportChildren(self, outfile, level, name_)
        if self._rawImage is not None:
            self.rawImage.export(outfile, level, name_="rawImage")
        else:
            warnEmptyAttribute("rawImage", "XSDataImage")
        if self._logFile is not None:
            self.logFile.export(outfile, level, name_="logFile")
        if self._normalizedImage is not None:
            self.normalizedImage.export(outfile, level, name_="normalizedImage")
        else:
            warnEmptyAttribute("normalizedImage", "XSDataImage")
        if self._rawImageSize is not None:
            self.rawImageSize.export(outfile, level, name_="rawImageSize")
        else:
            warnEmptyAttribute("rawImageSize", "XSDataInteger")
        if self._sample is not None:
            self.sample.export(outfile, level, name_="sample")
        else:
            warnEmptyAttribute("sample", "XSDataBioSaxsSample")
        if self._experimentSetup is not None:
            self.experimentSetup.export(outfile, level, name_="experimentSetup")
        else:
            warnEmptyAttribute("experimentSetup", "XSDataBioSaxsExperimentSetup")

    def build(self, node_):
        for child_ in node_.childNodes:
            nodeName_ = child_.nodeName.split(":")[-1]
            self.buildChildren(child_, nodeName_)

    def buildChildren(self, child_, nodeName_):
        if child_.nodeType == Node.ELEMENT_NODE and nodeName_ == "rawImage":
            obj_ = XSDataImage()
            obj_.build(child_)
            self.setRawImage(obj_)
        elif child_.nodeType == Node.ELEMENT_NODE and nodeName_ == "logFile":
            obj_ = XSDataFile()
            obj_.build(child_)
            self.setLogFile(obj_)
        elif child_.nodeType == Node.ELEMENT_NODE and nodeName_ == "normalizedImage":
            obj_ = XSDataImage()
            obj_.build(child_)
            self.setNormalizedImage(obj_)
        elif child_.nodeType == Node.ELEMENT_NODE and nodeName_ == "rawImageSize":
            obj_ = XSDataInteger()
            obj_.build(child_)
            self.setRawImageSize(obj_)
        elif child_.nodeType == Node.ELEMENT_NODE and nodeName_ == "sample":
            obj_ = XSDataBioSaxsSample()
            obj_.build(child_)
            self.setSample(obj_)
        elif child_.nodeType == Node.ELEMENT_NODE and nodeName_ == "experimentSetup":
            obj_ = XSDataBioSaxsExperimentSetup()
            obj_.build(child_)
            self.setExperimentSetup(obj_)
        XSDataInput.buildChildren(self, child_, nodeName_)

    # Method for marshalling an object
    def marshal(self):
        oStreamString = StringIO()
        oStreamString.write(unicode('<?xml version="1.0" ?>\n'))
        self.export(oStreamString, 0, name_="XSDataInputBioSaxsNormalizev1_0")
        oStringXML = oStreamString.getvalue()
        oStreamString.close()
        return oStringXML

    # Only to export the entire XML tree to a file stream on disk
    def exportToFile(self, _outfileName):
        outfile = open(_outfileName, "w")
        outfile.write(unicode('<?xml version="1.0" ?>\n'))
        self.export(outfile, 0, name_="XSDataInputBioSaxsNormalizev1_0")
        outfile.close()

    # Deprecated method, replaced by exportToFile
    def outputFile(self, _outfileName):
        print(
            "WARNING: Method outputFile in class XSDataInputBioSaxsNormalizev1_0 is deprecated, please use instead exportToFile!"
        )
        self.exportToFile(_outfileName)

    # Method for making a copy in a new instance
    def copy(self):
        return XSDataInputBioSaxsNormalizev1_0.parseString(self.marshal())

    # Static method for parsing a string
    def parseString(_inString):
        doc = minidom.parseString(_inString)
        rootNode = doc.documentElement
        rootObj = XSDataInputBioSaxsNormalizev1_0()
        rootObj.build(rootNode)
        # Check that all minOccurs are obeyed by marshalling the created object
        oStreamString = StringIO()
        rootObj.export(oStreamString, 0, name_="XSDataInputBioSaxsNormalizev1_0")
        oStreamString.close()
        return rootObj

    parseString = staticmethod(parseString)
    # Static method for parsing a file
    def parseFile(_inFilePath):
        doc = minidom.parse(_inFilePath)
        rootNode = doc.documentElement
        rootObj = XSDataInputBioSaxsNormalizev1_0()
        rootObj.build(rootNode)
        return rootObj

    parseFile = staticmethod(parseFile)


# end class XSDataInputBioSaxsNormalizev1_0


class XSDataInputBioSaxsProcessOneFilev1_0(XSDataInput):
    """Plugin that runs subsequently Normalize and Azimuthal integration"""

    def __init__(
        self,
        configuration=None,
        frameId=None,
        runId=None,
        integratedCurve=None,
        integratedImage=None,
        normalizedImage=None,
        logFile=None,
        rawImageSize=None,
        experimentSetup=None,
        sample=None,
        rawImage=None,
    ):
        XSDataInput.__init__(self, configuration)
        if rawImage is None:
            self._rawImage = None
        elif rawImage.__class__.__name__ == "XSDataImage":
            self._rawImage = rawImage
        else:
            strMessage = (
                "ERROR! XSDataInputBioSaxsProcessOneFilev1_0 constructor argument 'rawImage' is not XSDataImage but %s"
                % self._rawImage.__class__.__name__
            )
            raise BaseException(strMessage)
        if sample is None:
            self._sample = None
        elif sample.__class__.__name__ == "XSDataBioSaxsSample":
            self._sample = sample
        else:
            strMessage = (
                "ERROR! XSDataInputBioSaxsProcessOneFilev1_0 constructor argument 'sample' is not XSDataBioSaxsSample but %s"
                % self._sample.__class__.__name__
            )
            raise BaseException(strMessage)
        if experimentSetup is None:
            self._experimentSetup = None
        elif experimentSetup.__class__.__name__ == "XSDataBioSaxsExperimentSetup":
            self._experimentSetup = experimentSetup
        else:
            strMessage = (
                "ERROR! XSDataInputBioSaxsProcessOneFilev1_0 constructor argument 'experimentSetup' is not XSDataBioSaxsExperimentSetup but %s"
                % self._experimentSetup.__class__.__name__
            )
            raise BaseException(strMessage)
        if rawImageSize is None:
            self._rawImageSize = None
        elif rawImageSize.__class__.__name__ == "XSDataInteger":
            self._rawImageSize = rawImageSize
        else:
            strMessage = (
                "ERROR! XSDataInputBioSaxsProcessOneFilev1_0 constructor argument 'rawImageSize' is not XSDataInteger but %s"
                % self._rawImageSize.__class__.__name__
            )
            raise BaseException(strMessage)
        if logFile is None:
            self._logFile = None
        elif logFile.__class__.__name__ == "XSDataFile":
            self._logFile = logFile
        else:
            strMessage = (
                "ERROR! XSDataInputBioSaxsProcessOneFilev1_0 constructor argument 'logFile' is not XSDataFile but %s"
                % self._logFile.__class__.__name__
            )
            raise BaseException(strMessage)
        if normalizedImage is None:
            self._normalizedImage = None
        elif normalizedImage.__class__.__name__ == "XSDataImage":
            self._normalizedImage = normalizedImage
        else:
            strMessage = (
                "ERROR! XSDataInputBioSaxsProcessOneFilev1_0 constructor argument 'normalizedImage' is not XSDataImage but %s"
                % self._normalizedImage.__class__.__name__
            )
            raise BaseException(strMessage)
        if integratedImage is None:
            self._integratedImage = None
        elif integratedImage.__class__.__name__ == "XSDataImage":
            self._integratedImage = integratedImage
        else:
            strMessage = (
                "ERROR! XSDataInputBioSaxsProcessOneFilev1_0 constructor argument 'integratedImage' is not XSDataImage but %s"
                % self._integratedImage.__class__.__name__
            )
            raise BaseException(strMessage)
        if integratedCurve is None:
            self._integratedCurve = None
        elif integratedCurve.__class__.__name__ == "XSDataFile":
            self._integratedCurve = integratedCurve
        else:
            strMessage = (
                "ERROR! XSDataInputBioSaxsProcessOneFilev1_0 constructor argument 'integratedCurve' is not XSDataFile but %s"
                % self._integratedCurve.__class__.__name__
            )
            raise BaseException(strMessage)
        if runId is None:
            self._runId = None
        elif runId.__class__.__name__ == "XSDataString":
            self._runId = runId
        else:
            strMessage = (
                "ERROR! XSDataInputBioSaxsProcessOneFilev1_0 constructor argument 'runId' is not XSDataString but %s"
                % self._runId.__class__.__name__
            )
            raise BaseException(strMessage)
        if frameId is None:
            self._frameId = None
        elif frameId.__class__.__name__ == "XSDataInteger":
            self._frameId = frameId
        else:
            strMessage = (
                "ERROR! XSDataInputBioSaxsProcessOneFilev1_0 constructor argument 'frameId' is not XSDataInteger but %s"
                % self._frameId.__class__.__name__
            )
            raise BaseException(strMessage)

    # Methods and properties for the 'rawImage' attribute
    def getRawImage(self):
        return self._rawImage

    def setRawImage(self, rawImage):
        if rawImage is None:
            self._rawImage = None
        elif rawImage.__class__.__name__ == "XSDataImage":
            self._rawImage = rawImage
        else:
            strMessage = (
                "ERROR! XSDataInputBioSaxsProcessOneFilev1_0.setRawImage argument is not XSDataImage but %s"
                % rawImage.__class__.__name__
            )
            raise BaseException(strMessage)

    def delRawImage(self):
        self._rawImage = None

    rawImage = property(getRawImage, setRawImage, delRawImage, "Property for rawImage")
    # Methods and properties for the 'sample' attribute
    def getSample(self):
        return self._sample

    def setSample(self, sample):
        if sample is None:
            self._sample = None
        elif sample.__class__.__name__ == "XSDataBioSaxsSample":
            self._sample = sample
        else:
            strMessage = (
                "ERROR! XSDataInputBioSaxsProcessOneFilev1_0.setSample argument is not XSDataBioSaxsSample but %s"
                % sample.__class__.__name__
            )
            raise BaseException(strMessage)

    def delSample(self):
        self._sample = None

    sample = property(getSample, setSample, delSample, "Property for sample")
    # Methods and properties for the 'experimentSetup' attribute
    def getExperimentSetup(self):
        return self._experimentSetup

    def setExperimentSetup(self, experimentSetup):
        if experimentSetup is None:
            self._experimentSetup = None
        elif experimentSetup.__class__.__name__ == "XSDataBioSaxsExperimentSetup":
            self._experimentSetup = experimentSetup
        else:
            strMessage = (
                "ERROR! XSDataInputBioSaxsProcessOneFilev1_0.setExperimentSetup argument is not XSDataBioSaxsExperimentSetup but %s"
                % experimentSetup.__class__.__name__
            )
            raise BaseException(strMessage)

    def delExperimentSetup(self):
        self._experimentSetup = None

    experimentSetup = property(
        getExperimentSetup,
        setExperimentSetup,
        delExperimentSetup,
        "Property for experimentSetup",
    )
    # Methods and properties for the 'rawImageSize' attribute
    def getRawImageSize(self):
        return self._rawImageSize

    def setRawImageSize(self, rawImageSize):
        if rawImageSize is None:
            self._rawImageSize = None
        elif rawImageSize.__class__.__name__ == "XSDataInteger":
            self._rawImageSize = rawImageSize
        else:
            strMessage = (
                "ERROR! XSDataInputBioSaxsProcessOneFilev1_0.setRawImageSize argument is not XSDataInteger but %s"
                % rawImageSize.__class__.__name__
            )
            raise BaseException(strMessage)

    def delRawImageSize(self):
        self._rawImageSize = None

    rawImageSize = property(
        getRawImageSize, setRawImageSize, delRawImageSize, "Property for rawImageSize"
    )
    # Methods and properties for the 'logFile' attribute
    def getLogFile(self):
        return self._logFile

    def setLogFile(self, logFile):
        if logFile is None:
            self._logFile = None
        elif logFile.__class__.__name__ == "XSDataFile":
            self._logFile = logFile
        else:
            strMessage = (
                "ERROR! XSDataInputBioSaxsProcessOneFilev1_0.setLogFile argument is not XSDataFile but %s"
                % logFile.__class__.__name__
            )
            raise BaseException(strMessage)

    def delLogFile(self):
        self._logFile = None

    logFile = property(getLogFile, setLogFile, delLogFile, "Property for logFile")
    # Methods and properties for the 'normalizedImage' attribute
    def getNormalizedImage(self):
        return self._normalizedImage

    def setNormalizedImage(self, normalizedImage):
        if normalizedImage is None:
            self._normalizedImage = None
        elif normalizedImage.__class__.__name__ == "XSDataImage":
            self._normalizedImage = normalizedImage
        else:
            strMessage = (
                "ERROR! XSDataInputBioSaxsProcessOneFilev1_0.setNormalizedImage argument is not XSDataImage but %s"
                % normalizedImage.__class__.__name__
            )
            raise BaseException(strMessage)

    def delNormalizedImage(self):
        self._normalizedImage = None

    normalizedImage = property(
        getNormalizedImage,
        setNormalizedImage,
        delNormalizedImage,
        "Property for normalizedImage",
    )
    # Methods and properties for the 'integratedImage' attribute
    def getIntegratedImage(self):
        return self._integratedImage

    def setIntegratedImage(self, integratedImage):
        if integratedImage is None:
            self._integratedImage = None
        elif integratedImage.__class__.__name__ == "XSDataImage":
            self._integratedImage = integratedImage
        else:
            strMessage = (
                "ERROR! XSDataInputBioSaxsProcessOneFilev1_0.setIntegratedImage argument is not XSDataImage but %s"
                % integratedImage.__class__.__name__
            )
            raise BaseException(strMessage)

    def delIntegratedImage(self):
        self._integratedImage = None

    integratedImage = property(
        getIntegratedImage,
        setIntegratedImage,
        delIntegratedImage,
        "Property for integratedImage",
    )
    # Methods and properties for the 'integratedCurve' attribute
    def getIntegratedCurve(self):
        return self._integratedCurve

    def setIntegratedCurve(self, integratedCurve):
        if integratedCurve is None:
            self._integratedCurve = None
        elif integratedCurve.__class__.__name__ == "XSDataFile":
            self._integratedCurve = integratedCurve
        else:
            strMessage = (
                "ERROR! XSDataInputBioSaxsProcessOneFilev1_0.setIntegratedCurve argument is not XSDataFile but %s"
                % integratedCurve.__class__.__name__
            )
            raise BaseException(strMessage)

    def delIntegratedCurve(self):
        self._integratedCurve = None

    integratedCurve = property(
        getIntegratedCurve,
        setIntegratedCurve,
        delIntegratedCurve,
        "Property for integratedCurve",
    )
    # Methods and properties for the 'runId' attribute
    def getRunId(self):
        return self._runId

    def setRunId(self, runId):
        if runId is None:
            self._runId = None
        elif runId.__class__.__name__ == "XSDataString":
            self._runId = runId
        else:
            strMessage = (
                "ERROR! XSDataInputBioSaxsProcessOneFilev1_0.setRunId argument is not XSDataString but %s"
                % runId.__class__.__name__
            )
            raise BaseException(strMessage)

    def delRunId(self):
        self._runId = None

    runId = property(getRunId, setRunId, delRunId, "Property for runId")
    # Methods and properties for the 'frameId' attribute
    def getFrameId(self):
        return self._frameId

    def setFrameId(self, frameId):
        if frameId is None:
            self._frameId = None
        elif frameId.__class__.__name__ == "XSDataInteger":
            self._frameId = frameId
        else:
            strMessage = (
                "ERROR! XSDataInputBioSaxsProcessOneFilev1_0.setFrameId argument is not XSDataInteger but %s"
                % frameId.__class__.__name__
            )
            raise BaseException(strMessage)

    def delFrameId(self):
        self._frameId = None

    frameId = property(getFrameId, setFrameId, delFrameId, "Property for frameId")

    def export(self, outfile, level, name_="XSDataInputBioSaxsProcessOneFilev1_0"):
        showIndent(outfile, level)
        outfile.write(unicode("<%s>\n" % name_))
        self.exportChildren(outfile, level + 1, name_)
        showIndent(outfile, level)
        outfile.write(unicode("</%s>\n" % name_))

    def exportChildren(
        self, outfile, level, name_="XSDataInputBioSaxsProcessOneFilev1_0"
    ):
        XSDataInput.exportChildren(self, outfile, level, name_)
        if self._rawImage is not None:
            self.rawImage.export(outfile, level, name_="rawImage")
        else:
            warnEmptyAttribute("rawImage", "XSDataImage")
        if self._sample is not None:
            self.sample.export(outfile, level, name_="sample")
        else:
            warnEmptyAttribute("sample", "XSDataBioSaxsSample")
        if self._experimentSetup is not None:
            self.experimentSetup.export(outfile, level, name_="experimentSetup")
        else:
            warnEmptyAttribute("experimentSetup", "XSDataBioSaxsExperimentSetup")
        if self._rawImageSize is not None:
            self.rawImageSize.export(outfile, level, name_="rawImageSize")
        if self._logFile is not None:
            self.logFile.export(outfile, level, name_="logFile")
        if self._normalizedImage is not None:
            self.normalizedImage.export(outfile, level, name_="normalizedImage")
        if self._integratedImage is not None:
            self.integratedImage.export(outfile, level, name_="integratedImage")
        if self._integratedCurve is not None:
            self.integratedCurve.export(outfile, level, name_="integratedCurve")
        if self._runId is not None:
            self.runId.export(outfile, level, name_="runId")
        if self._frameId is not None:
            self.frameId.export(outfile, level, name_="frameId")

    def build(self, node_):
        for child_ in node_.childNodes:
            nodeName_ = child_.nodeName.split(":")[-1]
            self.buildChildren(child_, nodeName_)

    def buildChildren(self, child_, nodeName_):
        if child_.nodeType == Node.ELEMENT_NODE and nodeName_ == "rawImage":
            obj_ = XSDataImage()
            obj_.build(child_)
            self.setRawImage(obj_)
        elif child_.nodeType == Node.ELEMENT_NODE and nodeName_ == "sample":
            obj_ = XSDataBioSaxsSample()
            obj_.build(child_)
            self.setSample(obj_)
        elif child_.nodeType == Node.ELEMENT_NODE and nodeName_ == "experimentSetup":
            obj_ = XSDataBioSaxsExperimentSetup()
            obj_.build(child_)
            self.setExperimentSetup(obj_)
        elif child_.nodeType == Node.ELEMENT_NODE and nodeName_ == "rawImageSize":
            obj_ = XSDataInteger()
            obj_.build(child_)
            self.setRawImageSize(obj_)
        elif child_.nodeType == Node.ELEMENT_NODE and nodeName_ == "logFile":
            obj_ = XSDataFile()
            obj_.build(child_)
            self.setLogFile(obj_)
        elif child_.nodeType == Node.ELEMENT_NODE and nodeName_ == "normalizedImage":
            obj_ = XSDataImage()
            obj_.build(child_)
            self.setNormalizedImage(obj_)
        elif child_.nodeType == Node.ELEMENT_NODE and nodeName_ == "integratedImage":
            obj_ = XSDataImage()
            obj_.build(child_)
            self.setIntegratedImage(obj_)
        elif child_.nodeType == Node.ELEMENT_NODE and nodeName_ == "integratedCurve":
            obj_ = XSDataFile()
            obj_.build(child_)
            self.setIntegratedCurve(obj_)
        elif child_.nodeType == Node.ELEMENT_NODE and nodeName_ == "runId":
            obj_ = XSDataString()
            obj_.build(child_)
            self.setRunId(obj_)
        elif child_.nodeType == Node.ELEMENT_NODE and nodeName_ == "frameId":
            obj_ = XSDataInteger()
            obj_.build(child_)
            self.setFrameId(obj_)
        XSDataInput.buildChildren(self, child_, nodeName_)

    # Method for marshalling an object
    def marshal(self):
        oStreamString = StringIO()
        oStreamString.write(unicode('<?xml version="1.0" ?>\n'))
        self.export(oStreamString, 0, name_="XSDataInputBioSaxsProcessOneFilev1_0")
        oStringXML = oStreamString.getvalue()
        oStreamString.close()
        return oStringXML

    # Only to export the entire XML tree to a file stream on disk
    def exportToFile(self, _outfileName):
        outfile = open(_outfileName, "w")
        outfile.write(unicode('<?xml version="1.0" ?>\n'))
        self.export(outfile, 0, name_="XSDataInputBioSaxsProcessOneFilev1_0")
        outfile.close()

    # Deprecated method, replaced by exportToFile
    def outputFile(self, _outfileName):
        print(
            "WARNING: Method outputFile in class XSDataInputBioSaxsProcessOneFilev1_0 is deprecated, please use instead exportToFile!"
        )
        self.exportToFile(_outfileName)

    # Method for making a copy in a new instance
    def copy(self):
        return XSDataInputBioSaxsProcessOneFilev1_0.parseString(self.marshal())

    # Static method for parsing a string
    def parseString(_inString):
        doc = minidom.parseString(_inString)
        rootNode = doc.documentElement
        rootObj = XSDataInputBioSaxsProcessOneFilev1_0()
        rootObj.build(rootNode)
        # Check that all minOccurs are obeyed by marshalling the created object
        oStreamString = StringIO()
        rootObj.export(oStreamString, 0, name_="XSDataInputBioSaxsProcessOneFilev1_0")
        oStreamString.close()
        return rootObj

    parseString = staticmethod(parseString)
    # Static method for parsing a file
    def parseFile(_inFilePath):
        doc = minidom.parse(_inFilePath)
        rootNode = doc.documentElement
        rootObj = XSDataInputBioSaxsProcessOneFilev1_0()
        rootObj.build(rootNode)
        return rootObj

    parseFile = staticmethod(parseFile)


# end class XSDataInputBioSaxsProcessOneFilev1_0


class XSDataInputBioSaxsReduceFileSeriev1_0(XSDataInput):
    """Run ProcessOneFile on each file of a time time serie  """

    def __init__(
        self,
        configuration=None,
        rawImageSize=None,
        relativeFidelity=None,
        absoluteFidelity=None,
        forceReprocess=None,
        directoryMisc=None,
        directory2D=None,
        directory1D=None,
        experimentSetup=None,
        sample=None,
        fileSerie=None,
    ):
        XSDataInput.__init__(self, configuration)
        if fileSerie is None:
            self._fileSerie = None
        elif fileSerie.__class__.__name__ == "XSDataFileSeries":
            self._fileSerie = fileSerie
        else:
            strMessage = (
                "ERROR! XSDataInputBioSaxsReduceFileSeriev1_0 constructor argument 'fileSerie' is not XSDataFileSeries but %s"
                % self._fileSerie.__class__.__name__
            )
            raise BaseException(strMessage)
        if sample is None:
            self._sample = None
        elif sample.__class__.__name__ == "XSDataBioSaxsSample":
            self._sample = sample
        else:
            strMessage = (
                "ERROR! XSDataInputBioSaxsReduceFileSeriev1_0 constructor argument 'sample' is not XSDataBioSaxsSample but %s"
                % self._sample.__class__.__name__
            )
            raise BaseException(strMessage)
        if experimentSetup is None:
            self._experimentSetup = None
        elif experimentSetup.__class__.__name__ == "XSDataBioSaxsExperimentSetup":
            self._experimentSetup = experimentSetup
        else:
            strMessage = (
                "ERROR! XSDataInputBioSaxsReduceFileSeriev1_0 constructor argument 'experimentSetup' is not XSDataBioSaxsExperimentSetup but %s"
                % self._experimentSetup.__class__.__name__
            )
            raise BaseException(strMessage)
        if directory1D is None:
            self._directory1D = None
        elif directory1D.__class__.__name__ == "XSDataFile":
            self._directory1D = directory1D
        else:
            strMessage = (
                "ERROR! XSDataInputBioSaxsReduceFileSeriev1_0 constructor argument 'directory1D' is not XSDataFile but %s"
                % self._directory1D.__class__.__name__
            )
            raise BaseException(strMessage)
        if directory2D is None:
            self._directory2D = None
        elif directory2D.__class__.__name__ == "XSDataFile":
            self._directory2D = directory2D
        else:
            strMessage = (
                "ERROR! XSDataInputBioSaxsReduceFileSeriev1_0 constructor argument 'directory2D' is not XSDataFile but %s"
                % self._directory2D.__class__.__name__
            )
            raise BaseException(strMessage)
        if directoryMisc is None:
            self._directoryMisc = None
        elif directoryMisc.__class__.__name__ == "XSDataFile":
            self._directoryMisc = directoryMisc
        else:
            strMessage = (
                "ERROR! XSDataInputBioSaxsReduceFileSeriev1_0 constructor argument 'directoryMisc' is not XSDataFile but %s"
                % self._directoryMisc.__class__.__name__
            )
            raise BaseException(strMessage)
        if forceReprocess is None:
            self._forceReprocess = None
        elif forceReprocess.__class__.__name__ == "XSDataBoolean":
            self._forceReprocess = forceReprocess
        else:
            strMessage = (
                "ERROR! XSDataInputBioSaxsReduceFileSeriev1_0 constructor argument 'forceReprocess' is not XSDataBoolean but %s"
                % self._forceReprocess.__class__.__name__
            )
            raise BaseException(strMessage)
        if absoluteFidelity is None:
            self._absoluteFidelity = None
        elif absoluteFidelity.__class__.__name__ == "XSDataDouble":
            self._absoluteFidelity = absoluteFidelity
        else:
            strMessage = (
                "ERROR! XSDataInputBioSaxsReduceFileSeriev1_0 constructor argument 'absoluteFidelity' is not XSDataDouble but %s"
                % self._absoluteFidelity.__class__.__name__
            )
            raise BaseException(strMessage)
        if relativeFidelity is None:
            self._relativeFidelity = None
        elif relativeFidelity.__class__.__name__ == "XSDataDouble":
            self._relativeFidelity = relativeFidelity
        else:
            strMessage = (
                "ERROR! XSDataInputBioSaxsReduceFileSeriev1_0 constructor argument 'relativeFidelity' is not XSDataDouble but %s"
                % self._relativeFidelity.__class__.__name__
            )
            raise BaseException(strMessage)
        if rawImageSize is None:
            self._rawImageSize = None
        elif rawImageSize.__class__.__name__ == "XSDataInteger":
            self._rawImageSize = rawImageSize
        else:
            strMessage = (
                "ERROR! XSDataInputBioSaxsReduceFileSeriev1_0 constructor argument 'rawImageSize' is not XSDataInteger but %s"
                % self._rawImageSize.__class__.__name__
            )
            raise BaseException(strMessage)

    # Methods and properties for the 'fileSerie' attribute
    def getFileSerie(self):
        return self._fileSerie

    def setFileSerie(self, fileSerie):
        if fileSerie is None:
            self._fileSerie = None
        elif fileSerie.__class__.__name__ == "XSDataFileSeries":
            self._fileSerie = fileSerie
        else:
            strMessage = (
                "ERROR! XSDataInputBioSaxsReduceFileSeriev1_0.setFileSerie argument is not XSDataFileSeries but %s"
                % fileSerie.__class__.__name__
            )
            raise BaseException(strMessage)

    def delFileSerie(self):
        self._fileSerie = None

    fileSerie = property(
        getFileSerie, setFileSerie, delFileSerie, "Property for fileSerie"
    )
    # Methods and properties for the 'sample' attribute
    def getSample(self):
        return self._sample

    def setSample(self, sample):
        if sample is None:
            self._sample = None
        elif sample.__class__.__name__ == "XSDataBioSaxsSample":
            self._sample = sample
        else:
            strMessage = (
                "ERROR! XSDataInputBioSaxsReduceFileSeriev1_0.setSample argument is not XSDataBioSaxsSample but %s"
                % sample.__class__.__name__
            )
            raise BaseException(strMessage)

    def delSample(self):
        self._sample = None

    sample = property(getSample, setSample, delSample, "Property for sample")
    # Methods and properties for the 'experimentSetup' attribute
    def getExperimentSetup(self):
        return self._experimentSetup

    def setExperimentSetup(self, experimentSetup):
        if experimentSetup is None:
            self._experimentSetup = None
        elif experimentSetup.__class__.__name__ == "XSDataBioSaxsExperimentSetup":
            self._experimentSetup = experimentSetup
        else:
            strMessage = (
                "ERROR! XSDataInputBioSaxsReduceFileSeriev1_0.setExperimentSetup argument is not XSDataBioSaxsExperimentSetup but %s"
                % experimentSetup.__class__.__name__
            )
            raise BaseException(strMessage)

    def delExperimentSetup(self):
        self._experimentSetup = None

    experimentSetup = property(
        getExperimentSetup,
        setExperimentSetup,
        delExperimentSetup,
        "Property for experimentSetup",
    )
    # Methods and properties for the 'directory1D' attribute
    def getDirectory1D(self):
        return self._directory1D

    def setDirectory1D(self, directory1D):
        if directory1D is None:
            self._directory1D = None
        elif directory1D.__class__.__name__ == "XSDataFile":
            self._directory1D = directory1D
        else:
            strMessage = (
                "ERROR! XSDataInputBioSaxsReduceFileSeriev1_0.setDirectory1D argument is not XSDataFile but %s"
                % directory1D.__class__.__name__
            )
            raise BaseException(strMessage)

    def delDirectory1D(self):
        self._directory1D = None

    directory1D = property(
        getDirectory1D, setDirectory1D, delDirectory1D, "Property for directory1D"
    )
    # Methods and properties for the 'directory2D' attribute
    def getDirectory2D(self):
        return self._directory2D

    def setDirectory2D(self, directory2D):
        if directory2D is None:
            self._directory2D = None
        elif directory2D.__class__.__name__ == "XSDataFile":
            self._directory2D = directory2D
        else:
            strMessage = (
                "ERROR! XSDataInputBioSaxsReduceFileSeriev1_0.setDirectory2D argument is not XSDataFile but %s"
                % directory2D.__class__.__name__
            )
            raise BaseException(strMessage)

    def delDirectory2D(self):
        self._directory2D = None

    directory2D = property(
        getDirectory2D, setDirectory2D, delDirectory2D, "Property for directory2D"
    )
    # Methods and properties for the 'directoryMisc' attribute
    def getDirectoryMisc(self):
        return self._directoryMisc

    def setDirectoryMisc(self, directoryMisc):
        if directoryMisc is None:
            self._directoryMisc = None
        elif directoryMisc.__class__.__name__ == "XSDataFile":
            self._directoryMisc = directoryMisc
        else:
            strMessage = (
                "ERROR! XSDataInputBioSaxsReduceFileSeriev1_0.setDirectoryMisc argument is not XSDataFile but %s"
                % directoryMisc.__class__.__name__
            )
            raise BaseException(strMessage)

    def delDirectoryMisc(self):
        self._directoryMisc = None

    directoryMisc = property(
        getDirectoryMisc,
        setDirectoryMisc,
        delDirectoryMisc,
        "Property for directoryMisc",
    )
    # Methods and properties for the 'forceReprocess' attribute
    def getForceReprocess(self):
        return self._forceReprocess

    def setForceReprocess(self, forceReprocess):
        if forceReprocess is None:
            self._forceReprocess = None
        elif forceReprocess.__class__.__name__ == "XSDataBoolean":
            self._forceReprocess = forceReprocess
        else:
            strMessage = (
                "ERROR! XSDataInputBioSaxsReduceFileSeriev1_0.setForceReprocess argument is not XSDataBoolean but %s"
                % forceReprocess.__class__.__name__
            )
            raise BaseException(strMessage)

    def delForceReprocess(self):
        self._forceReprocess = None

    forceReprocess = property(
        getForceReprocess,
        setForceReprocess,
        delForceReprocess,
        "Property for forceReprocess",
    )
    # Methods and properties for the 'absoluteFidelity' attribute
    def getAbsoluteFidelity(self):
        return self._absoluteFidelity

    def setAbsoluteFidelity(self, absoluteFidelity):
        if absoluteFidelity is None:
            self._absoluteFidelity = None
        elif absoluteFidelity.__class__.__name__ == "XSDataDouble":
            self._absoluteFidelity = absoluteFidelity
        else:
            strMessage = (
                "ERROR! XSDataInputBioSaxsReduceFileSeriev1_0.setAbsoluteFidelity argument is not XSDataDouble but %s"
                % absoluteFidelity.__class__.__name__
            )
            raise BaseException(strMessage)

    def delAbsoluteFidelity(self):
        self._absoluteFidelity = None

    absoluteFidelity = property(
        getAbsoluteFidelity,
        setAbsoluteFidelity,
        delAbsoluteFidelity,
        "Property for absoluteFidelity",
    )
    # Methods and properties for the 'relativeFidelity' attribute
    def getRelativeFidelity(self):
        return self._relativeFidelity

    def setRelativeFidelity(self, relativeFidelity):
        if relativeFidelity is None:
            self._relativeFidelity = None
        elif relativeFidelity.__class__.__name__ == "XSDataDouble":
            self._relativeFidelity = relativeFidelity
        else:
            strMessage = (
                "ERROR! XSDataInputBioSaxsReduceFileSeriev1_0.setRelativeFidelity argument is not XSDataDouble but %s"
                % relativeFidelity.__class__.__name__
            )
            raise BaseException(strMessage)

    def delRelativeFidelity(self):
        self._relativeFidelity = None

    relativeFidelity = property(
        getRelativeFidelity,
        setRelativeFidelity,
        delRelativeFidelity,
        "Property for relativeFidelity",
    )
    # Methods and properties for the 'rawImageSize' attribute
    def getRawImageSize(self):
        return self._rawImageSize

    def setRawImageSize(self, rawImageSize):
        if rawImageSize is None:
            self._rawImageSize = None
        elif rawImageSize.__class__.__name__ == "XSDataInteger":
            self._rawImageSize = rawImageSize
        else:
            strMessage = (
                "ERROR! XSDataInputBioSaxsReduceFileSeriev1_0.setRawImageSize argument is not XSDataInteger but %s"
                % rawImageSize.__class__.__name__
            )
            raise BaseException(strMessage)

    def delRawImageSize(self):
        self._rawImageSize = None

    rawImageSize = property(
        getRawImageSize, setRawImageSize, delRawImageSize, "Property for rawImageSize"
    )

    def export(self, outfile, level, name_="XSDataInputBioSaxsReduceFileSeriev1_0"):
        showIndent(outfile, level)
        outfile.write(unicode("<%s>\n" % name_))
        self.exportChildren(outfile, level + 1, name_)
        showIndent(outfile, level)
        outfile.write(unicode("</%s>\n" % name_))

    def exportChildren(
        self, outfile, level, name_="XSDataInputBioSaxsReduceFileSeriev1_0"
    ):
        XSDataInput.exportChildren(self, outfile, level, name_)
        if self._fileSerie is not None:
            self.fileSerie.export(outfile, level, name_="fileSerie")
        else:
            warnEmptyAttribute("fileSerie", "XSDataFileSeries")
        if self._sample is not None:
            self.sample.export(outfile, level, name_="sample")
        else:
            warnEmptyAttribute("sample", "XSDataBioSaxsSample")
        if self._experimentSetup is not None:
            self.experimentSetup.export(outfile, level, name_="experimentSetup")
        else:
            warnEmptyAttribute("experimentSetup", "XSDataBioSaxsExperimentSetup")
        if self._directory1D is not None:
            self.directory1D.export(outfile, level, name_="directory1D")
        else:
            warnEmptyAttribute("directory1D", "XSDataFile")
        if self._directory2D is not None:
            self.directory2D.export(outfile, level, name_="directory2D")
        else:
            warnEmptyAttribute("directory2D", "XSDataFile")
        if self._directoryMisc is not None:
            self.directoryMisc.export(outfile, level, name_="directoryMisc")
        else:
            warnEmptyAttribute("directoryMisc", "XSDataFile")
        if self._forceReprocess is not None:
            self.forceReprocess.export(outfile, level, name_="forceReprocess")
        if self._absoluteFidelity is not None:
            self.absoluteFidelity.export(outfile, level, name_="absoluteFidelity")
        if self._relativeFidelity is not None:
            self.relativeFidelity.export(outfile, level, name_="relativeFidelity")
        if self._rawImageSize is not None:
            self.rawImageSize.export(outfile, level, name_="rawImageSize")

    def build(self, node_):
        for child_ in node_.childNodes:
            nodeName_ = child_.nodeName.split(":")[-1]
            self.buildChildren(child_, nodeName_)

    def buildChildren(self, child_, nodeName_):
        if child_.nodeType == Node.ELEMENT_NODE and nodeName_ == "fileSerie":
            obj_ = XSDataFileSeries()
            obj_.build(child_)
            self.setFileSerie(obj_)
        elif child_.nodeType == Node.ELEMENT_NODE and nodeName_ == "sample":
            obj_ = XSDataBioSaxsSample()
            obj_.build(child_)
            self.setSample(obj_)
        elif child_.nodeType == Node.ELEMENT_NODE and nodeName_ == "experimentSetup":
            obj_ = XSDataBioSaxsExperimentSetup()
            obj_.build(child_)
            self.setExperimentSetup(obj_)
        elif child_.nodeType == Node.ELEMENT_NODE and nodeName_ == "directory1D":
            obj_ = XSDataFile()
            obj_.build(child_)
            self.setDirectory1D(obj_)
        elif child_.nodeType == Node.ELEMENT_NODE and nodeName_ == "directory2D":
            obj_ = XSDataFile()
            obj_.build(child_)
            self.setDirectory2D(obj_)
        elif child_.nodeType == Node.ELEMENT_NODE and nodeName_ == "directoryMisc":
            obj_ = XSDataFile()
            obj_.build(child_)
            self.setDirectoryMisc(obj_)
        elif child_.nodeType == Node.ELEMENT_NODE and nodeName_ == "forceReprocess":
            obj_ = XSDataBoolean()
            obj_.build(child_)
            self.setForceReprocess(obj_)
        elif child_.nodeType == Node.ELEMENT_NODE and nodeName_ == "absoluteFidelity":
            obj_ = XSDataDouble()
            obj_.build(child_)
            self.setAbsoluteFidelity(obj_)
        elif child_.nodeType == Node.ELEMENT_NODE and nodeName_ == "relativeFidelity":
            obj_ = XSDataDouble()
            obj_.build(child_)
            self.setRelativeFidelity(obj_)
        elif child_.nodeType == Node.ELEMENT_NODE and nodeName_ == "rawImageSize":
            obj_ = XSDataInteger()
            obj_.build(child_)
            self.setRawImageSize(obj_)
        XSDataInput.buildChildren(self, child_, nodeName_)

    # Method for marshalling an object
    def marshal(self):
        oStreamString = StringIO()
        oStreamString.write(unicode('<?xml version="1.0" ?>\n'))
        self.export(oStreamString, 0, name_="XSDataInputBioSaxsReduceFileSeriev1_0")
        oStringXML = oStreamString.getvalue()
        oStreamString.close()
        return oStringXML

    # Only to export the entire XML tree to a file stream on disk
    def exportToFile(self, _outfileName):
        outfile = open(_outfileName, "w")
        outfile.write(unicode('<?xml version="1.0" ?>\n'))
        self.export(outfile, 0, name_="XSDataInputBioSaxsReduceFileSeriev1_0")
        outfile.close()

    # Deprecated method, replaced by exportToFile
    def outputFile(self, _outfileName):
        print(
            "WARNING: Method outputFile in class XSDataInputBioSaxsReduceFileSeriev1_0 is deprecated, please use instead exportToFile!"
        )
        self.exportToFile(_outfileName)

    # Method for making a copy in a new instance
    def copy(self):
        return XSDataInputBioSaxsReduceFileSeriev1_0.parseString(self.marshal())

    # Static method for parsing a string
    def parseString(_inString):
        doc = minidom.parseString(_inString)
        rootNode = doc.documentElement
        rootObj = XSDataInputBioSaxsReduceFileSeriev1_0()
        rootObj.build(rootNode)
        # Check that all minOccurs are obeyed by marshalling the created object
        oStreamString = StringIO()
        rootObj.export(oStreamString, 0, name_="XSDataInputBioSaxsReduceFileSeriev1_0")
        oStreamString.close()
        return rootObj

    parseString = staticmethod(parseString)
    # Static method for parsing a file
    def parseFile(_inFilePath):
        doc = minidom.parse(_inFilePath)
        rootNode = doc.documentElement
        rootObj = XSDataInputBioSaxsReduceFileSeriev1_0()
        rootObj.build(rootNode)
        return rootObj

    parseFile = staticmethod(parseFile)


# end class XSDataInputBioSaxsReduceFileSeriev1_0


class XSDataInputBioSaxsSample(XSDataInput):
    """temporary class for multiple inhertitance emulation"""

    def __init__(
        self, configuration=None, code=None, comments=None, concentration=None
    ):
        XSDataInput.__init__(self, configuration)
        if concentration is None:
            self._concentration = None
        elif concentration.__class__.__name__ == "XSDataDouble":
            self._concentration = concentration
        else:
            strMessage = (
                "ERROR! XSDataInputBioSaxsSample constructor argument 'concentration' is not XSDataDouble but %s"
                % self._concentration.__class__.__name__
            )
            raise BaseException(strMessage)
        if comments is None:
            self._comments = None
        elif comments.__class__.__name__ == "XSDataString":
            self._comments = comments
        else:
            strMessage = (
                "ERROR! XSDataInputBioSaxsSample constructor argument 'comments' is not XSDataString but %s"
                % self._comments.__class__.__name__
            )
            raise BaseException(strMessage)
        if code is None:
            self._code = None
        elif code.__class__.__name__ == "XSDataString":
            self._code = code
        else:
            strMessage = (
                "ERROR! XSDataInputBioSaxsSample constructor argument 'code' is not XSDataString but %s"
                % self._code.__class__.__name__
            )
            raise BaseException(strMessage)

    # Methods and properties for the 'concentration' attribute
    def getConcentration(self):
        return self._concentration

    def setConcentration(self, concentration):
        if concentration is None:
            self._concentration = None
        elif concentration.__class__.__name__ == "XSDataDouble":
            self._concentration = concentration
        else:
            strMessage = (
                "ERROR! XSDataInputBioSaxsSample.setConcentration argument is not XSDataDouble but %s"
                % concentration.__class__.__name__
            )
            raise BaseException(strMessage)

    def delConcentration(self):
        self._concentration = None

    concentration = property(
        getConcentration,
        setConcentration,
        delConcentration,
        "Property for concentration",
    )
    # Methods and properties for the 'comments' attribute
    def getComments(self):
        return self._comments

    def setComments(self, comments):
        if comments is None:
            self._comments = None
        elif comments.__class__.__name__ == "XSDataString":
            self._comments = comments
        else:
            strMessage = (
                "ERROR! XSDataInputBioSaxsSample.setComments argument is not XSDataString but %s"
                % comments.__class__.__name__
            )
            raise BaseException(strMessage)

    def delComments(self):
        self._comments = None

    comments = property(getComments, setComments, delComments, "Property for comments")
    # Methods and properties for the 'code' attribute
    def getCode(self):
        return self._code

    def setCode(self, code):
        if code is None:
            self._code = None
        elif code.__class__.__name__ == "XSDataString":
            self._code = code
        else:
            strMessage = (
                "ERROR! XSDataInputBioSaxsSample.setCode argument is not XSDataString but %s"
                % code.__class__.__name__
            )
            raise BaseException(strMessage)

    def delCode(self):
        self._code = None

    code = property(getCode, setCode, delCode, "Property for code")

    def export(self, outfile, level, name_="XSDataInputBioSaxsSample"):
        showIndent(outfile, level)
        outfile.write(unicode("<%s>\n" % name_))
        self.exportChildren(outfile, level + 1, name_)
        showIndent(outfile, level)
        outfile.write(unicode("</%s>\n" % name_))

    def exportChildren(self, outfile, level, name_="XSDataInputBioSaxsSample"):
        XSDataInput.exportChildren(self, outfile, level, name_)
        if self._concentration is not None:
            self.concentration.export(outfile, level, name_="concentration")
        if self._comments is not None:
            self.comments.export(outfile, level, name_="comments")
        if self._code is not None:
            self.code.export(outfile, level, name_="code")

    def build(self, node_):
        for child_ in node_.childNodes:
            nodeName_ = child_.nodeName.split(":")[-1]
            self.buildChildren(child_, nodeName_)

    def buildChildren(self, child_, nodeName_):
        if child_.nodeType == Node.ELEMENT_NODE and nodeName_ == "concentration":
            obj_ = XSDataDouble()
            obj_.build(child_)
            self.setConcentration(obj_)
        elif child_.nodeType == Node.ELEMENT_NODE and nodeName_ == "comments":
            obj_ = XSDataString()
            obj_.build(child_)
            self.setComments(obj_)
        elif child_.nodeType == Node.ELEMENT_NODE and nodeName_ == "code":
            obj_ = XSDataString()
            obj_.build(child_)
            self.setCode(obj_)
        XSDataInput.buildChildren(self, child_, nodeName_)

    # Method for marshalling an object
    def marshal(self):
        oStreamString = StringIO()
        oStreamString.write(unicode('<?xml version="1.0" ?>\n'))
        self.export(oStreamString, 0, name_="XSDataInputBioSaxsSample")
        oStringXML = oStreamString.getvalue()
        oStreamString.close()
        return oStringXML

    # Only to export the entire XML tree to a file stream on disk
    def exportToFile(self, _outfileName):
        outfile = open(_outfileName, "w")
        outfile.write(unicode('<?xml version="1.0" ?>\n'))
        self.export(outfile, 0, name_="XSDataInputBioSaxsSample")
        outfile.close()

    # Deprecated method, replaced by exportToFile
    def outputFile(self, _outfileName):
        print(
            "WARNING: Method outputFile in class XSDataInputBioSaxsSample is deprecated, please use instead exportToFile!"
        )
        self.exportToFile(_outfileName)

    # Method for making a copy in a new instance
    def copy(self):
        return XSDataInputBioSaxsSample.parseString(self.marshal())

    # Static method for parsing a string
    def parseString(_inString):
        doc = minidom.parseString(_inString)
        rootNode = doc.documentElement
        rootObj = XSDataInputBioSaxsSample()
        rootObj.build(rootNode)
        # Check that all minOccurs are obeyed by marshalling the created object
        oStreamString = StringIO()
        rootObj.export(oStreamString, 0, name_="XSDataInputBioSaxsSample")
        oStreamString.close()
        return rootObj

    parseString = staticmethod(parseString)
    # Static method for parsing a file
    def parseFile(_inFilePath):
        doc = minidom.parse(_inFilePath)
        rootNode = doc.documentElement
        rootObj = XSDataInputBioSaxsSample()
        rootObj.build(rootNode)
        return rootObj

    parseFile = staticmethod(parseFile)


# end class XSDataInputBioSaxsSample


class XSDataInputBioSaxsSmartMergev1_0(XSDataInput):
    def __init__(
        self,
        configuration=None,
        bufferCurves=None,
        runId=None,
        subtractedCurve=None,
        mergedCurve=None,
        sample=None,
        relativeFidelity=None,
        absoluteFidelity=None,
        inputCurves=None,
    ):
        XSDataInput.__init__(self, configuration)
        if inputCurves is None:
            self._inputCurves = []
        elif inputCurves.__class__.__name__ == "list":
            self._inputCurves = inputCurves
        else:
            strMessage = (
                "ERROR! XSDataInputBioSaxsSmartMergev1_0 constructor argument 'inputCurves' is not list but %s"
                % self._inputCurves.__class__.__name__
            )
            raise BaseException(strMessage)
        if absoluteFidelity is None:
            self._absoluteFidelity = None
        elif absoluteFidelity.__class__.__name__ == "XSDataDouble":
            self._absoluteFidelity = absoluteFidelity
        else:
            strMessage = (
                "ERROR! XSDataInputBioSaxsSmartMergev1_0 constructor argument 'absoluteFidelity' is not XSDataDouble but %s"
                % self._absoluteFidelity.__class__.__name__
            )
            raise BaseException(strMessage)
        if relativeFidelity is None:
            self._relativeFidelity = None
        elif relativeFidelity.__class__.__name__ == "XSDataDouble":
            self._relativeFidelity = relativeFidelity
        else:
            strMessage = (
                "ERROR! XSDataInputBioSaxsSmartMergev1_0 constructor argument 'relativeFidelity' is not XSDataDouble but %s"
                % self._relativeFidelity.__class__.__name__
            )
            raise BaseException(strMessage)
        if sample is None:
            self._sample = None
        elif sample.__class__.__name__ == "XSDataBioSaxsSample":
            self._sample = sample
        else:
            strMessage = (
                "ERROR! XSDataInputBioSaxsSmartMergev1_0 constructor argument 'sample' is not XSDataBioSaxsSample but %s"
                % self._sample.__class__.__name__
            )
            raise BaseException(strMessage)
        if mergedCurve is None:
            self._mergedCurve = None
        elif mergedCurve.__class__.__name__ == "XSDataFile":
            self._mergedCurve = mergedCurve
        else:
            strMessage = (
                "ERROR! XSDataInputBioSaxsSmartMergev1_0 constructor argument 'mergedCurve' is not XSDataFile but %s"
                % self._mergedCurve.__class__.__name__
            )
            raise BaseException(strMessage)
        if subtractedCurve is None:
            self._subtractedCurve = None
        elif subtractedCurve.__class__.__name__ == "XSDataFile":
            self._subtractedCurve = subtractedCurve
        else:
            strMessage = (
                "ERROR! XSDataInputBioSaxsSmartMergev1_0 constructor argument 'subtractedCurve' is not XSDataFile but %s"
                % self._subtractedCurve.__class__.__name__
            )
            raise BaseException(strMessage)
        if runId is None:
            self._runId = None
        elif runId.__class__.__name__ == "XSDataString":
            self._runId = runId
        else:
            strMessage = (
                "ERROR! XSDataInputBioSaxsSmartMergev1_0 constructor argument 'runId' is not XSDataString but %s"
                % self._runId.__class__.__name__
            )
            raise BaseException(strMessage)
        if bufferCurves is None:
            self._bufferCurves = []
        elif bufferCurves.__class__.__name__ == "list":
            self._bufferCurves = bufferCurves
        else:
            strMessage = (
                "ERROR! XSDataInputBioSaxsSmartMergev1_0 constructor argument 'bufferCurves' is not list but %s"
                % self._bufferCurves.__class__.__name__
            )
            raise BaseException(strMessage)

    # Methods and properties for the 'inputCurves' attribute
    def getInputCurves(self):
        return self._inputCurves

    def setInputCurves(self, inputCurves):
        if inputCurves is None:
            self._inputCurves = []
        elif inputCurves.__class__.__name__ == "list":
            self._inputCurves = inputCurves
        else:
            strMessage = (
                "ERROR! XSDataInputBioSaxsSmartMergev1_0.setInputCurves argument is not list but %s"
                % inputCurves.__class__.__name__
            )
            raise BaseException(strMessage)

    def delInputCurves(self):
        self._inputCurves = None

    inputCurves = property(
        getInputCurves, setInputCurves, delInputCurves, "Property for inputCurves"
    )

    def addInputCurves(self, value):
        if value is None:
            strMessage = "ERROR! XSDataInputBioSaxsSmartMergev1_0.addInputCurves argument is None"
            raise BaseException(strMessage)
        elif value.__class__.__name__ == "XSDataFile":
            self._inputCurves.append(value)
        else:
            strMessage = (
                "ERROR! XSDataInputBioSaxsSmartMergev1_0.addInputCurves argument is not XSDataFile but %s"
                % value.__class__.__name__
            )
            raise BaseException(strMessage)

    def insertInputCurves(self, index, value):
        if index is None:
            strMessage = "ERROR! XSDataInputBioSaxsSmartMergev1_0.insertInputCurves argument 'index' is None"
            raise BaseException(strMessage)
        if value is None:
            strMessage = "ERROR! XSDataInputBioSaxsSmartMergev1_0.insertInputCurves argument 'value' is None"
            raise BaseException(strMessage)
        elif value.__class__.__name__ == "XSDataFile":
            self._inputCurves[index] = value
        else:
            strMessage = (
                "ERROR! XSDataInputBioSaxsSmartMergev1_0.addInputCurves argument is not XSDataFile but %s"
                % value.__class__.__name__
            )
            raise BaseException(strMessage)

    # Methods and properties for the 'absoluteFidelity' attribute
    def getAbsoluteFidelity(self):
        return self._absoluteFidelity

    def setAbsoluteFidelity(self, absoluteFidelity):
        if absoluteFidelity is None:
            self._absoluteFidelity = None
        elif absoluteFidelity.__class__.__name__ == "XSDataDouble":
            self._absoluteFidelity = absoluteFidelity
        else:
            strMessage = (
                "ERROR! XSDataInputBioSaxsSmartMergev1_0.setAbsoluteFidelity argument is not XSDataDouble but %s"
                % absoluteFidelity.__class__.__name__
            )
            raise BaseException(strMessage)

    def delAbsoluteFidelity(self):
        self._absoluteFidelity = None

    absoluteFidelity = property(
        getAbsoluteFidelity,
        setAbsoluteFidelity,
        delAbsoluteFidelity,
        "Property for absoluteFidelity",
    )
    # Methods and properties for the 'relativeFidelity' attribute
    def getRelativeFidelity(self):
        return self._relativeFidelity

    def setRelativeFidelity(self, relativeFidelity):
        if relativeFidelity is None:
            self._relativeFidelity = None
        elif relativeFidelity.__class__.__name__ == "XSDataDouble":
            self._relativeFidelity = relativeFidelity
        else:
            strMessage = (
                "ERROR! XSDataInputBioSaxsSmartMergev1_0.setRelativeFidelity argument is not XSDataDouble but %s"
                % relativeFidelity.__class__.__name__
            )
            raise BaseException(strMessage)

    def delRelativeFidelity(self):
        self._relativeFidelity = None

    relativeFidelity = property(
        getRelativeFidelity,
        setRelativeFidelity,
        delRelativeFidelity,
        "Property for relativeFidelity",
    )
    # Methods and properties for the 'sample' attribute
    def getSample(self):
        return self._sample

    def setSample(self, sample):
        if sample is None:
            self._sample = None
        elif sample.__class__.__name__ == "XSDataBioSaxsSample":
            self._sample = sample
        else:
            strMessage = (
                "ERROR! XSDataInputBioSaxsSmartMergev1_0.setSample argument is not XSDataBioSaxsSample but %s"
                % sample.__class__.__name__
            )
            raise BaseException(strMessage)

    def delSample(self):
        self._sample = None

    sample = property(getSample, setSample, delSample, "Property for sample")
    # Methods and properties for the 'mergedCurve' attribute
    def getMergedCurve(self):
        return self._mergedCurve

    def setMergedCurve(self, mergedCurve):
        if mergedCurve is None:
            self._mergedCurve = None
        elif mergedCurve.__class__.__name__ == "XSDataFile":
            self._mergedCurve = mergedCurve
        else:
            strMessage = (
                "ERROR! XSDataInputBioSaxsSmartMergev1_0.setMergedCurve argument is not XSDataFile but %s"
                % mergedCurve.__class__.__name__
            )
            raise BaseException(strMessage)

    def delMergedCurve(self):
        self._mergedCurve = None

    mergedCurve = property(
        getMergedCurve, setMergedCurve, delMergedCurve, "Property for mergedCurve"
    )
    # Methods and properties for the 'subtractedCurve' attribute
    def getSubtractedCurve(self):
        return self._subtractedCurve

    def setSubtractedCurve(self, subtractedCurve):
        if subtractedCurve is None:
            self._subtractedCurve = None
        elif subtractedCurve.__class__.__name__ == "XSDataFile":
            self._subtractedCurve = subtractedCurve
        else:
            strMessage = (
                "ERROR! XSDataInputBioSaxsSmartMergev1_0.setSubtractedCurve argument is not XSDataFile but %s"
                % subtractedCurve.__class__.__name__
            )
            raise BaseException(strMessage)

    def delSubtractedCurve(self):
        self._subtractedCurve = None

    subtractedCurve = property(
        getSubtractedCurve,
        setSubtractedCurve,
        delSubtractedCurve,
        "Property for subtractedCurve",
    )
    # Methods and properties for the 'runId' attribute
    def getRunId(self):
        return self._runId

    def setRunId(self, runId):
        if runId is None:
            self._runId = None
        elif runId.__class__.__name__ == "XSDataString":
            self._runId = runId
        else:
            strMessage = (
                "ERROR! XSDataInputBioSaxsSmartMergev1_0.setRunId argument is not XSDataString but %s"
                % runId.__class__.__name__
            )
            raise BaseException(strMessage)

    def delRunId(self):
        self._runId = None

    runId = property(getRunId, setRunId, delRunId, "Property for runId")
    # Methods and properties for the 'bufferCurves' attribute
    def getBufferCurves(self):
        return self._bufferCurves

    def setBufferCurves(self, bufferCurves):
        if bufferCurves is None:
            self._bufferCurves = []
        elif bufferCurves.__class__.__name__ == "list":
            self._bufferCurves = bufferCurves
        else:
            strMessage = (
                "ERROR! XSDataInputBioSaxsSmartMergev1_0.setBufferCurves argument is not list but %s"
                % bufferCurves.__class__.__name__
            )
            raise BaseException(strMessage)

    def delBufferCurves(self):
        self._bufferCurves = None

    bufferCurves = property(
        getBufferCurves, setBufferCurves, delBufferCurves, "Property for bufferCurves"
    )

    def addBufferCurves(self, value):
        if value is None:
            strMessage = "ERROR! XSDataInputBioSaxsSmartMergev1_0.addBufferCurves argument is None"
            raise BaseException(strMessage)
        elif value.__class__.__name__ == "XSDataFile":
            self._bufferCurves.append(value)
        else:
            strMessage = (
                "ERROR! XSDataInputBioSaxsSmartMergev1_0.addBufferCurves argument is not XSDataFile but %s"
                % value.__class__.__name__
            )
            raise BaseException(strMessage)

    def insertBufferCurves(self, index, value):
        if index is None:
            strMessage = "ERROR! XSDataInputBioSaxsSmartMergev1_0.insertBufferCurves argument 'index' is None"
            raise BaseException(strMessage)
        if value is None:
            strMessage = "ERROR! XSDataInputBioSaxsSmartMergev1_0.insertBufferCurves argument 'value' is None"
            raise BaseException(strMessage)
        elif value.__class__.__name__ == "XSDataFile":
            self._bufferCurves[index] = value
        else:
            strMessage = (
                "ERROR! XSDataInputBioSaxsSmartMergev1_0.addBufferCurves argument is not XSDataFile but %s"
                % value.__class__.__name__
            )
            raise BaseException(strMessage)

    def export(self, outfile, level, name_="XSDataInputBioSaxsSmartMergev1_0"):
        showIndent(outfile, level)
        outfile.write(unicode("<%s>\n" % name_))
        self.exportChildren(outfile, level + 1, name_)
        showIndent(outfile, level)
        outfile.write(unicode("</%s>\n" % name_))

    def exportChildren(self, outfile, level, name_="XSDataInputBioSaxsSmartMergev1_0"):
        XSDataInput.exportChildren(self, outfile, level, name_)
        for inputCurves_ in self.getInputCurves():
            inputCurves_.export(outfile, level, name_="inputCurves")
        if self.getInputCurves() == []:
            warnEmptyAttribute("inputCurves", "XSDataFile")
        if self._absoluteFidelity is not None:
            self.absoluteFidelity.export(outfile, level, name_="absoluteFidelity")
        if self._relativeFidelity is not None:
            self.relativeFidelity.export(outfile, level, name_="relativeFidelity")
        if self._sample is not None:
            self.sample.export(outfile, level, name_="sample")
        if self._mergedCurve is not None:
            self.mergedCurve.export(outfile, level, name_="mergedCurve")
        else:
            warnEmptyAttribute("mergedCurve", "XSDataFile")
        if self._subtractedCurve is not None:
            self.subtractedCurve.export(outfile, level, name_="subtractedCurve")
        if self._runId is not None:
            self.runId.export(outfile, level, name_="runId")
        for bufferCurves_ in self.getBufferCurves():
            bufferCurves_.export(outfile, level, name_="bufferCurves")

    def build(self, node_):
        for child_ in node_.childNodes:
            nodeName_ = child_.nodeName.split(":")[-1]
            self.buildChildren(child_, nodeName_)

    def buildChildren(self, child_, nodeName_):
        if child_.nodeType == Node.ELEMENT_NODE and nodeName_ == "inputCurves":
            obj_ = XSDataFile()
            obj_.build(child_)
            self.inputCurves.append(obj_)
        elif child_.nodeType == Node.ELEMENT_NODE and nodeName_ == "absoluteFidelity":
            obj_ = XSDataDouble()
            obj_.build(child_)
            self.setAbsoluteFidelity(obj_)
        elif child_.nodeType == Node.ELEMENT_NODE and nodeName_ == "relativeFidelity":
            obj_ = XSDataDouble()
            obj_.build(child_)
            self.setRelativeFidelity(obj_)
        elif child_.nodeType == Node.ELEMENT_NODE and nodeName_ == "sample":
            obj_ = XSDataBioSaxsSample()
            obj_.build(child_)
            self.setSample(obj_)
        elif child_.nodeType == Node.ELEMENT_NODE and nodeName_ == "mergedCurve":
            obj_ = XSDataFile()
            obj_.build(child_)
            self.setMergedCurve(obj_)
        elif child_.nodeType == Node.ELEMENT_NODE and nodeName_ == "subtractedCurve":
            obj_ = XSDataFile()
            obj_.build(child_)
            self.setSubtractedCurve(obj_)
        elif child_.nodeType == Node.ELEMENT_NODE and nodeName_ == "runId":
            obj_ = XSDataString()
            obj_.build(child_)
            self.setRunId(obj_)
        elif child_.nodeType == Node.ELEMENT_NODE and nodeName_ == "bufferCurves":
            obj_ = XSDataFile()
            obj_.build(child_)
            self.bufferCurves.append(obj_)
        XSDataInput.buildChildren(self, child_, nodeName_)

    # Method for marshalling an object
    def marshal(self):
        oStreamString = StringIO()
        oStreamString.write(unicode('<?xml version="1.0" ?>\n'))
        self.export(oStreamString, 0, name_="XSDataInputBioSaxsSmartMergev1_0")
        oStringXML = oStreamString.getvalue()
        oStreamString.close()
        return oStringXML

    # Only to export the entire XML tree to a file stream on disk
    def exportToFile(self, _outfileName):
        outfile = open(_outfileName, "w")
        outfile.write(unicode('<?xml version="1.0" ?>\n'))
        self.export(outfile, 0, name_="XSDataInputBioSaxsSmartMergev1_0")
        outfile.close()

    # Deprecated method, replaced by exportToFile
    def outputFile(self, _outfileName):
        print(
            "WARNING: Method outputFile in class XSDataInputBioSaxsSmartMergev1_0 is deprecated, please use instead exportToFile!"
        )
        self.exportToFile(_outfileName)

    # Method for making a copy in a new instance
    def copy(self):
        return XSDataInputBioSaxsSmartMergev1_0.parseString(self.marshal())

    # Static method for parsing a string
    def parseString(_inString):
        doc = minidom.parseString(_inString)
        rootNode = doc.documentElement
        rootObj = XSDataInputBioSaxsSmartMergev1_0()
        rootObj.build(rootNode)
        # Check that all minOccurs are obeyed by marshalling the created object
        oStreamString = StringIO()
        rootObj.export(oStreamString, 0, name_="XSDataInputBioSaxsSmartMergev1_0")
        oStreamString.close()
        return rootObj

    parseString = staticmethod(parseString)
    # Static method for parsing a file
    def parseFile(_inFilePath):
        doc = minidom.parse(_inFilePath)
        rootNode = doc.documentElement
        rootObj = XSDataInputBioSaxsSmartMergev1_0()
        rootObj.build(rootNode)
        return rootObj

    parseFile = staticmethod(parseFile)


# end class XSDataInputBioSaxsSmartMergev1_0


class XSDataInputBioSaxsSubtractv1_0(XSDataInput):
    """Runs sequentially subtraction of buffer and SaxsAnalysis"""

    def __init__(
        self,
        configuration=None,
        gnomFile=None,
        subtractedCurve=None,
        sample=None,
        bufferCurves=None,
        sampleCurve=None,
    ):
        XSDataInput.__init__(self, configuration)
        if sampleCurve is None:
            self._sampleCurve = None
        elif sampleCurve.__class__.__name__ == "XSDataFile":
            self._sampleCurve = sampleCurve
        else:
            strMessage = (
                "ERROR! XSDataInputBioSaxsSubtractv1_0 constructor argument 'sampleCurve' is not XSDataFile but %s"
                % self._sampleCurve.__class__.__name__
            )
            raise BaseException(strMessage)
        if bufferCurves is None:
            self._bufferCurves = []
        elif bufferCurves.__class__.__name__ == "list":
            self._bufferCurves = bufferCurves
        else:
            strMessage = (
                "ERROR! XSDataInputBioSaxsSubtractv1_0 constructor argument 'bufferCurves' is not list but %s"
                % self._bufferCurves.__class__.__name__
            )
            raise BaseException(strMessage)
        if sample is None:
            self._sample = None
        elif sample.__class__.__name__ == "XSDataBioSaxsSample":
            self._sample = sample
        else:
            strMessage = (
                "ERROR! XSDataInputBioSaxsSubtractv1_0 constructor argument 'sample' is not XSDataBioSaxsSample but %s"
                % self._sample.__class__.__name__
            )
            raise BaseException(strMessage)
        if subtractedCurve is None:
            self._subtractedCurve = None
        elif subtractedCurve.__class__.__name__ == "XSDataFile":
            self._subtractedCurve = subtractedCurve
        else:
            strMessage = (
                "ERROR! XSDataInputBioSaxsSubtractv1_0 constructor argument 'subtractedCurve' is not XSDataFile but %s"
                % self._subtractedCurve.__class__.__name__
            )
            raise BaseException(strMessage)
        if gnomFile is None:
            self._gnomFile = None
        elif gnomFile.__class__.__name__ == "XSDataFile":
            self._gnomFile = gnomFile
        else:
            strMessage = (
                "ERROR! XSDataInputBioSaxsSubtractv1_0 constructor argument 'gnomFile' is not XSDataFile but %s"
                % self._gnomFile.__class__.__name__
            )
            raise BaseException(strMessage)

    # Methods and properties for the 'sampleCurve' attribute
    def getSampleCurve(self):
        return self._sampleCurve

    def setSampleCurve(self, sampleCurve):
        if sampleCurve is None:
            self._sampleCurve = None
        elif sampleCurve.__class__.__name__ == "XSDataFile":
            self._sampleCurve = sampleCurve
        else:
            strMessage = (
                "ERROR! XSDataInputBioSaxsSubtractv1_0.setSampleCurve argument is not XSDataFile but %s"
                % sampleCurve.__class__.__name__
            )
            raise BaseException(strMessage)

    def delSampleCurve(self):
        self._sampleCurve = None

    sampleCurve = property(
        getSampleCurve, setSampleCurve, delSampleCurve, "Property for sampleCurve"
    )
    # Methods and properties for the 'bufferCurves' attribute
    def getBufferCurves(self):
        return self._bufferCurves

    def setBufferCurves(self, bufferCurves):
        if bufferCurves is None:
            self._bufferCurves = []
        elif bufferCurves.__class__.__name__ == "list":
            self._bufferCurves = bufferCurves
        else:
            strMessage = (
                "ERROR! XSDataInputBioSaxsSubtractv1_0.setBufferCurves argument is not list but %s"
                % bufferCurves.__class__.__name__
            )
            raise BaseException(strMessage)

    def delBufferCurves(self):
        self._bufferCurves = None

    bufferCurves = property(
        getBufferCurves, setBufferCurves, delBufferCurves, "Property for bufferCurves"
    )

    def addBufferCurves(self, value):
        if value is None:
            strMessage = (
                "ERROR! XSDataInputBioSaxsSubtractv1_0.addBufferCurves argument is None"
            )
            raise BaseException(strMessage)
        elif value.__class__.__name__ == "XSDataFile":
            self._bufferCurves.append(value)
        else:
            strMessage = (
                "ERROR! XSDataInputBioSaxsSubtractv1_0.addBufferCurves argument is not XSDataFile but %s"
                % value.__class__.__name__
            )
            raise BaseException(strMessage)

    def insertBufferCurves(self, index, value):
        if index is None:
            strMessage = "ERROR! XSDataInputBioSaxsSubtractv1_0.insertBufferCurves argument 'index' is None"
            raise BaseException(strMessage)
        if value is None:
            strMessage = "ERROR! XSDataInputBioSaxsSubtractv1_0.insertBufferCurves argument 'value' is None"
            raise BaseException(strMessage)
        elif value.__class__.__name__ == "XSDataFile":
            self._bufferCurves[index] = value
        else:
            strMessage = (
                "ERROR! XSDataInputBioSaxsSubtractv1_0.addBufferCurves argument is not XSDataFile but %s"
                % value.__class__.__name__
            )
            raise BaseException(strMessage)

    # Methods and properties for the 'sample' attribute
    def getSample(self):
        return self._sample

    def setSample(self, sample):
        if sample is None:
            self._sample = None
        elif sample.__class__.__name__ == "XSDataBioSaxsSample":
            self._sample = sample
        else:
            strMessage = (
                "ERROR! XSDataInputBioSaxsSubtractv1_0.setSample argument is not XSDataBioSaxsSample but %s"
                % sample.__class__.__name__
            )
            raise BaseException(strMessage)

    def delSample(self):
        self._sample = None

    sample = property(getSample, setSample, delSample, "Property for sample")
    # Methods and properties for the 'subtractedCurve' attribute
    def getSubtractedCurve(self):
        return self._subtractedCurve

    def setSubtractedCurve(self, subtractedCurve):
        if subtractedCurve is None:
            self._subtractedCurve = None
        elif subtractedCurve.__class__.__name__ == "XSDataFile":
            self._subtractedCurve = subtractedCurve
        else:
            strMessage = (
                "ERROR! XSDataInputBioSaxsSubtractv1_0.setSubtractedCurve argument is not XSDataFile but %s"
                % subtractedCurve.__class__.__name__
            )
            raise BaseException(strMessage)

    def delSubtractedCurve(self):
        self._subtractedCurve = None

    subtractedCurve = property(
        getSubtractedCurve,
        setSubtractedCurve,
        delSubtractedCurve,
        "Property for subtractedCurve",
    )
    # Methods and properties for the 'gnomFile' attribute
    def getGnomFile(self):
        return self._gnomFile

    def setGnomFile(self, gnomFile):
        if gnomFile is None:
            self._gnomFile = None
        elif gnomFile.__class__.__name__ == "XSDataFile":
            self._gnomFile = gnomFile
        else:
            strMessage = (
                "ERROR! XSDataInputBioSaxsSubtractv1_0.setGnomFile argument is not XSDataFile but %s"
                % gnomFile.__class__.__name__
            )
            raise BaseException(strMessage)

    def delGnomFile(self):
        self._gnomFile = None

    gnomFile = property(getGnomFile, setGnomFile, delGnomFile, "Property for gnomFile")

    def export(self, outfile, level, name_="XSDataInputBioSaxsSubtractv1_0"):
        showIndent(outfile, level)
        outfile.write(unicode("<%s>\n" % name_))
        self.exportChildren(outfile, level + 1, name_)
        showIndent(outfile, level)
        outfile.write(unicode("</%s>\n" % name_))

    def exportChildren(self, outfile, level, name_="XSDataInputBioSaxsSubtractv1_0"):
        XSDataInput.exportChildren(self, outfile, level, name_)
        if self._sampleCurve is not None:
            self.sampleCurve.export(outfile, level, name_="sampleCurve")
        else:
            warnEmptyAttribute("sampleCurve", "XSDataFile")
        for bufferCurves_ in self.getBufferCurves():
            bufferCurves_.export(outfile, level, name_="bufferCurves")
        if self._sample is not None:
            self.sample.export(outfile, level, name_="sample")
        if self._subtractedCurve is not None:
            self.subtractedCurve.export(outfile, level, name_="subtractedCurve")
        if self._gnomFile is not None:
            self.gnomFile.export(outfile, level, name_="gnomFile")

    def build(self, node_):
        for child_ in node_.childNodes:
            nodeName_ = child_.nodeName.split(":")[-1]
            self.buildChildren(child_, nodeName_)

    def buildChildren(self, child_, nodeName_):
        if child_.nodeType == Node.ELEMENT_NODE and nodeName_ == "sampleCurve":
            obj_ = XSDataFile()
            obj_.build(child_)
            self.setSampleCurve(obj_)
        elif child_.nodeType == Node.ELEMENT_NODE and nodeName_ == "bufferCurves":
            obj_ = XSDataFile()
            obj_.build(child_)
            self.bufferCurves.append(obj_)
        elif child_.nodeType == Node.ELEMENT_NODE and nodeName_ == "sample":
            obj_ = XSDataBioSaxsSample()
            obj_.build(child_)
            self.setSample(obj_)
        elif child_.nodeType == Node.ELEMENT_NODE and nodeName_ == "subtractedCurve":
            obj_ = XSDataFile()
            obj_.build(child_)
            self.setSubtractedCurve(obj_)
        elif child_.nodeType == Node.ELEMENT_NODE and nodeName_ == "gnomFile":
            obj_ = XSDataFile()
            obj_.build(child_)
            self.setGnomFile(obj_)
        XSDataInput.buildChildren(self, child_, nodeName_)

    # Method for marshalling an object
    def marshal(self):
        oStreamString = StringIO()
        oStreamString.write(unicode('<?xml version="1.0" ?>\n'))
        self.export(oStreamString, 0, name_="XSDataInputBioSaxsSubtractv1_0")
        oStringXML = oStreamString.getvalue()
        oStreamString.close()
        return oStringXML

    # Only to export the entire XML tree to a file stream on disk
    def exportToFile(self, _outfileName):
        outfile = open(_outfileName, "w")
        outfile.write(unicode('<?xml version="1.0" ?>\n'))
        self.export(outfile, 0, name_="XSDataInputBioSaxsSubtractv1_0")
        outfile.close()

    # Deprecated method, replaced by exportToFile
    def outputFile(self, _outfileName):
        print(
            "WARNING: Method outputFile in class XSDataInputBioSaxsSubtractv1_0 is deprecated, please use instead exportToFile!"
        )
        self.exportToFile(_outfileName)

    # Method for making a copy in a new instance
    def copy(self):
        return XSDataInputBioSaxsSubtractv1_0.parseString(self.marshal())

    # Static method for parsing a string
    def parseString(_inString):
        doc = minidom.parseString(_inString)
        rootNode = doc.documentElement
        rootObj = XSDataInputBioSaxsSubtractv1_0()
        rootObj.build(rootNode)
        # Check that all minOccurs are obeyed by marshalling the created object
        oStreamString = StringIO()
        rootObj.export(oStreamString, 0, name_="XSDataInputBioSaxsSubtractv1_0")
        oStreamString.close()
        return rootObj

    parseString = staticmethod(parseString)
    # Static method for parsing a file
    def parseFile(_inFilePath):
        doc = minidom.parse(_inFilePath)
        rootNode = doc.documentElement
        rootObj = XSDataInputBioSaxsSubtractv1_0()
        rootObj.build(rootNode)
        return rootObj

    parseFile = staticmethod(parseFile)


# end class XSDataInputBioSaxsSubtractv1_0


class XSDataInputBioSaxsToSASv1_0(XSDataInput):
    """This is just a wrapper for the SAS downstream pipeline"""

    def __init__(
        self,
        configuration=None,
        sample=None,
        destinationDirectory=None,
        qMax=None,
        lastPoint=None,
        firstPoint=None,
        gnomFile=None,
        subtractedCurve=None,
    ):
        XSDataInput.__init__(self, configuration)
        if subtractedCurve is None:
            self._subtractedCurve = None
        elif subtractedCurve.__class__.__name__ == "XSDataFile":
            self._subtractedCurve = subtractedCurve
        else:
            strMessage = (
                "ERROR! XSDataInputBioSaxsToSASv1_0 constructor argument 'subtractedCurve' is not XSDataFile but %s"
                % self._subtractedCurve.__class__.__name__
            )
            raise BaseException(strMessage)
        if gnomFile is None:
            self._gnomFile = None
        elif gnomFile.__class__.__name__ == "XSDataFile":
            self._gnomFile = gnomFile
        else:
            strMessage = (
                "ERROR! XSDataInputBioSaxsToSASv1_0 constructor argument 'gnomFile' is not XSDataFile but %s"
                % self._gnomFile.__class__.__name__
            )
            raise BaseException(strMessage)
        if firstPoint is None:
            self._firstPoint = None
        elif firstPoint.__class__.__name__ == "XSDataInteger":
            self._firstPoint = firstPoint
        else:
            strMessage = (
                "ERROR! XSDataInputBioSaxsToSASv1_0 constructor argument 'firstPoint' is not XSDataInteger but %s"
                % self._firstPoint.__class__.__name__
            )
            raise BaseException(strMessage)
        if lastPoint is None:
            self._lastPoint = None
        elif lastPoint.__class__.__name__ == "XSDataInteger":
            self._lastPoint = lastPoint
        else:
            strMessage = (
                "ERROR! XSDataInputBioSaxsToSASv1_0 constructor argument 'lastPoint' is not XSDataInteger but %s"
                % self._lastPoint.__class__.__name__
            )
            raise BaseException(strMessage)
        if qMax is None:
            self._qMax = None
        elif qMax.__class__.__name__ == "XSDataDouble":
            self._qMax = qMax
        else:
            strMessage = (
                "ERROR! XSDataInputBioSaxsToSASv1_0 constructor argument 'qMax' is not XSDataDouble but %s"
                % self._qMax.__class__.__name__
            )
            raise BaseException(strMessage)
        if destinationDirectory is None:
            self._destinationDirectory = None
        elif destinationDirectory.__class__.__name__ == "XSDataFile":
            self._destinationDirectory = destinationDirectory
        else:
            strMessage = (
                "ERROR! XSDataInputBioSaxsToSASv1_0 constructor argument 'destinationDirectory' is not XSDataFile but %s"
                % self._destinationDirectory.__class__.__name__
            )
            raise BaseException(strMessage)
        if sample is None:
            self._sample = None
        elif sample.__class__.__name__ == "XSDataBioSaxsSample":
            self._sample = sample
        else:
            strMessage = (
                "ERROR! XSDataInputBioSaxsToSASv1_0 constructor argument 'sample' is not XSDataBioSaxsSample but %s"
                % self._sample.__class__.__name__
            )
            raise BaseException(strMessage)

    # Methods and properties for the 'subtractedCurve' attribute
    def getSubtractedCurve(self):
        return self._subtractedCurve

    def setSubtractedCurve(self, subtractedCurve):
        if subtractedCurve is None:
            self._subtractedCurve = None
        elif subtractedCurve.__class__.__name__ == "XSDataFile":
            self._subtractedCurve = subtractedCurve
        else:
            strMessage = (
                "ERROR! XSDataInputBioSaxsToSASv1_0.setSubtractedCurve argument is not XSDataFile but %s"
                % subtractedCurve.__class__.__name__
            )
            raise BaseException(strMessage)

    def delSubtractedCurve(self):
        self._subtractedCurve = None

    subtractedCurve = property(
        getSubtractedCurve,
        setSubtractedCurve,
        delSubtractedCurve,
        "Property for subtractedCurve",
    )
    # Methods and properties for the 'gnomFile' attribute
    def getGnomFile(self):
        return self._gnomFile

    def setGnomFile(self, gnomFile):
        if gnomFile is None:
            self._gnomFile = None
        elif gnomFile.__class__.__name__ == "XSDataFile":
            self._gnomFile = gnomFile
        else:
            strMessage = (
                "ERROR! XSDataInputBioSaxsToSASv1_0.setGnomFile argument is not XSDataFile but %s"
                % gnomFile.__class__.__name__
            )
            raise BaseException(strMessage)

    def delGnomFile(self):
        self._gnomFile = None

    gnomFile = property(getGnomFile, setGnomFile, delGnomFile, "Property for gnomFile")
    # Methods and properties for the 'firstPoint' attribute
    def getFirstPoint(self):
        return self._firstPoint

    def setFirstPoint(self, firstPoint):
        if firstPoint is None:
            self._firstPoint = None
        elif firstPoint.__class__.__name__ == "XSDataInteger":
            self._firstPoint = firstPoint
        else:
            strMessage = (
                "ERROR! XSDataInputBioSaxsToSASv1_0.setFirstPoint argument is not XSDataInteger but %s"
                % firstPoint.__class__.__name__
            )
            raise BaseException(strMessage)

    def delFirstPoint(self):
        self._firstPoint = None

    firstPoint = property(
        getFirstPoint, setFirstPoint, delFirstPoint, "Property for firstPoint"
    )
    # Methods and properties for the 'lastPoint' attribute
    def getLastPoint(self):
        return self._lastPoint

    def setLastPoint(self, lastPoint):
        if lastPoint is None:
            self._lastPoint = None
        elif lastPoint.__class__.__name__ == "XSDataInteger":
            self._lastPoint = lastPoint
        else:
            strMessage = (
                "ERROR! XSDataInputBioSaxsToSASv1_0.setLastPoint argument is not XSDataInteger but %s"
                % lastPoint.__class__.__name__
            )
            raise BaseException(strMessage)

    def delLastPoint(self):
        self._lastPoint = None

    lastPoint = property(
        getLastPoint, setLastPoint, delLastPoint, "Property for lastPoint"
    )
    # Methods and properties for the 'qMax' attribute
    def getQMax(self):
        return self._qMax

    def setQMax(self, qMax):
        if qMax is None:
            self._qMax = None
        elif qMax.__class__.__name__ == "XSDataDouble":
            self._qMax = qMax
        else:
            strMessage = (
                "ERROR! XSDataInputBioSaxsToSASv1_0.setQMax argument is not XSDataDouble but %s"
                % qMax.__class__.__name__
            )
            raise BaseException(strMessage)

    def delQMax(self):
        self._qMax = None

    qMax = property(getQMax, setQMax, delQMax, "Property for qMax")
    # Methods and properties for the 'destinationDirectory' attribute
    def getDestinationDirectory(self):
        return self._destinationDirectory

    def setDestinationDirectory(self, destinationDirectory):
        if destinationDirectory is None:
            self._destinationDirectory = None
        elif destinationDirectory.__class__.__name__ == "XSDataFile":
            self._destinationDirectory = destinationDirectory
        else:
            strMessage = (
                "ERROR! XSDataInputBioSaxsToSASv1_0.setDestinationDirectory argument is not XSDataFile but %s"
                % destinationDirectory.__class__.__name__
            )
            raise BaseException(strMessage)

    def delDestinationDirectory(self):
        self._destinationDirectory = None

    destinationDirectory = property(
        getDestinationDirectory,
        setDestinationDirectory,
        delDestinationDirectory,
        "Property for destinationDirectory",
    )
    # Methods and properties for the 'sample' attribute
    def getSample(self):
        return self._sample

    def setSample(self, sample):
        if sample is None:
            self._sample = None
        elif sample.__class__.__name__ == "XSDataBioSaxsSample":
            self._sample = sample
        else:
            strMessage = (
                "ERROR! XSDataInputBioSaxsToSASv1_0.setSample argument is not XSDataBioSaxsSample but %s"
                % sample.__class__.__name__
            )
            raise BaseException(strMessage)

    def delSample(self):
        self._sample = None

    sample = property(getSample, setSample, delSample, "Property for sample")

    def export(self, outfile, level, name_="XSDataInputBioSaxsToSASv1_0"):
        showIndent(outfile, level)
        outfile.write(unicode("<%s>\n" % name_))
        self.exportChildren(outfile, level + 1, name_)
        showIndent(outfile, level)
        outfile.write(unicode("</%s>\n" % name_))

    def exportChildren(self, outfile, level, name_="XSDataInputBioSaxsToSASv1_0"):
        XSDataInput.exportChildren(self, outfile, level, name_)
        if self._subtractedCurve is not None:
            self.subtractedCurve.export(outfile, level, name_="subtractedCurve")
        if self._gnomFile is not None:
            self.gnomFile.export(outfile, level, name_="gnomFile")
        if self._firstPoint is not None:
            self.firstPoint.export(outfile, level, name_="firstPoint")
        if self._lastPoint is not None:
            self.lastPoint.export(outfile, level, name_="lastPoint")
        if self._qMax is not None:
            self.qMax.export(outfile, level, name_="qMax")
        if self._destinationDirectory is not None:
            self.destinationDirectory.export(
                outfile, level, name_="destinationDirectory"
            )
        if self._sample is not None:
            self.sample.export(outfile, level, name_="sample")

    def build(self, node_):
        for child_ in node_.childNodes:
            nodeName_ = child_.nodeName.split(":")[-1]
            self.buildChildren(child_, nodeName_)

    def buildChildren(self, child_, nodeName_):
        if child_.nodeType == Node.ELEMENT_NODE and nodeName_ == "subtractedCurve":
            obj_ = XSDataFile()
            obj_.build(child_)
            self.setSubtractedCurve(obj_)
        elif child_.nodeType == Node.ELEMENT_NODE and nodeName_ == "gnomFile":
            obj_ = XSDataFile()
            obj_.build(child_)
            self.setGnomFile(obj_)
        elif child_.nodeType == Node.ELEMENT_NODE and nodeName_ == "firstPoint":
            obj_ = XSDataInteger()
            obj_.build(child_)
            self.setFirstPoint(obj_)
        elif child_.nodeType == Node.ELEMENT_NODE and nodeName_ == "lastPoint":
            obj_ = XSDataInteger()
            obj_.build(child_)
            self.setLastPoint(obj_)
        elif child_.nodeType == Node.ELEMENT_NODE and nodeName_ == "qMax":
            obj_ = XSDataDouble()
            obj_.build(child_)
            self.setQMax(obj_)
        elif (
            child_.nodeType == Node.ELEMENT_NODE and nodeName_ == "destinationDirectory"
        ):
            obj_ = XSDataFile()
            obj_.build(child_)
            self.setDestinationDirectory(obj_)
        elif child_.nodeType == Node.ELEMENT_NODE and nodeName_ == "sample":
            obj_ = XSDataBioSaxsSample()
            obj_.build(child_)
            self.setSample(obj_)
        XSDataInput.buildChildren(self, child_, nodeName_)

    # Method for marshalling an object
    def marshal(self):
        oStreamString = StringIO()
        oStreamString.write(unicode('<?xml version="1.0" ?>\n'))
        self.export(oStreamString, 0, name_="XSDataInputBioSaxsToSASv1_0")
        oStringXML = oStreamString.getvalue()
        oStreamString.close()
        return oStringXML

    # Only to export the entire XML tree to a file stream on disk
    def exportToFile(self, _outfileName):
        outfile = open(_outfileName, "w")
        outfile.write(unicode('<?xml version="1.0" ?>\n'))
        self.export(outfile, 0, name_="XSDataInputBioSaxsToSASv1_0")
        outfile.close()

    # Deprecated method, replaced by exportToFile
    def outputFile(self, _outfileName):
        print(
            "WARNING: Method outputFile in class XSDataInputBioSaxsToSASv1_0 is deprecated, please use instead exportToFile!"
        )
        self.exportToFile(_outfileName)

    # Method for making a copy in a new instance
    def copy(self):
        return XSDataInputBioSaxsToSASv1_0.parseString(self.marshal())

    # Static method for parsing a string
    def parseString(_inString):
        doc = minidom.parseString(_inString)
        rootNode = doc.documentElement
        rootObj = XSDataInputBioSaxsToSASv1_0()
        rootObj.build(rootNode)
        # Check that all minOccurs are obeyed by marshalling the created object
        oStreamString = StringIO()
        rootObj.export(oStreamString, 0, name_="XSDataInputBioSaxsToSASv1_0")
        oStreamString.close()
        return rootObj

    parseString = staticmethod(parseString)
    # Static method for parsing a file
    def parseFile(_inFilePath):
        doc = minidom.parse(_inFilePath)
        rootNode = doc.documentElement
        rootObj = XSDataInputBioSaxsToSASv1_0()
        rootObj.build(rootNode)
        return rootObj

    parseFile = staticmethod(parseFile)


# end class XSDataInputBioSaxsToSASv1_0


class XSDataResultBioSaxsAsciiExportv1_0(XSDataResult):
    def __init__(self, status=None, processLog=None, integratedCurve=None):
        XSDataResult.__init__(self, status)
        if integratedCurve is None:
            self._integratedCurve = None
        elif integratedCurve.__class__.__name__ == "XSDataFile":
            self._integratedCurve = integratedCurve
        else:
            strMessage = (
                "ERROR! XSDataResultBioSaxsAsciiExportv1_0 constructor argument 'integratedCurve' is not XSDataFile but %s"
                % self._integratedCurve.__class__.__name__
            )
            raise BaseException(strMessage)
        if processLog is None:
            self._processLog = None
        elif processLog.__class__.__name__ == "XSDataString":
            self._processLog = processLog
        else:
            strMessage = (
                "ERROR! XSDataResultBioSaxsAsciiExportv1_0 constructor argument 'processLog' is not XSDataString but %s"
                % self._processLog.__class__.__name__
            )
            raise BaseException(strMessage)

    # Methods and properties for the 'integratedCurve' attribute
    def getIntegratedCurve(self):
        return self._integratedCurve

    def setIntegratedCurve(self, integratedCurve):
        if integratedCurve is None:
            self._integratedCurve = None
        elif integratedCurve.__class__.__name__ == "XSDataFile":
            self._integratedCurve = integratedCurve
        else:
            strMessage = (
                "ERROR! XSDataResultBioSaxsAsciiExportv1_0.setIntegratedCurve argument is not XSDataFile but %s"
                % integratedCurve.__class__.__name__
            )
            raise BaseException(strMessage)

    def delIntegratedCurve(self):
        self._integratedCurve = None

    integratedCurve = property(
        getIntegratedCurve,
        setIntegratedCurve,
        delIntegratedCurve,
        "Property for integratedCurve",
    )
    # Methods and properties for the 'processLog' attribute
    def getProcessLog(self):
        return self._processLog

    def setProcessLog(self, processLog):
        if processLog is None:
            self._processLog = None
        elif processLog.__class__.__name__ == "XSDataString":
            self._processLog = processLog
        else:
            strMessage = (
                "ERROR! XSDataResultBioSaxsAsciiExportv1_0.setProcessLog argument is not XSDataString but %s"
                % processLog.__class__.__name__
            )
            raise BaseException(strMessage)

    def delProcessLog(self):
        self._processLog = None

    processLog = property(
        getProcessLog, setProcessLog, delProcessLog, "Property for processLog"
    )

    def export(self, outfile, level, name_="XSDataResultBioSaxsAsciiExportv1_0"):
        showIndent(outfile, level)
        outfile.write(unicode("<%s>\n" % name_))
        self.exportChildren(outfile, level + 1, name_)
        showIndent(outfile, level)
        outfile.write(unicode("</%s>\n" % name_))

    def exportChildren(
        self, outfile, level, name_="XSDataResultBioSaxsAsciiExportv1_0"
    ):
        XSDataResult.exportChildren(self, outfile, level, name_)
        if self._integratedCurve is not None:
            self.integratedCurve.export(outfile, level, name_="integratedCurve")
        else:
            warnEmptyAttribute("integratedCurve", "XSDataFile")
        if self._processLog is not None:
            self.processLog.export(outfile, level, name_="processLog")
        else:
            warnEmptyAttribute("processLog", "XSDataString")

    def build(self, node_):
        for child_ in node_.childNodes:
            nodeName_ = child_.nodeName.split(":")[-1]
            self.buildChildren(child_, nodeName_)

    def buildChildren(self, child_, nodeName_):
        if child_.nodeType == Node.ELEMENT_NODE and nodeName_ == "integratedCurve":
            obj_ = XSDataFile()
            obj_.build(child_)
            self.setIntegratedCurve(obj_)
        elif child_.nodeType == Node.ELEMENT_NODE and nodeName_ == "processLog":
            obj_ = XSDataString()
            obj_.build(child_)
            self.setProcessLog(obj_)
        XSDataResult.buildChildren(self, child_, nodeName_)

    # Method for marshalling an object
    def marshal(self):
        oStreamString = StringIO()
        oStreamString.write(unicode('<?xml version="1.0" ?>\n'))
        self.export(oStreamString, 0, name_="XSDataResultBioSaxsAsciiExportv1_0")
        oStringXML = oStreamString.getvalue()
        oStreamString.close()
        return oStringXML

    # Only to export the entire XML tree to a file stream on disk
    def exportToFile(self, _outfileName):
        outfile = open(_outfileName, "w")
        outfile.write(unicode('<?xml version="1.0" ?>\n'))
        self.export(outfile, 0, name_="XSDataResultBioSaxsAsciiExportv1_0")
        outfile.close()

    # Deprecated method, replaced by exportToFile
    def outputFile(self, _outfileName):
        print(
            "WARNING: Method outputFile in class XSDataResultBioSaxsAsciiExportv1_0 is deprecated, please use instead exportToFile!"
        )
        self.exportToFile(_outfileName)

    # Method for making a copy in a new instance
    def copy(self):
        return XSDataResultBioSaxsAsciiExportv1_0.parseString(self.marshal())

    # Static method for parsing a string
    def parseString(_inString):
        doc = minidom.parseString(_inString)
        rootNode = doc.documentElement
        rootObj = XSDataResultBioSaxsAsciiExportv1_0()
        rootObj.build(rootNode)
        # Check that all minOccurs are obeyed by marshalling the created object
        oStreamString = StringIO()
        rootObj.export(oStreamString, 0, name_="XSDataResultBioSaxsAsciiExportv1_0")
        oStreamString.close()
        return rootObj

    parseString = staticmethod(parseString)
    # Static method for parsing a file
    def parseFile(_inFilePath):
        doc = minidom.parse(_inFilePath)
        rootNode = doc.documentElement
        rootObj = XSDataResultBioSaxsAsciiExportv1_0()
        rootObj.build(rootNode)
        return rootObj

    parseFile = staticmethod(parseFile)


# end class XSDataResultBioSaxsAsciiExportv1_0


class XSDataResultBioSaxsAveragev1_0(XSDataResult):
    def __init__(
        self,
        status=None,
        logFile=None,
        processLog=None,
        averagedCurve=None,
        averagedImage=None,
    ):
        XSDataResult.__init__(self, status)
        if averagedImage is None:
            self._averagedImage = None
        elif averagedImage.__class__.__name__ == "XSDataImage":
            self._averagedImage = averagedImage
        else:
            strMessage = (
                "ERROR! XSDataResultBioSaxsAveragev1_0 constructor argument 'averagedImage' is not XSDataImage but %s"
                % self._averagedImage.__class__.__name__
            )
            raise BaseException(strMessage)
        if averagedCurve is None:
            self._averagedCurve = None
        elif averagedCurve.__class__.__name__ == "XSDataFile":
            self._averagedCurve = averagedCurve
        else:
            strMessage = (
                "ERROR! XSDataResultBioSaxsAveragev1_0 constructor argument 'averagedCurve' is not XSDataFile but %s"
                % self._averagedCurve.__class__.__name__
            )
            raise BaseException(strMessage)
        if processLog is None:
            self._processLog = None
        elif processLog.__class__.__name__ == "XSDataString":
            self._processLog = processLog
        else:
            strMessage = (
                "ERROR! XSDataResultBioSaxsAveragev1_0 constructor argument 'processLog' is not XSDataString but %s"
                % self._processLog.__class__.__name__
            )
            raise BaseException(strMessage)
        if logFile is None:
            self._logFile = None
        elif logFile.__class__.__name__ == "XSDataFile":
            self._logFile = logFile
        else:
            strMessage = (
                "ERROR! XSDataResultBioSaxsAveragev1_0 constructor argument 'logFile' is not XSDataFile but %s"
                % self._logFile.__class__.__name__
            )
            raise BaseException(strMessage)

    # Methods and properties for the 'averagedImage' attribute
    def getAveragedImage(self):
        return self._averagedImage

    def setAveragedImage(self, averagedImage):
        if averagedImage is None:
            self._averagedImage = None
        elif averagedImage.__class__.__name__ == "XSDataImage":
            self._averagedImage = averagedImage
        else:
            strMessage = (
                "ERROR! XSDataResultBioSaxsAveragev1_0.setAveragedImage argument is not XSDataImage but %s"
                % averagedImage.__class__.__name__
            )
            raise BaseException(strMessage)

    def delAveragedImage(self):
        self._averagedImage = None

    averagedImage = property(
        getAveragedImage,
        setAveragedImage,
        delAveragedImage,
        "Property for averagedImage",
    )
    # Methods and properties for the 'averagedCurve' attribute
    def getAveragedCurve(self):
        return self._averagedCurve

    def setAveragedCurve(self, averagedCurve):
        if averagedCurve is None:
            self._averagedCurve = None
        elif averagedCurve.__class__.__name__ == "XSDataFile":
            self._averagedCurve = averagedCurve
        else:
            strMessage = (
                "ERROR! XSDataResultBioSaxsAveragev1_0.setAveragedCurve argument is not XSDataFile but %s"
                % averagedCurve.__class__.__name__
            )
            raise BaseException(strMessage)

    def delAveragedCurve(self):
        self._averagedCurve = None

    averagedCurve = property(
        getAveragedCurve,
        setAveragedCurve,
        delAveragedCurve,
        "Property for averagedCurve",
    )
    # Methods and properties for the 'processLog' attribute
    def getProcessLog(self):
        return self._processLog

    def setProcessLog(self, processLog):
        if processLog is None:
            self._processLog = None
        elif processLog.__class__.__name__ == "XSDataString":
            self._processLog = processLog
        else:
            strMessage = (
                "ERROR! XSDataResultBioSaxsAveragev1_0.setProcessLog argument is not XSDataString but %s"
                % processLog.__class__.__name__
            )
            raise BaseException(strMessage)

    def delProcessLog(self):
        self._processLog = None

    processLog = property(
        getProcessLog, setProcessLog, delProcessLog, "Property for processLog"
    )
    # Methods and properties for the 'logFile' attribute
    def getLogFile(self):
        return self._logFile

    def setLogFile(self, logFile):
        if logFile is None:
            self._logFile = None
        elif logFile.__class__.__name__ == "XSDataFile":
            self._logFile = logFile
        else:
            strMessage = (
                "ERROR! XSDataResultBioSaxsAveragev1_0.setLogFile argument is not XSDataFile but %s"
                % logFile.__class__.__name__
            )
            raise BaseException(strMessage)

    def delLogFile(self):
        self._logFile = None

    logFile = property(getLogFile, setLogFile, delLogFile, "Property for logFile")

    def export(self, outfile, level, name_="XSDataResultBioSaxsAveragev1_0"):
        showIndent(outfile, level)
        outfile.write(unicode("<%s>\n" % name_))
        self.exportChildren(outfile, level + 1, name_)
        showIndent(outfile, level)
        outfile.write(unicode("</%s>\n" % name_))

    def exportChildren(self, outfile, level, name_="XSDataResultBioSaxsAveragev1_0"):
        XSDataResult.exportChildren(self, outfile, level, name_)
        if self._averagedImage is not None:
            self.averagedImage.export(outfile, level, name_="averagedImage")
        else:
            warnEmptyAttribute("averagedImage", "XSDataImage")
        if self._averagedCurve is not None:
            self.averagedCurve.export(outfile, level, name_="averagedCurve")
        else:
            warnEmptyAttribute("averagedCurve", "XSDataFile")
        if self._processLog is not None:
            self.processLog.export(outfile, level, name_="processLog")
        else:
            warnEmptyAttribute("processLog", "XSDataString")
        if self._logFile is not None:
            self.logFile.export(outfile, level, name_="logFile")
        else:
            warnEmptyAttribute("logFile", "XSDataFile")

    def build(self, node_):
        for child_ in node_.childNodes:
            nodeName_ = child_.nodeName.split(":")[-1]
            self.buildChildren(child_, nodeName_)

    def buildChildren(self, child_, nodeName_):
        if child_.nodeType == Node.ELEMENT_NODE and nodeName_ == "averagedImage":
            obj_ = XSDataImage()
            obj_.build(child_)
            self.setAveragedImage(obj_)
        elif child_.nodeType == Node.ELEMENT_NODE and nodeName_ == "averagedCurve":
            obj_ = XSDataFile()
            obj_.build(child_)
            self.setAveragedCurve(obj_)
        elif child_.nodeType == Node.ELEMENT_NODE and nodeName_ == "processLog":
            obj_ = XSDataString()
            obj_.build(child_)
            self.setProcessLog(obj_)
        elif child_.nodeType == Node.ELEMENT_NODE and nodeName_ == "logFile":
            obj_ = XSDataFile()
            obj_.build(child_)
            self.setLogFile(obj_)
        XSDataResult.buildChildren(self, child_, nodeName_)

    # Method for marshalling an object
    def marshal(self):
        oStreamString = StringIO()
        oStreamString.write(unicode('<?xml version="1.0" ?>\n'))
        self.export(oStreamString, 0, name_="XSDataResultBioSaxsAveragev1_0")
        oStringXML = oStreamString.getvalue()
        oStreamString.close()
        return oStringXML

    # Only to export the entire XML tree to a file stream on disk
    def exportToFile(self, _outfileName):
        outfile = open(_outfileName, "w")
        outfile.write(unicode('<?xml version="1.0" ?>\n'))
        self.export(outfile, 0, name_="XSDataResultBioSaxsAveragev1_0")
        outfile.close()

    # Deprecated method, replaced by exportToFile
    def outputFile(self, _outfileName):
        print(
            "WARNING: Method outputFile in class XSDataResultBioSaxsAveragev1_0 is deprecated, please use instead exportToFile!"
        )
        self.exportToFile(_outfileName)

    # Method for making a copy in a new instance
    def copy(self):
        return XSDataResultBioSaxsAveragev1_0.parseString(self.marshal())

    # Static method for parsing a string
    def parseString(_inString):
        doc = minidom.parseString(_inString)
        rootNode = doc.documentElement
        rootObj = XSDataResultBioSaxsAveragev1_0()
        rootObj.build(rootNode)
        # Check that all minOccurs are obeyed by marshalling the created object
        oStreamString = StringIO()
        rootObj.export(oStreamString, 0, name_="XSDataResultBioSaxsAveragev1_0")
        oStreamString.close()
        return rootObj

    parseString = staticmethod(parseString)
    # Static method for parsing a file
    def parseFile(_inFilePath):
        doc = minidom.parse(_inFilePath)
        rootNode = doc.documentElement
        rootObj = XSDataResultBioSaxsAveragev1_0()
        rootObj.build(rootNode)
        return rootObj

    parseFile = staticmethod(parseFile)


# end class XSDataResultBioSaxsAveragev1_0


class XSDataResultBioSaxsAzimutIntv1_0(XSDataResult):
    def __init__(
        self,
        status=None,
        experimentSetup=None,
        sample=None,
        integratedCurve=None,
        integratedImage=None,
        correctedImage=None,
    ):
        XSDataResult.__init__(self, status)
        if correctedImage is None:
            self._correctedImage = None
        elif correctedImage.__class__.__name__ == "XSDataImage":
            self._correctedImage = correctedImage
        else:
            strMessage = (
                "ERROR! XSDataResultBioSaxsAzimutIntv1_0 constructor argument 'correctedImage' is not XSDataImage but %s"
                % self._correctedImage.__class__.__name__
            )
            raise BaseException(strMessage)
        if integratedImage is None:
            self._integratedImage = None
        elif integratedImage.__class__.__name__ == "XSDataImage":
            self._integratedImage = integratedImage
        else:
            strMessage = (
                "ERROR! XSDataResultBioSaxsAzimutIntv1_0 constructor argument 'integratedImage' is not XSDataImage but %s"
                % self._integratedImage.__class__.__name__
            )
            raise BaseException(strMessage)
        if integratedCurve is None:
            self._integratedCurve = None
        elif integratedCurve.__class__.__name__ == "XSDataFile":
            self._integratedCurve = integratedCurve
        else:
            strMessage = (
                "ERROR! XSDataResultBioSaxsAzimutIntv1_0 constructor argument 'integratedCurve' is not XSDataFile but %s"
                % self._integratedCurve.__class__.__name__
            )
            raise BaseException(strMessage)
        if sample is None:
            self._sample = None
        elif sample.__class__.__name__ == "XSDataBioSaxsSample":
            self._sample = sample
        else:
            strMessage = (
                "ERROR! XSDataResultBioSaxsAzimutIntv1_0 constructor argument 'sample' is not XSDataBioSaxsSample but %s"
                % self._sample.__class__.__name__
            )
            raise BaseException(strMessage)
        if experimentSetup is None:
            self._experimentSetup = None
        elif experimentSetup.__class__.__name__ == "XSDataBioSaxsExperimentSetup":
            self._experimentSetup = experimentSetup
        else:
            strMessage = (
                "ERROR! XSDataResultBioSaxsAzimutIntv1_0 constructor argument 'experimentSetup' is not XSDataBioSaxsExperimentSetup but %s"
                % self._experimentSetup.__class__.__name__
            )
            raise BaseException(strMessage)

    # Methods and properties for the 'correctedImage' attribute
    def getCorrectedImage(self):
        return self._correctedImage

    def setCorrectedImage(self, correctedImage):
        if correctedImage is None:
            self._correctedImage = None
        elif correctedImage.__class__.__name__ == "XSDataImage":
            self._correctedImage = correctedImage
        else:
            strMessage = (
                "ERROR! XSDataResultBioSaxsAzimutIntv1_0.setCorrectedImage argument is not XSDataImage but %s"
                % correctedImage.__class__.__name__
            )
            raise BaseException(strMessage)

    def delCorrectedImage(self):
        self._correctedImage = None

    correctedImage = property(
        getCorrectedImage,
        setCorrectedImage,
        delCorrectedImage,
        "Property for correctedImage",
    )
    # Methods and properties for the 'integratedImage' attribute
    def getIntegratedImage(self):
        return self._integratedImage

    def setIntegratedImage(self, integratedImage):
        if integratedImage is None:
            self._integratedImage = None
        elif integratedImage.__class__.__name__ == "XSDataImage":
            self._integratedImage = integratedImage
        else:
            strMessage = (
                "ERROR! XSDataResultBioSaxsAzimutIntv1_0.setIntegratedImage argument is not XSDataImage but %s"
                % integratedImage.__class__.__name__
            )
            raise BaseException(strMessage)

    def delIntegratedImage(self):
        self._integratedImage = None

    integratedImage = property(
        getIntegratedImage,
        setIntegratedImage,
        delIntegratedImage,
        "Property for integratedImage",
    )
    # Methods and properties for the 'integratedCurve' attribute
    def getIntegratedCurve(self):
        return self._integratedCurve

    def setIntegratedCurve(self, integratedCurve):
        if integratedCurve is None:
            self._integratedCurve = None
        elif integratedCurve.__class__.__name__ == "XSDataFile":
            self._integratedCurve = integratedCurve
        else:
            strMessage = (
                "ERROR! XSDataResultBioSaxsAzimutIntv1_0.setIntegratedCurve argument is not XSDataFile but %s"
                % integratedCurve.__class__.__name__
            )
            raise BaseException(strMessage)

    def delIntegratedCurve(self):
        self._integratedCurve = None

    integratedCurve = property(
        getIntegratedCurve,
        setIntegratedCurve,
        delIntegratedCurve,
        "Property for integratedCurve",
    )
    # Methods and properties for the 'sample' attribute
    def getSample(self):
        return self._sample

    def setSample(self, sample):
        if sample is None:
            self._sample = None
        elif sample.__class__.__name__ == "XSDataBioSaxsSample":
            self._sample = sample
        else:
            strMessage = (
                "ERROR! XSDataResultBioSaxsAzimutIntv1_0.setSample argument is not XSDataBioSaxsSample but %s"
                % sample.__class__.__name__
            )
            raise BaseException(strMessage)

    def delSample(self):
        self._sample = None

    sample = property(getSample, setSample, delSample, "Property for sample")
    # Methods and properties for the 'experimentSetup' attribute
    def getExperimentSetup(self):
        return self._experimentSetup

    def setExperimentSetup(self, experimentSetup):
        if experimentSetup is None:
            self._experimentSetup = None
        elif experimentSetup.__class__.__name__ == "XSDataBioSaxsExperimentSetup":
            self._experimentSetup = experimentSetup
        else:
            strMessage = (
                "ERROR! XSDataResultBioSaxsAzimutIntv1_0.setExperimentSetup argument is not XSDataBioSaxsExperimentSetup but %s"
                % experimentSetup.__class__.__name__
            )
            raise BaseException(strMessage)

    def delExperimentSetup(self):
        self._experimentSetup = None

    experimentSetup = property(
        getExperimentSetup,
        setExperimentSetup,
        delExperimentSetup,
        "Property for experimentSetup",
    )

    def export(self, outfile, level, name_="XSDataResultBioSaxsAzimutIntv1_0"):
        showIndent(outfile, level)
        outfile.write(unicode("<%s>\n" % name_))
        self.exportChildren(outfile, level + 1, name_)
        showIndent(outfile, level)
        outfile.write(unicode("</%s>\n" % name_))

    def exportChildren(self, outfile, level, name_="XSDataResultBioSaxsAzimutIntv1_0"):
        XSDataResult.exportChildren(self, outfile, level, name_)
        if self._correctedImage is not None:
            self.correctedImage.export(outfile, level, name_="correctedImage")
        else:
            warnEmptyAttribute("correctedImage", "XSDataImage")
        if self._integratedImage is not None:
            self.integratedImage.export(outfile, level, name_="integratedImage")
        else:
            warnEmptyAttribute("integratedImage", "XSDataImage")
        if self._integratedCurve is not None:
            self.integratedCurve.export(outfile, level, name_="integratedCurve")
        else:
            warnEmptyAttribute("integratedCurve", "XSDataFile")
        if self._sample is not None:
            self.sample.export(outfile, level, name_="sample")
        if self._experimentSetup is not None:
            self.experimentSetup.export(outfile, level, name_="experimentSetup")

    def build(self, node_):
        for child_ in node_.childNodes:
            nodeName_ = child_.nodeName.split(":")[-1]
            self.buildChildren(child_, nodeName_)

    def buildChildren(self, child_, nodeName_):
        if child_.nodeType == Node.ELEMENT_NODE and nodeName_ == "correctedImage":
            obj_ = XSDataImage()
            obj_.build(child_)
            self.setCorrectedImage(obj_)
        elif child_.nodeType == Node.ELEMENT_NODE and nodeName_ == "integratedImage":
            obj_ = XSDataImage()
            obj_.build(child_)
            self.setIntegratedImage(obj_)
        elif child_.nodeType == Node.ELEMENT_NODE and nodeName_ == "integratedCurve":
            obj_ = XSDataFile()
            obj_.build(child_)
            self.setIntegratedCurve(obj_)
        elif child_.nodeType == Node.ELEMENT_NODE and nodeName_ == "sample":
            obj_ = XSDataBioSaxsSample()
            obj_.build(child_)
            self.setSample(obj_)
        elif child_.nodeType == Node.ELEMENT_NODE and nodeName_ == "experimentSetup":
            obj_ = XSDataBioSaxsExperimentSetup()
            obj_.build(child_)
            self.setExperimentSetup(obj_)
        XSDataResult.buildChildren(self, child_, nodeName_)

    # Method for marshalling an object
    def marshal(self):
        oStreamString = StringIO()
        oStreamString.write(unicode('<?xml version="1.0" ?>\n'))
        self.export(oStreamString, 0, name_="XSDataResultBioSaxsAzimutIntv1_0")
        oStringXML = oStreamString.getvalue()
        oStreamString.close()
        return oStringXML

    # Only to export the entire XML tree to a file stream on disk
    def exportToFile(self, _outfileName):
        outfile = open(_outfileName, "w")
        outfile.write(unicode('<?xml version="1.0" ?>\n'))
        self.export(outfile, 0, name_="XSDataResultBioSaxsAzimutIntv1_0")
        outfile.close()

    # Deprecated method, replaced by exportToFile
    def outputFile(self, _outfileName):
        print(
            "WARNING: Method outputFile in class XSDataResultBioSaxsAzimutIntv1_0 is deprecated, please use instead exportToFile!"
        )
        self.exportToFile(_outfileName)

    # Method for making a copy in a new instance
    def copy(self):
        return XSDataResultBioSaxsAzimutIntv1_0.parseString(self.marshal())

    # Static method for parsing a string
    def parseString(_inString):
        doc = minidom.parseString(_inString)
        rootNode = doc.documentElement
        rootObj = XSDataResultBioSaxsAzimutIntv1_0()
        rootObj.build(rootNode)
        # Check that all minOccurs are obeyed by marshalling the created object
        oStreamString = StringIO()
        rootObj.export(oStreamString, 0, name_="XSDataResultBioSaxsAzimutIntv1_0")
        oStreamString.close()
        return rootObj

    parseString = staticmethod(parseString)
    # Static method for parsing a file
    def parseFile(_inFilePath):
        doc = minidom.parse(_inFilePath)
        rootNode = doc.documentElement
        rootObj = XSDataResultBioSaxsAzimutIntv1_0()
        rootObj.build(rootNode)
        return rootObj

    parseFile = staticmethod(parseFile)


# end class XSDataResultBioSaxsAzimutIntv1_0


class XSDataResultBioSaxsISPyBModellingv1_0(XSDataResult):
    def __init__(self, status=None):
        XSDataResult.__init__(self, status)

    def export(self, outfile, level, name_="XSDataResultBioSaxsISPyBModellingv1_0"):
        showIndent(outfile, level)
        outfile.write(unicode("<%s>\n" % name_))
        self.exportChildren(outfile, level + 1, name_)
        showIndent(outfile, level)
        outfile.write(unicode("</%s>\n" % name_))

    def exportChildren(
        self, outfile, level, name_="XSDataResultBioSaxsISPyBModellingv1_0"
    ):
        XSDataResult.exportChildren(self, outfile, level, name_)

    def build(self, node_):
        for child_ in node_.childNodes:
            nodeName_ = child_.nodeName.split(":")[-1]
            self.buildChildren(child_, nodeName_)

    def buildChildren(self, child_, nodeName_):
        pass
        XSDataResult.buildChildren(self, child_, nodeName_)

    # Method for marshalling an object
    def marshal(self):
        oStreamString = StringIO()
        oStreamString.write(unicode('<?xml version="1.0" ?>\n'))
        self.export(oStreamString, 0, name_="XSDataResultBioSaxsISPyBModellingv1_0")
        oStringXML = oStreamString.getvalue()
        oStreamString.close()
        return oStringXML

    # Only to export the entire XML tree to a file stream on disk
    def exportToFile(self, _outfileName):
        outfile = open(_outfileName, "w")
        outfile.write(unicode('<?xml version="1.0" ?>\n'))
        self.export(outfile, 0, name_="XSDataResultBioSaxsISPyBModellingv1_0")
        outfile.close()

    # Deprecated method, replaced by exportToFile
    def outputFile(self, _outfileName):
        print(
            "WARNING: Method outputFile in class XSDataResultBioSaxsISPyBModellingv1_0 is deprecated, please use instead exportToFile!"
        )
        self.exportToFile(_outfileName)

    # Method for making a copy in a new instance
    def copy(self):
        return XSDataResultBioSaxsISPyBModellingv1_0.parseString(self.marshal())

    # Static method for parsing a string
    def parseString(_inString):
        doc = minidom.parseString(_inString)
        rootNode = doc.documentElement
        rootObj = XSDataResultBioSaxsISPyBModellingv1_0()
        rootObj.build(rootNode)
        # Check that all minOccurs are obeyed by marshalling the created object
        oStreamString = StringIO()
        rootObj.export(oStreamString, 0, name_="XSDataResultBioSaxsISPyBModellingv1_0")
        oStreamString.close()
        return rootObj

    parseString = staticmethod(parseString)
    # Static method for parsing a file
    def parseFile(_inFilePath):
        doc = minidom.parse(_inFilePath)
        rootNode = doc.documentElement
        rootObj = XSDataResultBioSaxsISPyBModellingv1_0()
        rootObj.build(rootNode)
        return rootObj

    parseFile = staticmethod(parseFile)


# end class XSDataResultBioSaxsISPyBModellingv1_0


class XSDataResultBioSaxsISPyB_HPLCv1_0(XSDataResult):
    def __init__(self, status=None, experimentId=None, sample=None):
        XSDataResult.__init__(self, status)
        if sample is None:
            self._sample = None
        elif sample.__class__.__name__ == "XSDataBioSaxsSample":
            self._sample = sample
        else:
            strMessage = (
                "ERROR! XSDataResultBioSaxsISPyB_HPLCv1_0 constructor argument 'sample' is not XSDataBioSaxsSample but %s"
                % self._sample.__class__.__name__
            )
            raise BaseException(strMessage)
        if experimentId is None:
            self._experimentId = None
        elif experimentId.__class__.__name__ == "XSDataInteger":
            self._experimentId = experimentId
        else:
            strMessage = (
                "ERROR! XSDataResultBioSaxsISPyB_HPLCv1_0 constructor argument 'experimentId' is not XSDataInteger but %s"
                % self._experimentId.__class__.__name__
            )
            raise BaseException(strMessage)

    # Methods and properties for the 'sample' attribute
    def getSample(self):
        return self._sample

    def setSample(self, sample):
        if sample is None:
            self._sample = None
        elif sample.__class__.__name__ == "XSDataBioSaxsSample":
            self._sample = sample
        else:
            strMessage = (
                "ERROR! XSDataResultBioSaxsISPyB_HPLCv1_0.setSample argument is not XSDataBioSaxsSample but %s"
                % sample.__class__.__name__
            )
            raise BaseException(strMessage)

    def delSample(self):
        self._sample = None

    sample = property(getSample, setSample, delSample, "Property for sample")
    # Methods and properties for the 'experimentId' attribute
    def getExperimentId(self):
        return self._experimentId

    def setExperimentId(self, experimentId):
        if experimentId is None:
            self._experimentId = None
        elif experimentId.__class__.__name__ == "XSDataInteger":
            self._experimentId = experimentId
        else:
            strMessage = (
                "ERROR! XSDataResultBioSaxsISPyB_HPLCv1_0.setExperimentId argument is not XSDataInteger but %s"
                % experimentId.__class__.__name__
            )
            raise BaseException(strMessage)

    def delExperimentId(self):
        self._experimentId = None

    experimentId = property(
        getExperimentId, setExperimentId, delExperimentId, "Property for experimentId"
    )

    def export(self, outfile, level, name_="XSDataResultBioSaxsISPyB_HPLCv1_0"):
        showIndent(outfile, level)
        outfile.write(unicode("<%s>\n" % name_))
        self.exportChildren(outfile, level + 1, name_)
        showIndent(outfile, level)
        outfile.write(unicode("</%s>\n" % name_))

    def exportChildren(self, outfile, level, name_="XSDataResultBioSaxsISPyB_HPLCv1_0"):
        XSDataResult.exportChildren(self, outfile, level, name_)
        if self._sample is not None:
            self.sample.export(outfile, level, name_="sample")
        else:
            warnEmptyAttribute("sample", "XSDataBioSaxsSample")
        if self._experimentId is not None:
            self.experimentId.export(outfile, level, name_="experimentId")
        else:
            warnEmptyAttribute("experimentId", "XSDataInteger")

    def build(self, node_):
        for child_ in node_.childNodes:
            nodeName_ = child_.nodeName.split(":")[-1]
            self.buildChildren(child_, nodeName_)

    def buildChildren(self, child_, nodeName_):
        if child_.nodeType == Node.ELEMENT_NODE and nodeName_ == "sample":
            obj_ = XSDataBioSaxsSample()
            obj_.build(child_)
            self.setSample(obj_)
        elif child_.nodeType == Node.ELEMENT_NODE and nodeName_ == "experimentId":
            obj_ = XSDataInteger()
            obj_.build(child_)
            self.setExperimentId(obj_)
        XSDataResult.buildChildren(self, child_, nodeName_)

    # Method for marshalling an object
    def marshal(self):
        oStreamString = StringIO()
        oStreamString.write(unicode('<?xml version="1.0" ?>\n'))
        self.export(oStreamString, 0, name_="XSDataResultBioSaxsISPyB_HPLCv1_0")
        oStringXML = oStreamString.getvalue()
        oStreamString.close()
        return oStringXML

    # Only to export the entire XML tree to a file stream on disk
    def exportToFile(self, _outfileName):
        outfile = open(_outfileName, "w")
        outfile.write(unicode('<?xml version="1.0" ?>\n'))
        self.export(outfile, 0, name_="XSDataResultBioSaxsISPyB_HPLCv1_0")
        outfile.close()

    # Deprecated method, replaced by exportToFile
    def outputFile(self, _outfileName):
        print(
            "WARNING: Method outputFile in class XSDataResultBioSaxsISPyB_HPLCv1_0 is deprecated, please use instead exportToFile!"
        )
        self.exportToFile(_outfileName)

    # Method for making a copy in a new instance
    def copy(self):
        return XSDataResultBioSaxsISPyB_HPLCv1_0.parseString(self.marshal())

    # Static method for parsing a string
    def parseString(_inString):
        doc = minidom.parseString(_inString)
        rootNode = doc.documentElement
        rootObj = XSDataResultBioSaxsISPyB_HPLCv1_0()
        rootObj.build(rootNode)
        # Check that all minOccurs are obeyed by marshalling the created object
        oStreamString = StringIO()
        rootObj.export(oStreamString, 0, name_="XSDataResultBioSaxsISPyB_HPLCv1_0")
        oStreamString.close()
        return rootObj

    parseString = staticmethod(parseString)
    # Static method for parsing a file
    def parseFile(_inFilePath):
        doc = minidom.parse(_inFilePath)
        rootNode = doc.documentElement
        rootObj = XSDataResultBioSaxsISPyB_HPLCv1_0()
        rootObj.build(rootNode)
        return rootObj

    parseFile = staticmethod(parseFile)


# end class XSDataResultBioSaxsISPyB_HPLCv1_0


class XSDataResultBioSaxsISPyBv1_0(XSDataResult):
    def __init__(self, status=None):
        XSDataResult.__init__(self, status)

    def export(self, outfile, level, name_="XSDataResultBioSaxsISPyBv1_0"):
        showIndent(outfile, level)
        outfile.write(unicode("<%s>\n" % name_))
        self.exportChildren(outfile, level + 1, name_)
        showIndent(outfile, level)
        outfile.write(unicode("</%s>\n" % name_))

    def exportChildren(self, outfile, level, name_="XSDataResultBioSaxsISPyBv1_0"):
        XSDataResult.exportChildren(self, outfile, level, name_)

    def build(self, node_):
        for child_ in node_.childNodes:
            nodeName_ = child_.nodeName.split(":")[-1]
            self.buildChildren(child_, nodeName_)

    def buildChildren(self, child_, nodeName_):
        pass
        XSDataResult.buildChildren(self, child_, nodeName_)

    # Method for marshalling an object
    def marshal(self):
        oStreamString = StringIO()
        oStreamString.write(unicode('<?xml version="1.0" ?>\n'))
        self.export(oStreamString, 0, name_="XSDataResultBioSaxsISPyBv1_0")
        oStringXML = oStreamString.getvalue()
        oStreamString.close()
        return oStringXML

    # Only to export the entire XML tree to a file stream on disk
    def exportToFile(self, _outfileName):
        outfile = open(_outfileName, "w")
        outfile.write(unicode('<?xml version="1.0" ?>\n'))
        self.export(outfile, 0, name_="XSDataResultBioSaxsISPyBv1_0")
        outfile.close()

    # Deprecated method, replaced by exportToFile
    def outputFile(self, _outfileName):
        print(
            "WARNING: Method outputFile in class XSDataResultBioSaxsISPyBv1_0 is deprecated, please use instead exportToFile!"
        )
        self.exportToFile(_outfileName)

    # Method for making a copy in a new instance
    def copy(self):
        return XSDataResultBioSaxsISPyBv1_0.parseString(self.marshal())

    # Static method for parsing a string
    def parseString(_inString):
        doc = minidom.parseString(_inString)
        rootNode = doc.documentElement
        rootObj = XSDataResultBioSaxsISPyBv1_0()
        rootObj.build(rootNode)
        # Check that all minOccurs are obeyed by marshalling the created object
        oStreamString = StringIO()
        rootObj.export(oStreamString, 0, name_="XSDataResultBioSaxsISPyBv1_0")
        oStreamString.close()
        return rootObj

    parseString = staticmethod(parseString)
    # Static method for parsing a file
    def parseFile(_inFilePath):
        doc = minidom.parse(_inFilePath)
        rootNode = doc.documentElement
        rootObj = XSDataResultBioSaxsISPyBv1_0()
        rootObj.build(rootNode)
        return rootObj

    parseFile = staticmethod(parseFile)


# end class XSDataResultBioSaxsISPyBv1_0


class XSDataResultBioSaxsNormalizev1_0(XSDataResult):
    def __init__(
        self, status=None, processLog=None, logFile=None, normalizedImage=None
    ):
        XSDataResult.__init__(self, status)
        if normalizedImage is None:
            self._normalizedImage = None
        elif normalizedImage.__class__.__name__ == "XSDataImage":
            self._normalizedImage = normalizedImage
        else:
            strMessage = (
                "ERROR! XSDataResultBioSaxsNormalizev1_0 constructor argument 'normalizedImage' is not XSDataImage but %s"
                % self._normalizedImage.__class__.__name__
            )
            raise BaseException(strMessage)
        if logFile is None:
            self._logFile = None
        elif logFile.__class__.__name__ == "XSDataFile":
            self._logFile = logFile
        else:
            strMessage = (
                "ERROR! XSDataResultBioSaxsNormalizev1_0 constructor argument 'logFile' is not XSDataFile but %s"
                % self._logFile.__class__.__name__
            )
            raise BaseException(strMessage)
        if processLog is None:
            self._processLog = None
        elif processLog.__class__.__name__ == "XSDataString":
            self._processLog = processLog
        else:
            strMessage = (
                "ERROR! XSDataResultBioSaxsNormalizev1_0 constructor argument 'processLog' is not XSDataString but %s"
                % self._processLog.__class__.__name__
            )
            raise BaseException(strMessage)

    # Methods and properties for the 'normalizedImage' attribute
    def getNormalizedImage(self):
        return self._normalizedImage

    def setNormalizedImage(self, normalizedImage):
        if normalizedImage is None:
            self._normalizedImage = None
        elif normalizedImage.__class__.__name__ == "XSDataImage":
            self._normalizedImage = normalizedImage
        else:
            strMessage = (
                "ERROR! XSDataResultBioSaxsNormalizev1_0.setNormalizedImage argument is not XSDataImage but %s"
                % normalizedImage.__class__.__name__
            )
            raise BaseException(strMessage)

    def delNormalizedImage(self):
        self._normalizedImage = None

    normalizedImage = property(
        getNormalizedImage,
        setNormalizedImage,
        delNormalizedImage,
        "Property for normalizedImage",
    )
    # Methods and properties for the 'logFile' attribute
    def getLogFile(self):
        return self._logFile

    def setLogFile(self, logFile):
        if logFile is None:
            self._logFile = None
        elif logFile.__class__.__name__ == "XSDataFile":
            self._logFile = logFile
        else:
            strMessage = (
                "ERROR! XSDataResultBioSaxsNormalizev1_0.setLogFile argument is not XSDataFile but %s"
                % logFile.__class__.__name__
            )
            raise BaseException(strMessage)

    def delLogFile(self):
        self._logFile = None

    logFile = property(getLogFile, setLogFile, delLogFile, "Property for logFile")
    # Methods and properties for the 'processLog' attribute
    def getProcessLog(self):
        return self._processLog

    def setProcessLog(self, processLog):
        if processLog is None:
            self._processLog = None
        elif processLog.__class__.__name__ == "XSDataString":
            self._processLog = processLog
        else:
            strMessage = (
                "ERROR! XSDataResultBioSaxsNormalizev1_0.setProcessLog argument is not XSDataString but %s"
                % processLog.__class__.__name__
            )
            raise BaseException(strMessage)

    def delProcessLog(self):
        self._processLog = None

    processLog = property(
        getProcessLog, setProcessLog, delProcessLog, "Property for processLog"
    )

    def export(self, outfile, level, name_="XSDataResultBioSaxsNormalizev1_0"):
        showIndent(outfile, level)
        outfile.write(unicode("<%s>\n" % name_))
        self.exportChildren(outfile, level + 1, name_)
        showIndent(outfile, level)
        outfile.write(unicode("</%s>\n" % name_))

    def exportChildren(self, outfile, level, name_="XSDataResultBioSaxsNormalizev1_0"):
        XSDataResult.exportChildren(self, outfile, level, name_)
        if self._normalizedImage is not None:
            self.normalizedImage.export(outfile, level, name_="normalizedImage")
        else:
            warnEmptyAttribute("normalizedImage", "XSDataImage")
        if self._logFile is not None:
            self.logFile.export(outfile, level, name_="logFile")
        else:
            warnEmptyAttribute("logFile", "XSDataFile")
        if self._processLog is not None:
            self.processLog.export(outfile, level, name_="processLog")
        else:
            warnEmptyAttribute("processLog", "XSDataString")

    def build(self, node_):
        for child_ in node_.childNodes:
            nodeName_ = child_.nodeName.split(":")[-1]
            self.buildChildren(child_, nodeName_)

    def buildChildren(self, child_, nodeName_):
        if child_.nodeType == Node.ELEMENT_NODE and nodeName_ == "normalizedImage":
            obj_ = XSDataImage()
            obj_.build(child_)
            self.setNormalizedImage(obj_)
        elif child_.nodeType == Node.ELEMENT_NODE and nodeName_ == "logFile":
            obj_ = XSDataFile()
            obj_.build(child_)
            self.setLogFile(obj_)
        elif child_.nodeType == Node.ELEMENT_NODE and nodeName_ == "processLog":
            obj_ = XSDataString()
            obj_.build(child_)
            self.setProcessLog(obj_)
        XSDataResult.buildChildren(self, child_, nodeName_)

    # Method for marshalling an object
    def marshal(self):
        oStreamString = StringIO()
        oStreamString.write(unicode('<?xml version="1.0" ?>\n'))
        self.export(oStreamString, 0, name_="XSDataResultBioSaxsNormalizev1_0")
        oStringXML = oStreamString.getvalue()
        oStreamString.close()
        return oStringXML

    # Only to export the entire XML tree to a file stream on disk
    def exportToFile(self, _outfileName):
        outfile = open(_outfileName, "w")
        outfile.write(unicode('<?xml version="1.0" ?>\n'))
        self.export(outfile, 0, name_="XSDataResultBioSaxsNormalizev1_0")
        outfile.close()

    # Deprecated method, replaced by exportToFile
    def outputFile(self, _outfileName):
        print(
            "WARNING: Method outputFile in class XSDataResultBioSaxsNormalizev1_0 is deprecated, please use instead exportToFile!"
        )
        self.exportToFile(_outfileName)

    # Method for making a copy in a new instance
    def copy(self):
        return XSDataResultBioSaxsNormalizev1_0.parseString(self.marshal())

    # Static method for parsing a string
    def parseString(_inString):
        doc = minidom.parseString(_inString)
        rootNode = doc.documentElement
        rootObj = XSDataResultBioSaxsNormalizev1_0()
        rootObj.build(rootNode)
        # Check that all minOccurs are obeyed by marshalling the created object
        oStreamString = StringIO()
        rootObj.export(oStreamString, 0, name_="XSDataResultBioSaxsNormalizev1_0")
        oStreamString.close()
        return rootObj

    parseString = staticmethod(parseString)
    # Static method for parsing a file
    def parseFile(_inFilePath):
        doc = minidom.parse(_inFilePath)
        rootNode = doc.documentElement
        rootObj = XSDataResultBioSaxsNormalizev1_0()
        rootObj.build(rootNode)
        return rootObj

    parseFile = staticmethod(parseFile)


# end class XSDataResultBioSaxsNormalizev1_0


class XSDataResultBioSaxsProcessOneFilev1_0(XSDataResult):
    def __init__(
        self,
        status=None,
        dataStdErr=None,
        dataI=None,
        dataQ=None,
        experimentSetup=None,
        sample=None,
        integratedCurve=None,
        integratedImage=None,
        normalizedImage=None,
    ):
        XSDataResult.__init__(self, status)
        if normalizedImage is None:
            self._normalizedImage = None
        elif normalizedImage.__class__.__name__ == "XSDataImage":
            self._normalizedImage = normalizedImage
        else:
            strMessage = (
                "ERROR! XSDataResultBioSaxsProcessOneFilev1_0 constructor argument 'normalizedImage' is not XSDataImage but %s"
                % self._normalizedImage.__class__.__name__
            )
            raise BaseException(strMessage)
        if integratedImage is None:
            self._integratedImage = None
        elif integratedImage.__class__.__name__ == "XSDataImage":
            self._integratedImage = integratedImage
        else:
            strMessage = (
                "ERROR! XSDataResultBioSaxsProcessOneFilev1_0 constructor argument 'integratedImage' is not XSDataImage but %s"
                % self._integratedImage.__class__.__name__
            )
            raise BaseException(strMessage)
        if integratedCurve is None:
            self._integratedCurve = None
        elif integratedCurve.__class__.__name__ == "XSDataFile":
            self._integratedCurve = integratedCurve
        else:
            strMessage = (
                "ERROR! XSDataResultBioSaxsProcessOneFilev1_0 constructor argument 'integratedCurve' is not XSDataFile but %s"
                % self._integratedCurve.__class__.__name__
            )
            raise BaseException(strMessage)
        if sample is None:
            self._sample = None
        elif sample.__class__.__name__ == "XSDataBioSaxsSample":
            self._sample = sample
        else:
            strMessage = (
                "ERROR! XSDataResultBioSaxsProcessOneFilev1_0 constructor argument 'sample' is not XSDataBioSaxsSample but %s"
                % self._sample.__class__.__name__
            )
            raise BaseException(strMessage)
        if experimentSetup is None:
            self._experimentSetup = None
        elif experimentSetup.__class__.__name__ == "XSDataBioSaxsExperimentSetup":
            self._experimentSetup = experimentSetup
        else:
            strMessage = (
                "ERROR! XSDataResultBioSaxsProcessOneFilev1_0 constructor argument 'experimentSetup' is not XSDataBioSaxsExperimentSetup but %s"
                % self._experimentSetup.__class__.__name__
            )
            raise BaseException(strMessage)
        if dataQ is None:
            self._dataQ = None
        elif dataQ.__class__.__name__ == "XSDataArray":
            self._dataQ = dataQ
        else:
            strMessage = (
                "ERROR! XSDataResultBioSaxsProcessOneFilev1_0 constructor argument 'dataQ' is not XSDataArray but %s"
                % self._dataQ.__class__.__name__
            )
            raise BaseException(strMessage)
        if dataI is None:
            self._dataI = None
        elif dataI.__class__.__name__ == "XSDataArray":
            self._dataI = dataI
        else:
            strMessage = (
                "ERROR! XSDataResultBioSaxsProcessOneFilev1_0 constructor argument 'dataI' is not XSDataArray but %s"
                % self._dataI.__class__.__name__
            )
            raise BaseException(strMessage)
        if dataStdErr is None:
            self._dataStdErr = None
        elif dataStdErr.__class__.__name__ == "XSDataArray":
            self._dataStdErr = dataStdErr
        else:
            strMessage = (
                "ERROR! XSDataResultBioSaxsProcessOneFilev1_0 constructor argument 'dataStdErr' is not XSDataArray but %s"
                % self._dataStdErr.__class__.__name__
            )
            raise BaseException(strMessage)

    # Methods and properties for the 'normalizedImage' attribute
    def getNormalizedImage(self):
        return self._normalizedImage

    def setNormalizedImage(self, normalizedImage):
        if normalizedImage is None:
            self._normalizedImage = None
        elif normalizedImage.__class__.__name__ == "XSDataImage":
            self._normalizedImage = normalizedImage
        else:
            strMessage = (
                "ERROR! XSDataResultBioSaxsProcessOneFilev1_0.setNormalizedImage argument is not XSDataImage but %s"
                % normalizedImage.__class__.__name__
            )
            raise BaseException(strMessage)

    def delNormalizedImage(self):
        self._normalizedImage = None

    normalizedImage = property(
        getNormalizedImage,
        setNormalizedImage,
        delNormalizedImage,
        "Property for normalizedImage",
    )
    # Methods and properties for the 'integratedImage' attribute
    def getIntegratedImage(self):
        return self._integratedImage

    def setIntegratedImage(self, integratedImage):
        if integratedImage is None:
            self._integratedImage = None
        elif integratedImage.__class__.__name__ == "XSDataImage":
            self._integratedImage = integratedImage
        else:
            strMessage = (
                "ERROR! XSDataResultBioSaxsProcessOneFilev1_0.setIntegratedImage argument is not XSDataImage but %s"
                % integratedImage.__class__.__name__
            )
            raise BaseException(strMessage)

    def delIntegratedImage(self):
        self._integratedImage = None

    integratedImage = property(
        getIntegratedImage,
        setIntegratedImage,
        delIntegratedImage,
        "Property for integratedImage",
    )
    # Methods and properties for the 'integratedCurve' attribute
    def getIntegratedCurve(self):
        return self._integratedCurve

    def setIntegratedCurve(self, integratedCurve):
        if integratedCurve is None:
            self._integratedCurve = None
        elif integratedCurve.__class__.__name__ == "XSDataFile":
            self._integratedCurve = integratedCurve
        else:
            strMessage = (
                "ERROR! XSDataResultBioSaxsProcessOneFilev1_0.setIntegratedCurve argument is not XSDataFile but %s"
                % integratedCurve.__class__.__name__
            )
            raise BaseException(strMessage)

    def delIntegratedCurve(self):
        self._integratedCurve = None

    integratedCurve = property(
        getIntegratedCurve,
        setIntegratedCurve,
        delIntegratedCurve,
        "Property for integratedCurve",
    )
    # Methods and properties for the 'sample' attribute
    def getSample(self):
        return self._sample

    def setSample(self, sample):
        if sample is None:
            self._sample = None
        elif sample.__class__.__name__ == "XSDataBioSaxsSample":
            self._sample = sample
        else:
            strMessage = (
                "ERROR! XSDataResultBioSaxsProcessOneFilev1_0.setSample argument is not XSDataBioSaxsSample but %s"
                % sample.__class__.__name__
            )
            raise BaseException(strMessage)

    def delSample(self):
        self._sample = None

    sample = property(getSample, setSample, delSample, "Property for sample")
    # Methods and properties for the 'experimentSetup' attribute
    def getExperimentSetup(self):
        return self._experimentSetup

    def setExperimentSetup(self, experimentSetup):
        if experimentSetup is None:
            self._experimentSetup = None
        elif experimentSetup.__class__.__name__ == "XSDataBioSaxsExperimentSetup":
            self._experimentSetup = experimentSetup
        else:
            strMessage = (
                "ERROR! XSDataResultBioSaxsProcessOneFilev1_0.setExperimentSetup argument is not XSDataBioSaxsExperimentSetup but %s"
                % experimentSetup.__class__.__name__
            )
            raise BaseException(strMessage)

    def delExperimentSetup(self):
        self._experimentSetup = None

    experimentSetup = property(
        getExperimentSetup,
        setExperimentSetup,
        delExperimentSetup,
        "Property for experimentSetup",
    )
    # Methods and properties for the 'dataQ' attribute
    def getDataQ(self):
        return self._dataQ

    def setDataQ(self, dataQ):
        if dataQ is None:
            self._dataQ = None
        elif dataQ.__class__.__name__ == "XSDataArray":
            self._dataQ = dataQ
        else:
            strMessage = (
                "ERROR! XSDataResultBioSaxsProcessOneFilev1_0.setDataQ argument is not XSDataArray but %s"
                % dataQ.__class__.__name__
            )
            raise BaseException(strMessage)

    def delDataQ(self):
        self._dataQ = None

    dataQ = property(getDataQ, setDataQ, delDataQ, "Property for dataQ")
    # Methods and properties for the 'dataI' attribute
    def getDataI(self):
        return self._dataI

    def setDataI(self, dataI):
        if dataI is None:
            self._dataI = None
        elif dataI.__class__.__name__ == "XSDataArray":
            self._dataI = dataI
        else:
            strMessage = (
                "ERROR! XSDataResultBioSaxsProcessOneFilev1_0.setDataI argument is not XSDataArray but %s"
                % dataI.__class__.__name__
            )
            raise BaseException(strMessage)

    def delDataI(self):
        self._dataI = None

    dataI = property(getDataI, setDataI, delDataI, "Property for dataI")
    # Methods and properties for the 'dataStdErr' attribute
    def getDataStdErr(self):
        return self._dataStdErr

    def setDataStdErr(self, dataStdErr):
        if dataStdErr is None:
            self._dataStdErr = None
        elif dataStdErr.__class__.__name__ == "XSDataArray":
            self._dataStdErr = dataStdErr
        else:
            strMessage = (
                "ERROR! XSDataResultBioSaxsProcessOneFilev1_0.setDataStdErr argument is not XSDataArray but %s"
                % dataStdErr.__class__.__name__
            )
            raise BaseException(strMessage)

    def delDataStdErr(self):
        self._dataStdErr = None

    dataStdErr = property(
        getDataStdErr, setDataStdErr, delDataStdErr, "Property for dataStdErr"
    )

    def export(self, outfile, level, name_="XSDataResultBioSaxsProcessOneFilev1_0"):
        showIndent(outfile, level)
        outfile.write(unicode("<%s>\n" % name_))
        self.exportChildren(outfile, level + 1, name_)
        showIndent(outfile, level)
        outfile.write(unicode("</%s>\n" % name_))

    def exportChildren(
        self, outfile, level, name_="XSDataResultBioSaxsProcessOneFilev1_0"
    ):
        XSDataResult.exportChildren(self, outfile, level, name_)
        if self._normalizedImage is not None:
            self.normalizedImage.export(outfile, level, name_="normalizedImage")
        if self._integratedImage is not None:
            self.integratedImage.export(outfile, level, name_="integratedImage")
        if self._integratedCurve is not None:
            self.integratedCurve.export(outfile, level, name_="integratedCurve")
        else:
            warnEmptyAttribute("integratedCurve", "XSDataFile")
        if self._sample is not None:
            self.sample.export(outfile, level, name_="sample")
        if self._experimentSetup is not None:
            self.experimentSetup.export(outfile, level, name_="experimentSetup")
        if self._dataQ is not None:
            self.dataQ.export(outfile, level, name_="dataQ")
        if self._dataI is not None:
            self.dataI.export(outfile, level, name_="dataI")
        if self._dataStdErr is not None:
            self.dataStdErr.export(outfile, level, name_="dataStdErr")

    def build(self, node_):
        for child_ in node_.childNodes:
            nodeName_ = child_.nodeName.split(":")[-1]
            self.buildChildren(child_, nodeName_)

    def buildChildren(self, child_, nodeName_):
        if child_.nodeType == Node.ELEMENT_NODE and nodeName_ == "normalizedImage":
            obj_ = XSDataImage()
            obj_.build(child_)
            self.setNormalizedImage(obj_)
        elif child_.nodeType == Node.ELEMENT_NODE and nodeName_ == "integratedImage":
            obj_ = XSDataImage()
            obj_.build(child_)
            self.setIntegratedImage(obj_)
        elif child_.nodeType == Node.ELEMENT_NODE and nodeName_ == "integratedCurve":
            obj_ = XSDataFile()
            obj_.build(child_)
            self.setIntegratedCurve(obj_)
        elif child_.nodeType == Node.ELEMENT_NODE and nodeName_ == "sample":
            obj_ = XSDataBioSaxsSample()
            obj_.build(child_)
            self.setSample(obj_)
        elif child_.nodeType == Node.ELEMENT_NODE and nodeName_ == "experimentSetup":
            obj_ = XSDataBioSaxsExperimentSetup()
            obj_.build(child_)
            self.setExperimentSetup(obj_)
        elif child_.nodeType == Node.ELEMENT_NODE and nodeName_ == "dataQ":
            obj_ = XSDataArray()
            obj_.build(child_)
            self.setDataQ(obj_)
        elif child_.nodeType == Node.ELEMENT_NODE and nodeName_ == "dataI":
            obj_ = XSDataArray()
            obj_.build(child_)
            self.setDataI(obj_)
        elif child_.nodeType == Node.ELEMENT_NODE and nodeName_ == "dataStdErr":
            obj_ = XSDataArray()
            obj_.build(child_)
            self.setDataStdErr(obj_)
        XSDataResult.buildChildren(self, child_, nodeName_)

    # Method for marshalling an object
    def marshal(self):
        oStreamString = StringIO()
        oStreamString.write(unicode('<?xml version="1.0" ?>\n'))
        self.export(oStreamString, 0, name_="XSDataResultBioSaxsProcessOneFilev1_0")
        oStringXML = oStreamString.getvalue()
        oStreamString.close()
        return oStringXML

    # Only to export the entire XML tree to a file stream on disk
    def exportToFile(self, _outfileName):
        outfile = open(_outfileName, "w")
        outfile.write(unicode('<?xml version="1.0" ?>\n'))
        self.export(outfile, 0, name_="XSDataResultBioSaxsProcessOneFilev1_0")
        outfile.close()

    # Deprecated method, replaced by exportToFile
    def outputFile(self, _outfileName):
        print(
            "WARNING: Method outputFile in class XSDataResultBioSaxsProcessOneFilev1_0 is deprecated, please use instead exportToFile!"
        )
        self.exportToFile(_outfileName)

    # Method for making a copy in a new instance
    def copy(self):
        return XSDataResultBioSaxsProcessOneFilev1_0.parseString(self.marshal())

    # Static method for parsing a string
    def parseString(_inString):
        doc = minidom.parseString(_inString)
        rootNode = doc.documentElement
        rootObj = XSDataResultBioSaxsProcessOneFilev1_0()
        rootObj.build(rootNode)
        # Check that all minOccurs are obeyed by marshalling the created object
        oStreamString = StringIO()
        rootObj.export(oStreamString, 0, name_="XSDataResultBioSaxsProcessOneFilev1_0")
        oStreamString.close()
        return rootObj

    parseString = staticmethod(parseString)
    # Static method for parsing a file
    def parseFile(_inFilePath):
        doc = minidom.parse(_inFilePath)
        rootNode = doc.documentElement
        rootObj = XSDataResultBioSaxsProcessOneFilev1_0()
        rootObj.build(rootNode)
        return rootObj

    parseFile = staticmethod(parseFile)


# end class XSDataResultBioSaxsProcessOneFilev1_0


class XSDataResultBioSaxsReduceFileSeriev1_0(XSDataResult):
    def __init__(
        self,
        status=None,
        directoryMisc=None,
        directory2D=None,
        directory1D=None,
        mergedCurve=None,
    ):
        XSDataResult.__init__(self, status)
        if mergedCurve is None:
            self._mergedCurve = None
        elif mergedCurve.__class__.__name__ == "XSDataFile":
            self._mergedCurve = mergedCurve
        else:
            strMessage = (
                "ERROR! XSDataResultBioSaxsReduceFileSeriev1_0 constructor argument 'mergedCurve' is not XSDataFile but %s"
                % self._mergedCurve.__class__.__name__
            )
            raise BaseException(strMessage)
        if directory1D is None:
            self._directory1D = None
        elif directory1D.__class__.__name__ == "XSDataFile":
            self._directory1D = directory1D
        else:
            strMessage = (
                "ERROR! XSDataResultBioSaxsReduceFileSeriev1_0 constructor argument 'directory1D' is not XSDataFile but %s"
                % self._directory1D.__class__.__name__
            )
            raise BaseException(strMessage)
        if directory2D is None:
            self._directory2D = None
        elif directory2D.__class__.__name__ == "XSDataFile":
            self._directory2D = directory2D
        else:
            strMessage = (
                "ERROR! XSDataResultBioSaxsReduceFileSeriev1_0 constructor argument 'directory2D' is not XSDataFile but %s"
                % self._directory2D.__class__.__name__
            )
            raise BaseException(strMessage)
        if directoryMisc is None:
            self._directoryMisc = None
        elif directoryMisc.__class__.__name__ == "XSDataFile":
            self._directoryMisc = directoryMisc
        else:
            strMessage = (
                "ERROR! XSDataResultBioSaxsReduceFileSeriev1_0 constructor argument 'directoryMisc' is not XSDataFile but %s"
                % self._directoryMisc.__class__.__name__
            )
            raise BaseException(strMessage)

    # Methods and properties for the 'mergedCurve' attribute
    def getMergedCurve(self):
        return self._mergedCurve

    def setMergedCurve(self, mergedCurve):
        if mergedCurve is None:
            self._mergedCurve = None
        elif mergedCurve.__class__.__name__ == "XSDataFile":
            self._mergedCurve = mergedCurve
        else:
            strMessage = (
                "ERROR! XSDataResultBioSaxsReduceFileSeriev1_0.setMergedCurve argument is not XSDataFile but %s"
                % mergedCurve.__class__.__name__
            )
            raise BaseException(strMessage)

    def delMergedCurve(self):
        self._mergedCurve = None

    mergedCurve = property(
        getMergedCurve, setMergedCurve, delMergedCurve, "Property for mergedCurve"
    )
    # Methods and properties for the 'directory1D' attribute
    def getDirectory1D(self):
        return self._directory1D

    def setDirectory1D(self, directory1D):
        if directory1D is None:
            self._directory1D = None
        elif directory1D.__class__.__name__ == "XSDataFile":
            self._directory1D = directory1D
        else:
            strMessage = (
                "ERROR! XSDataResultBioSaxsReduceFileSeriev1_0.setDirectory1D argument is not XSDataFile but %s"
                % directory1D.__class__.__name__
            )
            raise BaseException(strMessage)

    def delDirectory1D(self):
        self._directory1D = None

    directory1D = property(
        getDirectory1D, setDirectory1D, delDirectory1D, "Property for directory1D"
    )
    # Methods and properties for the 'directory2D' attribute
    def getDirectory2D(self):
        return self._directory2D

    def setDirectory2D(self, directory2D):
        if directory2D is None:
            self._directory2D = None
        elif directory2D.__class__.__name__ == "XSDataFile":
            self._directory2D = directory2D
        else:
            strMessage = (
                "ERROR! XSDataResultBioSaxsReduceFileSeriev1_0.setDirectory2D argument is not XSDataFile but %s"
                % directory2D.__class__.__name__
            )
            raise BaseException(strMessage)

    def delDirectory2D(self):
        self._directory2D = None

    directory2D = property(
        getDirectory2D, setDirectory2D, delDirectory2D, "Property for directory2D"
    )
    # Methods and properties for the 'directoryMisc' attribute
    def getDirectoryMisc(self):
        return self._directoryMisc

    def setDirectoryMisc(self, directoryMisc):
        if directoryMisc is None:
            self._directoryMisc = None
        elif directoryMisc.__class__.__name__ == "XSDataFile":
            self._directoryMisc = directoryMisc
        else:
            strMessage = (
                "ERROR! XSDataResultBioSaxsReduceFileSeriev1_0.setDirectoryMisc argument is not XSDataFile but %s"
                % directoryMisc.__class__.__name__
            )
            raise BaseException(strMessage)

    def delDirectoryMisc(self):
        self._directoryMisc = None

    directoryMisc = property(
        getDirectoryMisc,
        setDirectoryMisc,
        delDirectoryMisc,
        "Property for directoryMisc",
    )

    def export(self, outfile, level, name_="XSDataResultBioSaxsReduceFileSeriev1_0"):
        showIndent(outfile, level)
        outfile.write(unicode("<%s>\n" % name_))
        self.exportChildren(outfile, level + 1, name_)
        showIndent(outfile, level)
        outfile.write(unicode("</%s>\n" % name_))

    def exportChildren(
        self, outfile, level, name_="XSDataResultBioSaxsReduceFileSeriev1_0"
    ):
        XSDataResult.exportChildren(self, outfile, level, name_)
        if self._mergedCurve is not None:
            self.mergedCurve.export(outfile, level, name_="mergedCurve")
        else:
            warnEmptyAttribute("mergedCurve", "XSDataFile")
        if self._directory1D is not None:
            self.directory1D.export(outfile, level, name_="directory1D")
        else:
            warnEmptyAttribute("directory1D", "XSDataFile")
        if self._directory2D is not None:
            self.directory2D.export(outfile, level, name_="directory2D")
        else:
            warnEmptyAttribute("directory2D", "XSDataFile")
        if self._directoryMisc is not None:
            self.directoryMisc.export(outfile, level, name_="directoryMisc")
        else:
            warnEmptyAttribute("directoryMisc", "XSDataFile")

    def build(self, node_):
        for child_ in node_.childNodes:
            nodeName_ = child_.nodeName.split(":")[-1]
            self.buildChildren(child_, nodeName_)

    def buildChildren(self, child_, nodeName_):
        if child_.nodeType == Node.ELEMENT_NODE and nodeName_ == "mergedCurve":
            obj_ = XSDataFile()
            obj_.build(child_)
            self.setMergedCurve(obj_)
        elif child_.nodeType == Node.ELEMENT_NODE and nodeName_ == "directory1D":
            obj_ = XSDataFile()
            obj_.build(child_)
            self.setDirectory1D(obj_)
        elif child_.nodeType == Node.ELEMENT_NODE and nodeName_ == "directory2D":
            obj_ = XSDataFile()
            obj_.build(child_)
            self.setDirectory2D(obj_)
        elif child_.nodeType == Node.ELEMENT_NODE and nodeName_ == "directoryMisc":
            obj_ = XSDataFile()
            obj_.build(child_)
            self.setDirectoryMisc(obj_)
        XSDataResult.buildChildren(self, child_, nodeName_)

    # Method for marshalling an object
    def marshal(self):
        oStreamString = StringIO()
        oStreamString.write(unicode('<?xml version="1.0" ?>\n'))
        self.export(oStreamString, 0, name_="XSDataResultBioSaxsReduceFileSeriev1_0")
        oStringXML = oStreamString.getvalue()
        oStreamString.close()
        return oStringXML

    # Only to export the entire XML tree to a file stream on disk
    def exportToFile(self, _outfileName):
        outfile = open(_outfileName, "w")
        outfile.write(unicode('<?xml version="1.0" ?>\n'))
        self.export(outfile, 0, name_="XSDataResultBioSaxsReduceFileSeriev1_0")
        outfile.close()

    # Deprecated method, replaced by exportToFile
    def outputFile(self, _outfileName):
        print(
            "WARNING: Method outputFile in class XSDataResultBioSaxsReduceFileSeriev1_0 is deprecated, please use instead exportToFile!"
        )
        self.exportToFile(_outfileName)

    # Method for making a copy in a new instance
    def copy(self):
        return XSDataResultBioSaxsReduceFileSeriev1_0.parseString(self.marshal())

    # Static method for parsing a string
    def parseString(_inString):
        doc = minidom.parseString(_inString)
        rootNode = doc.documentElement
        rootObj = XSDataResultBioSaxsReduceFileSeriev1_0()
        rootObj.build(rootNode)
        # Check that all minOccurs are obeyed by marshalling the created object
        oStreamString = StringIO()
        rootObj.export(oStreamString, 0, name_="XSDataResultBioSaxsReduceFileSeriev1_0")
        oStreamString.close()
        return rootObj

    parseString = staticmethod(parseString)
    # Static method for parsing a file
    def parseFile(_inFilePath):
        doc = minidom.parse(_inFilePath)
        rootNode = doc.documentElement
        rootObj = XSDataResultBioSaxsReduceFileSeriev1_0()
        rootObj.build(rootNode)
        return rootObj

    parseFile = staticmethod(parseFile)


# end class XSDataResultBioSaxsReduceFileSeriev1_0


class XSDataResultBioSaxsSample(XSDataResult):
    """temporary class for multiple inhertitance emulation"""

    def __init__(self, status=None, code=None, comments=None, concentration=None):
        XSDataResult.__init__(self, status)
        if concentration is None:
            self._concentration = None
        elif concentration.__class__.__name__ == "XSDataDouble":
            self._concentration = concentration
        else:
            strMessage = (
                "ERROR! XSDataResultBioSaxsSample constructor argument 'concentration' is not XSDataDouble but %s"
                % self._concentration.__class__.__name__
            )
            raise BaseException(strMessage)
        if comments is None:
            self._comments = None
        elif comments.__class__.__name__ == "XSDataString":
            self._comments = comments
        else:
            strMessage = (
                "ERROR! XSDataResultBioSaxsSample constructor argument 'comments' is not XSDataString but %s"
                % self._comments.__class__.__name__
            )
            raise BaseException(strMessage)
        if code is None:
            self._code = None
        elif code.__class__.__name__ == "XSDataString":
            self._code = code
        else:
            strMessage = (
                "ERROR! XSDataResultBioSaxsSample constructor argument 'code' is not XSDataString but %s"
                % self._code.__class__.__name__
            )
            raise BaseException(strMessage)

    # Methods and properties for the 'concentration' attribute
    def getConcentration(self):
        return self._concentration

    def setConcentration(self, concentration):
        if concentration is None:
            self._concentration = None
        elif concentration.__class__.__name__ == "XSDataDouble":
            self._concentration = concentration
        else:
            strMessage = (
                "ERROR! XSDataResultBioSaxsSample.setConcentration argument is not XSDataDouble but %s"
                % concentration.__class__.__name__
            )
            raise BaseException(strMessage)

    def delConcentration(self):
        self._concentration = None

    concentration = property(
        getConcentration,
        setConcentration,
        delConcentration,
        "Property for concentration",
    )
    # Methods and properties for the 'comments' attribute
    def getComments(self):
        return self._comments

    def setComments(self, comments):
        if comments is None:
            self._comments = None
        elif comments.__class__.__name__ == "XSDataString":
            self._comments = comments
        else:
            strMessage = (
                "ERROR! XSDataResultBioSaxsSample.setComments argument is not XSDataString but %s"
                % comments.__class__.__name__
            )
            raise BaseException(strMessage)

    def delComments(self):
        self._comments = None

    comments = property(getComments, setComments, delComments, "Property for comments")
    # Methods and properties for the 'code' attribute
    def getCode(self):
        return self._code

    def setCode(self, code):
        if code is None:
            self._code = None
        elif code.__class__.__name__ == "XSDataString":
            self._code = code
        else:
            strMessage = (
                "ERROR! XSDataResultBioSaxsSample.setCode argument is not XSDataString but %s"
                % code.__class__.__name__
            )
            raise BaseException(strMessage)

    def delCode(self):
        self._code = None

    code = property(getCode, setCode, delCode, "Property for code")

    def export(self, outfile, level, name_="XSDataResultBioSaxsSample"):
        showIndent(outfile, level)
        outfile.write(unicode("<%s>\n" % name_))
        self.exportChildren(outfile, level + 1, name_)
        showIndent(outfile, level)
        outfile.write(unicode("</%s>\n" % name_))

    def exportChildren(self, outfile, level, name_="XSDataResultBioSaxsSample"):
        XSDataResult.exportChildren(self, outfile, level, name_)
        if self._concentration is not None:
            self.concentration.export(outfile, level, name_="concentration")
        if self._comments is not None:
            self.comments.export(outfile, level, name_="comments")
        if self._code is not None:
            self.code.export(outfile, level, name_="code")

    def build(self, node_):
        for child_ in node_.childNodes:
            nodeName_ = child_.nodeName.split(":")[-1]
            self.buildChildren(child_, nodeName_)

    def buildChildren(self, child_, nodeName_):
        if child_.nodeType == Node.ELEMENT_NODE and nodeName_ == "concentration":
            obj_ = XSDataDouble()
            obj_.build(child_)
            self.setConcentration(obj_)
        elif child_.nodeType == Node.ELEMENT_NODE and nodeName_ == "comments":
            obj_ = XSDataString()
            obj_.build(child_)
            self.setComments(obj_)
        elif child_.nodeType == Node.ELEMENT_NODE and nodeName_ == "code":
            obj_ = XSDataString()
            obj_.build(child_)
            self.setCode(obj_)
        XSDataResult.buildChildren(self, child_, nodeName_)

    # Method for marshalling an object
    def marshal(self):
        oStreamString = StringIO()
        oStreamString.write(unicode('<?xml version="1.0" ?>\n'))
        self.export(oStreamString, 0, name_="XSDataResultBioSaxsSample")
        oStringXML = oStreamString.getvalue()
        oStreamString.close()
        return oStringXML

    # Only to export the entire XML tree to a file stream on disk
    def exportToFile(self, _outfileName):
        outfile = open(_outfileName, "w")
        outfile.write(unicode('<?xml version="1.0" ?>\n'))
        self.export(outfile, 0, name_="XSDataResultBioSaxsSample")
        outfile.close()

    # Deprecated method, replaced by exportToFile
    def outputFile(self, _outfileName):
        print(
            "WARNING: Method outputFile in class XSDataResultBioSaxsSample is deprecated, please use instead exportToFile!"
        )
        self.exportToFile(_outfileName)

    # Method for making a copy in a new instance
    def copy(self):
        return XSDataResultBioSaxsSample.parseString(self.marshal())

    # Static method for parsing a string
    def parseString(_inString):
        doc = minidom.parseString(_inString)
        rootNode = doc.documentElement
        rootObj = XSDataResultBioSaxsSample()
        rootObj.build(rootNode)
        # Check that all minOccurs are obeyed by marshalling the created object
        oStreamString = StringIO()
        rootObj.export(oStreamString, 0, name_="XSDataResultBioSaxsSample")
        oStreamString.close()
        return rootObj

    parseString = staticmethod(parseString)
    # Static method for parsing a file
    def parseFile(_inFilePath):
        doc = minidom.parse(_inFilePath)
        rootNode = doc.documentElement
        rootObj = XSDataResultBioSaxsSample()
        rootObj.build(rootNode)
        return rootObj

    parseFile = staticmethod(parseFile)


# end class XSDataResultBioSaxsSample


class XSDataResultBioSaxsSingleSamplev1_0(XSDataResult):
    """Class for precessing a single sample (at 1 single concentration)"""

    def __init__(
        self, status=None, directory2D=None, directory1D=None, outputCurve=None
    ):
        XSDataResult.__init__(self, status)
        if outputCurve is None:
            self._outputCurve = None
        elif outputCurve.__class__.__name__ == "XSDataFile":
            self._outputCurve = outputCurve
        else:
            strMessage = (
                "ERROR! XSDataResultBioSaxsSingleSamplev1_0 constructor argument 'outputCurve' is not XSDataFile but %s"
                % self._outputCurve.__class__.__name__
            )
            raise BaseException(strMessage)
        if directory1D is None:
            self._directory1D = None
        elif directory1D.__class__.__name__ == "XSDataFile":
            self._directory1D = directory1D
        else:
            strMessage = (
                "ERROR! XSDataResultBioSaxsSingleSamplev1_0 constructor argument 'directory1D' is not XSDataFile but %s"
                % self._directory1D.__class__.__name__
            )
            raise BaseException(strMessage)
        if directory2D is None:
            self._directory2D = None
        elif directory2D.__class__.__name__ == "XSDataFile":
            self._directory2D = directory2D
        else:
            strMessage = (
                "ERROR! XSDataResultBioSaxsSingleSamplev1_0 constructor argument 'directory2D' is not XSDataFile but %s"
                % self._directory2D.__class__.__name__
            )
            raise BaseException(strMessage)

    # Methods and properties for the 'outputCurve' attribute
    def getOutputCurve(self):
        return self._outputCurve

    def setOutputCurve(self, outputCurve):
        if outputCurve is None:
            self._outputCurve = None
        elif outputCurve.__class__.__name__ == "XSDataFile":
            self._outputCurve = outputCurve
        else:
            strMessage = (
                "ERROR! XSDataResultBioSaxsSingleSamplev1_0.setOutputCurve argument is not XSDataFile but %s"
                % outputCurve.__class__.__name__
            )
            raise BaseException(strMessage)

    def delOutputCurve(self):
        self._outputCurve = None

    outputCurve = property(
        getOutputCurve, setOutputCurve, delOutputCurve, "Property for outputCurve"
    )
    # Methods and properties for the 'directory1D' attribute
    def getDirectory1D(self):
        return self._directory1D

    def setDirectory1D(self, directory1D):
        if directory1D is None:
            self._directory1D = None
        elif directory1D.__class__.__name__ == "XSDataFile":
            self._directory1D = directory1D
        else:
            strMessage = (
                "ERROR! XSDataResultBioSaxsSingleSamplev1_0.setDirectory1D argument is not XSDataFile but %s"
                % directory1D.__class__.__name__
            )
            raise BaseException(strMessage)

    def delDirectory1D(self):
        self._directory1D = None

    directory1D = property(
        getDirectory1D, setDirectory1D, delDirectory1D, "Property for directory1D"
    )
    # Methods and properties for the 'directory2D' attribute
    def getDirectory2D(self):
        return self._directory2D

    def setDirectory2D(self, directory2D):
        if directory2D is None:
            self._directory2D = None
        elif directory2D.__class__.__name__ == "XSDataFile":
            self._directory2D = directory2D
        else:
            strMessage = (
                "ERROR! XSDataResultBioSaxsSingleSamplev1_0.setDirectory2D argument is not XSDataFile but %s"
                % directory2D.__class__.__name__
            )
            raise BaseException(strMessage)

    def delDirectory2D(self):
        self._directory2D = None

    directory2D = property(
        getDirectory2D, setDirectory2D, delDirectory2D, "Property for directory2D"
    )

    def export(self, outfile, level, name_="XSDataResultBioSaxsSingleSamplev1_0"):
        showIndent(outfile, level)
        outfile.write(unicode("<%s>\n" % name_))
        self.exportChildren(outfile, level + 1, name_)
        showIndent(outfile, level)
        outfile.write(unicode("</%s>\n" % name_))

    def exportChildren(
        self, outfile, level, name_="XSDataResultBioSaxsSingleSamplev1_0"
    ):
        XSDataResult.exportChildren(self, outfile, level, name_)
        if self._outputCurve is not None:
            self.outputCurve.export(outfile, level, name_="outputCurve")
        else:
            warnEmptyAttribute("outputCurve", "XSDataFile")
        if self._directory1D is not None:
            self.directory1D.export(outfile, level, name_="directory1D")
        else:
            warnEmptyAttribute("directory1D", "XSDataFile")
        if self._directory2D is not None:
            self.directory2D.export(outfile, level, name_="directory2D")
        else:
            warnEmptyAttribute("directory2D", "XSDataFile")

    def build(self, node_):
        for child_ in node_.childNodes:
            nodeName_ = child_.nodeName.split(":")[-1]
            self.buildChildren(child_, nodeName_)

    def buildChildren(self, child_, nodeName_):
        if child_.nodeType == Node.ELEMENT_NODE and nodeName_ == "outputCurve":
            obj_ = XSDataFile()
            obj_.build(child_)
            self.setOutputCurve(obj_)
        elif child_.nodeType == Node.ELEMENT_NODE and nodeName_ == "directory1D":
            obj_ = XSDataFile()
            obj_.build(child_)
            self.setDirectory1D(obj_)
        elif child_.nodeType == Node.ELEMENT_NODE and nodeName_ == "directory2D":
            obj_ = XSDataFile()
            obj_.build(child_)
            self.setDirectory2D(obj_)
        XSDataResult.buildChildren(self, child_, nodeName_)

    # Method for marshalling an object
    def marshal(self):
        oStreamString = StringIO()
        oStreamString.write(unicode('<?xml version="1.0" ?>\n'))
        self.export(oStreamString, 0, name_="XSDataResultBioSaxsSingleSamplev1_0")
        oStringXML = oStreamString.getvalue()
        oStreamString.close()
        return oStringXML

    # Only to export the entire XML tree to a file stream on disk
    def exportToFile(self, _outfileName):
        outfile = open(_outfileName, "w")
        outfile.write(unicode('<?xml version="1.0" ?>\n'))
        self.export(outfile, 0, name_="XSDataResultBioSaxsSingleSamplev1_0")
        outfile.close()

    # Deprecated method, replaced by exportToFile
    def outputFile(self, _outfileName):
        print(
            "WARNING: Method outputFile in class XSDataResultBioSaxsSingleSamplev1_0 is deprecated, please use instead exportToFile!"
        )
        self.exportToFile(_outfileName)

    # Method for making a copy in a new instance
    def copy(self):
        return XSDataResultBioSaxsSingleSamplev1_0.parseString(self.marshal())

    # Static method for parsing a string
    def parseString(_inString):
        doc = minidom.parseString(_inString)
        rootNode = doc.documentElement
        rootObj = XSDataResultBioSaxsSingleSamplev1_0()
        rootObj.build(rootNode)
        # Check that all minOccurs are obeyed by marshalling the created object
        oStreamString = StringIO()
        rootObj.export(oStreamString, 0, name_="XSDataResultBioSaxsSingleSamplev1_0")
        oStreamString.close()
        return rootObj

    parseString = staticmethod(parseString)
    # Static method for parsing a file
    def parseFile(_inFilePath):
        doc = minidom.parse(_inFilePath)
        rootNode = doc.documentElement
        rootObj = XSDataResultBioSaxsSingleSamplev1_0()
        rootObj.build(rootNode)
        return rootObj

    parseFile = staticmethod(parseFile)


# end class XSDataResultBioSaxsSingleSamplev1_0


class XSDataResultBioSaxsSmartMergev1_0(XSDataResult):
    def __init__(
        self,
        status=None,
        sample=None,
        subtractedCurve=None,
        volume=None,
        gnom=None,
        autoRg=None,
        mergedCurve=None,
    ):
        XSDataResult.__init__(self, status)
        if mergedCurve is None:
            self._mergedCurve = None
        elif mergedCurve.__class__.__name__ == "XSDataFile":
            self._mergedCurve = mergedCurve
        else:
            strMessage = (
                "ERROR! XSDataResultBioSaxsSmartMergev1_0 constructor argument 'mergedCurve' is not XSDataFile but %s"
                % self._mergedCurve.__class__.__name__
            )
            raise BaseException(strMessage)
        if autoRg is None:
            self._autoRg = None
        elif autoRg.__class__.__name__ == "XSDataAutoRg":
            self._autoRg = autoRg
        else:
            strMessage = (
                "ERROR! XSDataResultBioSaxsSmartMergev1_0 constructor argument 'autoRg' is not XSDataAutoRg but %s"
                % self._autoRg.__class__.__name__
            )
            raise BaseException(strMessage)
        if gnom is None:
            self._gnom = None
        elif gnom.__class__.__name__ == "XSDataGnom":
            self._gnom = gnom
        else:
            strMessage = (
                "ERROR! XSDataResultBioSaxsSmartMergev1_0 constructor argument 'gnom' is not XSDataGnom but %s"
                % self._gnom.__class__.__name__
            )
            raise BaseException(strMessage)
        if volume is None:
            self._volume = None
        elif volume.__class__.__name__ == "XSDataDoubleWithUnit":
            self._volume = volume
        else:
            strMessage = (
                "ERROR! XSDataResultBioSaxsSmartMergev1_0 constructor argument 'volume' is not XSDataDoubleWithUnit but %s"
                % self._volume.__class__.__name__
            )
            raise BaseException(strMessage)
        if subtractedCurve is None:
            self._subtractedCurve = None
        elif subtractedCurve.__class__.__name__ == "XSDataFile":
            self._subtractedCurve = subtractedCurve
        else:
            strMessage = (
                "ERROR! XSDataResultBioSaxsSmartMergev1_0 constructor argument 'subtractedCurve' is not XSDataFile but %s"
                % self._subtractedCurve.__class__.__name__
            )
            raise BaseException(strMessage)
        if sample is None:
            self._sample = None
        elif sample.__class__.__name__ == "XSDataBioSaxsSample":
            self._sample = sample
        else:
            strMessage = (
                "ERROR! XSDataResultBioSaxsSmartMergev1_0 constructor argument 'sample' is not XSDataBioSaxsSample but %s"
                % self._sample.__class__.__name__
            )
            raise BaseException(strMessage)

    # Methods and properties for the 'mergedCurve' attribute
    def getMergedCurve(self):
        return self._mergedCurve

    def setMergedCurve(self, mergedCurve):
        if mergedCurve is None:
            self._mergedCurve = None
        elif mergedCurve.__class__.__name__ == "XSDataFile":
            self._mergedCurve = mergedCurve
        else:
            strMessage = (
                "ERROR! XSDataResultBioSaxsSmartMergev1_0.setMergedCurve argument is not XSDataFile but %s"
                % mergedCurve.__class__.__name__
            )
            raise BaseException(strMessage)

    def delMergedCurve(self):
        self._mergedCurve = None

    mergedCurve = property(
        getMergedCurve, setMergedCurve, delMergedCurve, "Property for mergedCurve"
    )
    # Methods and properties for the 'autoRg' attribute
    def getAutoRg(self):
        return self._autoRg

    def setAutoRg(self, autoRg):
        if autoRg is None:
            self._autoRg = None
        elif autoRg.__class__.__name__ == "XSDataAutoRg":
            self._autoRg = autoRg
        else:
            strMessage = (
                "ERROR! XSDataResultBioSaxsSmartMergev1_0.setAutoRg argument is not XSDataAutoRg but %s"
                % autoRg.__class__.__name__
            )
            raise BaseException(strMessage)

    def delAutoRg(self):
        self._autoRg = None

    autoRg = property(getAutoRg, setAutoRg, delAutoRg, "Property for autoRg")
    # Methods and properties for the 'gnom' attribute
    def getGnom(self):
        return self._gnom

    def setGnom(self, gnom):
        if gnom is None:
            self._gnom = None
        elif gnom.__class__.__name__ == "XSDataGnom":
            self._gnom = gnom
        else:
            strMessage = (
                "ERROR! XSDataResultBioSaxsSmartMergev1_0.setGnom argument is not XSDataGnom but %s"
                % gnom.__class__.__name__
            )
            raise BaseException(strMessage)

    def delGnom(self):
        self._gnom = None

    gnom = property(getGnom, setGnom, delGnom, "Property for gnom")
    # Methods and properties for the 'volume' attribute
    def getVolume(self):
        return self._volume

    def setVolume(self, volume):
        if volume is None:
            self._volume = None
        elif volume.__class__.__name__ == "XSDataDoubleWithUnit":
            self._volume = volume
        else:
            strMessage = (
                "ERROR! XSDataResultBioSaxsSmartMergev1_0.setVolume argument is not XSDataDoubleWithUnit but %s"
                % volume.__class__.__name__
            )
            raise BaseException(strMessage)

    def delVolume(self):
        self._volume = None

    volume = property(getVolume, setVolume, delVolume, "Property for volume")
    # Methods and properties for the 'subtractedCurve' attribute
    def getSubtractedCurve(self):
        return self._subtractedCurve

    def setSubtractedCurve(self, subtractedCurve):
        if subtractedCurve is None:
            self._subtractedCurve = None
        elif subtractedCurve.__class__.__name__ == "XSDataFile":
            self._subtractedCurve = subtractedCurve
        else:
            strMessage = (
                "ERROR! XSDataResultBioSaxsSmartMergev1_0.setSubtractedCurve argument is not XSDataFile but %s"
                % subtractedCurve.__class__.__name__
            )
            raise BaseException(strMessage)

    def delSubtractedCurve(self):
        self._subtractedCurve = None

    subtractedCurve = property(
        getSubtractedCurve,
        setSubtractedCurve,
        delSubtractedCurve,
        "Property for subtractedCurve",
    )
    # Methods and properties for the 'sample' attribute
    def getSample(self):
        return self._sample

    def setSample(self, sample):
        if sample is None:
            self._sample = None
        elif sample.__class__.__name__ == "XSDataBioSaxsSample":
            self._sample = sample
        else:
            strMessage = (
                "ERROR! XSDataResultBioSaxsSmartMergev1_0.setSample argument is not XSDataBioSaxsSample but %s"
                % sample.__class__.__name__
            )
            raise BaseException(strMessage)

    def delSample(self):
        self._sample = None

    sample = property(getSample, setSample, delSample, "Property for sample")

    def export(self, outfile, level, name_="XSDataResultBioSaxsSmartMergev1_0"):
        showIndent(outfile, level)
        outfile.write(unicode("<%s>\n" % name_))
        self.exportChildren(outfile, level + 1, name_)
        showIndent(outfile, level)
        outfile.write(unicode("</%s>\n" % name_))

    def exportChildren(self, outfile, level, name_="XSDataResultBioSaxsSmartMergev1_0"):
        XSDataResult.exportChildren(self, outfile, level, name_)
        if self._mergedCurve is not None:
            self.mergedCurve.export(outfile, level, name_="mergedCurve")
        else:
            warnEmptyAttribute("mergedCurve", "XSDataFile")
        if self._autoRg is not None:
            self.autoRg.export(outfile, level, name_="autoRg")
        if self._gnom is not None:
            self.gnom.export(outfile, level, name_="gnom")
        if self._volume is not None:
            self.volume.export(outfile, level, name_="volume")
        if self._subtractedCurve is not None:
            self.subtractedCurve.export(outfile, level, name_="subtractedCurve")
        if self._sample is not None:
            self.sample.export(outfile, level, name_="sample")

    def build(self, node_):
        for child_ in node_.childNodes:
            nodeName_ = child_.nodeName.split(":")[-1]
            self.buildChildren(child_, nodeName_)

    def buildChildren(self, child_, nodeName_):
        if child_.nodeType == Node.ELEMENT_NODE and nodeName_ == "mergedCurve":
            obj_ = XSDataFile()
            obj_.build(child_)
            self.setMergedCurve(obj_)
        elif child_.nodeType == Node.ELEMENT_NODE and nodeName_ == "autoRg":
            obj_ = XSDataAutoRg()
            obj_.build(child_)
            self.setAutoRg(obj_)
        elif child_.nodeType == Node.ELEMENT_NODE and nodeName_ == "gnom":
            obj_ = XSDataGnom()
            obj_.build(child_)
            self.setGnom(obj_)
        elif child_.nodeType == Node.ELEMENT_NODE and nodeName_ == "volume":
            obj_ = XSDataDoubleWithUnit()
            obj_.build(child_)
            self.setVolume(obj_)
        elif child_.nodeType == Node.ELEMENT_NODE and nodeName_ == "subtractedCurve":
            obj_ = XSDataFile()
            obj_.build(child_)
            self.setSubtractedCurve(obj_)
        elif child_.nodeType == Node.ELEMENT_NODE and nodeName_ == "sample":
            obj_ = XSDataBioSaxsSample()
            obj_.build(child_)
            self.setSample(obj_)
        XSDataResult.buildChildren(self, child_, nodeName_)

    # Method for marshalling an object
    def marshal(self):
        oStreamString = StringIO()
        oStreamString.write(unicode('<?xml version="1.0" ?>\n'))
        self.export(oStreamString, 0, name_="XSDataResultBioSaxsSmartMergev1_0")
        oStringXML = oStreamString.getvalue()
        oStreamString.close()
        return oStringXML

    # Only to export the entire XML tree to a file stream on disk
    def exportToFile(self, _outfileName):
        outfile = open(_outfileName, "w")
        outfile.write(unicode('<?xml version="1.0" ?>\n'))
        self.export(outfile, 0, name_="XSDataResultBioSaxsSmartMergev1_0")
        outfile.close()

    # Deprecated method, replaced by exportToFile
    def outputFile(self, _outfileName):
        print(
            "WARNING: Method outputFile in class XSDataResultBioSaxsSmartMergev1_0 is deprecated, please use instead exportToFile!"
        )
        self.exportToFile(_outfileName)

    # Method for making a copy in a new instance
    def copy(self):
        return XSDataResultBioSaxsSmartMergev1_0.parseString(self.marshal())

    # Static method for parsing a string
    def parseString(_inString):
        doc = minidom.parseString(_inString)
        rootNode = doc.documentElement
        rootObj = XSDataResultBioSaxsSmartMergev1_0()
        rootObj.build(rootNode)
        # Check that all minOccurs are obeyed by marshalling the created object
        oStreamString = StringIO()
        rootObj.export(oStreamString, 0, name_="XSDataResultBioSaxsSmartMergev1_0")
        oStreamString.close()
        return rootObj

    parseString = staticmethod(parseString)
    # Static method for parsing a file
    def parseFile(_inFilePath):
        doc = minidom.parse(_inFilePath)
        rootNode = doc.documentElement
        rootObj = XSDataResultBioSaxsSmartMergev1_0()
        rootObj.build(rootNode)
        return rootObj

    parseFile = staticmethod(parseFile)


# end class XSDataResultBioSaxsSmartMergev1_0


class XSDataResultBioSaxsSubtractv1_0(XSDataResult):
    def __init__(
        self, status=None, volume=None, gnom=None, autorg=None, subtractedCurve=None
    ):
        XSDataResult.__init__(self, status)
        if subtractedCurve is None:
            self._subtractedCurve = None
        elif subtractedCurve.__class__.__name__ == "XSDataFile":
            self._subtractedCurve = subtractedCurve
        else:
            strMessage = (
                "ERROR! XSDataResultBioSaxsSubtractv1_0 constructor argument 'subtractedCurve' is not XSDataFile but %s"
                % self._subtractedCurve.__class__.__name__
            )
            raise BaseException(strMessage)
        if autorg is None:
            self._autorg = None
        elif autorg.__class__.__name__ == "XSDataAutoRg":
            self._autorg = autorg
        else:
            strMessage = (
                "ERROR! XSDataResultBioSaxsSubtractv1_0 constructor argument 'autorg' is not XSDataAutoRg but %s"
                % self._autorg.__class__.__name__
            )
            raise BaseException(strMessage)
        if gnom is None:
            self._gnom = None
        elif gnom.__class__.__name__ == "XSDataGnom":
            self._gnom = gnom
        else:
            strMessage = (
                "ERROR! XSDataResultBioSaxsSubtractv1_0 constructor argument 'gnom' is not XSDataGnom but %s"
                % self._gnom.__class__.__name__
            )
            raise BaseException(strMessage)
        if volume is None:
            self._volume = None
        elif volume.__class__.__name__ == "XSDataDoubleWithUnit":
            self._volume = volume
        else:
            strMessage = (
                "ERROR! XSDataResultBioSaxsSubtractv1_0 constructor argument 'volume' is not XSDataDoubleWithUnit but %s"
                % self._volume.__class__.__name__
            )
            raise BaseException(strMessage)

    # Methods and properties for the 'subtractedCurve' attribute
    def getSubtractedCurve(self):
        return self._subtractedCurve

    def setSubtractedCurve(self, subtractedCurve):
        if subtractedCurve is None:
            self._subtractedCurve = None
        elif subtractedCurve.__class__.__name__ == "XSDataFile":
            self._subtractedCurve = subtractedCurve
        else:
            strMessage = (
                "ERROR! XSDataResultBioSaxsSubtractv1_0.setSubtractedCurve argument is not XSDataFile but %s"
                % subtractedCurve.__class__.__name__
            )
            raise BaseException(strMessage)

    def delSubtractedCurve(self):
        self._subtractedCurve = None

    subtractedCurve = property(
        getSubtractedCurve,
        setSubtractedCurve,
        delSubtractedCurve,
        "Property for subtractedCurve",
    )
    # Methods and properties for the 'autorg' attribute
    def getAutorg(self):
        return self._autorg

    def setAutorg(self, autorg):
        if autorg is None:
            self._autorg = None
        elif autorg.__class__.__name__ == "XSDataAutoRg":
            self._autorg = autorg
        else:
            strMessage = (
                "ERROR! XSDataResultBioSaxsSubtractv1_0.setAutorg argument is not XSDataAutoRg but %s"
                % autorg.__class__.__name__
            )
            raise BaseException(strMessage)

    def delAutorg(self):
        self._autorg = None

    autorg = property(getAutorg, setAutorg, delAutorg, "Property for autorg")
    # Methods and properties for the 'gnom' attribute
    def getGnom(self):
        return self._gnom

    def setGnom(self, gnom):
        if gnom is None:
            self._gnom = None
        elif gnom.__class__.__name__ == "XSDataGnom":
            self._gnom = gnom
        else:
            strMessage = (
                "ERROR! XSDataResultBioSaxsSubtractv1_0.setGnom argument is not XSDataGnom but %s"
                % gnom.__class__.__name__
            )
            raise BaseException(strMessage)

    def delGnom(self):
        self._gnom = None

    gnom = property(getGnom, setGnom, delGnom, "Property for gnom")
    # Methods and properties for the 'volume' attribute
    def getVolume(self):
        return self._volume

    def setVolume(self, volume):
        if volume is None:
            self._volume = None
        elif volume.__class__.__name__ == "XSDataDoubleWithUnit":
            self._volume = volume
        else:
            strMessage = (
                "ERROR! XSDataResultBioSaxsSubtractv1_0.setVolume argument is not XSDataDoubleWithUnit but %s"
                % volume.__class__.__name__
            )
            raise BaseException(strMessage)

    def delVolume(self):
        self._volume = None

    volume = property(getVolume, setVolume, delVolume, "Property for volume")

    def export(self, outfile, level, name_="XSDataResultBioSaxsSubtractv1_0"):
        showIndent(outfile, level)
        outfile.write(unicode("<%s>\n" % name_))
        self.exportChildren(outfile, level + 1, name_)
        showIndent(outfile, level)
        outfile.write(unicode("</%s>\n" % name_))

    def exportChildren(self, outfile, level, name_="XSDataResultBioSaxsSubtractv1_0"):
        XSDataResult.exportChildren(self, outfile, level, name_)
        if self._subtractedCurve is not None:
            self.subtractedCurve.export(outfile, level, name_="subtractedCurve")
        else:
            warnEmptyAttribute("subtractedCurve", "XSDataFile")
        if self._autorg is not None:
            self.autorg.export(outfile, level, name_="autorg")
        if self._gnom is not None:
            self.gnom.export(outfile, level, name_="gnom")
        if self._volume is not None:
            self.volume.export(outfile, level, name_="volume")

    def build(self, node_):
        for child_ in node_.childNodes:
            nodeName_ = child_.nodeName.split(":")[-1]
            self.buildChildren(child_, nodeName_)

    def buildChildren(self, child_, nodeName_):
        if child_.nodeType == Node.ELEMENT_NODE and nodeName_ == "subtractedCurve":
            obj_ = XSDataFile()
            obj_.build(child_)
            self.setSubtractedCurve(obj_)
        elif child_.nodeType == Node.ELEMENT_NODE and nodeName_ == "autorg":
            obj_ = XSDataAutoRg()
            obj_.build(child_)
            self.setAutorg(obj_)
        elif child_.nodeType == Node.ELEMENT_NODE and nodeName_ == "gnom":
            obj_ = XSDataGnom()
            obj_.build(child_)
            self.setGnom(obj_)
        elif child_.nodeType == Node.ELEMENT_NODE and nodeName_ == "volume":
            obj_ = XSDataDoubleWithUnit()
            obj_.build(child_)
            self.setVolume(obj_)
        XSDataResult.buildChildren(self, child_, nodeName_)

    # Method for marshalling an object
    def marshal(self):
        oStreamString = StringIO()
        oStreamString.write(unicode('<?xml version="1.0" ?>\n'))
        self.export(oStreamString, 0, name_="XSDataResultBioSaxsSubtractv1_0")
        oStringXML = oStreamString.getvalue()
        oStreamString.close()
        return oStringXML

    # Only to export the entire XML tree to a file stream on disk
    def exportToFile(self, _outfileName):
        outfile = open(_outfileName, "w")
        outfile.write(unicode('<?xml version="1.0" ?>\n'))
        self.export(outfile, 0, name_="XSDataResultBioSaxsSubtractv1_0")
        outfile.close()

    # Deprecated method, replaced by exportToFile
    def outputFile(self, _outfileName):
        print(
            "WARNING: Method outputFile in class XSDataResultBioSaxsSubtractv1_0 is deprecated, please use instead exportToFile!"
        )
        self.exportToFile(_outfileName)

    # Method for making a copy in a new instance
    def copy(self):
        return XSDataResultBioSaxsSubtractv1_0.parseString(self.marshal())

    # Static method for parsing a string
    def parseString(_inString):
        doc = minidom.parseString(_inString)
        rootNode = doc.documentElement
        rootObj = XSDataResultBioSaxsSubtractv1_0()
        rootObj.build(rootNode)
        # Check that all minOccurs are obeyed by marshalling the created object
        oStreamString = StringIO()
        rootObj.export(oStreamString, 0, name_="XSDataResultBioSaxsSubtractv1_0")
        oStreamString.close()
        return rootObj

    parseString = staticmethod(parseString)
    # Static method for parsing a file
    def parseFile(_inFilePath):
        doc = minidom.parse(_inFilePath)
        rootNode = doc.documentElement
        rootObj = XSDataResultBioSaxsSubtractv1_0()
        rootObj.build(rootNode)
        return rootObj

    parseFile = staticmethod(parseFile)


# end class XSDataResultBioSaxsSubtractv1_0


class XSDataResultBioSaxsToSASv1_0(XSDataResult):
    def __init__(self, status=None, htmlPage=None):
        XSDataResult.__init__(self, status)
        if htmlPage is None:
            self._htmlPage = None
        elif htmlPage.__class__.__name__ == "XSDataFile":
            self._htmlPage = htmlPage
        else:
            strMessage = (
                "ERROR! XSDataResultBioSaxsToSASv1_0 constructor argument 'htmlPage' is not XSDataFile but %s"
                % self._htmlPage.__class__.__name__
            )
            raise BaseException(strMessage)

    # Methods and properties for the 'htmlPage' attribute
    def getHtmlPage(self):
        return self._htmlPage

    def setHtmlPage(self, htmlPage):
        if htmlPage is None:
            self._htmlPage = None
        elif htmlPage.__class__.__name__ == "XSDataFile":
            self._htmlPage = htmlPage
        else:
            strMessage = (
                "ERROR! XSDataResultBioSaxsToSASv1_0.setHtmlPage argument is not XSDataFile but %s"
                % htmlPage.__class__.__name__
            )
            raise BaseException(strMessage)

    def delHtmlPage(self):
        self._htmlPage = None

    htmlPage = property(getHtmlPage, setHtmlPage, delHtmlPage, "Property for htmlPage")

    def export(self, outfile, level, name_="XSDataResultBioSaxsToSASv1_0"):
        showIndent(outfile, level)
        outfile.write(unicode("<%s>\n" % name_))
        self.exportChildren(outfile, level + 1, name_)
        showIndent(outfile, level)
        outfile.write(unicode("</%s>\n" % name_))

    def exportChildren(self, outfile, level, name_="XSDataResultBioSaxsToSASv1_0"):
        XSDataResult.exportChildren(self, outfile, level, name_)
        if self._htmlPage is not None:
            self.htmlPage.export(outfile, level, name_="htmlPage")
        else:
            warnEmptyAttribute("htmlPage", "XSDataFile")

    def build(self, node_):
        for child_ in node_.childNodes:
            nodeName_ = child_.nodeName.split(":")[-1]
            self.buildChildren(child_, nodeName_)

    def buildChildren(self, child_, nodeName_):
        if child_.nodeType == Node.ELEMENT_NODE and nodeName_ == "htmlPage":
            obj_ = XSDataFile()
            obj_.build(child_)
            self.setHtmlPage(obj_)
        XSDataResult.buildChildren(self, child_, nodeName_)

    # Method for marshalling an object
    def marshal(self):
        oStreamString = StringIO()
        oStreamString.write(unicode('<?xml version="1.0" ?>\n'))
        self.export(oStreamString, 0, name_="XSDataResultBioSaxsToSASv1_0")
        oStringXML = oStreamString.getvalue()
        oStreamString.close()
        return oStringXML

    # Only to export the entire XML tree to a file stream on disk
    def exportToFile(self, _outfileName):
        outfile = open(_outfileName, "w")
        outfile.write(unicode('<?xml version="1.0" ?>\n'))
        self.export(outfile, 0, name_="XSDataResultBioSaxsToSASv1_0")
        outfile.close()

    # Deprecated method, replaced by exportToFile
    def outputFile(self, _outfileName):
        print(
            "WARNING: Method outputFile in class XSDataResultBioSaxsToSASv1_0 is deprecated, please use instead exportToFile!"
        )
        self.exportToFile(_outfileName)

    # Method for making a copy in a new instance
    def copy(self):
        return XSDataResultBioSaxsToSASv1_0.parseString(self.marshal())

    # Static method for parsing a string
    def parseString(_inString):
        doc = minidom.parseString(_inString)
        rootNode = doc.documentElement
        rootObj = XSDataResultBioSaxsToSASv1_0()
        rootObj.build(rootNode)
        # Check that all minOccurs are obeyed by marshalling the created object
        oStreamString = StringIO()
        rootObj.export(oStreamString, 0, name_="XSDataResultBioSaxsToSASv1_0")
        oStreamString.close()
        return rootObj

    parseString = staticmethod(parseString)
    # Static method for parsing a file
    def parseFile(_inFilePath):
        doc = minidom.parse(_inFilePath)
        rootNode = doc.documentElement
        rootObj = XSDataResultBioSaxsToSASv1_0()
        rootObj.build(rootNode)
        return rootObj

    parseFile = staticmethod(parseFile)


# end class XSDataResultBioSaxsToSASv1_0


class XSDataInputBioSaxsHPLCv1_0(XSDataInputBioSaxsProcessOneFilev1_0):
    """Plugin that runs subsequently ProcessOneFile, subtraction of buffer and SaxsAnalysis"""

    def __init__(
        self,
        configuration=None,
        frameId=None,
        runId=None,
        integratedCurve=None,
        integratedImage=None,
        normalizedImage=None,
        logFile=None,
        rawImageSize=None,
        experimentSetup=None,
        sample=None,
        rawImage=None,
        hplcFile=None,
        gnomFile=None,
        subtractedCurve=None,
        bufferCurve=None,
    ):
        XSDataInputBioSaxsProcessOneFilev1_0.__init__(
            self,
            configuration,
            frameId,
            runId,
            integratedCurve,
            integratedImage,
            normalizedImage,
            logFile,
            rawImageSize,
            experimentSetup,
            sample,
            rawImage,
        )
        if bufferCurve is None:
            self._bufferCurve = None
        elif bufferCurve.__class__.__name__ == "XSDataFile":
            self._bufferCurve = bufferCurve
        else:
            strMessage = (
                "ERROR! XSDataInputBioSaxsHPLCv1_0 constructor argument 'bufferCurve' is not XSDataFile but %s"
                % self._bufferCurve.__class__.__name__
            )
            raise BaseException(strMessage)
        if subtractedCurve is None:
            self._subtractedCurve = None
        elif subtractedCurve.__class__.__name__ == "XSDataFile":
            self._subtractedCurve = subtractedCurve
        else:
            strMessage = (
                "ERROR! XSDataInputBioSaxsHPLCv1_0 constructor argument 'subtractedCurve' is not XSDataFile but %s"
                % self._subtractedCurve.__class__.__name__
            )
            raise BaseException(strMessage)
        if gnomFile is None:
            self._gnomFile = None
        elif gnomFile.__class__.__name__ == "XSDataFile":
            self._gnomFile = gnomFile
        else:
            strMessage = (
                "ERROR! XSDataInputBioSaxsHPLCv1_0 constructor argument 'gnomFile' is not XSDataFile but %s"
                % self._gnomFile.__class__.__name__
            )
            raise BaseException(strMessage)
        if hplcFile is None:
            self._hplcFile = None
        elif hplcFile.__class__.__name__ == "XSDataFile":
            self._hplcFile = hplcFile
        else:
            strMessage = (
                "ERROR! XSDataInputBioSaxsHPLCv1_0 constructor argument 'hplcFile' is not XSDataFile but %s"
                % self._hplcFile.__class__.__name__
            )
            raise BaseException(strMessage)

    # Methods and properties for the 'bufferCurve' attribute
    def getBufferCurve(self):
        return self._bufferCurve

    def setBufferCurve(self, bufferCurve):
        if bufferCurve is None:
            self._bufferCurve = None
        elif bufferCurve.__class__.__name__ == "XSDataFile":
            self._bufferCurve = bufferCurve
        else:
            strMessage = (
                "ERROR! XSDataInputBioSaxsHPLCv1_0.setBufferCurve argument is not XSDataFile but %s"
                % bufferCurve.__class__.__name__
            )
            raise BaseException(strMessage)

    def delBufferCurve(self):
        self._bufferCurve = None

    bufferCurve = property(
        getBufferCurve, setBufferCurve, delBufferCurve, "Property for bufferCurve"
    )
    # Methods and properties for the 'subtractedCurve' attribute
    def getSubtractedCurve(self):
        return self._subtractedCurve

    def setSubtractedCurve(self, subtractedCurve):
        if subtractedCurve is None:
            self._subtractedCurve = None
        elif subtractedCurve.__class__.__name__ == "XSDataFile":
            self._subtractedCurve = subtractedCurve
        else:
            strMessage = (
                "ERROR! XSDataInputBioSaxsHPLCv1_0.setSubtractedCurve argument is not XSDataFile but %s"
                % subtractedCurve.__class__.__name__
            )
            raise BaseException(strMessage)

    def delSubtractedCurve(self):
        self._subtractedCurve = None

    subtractedCurve = property(
        getSubtractedCurve,
        setSubtractedCurve,
        delSubtractedCurve,
        "Property for subtractedCurve",
    )
    # Methods and properties for the 'gnomFile' attribute
    def getGnomFile(self):
        return self._gnomFile

    def setGnomFile(self, gnomFile):
        if gnomFile is None:
            self._gnomFile = None
        elif gnomFile.__class__.__name__ == "XSDataFile":
            self._gnomFile = gnomFile
        else:
            strMessage = (
                "ERROR! XSDataInputBioSaxsHPLCv1_0.setGnomFile argument is not XSDataFile but %s"
                % gnomFile.__class__.__name__
            )
            raise BaseException(strMessage)

    def delGnomFile(self):
        self._gnomFile = None

    gnomFile = property(getGnomFile, setGnomFile, delGnomFile, "Property for gnomFile")
    # Methods and properties for the 'hplcFile' attribute
    def getHplcFile(self):
        return self._hplcFile

    def setHplcFile(self, hplcFile):
        if hplcFile is None:
            self._hplcFile = None
        elif hplcFile.__class__.__name__ == "XSDataFile":
            self._hplcFile = hplcFile
        else:
            strMessage = (
                "ERROR! XSDataInputBioSaxsHPLCv1_0.setHplcFile argument is not XSDataFile but %s"
                % hplcFile.__class__.__name__
            )
            raise BaseException(strMessage)

    def delHplcFile(self):
        self._hplcFile = None

    hplcFile = property(getHplcFile, setHplcFile, delHplcFile, "Property for hplcFile")

    def export(self, outfile, level, name_="XSDataInputBioSaxsHPLCv1_0"):
        showIndent(outfile, level)
        outfile.write(unicode("<%s>\n" % name_))
        self.exportChildren(outfile, level + 1, name_)
        showIndent(outfile, level)
        outfile.write(unicode("</%s>\n" % name_))

    def exportChildren(self, outfile, level, name_="XSDataInputBioSaxsHPLCv1_0"):
        XSDataInputBioSaxsProcessOneFilev1_0.exportChildren(self, outfile, level, name_)
        if self._bufferCurve is not None:
            self.bufferCurve.export(outfile, level, name_="bufferCurve")
        if self._subtractedCurve is not None:
            self.subtractedCurve.export(outfile, level, name_="subtractedCurve")
        if self._gnomFile is not None:
            self.gnomFile.export(outfile, level, name_="gnomFile")
        if self._hplcFile is not None:
            self.hplcFile.export(outfile, level, name_="hplcFile")

    def build(self, node_):
        for child_ in node_.childNodes:
            nodeName_ = child_.nodeName.split(":")[-1]
            self.buildChildren(child_, nodeName_)

    def buildChildren(self, child_, nodeName_):
        if child_.nodeType == Node.ELEMENT_NODE and nodeName_ == "bufferCurve":
            obj_ = XSDataFile()
            obj_.build(child_)
            self.setBufferCurve(obj_)
        elif child_.nodeType == Node.ELEMENT_NODE and nodeName_ == "subtractedCurve":
            obj_ = XSDataFile()
            obj_.build(child_)
            self.setSubtractedCurve(obj_)
        elif child_.nodeType == Node.ELEMENT_NODE and nodeName_ == "gnomFile":
            obj_ = XSDataFile()
            obj_.build(child_)
            self.setGnomFile(obj_)
        elif child_.nodeType == Node.ELEMENT_NODE and nodeName_ == "hplcFile":
            obj_ = XSDataFile()
            obj_.build(child_)
            self.setHplcFile(obj_)
        XSDataInputBioSaxsProcessOneFilev1_0.buildChildren(self, child_, nodeName_)

    # Method for marshalling an object
    def marshal(self):
        oStreamString = StringIO()
        oStreamString.write(unicode('<?xml version="1.0" ?>\n'))
        self.export(oStreamString, 0, name_="XSDataInputBioSaxsHPLCv1_0")
        oStringXML = oStreamString.getvalue()
        oStreamString.close()
        return oStringXML

    # Only to export the entire XML tree to a file stream on disk
    def exportToFile(self, _outfileName):
        outfile = open(_outfileName, "w")
        outfile.write(unicode('<?xml version="1.0" ?>\n'))
        self.export(outfile, 0, name_="XSDataInputBioSaxsHPLCv1_0")
        outfile.close()

    # Deprecated method, replaced by exportToFile
    def outputFile(self, _outfileName):
        print(
            "WARNING: Method outputFile in class XSDataInputBioSaxsHPLCv1_0 is deprecated, please use instead exportToFile!"
        )
        self.exportToFile(_outfileName)

    # Method for making a copy in a new instance
    def copy(self):
        return XSDataInputBioSaxsHPLCv1_0.parseString(self.marshal())

    # Static method for parsing a string
    def parseString(_inString):
        doc = minidom.parseString(_inString)
        rootNode = doc.documentElement
        rootObj = XSDataInputBioSaxsHPLCv1_0()
        rootObj.build(rootNode)
        # Check that all minOccurs are obeyed by marshalling the created object
        oStreamString = StringIO()
        rootObj.export(oStreamString, 0, name_="XSDataInputBioSaxsHPLCv1_0")
        oStreamString.close()
        return rootObj

    parseString = staticmethod(parseString)
    # Static method for parsing a file
    def parseFile(_inFilePath):
        doc = minidom.parse(_inFilePath)
        rootNode = doc.documentElement
        rootObj = XSDataInputBioSaxsHPLCv1_0()
        rootObj.build(rootNode)
        return rootObj

    parseFile = staticmethod(parseFile)


# end class XSDataInputBioSaxsHPLCv1_0


class XSDataInputBioSaxsSampleExperiment(XSDataInputBioSaxsSample):
    """temporary class for multiple inhertitance emulation"""

    def __init__(
        self,
        configuration=None,
        code=None,
        comments=None,
        concentration=None,
        timeOfFrame=None,
        frameMax=None,
        frameNumber=None,
        exposureTime=None,
        exposureTemperature=None,
        storageTemperature=None,
        normalizationFactor=None,
        maskFile=None,
        machineCurrent=None,
        wavelength=None,
        beamStopDiode=None,
        beamCenter_2=None,
        beamCenter_1=None,
        pixelSize_2=None,
        pixelSize_1=None,
        detectorDistance=None,
        detector=None,
    ):
        XSDataInputBioSaxsSample.__init__(
            self, configuration, code, comments, concentration
        )
        if detector is None:
            self._detector = None
        elif detector.__class__.__name__ == "XSDataString":
            self._detector = detector
        else:
            strMessage = (
                "ERROR! XSDataInputBioSaxsSampleExperiment constructor argument 'detector' is not XSDataString but %s"
                % self._detector.__class__.__name__
            )
            raise BaseException(strMessage)
        if detectorDistance is None:
            self._detectorDistance = None
        elif detectorDistance.__class__.__name__ == "XSDataLength":
            self._detectorDistance = detectorDistance
        else:
            strMessage = (
                "ERROR! XSDataInputBioSaxsSampleExperiment constructor argument 'detectorDistance' is not XSDataLength but %s"
                % self._detectorDistance.__class__.__name__
            )
            raise BaseException(strMessage)
        if pixelSize_1 is None:
            self._pixelSize_1 = None
        elif pixelSize_1.__class__.__name__ == "XSDataLength":
            self._pixelSize_1 = pixelSize_1
        else:
            strMessage = (
                "ERROR! XSDataInputBioSaxsSampleExperiment constructor argument 'pixelSize_1' is not XSDataLength but %s"
                % self._pixelSize_1.__class__.__name__
            )
            raise BaseException(strMessage)
        if pixelSize_2 is None:
            self._pixelSize_2 = None
        elif pixelSize_2.__class__.__name__ == "XSDataLength":
            self._pixelSize_2 = pixelSize_2
        else:
            strMessage = (
                "ERROR! XSDataInputBioSaxsSampleExperiment constructor argument 'pixelSize_2' is not XSDataLength but %s"
                % self._pixelSize_2.__class__.__name__
            )
            raise BaseException(strMessage)
        if beamCenter_1 is None:
            self._beamCenter_1 = None
        elif beamCenter_1.__class__.__name__ == "XSDataDouble":
            self._beamCenter_1 = beamCenter_1
        else:
            strMessage = (
                "ERROR! XSDataInputBioSaxsSampleExperiment constructor argument 'beamCenter_1' is not XSDataDouble but %s"
                % self._beamCenter_1.__class__.__name__
            )
            raise BaseException(strMessage)
        if beamCenter_2 is None:
            self._beamCenter_2 = None
        elif beamCenter_2.__class__.__name__ == "XSDataDouble":
            self._beamCenter_2 = beamCenter_2
        else:
            strMessage = (
                "ERROR! XSDataInputBioSaxsSampleExperiment constructor argument 'beamCenter_2' is not XSDataDouble but %s"
                % self._beamCenter_2.__class__.__name__
            )
            raise BaseException(strMessage)
        if beamStopDiode is None:
            self._beamStopDiode = None
        elif beamStopDiode.__class__.__name__ == "XSDataDouble":
            self._beamStopDiode = beamStopDiode
        else:
            strMessage = (
                "ERROR! XSDataInputBioSaxsSampleExperiment constructor argument 'beamStopDiode' is not XSDataDouble but %s"
                % self._beamStopDiode.__class__.__name__
            )
            raise BaseException(strMessage)
        if wavelength is None:
            self._wavelength = None
        elif wavelength.__class__.__name__ == "XSDataWavelength":
            self._wavelength = wavelength
        else:
            strMessage = (
                "ERROR! XSDataInputBioSaxsSampleExperiment constructor argument 'wavelength' is not XSDataWavelength but %s"
                % self._wavelength.__class__.__name__
            )
            raise BaseException(strMessage)
        if machineCurrent is None:
            self._machineCurrent = None
        elif machineCurrent.__class__.__name__ == "XSDataDouble":
            self._machineCurrent = machineCurrent
        else:
            strMessage = (
                "ERROR! XSDataInputBioSaxsSampleExperiment constructor argument 'machineCurrent' is not XSDataDouble but %s"
                % self._machineCurrent.__class__.__name__
            )
            raise BaseException(strMessage)
        if maskFile is None:
            self._maskFile = None
        elif maskFile.__class__.__name__ == "XSDataImage":
            self._maskFile = maskFile
        else:
            strMessage = (
                "ERROR! XSDataInputBioSaxsSampleExperiment constructor argument 'maskFile' is not XSDataImage but %s"
                % self._maskFile.__class__.__name__
            )
            raise BaseException(strMessage)
        if normalizationFactor is None:
            self._normalizationFactor = None
        elif normalizationFactor.__class__.__name__ == "XSDataDouble":
            self._normalizationFactor = normalizationFactor
        else:
            strMessage = (
                "ERROR! XSDataInputBioSaxsSampleExperiment constructor argument 'normalizationFactor' is not XSDataDouble but %s"
                % self._normalizationFactor.__class__.__name__
            )
            raise BaseException(strMessage)
        if storageTemperature is None:
            self._storageTemperature = None
        elif storageTemperature.__class__.__name__ == "XSDataDouble":
            self._storageTemperature = storageTemperature
        else:
            strMessage = (
                "ERROR! XSDataInputBioSaxsSampleExperiment constructor argument 'storageTemperature' is not XSDataDouble but %s"
                % self._storageTemperature.__class__.__name__
            )
            raise BaseException(strMessage)
        if exposureTemperature is None:
            self._exposureTemperature = None
        elif exposureTemperature.__class__.__name__ == "XSDataDouble":
            self._exposureTemperature = exposureTemperature
        else:
            strMessage = (
                "ERROR! XSDataInputBioSaxsSampleExperiment constructor argument 'exposureTemperature' is not XSDataDouble but %s"
                % self._exposureTemperature.__class__.__name__
            )
            raise BaseException(strMessage)
        if exposureTime is None:
            self._exposureTime = None
        elif exposureTime.__class__.__name__ == "XSDataTime":
            self._exposureTime = exposureTime
        else:
            strMessage = (
                "ERROR! XSDataInputBioSaxsSampleExperiment constructor argument 'exposureTime' is not XSDataTime but %s"
                % self._exposureTime.__class__.__name__
            )
            raise BaseException(strMessage)
        if frameNumber is None:
            self._frameNumber = None
        elif frameNumber.__class__.__name__ == "XSDataInteger":
            self._frameNumber = frameNumber
        else:
            strMessage = (
                "ERROR! XSDataInputBioSaxsSampleExperiment constructor argument 'frameNumber' is not XSDataInteger but %s"
                % self._frameNumber.__class__.__name__
            )
            raise BaseException(strMessage)
        if frameMax is None:
            self._frameMax = None
        elif frameMax.__class__.__name__ == "XSDataInteger":
            self._frameMax = frameMax
        else:
            strMessage = (
                "ERROR! XSDataInputBioSaxsSampleExperiment constructor argument 'frameMax' is not XSDataInteger but %s"
                % self._frameMax.__class__.__name__
            )
            raise BaseException(strMessage)
        if timeOfFrame is None:
            self._timeOfFrame = None
        elif timeOfFrame.__class__.__name__ == "XSDataTime":
            self._timeOfFrame = timeOfFrame
        else:
            strMessage = (
                "ERROR! XSDataInputBioSaxsSampleExperiment constructor argument 'timeOfFrame' is not XSDataTime but %s"
                % self._timeOfFrame.__class__.__name__
            )
            raise BaseException(strMessage)

    # Methods and properties for the 'detector' attribute
    def getDetector(self):
        return self._detector

    def setDetector(self, detector):
        if detector is None:
            self._detector = None
        elif detector.__class__.__name__ == "XSDataString":
            self._detector = detector
        else:
            strMessage = (
                "ERROR! XSDataInputBioSaxsSampleExperiment.setDetector argument is not XSDataString but %s"
                % detector.__class__.__name__
            )
            raise BaseException(strMessage)

    def delDetector(self):
        self._detector = None

    detector = property(getDetector, setDetector, delDetector, "Property for detector")
    # Methods and properties for the 'detectorDistance' attribute
    def getDetectorDistance(self):
        return self._detectorDistance

    def setDetectorDistance(self, detectorDistance):
        if detectorDistance is None:
            self._detectorDistance = None
        elif detectorDistance.__class__.__name__ == "XSDataLength":
            self._detectorDistance = detectorDistance
        else:
            strMessage = (
                "ERROR! XSDataInputBioSaxsSampleExperiment.setDetectorDistance argument is not XSDataLength but %s"
                % detectorDistance.__class__.__name__
            )
            raise BaseException(strMessage)

    def delDetectorDistance(self):
        self._detectorDistance = None

    detectorDistance = property(
        getDetectorDistance,
        setDetectorDistance,
        delDetectorDistance,
        "Property for detectorDistance",
    )
    # Methods and properties for the 'pixelSize_1' attribute
    def getPixelSize_1(self):
        return self._pixelSize_1

    def setPixelSize_1(self, pixelSize_1):
        if pixelSize_1 is None:
            self._pixelSize_1 = None
        elif pixelSize_1.__class__.__name__ == "XSDataLength":
            self._pixelSize_1 = pixelSize_1
        else:
            strMessage = (
                "ERROR! XSDataInputBioSaxsSampleExperiment.setPixelSize_1 argument is not XSDataLength but %s"
                % pixelSize_1.__class__.__name__
            )
            raise BaseException(strMessage)

    def delPixelSize_1(self):
        self._pixelSize_1 = None

    pixelSize_1 = property(
        getPixelSize_1, setPixelSize_1, delPixelSize_1, "Property for pixelSize_1"
    )
    # Methods and properties for the 'pixelSize_2' attribute
    def getPixelSize_2(self):
        return self._pixelSize_2

    def setPixelSize_2(self, pixelSize_2):
        if pixelSize_2 is None:
            self._pixelSize_2 = None
        elif pixelSize_2.__class__.__name__ == "XSDataLength":
            self._pixelSize_2 = pixelSize_2
        else:
            strMessage = (
                "ERROR! XSDataInputBioSaxsSampleExperiment.setPixelSize_2 argument is not XSDataLength but %s"
                % pixelSize_2.__class__.__name__
            )
            raise BaseException(strMessage)

    def delPixelSize_2(self):
        self._pixelSize_2 = None

    pixelSize_2 = property(
        getPixelSize_2, setPixelSize_2, delPixelSize_2, "Property for pixelSize_2"
    )
    # Methods and properties for the 'beamCenter_1' attribute
    def getBeamCenter_1(self):
        return self._beamCenter_1

    def setBeamCenter_1(self, beamCenter_1):
        if beamCenter_1 is None:
            self._beamCenter_1 = None
        elif beamCenter_1.__class__.__name__ == "XSDataDouble":
            self._beamCenter_1 = beamCenter_1
        else:
            strMessage = (
                "ERROR! XSDataInputBioSaxsSampleExperiment.setBeamCenter_1 argument is not XSDataDouble but %s"
                % beamCenter_1.__class__.__name__
            )
            raise BaseException(strMessage)

    def delBeamCenter_1(self):
        self._beamCenter_1 = None

    beamCenter_1 = property(
        getBeamCenter_1, setBeamCenter_1, delBeamCenter_1, "Property for beamCenter_1"
    )
    # Methods and properties for the 'beamCenter_2' attribute
    def getBeamCenter_2(self):
        return self._beamCenter_2

    def setBeamCenter_2(self, beamCenter_2):
        if beamCenter_2 is None:
            self._beamCenter_2 = None
        elif beamCenter_2.__class__.__name__ == "XSDataDouble":
            self._beamCenter_2 = beamCenter_2
        else:
            strMessage = (
                "ERROR! XSDataInputBioSaxsSampleExperiment.setBeamCenter_2 argument is not XSDataDouble but %s"
                % beamCenter_2.__class__.__name__
            )
            raise BaseException(strMessage)

    def delBeamCenter_2(self):
        self._beamCenter_2 = None

    beamCenter_2 = property(
        getBeamCenter_2, setBeamCenter_2, delBeamCenter_2, "Property for beamCenter_2"
    )
    # Methods and properties for the 'beamStopDiode' attribute
    def getBeamStopDiode(self):
        return self._beamStopDiode

    def setBeamStopDiode(self, beamStopDiode):
        if beamStopDiode is None:
            self._beamStopDiode = None
        elif beamStopDiode.__class__.__name__ == "XSDataDouble":
            self._beamStopDiode = beamStopDiode
        else:
            strMessage = (
                "ERROR! XSDataInputBioSaxsSampleExperiment.setBeamStopDiode argument is not XSDataDouble but %s"
                % beamStopDiode.__class__.__name__
            )
            raise BaseException(strMessage)

    def delBeamStopDiode(self):
        self._beamStopDiode = None

    beamStopDiode = property(
        getBeamStopDiode,
        setBeamStopDiode,
        delBeamStopDiode,
        "Property for beamStopDiode",
    )
    # Methods and properties for the 'wavelength' attribute
    def getWavelength(self):
        return self._wavelength

    def setWavelength(self, wavelength):
        if wavelength is None:
            self._wavelength = None
        elif wavelength.__class__.__name__ == "XSDataWavelength":
            self._wavelength = wavelength
        else:
            strMessage = (
                "ERROR! XSDataInputBioSaxsSampleExperiment.setWavelength argument is not XSDataWavelength but %s"
                % wavelength.__class__.__name__
            )
            raise BaseException(strMessage)

    def delWavelength(self):
        self._wavelength = None

    wavelength = property(
        getWavelength, setWavelength, delWavelength, "Property for wavelength"
    )
    # Methods and properties for the 'machineCurrent' attribute
    def getMachineCurrent(self):
        return self._machineCurrent

    def setMachineCurrent(self, machineCurrent):
        if machineCurrent is None:
            self._machineCurrent = None
        elif machineCurrent.__class__.__name__ == "XSDataDouble":
            self._machineCurrent = machineCurrent
        else:
            strMessage = (
                "ERROR! XSDataInputBioSaxsSampleExperiment.setMachineCurrent argument is not XSDataDouble but %s"
                % machineCurrent.__class__.__name__
            )
            raise BaseException(strMessage)

    def delMachineCurrent(self):
        self._machineCurrent = None

    machineCurrent = property(
        getMachineCurrent,
        setMachineCurrent,
        delMachineCurrent,
        "Property for machineCurrent",
    )
    # Methods and properties for the 'maskFile' attribute
    def getMaskFile(self):
        return self._maskFile

    def setMaskFile(self, maskFile):
        if maskFile is None:
            self._maskFile = None
        elif maskFile.__class__.__name__ == "XSDataImage":
            self._maskFile = maskFile
        else:
            strMessage = (
                "ERROR! XSDataInputBioSaxsSampleExperiment.setMaskFile argument is not XSDataImage but %s"
                % maskFile.__class__.__name__
            )
            raise BaseException(strMessage)

    def delMaskFile(self):
        self._maskFile = None

    maskFile = property(getMaskFile, setMaskFile, delMaskFile, "Property for maskFile")
    # Methods and properties for the 'normalizationFactor' attribute
    def getNormalizationFactor(self):
        return self._normalizationFactor

    def setNormalizationFactor(self, normalizationFactor):
        if normalizationFactor is None:
            self._normalizationFactor = None
        elif normalizationFactor.__class__.__name__ == "XSDataDouble":
            self._normalizationFactor = normalizationFactor
        else:
            strMessage = (
                "ERROR! XSDataInputBioSaxsSampleExperiment.setNormalizationFactor argument is not XSDataDouble but %s"
                % normalizationFactor.__class__.__name__
            )
            raise BaseException(strMessage)

    def delNormalizationFactor(self):
        self._normalizationFactor = None

    normalizationFactor = property(
        getNormalizationFactor,
        setNormalizationFactor,
        delNormalizationFactor,
        "Property for normalizationFactor",
    )
    # Methods and properties for the 'storageTemperature' attribute
    def getStorageTemperature(self):
        return self._storageTemperature

    def setStorageTemperature(self, storageTemperature):
        if storageTemperature is None:
            self._storageTemperature = None
        elif storageTemperature.__class__.__name__ == "XSDataDouble":
            self._storageTemperature = storageTemperature
        else:
            strMessage = (
                "ERROR! XSDataInputBioSaxsSampleExperiment.setStorageTemperature argument is not XSDataDouble but %s"
                % storageTemperature.__class__.__name__
            )
            raise BaseException(strMessage)

    def delStorageTemperature(self):
        self._storageTemperature = None

    storageTemperature = property(
        getStorageTemperature,
        setStorageTemperature,
        delStorageTemperature,
        "Property for storageTemperature",
    )
    # Methods and properties for the 'exposureTemperature' attribute
    def getExposureTemperature(self):
        return self._exposureTemperature

    def setExposureTemperature(self, exposureTemperature):
        if exposureTemperature is None:
            self._exposureTemperature = None
        elif exposureTemperature.__class__.__name__ == "XSDataDouble":
            self._exposureTemperature = exposureTemperature
        else:
            strMessage = (
                "ERROR! XSDataInputBioSaxsSampleExperiment.setExposureTemperature argument is not XSDataDouble but %s"
                % exposureTemperature.__class__.__name__
            )
            raise BaseException(strMessage)

    def delExposureTemperature(self):
        self._exposureTemperature = None

    exposureTemperature = property(
        getExposureTemperature,
        setExposureTemperature,
        delExposureTemperature,
        "Property for exposureTemperature",
    )
    # Methods and properties for the 'exposureTime' attribute
    def getExposureTime(self):
        return self._exposureTime

    def setExposureTime(self, exposureTime):
        if exposureTime is None:
            self._exposureTime = None
        elif exposureTime.__class__.__name__ == "XSDataTime":
            self._exposureTime = exposureTime
        else:
            strMessage = (
                "ERROR! XSDataInputBioSaxsSampleExperiment.setExposureTime argument is not XSDataTime but %s"
                % exposureTime.__class__.__name__
            )
            raise BaseException(strMessage)

    def delExposureTime(self):
        self._exposureTime = None

    exposureTime = property(
        getExposureTime, setExposureTime, delExposureTime, "Property for exposureTime"
    )
    # Methods and properties for the 'frameNumber' attribute
    def getFrameNumber(self):
        return self._frameNumber

    def setFrameNumber(self, frameNumber):
        if frameNumber is None:
            self._frameNumber = None
        elif frameNumber.__class__.__name__ == "XSDataInteger":
            self._frameNumber = frameNumber
        else:
            strMessage = (
                "ERROR! XSDataInputBioSaxsSampleExperiment.setFrameNumber argument is not XSDataInteger but %s"
                % frameNumber.__class__.__name__
            )
            raise BaseException(strMessage)

    def delFrameNumber(self):
        self._frameNumber = None

    frameNumber = property(
        getFrameNumber, setFrameNumber, delFrameNumber, "Property for frameNumber"
    )
    # Methods and properties for the 'frameMax' attribute
    def getFrameMax(self):
        return self._frameMax

    def setFrameMax(self, frameMax):
        if frameMax is None:
            self._frameMax = None
        elif frameMax.__class__.__name__ == "XSDataInteger":
            self._frameMax = frameMax
        else:
            strMessage = (
                "ERROR! XSDataInputBioSaxsSampleExperiment.setFrameMax argument is not XSDataInteger but %s"
                % frameMax.__class__.__name__
            )
            raise BaseException(strMessage)

    def delFrameMax(self):
        self._frameMax = None

    frameMax = property(getFrameMax, setFrameMax, delFrameMax, "Property for frameMax")
    # Methods and properties for the 'timeOfFrame' attribute
    def getTimeOfFrame(self):
        return self._timeOfFrame

    def setTimeOfFrame(self, timeOfFrame):
        if timeOfFrame is None:
            self._timeOfFrame = None
        elif timeOfFrame.__class__.__name__ == "XSDataTime":
            self._timeOfFrame = timeOfFrame
        else:
            strMessage = (
                "ERROR! XSDataInputBioSaxsSampleExperiment.setTimeOfFrame argument is not XSDataTime but %s"
                % timeOfFrame.__class__.__name__
            )
            raise BaseException(strMessage)

    def delTimeOfFrame(self):
        self._timeOfFrame = None

    timeOfFrame = property(
        getTimeOfFrame, setTimeOfFrame, delTimeOfFrame, "Property for timeOfFrame"
    )

    def export(self, outfile, level, name_="XSDataInputBioSaxsSampleExperiment"):
        showIndent(outfile, level)
        outfile.write(unicode("<%s>\n" % name_))
        self.exportChildren(outfile, level + 1, name_)
        showIndent(outfile, level)
        outfile.write(unicode("</%s>\n" % name_))

    def exportChildren(
        self, outfile, level, name_="XSDataInputBioSaxsSampleExperiment"
    ):
        XSDataInputBioSaxsSample.exportChildren(self, outfile, level, name_)
        if self._detector is not None:
            self.detector.export(outfile, level, name_="detector")
        if self._detectorDistance is not None:
            self.detectorDistance.export(outfile, level, name_="detectorDistance")
        if self._pixelSize_1 is not None:
            self.pixelSize_1.export(outfile, level, name_="pixelSize_1")
        if self._pixelSize_2 is not None:
            self.pixelSize_2.export(outfile, level, name_="pixelSize_2")
        if self._beamCenter_1 is not None:
            self.beamCenter_1.export(outfile, level, name_="beamCenter_1")
        if self._beamCenter_2 is not None:
            self.beamCenter_2.export(outfile, level, name_="beamCenter_2")
        if self._beamStopDiode is not None:
            self.beamStopDiode.export(outfile, level, name_="beamStopDiode")
        if self._wavelength is not None:
            self.wavelength.export(outfile, level, name_="wavelength")
        if self._machineCurrent is not None:
            self.machineCurrent.export(outfile, level, name_="machineCurrent")
        if self._maskFile is not None:
            self.maskFile.export(outfile, level, name_="maskFile")
        if self._normalizationFactor is not None:
            self.normalizationFactor.export(outfile, level, name_="normalizationFactor")
        if self._storageTemperature is not None:
            self.storageTemperature.export(outfile, level, name_="storageTemperature")
        if self._exposureTemperature is not None:
            self.exposureTemperature.export(outfile, level, name_="exposureTemperature")
        if self._exposureTime is not None:
            self.exposureTime.export(outfile, level, name_="exposureTime")
        if self._frameNumber is not None:
            self.frameNumber.export(outfile, level, name_="frameNumber")
        if self._frameMax is not None:
            self.frameMax.export(outfile, level, name_="frameMax")
        if self._timeOfFrame is not None:
            self.timeOfFrame.export(outfile, level, name_="timeOfFrame")

    def build(self, node_):
        for child_ in node_.childNodes:
            nodeName_ = child_.nodeName.split(":")[-1]
            self.buildChildren(child_, nodeName_)

    def buildChildren(self, child_, nodeName_):
        if child_.nodeType == Node.ELEMENT_NODE and nodeName_ == "detector":
            obj_ = XSDataString()
            obj_.build(child_)
            self.setDetector(obj_)
        elif child_.nodeType == Node.ELEMENT_NODE and nodeName_ == "detectorDistance":
            obj_ = XSDataLength()
            obj_.build(child_)
            self.setDetectorDistance(obj_)
        elif child_.nodeType == Node.ELEMENT_NODE and nodeName_ == "pixelSize_1":
            obj_ = XSDataLength()
            obj_.build(child_)
            self.setPixelSize_1(obj_)
        elif child_.nodeType == Node.ELEMENT_NODE and nodeName_ == "pixelSize_2":
            obj_ = XSDataLength()
            obj_.build(child_)
            self.setPixelSize_2(obj_)
        elif child_.nodeType == Node.ELEMENT_NODE and nodeName_ == "beamCenter_1":
            obj_ = XSDataDouble()
            obj_.build(child_)
            self.setBeamCenter_1(obj_)
        elif child_.nodeType == Node.ELEMENT_NODE and nodeName_ == "beamCenter_2":
            obj_ = XSDataDouble()
            obj_.build(child_)
            self.setBeamCenter_2(obj_)
        elif child_.nodeType == Node.ELEMENT_NODE and nodeName_ == "beamStopDiode":
            obj_ = XSDataDouble()
            obj_.build(child_)
            self.setBeamStopDiode(obj_)
        elif child_.nodeType == Node.ELEMENT_NODE and nodeName_ == "wavelength":
            obj_ = XSDataWavelength()
            obj_.build(child_)
            self.setWavelength(obj_)
        elif child_.nodeType == Node.ELEMENT_NODE and nodeName_ == "machineCurrent":
            obj_ = XSDataDouble()
            obj_.build(child_)
            self.setMachineCurrent(obj_)
        elif child_.nodeType == Node.ELEMENT_NODE and nodeName_ == "maskFile":
            obj_ = XSDataImage()
            obj_.build(child_)
            self.setMaskFile(obj_)
        elif (
            child_.nodeType == Node.ELEMENT_NODE and nodeName_ == "normalizationFactor"
        ):
            obj_ = XSDataDouble()
            obj_.build(child_)
            self.setNormalizationFactor(obj_)
        elif child_.nodeType == Node.ELEMENT_NODE and nodeName_ == "storageTemperature":
            obj_ = XSDataDouble()
            obj_.build(child_)
            self.setStorageTemperature(obj_)
        elif (
            child_.nodeType == Node.ELEMENT_NODE and nodeName_ == "exposureTemperature"
        ):
            obj_ = XSDataDouble()
            obj_.build(child_)
            self.setExposureTemperature(obj_)
        elif child_.nodeType == Node.ELEMENT_NODE and nodeName_ == "exposureTime":
            obj_ = XSDataTime()
            obj_.build(child_)
            self.setExposureTime(obj_)
        elif child_.nodeType == Node.ELEMENT_NODE and nodeName_ == "frameNumber":
            obj_ = XSDataInteger()
            obj_.build(child_)
            self.setFrameNumber(obj_)
        elif child_.nodeType == Node.ELEMENT_NODE and nodeName_ == "frameMax":
            obj_ = XSDataInteger()
            obj_.build(child_)
            self.setFrameMax(obj_)
        elif child_.nodeType == Node.ELEMENT_NODE and nodeName_ == "timeOfFrame":
            obj_ = XSDataTime()
            obj_.build(child_)
            self.setTimeOfFrame(obj_)
        XSDataInputBioSaxsSample.buildChildren(self, child_, nodeName_)

    # Method for marshalling an object
    def marshal(self):
        oStreamString = StringIO()
        oStreamString.write(unicode('<?xml version="1.0" ?>\n'))
        self.export(oStreamString, 0, name_="XSDataInputBioSaxsSampleExperiment")
        oStringXML = oStreamString.getvalue()
        oStreamString.close()
        return oStringXML

    # Only to export the entire XML tree to a file stream on disk
    def exportToFile(self, _outfileName):
        outfile = open(_outfileName, "w")
        outfile.write(unicode('<?xml version="1.0" ?>\n'))
        self.export(outfile, 0, name_="XSDataInputBioSaxsSampleExperiment")
        outfile.close()

    # Deprecated method, replaced by exportToFile
    def outputFile(self, _outfileName):
        print(
            "WARNING: Method outputFile in class XSDataInputBioSaxsSampleExperiment is deprecated, please use instead exportToFile!"
        )
        self.exportToFile(_outfileName)

    # Method for making a copy in a new instance
    def copy(self):
        return XSDataInputBioSaxsSampleExperiment.parseString(self.marshal())

    # Static method for parsing a string
    def parseString(_inString):
        doc = minidom.parseString(_inString)
        rootNode = doc.documentElement
        rootObj = XSDataInputBioSaxsSampleExperiment()
        rootObj.build(rootNode)
        # Check that all minOccurs are obeyed by marshalling the created object
        oStreamString = StringIO()
        rootObj.export(oStreamString, 0, name_="XSDataInputBioSaxsSampleExperiment")
        oStreamString.close()
        return rootObj

    parseString = staticmethod(parseString)
    # Static method for parsing a file
    def parseFile(_inFilePath):
        doc = minidom.parse(_inFilePath)
        rootNode = doc.documentElement
        rootObj = XSDataInputBioSaxsSampleExperiment()
        rootObj.build(rootNode)
        return rootObj

    parseFile = staticmethod(parseFile)


# end class XSDataInputBioSaxsSampleExperiment


class XSDataResultBioSaxsHPLCv1_0(XSDataResultBioSaxsProcessOneFilev1_0):
    """Plugin that runs subsequently ProcessOneFile, subtraction of buffer and SaxsAnalysis"""

    def __init__(
        self,
        status=None,
        dataStdErr=None,
        dataI=None,
        dataQ=None,
        experimentSetup=None,
        sample=None,
        integratedCurve=None,
        integratedImage=None,
        normalizedImage=None,
        rti=None,
        timeStamp=None,
        summedIntensity=None,
        hplcImage=None,
        mergedCurves=None,
        hplcFile=None,
        volume=None,
        gnom=None,
        autoRg=None,
        subtractedCurve=None,
        bufferCurve=None,
    ):
        XSDataResultBioSaxsProcessOneFilev1_0.__init__(
            self,
            status,
            dataStdErr,
            dataI,
            dataQ,
            experimentSetup,
            sample,
            integratedCurve,
            integratedImage,
            normalizedImage,
        )
        if bufferCurve is None:
            self._bufferCurve = None
        elif bufferCurve.__class__.__name__ == "XSDataFile":
            self._bufferCurve = bufferCurve
        else:
            strMessage = (
                "ERROR! XSDataResultBioSaxsHPLCv1_0 constructor argument 'bufferCurve' is not XSDataFile but %s"
                % self._bufferCurve.__class__.__name__
            )
            raise BaseException(strMessage)
        if subtractedCurve is None:
            self._subtractedCurve = None
        elif subtractedCurve.__class__.__name__ == "XSDataFile":
            self._subtractedCurve = subtractedCurve
        else:
            strMessage = (
                "ERROR! XSDataResultBioSaxsHPLCv1_0 constructor argument 'subtractedCurve' is not XSDataFile but %s"
                % self._subtractedCurve.__class__.__name__
            )
            raise BaseException(strMessage)
        if autoRg is None:
            self._autoRg = None
        elif autoRg.__class__.__name__ == "XSDataAutoRg":
            self._autoRg = autoRg
        else:
            strMessage = (
                "ERROR! XSDataResultBioSaxsHPLCv1_0 constructor argument 'autoRg' is not XSDataAutoRg but %s"
                % self._autoRg.__class__.__name__
            )
            raise BaseException(strMessage)
        if gnom is None:
            self._gnom = None
        elif gnom.__class__.__name__ == "XSDataGnom":
            self._gnom = gnom
        else:
            strMessage = (
                "ERROR! XSDataResultBioSaxsHPLCv1_0 constructor argument 'gnom' is not XSDataGnom but %s"
                % self._gnom.__class__.__name__
            )
            raise BaseException(strMessage)
        if volume is None:
            self._volume = None
        elif volume.__class__.__name__ == "XSDataDoubleWithUnit":
            self._volume = volume
        else:
            strMessage = (
                "ERROR! XSDataResultBioSaxsHPLCv1_0 constructor argument 'volume' is not XSDataDoubleWithUnit but %s"
                % self._volume.__class__.__name__
            )
            raise BaseException(strMessage)
        if hplcFile is None:
            self._hplcFile = None
        elif hplcFile.__class__.__name__ == "XSDataFile":
            self._hplcFile = hplcFile
        else:
            strMessage = (
                "ERROR! XSDataResultBioSaxsHPLCv1_0 constructor argument 'hplcFile' is not XSDataFile but %s"
                % self._hplcFile.__class__.__name__
            )
            raise BaseException(strMessage)
        if mergedCurves is None:
            self._mergedCurves = []
        elif mergedCurves.__class__.__name__ == "list":
            self._mergedCurves = mergedCurves
        else:
            strMessage = (
                "ERROR! XSDataResultBioSaxsHPLCv1_0 constructor argument 'mergedCurves' is not list but %s"
                % self._mergedCurves.__class__.__name__
            )
            raise BaseException(strMessage)
        if hplcImage is None:
            self._hplcImage = None
        elif hplcImage.__class__.__name__ == "XSDataFile":
            self._hplcImage = hplcImage
        else:
            strMessage = (
                "ERROR! XSDataResultBioSaxsHPLCv1_0 constructor argument 'hplcImage' is not XSDataFile but %s"
                % self._hplcImage.__class__.__name__
            )
            raise BaseException(strMessage)
        if summedIntensity is None:
            self._summedIntensity = None
        elif summedIntensity.__class__.__name__ == "XSDataDouble":
            self._summedIntensity = summedIntensity
        else:
            strMessage = (
                "ERROR! XSDataResultBioSaxsHPLCv1_0 constructor argument 'summedIntensity' is not XSDataDouble but %s"
                % self._summedIntensity.__class__.__name__
            )
            raise BaseException(strMessage)
        if timeStamp is None:
            self._timeStamp = None
        elif timeStamp.__class__.__name__ == "XSDataTime":
            self._timeStamp = timeStamp
        else:
            strMessage = (
                "ERROR! XSDataResultBioSaxsHPLCv1_0 constructor argument 'timeStamp' is not XSDataTime but %s"
                % self._timeStamp.__class__.__name__
            )
            raise BaseException(strMessage)
        if rti is None:
            self._rti = None
        elif rti.__class__.__name__ == "XSDataRamboTainer":
            self._rti = rti
        else:
            strMessage = (
                "ERROR! XSDataResultBioSaxsHPLCv1_0 constructor argument 'rti' is not XSDataRamboTainer but %s"
                % self._rti.__class__.__name__
            )
            raise BaseException(strMessage)

    # Methods and properties for the 'bufferCurve' attribute
    def getBufferCurve(self):
        return self._bufferCurve

    def setBufferCurve(self, bufferCurve):
        if bufferCurve is None:
            self._bufferCurve = None
        elif bufferCurve.__class__.__name__ == "XSDataFile":
            self._bufferCurve = bufferCurve
        else:
            strMessage = (
                "ERROR! XSDataResultBioSaxsHPLCv1_0.setBufferCurve argument is not XSDataFile but %s"
                % bufferCurve.__class__.__name__
            )
            raise BaseException(strMessage)

    def delBufferCurve(self):
        self._bufferCurve = None

    bufferCurve = property(
        getBufferCurve, setBufferCurve, delBufferCurve, "Property for bufferCurve"
    )
    # Methods and properties for the 'subtractedCurve' attribute
    def getSubtractedCurve(self):
        return self._subtractedCurve

    def setSubtractedCurve(self, subtractedCurve):
        if subtractedCurve is None:
            self._subtractedCurve = None
        elif subtractedCurve.__class__.__name__ == "XSDataFile":
            self._subtractedCurve = subtractedCurve
        else:
            strMessage = (
                "ERROR! XSDataResultBioSaxsHPLCv1_0.setSubtractedCurve argument is not XSDataFile but %s"
                % subtractedCurve.__class__.__name__
            )
            raise BaseException(strMessage)

    def delSubtractedCurve(self):
        self._subtractedCurve = None

    subtractedCurve = property(
        getSubtractedCurve,
        setSubtractedCurve,
        delSubtractedCurve,
        "Property for subtractedCurve",
    )
    # Methods and properties for the 'autoRg' attribute
    def getAutoRg(self):
        return self._autoRg

    def setAutoRg(self, autoRg):
        if autoRg is None:
            self._autoRg = None
        elif autoRg.__class__.__name__ == "XSDataAutoRg":
            self._autoRg = autoRg
        else:
            strMessage = (
                "ERROR! XSDataResultBioSaxsHPLCv1_0.setAutoRg argument is not XSDataAutoRg but %s"
                % autoRg.__class__.__name__
            )
            raise BaseException(strMessage)

    def delAutoRg(self):
        self._autoRg = None

    autoRg = property(getAutoRg, setAutoRg, delAutoRg, "Property for autoRg")
    # Methods and properties for the 'gnom' attribute
    def getGnom(self):
        return self._gnom

    def setGnom(self, gnom):
        if gnom is None:
            self._gnom = None
        elif gnom.__class__.__name__ == "XSDataGnom":
            self._gnom = gnom
        else:
            strMessage = (
                "ERROR! XSDataResultBioSaxsHPLCv1_0.setGnom argument is not XSDataGnom but %s"
                % gnom.__class__.__name__
            )
            raise BaseException(strMessage)

    def delGnom(self):
        self._gnom = None

    gnom = property(getGnom, setGnom, delGnom, "Property for gnom")
    # Methods and properties for the 'volume' attribute
    def getVolume(self):
        return self._volume

    def setVolume(self, volume):
        if volume is None:
            self._volume = None
        elif volume.__class__.__name__ == "XSDataDoubleWithUnit":
            self._volume = volume
        else:
            strMessage = (
                "ERROR! XSDataResultBioSaxsHPLCv1_0.setVolume argument is not XSDataDoubleWithUnit but %s"
                % volume.__class__.__name__
            )
            raise BaseException(strMessage)

    def delVolume(self):
        self._volume = None

    volume = property(getVolume, setVolume, delVolume, "Property for volume")
    # Methods and properties for the 'hplcFile' attribute
    def getHplcFile(self):
        return self._hplcFile

    def setHplcFile(self, hplcFile):
        if hplcFile is None:
            self._hplcFile = None
        elif hplcFile.__class__.__name__ == "XSDataFile":
            self._hplcFile = hplcFile
        else:
            strMessage = (
                "ERROR! XSDataResultBioSaxsHPLCv1_0.setHplcFile argument is not XSDataFile but %s"
                % hplcFile.__class__.__name__
            )
            raise BaseException(strMessage)

    def delHplcFile(self):
        self._hplcFile = None

    hplcFile = property(getHplcFile, setHplcFile, delHplcFile, "Property for hplcFile")
    # Methods and properties for the 'mergedCurves' attribute
    def getMergedCurves(self):
        return self._mergedCurves

    def setMergedCurves(self, mergedCurves):
        if mergedCurves is None:
            self._mergedCurves = []
        elif mergedCurves.__class__.__name__ == "list":
            self._mergedCurves = mergedCurves
        else:
            strMessage = (
                "ERROR! XSDataResultBioSaxsHPLCv1_0.setMergedCurves argument is not list but %s"
                % mergedCurves.__class__.__name__
            )
            raise BaseException(strMessage)

    def delMergedCurves(self):
        self._mergedCurves = None

    mergedCurves = property(
        getMergedCurves, setMergedCurves, delMergedCurves, "Property for mergedCurves"
    )

    def addMergedCurves(self, value):
        if value is None:
            strMessage = (
                "ERROR! XSDataResultBioSaxsHPLCv1_0.addMergedCurves argument is None"
            )
            raise BaseException(strMessage)
        elif value.__class__.__name__ == "XSDataFile":
            self._mergedCurves.append(value)
        else:
            strMessage = (
                "ERROR! XSDataResultBioSaxsHPLCv1_0.addMergedCurves argument is not XSDataFile but %s"
                % value.__class__.__name__
            )
            raise BaseException(strMessage)

    def insertMergedCurves(self, index, value):
        if index is None:
            strMessage = "ERROR! XSDataResultBioSaxsHPLCv1_0.insertMergedCurves argument 'index' is None"
            raise BaseException(strMessage)
        if value is None:
            strMessage = "ERROR! XSDataResultBioSaxsHPLCv1_0.insertMergedCurves argument 'value' is None"
            raise BaseException(strMessage)
        elif value.__class__.__name__ == "XSDataFile":
            self._mergedCurves[index] = value
        else:
            strMessage = (
                "ERROR! XSDataResultBioSaxsHPLCv1_0.addMergedCurves argument is not XSDataFile but %s"
                % value.__class__.__name__
            )
            raise BaseException(strMessage)

    # Methods and properties for the 'hplcImage' attribute
    def getHplcImage(self):
        return self._hplcImage

    def setHplcImage(self, hplcImage):
        if hplcImage is None:
            self._hplcImage = None
        elif hplcImage.__class__.__name__ == "XSDataFile":
            self._hplcImage = hplcImage
        else:
            strMessage = (
                "ERROR! XSDataResultBioSaxsHPLCv1_0.setHplcImage argument is not XSDataFile but %s"
                % hplcImage.__class__.__name__
            )
            raise BaseException(strMessage)

    def delHplcImage(self):
        self._hplcImage = None

    hplcImage = property(
        getHplcImage, setHplcImage, delHplcImage, "Property for hplcImage"
    )
    # Methods and properties for the 'summedIntensity' attribute
    def getSummedIntensity(self):
        return self._summedIntensity

    def setSummedIntensity(self, summedIntensity):
        if summedIntensity is None:
            self._summedIntensity = None
        elif summedIntensity.__class__.__name__ == "XSDataDouble":
            self._summedIntensity = summedIntensity
        else:
            strMessage = (
                "ERROR! XSDataResultBioSaxsHPLCv1_0.setSummedIntensity argument is not XSDataDouble but %s"
                % summedIntensity.__class__.__name__
            )
            raise BaseException(strMessage)

    def delSummedIntensity(self):
        self._summedIntensity = None

    summedIntensity = property(
        getSummedIntensity,
        setSummedIntensity,
        delSummedIntensity,
        "Property for summedIntensity",
    )
    # Methods and properties for the 'timeStamp' attribute
    def getTimeStamp(self):
        return self._timeStamp

    def setTimeStamp(self, timeStamp):
        if timeStamp is None:
            self._timeStamp = None
        elif timeStamp.__class__.__name__ == "XSDataTime":
            self._timeStamp = timeStamp
        else:
            strMessage = (
                "ERROR! XSDataResultBioSaxsHPLCv1_0.setTimeStamp argument is not XSDataTime but %s"
                % timeStamp.__class__.__name__
            )
            raise BaseException(strMessage)

    def delTimeStamp(self):
        self._timeStamp = None

    timeStamp = property(
        getTimeStamp, setTimeStamp, delTimeStamp, "Property for timeStamp"
    )
    # Methods and properties for the 'rti' attribute
    def getRti(self):
        return self._rti

    def setRti(self, rti):
        if rti is None:
            self._rti = None
        elif rti.__class__.__name__ == "XSDataRamboTainer":
            self._rti = rti
        else:
            strMessage = (
                "ERROR! XSDataResultBioSaxsHPLCv1_0.setRti argument is not XSDataRamboTainer but %s"
                % rti.__class__.__name__
            )
            raise BaseException(strMessage)

    def delRti(self):
        self._rti = None

    rti = property(getRti, setRti, delRti, "Property for rti")

    def export(self, outfile, level, name_="XSDataResultBioSaxsHPLCv1_0"):
        showIndent(outfile, level)
        outfile.write(unicode("<%s>\n" % name_))
        self.exportChildren(outfile, level + 1, name_)
        showIndent(outfile, level)
        outfile.write(unicode("</%s>\n" % name_))

    def exportChildren(self, outfile, level, name_="XSDataResultBioSaxsHPLCv1_0"):
        XSDataResultBioSaxsProcessOneFilev1_0.exportChildren(
            self, outfile, level, name_
        )
        if self._bufferCurve is not None:
            self.bufferCurve.export(outfile, level, name_="bufferCurve")
        if self._subtractedCurve is not None:
            self.subtractedCurve.export(outfile, level, name_="subtractedCurve")
        if self._autoRg is not None:
            self.autoRg.export(outfile, level, name_="autoRg")
        if self._gnom is not None:
            self.gnom.export(outfile, level, name_="gnom")
        if self._volume is not None:
            self.volume.export(outfile, level, name_="volume")
        if self._hplcFile is not None:
            self.hplcFile.export(outfile, level, name_="hplcFile")
        for mergedCurves_ in self.getMergedCurves():
            mergedCurves_.export(outfile, level, name_="mergedCurves")
        if self._hplcImage is not None:
            self.hplcImage.export(outfile, level, name_="hplcImage")
        if self._summedIntensity is not None:
            self.summedIntensity.export(outfile, level, name_="summedIntensity")
        if self._timeStamp is not None:
            self.timeStamp.export(outfile, level, name_="timeStamp")
        if self._rti is not None:
            self.rti.export(outfile, level, name_="rti")

    def build(self, node_):
        for child_ in node_.childNodes:
            nodeName_ = child_.nodeName.split(":")[-1]
            self.buildChildren(child_, nodeName_)

    def buildChildren(self, child_, nodeName_):
        if child_.nodeType == Node.ELEMENT_NODE and nodeName_ == "bufferCurve":
            obj_ = XSDataFile()
            obj_.build(child_)
            self.setBufferCurve(obj_)
        elif child_.nodeType == Node.ELEMENT_NODE and nodeName_ == "subtractedCurve":
            obj_ = XSDataFile()
            obj_.build(child_)
            self.setSubtractedCurve(obj_)
        elif child_.nodeType == Node.ELEMENT_NODE and nodeName_ == "autoRg":
            obj_ = XSDataAutoRg()
            obj_.build(child_)
            self.setAutoRg(obj_)
        elif child_.nodeType == Node.ELEMENT_NODE and nodeName_ == "gnom":
            obj_ = XSDataGnom()
            obj_.build(child_)
            self.setGnom(obj_)
        elif child_.nodeType == Node.ELEMENT_NODE and nodeName_ == "volume":
            obj_ = XSDataDoubleWithUnit()
            obj_.build(child_)
            self.setVolume(obj_)
        elif child_.nodeType == Node.ELEMENT_NODE and nodeName_ == "hplcFile":
            obj_ = XSDataFile()
            obj_.build(child_)
            self.setHplcFile(obj_)
        elif child_.nodeType == Node.ELEMENT_NODE and nodeName_ == "mergedCurves":
            obj_ = XSDataFile()
            obj_.build(child_)
            self.mergedCurves.append(obj_)
        elif child_.nodeType == Node.ELEMENT_NODE and nodeName_ == "hplcImage":
            obj_ = XSDataFile()
            obj_.build(child_)
            self.setHplcImage(obj_)
        elif child_.nodeType == Node.ELEMENT_NODE and nodeName_ == "summedIntensity":
            obj_ = XSDataDouble()
            obj_.build(child_)
            self.setSummedIntensity(obj_)
        elif child_.nodeType == Node.ELEMENT_NODE and nodeName_ == "timeStamp":
            obj_ = XSDataTime()
            obj_.build(child_)
            self.setTimeStamp(obj_)
        elif child_.nodeType == Node.ELEMENT_NODE and nodeName_ == "rti":
            obj_ = XSDataRamboTainer()
            obj_.build(child_)
            self.setRti(obj_)
        XSDataResultBioSaxsProcessOneFilev1_0.buildChildren(self, child_, nodeName_)

    # Method for marshalling an object
    def marshal(self):
        oStreamString = StringIO()
        oStreamString.write(unicode('<?xml version="1.0" ?>\n'))
        self.export(oStreamString, 0, name_="XSDataResultBioSaxsHPLCv1_0")
        oStringXML = oStreamString.getvalue()
        oStreamString.close()
        return oStringXML

    # Only to export the entire XML tree to a file stream on disk
    def exportToFile(self, _outfileName):
        outfile = open(_outfileName, "w")
        outfile.write(unicode('<?xml version="1.0" ?>\n'))
        self.export(outfile, 0, name_="XSDataResultBioSaxsHPLCv1_0")
        outfile.close()

    # Deprecated method, replaced by exportToFile
    def outputFile(self, _outfileName):
        print(
            "WARNING: Method outputFile in class XSDataResultBioSaxsHPLCv1_0 is deprecated, please use instead exportToFile!"
        )
        self.exportToFile(_outfileName)

    # Method for making a copy in a new instance
    def copy(self):
        return XSDataResultBioSaxsHPLCv1_0.parseString(self.marshal())

    # Static method for parsing a string
    def parseString(_inString):
        doc = minidom.parseString(_inString)
        rootNode = doc.documentElement
        rootObj = XSDataResultBioSaxsHPLCv1_0()
        rootObj.build(rootNode)
        # Check that all minOccurs are obeyed by marshalling the created object
        oStreamString = StringIO()
        rootObj.export(oStreamString, 0, name_="XSDataResultBioSaxsHPLCv1_0")
        oStreamString.close()
        return rootObj

    parseString = staticmethod(parseString)
    # Static method for parsing a file
    def parseFile(_inFilePath):
        doc = minidom.parse(_inFilePath)
        rootNode = doc.documentElement
        rootObj = XSDataResultBioSaxsHPLCv1_0()
        rootObj.build(rootNode)
        return rootObj

    parseFile = staticmethod(parseFile)


# end class XSDataResultBioSaxsHPLCv1_0


class XSDataResultBioSaxsSampleExperiment(XSDataResultBioSaxsSample):
    """temporary class for multiple inhertitance emulation"""

    def __init__(
        self,
        status=None,
        code=None,
        comments=None,
        concentration=None,
        timeOfFrame=None,
        frameMax=None,
        frameNumber=None,
        exposureTime=None,
        exposureTemperature=None,
        storageTemperature=None,
        normalizationFactor=None,
        maskFile=None,
        machineCurrent=None,
        wavelength=None,
        beamStopDiode=None,
        beamCenter_2=None,
        beamCenter_1=None,
        pixelSize_2=None,
        pixelSize_1=None,
        detectorDistance=None,
        detector=None,
    ):
        XSDataResultBioSaxsSample.__init__(self, status, code, comments, concentration)
        if detector is None:
            self._detector = None
        elif detector.__class__.__name__ == "XSDataString":
            self._detector = detector
        else:
            strMessage = (
                "ERROR! XSDataResultBioSaxsSampleExperiment constructor argument 'detector' is not XSDataString but %s"
                % self._detector.__class__.__name__
            )
            raise BaseException(strMessage)
        if detectorDistance is None:
            self._detectorDistance = None
        elif detectorDistance.__class__.__name__ == "XSDataLength":
            self._detectorDistance = detectorDistance
        else:
            strMessage = (
                "ERROR! XSDataResultBioSaxsSampleExperiment constructor argument 'detectorDistance' is not XSDataLength but %s"
                % self._detectorDistance.__class__.__name__
            )
            raise BaseException(strMessage)
        if pixelSize_1 is None:
            self._pixelSize_1 = None
        elif pixelSize_1.__class__.__name__ == "XSDataLength":
            self._pixelSize_1 = pixelSize_1
        else:
            strMessage = (
                "ERROR! XSDataResultBioSaxsSampleExperiment constructor argument 'pixelSize_1' is not XSDataLength but %s"
                % self._pixelSize_1.__class__.__name__
            )
            raise BaseException(strMessage)
        if pixelSize_2 is None:
            self._pixelSize_2 = None
        elif pixelSize_2.__class__.__name__ == "XSDataLength":
            self._pixelSize_2 = pixelSize_2
        else:
            strMessage = (
                "ERROR! XSDataResultBioSaxsSampleExperiment constructor argument 'pixelSize_2' is not XSDataLength but %s"
                % self._pixelSize_2.__class__.__name__
            )
            raise BaseException(strMessage)
        if beamCenter_1 is None:
            self._beamCenter_1 = None
        elif beamCenter_1.__class__.__name__ == "XSDataDouble":
            self._beamCenter_1 = beamCenter_1
        else:
            strMessage = (
                "ERROR! XSDataResultBioSaxsSampleExperiment constructor argument 'beamCenter_1' is not XSDataDouble but %s"
                % self._beamCenter_1.__class__.__name__
            )
            raise BaseException(strMessage)
        if beamCenter_2 is None:
            self._beamCenter_2 = None
        elif beamCenter_2.__class__.__name__ == "XSDataDouble":
            self._beamCenter_2 = beamCenter_2
        else:
            strMessage = (
                "ERROR! XSDataResultBioSaxsSampleExperiment constructor argument 'beamCenter_2' is not XSDataDouble but %s"
                % self._beamCenter_2.__class__.__name__
            )
            raise BaseException(strMessage)
        if beamStopDiode is None:
            self._beamStopDiode = None
        elif beamStopDiode.__class__.__name__ == "XSDataDouble":
            self._beamStopDiode = beamStopDiode
        else:
            strMessage = (
                "ERROR! XSDataResultBioSaxsSampleExperiment constructor argument 'beamStopDiode' is not XSDataDouble but %s"
                % self._beamStopDiode.__class__.__name__
            )
            raise BaseException(strMessage)
        if wavelength is None:
            self._wavelength = None
        elif wavelength.__class__.__name__ == "XSDataWavelength":
            self._wavelength = wavelength
        else:
            strMessage = (
                "ERROR! XSDataResultBioSaxsSampleExperiment constructor argument 'wavelength' is not XSDataWavelength but %s"
                % self._wavelength.__class__.__name__
            )
            raise BaseException(strMessage)
        if machineCurrent is None:
            self._machineCurrent = None
        elif machineCurrent.__class__.__name__ == "XSDataDouble":
            self._machineCurrent = machineCurrent
        else:
            strMessage = (
                "ERROR! XSDataResultBioSaxsSampleExperiment constructor argument 'machineCurrent' is not XSDataDouble but %s"
                % self._machineCurrent.__class__.__name__
            )
            raise BaseException(strMessage)
        if maskFile is None:
            self._maskFile = None
        elif maskFile.__class__.__name__ == "XSDataImage":
            self._maskFile = maskFile
        else:
            strMessage = (
                "ERROR! XSDataResultBioSaxsSampleExperiment constructor argument 'maskFile' is not XSDataImage but %s"
                % self._maskFile.__class__.__name__
            )
            raise BaseException(strMessage)
        if normalizationFactor is None:
            self._normalizationFactor = None
        elif normalizationFactor.__class__.__name__ == "XSDataDouble":
            self._normalizationFactor = normalizationFactor
        else:
            strMessage = (
                "ERROR! XSDataResultBioSaxsSampleExperiment constructor argument 'normalizationFactor' is not XSDataDouble but %s"
                % self._normalizationFactor.__class__.__name__
            )
            raise BaseException(strMessage)
        if storageTemperature is None:
            self._storageTemperature = None
        elif storageTemperature.__class__.__name__ == "XSDataDouble":
            self._storageTemperature = storageTemperature
        else:
            strMessage = (
                "ERROR! XSDataResultBioSaxsSampleExperiment constructor argument 'storageTemperature' is not XSDataDouble but %s"
                % self._storageTemperature.__class__.__name__
            )
            raise BaseException(strMessage)
        if exposureTemperature is None:
            self._exposureTemperature = None
        elif exposureTemperature.__class__.__name__ == "XSDataDouble":
            self._exposureTemperature = exposureTemperature
        else:
            strMessage = (
                "ERROR! XSDataResultBioSaxsSampleExperiment constructor argument 'exposureTemperature' is not XSDataDouble but %s"
                % self._exposureTemperature.__class__.__name__
            )
            raise BaseException(strMessage)
        if exposureTime is None:
            self._exposureTime = None
        elif exposureTime.__class__.__name__ == "XSDataTime":
            self._exposureTime = exposureTime
        else:
            strMessage = (
                "ERROR! XSDataResultBioSaxsSampleExperiment constructor argument 'exposureTime' is not XSDataTime but %s"
                % self._exposureTime.__class__.__name__
            )
            raise BaseException(strMessage)
        if frameNumber is None:
            self._frameNumber = None
        elif frameNumber.__class__.__name__ == "XSDataInteger":
            self._frameNumber = frameNumber
        else:
            strMessage = (
                "ERROR! XSDataResultBioSaxsSampleExperiment constructor argument 'frameNumber' is not XSDataInteger but %s"
                % self._frameNumber.__class__.__name__
            )
            raise BaseException(strMessage)
        if frameMax is None:
            self._frameMax = None
        elif frameMax.__class__.__name__ == "XSDataInteger":
            self._frameMax = frameMax
        else:
            strMessage = (
                "ERROR! XSDataResultBioSaxsSampleExperiment constructor argument 'frameMax' is not XSDataInteger but %s"
                % self._frameMax.__class__.__name__
            )
            raise BaseException(strMessage)
        if timeOfFrame is None:
            self._timeOfFrame = None
        elif timeOfFrame.__class__.__name__ == "XSDataTime":
            self._timeOfFrame = timeOfFrame
        else:
            strMessage = (
                "ERROR! XSDataResultBioSaxsSampleExperiment constructor argument 'timeOfFrame' is not XSDataTime but %s"
                % self._timeOfFrame.__class__.__name__
            )
            raise BaseException(strMessage)

    # Methods and properties for the 'detector' attribute
    def getDetector(self):
        return self._detector

    def setDetector(self, detector):
        if detector is None:
            self._detector = None
        elif detector.__class__.__name__ == "XSDataString":
            self._detector = detector
        else:
            strMessage = (
                "ERROR! XSDataResultBioSaxsSampleExperiment.setDetector argument is not XSDataString but %s"
                % detector.__class__.__name__
            )
            raise BaseException(strMessage)

    def delDetector(self):
        self._detector = None

    detector = property(getDetector, setDetector, delDetector, "Property for detector")
    # Methods and properties for the 'detectorDistance' attribute
    def getDetectorDistance(self):
        return self._detectorDistance

    def setDetectorDistance(self, detectorDistance):
        if detectorDistance is None:
            self._detectorDistance = None
        elif detectorDistance.__class__.__name__ == "XSDataLength":
            self._detectorDistance = detectorDistance
        else:
            strMessage = (
                "ERROR! XSDataResultBioSaxsSampleExperiment.setDetectorDistance argument is not XSDataLength but %s"
                % detectorDistance.__class__.__name__
            )
            raise BaseException(strMessage)

    def delDetectorDistance(self):
        self._detectorDistance = None

    detectorDistance = property(
        getDetectorDistance,
        setDetectorDistance,
        delDetectorDistance,
        "Property for detectorDistance",
    )
    # Methods and properties for the 'pixelSize_1' attribute
    def getPixelSize_1(self):
        return self._pixelSize_1

    def setPixelSize_1(self, pixelSize_1):
        if pixelSize_1 is None:
            self._pixelSize_1 = None
        elif pixelSize_1.__class__.__name__ == "XSDataLength":
            self._pixelSize_1 = pixelSize_1
        else:
            strMessage = (
                "ERROR! XSDataResultBioSaxsSampleExperiment.setPixelSize_1 argument is not XSDataLength but %s"
                % pixelSize_1.__class__.__name__
            )
            raise BaseException(strMessage)

    def delPixelSize_1(self):
        self._pixelSize_1 = None

    pixelSize_1 = property(
        getPixelSize_1, setPixelSize_1, delPixelSize_1, "Property for pixelSize_1"
    )
    # Methods and properties for the 'pixelSize_2' attribute
    def getPixelSize_2(self):
        return self._pixelSize_2

    def setPixelSize_2(self, pixelSize_2):
        if pixelSize_2 is None:
            self._pixelSize_2 = None
        elif pixelSize_2.__class__.__name__ == "XSDataLength":
            self._pixelSize_2 = pixelSize_2
        else:
            strMessage = (
                "ERROR! XSDataResultBioSaxsSampleExperiment.setPixelSize_2 argument is not XSDataLength but %s"
                % pixelSize_2.__class__.__name__
            )
            raise BaseException(strMessage)

    def delPixelSize_2(self):
        self._pixelSize_2 = None

    pixelSize_2 = property(
        getPixelSize_2, setPixelSize_2, delPixelSize_2, "Property for pixelSize_2"
    )
    # Methods and properties for the 'beamCenter_1' attribute
    def getBeamCenter_1(self):
        return self._beamCenter_1

    def setBeamCenter_1(self, beamCenter_1):
        if beamCenter_1 is None:
            self._beamCenter_1 = None
        elif beamCenter_1.__class__.__name__ == "XSDataDouble":
            self._beamCenter_1 = beamCenter_1
        else:
            strMessage = (
                "ERROR! XSDataResultBioSaxsSampleExperiment.setBeamCenter_1 argument is not XSDataDouble but %s"
                % beamCenter_1.__class__.__name__
            )
            raise BaseException(strMessage)

    def delBeamCenter_1(self):
        self._beamCenter_1 = None

    beamCenter_1 = property(
        getBeamCenter_1, setBeamCenter_1, delBeamCenter_1, "Property for beamCenter_1"
    )
    # Methods and properties for the 'beamCenter_2' attribute
    def getBeamCenter_2(self):
        return self._beamCenter_2

    def setBeamCenter_2(self, beamCenter_2):
        if beamCenter_2 is None:
            self._beamCenter_2 = None
        elif beamCenter_2.__class__.__name__ == "XSDataDouble":
            self._beamCenter_2 = beamCenter_2
        else:
            strMessage = (
                "ERROR! XSDataResultBioSaxsSampleExperiment.setBeamCenter_2 argument is not XSDataDouble but %s"
                % beamCenter_2.__class__.__name__
            )
            raise BaseException(strMessage)

    def delBeamCenter_2(self):
        self._beamCenter_2 = None

    beamCenter_2 = property(
        getBeamCenter_2, setBeamCenter_2, delBeamCenter_2, "Property for beamCenter_2"
    )
    # Methods and properties for the 'beamStopDiode' attribute
    def getBeamStopDiode(self):
        return self._beamStopDiode

    def setBeamStopDiode(self, beamStopDiode):
        if beamStopDiode is None:
            self._beamStopDiode = None
        elif beamStopDiode.__class__.__name__ == "XSDataDouble":
            self._beamStopDiode = beamStopDiode
        else:
            strMessage = (
                "ERROR! XSDataResultBioSaxsSampleExperiment.setBeamStopDiode argument is not XSDataDouble but %s"
                % beamStopDiode.__class__.__name__
            )
            raise BaseException(strMessage)

    def delBeamStopDiode(self):
        self._beamStopDiode = None

    beamStopDiode = property(
        getBeamStopDiode,
        setBeamStopDiode,
        delBeamStopDiode,
        "Property for beamStopDiode",
    )
    # Methods and properties for the 'wavelength' attribute
    def getWavelength(self):
        return self._wavelength

    def setWavelength(self, wavelength):
        if wavelength is None:
            self._wavelength = None
        elif wavelength.__class__.__name__ == "XSDataWavelength":
            self._wavelength = wavelength
        else:
            strMessage = (
                "ERROR! XSDataResultBioSaxsSampleExperiment.setWavelength argument is not XSDataWavelength but %s"
                % wavelength.__class__.__name__
            )
            raise BaseException(strMessage)

    def delWavelength(self):
        self._wavelength = None

    wavelength = property(
        getWavelength, setWavelength, delWavelength, "Property for wavelength"
    )
    # Methods and properties for the 'machineCurrent' attribute
    def getMachineCurrent(self):
        return self._machineCurrent

    def setMachineCurrent(self, machineCurrent):
        if machineCurrent is None:
            self._machineCurrent = None
        elif machineCurrent.__class__.__name__ == "XSDataDouble":
            self._machineCurrent = machineCurrent
        else:
            strMessage = (
                "ERROR! XSDataResultBioSaxsSampleExperiment.setMachineCurrent argument is not XSDataDouble but %s"
                % machineCurrent.__class__.__name__
            )
            raise BaseException(strMessage)

    def delMachineCurrent(self):
        self._machineCurrent = None

    machineCurrent = property(
        getMachineCurrent,
        setMachineCurrent,
        delMachineCurrent,
        "Property for machineCurrent",
    )
    # Methods and properties for the 'maskFile' attribute
    def getMaskFile(self):
        return self._maskFile

    def setMaskFile(self, maskFile):
        if maskFile is None:
            self._maskFile = None
        elif maskFile.__class__.__name__ == "XSDataImage":
            self._maskFile = maskFile
        else:
            strMessage = (
                "ERROR! XSDataResultBioSaxsSampleExperiment.setMaskFile argument is not XSDataImage but %s"
                % maskFile.__class__.__name__
            )
            raise BaseException(strMessage)

    def delMaskFile(self):
        self._maskFile = None

    maskFile = property(getMaskFile, setMaskFile, delMaskFile, "Property for maskFile")
    # Methods and properties for the 'normalizationFactor' attribute
    def getNormalizationFactor(self):
        return self._normalizationFactor

    def setNormalizationFactor(self, normalizationFactor):
        if normalizationFactor is None:
            self._normalizationFactor = None
        elif normalizationFactor.__class__.__name__ == "XSDataDouble":
            self._normalizationFactor = normalizationFactor
        else:
            strMessage = (
                "ERROR! XSDataResultBioSaxsSampleExperiment.setNormalizationFactor argument is not XSDataDouble but %s"
                % normalizationFactor.__class__.__name__
            )
            raise BaseException(strMessage)

    def delNormalizationFactor(self):
        self._normalizationFactor = None

    normalizationFactor = property(
        getNormalizationFactor,
        setNormalizationFactor,
        delNormalizationFactor,
        "Property for normalizationFactor",
    )
    # Methods and properties for the 'storageTemperature' attribute
    def getStorageTemperature(self):
        return self._storageTemperature

    def setStorageTemperature(self, storageTemperature):
        if storageTemperature is None:
            self._storageTemperature = None
        elif storageTemperature.__class__.__name__ == "XSDataDouble":
            self._storageTemperature = storageTemperature
        else:
            strMessage = (
                "ERROR! XSDataResultBioSaxsSampleExperiment.setStorageTemperature argument is not XSDataDouble but %s"
                % storageTemperature.__class__.__name__
            )
            raise BaseException(strMessage)

    def delStorageTemperature(self):
        self._storageTemperature = None

    storageTemperature = property(
        getStorageTemperature,
        setStorageTemperature,
        delStorageTemperature,
        "Property for storageTemperature",
    )
    # Methods and properties for the 'exposureTemperature' attribute
    def getExposureTemperature(self):
        return self._exposureTemperature

    def setExposureTemperature(self, exposureTemperature):
        if exposureTemperature is None:
            self._exposureTemperature = None
        elif exposureTemperature.__class__.__name__ == "XSDataDouble":
            self._exposureTemperature = exposureTemperature
        else:
            strMessage = (
                "ERROR! XSDataResultBioSaxsSampleExperiment.setExposureTemperature argument is not XSDataDouble but %s"
                % exposureTemperature.__class__.__name__
            )
            raise BaseException(strMessage)

    def delExposureTemperature(self):
        self._exposureTemperature = None

    exposureTemperature = property(
        getExposureTemperature,
        setExposureTemperature,
        delExposureTemperature,
        "Property for exposureTemperature",
    )
    # Methods and properties for the 'exposureTime' attribute
    def getExposureTime(self):
        return self._exposureTime

    def setExposureTime(self, exposureTime):
        if exposureTime is None:
            self._exposureTime = None
        elif exposureTime.__class__.__name__ == "XSDataTime":
            self._exposureTime = exposureTime
        else:
            strMessage = (
                "ERROR! XSDataResultBioSaxsSampleExperiment.setExposureTime argument is not XSDataTime but %s"
                % exposureTime.__class__.__name__
            )
            raise BaseException(strMessage)

    def delExposureTime(self):
        self._exposureTime = None

    exposureTime = property(
        getExposureTime, setExposureTime, delExposureTime, "Property for exposureTime"
    )
    # Methods and properties for the 'frameNumber' attribute
    def getFrameNumber(self):
        return self._frameNumber

    def setFrameNumber(self, frameNumber):
        if frameNumber is None:
            self._frameNumber = None
        elif frameNumber.__class__.__name__ == "XSDataInteger":
            self._frameNumber = frameNumber
        else:
            strMessage = (
                "ERROR! XSDataResultBioSaxsSampleExperiment.setFrameNumber argument is not XSDataInteger but %s"
                % frameNumber.__class__.__name__
            )
            raise BaseException(strMessage)

    def delFrameNumber(self):
        self._frameNumber = None

    frameNumber = property(
        getFrameNumber, setFrameNumber, delFrameNumber, "Property for frameNumber"
    )
    # Methods and properties for the 'frameMax' attribute
    def getFrameMax(self):
        return self._frameMax

    def setFrameMax(self, frameMax):
        if frameMax is None:
            self._frameMax = None
        elif frameMax.__class__.__name__ == "XSDataInteger":
            self._frameMax = frameMax
        else:
            strMessage = (
                "ERROR! XSDataResultBioSaxsSampleExperiment.setFrameMax argument is not XSDataInteger but %s"
                % frameMax.__class__.__name__
            )
            raise BaseException(strMessage)

    def delFrameMax(self):
        self._frameMax = None

    frameMax = property(getFrameMax, setFrameMax, delFrameMax, "Property for frameMax")
    # Methods and properties for the 'timeOfFrame' attribute
    def getTimeOfFrame(self):
        return self._timeOfFrame

    def setTimeOfFrame(self, timeOfFrame):
        if timeOfFrame is None:
            self._timeOfFrame = None
        elif timeOfFrame.__class__.__name__ == "XSDataTime":
            self._timeOfFrame = timeOfFrame
        else:
            strMessage = (
                "ERROR! XSDataResultBioSaxsSampleExperiment.setTimeOfFrame argument is not XSDataTime but %s"
                % timeOfFrame.__class__.__name__
            )
            raise BaseException(strMessage)

    def delTimeOfFrame(self):
        self._timeOfFrame = None

    timeOfFrame = property(
        getTimeOfFrame, setTimeOfFrame, delTimeOfFrame, "Property for timeOfFrame"
    )

    def export(self, outfile, level, name_="XSDataResultBioSaxsSampleExperiment"):
        showIndent(outfile, level)
        outfile.write(unicode("<%s>\n" % name_))
        self.exportChildren(outfile, level + 1, name_)
        showIndent(outfile, level)
        outfile.write(unicode("</%s>\n" % name_))

    def exportChildren(
        self, outfile, level, name_="XSDataResultBioSaxsSampleExperiment"
    ):
        XSDataResultBioSaxsSample.exportChildren(self, outfile, level, name_)
        if self._detector is not None:
            self.detector.export(outfile, level, name_="detector")
        if self._detectorDistance is not None:
            self.detectorDistance.export(outfile, level, name_="detectorDistance")
        if self._pixelSize_1 is not None:
            self.pixelSize_1.export(outfile, level, name_="pixelSize_1")
        if self._pixelSize_2 is not None:
            self.pixelSize_2.export(outfile, level, name_="pixelSize_2")
        if self._beamCenter_1 is not None:
            self.beamCenter_1.export(outfile, level, name_="beamCenter_1")
        if self._beamCenter_2 is not None:
            self.beamCenter_2.export(outfile, level, name_="beamCenter_2")
        if self._beamStopDiode is not None:
            self.beamStopDiode.export(outfile, level, name_="beamStopDiode")
        if self._wavelength is not None:
            self.wavelength.export(outfile, level, name_="wavelength")
        if self._machineCurrent is not None:
            self.machineCurrent.export(outfile, level, name_="machineCurrent")
        if self._maskFile is not None:
            self.maskFile.export(outfile, level, name_="maskFile")
        if self._normalizationFactor is not None:
            self.normalizationFactor.export(outfile, level, name_="normalizationFactor")
        if self._storageTemperature is not None:
            self.storageTemperature.export(outfile, level, name_="storageTemperature")
        if self._exposureTemperature is not None:
            self.exposureTemperature.export(outfile, level, name_="exposureTemperature")
        if self._exposureTime is not None:
            self.exposureTime.export(outfile, level, name_="exposureTime")
        if self._frameNumber is not None:
            self.frameNumber.export(outfile, level, name_="frameNumber")
        if self._frameMax is not None:
            self.frameMax.export(outfile, level, name_="frameMax")
        if self._timeOfFrame is not None:
            self.timeOfFrame.export(outfile, level, name_="timeOfFrame")

    def build(self, node_):
        for child_ in node_.childNodes:
            nodeName_ = child_.nodeName.split(":")[-1]
            self.buildChildren(child_, nodeName_)

    def buildChildren(self, child_, nodeName_):
        if child_.nodeType == Node.ELEMENT_NODE and nodeName_ == "detector":
            obj_ = XSDataString()
            obj_.build(child_)
            self.setDetector(obj_)
        elif child_.nodeType == Node.ELEMENT_NODE and nodeName_ == "detectorDistance":
            obj_ = XSDataLength()
            obj_.build(child_)
            self.setDetectorDistance(obj_)
        elif child_.nodeType == Node.ELEMENT_NODE and nodeName_ == "pixelSize_1":
            obj_ = XSDataLength()
            obj_.build(child_)
            self.setPixelSize_1(obj_)
        elif child_.nodeType == Node.ELEMENT_NODE and nodeName_ == "pixelSize_2":
            obj_ = XSDataLength()
            obj_.build(child_)
            self.setPixelSize_2(obj_)
        elif child_.nodeType == Node.ELEMENT_NODE and nodeName_ == "beamCenter_1":
            obj_ = XSDataDouble()
            obj_.build(child_)
            self.setBeamCenter_1(obj_)
        elif child_.nodeType == Node.ELEMENT_NODE and nodeName_ == "beamCenter_2":
            obj_ = XSDataDouble()
            obj_.build(child_)
            self.setBeamCenter_2(obj_)
        elif child_.nodeType == Node.ELEMENT_NODE and nodeName_ == "beamStopDiode":
            obj_ = XSDataDouble()
            obj_.build(child_)
            self.setBeamStopDiode(obj_)
        elif child_.nodeType == Node.ELEMENT_NODE and nodeName_ == "wavelength":
            obj_ = XSDataWavelength()
            obj_.build(child_)
            self.setWavelength(obj_)
        elif child_.nodeType == Node.ELEMENT_NODE and nodeName_ == "machineCurrent":
            obj_ = XSDataDouble()
            obj_.build(child_)
            self.setMachineCurrent(obj_)
        elif child_.nodeType == Node.ELEMENT_NODE and nodeName_ == "maskFile":
            obj_ = XSDataImage()
            obj_.build(child_)
            self.setMaskFile(obj_)
        elif (
            child_.nodeType == Node.ELEMENT_NODE and nodeName_ == "normalizationFactor"
        ):
            obj_ = XSDataDouble()
            obj_.build(child_)
            self.setNormalizationFactor(obj_)
        elif child_.nodeType == Node.ELEMENT_NODE and nodeName_ == "storageTemperature":
            obj_ = XSDataDouble()
            obj_.build(child_)
            self.setStorageTemperature(obj_)
        elif (
            child_.nodeType == Node.ELEMENT_NODE and nodeName_ == "exposureTemperature"
        ):
            obj_ = XSDataDouble()
            obj_.build(child_)
            self.setExposureTemperature(obj_)
        elif child_.nodeType == Node.ELEMENT_NODE and nodeName_ == "exposureTime":
            obj_ = XSDataTime()
            obj_.build(child_)
            self.setExposureTime(obj_)
        elif child_.nodeType == Node.ELEMENT_NODE and nodeName_ == "frameNumber":
            obj_ = XSDataInteger()
            obj_.build(child_)
            self.setFrameNumber(obj_)
        elif child_.nodeType == Node.ELEMENT_NODE and nodeName_ == "frameMax":
            obj_ = XSDataInteger()
            obj_.build(child_)
            self.setFrameMax(obj_)
        elif child_.nodeType == Node.ELEMENT_NODE and nodeName_ == "timeOfFrame":
            obj_ = XSDataTime()
            obj_.build(child_)
            self.setTimeOfFrame(obj_)
        XSDataResultBioSaxsSample.buildChildren(self, child_, nodeName_)

    # Method for marshalling an object
    def marshal(self):
        oStreamString = StringIO()
        oStreamString.write(unicode('<?xml version="1.0" ?>\n'))
        self.export(oStreamString, 0, name_="XSDataResultBioSaxsSampleExperiment")
        oStringXML = oStreamString.getvalue()
        oStreamString.close()
        return oStringXML

    # Only to export the entire XML tree to a file stream on disk
    def exportToFile(self, _outfileName):
        outfile = open(_outfileName, "w")
        outfile.write(unicode('<?xml version="1.0" ?>\n'))
        self.export(outfile, 0, name_="XSDataResultBioSaxsSampleExperiment")
        outfile.close()

    # Deprecated method, replaced by exportToFile
    def outputFile(self, _outfileName):
        print(
            "WARNING: Method outputFile in class XSDataResultBioSaxsSampleExperiment is deprecated, please use instead exportToFile!"
        )
        self.exportToFile(_outfileName)

    # Method for making a copy in a new instance
    def copy(self):
        return XSDataResultBioSaxsSampleExperiment.parseString(self.marshal())

    # Static method for parsing a string
    def parseString(_inString):
        doc = minidom.parseString(_inString)
        rootNode = doc.documentElement
        rootObj = XSDataResultBioSaxsSampleExperiment()
        rootObj.build(rootNode)
        # Check that all minOccurs are obeyed by marshalling the created object
        oStreamString = StringIO()
        rootObj.export(oStreamString, 0, name_="XSDataResultBioSaxsSampleExperiment")
        oStreamString.close()
        return rootObj

    parseString = staticmethod(parseString)
    # Static method for parsing a file
    def parseFile(_inFilePath):
        doc = minidom.parse(_inFilePath)
        rootNode = doc.documentElement
        rootObj = XSDataResultBioSaxsSampleExperiment()
        rootObj.build(rootNode)
        return rootObj

    parseFile = staticmethod(parseFile)


# end class XSDataResultBioSaxsSampleExperiment


class XSDataInputBioSaxsAveragev1_0(XSDataInputBioSaxsSampleExperiment):
    def __init__(
        self,
        configuration=None,
        code=None,
        comments=None,
        concentration=None,
        timeOfFrame=None,
        frameMax=None,
        frameNumber=None,
        exposureTime=None,
        exposureTemperature=None,
        storageTemperature=None,
        normalizationFactor=None,
        maskFile=None,
        machineCurrent=None,
        wavelength=None,
        beamStopDiode=None,
        beamCenter_2=None,
        beamCenter_1=None,
        pixelSize_2=None,
        pixelSize_1=None,
        detectorDistance=None,
        detector=None,
        logFile=None,
        averagedCurve=None,
        averagedImage=None,
        integratedImageSize=None,
        integratedImage=None,
    ):
        XSDataInputBioSaxsSampleExperiment.__init__(
            self,
            configuration,
            code,
            comments,
            concentration,
            timeOfFrame,
            frameMax,
            frameNumber,
            exposureTime,
            exposureTemperature,
            storageTemperature,
            normalizationFactor,
            maskFile,
            machineCurrent,
            wavelength,
            beamStopDiode,
            beamCenter_2,
            beamCenter_1,
            pixelSize_2,
            pixelSize_1,
            detectorDistance,
            detector,
        )
        if integratedImage is None:
            self._integratedImage = []
        elif integratedImage.__class__.__name__ == "list":
            self._integratedImage = integratedImage
        else:
            strMessage = (
                "ERROR! XSDataInputBioSaxsAveragev1_0 constructor argument 'integratedImage' is not list but %s"
                % self._integratedImage.__class__.__name__
            )
            raise BaseException(strMessage)
        if integratedImageSize is None:
            self._integratedImageSize = None
        elif integratedImageSize.__class__.__name__ == "XSDataInteger":
            self._integratedImageSize = integratedImageSize
        else:
            strMessage = (
                "ERROR! XSDataInputBioSaxsAveragev1_0 constructor argument 'integratedImageSize' is not XSDataInteger but %s"
                % self._integratedImageSize.__class__.__name__
            )
            raise BaseException(strMessage)
        if averagedImage is None:
            self._averagedImage = None
        elif averagedImage.__class__.__name__ == "XSDataImage":
            self._averagedImage = averagedImage
        else:
            strMessage = (
                "ERROR! XSDataInputBioSaxsAveragev1_0 constructor argument 'averagedImage' is not XSDataImage but %s"
                % self._averagedImage.__class__.__name__
            )
            raise BaseException(strMessage)
        if averagedCurve is None:
            self._averagedCurve = None
        elif averagedCurve.__class__.__name__ == "XSDataFile":
            self._averagedCurve = averagedCurve
        else:
            strMessage = (
                "ERROR! XSDataInputBioSaxsAveragev1_0 constructor argument 'averagedCurve' is not XSDataFile but %s"
                % self._averagedCurve.__class__.__name__
            )
            raise BaseException(strMessage)
        if logFile is None:
            self._logFile = None
        elif logFile.__class__.__name__ == "XSDataFile":
            self._logFile = logFile
        else:
            strMessage = (
                "ERROR! XSDataInputBioSaxsAveragev1_0 constructor argument 'logFile' is not XSDataFile but %s"
                % self._logFile.__class__.__name__
            )
            raise BaseException(strMessage)

    # Methods and properties for the 'integratedImage' attribute
    def getIntegratedImage(self):
        return self._integratedImage

    def setIntegratedImage(self, integratedImage):
        if integratedImage is None:
            self._integratedImage = []
        elif integratedImage.__class__.__name__ == "list":
            self._integratedImage = integratedImage
        else:
            strMessage = (
                "ERROR! XSDataInputBioSaxsAveragev1_0.setIntegratedImage argument is not list but %s"
                % integratedImage.__class__.__name__
            )
            raise BaseException(strMessage)

    def delIntegratedImage(self):
        self._integratedImage = None

    integratedImage = property(
        getIntegratedImage,
        setIntegratedImage,
        delIntegratedImage,
        "Property for integratedImage",
    )

    def addIntegratedImage(self, value):
        if value is None:
            strMessage = "ERROR! XSDataInputBioSaxsAveragev1_0.addIntegratedImage argument is None"
            raise BaseException(strMessage)
        elif value.__class__.__name__ == "XSDataImage":
            self._integratedImage.append(value)
        else:
            strMessage = (
                "ERROR! XSDataInputBioSaxsAveragev1_0.addIntegratedImage argument is not XSDataImage but %s"
                % value.__class__.__name__
            )
            raise BaseException(strMessage)

    def insertIntegratedImage(self, index, value):
        if index is None:
            strMessage = "ERROR! XSDataInputBioSaxsAveragev1_0.insertIntegratedImage argument 'index' is None"
            raise BaseException(strMessage)
        if value is None:
            strMessage = "ERROR! XSDataInputBioSaxsAveragev1_0.insertIntegratedImage argument 'value' is None"
            raise BaseException(strMessage)
        elif value.__class__.__name__ == "XSDataImage":
            self._integratedImage[index] = value
        else:
            strMessage = (
                "ERROR! XSDataInputBioSaxsAveragev1_0.addIntegratedImage argument is not XSDataImage but %s"
                % value.__class__.__name__
            )
            raise BaseException(strMessage)

    # Methods and properties for the 'integratedImageSize' attribute
    def getIntegratedImageSize(self):
        return self._integratedImageSize

    def setIntegratedImageSize(self, integratedImageSize):
        if integratedImageSize is None:
            self._integratedImageSize = None
        elif integratedImageSize.__class__.__name__ == "XSDataInteger":
            self._integratedImageSize = integratedImageSize
        else:
            strMessage = (
                "ERROR! XSDataInputBioSaxsAveragev1_0.setIntegratedImageSize argument is not XSDataInteger but %s"
                % integratedImageSize.__class__.__name__
            )
            raise BaseException(strMessage)

    def delIntegratedImageSize(self):
        self._integratedImageSize = None

    integratedImageSize = property(
        getIntegratedImageSize,
        setIntegratedImageSize,
        delIntegratedImageSize,
        "Property for integratedImageSize",
    )
    # Methods and properties for the 'averagedImage' attribute
    def getAveragedImage(self):
        return self._averagedImage

    def setAveragedImage(self, averagedImage):
        if averagedImage is None:
            self._averagedImage = None
        elif averagedImage.__class__.__name__ == "XSDataImage":
            self._averagedImage = averagedImage
        else:
            strMessage = (
                "ERROR! XSDataInputBioSaxsAveragev1_0.setAveragedImage argument is not XSDataImage but %s"
                % averagedImage.__class__.__name__
            )
            raise BaseException(strMessage)

    def delAveragedImage(self):
        self._averagedImage = None

    averagedImage = property(
        getAveragedImage,
        setAveragedImage,
        delAveragedImage,
        "Property for averagedImage",
    )
    # Methods and properties for the 'averagedCurve' attribute
    def getAveragedCurve(self):
        return self._averagedCurve

    def setAveragedCurve(self, averagedCurve):
        if averagedCurve is None:
            self._averagedCurve = None
        elif averagedCurve.__class__.__name__ == "XSDataFile":
            self._averagedCurve = averagedCurve
        else:
            strMessage = (
                "ERROR! XSDataInputBioSaxsAveragev1_0.setAveragedCurve argument is not XSDataFile but %s"
                % averagedCurve.__class__.__name__
            )
            raise BaseException(strMessage)

    def delAveragedCurve(self):
        self._averagedCurve = None

    averagedCurve = property(
        getAveragedCurve,
        setAveragedCurve,
        delAveragedCurve,
        "Property for averagedCurve",
    )
    # Methods and properties for the 'logFile' attribute
    def getLogFile(self):
        return self._logFile

    def setLogFile(self, logFile):
        if logFile is None:
            self._logFile = None
        elif logFile.__class__.__name__ == "XSDataFile":
            self._logFile = logFile
        else:
            strMessage = (
                "ERROR! XSDataInputBioSaxsAveragev1_0.setLogFile argument is not XSDataFile but %s"
                % logFile.__class__.__name__
            )
            raise BaseException(strMessage)

    def delLogFile(self):
        self._logFile = None

    logFile = property(getLogFile, setLogFile, delLogFile, "Property for logFile")

    def export(self, outfile, level, name_="XSDataInputBioSaxsAveragev1_0"):
        showIndent(outfile, level)
        outfile.write(unicode("<%s>\n" % name_))
        self.exportChildren(outfile, level + 1, name_)
        showIndent(outfile, level)
        outfile.write(unicode("</%s>\n" % name_))

    def exportChildren(self, outfile, level, name_="XSDataInputBioSaxsAveragev1_0"):
        XSDataInputBioSaxsSampleExperiment.exportChildren(self, outfile, level, name_)
        for integratedImage_ in self.getIntegratedImage():
            integratedImage_.export(outfile, level, name_="integratedImage")
        if self.getIntegratedImage() == []:
            warnEmptyAttribute("integratedImage", "XSDataImage")
        if self._integratedImageSize is not None:
            self.integratedImageSize.export(outfile, level, name_="integratedImageSize")
        else:
            warnEmptyAttribute("integratedImageSize", "XSDataInteger")
        if self._averagedImage is not None:
            self.averagedImage.export(outfile, level, name_="averagedImage")
        else:
            warnEmptyAttribute("averagedImage", "XSDataImage")
        if self._averagedCurve is not None:
            self.averagedCurve.export(outfile, level, name_="averagedCurve")
        else:
            warnEmptyAttribute("averagedCurve", "XSDataFile")
        if self._logFile is not None:
            self.logFile.export(outfile, level, name_="logFile")
        else:
            warnEmptyAttribute("logFile", "XSDataFile")

    def build(self, node_):
        for child_ in node_.childNodes:
            nodeName_ = child_.nodeName.split(":")[-1]
            self.buildChildren(child_, nodeName_)

    def buildChildren(self, child_, nodeName_):
        if child_.nodeType == Node.ELEMENT_NODE and nodeName_ == "integratedImage":
            obj_ = XSDataImage()
            obj_.build(child_)
            self.integratedImage.append(obj_)
        elif (
            child_.nodeType == Node.ELEMENT_NODE and nodeName_ == "integratedImageSize"
        ):
            obj_ = XSDataInteger()
            obj_.build(child_)
            self.setIntegratedImageSize(obj_)
        elif child_.nodeType == Node.ELEMENT_NODE and nodeName_ == "averagedImage":
            obj_ = XSDataImage()
            obj_.build(child_)
            self.setAveragedImage(obj_)
        elif child_.nodeType == Node.ELEMENT_NODE and nodeName_ == "averagedCurve":
            obj_ = XSDataFile()
            obj_.build(child_)
            self.setAveragedCurve(obj_)
        elif child_.nodeType == Node.ELEMENT_NODE and nodeName_ == "logFile":
            obj_ = XSDataFile()
            obj_.build(child_)
            self.setLogFile(obj_)
        XSDataInputBioSaxsSampleExperiment.buildChildren(self, child_, nodeName_)

    # Method for marshalling an object
    def marshal(self):
        oStreamString = StringIO()
        oStreamString.write(unicode('<?xml version="1.0" ?>\n'))
        self.export(oStreamString, 0, name_="XSDataInputBioSaxsAveragev1_0")
        oStringXML = oStreamString.getvalue()
        oStreamString.close()
        return oStringXML

    # Only to export the entire XML tree to a file stream on disk
    def exportToFile(self, _outfileName):
        outfile = open(_outfileName, "w")
        outfile.write(unicode('<?xml version="1.0" ?>\n'))
        self.export(outfile, 0, name_="XSDataInputBioSaxsAveragev1_0")
        outfile.close()

    # Deprecated method, replaced by exportToFile
    def outputFile(self, _outfileName):
        print(
            "WARNING: Method outputFile in class XSDataInputBioSaxsAveragev1_0 is deprecated, please use instead exportToFile!"
        )
        self.exportToFile(_outfileName)

    # Method for making a copy in a new instance
    def copy(self):
        return XSDataInputBioSaxsAveragev1_0.parseString(self.marshal())

    # Static method for parsing a string
    def parseString(_inString):
        doc = minidom.parseString(_inString)
        rootNode = doc.documentElement
        rootObj = XSDataInputBioSaxsAveragev1_0()
        rootObj.build(rootNode)
        # Check that all minOccurs are obeyed by marshalling the created object
        oStreamString = StringIO()
        rootObj.export(oStreamString, 0, name_="XSDataInputBioSaxsAveragev1_0")
        oStreamString.close()
        return rootObj

    parseString = staticmethod(parseString)
    # Static method for parsing a file
    def parseFile(_inFilePath):
        doc = minidom.parse(_inFilePath)
        rootNode = doc.documentElement
        rootObj = XSDataInputBioSaxsAveragev1_0()
        rootObj.build(rootNode)
        return rootObj

    parseFile = staticmethod(parseFile)


# end class XSDataInputBioSaxsAveragev1_0


class XSDataInputBioSaxsMetadatav1_0(XSDataInputBioSaxsSampleExperiment):
    def __init__(
        self,
        configuration=None,
        code=None,
        comments=None,
        concentration=None,
        timeOfFrame=None,
        frameMax=None,
        frameNumber=None,
        exposureTime=None,
        exposureTemperature=None,
        storageTemperature=None,
        normalizationFactor=None,
        maskFile=None,
        machineCurrent=None,
        wavelength=None,
        beamStopDiode=None,
        beamCenter_2=None,
        beamCenter_1=None,
        pixelSize_2=None,
        pixelSize_1=None,
        detectorDistance=None,
        detector=None,
        outputImage=None,
        inputImage=None,
    ):
        XSDataInputBioSaxsSampleExperiment.__init__(
            self,
            configuration,
            code,
            comments,
            concentration,
            timeOfFrame,
            frameMax,
            frameNumber,
            exposureTime,
            exposureTemperature,
            storageTemperature,
            normalizationFactor,
            maskFile,
            machineCurrent,
            wavelength,
            beamStopDiode,
            beamCenter_2,
            beamCenter_1,
            pixelSize_2,
            pixelSize_1,
            detectorDistance,
            detector,
        )
        if inputImage is None:
            self._inputImage = None
        elif inputImage.__class__.__name__ == "XSDataImage":
            self._inputImage = inputImage
        else:
            strMessage = (
                "ERROR! XSDataInputBioSaxsMetadatav1_0 constructor argument 'inputImage' is not XSDataImage but %s"
                % self._inputImage.__class__.__name__
            )
            raise BaseException(strMessage)
        if outputImage is None:
            self._outputImage = None
        elif outputImage.__class__.__name__ == "XSDataImage":
            self._outputImage = outputImage
        else:
            strMessage = (
                "ERROR! XSDataInputBioSaxsMetadatav1_0 constructor argument 'outputImage' is not XSDataImage but %s"
                % self._outputImage.__class__.__name__
            )
            raise BaseException(strMessage)

    # Methods and properties for the 'inputImage' attribute
    def getInputImage(self):
        return self._inputImage

    def setInputImage(self, inputImage):
        if inputImage is None:
            self._inputImage = None
        elif inputImage.__class__.__name__ == "XSDataImage":
            self._inputImage = inputImage
        else:
            strMessage = (
                "ERROR! XSDataInputBioSaxsMetadatav1_0.setInputImage argument is not XSDataImage but %s"
                % inputImage.__class__.__name__
            )
            raise BaseException(strMessage)

    def delInputImage(self):
        self._inputImage = None

    inputImage = property(
        getInputImage, setInputImage, delInputImage, "Property for inputImage"
    )
    # Methods and properties for the 'outputImage' attribute
    def getOutputImage(self):
        return self._outputImage

    def setOutputImage(self, outputImage):
        if outputImage is None:
            self._outputImage = None
        elif outputImage.__class__.__name__ == "XSDataImage":
            self._outputImage = outputImage
        else:
            strMessage = (
                "ERROR! XSDataInputBioSaxsMetadatav1_0.setOutputImage argument is not XSDataImage but %s"
                % outputImage.__class__.__name__
            )
            raise BaseException(strMessage)

    def delOutputImage(self):
        self._outputImage = None

    outputImage = property(
        getOutputImage, setOutputImage, delOutputImage, "Property for outputImage"
    )

    def export(self, outfile, level, name_="XSDataInputBioSaxsMetadatav1_0"):
        showIndent(outfile, level)
        outfile.write(unicode("<%s>\n" % name_))
        self.exportChildren(outfile, level + 1, name_)
        showIndent(outfile, level)
        outfile.write(unicode("</%s>\n" % name_))

    def exportChildren(self, outfile, level, name_="XSDataInputBioSaxsMetadatav1_0"):
        XSDataInputBioSaxsSampleExperiment.exportChildren(self, outfile, level, name_)
        if self._inputImage is not None:
            self.inputImage.export(outfile, level, name_="inputImage")
        else:
            warnEmptyAttribute("inputImage", "XSDataImage")
        if self._outputImage is not None:
            self.outputImage.export(outfile, level, name_="outputImage")

    def build(self, node_):
        for child_ in node_.childNodes:
            nodeName_ = child_.nodeName.split(":")[-1]
            self.buildChildren(child_, nodeName_)

    def buildChildren(self, child_, nodeName_):
        if child_.nodeType == Node.ELEMENT_NODE and nodeName_ == "inputImage":
            obj_ = XSDataImage()
            obj_.build(child_)
            self.setInputImage(obj_)
        elif child_.nodeType == Node.ELEMENT_NODE and nodeName_ == "outputImage":
            obj_ = XSDataImage()
            obj_.build(child_)
            self.setOutputImage(obj_)
        XSDataInputBioSaxsSampleExperiment.buildChildren(self, child_, nodeName_)

    # Method for marshalling an object
    def marshal(self):
        oStreamString = StringIO()
        oStreamString.write(unicode('<?xml version="1.0" ?>\n'))
        self.export(oStreamString, 0, name_="XSDataInputBioSaxsMetadatav1_0")
        oStringXML = oStreamString.getvalue()
        oStreamString.close()
        return oStringXML

    # Only to export the entire XML tree to a file stream on disk
    def exportToFile(self, _outfileName):
        outfile = open(_outfileName, "w")
        outfile.write(unicode('<?xml version="1.0" ?>\n'))
        self.export(outfile, 0, name_="XSDataInputBioSaxsMetadatav1_0")
        outfile.close()

    # Deprecated method, replaced by exportToFile
    def outputFile(self, _outfileName):
        print(
            "WARNING: Method outputFile in class XSDataInputBioSaxsMetadatav1_0 is deprecated, please use instead exportToFile!"
        )
        self.exportToFile(_outfileName)

    # Method for making a copy in a new instance
    def copy(self):
        return XSDataInputBioSaxsMetadatav1_0.parseString(self.marshal())

    # Static method for parsing a string
    def parseString(_inString):
        doc = minidom.parseString(_inString)
        rootNode = doc.documentElement
        rootObj = XSDataInputBioSaxsMetadatav1_0()
        rootObj.build(rootNode)
        # Check that all minOccurs are obeyed by marshalling the created object
        oStreamString = StringIO()
        rootObj.export(oStreamString, 0, name_="XSDataInputBioSaxsMetadatav1_0")
        oStreamString.close()
        return rootObj

    parseString = staticmethod(parseString)
    # Static method for parsing a file
    def parseFile(_inFilePath):
        doc = minidom.parse(_inFilePath)
        rootNode = doc.documentElement
        rootObj = XSDataInputBioSaxsMetadatav1_0()
        rootObj.build(rootNode)
        return rootObj

    parseFile = staticmethod(parseFile)


# end class XSDataInputBioSaxsMetadatav1_0


class XSDataInputBioSaxsSingleSamplev1_0(XSDataInputBioSaxsSampleExperiment):
    """Class for precessing a single sample (at 1 single concentration)"""

    def __init__(
        self,
        configuration=None,
        code=None,
        comments=None,
        concentration=None,
        timeOfFrame=None,
        frameMax=None,
        frameNumber=None,
        exposureTime=None,
        exposureTemperature=None,
        storageTemperature=None,
        normalizationFactor=None,
        maskFile=None,
        machineCurrent=None,
        wavelength=None,
        beamStopDiode=None,
        beamCenter_2=None,
        beamCenter_1=None,
        pixelSize_2=None,
        pixelSize_1=None,
        detectorDistance=None,
        detector=None,
        forceReprocess=None,
        sampleSeries=None,
        bufferSeries=None,
        directoryMisc=None,
        directory2D=None,
        directory1D=None,
    ):
        XSDataInputBioSaxsSampleExperiment.__init__(
            self,
            configuration,
            code,
            comments,
            concentration,
            timeOfFrame,
            frameMax,
            frameNumber,
            exposureTime,
            exposureTemperature,
            storageTemperature,
            normalizationFactor,
            maskFile,
            machineCurrent,
            wavelength,
            beamStopDiode,
            beamCenter_2,
            beamCenter_1,
            pixelSize_2,
            pixelSize_1,
            detectorDistance,
            detector,
        )
        if directory1D is None:
            self._directory1D = None
        elif directory1D.__class__.__name__ == "XSDataFile":
            self._directory1D = directory1D
        else:
            strMessage = (
                "ERROR! XSDataInputBioSaxsSingleSamplev1_0 constructor argument 'directory1D' is not XSDataFile but %s"
                % self._directory1D.__class__.__name__
            )
            raise BaseException(strMessage)
        if directory2D is None:
            self._directory2D = None
        elif directory2D.__class__.__name__ == "XSDataFile":
            self._directory2D = directory2D
        else:
            strMessage = (
                "ERROR! XSDataInputBioSaxsSingleSamplev1_0 constructor argument 'directory2D' is not XSDataFile but %s"
                % self._directory2D.__class__.__name__
            )
            raise BaseException(strMessage)
        if directoryMisc is None:
            self._directoryMisc = None
        elif directoryMisc.__class__.__name__ == "XSDataFile":
            self._directoryMisc = directoryMisc
        else:
            strMessage = (
                "ERROR! XSDataInputBioSaxsSingleSamplev1_0 constructor argument 'directoryMisc' is not XSDataFile but %s"
                % self._directoryMisc.__class__.__name__
            )
            raise BaseException(strMessage)
        if bufferSeries is None:
            self._bufferSeries = []
        elif bufferSeries.__class__.__name__ == "list":
            self._bufferSeries = bufferSeries
        else:
            strMessage = (
                "ERROR! XSDataInputBioSaxsSingleSamplev1_0 constructor argument 'bufferSeries' is not list but %s"
                % self._bufferSeries.__class__.__name__
            )
            raise BaseException(strMessage)
        if sampleSeries is None:
            self._sampleSeries = []
        elif sampleSeries.__class__.__name__ == "list":
            self._sampleSeries = sampleSeries
        else:
            strMessage = (
                "ERROR! XSDataInputBioSaxsSingleSamplev1_0 constructor argument 'sampleSeries' is not list but %s"
                % self._sampleSeries.__class__.__name__
            )
            raise BaseException(strMessage)
        if forceReprocess is None:
            self._forceReprocess = None
        elif forceReprocess.__class__.__name__ == "XSDataBoolean":
            self._forceReprocess = forceReprocess
        else:
            strMessage = (
                "ERROR! XSDataInputBioSaxsSingleSamplev1_0 constructor argument 'forceReprocess' is not XSDataBoolean but %s"
                % self._forceReprocess.__class__.__name__
            )
            raise BaseException(strMessage)

    # Methods and properties for the 'directory1D' attribute
    def getDirectory1D(self):
        return self._directory1D

    def setDirectory1D(self, directory1D):
        if directory1D is None:
            self._directory1D = None
        elif directory1D.__class__.__name__ == "XSDataFile":
            self._directory1D = directory1D
        else:
            strMessage = (
                "ERROR! XSDataInputBioSaxsSingleSamplev1_0.setDirectory1D argument is not XSDataFile but %s"
                % directory1D.__class__.__name__
            )
            raise BaseException(strMessage)

    def delDirectory1D(self):
        self._directory1D = None

    directory1D = property(
        getDirectory1D, setDirectory1D, delDirectory1D, "Property for directory1D"
    )
    # Methods and properties for the 'directory2D' attribute
    def getDirectory2D(self):
        return self._directory2D

    def setDirectory2D(self, directory2D):
        if directory2D is None:
            self._directory2D = None
        elif directory2D.__class__.__name__ == "XSDataFile":
            self._directory2D = directory2D
        else:
            strMessage = (
                "ERROR! XSDataInputBioSaxsSingleSamplev1_0.setDirectory2D argument is not XSDataFile but %s"
                % directory2D.__class__.__name__
            )
            raise BaseException(strMessage)

    def delDirectory2D(self):
        self._directory2D = None

    directory2D = property(
        getDirectory2D, setDirectory2D, delDirectory2D, "Property for directory2D"
    )
    # Methods and properties for the 'directoryMisc' attribute
    def getDirectoryMisc(self):
        return self._directoryMisc

    def setDirectoryMisc(self, directoryMisc):
        if directoryMisc is None:
            self._directoryMisc = None
        elif directoryMisc.__class__.__name__ == "XSDataFile":
            self._directoryMisc = directoryMisc
        else:
            strMessage = (
                "ERROR! XSDataInputBioSaxsSingleSamplev1_0.setDirectoryMisc argument is not XSDataFile but %s"
                % directoryMisc.__class__.__name__
            )
            raise BaseException(strMessage)

    def delDirectoryMisc(self):
        self._directoryMisc = None

    directoryMisc = property(
        getDirectoryMisc,
        setDirectoryMisc,
        delDirectoryMisc,
        "Property for directoryMisc",
    )
    # Methods and properties for the 'bufferSeries' attribute
    def getBufferSeries(self):
        return self._bufferSeries

    def setBufferSeries(self, bufferSeries):
        if bufferSeries is None:
            self._bufferSeries = []
        elif bufferSeries.__class__.__name__ == "list":
            self._bufferSeries = bufferSeries
        else:
            strMessage = (
                "ERROR! XSDataInputBioSaxsSingleSamplev1_0.setBufferSeries argument is not list but %s"
                % bufferSeries.__class__.__name__
            )
            raise BaseException(strMessage)

    def delBufferSeries(self):
        self._bufferSeries = None

    bufferSeries = property(
        getBufferSeries, setBufferSeries, delBufferSeries, "Property for bufferSeries"
    )

    def addBufferSeries(self, value):
        if value is None:
            strMessage = "ERROR! XSDataInputBioSaxsSingleSamplev1_0.addBufferSeries argument is None"
            raise BaseException(strMessage)
        elif value.__class__.__name__ == "XSDataFileSeries":
            self._bufferSeries.append(value)
        else:
            strMessage = (
                "ERROR! XSDataInputBioSaxsSingleSamplev1_0.addBufferSeries argument is not XSDataFileSeries but %s"
                % value.__class__.__name__
            )
            raise BaseException(strMessage)

    def insertBufferSeries(self, index, value):
        if index is None:
            strMessage = "ERROR! XSDataInputBioSaxsSingleSamplev1_0.insertBufferSeries argument 'index' is None"
            raise BaseException(strMessage)
        if value is None:
            strMessage = "ERROR! XSDataInputBioSaxsSingleSamplev1_0.insertBufferSeries argument 'value' is None"
            raise BaseException(strMessage)
        elif value.__class__.__name__ == "XSDataFileSeries":
            self._bufferSeries[index] = value
        else:
            strMessage = (
                "ERROR! XSDataInputBioSaxsSingleSamplev1_0.addBufferSeries argument is not XSDataFileSeries but %s"
                % value.__class__.__name__
            )
            raise BaseException(strMessage)

    # Methods and properties for the 'sampleSeries' attribute
    def getSampleSeries(self):
        return self._sampleSeries

    def setSampleSeries(self, sampleSeries):
        if sampleSeries is None:
            self._sampleSeries = []
        elif sampleSeries.__class__.__name__ == "list":
            self._sampleSeries = sampleSeries
        else:
            strMessage = (
                "ERROR! XSDataInputBioSaxsSingleSamplev1_0.setSampleSeries argument is not list but %s"
                % sampleSeries.__class__.__name__
            )
            raise BaseException(strMessage)

    def delSampleSeries(self):
        self._sampleSeries = None

    sampleSeries = property(
        getSampleSeries, setSampleSeries, delSampleSeries, "Property for sampleSeries"
    )

    def addSampleSeries(self, value):
        if value is None:
            strMessage = "ERROR! XSDataInputBioSaxsSingleSamplev1_0.addSampleSeries argument is None"
            raise BaseException(strMessage)
        elif value.__class__.__name__ == "XSDataFileSeries":
            self._sampleSeries.append(value)
        else:
            strMessage = (
                "ERROR! XSDataInputBioSaxsSingleSamplev1_0.addSampleSeries argument is not XSDataFileSeries but %s"
                % value.__class__.__name__
            )
            raise BaseException(strMessage)

    def insertSampleSeries(self, index, value):
        if index is None:
            strMessage = "ERROR! XSDataInputBioSaxsSingleSamplev1_0.insertSampleSeries argument 'index' is None"
            raise BaseException(strMessage)
        if value is None:
            strMessage = "ERROR! XSDataInputBioSaxsSingleSamplev1_0.insertSampleSeries argument 'value' is None"
            raise BaseException(strMessage)
        elif value.__class__.__name__ == "XSDataFileSeries":
            self._sampleSeries[index] = value
        else:
            strMessage = (
                "ERROR! XSDataInputBioSaxsSingleSamplev1_0.addSampleSeries argument is not XSDataFileSeries but %s"
                % value.__class__.__name__
            )
            raise BaseException(strMessage)

    # Methods and properties for the 'forceReprocess' attribute
    def getForceReprocess(self):
        return self._forceReprocess

    def setForceReprocess(self, forceReprocess):
        if forceReprocess is None:
            self._forceReprocess = None
        elif forceReprocess.__class__.__name__ == "XSDataBoolean":
            self._forceReprocess = forceReprocess
        else:
            strMessage = (
                "ERROR! XSDataInputBioSaxsSingleSamplev1_0.setForceReprocess argument is not XSDataBoolean but %s"
                % forceReprocess.__class__.__name__
            )
            raise BaseException(strMessage)

    def delForceReprocess(self):
        self._forceReprocess = None

    forceReprocess = property(
        getForceReprocess,
        setForceReprocess,
        delForceReprocess,
        "Property for forceReprocess",
    )

    def export(self, outfile, level, name_="XSDataInputBioSaxsSingleSamplev1_0"):
        showIndent(outfile, level)
        outfile.write(unicode("<%s>\n" % name_))
        self.exportChildren(outfile, level + 1, name_)
        showIndent(outfile, level)
        outfile.write(unicode("</%s>\n" % name_))

    def exportChildren(
        self, outfile, level, name_="XSDataInputBioSaxsSingleSamplev1_0"
    ):
        XSDataInputBioSaxsSampleExperiment.exportChildren(self, outfile, level, name_)
        if self._directory1D is not None:
            self.directory1D.export(outfile, level, name_="directory1D")
        else:
            warnEmptyAttribute("directory1D", "XSDataFile")
        if self._directory2D is not None:
            self.directory2D.export(outfile, level, name_="directory2D")
        else:
            warnEmptyAttribute("directory2D", "XSDataFile")
        if self._directoryMisc is not None:
            self.directoryMisc.export(outfile, level, name_="directoryMisc")
        else:
            warnEmptyAttribute("directoryMisc", "XSDataFile")
        for bufferSeries_ in self.getBufferSeries():
            bufferSeries_.export(outfile, level, name_="bufferSeries")
        if self.getBufferSeries() == []:
            warnEmptyAttribute("bufferSeries", "XSDataFileSeries")
        for sampleSeries_ in self.getSampleSeries():
            sampleSeries_.export(outfile, level, name_="sampleSeries")
        if self.getSampleSeries() == []:
            warnEmptyAttribute("sampleSeries", "XSDataFileSeries")
        if self._forceReprocess is not None:
            self.forceReprocess.export(outfile, level, name_="forceReprocess")

    def build(self, node_):
        for child_ in node_.childNodes:
            nodeName_ = child_.nodeName.split(":")[-1]
            self.buildChildren(child_, nodeName_)

    def buildChildren(self, child_, nodeName_):
        if child_.nodeType == Node.ELEMENT_NODE and nodeName_ == "directory1D":
            obj_ = XSDataFile()
            obj_.build(child_)
            self.setDirectory1D(obj_)
        elif child_.nodeType == Node.ELEMENT_NODE and nodeName_ == "directory2D":
            obj_ = XSDataFile()
            obj_.build(child_)
            self.setDirectory2D(obj_)
        elif child_.nodeType == Node.ELEMENT_NODE and nodeName_ == "directoryMisc":
            obj_ = XSDataFile()
            obj_.build(child_)
            self.setDirectoryMisc(obj_)
        elif child_.nodeType == Node.ELEMENT_NODE and nodeName_ == "bufferSeries":
            obj_ = XSDataFileSeries()
            obj_.build(child_)
            self.bufferSeries.append(obj_)
        elif child_.nodeType == Node.ELEMENT_NODE and nodeName_ == "sampleSeries":
            obj_ = XSDataFileSeries()
            obj_.build(child_)
            self.sampleSeries.append(obj_)
        elif child_.nodeType == Node.ELEMENT_NODE and nodeName_ == "forceReprocess":
            obj_ = XSDataBoolean()
            obj_.build(child_)
            self.setForceReprocess(obj_)
        XSDataInputBioSaxsSampleExperiment.buildChildren(self, child_, nodeName_)

    # Method for marshalling an object
    def marshal(self):
        oStreamString = StringIO()
        oStreamString.write(unicode('<?xml version="1.0" ?>\n'))
        self.export(oStreamString, 0, name_="XSDataInputBioSaxsSingleSamplev1_0")
        oStringXML = oStreamString.getvalue()
        oStreamString.close()
        return oStringXML

    # Only to export the entire XML tree to a file stream on disk
    def exportToFile(self, _outfileName):
        outfile = open(_outfileName, "w")
        outfile.write(unicode('<?xml version="1.0" ?>\n'))
        self.export(outfile, 0, name_="XSDataInputBioSaxsSingleSamplev1_0")
        outfile.close()

    # Deprecated method, replaced by exportToFile
    def outputFile(self, _outfileName):
        print(
            "WARNING: Method outputFile in class XSDataInputBioSaxsSingleSamplev1_0 is deprecated, please use instead exportToFile!"
        )
        self.exportToFile(_outfileName)

    # Method for making a copy in a new instance
    def copy(self):
        return XSDataInputBioSaxsSingleSamplev1_0.parseString(self.marshal())

    # Static method for parsing a string
    def parseString(_inString):
        doc = minidom.parseString(_inString)
        rootNode = doc.documentElement
        rootObj = XSDataInputBioSaxsSingleSamplev1_0()
        rootObj.build(rootNode)
        # Check that all minOccurs are obeyed by marshalling the created object
        oStreamString = StringIO()
        rootObj.export(oStreamString, 0, name_="XSDataInputBioSaxsSingleSamplev1_0")
        oStreamString.close()
        return rootObj

    parseString = staticmethod(parseString)
    # Static method for parsing a file
    def parseFile(_inFilePath):
        doc = minidom.parse(_inFilePath)
        rootNode = doc.documentElement
        rootObj = XSDataInputBioSaxsSingleSamplev1_0()
        rootObj.build(rootNode)
        return rootObj

    parseFile = staticmethod(parseFile)


# end class XSDataInputBioSaxsSingleSamplev1_0


class XSDataResultBioSaxsMetadatav1_0(XSDataResultBioSaxsSampleExperiment):
    def __init__(
        self,
        status=None,
        code=None,
        comments=None,
        concentration=None,
        timeOfFrame=None,
        frameMax=None,
        frameNumber=None,
        exposureTime=None,
        exposureTemperature=None,
        storageTemperature=None,
        normalizationFactor=None,
        maskFile=None,
        machineCurrent=None,
        wavelength=None,
        beamStopDiode=None,
        beamCenter_2=None,
        beamCenter_1=None,
        pixelSize_2=None,
        pixelSize_1=None,
        detectorDistance=None,
        detector=None,
        outputImage=None,
        experimentSetup=None,
        sample=None,
    ):
        XSDataResultBioSaxsSampleExperiment.__init__(
            self,
            status,
            code,
            comments,
            concentration,
            timeOfFrame,
            frameMax,
            frameNumber,
            exposureTime,
            exposureTemperature,
            storageTemperature,
            normalizationFactor,
            maskFile,
            machineCurrent,
            wavelength,
            beamStopDiode,
            beamCenter_2,
            beamCenter_1,
            pixelSize_2,
            pixelSize_1,
            detectorDistance,
            detector,
        )
        if sample is None:
            self._sample = None
        elif sample.__class__.__name__ == "XSDataBioSaxsSample":
            self._sample = sample
        else:
            strMessage = (
                "ERROR! XSDataResultBioSaxsMetadatav1_0 constructor argument 'sample' is not XSDataBioSaxsSample but %s"
                % self._sample.__class__.__name__
            )
            raise BaseException(strMessage)
        if experimentSetup is None:
            self._experimentSetup = None
        elif experimentSetup.__class__.__name__ == "XSDataBioSaxsExperimentSetup":
            self._experimentSetup = experimentSetup
        else:
            strMessage = (
                "ERROR! XSDataResultBioSaxsMetadatav1_0 constructor argument 'experimentSetup' is not XSDataBioSaxsExperimentSetup but %s"
                % self._experimentSetup.__class__.__name__
            )
            raise BaseException(strMessage)
        if outputImage is None:
            self._outputImage = None
        elif outputImage.__class__.__name__ == "XSDataImage":
            self._outputImage = outputImage
        else:
            strMessage = (
                "ERROR! XSDataResultBioSaxsMetadatav1_0 constructor argument 'outputImage' is not XSDataImage but %s"
                % self._outputImage.__class__.__name__
            )
            raise BaseException(strMessage)

    # Methods and properties for the 'sample' attribute
    def getSample(self):
        return self._sample

    def setSample(self, sample):
        if sample is None:
            self._sample = None
        elif sample.__class__.__name__ == "XSDataBioSaxsSample":
            self._sample = sample
        else:
            strMessage = (
                "ERROR! XSDataResultBioSaxsMetadatav1_0.setSample argument is not XSDataBioSaxsSample but %s"
                % sample.__class__.__name__
            )
            raise BaseException(strMessage)

    def delSample(self):
        self._sample = None

    sample = property(getSample, setSample, delSample, "Property for sample")
    # Methods and properties for the 'experimentSetup' attribute
    def getExperimentSetup(self):
        return self._experimentSetup

    def setExperimentSetup(self, experimentSetup):
        if experimentSetup is None:
            self._experimentSetup = None
        elif experimentSetup.__class__.__name__ == "XSDataBioSaxsExperimentSetup":
            self._experimentSetup = experimentSetup
        else:
            strMessage = (
                "ERROR! XSDataResultBioSaxsMetadatav1_0.setExperimentSetup argument is not XSDataBioSaxsExperimentSetup but %s"
                % experimentSetup.__class__.__name__
            )
            raise BaseException(strMessage)

    def delExperimentSetup(self):
        self._experimentSetup = None

    experimentSetup = property(
        getExperimentSetup,
        setExperimentSetup,
        delExperimentSetup,
        "Property for experimentSetup",
    )
    # Methods and properties for the 'outputImage' attribute
    def getOutputImage(self):
        return self._outputImage

    def setOutputImage(self, outputImage):
        if outputImage is None:
            self._outputImage = None
        elif outputImage.__class__.__name__ == "XSDataImage":
            self._outputImage = outputImage
        else:
            strMessage = (
                "ERROR! XSDataResultBioSaxsMetadatav1_0.setOutputImage argument is not XSDataImage but %s"
                % outputImage.__class__.__name__
            )
            raise BaseException(strMessage)

    def delOutputImage(self):
        self._outputImage = None

    outputImage = property(
        getOutputImage, setOutputImage, delOutputImage, "Property for outputImage"
    )

    def export(self, outfile, level, name_="XSDataResultBioSaxsMetadatav1_0"):
        showIndent(outfile, level)
        outfile.write(unicode("<%s>\n" % name_))
        self.exportChildren(outfile, level + 1, name_)
        showIndent(outfile, level)
        outfile.write(unicode("</%s>\n" % name_))

    def exportChildren(self, outfile, level, name_="XSDataResultBioSaxsMetadatav1_0"):
        XSDataResultBioSaxsSampleExperiment.exportChildren(self, outfile, level, name_)
        if self._sample is not None:
            self.sample.export(outfile, level, name_="sample")
        if self._experimentSetup is not None:
            self.experimentSetup.export(outfile, level, name_="experimentSetup")
        if self._outputImage is not None:
            self.outputImage.export(outfile, level, name_="outputImage")

    def build(self, node_):
        for child_ in node_.childNodes:
            nodeName_ = child_.nodeName.split(":")[-1]
            self.buildChildren(child_, nodeName_)

    def buildChildren(self, child_, nodeName_):
        if child_.nodeType == Node.ELEMENT_NODE and nodeName_ == "sample":
            obj_ = XSDataBioSaxsSample()
            obj_.build(child_)
            self.setSample(obj_)
        elif child_.nodeType == Node.ELEMENT_NODE and nodeName_ == "experimentSetup":
            obj_ = XSDataBioSaxsExperimentSetup()
            obj_.build(child_)
            self.setExperimentSetup(obj_)
        elif child_.nodeType == Node.ELEMENT_NODE and nodeName_ == "outputImage":
            obj_ = XSDataImage()
            obj_.build(child_)
            self.setOutputImage(obj_)
        XSDataResultBioSaxsSampleExperiment.buildChildren(self, child_, nodeName_)

    # Method for marshalling an object
    def marshal(self):
        oStreamString = StringIO()
        oStreamString.write(unicode('<?xml version="1.0" ?>\n'))
        self.export(oStreamString, 0, name_="XSDataResultBioSaxsMetadatav1_0")
        oStringXML = oStreamString.getvalue()
        oStreamString.close()
        return oStringXML

    # Only to export the entire XML tree to a file stream on disk
    def exportToFile(self, _outfileName):
        outfile = open(_outfileName, "w")
        outfile.write(unicode('<?xml version="1.0" ?>\n'))
        self.export(outfile, 0, name_="XSDataResultBioSaxsMetadatav1_0")
        outfile.close()

    # Deprecated method, replaced by exportToFile
    def outputFile(self, _outfileName):
        print(
            "WARNING: Method outputFile in class XSDataResultBioSaxsMetadatav1_0 is deprecated, please use instead exportToFile!"
        )
        self.exportToFile(_outfileName)

    # Method for making a copy in a new instance
    def copy(self):
        return XSDataResultBioSaxsMetadatav1_0.parseString(self.marshal())

    # Static method for parsing a string
    def parseString(_inString):
        doc = minidom.parseString(_inString)
        rootNode = doc.documentElement
        rootObj = XSDataResultBioSaxsMetadatav1_0()
        rootObj.build(rootNode)
        # Check that all minOccurs are obeyed by marshalling the created object
        oStreamString = StringIO()
        rootObj.export(oStreamString, 0, name_="XSDataResultBioSaxsMetadatav1_0")
        oStreamString.close()
        return rootObj

    parseString = staticmethod(parseString)
    # Static method for parsing a file
    def parseFile(_inFilePath):
        doc = minidom.parse(_inFilePath)
        rootNode = doc.documentElement
        rootObj = XSDataResultBioSaxsMetadatav1_0()
        rootObj.build(rootNode)
        return rootObj

    parseFile = staticmethod(parseFile)


# end class XSDataResultBioSaxsMetadatav1_0


# End of data representation classes.
