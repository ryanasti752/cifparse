import coordinate as c


class CIFPFunctions:
    def convertDMS(self, cifpDMSSubstring: str) -> c.Coordinate:
        latString = cifpDMSSubstring[0:9]
        lonString = cifpDMSSubstring[9:19]
        northSouth = latString[0:1]
        latD = int(latString[1:3])
        latM = int(latString[3:5])
        latS = int(latString[5:]) / 100
        eastWest = lonString[0:1]
        lonD = int(lonString[1:4])
        lonM = int(lonString[4:6])
        lonS = int(lonString[6:]) / 100
        coord = c.Coordinate()
        coord.fromDMS(northSouth, latD, latM, latS, eastWest, lonD, lonM, lonS)
        return coord

    def convertMagVar(self, cifpMagVarSubstring: str) -> float:
        magVarValue = int(cifpMagVarSubstring[1:]) / 10
        if cifpMagVarSubstring[0:1] == "W":
            magVarValue = -magVarValue
        return magVarValue

    def chunk(
        self,
        lineArray: list,
        idStart: int,
        idStop: int,
    ) -> list:
        lastId = ""
        chunk = []
        result = []
        for line in lineArray:
            currentId = line[idStart:idStop]
            if currentId != lastId and lastId != "":
                result.append(chunk)
                chunk = []
            chunk.append(line)
            lastId = currentId
        if len(chunk) > 0:
            result.append(chunk)
        return result

    def cleanDict(self, dictionary: dict) -> dict:
        for item, value in dictionary.items():
            if value == "":
                dictionary[item] = None
        return dictionary
