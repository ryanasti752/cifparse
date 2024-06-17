# cifparse

A python parser for the FAA CIFP.

# Installation

Install using `pip`:

```
pip install cifparse
```

# Usage

Usage is relatively straightforward. Setting the path to the file can be somewhat finnicky, as it will only accept relative paths. To keep things simple, place the CIFP file in your project directory. Otherwise, if you want to go up several folders into a download folder, it might end up looking like `../../../../Downloads/FAACIFP18`.

Given the amount of data, parsing can take a moment. If dumping the data to a file, that can also add time. Dumping every airport to JSON can take around 15 seconds, and the resulting file is about 330MB.

## Examples

```python
import cifparse

# Initialize the parser:
c = CIFP()

# Set the path to where you have the CIFP file:
c.setPath("FAACIFP18")

# Parse the data in the file:
c.parse()

# All of the results will be in the CIFP object, accessible via getters:
ndbs = c.getNDBs()
vors = c.getVHFDMEs()
fixes = c.getWaypoints()
airways = c.getAirways()
airports = c.getAirports()

# To find specific items, use the find functions:
ndb = c.findNDB("GTN")
vor = c.findVHFDME("AML")
fix = c.findWaypoint("RUANE")
airway = c.findAirway("J146")
airport = c.findAirport("KIAD")

# Because of the size of the objects, you may want to dump the results into a json file.
# To view the dump of a specific airport (KIAD, above), use something like this:
with open("output.json", "w") as jsonFile:
    json.dump(airport, jsonFile, indent=2)
```
