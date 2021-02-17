import numpy as np
import spglib as spg

natoms=14 # excluding [0,0,0] atom and removedatom
# import the saved numpy array for atom positions
R = np.load('R_out.npy')


# Use SPGLIB to classify crystal structure-------------*---------------

# define basis vectors


a_x= 0.00000000
a_y= 5.43094977
a_z= 5.43094977

b_x= 5.43094977
b_y= 0.00000000
b_z= 5.43094977

c_x= 5.43094977
c_y= 5.43094977
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
  r_2 = R[tcheck][2][:]
  r_3 = R[tcheck][3][:]
  r_4 = R[tcheck][4][:]
  r_5 = R[tcheck][5][:]
  r_6 = R[tcheck][6][:]
  r_7 = R[tcheck][7][:]
  r_8 = R[tcheck][8][:]
  r_9 = R[tcheck][9][:]
  r_10 = R[tcheck][10][:]
  r_11 = R[tcheck][11][:]
  r_12 = R[tcheck][12][:]
  r_13 = R[tcheck][13][:]



  # get scaled position
  x_0 = np.dot(np.linalg.inv(A),r_0)
  x_1 = np.dot(np.linalg.inv(A),r_1)
  x_2 = np.dot(np.linalg.inv(A),r_2)
  x_3 = np.dot(np.linalg.inv(A),r_3)
  x_4 = np.dot(np.linalg.inv(A),r_4)
  x_5 = np.dot(np.linalg.inv(A),r_5)
  x_6 = np.dot(np.linalg.inv(A),r_6)
  x_7 = np.dot(np.linalg.inv(A),r_7)
  x_8 = np.dot(np.linalg.inv(A),r_8)
  x_9 = np.dot(np.linalg.inv(A),r_9)
  x_10 = np.dot(np.linalg.inv(A),r_10)
  x_11 = np.dot(np.linalg.inv(A),r_11)
  x_12 = np.dot(np.linalg.inv(A),r_12)
  x_13 = np.dot(np.linalg.inv(A),r_13)



  lattice = [[a_x, a_y, a_z],
            [b_x, b_y, b_z],
            [c_x, c_y, c_z]]

  positions = [[float(x_0[0]), float(x_0[1]), float(x_0[2])],
              [float(x_1[0]), float(x_1[1]), float(x_1[2])],
              [float(x_2[0]), float(x_2[1]), float(x_2[2])],
              [float(x_3[0]), float(x_3[1]), float(x_3[2])],
              [float(x_4[0]), float(x_4[1]), float(x_4[2])],
              [float(x_5[0]), float(x_5[1]), float(x_5[2])],
              [float(x_6[0]), float(x_6[1]), float(x_6[2])],
              [float(x_7[0]), float(x_7[1]), float(x_7[2])],
              [float(x_8[0]), float(x_8[1]), float(x_8[2])],
              [float(x_9[0]), float(x_9[1]), float(x_9[2])],
              [float(x_10[0]), float(x_10[1]), float(x_10[2])],
              [float(x_11[0]), float(x_11[1]), float(x_11[2])],
              [float(x_12[0]), float(x_12[1]), float(x_12[2])],
              [float(x_13[0]), float(x_13[1]), float(x_13[2])]]
  if tcheck == tc1:
    x_7p1 = x_7
    x_8p1 = x_8
    positions1 = [[float(x_7p1[0]-x_7p1[0]), float(x_7p1[1]-x_7p1[1]), float(x_7p1[2]-x_7p1[2])],
                   [float(x_8p1[0]-x_7p1[0]), float(x_8p1[1]-x_7p1[1]), float(x_8p1[2]-x_7p1[2])]]
  if tcheck == tc2:
    x_7p2 = x_7
    x_8p2 = x_8
    positions2 = [[float(x_7p2[0]-x_7p2[0]), float(x_7p2[1]-x_7p2[1]), float(x_7p2[2]-x_7p2[2])],
                   [float(x_8p2[0]-x_7p2[0]), float(x_8p2[1]-x_7p2[1]), float(x_8p2[2]-x_7p2[2])]]

  numbers = [14,]*natoms

  cell = (lattice, positions, numbers)

  spacegroup = spg.get_spacegroup(cell, symprec=1e-5)
  print('Supercell Spacegroup (t ='+ str(tcheck)+') = ' + spacegroup)
  space_groups.append(spacegroup)


numbers1 = [14,]*2
numbers2 = [14,]*2
cellp1 = (lattice, positions1, numbers1)
cellp2 = (lattice, positions2, numbers2)
spacegroup1 = spg.get_spacegroup(cellp1, symprec=1e-5)
spacegroup2 = spg.get_spacegroup(cellp2, symprec=1e-5)
cellp1 = (lattice, positions1, numbers1)
cellp2 = (lattice, positions2, numbers2)
print('Unit Cell Spacegroup (t(n=' + str(tc1) +'))  = ' + spacegroup1 )
print('Unit Cell Spacegroup (t(n=' + str(tc2) +'))  = ' + spacegroup2 )
print('Shifted Positions of Atoms 9 and 10 at t(n=' + str(tc1) +') ...')
print(positions1)
print('Shifted Positions of Atoms 9 and 10 at t(n=' + str(tc2) +') ...')
print(positions2)
