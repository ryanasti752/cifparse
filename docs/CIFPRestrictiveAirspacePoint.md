# The CIFPRestrictiveAirspacePoint Object

The CIFP restrictive airspace point object comprises the following fields:

- area: The world region (e.g. `USA` or `CAN`).
- sec_code: The section code, used in parsing.
- sub_code: The subsection code, used in parsing.
- region: The ICAO region (e.g. `K6` for NE US).
- restrictive_type: The airspace type.
- restrictive_designation: The airspace designation.
- multiple_code: The multiple code, used in parsing.
- sequence_number: The sequence number of the point in the airspace.
- level: The airspace level.
- time_zone: The time zone.
- notam: A marker for NOTAM-controlled timing.
- boundary_via: A marker showing how the boundary is defined.
- lat: The latitude of the point.
- lon: The longitude of the point.
- arc_lat: The latitude of the arc.
- arc_lon: The longitude of the arc.
- arc_dist: The distance from the arc lat/lon point.
- arc_bearing: The starting bearing of the arc.
- lower_limit: The lower limit of the airspace.
- lower_unit: The unit of the lower limit.
- upper_limit The upper limit of the airspace.
- upper_unit: The unit of the upper limit.
- restrictive_name: The name of the airspace.
- record_number: The CIFP record number.
- cycle_data: The cycle ID of when the record was added/updated.
