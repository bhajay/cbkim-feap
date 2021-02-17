# cbkim-feap
The repository contains working FEAP input files, python processing scripts, and some sample output images for the multi-scale finite element simulation of a pure Silicon cube. The high level directories of 01_SingleCell, 02_Supercell, and 03_Supercell_Vacancy each contain an ordered set of subdirectories chronologically sequenced with newer processing codes and most current input files found in the subdirectory with the greatest leading number. 

##01_SingleCell
This directory contains multiple sets of FEAP simulation input files for a single unit cell of Silicon subject to a uniform vertical displacement. The single cell is composed of two atoms in the basis.

##02_Supercell
This directory contains the FEAP simulation input files for a supercell of Silicon subject to a uniform vertical displacement. The supercell is composed of 16 atoms in the basis.

##03_Supercell_Vacancy
This directory contains the FEAP simulation input files for a single unit cell of Silicon subject to a uniform vertical displacement. The supercell with vacancy is composed of 16-1=15 atoms in the basis in which the 14th atom was removed.
