import numpy as np
import matplotlib.pyplot as plt

filepath = 'Osi_p3'

load = np.zeros(500)
vert = np.zeros(500)
cnt = 0
with open(filepath) as fp:
  l = fp.readline()
  while l:
    ll = l.split()
    if len(ll)>0:
      if ll[0] == 'Pr.Sum':
        load[cnt]= np.abs(float(ll[3]))
#        vert[cnt]= float(ll[2])
        cnt +=1
    l = fp.readline()


plt.ion()
fig,ax = plt.subplots()
ax.plot(np.arange(cnt),load[0:cnt],label='Normal Stress Reaction, (33)')
#ax.plot(np.arange(cnt),vert[0:cnt],label='normal')
#ax.yaxis.set_major_locator(plt.MaxNLocator(10))
ax.legend()
fig.show()
