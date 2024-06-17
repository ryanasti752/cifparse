import cifpfunctions as cf
import cifpproceduresegment as cs


class CIFPProcedure:
    def __init__(self, cifpLines: list) -> None:
        self.area = None
        self.secCode = None
        self.id = None
        self.segmentChunked = []
        self.segments = []

        functions = cf.CIFPFunctions()
        self.segmentChunked = functions.chunk(cifpLines, 13, 20)
        self._segmentToObject()
        del self.segmentChunked

        cifpLine = str(cifpLines[0])
        self.area = cifpLine[1:4].strip()
        self.secCode = cifpLine[4:5].strip()
        self.id = cifpLine[13:19].strip()

    def _segmentToObject(self) -> None:
        for segmentChunk in self.segmentChunked:
            segment = cs.CIFPProcedureSegment(segmentChunk)
            self.segments.append(segment.toDict())

    def toDict(self) -> dict:
        functions = cf.CIFPFunctions()
        functions.cleanDict(self.__dict__)
        return self.__dict__
