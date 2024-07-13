import cifpfunctions as cf
import cifparse.cifpterminalpoint as cp
import cifpproceduresubsegment as cs


class CIFPProcedureSegment:
    def __init__(self, cifpLines: list) -> None:
        initial = str(cifpLines[0])
        subCode = initial[12:13].strip()
        routeType = initial[19:20].strip()
        self.type = self.translateRouteType(subCode, routeType)
        self.transitions = []
        self.points = []

        isCore = self.determineCore(subCode, routeType)
        if isCore:
            for cifpLine in cifpLines:
                contRecNo = int(cifpLine[38:39])
                if contRecNo == 0 or contRecNo == 1:
                    self.cont0(cifpLine)
            del self.transitions
        else:
            functions = cf.CIFPFunctions()
            subChunked = functions.chunk(cifpLines, 20, 25)
            for subChunk in subChunked:
                transition = cs.CIFPProcedureSubsegment(subChunk)
                self.transitions.append(transition.toDict())
            del self.points

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

    def determineCore(self, subCode: str, routeType: str) -> bool:
        result = False
        if subCode == "D":
            if (
                routeType == "0"
                or routeType == "2"
                or routeType == "5"
                or routeType == "M"
            ):
                result = True
        if subCode == "E":
            if (
                routeType == "2"
                or routeType == "5"
                or routeType == "8"
                or routeType == "M"
            ):
                result = True
        if subCode == "F":
            if routeType != "A" and routeType != "Z":
                result = True
        return result

    def translateRouteType(self, subCode: str, routeType: str) -> str | None:
        result = None
        if subCode == "D":
            if routeType == "0":
                result = "eosid"
            if (
                routeType == "1"
                or routeType == "4"
                or routeType == "F"
                or routeType == "T"
            ):
                result = "runway_transition"
            if routeType == "2" or routeType == "5" or routeType == "M":
                result = "core"
            if (
                routeType == "3"
                or routeType == "6"
                or routeType == "S"
                or routeType == "V"
            ):
                result = "transition"
        if subCode == "E":
            if (
                routeType == "1"
                or routeType == "4"
                or routeType == "7"
                or routeType == "F"
            ):
                result = "transition"
            if (
                routeType == "2"
                or routeType == "5"
                or routeType == "8"
                or routeType == "M"
            ):
                result = "core"
            if (
                routeType == "3"
                or routeType == "6"
                or routeType == "9"
                or routeType == "S"
            ):
                result = "runway_transition"
        if subCode == "F":
            if routeType == "A":
                result = "transition"
            if routeType == "B":
                result = "LOC/BC"
            if routeType == "D":
                result = "VOR/DME"
            if routeType == "F":
                result = "FMS"
            if routeType == "G":
                result = "IGS"
            if routeType == "H":
                result = "RNP"
            if routeType == "I":
                result = "ILS"
            if routeType == "J":
                result = "GNSS"
            if routeType == "L":
                result = "LOC"
            if routeType == "M":
                result = "MLS"
            if routeType == "N":
                result = "NDB"
            if routeType == "P":
                result = "GPS"
            if routeType == "Q":
                result = "NDB/DME"
            if routeType == "R":
                result = "RNAV"
            if routeType == "S":
                result = "VORTAC"
            if routeType == "T":
                result = "TACAN"
            if routeType == "U":
                result = "SDF"
            if routeType == "V":
                result = "VOR"
            if routeType == "W":
                result = "MLS-A"
            if routeType == "X":
                result = "LDA"
            if routeType == "Y":
                result = "MLS-B/C"
            if routeType == "Z":
                result = "Missed"
        return result

    def toDict(self) -> dict:
        functions = cf.CIFPFunctions()
        functions.cleanDict(self.__dict__)
        return self.__dict__
