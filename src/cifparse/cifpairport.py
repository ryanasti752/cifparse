import cifpfunctions as cf
import cifpprocedure as cp
import cifprunway as cr
import cifpwaypoint as cw


class CIFPAirport:
    def __init__(self, cifpLines: list) -> None:
        self.area = None
        self.secCode = None
        self.id = None
        self.region = None
        self.iata = None
        self.limitAlt = None
        self.longest = None
        self.isIfr = None
        self.longestSurface = None
        self.lat = None
        self.lon = None
        self.magvar = None
        self.elevation = None
        self.limit = None
        self.recvhf = None
        self.subregion = None
        self.transAlt = None
        self.transLevel = None
        self.usage = None
        self.timeZone = None
        self.daylightInd = None
        self.magTrue = None
        self.datumCode = None
        self.airportName = None
        self.recordNo = None
        self.cycleData = None
        self.points = []
        self.departureLines = []
        self.departureChunked = []
        self.departures = []
        self.arrivalLines = []
        self.arrivalChunked = []
        self.arrivals = []
        self.approachLines = []
        self.approachChunked = []
        self.approaches = []
        self.runways = []

        for cifpLine in cifpLines:
            subCode = cifpLine[12:13]
            contRecNo = int(cifpLine[38:39])
            if subCode == "A":
                self.secA(cifpLine)
            if subCode == "C":
                self.secC(cifpLine)
            if subCode == "D":
                self.departureLines.append(cifpLine)
            if subCode == "E":
                self.arrivalLines.append(cifpLine)
            if subCode == "F":
                self.approachLines.append(cifpLine)
            if subCode == "G":
                self.secG(cifpLine)

        functions = cf.CIFPFunctions()
        # Process Departures
        self.departureChunked = functions.chunk(self.departureLines, 6, 19)
        self._departureToObject()
        del self.departureLines
        del self.departureChunked
        # Process Arrivals
        self.arrivalChunked = functions.chunk(self.arrivalLines, 6, 19)
        self._arrivalToObject()
        del self.arrivalLines
        del self.arrivalChunked
        # Process Approaches
        self.approachChunked = functions.chunk(self.approachLines, 6, 19)
        self._approachToObject()
        del self.approachLines
        del self.approachChunked

    def _departureToObject(self) -> None:
        for departureChunk in self.departureChunked:
            departure = cp.CIFPProcedure(departureChunk)
            self.departures.append(departure.toDict())

    def _arrivalToObject(self) -> None:
        for arrivalChunk in self.arrivalChunked:
            arrival = cp.CIFPProcedure(arrivalChunk)
            self.arrivals.append(arrival.toDict())

    def _approachToObject(self) -> None:
        for approachChunk in self.approachChunked:
            approach = cp.CIFPProcedure(approachChunk)
            self.approaches.append(approach.toDict())

    def secA(self, cifpLine: str) -> None:
        # PAD 1
        self.area = cifpLine[1:4].strip()
        self.secCode = cifpLine[4:5].strip()
        # PAD 1
        self.id = cifpLine[6:10].strip()
        self.region = cifpLine[10:12].strip()
        # subCode = cifpLine[12:13].strip()
        self.iata = cifpLine[13:16].strip()
        # PAD 5
        # contRecNo = int(cifpLine[21:22].strip())
        self.speedLimitAlt = cifpLine[22:27].strip()
        self.limitAlt = None
        self.longestRunway = cifpLine[27:30].strip()
        self.longest = None
        self.isIfr = cifpLine[30:31].strip()
        self.longestSurface = cifpLine[31:32].strip()
        self.latlon = cifpLine[32:51].strip()
        self.lat = None
        self.lon = None
        self.variation = cifpLine[51:56].strip()
        self.magvar = None
        self.elev = cifpLine[56:61].strip()
        self.elevation = None
        self.speedLimit = cifpLine[61:64].strip()
        self.limit = None
        self.recvhf = cifpLine[64:68].strip()
        self.subregion = cifpLine[68:70].strip()
        self.transitionAlt = cifpLine[70:75].strip()
        self.transAlt = None
        self.transitionLevel = cifpLine[75:80].strip()
        self.transLevel = None
        self.usage = cifpLine[80:81].strip()
        self.timeZone = cifpLine[81:84].strip()
        self.daylightInd = cifpLine[84:85].strip()
        self.magTrue = cifpLine[85:86].strip()
        self.datumCode = cifpLine[86:89].strip()
        # PAD 4
        self.airportName = cifpLine[93:123].strip()
        self.recordNo = int(cifpLine[123:128].strip())
        self.cycleData = cifpLine[128:132].strip()

        functions = cf.CIFPFunctions()

        if self.speedLimitAlt != "":
            self.limitAlt = int(self.speedLimitAlt)
        del self.speedLimitAlt

        if self.longestRunway != "":
            self.longest = int(self.longestRunway)
        del self.longestRunway

        if self.latlon != "":
            coodinates = functions.convertDMS(self.latlon)
            self.lat = coodinates.lat
            self.lon = coodinates.lon
        del self.latlon

        if self.variation != "":
            magvar = functions.convertMagVar(self.variation)
            self.magvar = magvar
        del self.variation

        if self.elev != "":
            self.elevation = int(self.elev)
        del self.elev

        if self.speedLimit != "":
            self.limit = int(self.speedLimit)
        del self.speedLimit

        if self.transitionAlt != "":
            self.transAlt = int(self.transitionAlt)
        del self.transitionAlt

        if self.transitionLevel != "":
            self.transLevel = int(self.transitionLevel)
        del self.transitionLevel

    def secC(self, cifpLine: str) -> None:
        point = cw.CIFPWaypoint([cifpLine])
        self.points.append(point.toDict())

    def secG(self, cifpLine: str) -> None:
        functions = cf.CIFPFunctions()
        # PAD 1
        area = cifpLine[1:4].strip()
        secCode = cifpLine[4:5].strip()
        # PAD 1
        airportId = cifpLine[6:10].strip()
        region = cifpLine[10:12].strip()
        # subCode = cifpLine[12:13].strip()
        runwayId = cifpLine[13:18].strip()
        # PAD 3
        # contRecNo = int(cifpLine[21:22].strip())
        runwayLength = cifpLine[22:27].strip()
        length = None
        runwayBearing = cifpLine[27:31].strip()
        bearing = None
        # PAD 1
        latlon = cifpLine[32:51].strip()
        lat = None
        lon = None
        runwayGradient = cifpLine[51:56].strip()
        gradient = None
        # PAD 4
        ellipsoidHeight = cifpLine[60:66].strip()
        ellipHeight = None
        thresholdElevation = cifpLine[66:71].strip()
        thrElevation = None
        displacedThreshold = cifpLine[71:75].strip()
        dispThresh = None
        thresholdCrossHeight = cifpLine[75:77].strip()
        tch = None
        runwayWidth = cifpLine[77:80].strip()
        width = None
        thresholdCrossHeightId = cifpLine[80:81].strip()
        vhfIdent = cifpLine[81:85].strip()
        category = cifpLine[85:86].strip()
        runwayStopway = cifpLine[86:90].strip()
        stopway = None
        vhfIdent2 = cifpLine[90:94].strip()
        category2 = cifpLine[94:95].strip()
        # PAD 6
        runwayDesc = cifpLine[101:123].strip()
        recordNo = int(cifpLine[123:128].strip())
        cycleData = cifpLine[128:132].strip()

        if runwayLength != "":
            length = int(runwayLength)
        del runwayLength

        if runwayBearing != "":
            bearing = int(runwayBearing)
        del runwayBearing

        if latlon != "":
            coodinates = functions.convertDMS(latlon)
            lat = coodinates.lat
            lon = coodinates.lon
        del latlon

        if runwayGradient != "":
            gradient = int(runwayGradient)
        del runwayGradient

        if ellipsoidHeight != "":
            ellipHeight = int(ellipsoidHeight)
        del ellipsoidHeight

        if thresholdElevation != "":
            thrElevation = int(thresholdElevation)
        del thresholdElevation

        if displacedThreshold != "":
            dispThresh = int(displacedThreshold)
        del displacedThreshold

        if thresholdCrossHeight != "":
            tch = int(thresholdCrossHeight)
        del thresholdCrossHeight

        if runwayWidth != "":
            width = int(runwayWidth)
        del runwayWidth

        if runwayStopway != "":
            stopway = int(runwayStopway)
        del runwayStopway

        runway = cr.CIFPRunway(
            runwayId,
            length,
            bearing,
            lat,
            lon,
            gradient,
            ellipHeight,
            thrElevation,
            dispThresh,
            tch,
            width,
            thresholdCrossHeightId,
            vhfIdent,
            category,
            stopway,
            vhfIdent2,
            category2,
            runwayDesc,
            recordNo,
            cycleData,
        )
        self.runways.append(runway.toDict())

    def toDict(self) -> dict:
        functions = cf.CIFPFunctions()
        functions.cleanDict(self.__dict__)
        return self.__dict__
