import numpy as np
import spglib as spg

natoms=2 # excluding [0,0,0] atom and removedatom
# import the saved numpy array for atom positions
R = np.load('R_out.npy')


# Use SPGLIB to classify crystal structure-------------*---------------

# define basis vectors


a_x= 0.00000000
a_y= 5.43094977/2
a_z= 5.43094977/2

b_x= 5.43094977/2
b_y= 0.00000000
b_z= 5.43094977/2

c_x= 5.43094977/2
c_y= 5.43094977/2
c_z= 0.00000000

A = np.array([[a_x, b_x, c_x],
              [a_y, b_y, c_y],
              [a_z, b_z, c_z]])
trange = 169
tc1=5
tc2=165
space_groups = []
for tcheck in np.arange(trange):
  print('tcheck='+str(tcheck))
  r_0 = R[tcheck][0][:]
  r_1 = R[tcheck][1][:]



  # get scaled position
  x_0 = np.dot(np.linalg.inv(A),r_0)
  x_1 = np.dot(np.linalg.inv(A),r_1)


  lattice = [[a_x, a_y, a_z],
            [b_x, b_y, b_z],
            [c_x, c_y, c_z]]

  positions = [[float(x_0[0]), float(x_0[1]), float(x_0[2])],
              [float(x_1[0]), float(x_1[1]), float(x_1[2])]]

  numbers = [2,]*natoms

  cell = (lattice, positions, numbers)

  spacegroup = spg.get_spacegroup(cell, symprec=1e-5)
  print('Supercell Spacegroup (t ='+ str(tcheck)+') = ' + spacegroup)
  space_groups.append(spacegroup)


