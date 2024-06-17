import cifpairport as ca
import cifpndb as cn
import cifpairway as cr
import cifpvhfdme as cv
import cifpwaypoint as cw
import cifpfunctions as cf

import os


class CIFP:
    def __init__(self) -> None:
        self._exists = False
        self._filePath = ""
        self._airportLines = []
        self._airportChunked = []
        self._airports = []
        self._waypointLines = []
        self._waypointChunked = []
        self._waypoints = []
        self._heliportLines = []
        self._heliportChunked = []
        self._heliports = []
        self._ndbLines = []
        self._ndbChunked = []
        self._ndbs = []
        self._airwayLines = []
        self._airwayChunked = []
        self._airways = []
        self._vhfdmeLines = []
        self._vhfdmeChunked = []
        self._vhfdmes = []

    def setPath(self, path: str) -> None:
        dir = os.path.dirname(__file__)
        filePath = os.path.join(dir, path)
        self._filePath = filePath
        if os.path.exists(self._filePath):
            print(f"CIFPARSER :: Found CIFP file at: {path}")
            self._exists = True
        else:
            print(
                f"CIFPARSER :: Unable to find CIFP file at: {path} :: Interpreted as {filePath}"
            )

    def _splitSections(self) -> None:
        with open(self._filePath) as cifpFile:
            for line in cifpFile:
                sectionId = line[4:6]
                if sectionId == "D ":
                    self._vhfdmeLines.append(line)
                if sectionId == "DB" or sectionId == "PN":
                    self._ndbLines.append(line)
                if sectionId == "EA":
                    self._waypointLines.append(line)
                if sectionId == "ER":
                    self._airwayLines.append(line)
                if sectionId == "H ":
                    self._heliportLines.append(line)
                if sectionId == "P ":
                    self._airportLines.append(line)
                if sectionId == "UC":
                    pass
                if sectionId == "UR":
                    pass

    def _airportToObject(self) -> None:
        for airportChunk in self._airportChunked:
            airport = ca.CIFPAirport(airportChunk)
            self._airports.append(airport.toDict())

    def _ndbToObject(self) -> None:
        for ndbChunk in self._ndbChunked:
            ndb = cn.CIFPNDB(ndbChunk)
            self._ndbs.append(ndb.toDict())

    def _airwayToObject(self) -> None:
        for airwayChunk in self._airwayChunked:
            airway = cr.CIFPAirway(airwayChunk)
            self._airways.append(airway.toDict())

    def _vhfdmeToObject(self) -> None:
        for vhfdmeChunk in self._vhfdmeChunked:
            vhfdme = cv.CIFPVHFDME(vhfdmeChunk)
            self._vhfdmes.append(vhfdme.toDict())

    def _waypointToObject(self) -> None:
        for waypointChunk in self._waypointChunked:
            waypoint = cw.CIFPWaypoint(waypointChunk)
            self._waypoints.append(waypoint.toDict())

    def parse(self) -> None:
        if self._exists:
            functions = cf.CIFPFunctions()
            self._splitSections()
            # Process Airports
            self._airportChunked = functions.chunk(self._airportLines, 6, 10)
            self._airportToObject()
            del self._airportLines
            del self._airportChunked
            # Process NDBs
            self._ndbChunked = functions.chunk(self._ndbLines, 6, 22)
            self._ndbToObject()
            del self._ndbLines
            del self._ndbChunked
            # Process Routes
            self._airwayChunked = functions.chunk(self._airwayLines, 6, 19)
            self._airwayToObject()
            del self._airwayLines
            del self._airwayChunked
            # Process VHFDME
            self._vhfdmeChunked = functions.chunk(self._vhfdmeLines, 6, 22)
            self._vhfdmeToObject()
            del self._vhfdmeLines
            del self._vhfdmeChunked
            # Process Waypoint
            self._waypointChunked = functions.chunk(self._waypointLines, 6, 22)
            self._waypointToObject()
            del self._waypointLines
            del self._waypointChunked

    def getAirports(self) -> list:
        return self._airports

    def findAirport(self, airportId: str) -> dict:
        result = {}
        for airport in self._airports:
            if airport["id"] == airportId:
                result = airport
        return result

    def getAirways(self) -> list:
        return self._airways

    def findAirway(self, airwayId: str) -> dict:
        result = {}
        for airway in self._airways:
            if airway["id"] == airwayId:
                result = airway
        return result

    def getNDBs(self) -> list:
        return self._ndbs

    def findNDB(self, ndbId: str) -> dict:
        result = {}
        for ndb in self._ndbs:
            if ndb["id"] == ndbId:
                result = ndb
        return result

    def getVHFDMEs(self) -> list:
        return self._vhfdmes

    def findVHFDME(self, vhfdmeId: str) -> dict:
        result = {}
        for vhfdme in self._vhfdmes:
            if vhfdme["id"] == vhfdmeId:
                result = vhfdme
        return result

    def getWaypoints(self) -> list:
        return self._waypoints

    def findWaypoint(self, waypointId: str) -> dict:
        result = {}
        for waypoint in self._waypoints:
            if waypoint["id"] == waypointId:
                result = waypoint
        return result


import json

c = CIFP()
c.setPath("../../../../Downloads/FAACIFP18")
c.parse()
# ndb = c.findNDB("GTN")
# vor = c.findVHFDME("AML")
# fix = c.findWaypoint("RUANE")
# airway = c.findAirway("J146")
# airport = c.findAirport("KIAD")

airports = c.getAirports()
with open("temp.json", "w") as jsonFile:
    json.dump(airports, jsonFile, indent=2)
