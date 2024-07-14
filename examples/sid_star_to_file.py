from cifparse import CIFP
import json


def find_point(airport_object: object, point_string: str) -> list:
    for point in airport_object.points:
        if point.waypoint_id == point_string:
            return [point.lon, point.lat]
    point = c.find_waypoint(point_string)
    if point != None:
        return [point.lon, point.lat]
    vor = c.find_vhf_dme(point_string)
    if vor != None:
        return [vor.lon, vor.lat]
    ndb = c.find_ndb(point_string)
    if ndb != None:
        return [ndb.lon, ndb.lat]
    airport = c.find_airport(point_string)
    if airport != None:
        return [airport.lon, airport.lat]
    return [0, 0]


def build_sid_star(airport: object):
    for proc in airport.departures:
        proc_segments = []
        if hasattr(proc, "segments"):
            for seg in proc.segments:
                if hasattr(seg, "transitions") and len(seg.transitions) > 0:
                    for transition in seg.transitions:
                        print(
                            f"Assembling {proc.procedure_id} :: {transition.transition_id}"
                        )
                        points = []
                        if hasattr(transition, "points"):
                            for point in transition.points:
                                found_point = find_point(airport, point.fix_id)
                                if found_point[0] != 0:
                                    points.append([found_point[0], found_point[1]])
                        if len(points) > 1:
                            proc_segments.append(points)
                if hasattr(seg, "points") and len(seg.points) > 0:
                    points = []
                    for point in seg.points:
                        found_point = find_point(airport, point.fix_id)
                        if found_point[0] != 0:
                            points.append([found_point[0], found_point[1]])
                    if len(points) > 1:
                        proc_segments.append(points)
        json_data = {
            "type": "FeatureCollection",
            "features": [
                {
                    "type": "Feature",
                    "geometry": {
                        "type": "MultiLineString",
                        "coordinates": proc_segments,
                    },
                    "properties": {},
                }
            ],
        }

        with open(
            f"{airport.airport_id[1:]}_SID_{proc.procedure_id[:-1]}.geojson", "w"
        ) as json_file:
            json.dump(json_data, json_file, indent=2)

    for proc in airport.arrivals:
        proc_segments = []
        if hasattr(proc, "segments"):
            for seg in proc.segments:
                if hasattr(seg, "transitions") and len(seg.transitions) > 0:
                    for transition in seg.transitions:
                        print(
                            f"Assembling {proc.procedure_id} :: {transition.transition_id}"
                        )
                        points = []
                        if hasattr(transition, "points"):
                            for point in transition.points:
                                found_point = find_point(airport, point.fix_id)
                                if found_point[0] != 0:
                                    points.append([found_point[0], found_point[1]])
                        proc_segments.append(points)
                if hasattr(seg, "points") and len(seg.points) > 0:
                    points = []
                    for point in seg.points:
                        found_point = find_point(airport, point.fix_id)
                        if found_point[0] != 0:
                            points.append([found_point[0], found_point[1]])
                    proc_segments.append(points)
        json_data = {
            "type": "FeatureCollection",
            "features": [
                {
                    "type": "Feature",
                    "geometry": {
                        "type": "MultiLineString",
                        "coordinates": proc_segments,
                    },
                    "properties": {},
                }
            ],
        }

        with open(
            f"{airport.airport_id[1:]}_STAR_{proc.procedure_id[:-1]}.geojson", "w"
        ) as json_file:
            json.dump(json_data, json_file, indent=2)


c = CIFP("FAACIFP18")
c.parse()

airport = c.find_airport("KIAD")
build_sid_star(airport)
