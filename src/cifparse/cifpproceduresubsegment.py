import cifpfunctions as cf
import cifparse.cifpterminalpoint as cp


class CIFPProcedureSubsegment:
    def __init__(self, cifpLines: list) -> None:
        initial = str(cifpLines[0])
        transitionId = initial[20:25].strip()
        self.id = transitionId
        self.points = []

        for cifpLine in cifpLines:
            contRecNo = int(cifpLine[38:39])
            if contRecNo == 0 or contRecNo == 1:
                self.cont0(cifpLine)

    def cont0(self, cifpLine: str) -> None:
        # PAD 1
        area = cifpLine[1:4].strip()
        secCode = cifpLine[4:5].strip()
        # PAD 1
        airportId = cifpLine[6:10].strip()
        airportRegion = cifpLine[10:12].strip()
        subCode = cifpLine[12:13].strip()
        id = cifpLine[13:19].strip()
        routeType = cifpLine[19:20].strip()
        transitionId = cifpLine[20:25].strip()
        # PAD 1
        seqNo = int(cifpLine[26:29].strip())
        fixId = cifpLine[29:34].strip()
        fixRegion = cifpLine[34:36].strip()
        fixSecCode2 = cifpLine[36:37].strip()
        fixSubCode2 = cifpLine[37:38].strip()
        # contRecNo = int(cifpLine[38:39])
        descCode = cifpLine[39:43]
        turnDir = cifpLine[43:44].strip()
        rnp = cifpLine[44:47].strip()
        pathTerm = cifpLine[47:49].strip()
        tdv = cifpLine[49:50].strip()
        recvhf = cifpLine[50:54].strip()
        vhfRegion = cifpLine[54:56].strip()
        arcRad = cifpLine[56:62].strip()
        arcRadius = None
        thetaS = cifpLine[62:66].strip()
        theta = None
        rhoS = cifpLine[66:70].strip()
        rho = None
        crs = cifpLine[70:74].strip()
        magCrs = None
        distance = cifpLine[74:78].strip()
        dist = None
        time = None
        vhfSecCode = cifpLine[78:79].strip()
        vhfSubCode = cifpLine[79:80].strip()
        # PAD 2
        altDesc = cifpLine[82:83].strip()
        atc = cifpLine[83:84].strip()
        altitude = cifpLine[84:89].strip()
        alt = None
        flightLevel = None
        alt2 = cifpLine[89:94].strip()
        transAltitude = cifpLine[94:99].strip()
        transAlt = None
        speed = cifpLine[99:102].strip()
        speedLimit = None
        verticalAngle = cifpLine[102:106].strip()
        vertAngle = None
        centerFix = cifpLine[106:111].strip()
        multCode = cifpLine[111:112].strip()
        centerFixRegion = cifpLine[112:114].strip()
        centerFixSecCode = cifpLine[114:115].strip()
        centerFixSubCode = cifpLine[115:116].strip()
        gnsFMSId = cifpLine[116:117].strip()
        speedLimit2 = cifpLine[117:118].strip()
        rteQual1 = cifpLine[118:119].strip()
        rteQual2 = cifpLine[119:120].strip()
        # PAD 3
        recordNo = int(cifpLine[123:128].strip())
        cycleData = cifpLine[128:132].strip()

        if arcRad != "":
            arcRadius = int(arcRad) / 1000
        del arcRad

        if thetaS != "":
            theta = int(thetaS) / 10
        del thetaS

        if rhoS != "":
            rho = int(rhoS) / 10
        del rhoS

        if crs != "":
            magCrs = int(crs) / 10
        del crs

        if distance != "":
            if distance.startswith("T"):
                time = int(distance[1:]) / 10
            else:
                dist = int(distance) / 10
        del distance

        if altitude != "":
            if altitude.startswith("FL"):
                flightLevel = int(altitude[2:])
            else:
                alt = int(altitude)
        del altitude

        if transAltitude != "":
            transAlt = int(transAltitude)
        del transAltitude

        if speed != "":
            speedLimit = int(speed)
        del speed

        if verticalAngle != "":
            vertAngle = int(verticalAngle)
        del verticalAngle

        point = cp.ProcedurePoint(
            seqNo,
            fixId,
            fixRegion,
            fixSecCode2,
            fixSubCode2,
            descCode,
            turnDir,
            rnp,
            pathTerm,
            tdv,
            recvhf,
            vhfRegion,
            arcRadius,
            theta,
            rho,
            magCrs,
            dist,
            time,
            vhfSecCode,
            vhfSubCode,
            altDesc,
            atc,
            alt,
            flightLevel,
            alt2,
            transAlt,
            speedLimit,
            vertAngle,
            centerFix,
            multCode,
            centerFixRegion,
            centerFixSecCode,
            centerFixSubCode,
            gnsFMSId,
            speedLimit2,
            rteQual1,
            rteQual2,
            recordNo,
            cycleData,
        )
        self.points.append(point.toDict())

    def toDict(self) -> dict:
        functions = cf.CIFPFunctions()
        functions.cleanDict(self.__dict__)
        return self.__dict__
