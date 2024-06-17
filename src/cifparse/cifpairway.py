import cifpairwaypoint as cp
import cifpfunctions as cf


class CIFPAirway:
    def __init__(self, cifpLines: list) -> None:
        self.area = None
        self.secCode = None
        self.subCode = None
        self.id = None
        self.sixChar = None
        self.points = []
        self.startSet = False
        for cifpLine in cifpLines:
            contRecNo = int(cifpLine[38:39])
            if contRecNo == 0:
                self.cont0(cifpLine)
            if contRecNo == 1:
                self.cont1(cifpLine)
        del self.startSet

    def cont0(self, cifpLine: str) -> None:
        # PAD 1
        area = cifpLine[1:4].strip()
        secCode = cifpLine[4:5].strip()
        subCode = cifpLine[5:6].strip()
        # PAD 7
        id = cifpLine[13:18].strip()
        sixChar = cifpLine[18:19].strip()
        # PAD 6
        seqNo = int(cifpLine[26:29].strip())
        pointId = cifpLine[29:34].strip()
        subregion = cifpLine[34:36].strip()
        pointSecCode = cifpLine[36:37].strip()
        pointSubCode = cifpLine[37:38].strip()
        # contRecNo = int(cifpLine[38:39].strip())
        descCode = cifpLine[39:43]
        boundCode = cifpLine[43:44].strip()
        routeType = cifpLine[44:45].strip()
        level = cifpLine[45:46].strip()
        direct = cifpLine[46:47].strip()
        tcInd = cifpLine[47:49].strip()
        euInd = cifpLine[49:50].strip()
        recvhf = cifpLine[50:54].strip()
        region = cifpLine[54:56].strip()
        rnp = cifpLine[56:59].strip()
        # PAD 3
        theta = cifpLine[62:66].strip()
        rho = cifpLine[66:70].strip()
        outCrs = cifpLine[70:74].strip()
        outMagCrs = None
        dist = cifpLine[74:78].strip()
        fromDist = None
        inCrs = cifpLine[78:82].strip()
        inMagCrs = None
        # PAD 1
        minimumAlt = cifpLine[83:88].strip()
        minAlt = None
        minimumAlt2 = cifpLine[88:93].strip()
        minAlt2 = None
        maximumAlt = cifpLine[93:98].strip()
        maxAlt = None
        fixRad = cifpLine[98:102].strip()
        fixRadius = None
        # PAD 21
        recordNo = int(cifpLine[123:128].strip())
        cycleData = cifpLine[128:132].strip()

        if outCrs != "":
            outMagCrs = int(outCrs) / 10
        del outCrs

        if dist != "":
            fromDist = int(dist) / 10
        del dist

        if inCrs != "":
            inMagCrs = int(inCrs) / 10
        del inCrs

        if minimumAlt == "UNKNN":
            minimumAlt = ""
        if minimumAlt != "":
            minAlt = int(minimumAlt)
        del minimumAlt

        if minimumAlt2 == "UNKNN":
            minimumAlt2 = ""
        if minimumAlt2 != "":
            minAlt2 = int(minimumAlt2)
        del minimumAlt2

        if maximumAlt == "UNKNN":
            maximumAlt = ""
        if maximumAlt != "":
            maxAlt = int(maximumAlt)
        del maximumAlt

        if fixRad != "":
            fixRadius = int(fixRad)
        del fixRad

        isStart = False
        if self.startSet == False:
            self.startSet = True
            isStart = True

        isEnd = False
        if descCode[1:2] == "E":
            self.startSet = False
            isEnd = True

        sigPoint = None
        if isStart == True:
            sigPoint = "S"
        if isEnd == True:
            sigPoint = "E"

        point = cp.AirwayPoint(
            seqNo,
            sigPoint,
            pointId,
            subregion,
            pointSecCode,
            pointSubCode,
            descCode,
            boundCode,
            routeType,
            level,
            direct,
            tcInd,
            euInd,
            recvhf,
            region,
            rnp,
            theta,
            rho,
            outMagCrs,
            fromDist,
            inMagCrs,
            minAlt,
            minAlt2,
            maxAlt,
            fixRadius,
            recordNo,
            cycleData,
        )
        self.points.append(point.toDict())
        if self.id == None:
            self.area = area
            self.secCode = secCode
            self.subCode = subCode
            self.id = id
            self.sixChar = sixChar

    def cont1(self, cifpLine: str) -> None:
        # PAD 38
        self.application = cifpLine[39:40]
        self.notes = cifpLine[40:109]

    def toDict(self) -> dict:
        functions = cf.CIFPFunctions()
        functions.cleanDict(self.__dict__)
        return self.__dict__
