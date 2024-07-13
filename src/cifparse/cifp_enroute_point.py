import cifpfunctions as cf


class AirwayPoint:
    def __init__(
        self,
        seqNo: int,
        sigPoint: str | None,
        pointId: str,
        subregion: str,
        pointSecCode: str,
        pointSubCode: str,
        descCode: str,
        boundCode: str,
        routeType: str,
        level: str,
        direct: str,
        tcInd: str,
        euInd: str,
        recvhf: str,
        region: str,
        rnp: str,
        theta: str,
        rho: str,
        outMagCrs: float | None,
        fromDist: float | None,
        inMagCrs: float | None,
        minAlt: int | None,
        minAlt2: int | None,
        maxAlt: int | None,
        fixRadius: int | None,
        recordNo: int,
        cycleData: str,
    ) -> None:
        self.seqNo = seqNo
        self.sigPoint = sigPoint
        self.pointId = pointId
        self.subregion = subregion
        self.pointSecCode = pointSecCode
        self.pointSubCode = pointSubCode
        self.descCode = descCode
        self.boundCode = boundCode
        self.routeType = routeType
        self.level = level
        self.direct = direct
        self.tcInd = tcInd
        self.euInd = euInd
        self.recvhf = recvhf
        self.region = region
        self.rnp = rnp
        self.theta = theta
        self.rho = rho
        self.outMagCrs = outMagCrs
        self.fromDist = fromDist
        self.inMagCrs = inMagCrs
        self.minAlt = minAlt
        self.minAlt2 = minAlt2
        self.maxAlt = maxAlt
        self.fixRadius = fixRadius
        self.recordNo = recordNo
        self.cycleData = cycleData

    def toDict(self) -> dict:
        functions = cf.CIFPFunctions()
        functions.cleanDict(self.__dict__)
        return self.__dict__
