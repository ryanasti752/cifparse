# The CIFP_NDB Object

The CIFP NDB object comprises the following fields:

- area: The world region (e.g. `USA` or `CAN`).
- sec_code: The section code, used in parsing.
- sub_code: The subsection code, used in parsing.
- airport_id: The ICAO ID of the associated airport.
- airport_region: The ICAO region of the associated airport.
- ndb_id: The ID of the VHF navaid.
- ndb_region: The ICAO region of the VHF navaid.
- frequency: The frequency.
- nav_class: The class of NDB.
- lat: The latitude of the NDB.
- lon: The longitude of the NDB.
- mag_var: The magnetic variation.
- datum_code: The reference system used in surveying.
- name: The name of the NDB.
- application: The application type, used in parsing.
- notes: The NDB notes.
- record_number: The CIFP record number.
- cycle_data: The cycle ID of when the record was added/updated.
