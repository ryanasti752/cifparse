# The CIFPRestrictiveAirspace Object

The CIFP restrictive airspace object comprises the following fields:

- area: The world region (e.g. `USA` or `CAN`).
- sec_code: The section code, used in parsing.
- sub_code: The subsection code, used in parsing.
- region: The ICAO region (e.g. `K6` for NE US).
- restrictive_type: The type of restrictive airspace (e.g. MOA, Warning, Alert, etc.).
- restrictive_designation: The restrictive airspace designation (short name).
- restrictive_name: The restrictive airspace name.
- application: The application type, used in parsing.
- time_ind: The time indicator.
- op_time_1: The first operating time slot.
- op_time_2: The second operating time slot.
- op_time_3: The third operating time slot.
- op_time_4: The fourth operating time slot.
- op_time_5: The fifth operating time slot.
- op_time_6: The sixth operating time slot.
- op_time_7: The seventh operating time slot.
- controlling_agency: The controlling agency.

Additionally, the restrictive airspace object has lists of child objects:

- segments: A list of [CIFPRestrictiveAirspaceSegment](./CIFPRestrictiveAirspaceSegment.md) objects.
