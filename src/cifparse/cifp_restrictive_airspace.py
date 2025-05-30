from .cifp_functions import chunk, clean_value
from .cifp_restrictive_airspace_segment import CIFPRestrictiveAirspaceSegment

from sqlite3 import Cursor

TABLE_NAME = "restrictive_airspace"


class CIFPRestrictiveAirspace:
    def __init__(self) -> None:
        self.area = None
        self.sec_code = None
        self.sub_code = None
        self.region = None
        self.restrictive_type = None
        self.restrictive_designation = None
        self.restrictive_name = None
        self.application = None
        self.time_ind = None
        self.op_time_1 = None
        self.op_time_2 = None
        self.op_time_3 = None
        self.op_time_4 = None
        self.op_time_5 = None
        self.op_time_6 = None
        self.op_time_7 = None
        self.controlling_agency = None
        self.segments: list[CIFPRestrictiveAirspaceSegment] = []

    def from_lines(self, cifp_lines: list) -> None:
        point_lines = []
        for cifp_line in cifp_lines:
            cont_rec_no = int(cifp_line[24:25])
            if cont_rec_no == 0 or cont_rec_no == 1:
                point_lines.append(cifp_line)
            if cont_rec_no == 1:
                self._cont1(cifp_line)
            if cont_rec_no == 2:
                self._cont2(cifp_line)

        segment_chunked = chunk(point_lines, 19, 20)
        self._segment_to_object(segment_chunked)

    def _segment_to_object(self, chunked_list: list) -> None:
        for segment_chunk in chunked_list:
            segment = CIFPRestrictiveAirspaceSegment()
            segment.from_lines(segment_chunk)
            self.segments.append(segment)

    def _cont1(self, cifp_line: str) -> None:
        if self.restrictive_name == None:
            # PAD 1
            self.area = cifp_line[1:4].strip()
            self.sec_code = cifp_line[4:5].strip()
            self.sub_code = cifp_line[5:6].strip()
            self.region = cifp_line[6:8].strip()
            self.restrictive_type = cifp_line[8:9].strip()
            self.restrictive_designation = cifp_line[9:19].strip()
            self.restrictive_name = cifp_line[93:123].strip()

    def _cont2(self, cifp_line: str) -> None:
        # PAD 25
        # cont_rec_no = int(cifp_line[24:25].strip())
        self.application = cifp_line[25:26].strip()
        self.time_code = cifp_line[26:27].strip()
        self.notam = cifp_line[27:28].strip()
        self.time_ind = cifp_line[28:29].strip()
        self.op_time_1 = cifp_line[29:39].strip()
        self.op_time_2 = cifp_line[39:49].strip()
        self.op_time_3 = cifp_line[49:59].strip()
        self.op_time_4 = cifp_line[59:69].strip()
        self.op_time_5 = cifp_line[69:79].strip()
        self.op_time_6 = cifp_line[79:89].strip()
        self.op_time_7 = cifp_line[89:99].strip()
        self.controlling_agency = cifp_line[99:123].strip()
        # self.record_number = cifp_line[123:128].strip()
        # self.cycle_data = cifp_line[128:132].strip()

    def create_db_table(db_cursor: Cursor) -> None:
        CIFPRestrictiveAirspaceSegment.create_db_table(db_cursor)

        drop_statement = f"DROP TABLE IF EXISTS `{TABLE_NAME}`;"
        db_cursor.execute(drop_statement)

        create_statement = f"""
            CREATE TABLE IF NOT EXISTS `{TABLE_NAME}` (
                `area` TEXT,
                `sec_code` TEXT,
                `sub_code` TEXT,
                `region` TEXT,
                `restrictive_type` TEXT,
                `restrictive_designation` TEXT,
                `restrictive_name` TEXT,
                `application` TEXT,
                `time_ind` TEXT,
                `op_time_1` TEXT,
                `op_time_2` TEXT,
                `op_time_3` TEXT,
                `op_time_4` TEXT,
                `op_time_5` TEXT,
                `op_time_6` TEXT,
                `op_time_7` TEXT,
                `controlling_agency` TEXT
            );
        """
        db_cursor.execute(create_statement)

    def to_db(self, db_cursor: Cursor) -> None:
        for item in self.segments:
            item.to_db(db_cursor)

        insert_statement = f"""
            INSERT INTO `{TABLE_NAME}` (
                `area`,
                `sec_code`,
                `sub_code`,
                `region`,
                `restrictive_type`,
                `restrictive_designation`,
                `restrictive_name`,
                `application`,
                `time_ind`,
                `op_time_1`,
                `op_time_2`,
                `op_time_3`,
                `op_time_4`,
                `op_time_5`,
                `op_time_6`,
                `op_time_7`,
                `controlling_agency`
            ) VALUES (
                ?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?
            );
        """
        db_cursor.execute(
            insert_statement,
            (
                clean_value(self.area),
                clean_value(self.sec_code),
                clean_value(self.sub_code),
                clean_value(self.region),
                clean_value(self.restrictive_type),
                clean_value(self.restrictive_designation),
                clean_value(self.restrictive_name),
                clean_value(self.application),
                clean_value(self.time_ind),
                clean_value(self.op_time_1),
                clean_value(self.op_time_2),
                clean_value(self.op_time_3),
                clean_value(self.op_time_4),
                clean_value(self.op_time_5),
                clean_value(self.op_time_6),
                clean_value(self.op_time_7),
                clean_value(self.controlling_agency),
            ),
        )

    def to_dict(self) -> dict:
        segments = []
        for item in self.segments:
            segments.append(item.to_dict())

        return {
            "area": clean_value(self.area),
            "sec_code": clean_value(self.sec_code),
            "sub_code": clean_value(self.sub_code),
            "region": clean_value(self.region),
            "restrictive_type": clean_value(self.restrictive_type),
            "restrictive_designation": clean_value(self.restrictive_designation),
            "restrictive_name": clean_value(self.restrictive_name),
            "application": clean_value(self.application),
            "time_ind": clean_value(self.time_ind),
            "op_time_1": clean_value(self.op_time_1),
            "op_time_2": clean_value(self.op_time_2),
            "op_time_3": clean_value(self.op_time_3),
            "op_time_4": clean_value(self.op_time_4),
            "op_time_5": clean_value(self.op_time_5),
            "op_time_6": clean_value(self.op_time_6),
            "op_time_7": clean_value(self.op_time_7),
            "controlling_agency": clean_value(self.controlling_agency),
            "segments": segments,
        }
