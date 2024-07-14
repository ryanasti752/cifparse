# The CIFPControlledAirspace Object

The CIFP controlled airspace object comprises the following fields:

- area: The world region (e.g. `USA` or `CAN`).
- sec_code: The section code, used in parsing.
- sub_code: The subsection code, used in parsing.
- region: The ICAO region (e.g. `K6` for NE US).
- airspace_type: The airspace type.
- center_id: The airport ID of the center point.
- center_sec_code: The section code of the center point.
- center_sub_code: The subsection code of the center point.
- airspace_class: The class of the airspace.
- application: The application type, used in parsing.
- time_code: The time code.
- notam: A marker for NOTAM-controlled timing.
- time_ind: The time indicator.
- op_time_1: The first operating time slot.
- op_time_2: The second operating time slot.
- op_time_3: The third operating time slot.
- op_time_4: The fourth operating time slot.
- op_time_5: The fifth operating time slot.
- op_time_6: The sixth operating time slot.
- op_time_7: The seventh operating time slot.
- controlling_agency: The controlling agency.

Additionally, the controlled airspace object has lists of child objects:

- segments: A list of [CIFPControlledAirspaceSegment](./CIFPControlledAirspaceSegment.md) objects.
