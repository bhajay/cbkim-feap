# cbkim-feap
The repository contains working FEAP input files, python processing scripts, and some sample output images for the multi-scale finite element simulation of a pure Silicon cube. The high level directories of 01_SingleCell, 02_Supercell, and 03_Supercell_Vacancy each contain an ordered set of subdirectories chronologically sequenced with newer python processing codes and most recently tested input files found in the subdirectory with the greatest leading number. 

The CBKim api is inspired by the open knowledgebase of interatomic models website OpenKIM  
OpenKIM: https://openkim.org/doc/overview/getting-started/

You can get started by installing the KIM API package by following the instructions below.  
KIM API: https://openkim.org/doc/usage/obtaining-models/

To access the GitHub for CBKim, you will need a public ssh key if you don't already have one.  
SSH Key: https://git-scm.com/book/en/v2/Git-on-the-Server-Generating-Your-SSH-Public-Key

___

# Directory Overview
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

## cbkim_setup_documentation
Contains a PDF document outlining the process required to install CBKim and successfully integrate with FEAP.

## matlab_lattice_code
Contains a matlab script lattice.m which can be used as a visualization tool for a crystal lattice given lattice basis vectors and primitive unit cell atom positions.

___

# feap_cbkim.in 
Within each subdirectory of cases 1-3, feap_cbkim.in is the Cbkim input file to FEAP defining basis vectors, initial atom positions, atom masses, and constitutive information of the material lattice. The data within this file is defined with the following structure (Example is taken from 01_Singlecell/01_P1_Nanoindentation).

###### Set convergence tolerance for conjugate gradient optimization step when minimizing energy of configuration
```
% Set convergence tolerance for CG
 fact,gtol,1e-16
 ```
 ###### Read in material definitions
 ```
 % read in material definitions
 mate,dire
  1
  'Si(diamond)-SW'
  ```
  ###### Define lattice basis vectors 
  ```
    0.0000000000000000E+00 0.2715474887350542E+01 0.2715474887350542E+01
    0.2715474887350542E+01 0.0000000000000000E+00 0.2715474887350542E+01
    0.2715474887350542E+01 0.2715474887350542E+01 0.0000000000000000E+00
   ```
   ###### Define 2 atoms of material number 14 (Si) with 3 position components x1, x2, x3
   ```
   2
   14  0.0000000000000000E+00 0.0000000000000000E+00 0.0000000000000000E+00
   14  0.1357737443675271E+01 0.1357737443675271E+01 0.1357737443675271E+01
   ```
   ###### Define Masses of the 2 atoms
   ```
    0.2883000000000000E+02
    0.2883000000000000E+02
   ```
 ###### Read in the Consitutive Model information from OpenKim 
 ```
 % read in constitutive information
 cons,kim,SW_StillingerWeber_1985_Si__MO_405512056662_005
 
 % Find optimal lattice parameters and reset lattice
 opti,,1
 ```
# atom_position.py 
This script can be found in `02*\02*` and `\03*\03*` to plot the components of atom positions over time.   
Given output file (`Osi`) and history files (`Psia.his`, `Psia.his`) from FEAP, this python script will iteratively plot the 15 atom position components on one figure for all time steps throughout the simulation. Notice the atoms located at position `(0,0,0)` is implied to remain stationary and is therefore leftout from the history file data.  
A numpy array will be output as `R_out.npy` containing the components of each atom position for every time step through the simulation. This numpy array is then utilized within 
