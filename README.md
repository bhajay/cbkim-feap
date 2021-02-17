# cbkim-feap
The repository contains working FEAP input files, python processing scripts, and some sample output images for the multi-scale finite element simulation of a pure Silicon cube. The high level directories of 01_SingleCell, 02_Supercell, and 03_Supercell_Vacancy each contain an ordered set of subdirectories chronologically sequenced with newer processing codes and most current input files found in the subdirectory with the greatest leading number. 

## Case 1: 01_SingleCell
This directory contains multiple sets of FEAP simulation input files for a single unit cell of Silicon subject to a uniform vertical displacement. The single cell is composed of two atoms in the basis.

## Case 2: 02_Supercell
This directory contains the FEAP simulation input files for a supercell of Silicon subject to a uniform vertical displacement. The supercell is composed of 16 atoms in the basis.

## Case 3: 03_Supercell_Vacancy
This directory contains the FEAP simulation input files for a single unit cell of Silicon subject to a uniform vertical displacement. The supercell with vacancy is composed of 16-1=15 atoms in the basis in which the 14th atom was removed.

## spglib
This directory is a working copy of the spglib library (https://github.com/spglib/spglib) for handling crystal symmetries.

## spglib_test
This directory contains a test file spg_lib.py which can be used as an example script for identifying a crystal structure space group using spglib.

## Notes on feap_cbkim.in input files
Within each subdirectory of cases 1-3, the feap_cbkim.in is defined to provide 
