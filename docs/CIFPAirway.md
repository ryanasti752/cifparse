# The CIFPAirway Object

The CIFP airway object comprises the following fields:

- area: The world region (e.g. `USA` or `CAN`).
- sec_code: The section code, used in parsing.
- sub_code: The subsection code, used in parsing.
- airway_id: The ID of the airway.
- six_char: A six character representation, if one exists.
- application: The application type, used in parsing.
- notes: The airway notes.

Additionally, the airway object has lists of child objects:

- points: A list[CIFPAirwayPoint](./CIFPAirwayPoint.md) objects.
