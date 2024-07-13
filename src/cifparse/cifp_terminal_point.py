from cifp_functions import clean_value


class CIFPTerminalPoint:
    def __init__(self) -> None:
        self.area = None
        self.sec_code = None
        self.airport_id = None
        self.airport_region = None
        self.sub_code = None
        self.id = None
        self.route_type = None
        self.transition_id = None
        self.sequence_number = None
        self.fix_id = None
        self.fix_region = None
        self.fix_sec_code_2 = None
        self.fix_sub_code_2 = None
        self.description_code = None
        self.turn_direction = None
        self.rnp = None
        self.path_term = None
        self.tdv = None
        self.rec_vhf = None
        self.rec_vhf_region = None
        self.arc_radius = None
        self.theta = None
        self.rho = None
        self.course = None
        self.dist = None
        self.time = None
        self.vhf_sec_code = None
        self.vhf_sub_code = None
        self.alt_desc = None
        self.atc = None
        self.altitude = None
        self.flight_level = None
        self.altitude_2 = None
        self.flight_level_2 = None
        self.altitude2 = None
        self.trans_alt = None
        self.speed_limit = None
        self.vert_angle = None
        self.center_fix = None
        self.multiple_code = None
        self.center_fix_region = None
        self.center_fix_sec_code = None
        self.center_fix_sub_code = None
        self.gns_fms_id = None
        self.speed_limit_2 = None
        self.rte_qual_1 = None
        self.rte_qual_2 = None
        self.record_number = None
        self.cycle_data = None

    def from_line(self, cifp_line: str) -> None:
        # PAD 1
        self.area = cifp_line[1:4].strip()
        self.sec_code = cifp_line[4:5].strip()
        # PAD 1
        self.airport_id = cifp_line[6:10].strip()
        self.airport_region = cifp_line[10:12].strip()
        self.sub_code = cifp_line[12:13].strip()
        self.id = cifp_line[13:19].strip()
        self.route_type = cifp_line[19:20].strip()
        self.transition_id = cifp_line[20:25].strip()
        self.sequence_number = int(cifp_line[26:29].strip())
        self.fix_id = cifp_line[29:34].strip()
        self.fix_region = cifp_line[34:36].strip()
        self.fix_sec_code_2 = cifp_line[36:37].strip()
        self.fix_sub_code_2 = cifp_line[37:38].strip()
        # self.cont_rec_no = int(cifp_line[38:39])
        self.description_code = cifp_line[39:43]
        self.turn_direction = cifp_line[43:44].strip()
        self.rnp = cifp_line[44:47].strip()
        self.path_term = cifp_line[47:49].strip()
        self.tdv = cifp_line[49:50].strip()
        self.rec_vhf = cifp_line[50:54].strip()
        self.rec_vhf_region = cifp_line[54:56].strip()
        arc_rad = cifp_line[56:62].strip()
        theta_s = cifp_line[62:66].strip()
        rho_s = cifp_line[66:70].strip()
        crs = cifp_line[70:74].strip()
        dist = cifp_line[74:78].strip()
        self.vhf_sec_code = cifp_line[78:79].strip()
        self.vhf_sub_code = cifp_line[79:80].strip()
        self.alt_desc = cifp_line[82:83].strip()
        self.atc = cifp_line[83:84].strip()
        alt = cifp_line[84:89].strip()
        alt_2 = cifp_line[89:94].strip()
        trans_alt = cifp_line[94:99].strip()
        speed = cifp_line[99:102].strip()
        vert_angle = cifp_line[102:106].strip()
        self.center_fix = cifp_line[106:111].strip()
        self.multiple_code = cifp_line[111:112].strip()
        self.center_fix_region = cifp_line[112:114].strip()
        self.center_fix_sec_code = cifp_line[114:115].strip()
        self.center_fix_sub_code = cifp_line[115:116].strip()
        self.gns_fms_id = cifp_line[116:117].strip()
        self.speed_limit_2 = cifp_line[117:118].strip()
        self.rte_qual_1 = cifp_line[118:119].strip()
        self.rte_qual_2 = cifp_line[119:120].strip()
        self.record_number = int(cifp_line[123:128].strip())
        self.cycle_data = cifp_line[128:132].strip()

        if arc_rad != "":
            self.arc_radius = int(arc_rad) / 1000

        if theta_s != "":
            self.theta = int(theta_s) / 10

        if rho_s != "":
            self.rho = int(rho_s) / 10

        if crs != "":
            self.course = int(crs) / 10

        if dist != "":
            if dist.startswith("T"):
                self.time = int(dist[1:]) / 10
            else:
                self.distance = int(dist) / 10

        if alt != "":
            if alt.startswith("FL"):
                self.flight_level = int(alt[2:])
            else:
                self.altitude = int(alt)

        if alt_2 != "":
            if alt_2.startswith("FL"):
                self.flight_level_2 = int(alt_2[2:])
            else:
                self.altitude_2 = int(alt_2)

        if trans_alt != "":
            self.transition_alt = int(trans_alt)

        if speed != "":
            self.speed_limit = int(speed)

        if vert_angle != "":
            self.vertical_angle = int(vert_angle)

    def to_dict(self) -> dict:
        return {
            "area": clean_value(self.area),
            "sec_code": clean_value(self.sec_code),
            "airport_id": clean_value(self.airport_id),
            "airport_region": clean_value(self.airport_region),
            "sub_code": clean_value(self.sub_code),
            "id": clean_value(self.id),
            "route_type": clean_value(self.route_type),
            "transition_id": clean_value(self.transition_id),
            "sequence_number": clean_value(self.sequence_number),
            "fix_id": clean_value(self.fix_id),
            "fix_region": clean_value(self.fix_region),
            "fix_sec_code_2": clean_value(self.fix_sec_code_2),
            "fix_sub_code_2": clean_value(self.fix_sub_code_2),
            "description_code": clean_value(self.description_code),
            "turn_direction": clean_value(self.turn_direction),
            "rnp": clean_value(self.rnp),
            "path_term": clean_value(self.path_term),
            "tdv": clean_value(self.tdv),
            "rec_vhf": clean_value(self.rec_vhf),
            "rec_vhf_region": clean_value(self.rec_vhf_region),
            "arc_radius": clean_value(self.arc_radius),
            "theta": clean_value(self.theta),
            "rho": clean_value(self.rho),
            "course": clean_value(self.course),
            "dist": clean_value(self.dist),
            "time": clean_value(self.time),
            "vhf_sec_code": clean_value(self.vhf_sec_code),
            "vhf_sub_code": clean_value(self.vhf_sub_code),
            "alt_desc": clean_value(self.alt_desc),
            "atc": clean_value(self.atc),
            "altitude": clean_value(self.altitude),
            "flight_level": clean_value(self.flight_level),
            "altitude_2": clean_value(self.altitude_2),
            "flight_level_2": clean_value(self.flight_level_2),
            "altitude2": clean_value(self.altitude2),
            "trans_alt": clean_value(self.trans_alt),
            "speed_limit": clean_value(self.speed_limit),
            "vert_angle": clean_value(self.vert_angle),
            "center_fix": clean_value(self.center_fix),
            "multiple_code": clean_value(self.multiple_code),
            "center_fix_region": clean_value(self.center_fix_region),
            "center_fix_sec_code": clean_value(self.center_fix_sec_code),
            "center_fix_sub_code": clean_value(self.center_fix_sub_code),
            "gns_fms_id": clean_value(self.gns_fms_id),
            "speed_limit_2": clean_value(self.speed_limit_2),
            "rte_qual_1": clean_value(self.rte_qual_1),
            "rte_qual_2": clean_value(self.rte_qual_2),
            "record_number": clean_value(self.record_number),
            "cycle_data": clean_value(self.cycle_data),
        }
