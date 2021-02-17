import numpy as np
import matplotlib.pyplot as plt

outfile = 'Osi_p3'
hisfiles = ['Psi_p3a.his', 'Psi_p3b.his', 'Psi_p3c.his']
nbasis=14
rlxbasis = np.zeros((3,nbasis))
disp = np.zeros(((500,3,nbasis)))
time = np.zeros(500)

# extract the relaxed basis from output file
cnt = 0
with open(outfile) as fp:
  l = fp.readline()
  print("Getting relaxed basis from output file ...")
  while l:
    print("Splitting lines ...")
    ll = l.split()
    if len(ll)>0:
      if ll[0] == 'Relaxed':
        rlxbasis[0][cnt] = np.abs(float(ll[2]))
        rlxbasis[1][cnt] = np.abs(float(ll[3]))
        rlxbasis[2][cnt] = np.abs(float(ll[4]))
        cnt +=1
    l = fp.readline()

# combine the history files into 1 history file
cnt=0
with open("Psi_all.his","a+") as newfile:
  newfile.seek(0)
  print("Combining the 3 history files .....")
  data = newfile.read(100)
  if len(data) > 0 :
    newfile.write("\n") 
  for hisfile in hisfiles:
    print("For Looping over hisfiles.....")  
    newline=[]
    with open(hisfile) as fp:
       l = fp.readline()
       while l:
         print("splitting histfiles lines ...")
         ll = l.split()
         if len(ll)>0:
           if cnt == 0:
             newline.append(ll)
           else:
             newline.append(ll[1:len(ll)])
         print(newline)
         l = fp.readline()
    cnt+=1
  
#    newline_list=newline.tolist()
  newline_string_list=[str(value) for value in newline]  
  newfile.write(" ".join(newline_string_list))
  newfile.close() 
 
hisfile="Psi_all.his"

# extract the displacement information over time from history file
cnt=0
with open(hisfile) as fp:
  while l:
    ll = l.split()
    if len(ll)>0:
      time[cnt] = np.abs(float(ll[0]))
    for r in np.arange(nbasis):
      disp[cnt][0][r]=float(ll[3*r+1])
      disp[cnt][1][r]=float(ll[3*r+2])  
      disp[cnt][2][r]=float(ll[3*r+3])  
    cnt +=1
    l = fp.readline() 

# compute the displaced basis vectors over time for each atom
 # maybe later 

# plot the basis vector components over time
# 3 components to a plot
# 1 plot per tom
basis=0
fig, ax = plt.subplots(1,2)
print("Plotting.....")
ax[0].plot(time,rlxbasis[0][basis]+disp[:][0][basis],label='1 Component') 
ax[0].plot(time,rlxbasis[1][basis]+disp[:][1][basis],label='2 Component') 
ax[0].plot(time,rlxbasis[2][basis]+disp[:][2][basis],label='3 Component') 
ax.set_xlabel('Time')
ax.set_ylabel('Basis Vector Component Value') 
fig.show()
fig.savefig("basis_vector"+(basis+1)+".png")
fig.set_size_inches(10,5)
