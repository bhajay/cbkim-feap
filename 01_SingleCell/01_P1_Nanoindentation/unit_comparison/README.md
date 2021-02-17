# unit_comparison
FEAP input files to test how changes in units effect the output units.

When writing the length units in feap_cbkim.in as meters,
```
length 1.d0 !m 
```
this gives output stress in Pa.

When writing the length units in feap_cbkim.in as millimeters,
```
length 1.d-3 !mm 
```
this gives output stress in MPa.
