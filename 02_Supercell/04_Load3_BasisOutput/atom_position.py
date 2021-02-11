import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D
import spglib as spg

# history and output file definition for parsing
outfile = 'Osi'
hisfile1 = "Psia.his"
hisfile2 = "Psib.his"
hisfile3 = "Psic.his"
nsteps=414
natoms=15
atomposlinear1 = []
atomposlinear2 = []
atomposlinear3 = []
time = []
atomposall = []
rlxbasis = np.zeros((3,natoms))
# construct list of dimension N X (3*nbasis) which contains concatenated history file data
with open(hisfile1) as openfile1, open(hisfile2) as openfile2, open(hisfile3) as openfile3:
  line1 = openfile1.readline()
  line2 = openfile2.readline()
  line3 = openfile3.readline()

  n=0
  while line1 and line2 and line3:
    splitline1 = line1.split()
    splitline2 = line2.split()
    splitline3 = line3.split()

    if len(splitline1)>0:
      time.append(splitline1[0])
      splitline1.pop(0)
    if len(splitline2)>0:
      splitline2.pop(0)
    if len(splitline3)>0:
      splitline3.pop(0)
    total_line=splitline1+splitline2+splitline3
    atomposall.append(total_line)
    n+=1
    line1=openfile1.readline()
    line2=openfile2.readline()
    line3=openfile3.readline()

# Loop over the atomposall to parse out the 3 components per basis vector per atom
dispvec1 = np.zeros((natoms,len(atomposall)))
dispvec2 = np.zeros((natoms,len(atomposall)))
dispvec3 = np.zeros((natoms,len(atomposall)))
for n in np.arange(len(atomposall)): # loop over number of timesteps
  for r in np.arange(natoms): # loop over over number of atoms in the supercell
    dispvec1[r][n] = atomposall[n][3*r]
    dispvec2[r][n] = atomposall[n][3*r+1]
    dispvec3[r][n] = atomposall[n][3*r+2]

# Get the relaxed basis from the output file
cnt=0
with open(outfile) as fp:
  l = fp.readline()
  while l:
    ll = l.split()
    if len(ll)>0:
      if ll[0] == 'Relaxed':
        rlxbasis[0][cnt]=np.abs(float(ll[2]))
        rlxbasis[1][cnt]=np.abs(float(ll[3]))
        rlxbasis[2][cnt]=np.abs(float(ll[4]))
        cnt +=1
    l = fp.readline()
# CHECKED Monday December 21: relaxed basis output is correct


#debug
#print(rlxbasis)
print('Dispvec1....')
print(dispvec1)
print('len(dispvec1)...')
print(len(dispvec1))
print('len(dispvec1[0])...')
print(len(dispvec1[0]))
print('Dispvec2....')
print(dispvec2)
print('len(dispvec2)...')
print(len(dispvec2))
print('len(dispvec2[0])...')
print(len(dispvec2[0]))
print('Dispvec3....')
print(dispvec3)
print('len(dispvec3)...')
print(len(dispvec3))
print('len(dispvec3[0])...')
print(len(dispvec3[0]))


timearr = np.array(time)
time = timearr.astype(np.float)
time = time/2;

# plot the components over time for each atom
nrows=3
ncols=5
fig, ax = plt.subplots(nrows, ncols)
print('Plotting...')
p = 0
for i in np.arange(nrows):
  for j in np.arange(ncols):
    '''
    if p == 0:
      a_pos_time_1 = np.zeros(len(time))
      a_pos_time_2 = np.zeros(len(time))
      a_pos_time_3 = np.zeros(len(time))
    else:
      a_pos_time_1 = rlxbasis[0][p]+dispvec1[p][:]
      a_pos_time_2 = rlxbasis[1][p]+dispvec2[p][:]
      a_pos_time_3 = rlxbasis[2][p]+dispvec3[p][:]
    '''

    a_pos_time_1 = rlxbasis[0][p]+dispvec1[p][:]
    a_pos_time_2 = rlxbasis[1][p]+dispvec2[p][:]
    a_pos_time_3 = rlxbasis[2][p]+dispvec3[p][:]
    # debug

    print(30*'***')
    print('p = ...')
    print(p)
    print('a_pos_time_1 = ....')
    print(a_pos_time_1)
    print('a_pos_time_2 = ....')
    print(a_pos_time_2)
    print('a_pos_time_3 = ....')
    print(a_pos_time_3)
    print('dispvec1 = ....')
    print(dispvec1)
    print('dispvec2 = ....')
    print(dispvec2)
    print('dispvec3 = ....')
    print(dispvec3)
    ax[i][j].plot(time, a_pos_time_1, marker='1', markevery=30,markersize=10)
    ax[i][j].plot(time, a_pos_time_2, marker='2', markevery=30,markersize=10)
    ax[i][j].plot(time, a_pos_time_3, marker='3', markevery=30,markersize=10)
    ax[i][j].set_xlabel('Time')
    ax[i][j].set_ylabel('Position Component')
    ax[i][j].set_title('Atom '+str(p+1), loc='right')
    ax[i][j].grid(True)
    ax[i][j].legend()
    p += 1



