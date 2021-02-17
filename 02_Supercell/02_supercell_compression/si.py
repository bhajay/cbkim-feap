import numpy as np
import matplotlib.pyplot as plt

filepath = 'Osi_p2'

load = np.zeros(500)
stress33 = np.zeros(500)
strain = np.zeros(500)

del_eps = -0.0004831 # incremental strain applied per time step (per cnt)

cnt = 0
with open(filepath) as fp:
  l = fp.readline()
  while l:
    ll = l.split()
    if len(ll)>0:
      if ll[0] == 'Pr.Sum':
        load[cnt]= np.abs(float(ll[3]))
        strain[cnt]=np.abs(cnt*del_eps)
        #stress33[cnt]=
        cnt +=1

	strain[cnt]=np.abs(cnt*del_eps)
    l = fp.readline()


plt.ion()
fig,ax = plt.subplots()
ax.plot(np.arange(cnt),load[0:cnt],label='Normal Reaction, (33)')
#ax.plot(np.arange(cnt),vert[0:cnt],label='normal')
#ax.yaxis.set_major_locator(plt.MaxNLocator(10))
ax.legend()
fig.show()
