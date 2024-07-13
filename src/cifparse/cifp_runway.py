import cifpfunctions as cf


class CIFPRunway:
    def __init__(
        self,
        id: str,
        length: int | None,
        bearing: int | None,
        lat: float | None,
        lon: float | None,
        gradient: int | None,
        ellipHeight: int | None,
        thrElevation: int | None,
        dispThresh: int | None,
        tch: int | None,
        width: int | None,
        tchId: str,
        vhfIdent: str,
        cat: str,
        stopway: int | None,
        vhfIdent2: str,
        cat2: str,
        description: str,
        recordNo: int,
        cycleData: str,
    ) -> None:
        self.id = id
        self.length = length
        self.bearing = bearing
        self.lat = lat
        self.lon = lon
        self.gradient = gradient
        self.ellipHeight = ellipHeight
        self.thrElevation = thrElevation
        self.dispThresh = dispThresh
        self.tch = tch
        self.width = width
        self.tchId = tchId
        self.vhfIdent = vhfIdent
        self.cat = cat
        self.stopway = stopway
        self.vhfIdent2 = vhfIdent2
        self.cat2 = cat2
        self.description = description
        self.recordNo = recordNo
        self.cycleData = cycleData

    def toDict(self) -> dict:
        functions = cf.CIFPFunctions()
        functions.cleanDict(self.__dict__)
        return self.__dict__
