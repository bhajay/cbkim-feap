import numpy as np
import matplotlib.pyplot as plt
from matplotlib.pyplot import figure

filepath = 'Osi_p3'

load = np.zeros(500)
stress33 = np.zeros(500)
strain33 = np.zeros(500)

del_eps = -0.0004831 # incremental strain applied per time step (per cnt)

cnt = 0
with open(filepath) as fp:
  l = fp.readline()
  while l:
    ll = l.split()
    if len(ll)>0:
      if ll[0] == 'Pr.Sum':
        load[cnt]= np.abs(float(ll[3]))
        strain33[cnt]=np.abs(cnt*del_eps)
        cnt +=1
    l = fp.readline()

# compute elastic modulus, for delta_strain=0.05
cnt_marker=int(round(cnt/4))
delta_stress33 = load[cnt_marker]-load[0]
delta_strain33 = strain33[cnt_marker]-strain33[0]
Emod = delta_stress33/delta_strain33/10**9 # GPa

plt.ion()
fig,(ax1,ax2) = plt.subplots(nrows=1,ncols=2)
ax1.plot(np.arange(cnt),load[0:cnt],label='Normal Reaction, (33)')
ax2.plot(strain33[0:cnt],load[0:cnt],label='Stress, (33)')
ax2.plot([strain33[0],strain33[cnt_marker]],[load[0],load[cnt_marker]],'-ok',label='Elastic Modulus Approx')

ax1.set_xlabel('Time Step (count)')
ax1.set_ylabel('Normal Reaction (33)')
ax2.set_xlabel('Strain')
ax2.set_ylabel('Stress, (33)')
Emod = format(Emod, '.5f')
anno_text = 'E= ' + Emod  + ' GPa'
ax2.text(0.5, 0.5, anno_text, horizontalalignment='center', verticalalignment='center', transform=ax2.transAxes)
ax1.legend()
ax2.legend()
fig.set_size_inches(10,5)
fig.savefig('figures/Super_cell_Vacancy_SS_Emod.png', dpi=100)
fig.show()


# load in history variables for the lattice basis vectors

histfiles = ["Psi_p3a.his", "Psi_p3b.his", "Psi_p3c.his"] 

hn = np.zeros((3,500))
h1 = np.zeros((3,500))

fk=0
for filename in histfiles: 
  cnt=0
  with open(filename) as fp:
    l = fp.readline()
    while l:
      ll = l.split()
      if len(ll)>0:
        hn[fk][cnt] = float(ll[0])
        h1[fk][cnt] = float(ll[1])
        cnt+=1
      l=fp.readline()
  fk+=1


plt.ion()
fig2, (axha,axhb,axhc) = plt.subplots(nrows=1,ncols=3)
axha.plot(np.arange(cnt),hn[0][0:cnt],label='History Variable, hn, A component')
axhb.plot(np.arange(cnt),hn[1][0:cnt],label='History Variable, hn, B component')
axhc.plot(np.arange(cnt),hn[2][0:cnt],label='History Variable, hn, C component')

axha.set_xlabel('Time Step (Count)')
axha.set_ylabel('Hist Variable, hn, A component')
axhb.set_xlabel('Time Step (Count)')
axhb.set_ylabel('Hist Variable, hn, B component')
axhc.set_xlabel('Time Step (Count)')
axhc.set_ylabel('Hist Variable, hn, C component')


fig2.set_size_inches(15,5)
axha.grid(True)
axhb.grid(True)
axhc.grid(True)

fig2.savefig('figures/HistVar_hn_ABC.png', dpi=100)



fig3, (axh1a,axh1b,axh1c) = plt.subplots(nrows=1,ncols=3)
axh1a.plot(np.arange(cnt),h1[0][0:cnt],label='History Variable, h1, A component')
axh1b.plot(np.arange(cnt),h1[1][0:cnt],label='History Variable, h1, B component')
axh1c.plot(np.arange(cnt),h1[2][0:cnt],label='History Variable, h1, C component')

axh1a.set_xlabel('Time Step (Count)')
axh1a.set_ylabel('Hist Variable, h1, A component')
axh1b.set_xlabel('Time Step (Count)')
axh1b.set_ylabel('Hist Variable, h1, B component')
axh1c.set_xlabel('Time Step (Count)')
axh1c.set_ylabel('Hist Variable, h1, C component')

fig3.set_size_inches(15,5)
fig3.savefig('figures/HistVar_h1_ABC', dpi=100)
fig3.suptitle('Supercell Stress Strain Curve (Atom 15 Vacancy)')

axh1a.grid(True)
axh1b.grid(True)
axh1c.grid(True)
