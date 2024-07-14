# The CIFPProcedure Object

The CIFP procedure object comprises the following fields:

- area: The world region (e.g. `USA` or `CAN`).
- sec_code: The section code, used in parsing.
- procedure_id: The ID (or computer code) of the procedure.

Additionally, the procedure object has a list of child objects:

- segments: A list of [CIFPProcedureSegment](./CIFPProcedureSegment.md) objects.
