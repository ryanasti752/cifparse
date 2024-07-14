# The CIFP_LOC_GS Object

The CIFP LOC/GS object comprises the following fields:

- area: The world region (e.g. `USA` or `CAN`).
- sec_code: The section code, used in parsing.
- airport_id: The ICAO code of the airport.
- airport_region: The ICAO region (e.g. `K6` for NE US) of the airport.
- sub_code: The subsection code, used in parsing.
- loc_id: The ID of the localizer.
- cat: The category of the localizer.
- frequency: The frequency of the localizer.
- runway_id: The associated runway ID.
- loc_lat: The LOC antenna array latitude.
- loc_lon: The LOC antenna array longitude.
- loc_bearing: The bearing of the localizer.
- gs_lat: The glide slope antenna latitude.
- gs_lon: The glide slope antenna longitude.
- loc_dist: The distance from the end of the associated runway to the antenna array.
- plus_minus: Related to the above, if it is on the near or far end.
- gs_thr_dist: The distance from the end of the associated runway to the antenna.
- loc_width: The width of the localizer beam.
- gs_angle: The angle of the glide slope.
- mag_var: The magnetic variation.
- tch: The threshold crossing height.
- gs_elevation: The elevation of the glide slope antenna.
- support_fac: The support facility.
- support_region: The region of the support facility.
- support_sec_code: The section code of the support facility.
- support_sub_code: The subsection code of the support facility.
- application: The application type, used in parsing.
- notes: The LOC/GS notes.
- record_number: The CIFP record number.
- cycle_data: The cycle ID of when the record was added/updated.