fig.subplots_adjust(hspace=.5)
fig.suptitle('Position Vector Components of Atoms in Supercell (No Vacancies)')
fig.legend(['1 Component of Position', '2 Component of Position','3 Component of Position'], loc='upper right')
fig.set_size_inches(20,10)
fig.savefig('figures/Atom_Positions_Supercell_NoVacancy', dpi=100)
fig.show()

# plot the location of atoms in the basis over time -----------------
atom_fig=plt.figure()
I=2
J=2
K=2
n=2
m=0
print('Plotting position of atoms in R^3....')

a_pos_atoms_time = np.zeros(((natoms,len(time),3)))
for t in np.arange(len(dispvec1[0])):
  for atom in np.arange(len(dispvec1)):
    print('t='+str(t))
    print('atom='+str(atom))
    a_pos_time_1 = rlxbasis[0][atom]+dispvec1[atom][t]
    a_pos_time_2 = rlxbasis[1][atom]+dispvec2[atom][t]
    a_pos_time_3 = rlxbasis[2][atom]+dispvec3[atom][t]
    a_pos_atoms_time[atom][t][:] = np.array([a_pos_time_1, a_pos_time_2, a_pos_time_3])

R = np.zeros(((len(timearr),natoms,3)))
for t in np.arange(len(dispvec1[0])):
  atom_ax = plt.axes(projection='3d')
  for atom in np.arange(len(dispvec1)):
    a_pos_time_1 = rlxbasis[0][atom]+dispvec1[atom][t]
    a_pos_time_2 = rlxbasis[1][atom]+dispvec2[atom][t]
    a_pos_time_3 = rlxbasis[2][atom]+dispvec3[atom][t]
    print(30*'---*')
    print('atom='+str(atom))
    print('t='+str(t))
    print(a_pos_time_1)
    print(a_pos_time_2)
    print(a_pos_time_3)
    R[t][atom][:] = np.array([a_pos_time_1, a_pos_time_2, a_pos_time_3])
    atom_ax.scatter3D(a_pos_time_1, a_pos_time_2, a_pos_time_3,c='red')
    atom_ax.set_xlabel('X')
    atom_ax.set_ylabel('Y')
    atom_ax.set_zlabel('Z')
    atom_ax.grid(True)
    '''
    # draw lines for lattice shape
    for i in np.arange(I):
      for j in np.arange(J):
        for k in np.arange(K):
          for p in np.arange(n):
            m = m+1
            print('m='+str(m))
          x = a_pos_atoms_time[(m-1):(m)][t][0]
          y = a_pos_atoms_time[(m-1):(m)][t][1]
          z = a_pos_atoms_time[(m-1):(m)][t][2]
          print('x=.....')
          print(x)
          print('y=.....')
          print(y)
          print('z=.....')
          print(z)
          atom_ax.plot(x, y, z, color='k');
          '''

    atom_ax.set_xlabel('X')
    atom_ax.set_ylabel('Y')
    atom_ax.set_zlabel('Z')
    atom_ax.grid(True)
    atom_fig.savefig('figures/atoms_in_R3_over_time/atoms_tstep='+str(t))
    plt.close('all')

# save output variable R for later use
np.save('R_out',R)
