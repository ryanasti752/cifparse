import cifpfunctions as cf


class ProcedurePoint:
    def __init__(
        self,
        seqNo: int,
        fixId: str,
        fixRegion: str,
        fixSecCode2: str,
        fixSubCode2: str,
        descCode: str,
        turnDir: str,
        rnp: str,
        pathTerm: str,
        tdv: str,
        recvhf: str,
        vhfRegion: str,
        arcRadius: float | None,
        theta: float | None,
        rho: float | None,
        magCrs: float | None,
        dist: float | None,
        time: float | None,
        vhfSecCode: str,
        vhfSubCode: str,
        altDesc: str,
        atc: str,
        altitude: int | None,
        flightLevel: int | None,
        altitude2: str,
        transAlt: int | None,
        speedLimit: int | None,
        vertAngle: int | None,
        centerFix: str,
        multCode: str,
        centerFixRegion: str,
        centerFixSecCode: str,
        centerFixSubCode: str,
        gnsFMSId: str,
        speedLimit2: str,
        rteQual1: str,
        rteQual2: str,
        recordNo: int,
        cycleData: str,
    ) -> None:
        self.seqNo = seqNo
        self.fixId = fixId
        self.fixRegion = fixRegion
        self.fixSecCode2 = fixSecCode2
        self.fixSubCode2 = fixSubCode2
        self.descCode = descCode
        self.turnDir = turnDir
        self.rnp = rnp
        self.pathTerm = pathTerm
        self.tdv = tdv
        self.recvhf = recvhf
        self.vhfRegion = vhfRegion
        self.arcRadius = arcRadius
        self.theta = theta
        self.rho = rho
        self.magCrs = magCrs
        self.dist = dist
        self.time = time
        self.vhfSecCode = vhfSecCode
        self.vhfSubCode = vhfSubCode
        self.altDesc = altDesc
        self.atc = atc
        self.altitude = altitude
        self.flightLevel = flightLevel
        self.altitude2 = altitude2
        self.transAlt = transAlt
        self.speedLimit = speedLimit
        self.vertAngle = vertAngle
        self.centerFix = centerFix
        self.multCode = multCode
        self.centerFixRegion = centerFixRegion
        self.centerFixSecCode = centerFixSecCode
        self.centerFixSubCode = centerFixSubCode
        self.gnsFMSId = gnsFMSId
        self.speedLimit2 = speedLimit2
        self.rteQual1 = rteQual1
        self.rteQual2 = rteQual2
        self.recordNo = recordNo
        self.cycleData = cycleData

    def toDict(self) -> dict:
        functions = cf.CIFPFunctions()
        functions.cleanDict(self.__dict__)
        return self.__dict__
