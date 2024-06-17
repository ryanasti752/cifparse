import cifpfunctions as cf


class CIFPNDB:
    def __init__(self, cifpLines: list) -> None:
        for cifpLine in cifpLines:
            contRecNo = int(cifpLine[21:22])
            if contRecNo == 0:
                self.cont0(cifpLine)
            if contRecNo == 1:
                self.cont1(cifpLine)

    def cont0(self, cifpLine: str) -> None:
        # PAD 1
        self.area = cifpLine[1:4].strip()
        self.secCode = cifpLine[4:5].strip()
        self.subCode = cifpLine[5:6].strip()
        self.airportId = cifpLine[7:10].strip()
        self.region = cifpLine[10:12].strip()
        # PAD 1
        self.id = cifpLine[13:17].strip()
        # PAD 2
        self.subregion = cifpLine[19:21].strip()
        # self.contRecNo = int(cifpLine[21:22].strip())
        self.freq = cifpLine[22:27].strip()
        self.frequency = None
        self.navClass = cifpLine[27:32].strip()
        self.latlon = cifpLine[32:51].strip()
        self.lat = None
        self.lon = None
        # PAD 23
        self.variation = cifpLine[74:79].strip()
        self.magvar = None
        # PAD 6
        # RESERVED 5
        self.datumCode = cifpLine[90:93].strip()
        self.name = cifpLine[93:123].strip()
        self.recordNo = int(cifpLine[123:128].strip())
        self.cycleData = cifpLine[128:132].strip()
        self.translate()

    def cont1(self, cifpLine: str) -> None:
        # PAD 22
        self.application = cifpLine[22:23].strip()
        self.notes = cifpLine[23:91].strip()

    def translate(self) -> None:
        functions = cf.CIFPFunctions()
        if self.freq != "":
            self.frequency = int(self.freq) / 10
        del self.freq

        if self.latlon != "":
            coordinates = functions.convertDMS(self.latlon)
            self.lat = coordinates.lat
            self.lon = coordinates.lon
        del self.latlon

        if self.variation != "":
            magvar = functions.convertMagVar(self.variation)
            self.magvar = magvar
        del self.variation

    def toDict(self) -> dict:
        functions = cf.CIFPFunctions()
        functions.cleanDict(self.__dict__)
        return self.__dict__
