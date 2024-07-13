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
from cifparse import CIFP

# Set the path to where you have the CIFP file:
c = CIFP("FAACIFP18")

# Parse the data in the file:
c.parse()
# ...or to save time, parse only a specific subset:
c.parse_airports()
c.parse_heliports()
c.parse_ndbs()
c.parse_airways()
c.parse_vhf_dmes()
c.parse_waypoints()
c.parse_controlled()
c.parse_restrictive()

# The results will be in the CIFP object, accessible via getters that return lists of the objects:
airports = c.get_airports()
heliports = c.get_heliports()
airways = c.get_airways()
ndbs = c.get_NDBs()
vordmes = c.get_VHF_DMEs()
waypoints = c.get_waypoints()
controlled = c.get_controlled()
restrictive = c.get_restrictive()

# To find specific objects in the lists, use the find functions:
airport = c.find_airport("KIAD")
heliport = c.find_heliport("DC03")
airway = c.find_airway("J146")
ndb = c.find_NDB("GTN")
vor = c.find_VHF_DME("AML")
fix = c.find_waypoint("RAVNN")
dc_class_b = c.find_controlled("KDCA")
roa_class_c = c.find_controlled("KROA")
cho_class_d = c.find_controlled("KCHO")
moa = c.find_restrictive("DEMO 1 MOA")

# Because the Alert, MOA, Restricted, and Warning airspace can occasionally be named oddly, there is an additional helper function that finds all matches of a particular substring:
all_5314 = c.find_restrictive_match("5314")
# Returns: [R-5314A, R-5314B, R-5314C, R-5314D, R-5314E, R-5314F, R-5314H, R-5314J]

# Because of the size of the objects, you may want to dump the results into a json file.
# To view the dump of a specific airport (KIAD, above), use something like this:
with open("output.json", "w") as jsonFile:
    json.dump(airport, jsonFile, indent=2)
```
