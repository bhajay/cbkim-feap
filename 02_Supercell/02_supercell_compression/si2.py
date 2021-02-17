import numpy as np
import matplotlib.pyplot as plt
from matplotlib.pyplot import figure

filepath = 'Osi_p2'

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
cnt_marker=int(round(cnt/8))
A=1;
delta_stress33 = (load[cnt_marker]-load[0])/A
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
ax1.grid(True)
ax2.grid(True)
fig.set_size_inches(10,5)
fig.suptitle('Supercell Stress Strain Curve (No Vacancy)')

fig.savefig('figures/SS_Supercell_NoVacancy.png', dpi=100)
fig.show()
