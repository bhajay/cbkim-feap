# test SPGlib for a 2 atom cell
import numpy as np
import spglib as spg

a_x= 0.0000000000000000E+00
a_y= 0.2715474887350542E+01
a_z= 0.2715474887350542E+01

b_x= 0.2715474887350542E+01
b_y= 0.0000000000000000E+00
b_z= 0.2715474887350542E+01

c_x= 0.2715474887350542E+01
c_y= 0.2715474887350542E+01
c_z= 0.0000000000000000E+00

A = np.array([[a_x, b_x, c_x],
     [a_y, b_y, c_y],
     [a_z, b_z, c_z]])

# cartesian position of atom 1
r_1 = np.array([[0],[0],[0]])
# cartesian position of atom 2
r_2 = np.array([[ 0.1357737443675271E+01],[0.1357737443675271E+01],[0.1357737443675271E+01]])

# scaled position of atom 1
x_1 = np.dot(np.linalg.inv(A),r_1)
#scaled position of atom 2
x_2 = np.dot(np.linalg.inv(A),r_2)

a_1 = 0.00
b_1 = 0.00
c_1 = 0.00

a_2 = 0.25
b_2 = 0.25
c_2 = 0.25

n_1 = 14
n_2 = 14

lattice = [[a_x, a_y, a_z],
           [b_x, b_y, b_z],
           [c_x, c_y, c_z]]
positions = [[float(x_1[0]), float(x_1[1]), float(x_1[2])],
             [float(x_2[0]), float(x_2[1]), float(x_2[2])]]

numbers = [n_1, n_2]

cell = (lattice,positions,numbers)

spacegroup = spg.get_spacegroup(cell, symprec=1e-5)

print(spacegroup)

# the result gave Fd-3m (227) =====>  Silicon Cubic ... correct
