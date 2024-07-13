from cifp_functions import clean_value
from cifp_terminal_point import CIFPTerminalPoint


class CIFPProcedureSubsegment:
    def __init__(self) -> None:
        self.id = None
        self.points: list[CIFPTerminalPoint] = []

    def from_lines(self, cifp_lines: list) -> None:
        initial = str(cifp_lines[0])
        transition_id = initial[20:25].strip()
        self.id = transition_id

        for cifp_line in cifp_lines:
            cont_rec_no = int(cifp_line[38:39])
            if cont_rec_no == 0 or cont_rec_no == 1:
                self._cont0(cifp_line)

    def _cont0(self, cifp_line: str) -> None:
        point = CIFPTerminalPoint()
        point.from_line(cifp_line)
        self.points.append(point)

    def to_dict(self) -> dict:
        points = []
        for item in self.points:
            points.append(item.to_dict())

        return {"id": clean_value(self.id), "points": points}
