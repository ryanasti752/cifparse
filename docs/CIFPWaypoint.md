# The CIFPWaypoint Object

The CIFP waypoint object comprises the following fields:

- area: The world region (e.g. `USA` or `CAN`).
- sec_code: The section code, used in parsing.
- sub_code: The subsection code, used in parsing.
- environment: The waypoint association (e.g. `KIAD` for a waypoint associated with that airport).
- environment_region: The region of the association.
- waypoint_id: The ICAO code of the waypoint.
- region: The ICAO region (e.g. `K6` for NE US).
- type: The waypoint type
- usage: The use type (e.g. high, low, or both).
- lat: The waypoint latitude.
- lon: The waypoint longitude.
- mag_var: The magnetic variation.
- elevation: The elevation of the waypoint.
- datum_code: The reference system used in surveying.
- name: The name of the waypoint.
- name_description: The description of the name.
- application: The application type, used in parsing.
- notes: The waypoint notes.
- record_number: The CIFP record number.
- cycle_data: The cycle ID of when the record was added/updated.
