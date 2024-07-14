# The CIFPRestrictiveAirspaceSegment Object

The CIFP restrictive airspace segment object comprises the following fields:

- multiple_code: The multiple code, used in parsing.
- lower_limit: The lower limit of the airspace.
- lower_unit: The unit of the lower limit.
- upper_limit The upper limit of the airspace.
- upper_unit: The unit of the upper limit.

Additionally, the restrictive airspace segment object has lists of child objects:

- points: A list of [CIFPRestrictiveAirspacePoint](./CIFPRestrictiveAirspacePoint.md) objects.
