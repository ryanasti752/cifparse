# The CIFPAirwayPoint Object

The CIFP airway point object comprises the following fields:

- area: The world region (e.g. `USA` or `CAN`).
- sec_code: The section code, used in parsing.
- sub_code: The subsection code, used in parsing.
- airway_id: The ID of the airway.
- six_char: A six character ID if one exists.
- sequence_number: The sequence number of the point in the airway.
- point_id: The ID of the point along the airway.
- point_region: The region of the point.
- point_sec_code: The section code of the point.
- point_sub_code: The subsection of the point.
- description_code: The description code, used in parsing.
- bound_code: The code of the boundary being crossed.
- route_type: The airway type.
- level: The level of the airway (high, low, or both).
- direct: A one-way restriction in relation to the sequence numbers (forward or backward). Blank if none.
- tc_ind: The cruise table indicator.
- eu_ind: The EU indicator.
- rec_vhf: The ID of the recommended navaid.
- rec_vhf_region: The ICAO region of the recommended navaid.
- rnp: The RNP value.
- theta: The magnetic bearing to the `point_id` from the `rec_vhf`.
- rho: The distance to the `point_id` from the `rec_vhf`.
- out_mag_crs: The outbound magnetic course.
- from_dist: The distance from this point to the next.
- in_mag_crs: The inbound magnetic course.
- min_alt: The minimum altitude.
- min_alt_2: The second minimum altitude.
- max_alt: The maximum altitude.
- fix_radius: The fixed radius transition value.
- sig_point: Some airways are not continuous. This identifier notes if the point is the start (`S`) or end (`E`) point for that section.
- record_number: The CIFP record number.
- cycle_data: The cycle ID of when the record was added/updated.
