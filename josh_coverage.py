import numpy as np 
import matplotlib.pyplot as plt 
import scipy.interpolate 
from matplotlib.colors import LogNorm
import sys
N = 1000 #number of points for plotting/interpolation 
fig= plt.figure(figsize=(6,5))
left, buttom, width, height =0.1, 0.1, 0.8, 0.8
ax=fig.add_axes([left, buttom, width, height])

w, x, y, z = np.genfromtxt(r'CO_t.txt', unpack=True) 
#x=np.log10(x)
all_voltages=[]

for ww in w:
    if len(all_voltages)==0:
        all_voltages.append(ww)
        continue
    if any([abs(ww-v)<1e-3 for v in all_voltages]):
        continue
    all_voltages.append(ww)
 #   print('current',ww,all_voltages)
all_voltages=[round(v,4) for v in all_voltages]
lvoltages=len(all_voltages)
#all_voltages=sorted(list(set(list(w))))


inx=all_voltages.index(-2.0)
New=[]
for i,a in enumerate(w):
    if (i-inx)%(len(all_voltages))==0:
#        print(i)
        New.append(i)
print(New)
#sys.exit()
#x=np.array(sorted(list(set(x[New]))))
#y=np.array(sorted(list(set(y[New]))))
#z=z[New]
#w=np.log10(w)
#x=np.log10(x)

x=[]
y=[]
z=[]
for line in open('CO_t.txt','r'):
    ls=line.split()
    if ls[0]=='-2.0':
        x.append(float(ls[1]))
        y.append(float(ls[2]))
        z.append(float(ls[3]))
x=np.array(x)
y=np.array(y)
z=np.array(z)
print(x[:10])
print(y[:10])
print(z[:10])

z=np.log10(z)

wi = np.linspace(w.min(), w.max(), N) 
xi = np.linspace(x.min(), x.max(), N) 
yi = np.linspace(y.min(), y.max(), N) 

zi = scipy.interpolate.griddata((x, y), z, (xi[None,:], yi[:,None]), method='linear')

X,Y =np.meshgrid(xi, yi)
#axim = ax.imshow(Z, norm = LogNorm())
#axim   = ax.contourf(X,Y,Z,levels=[1e-3,1e-2,1e-1,1e0],cmap=plt.cm.jet,norm =LogNorm())

axim= ax.contourf(X,Y,zi,100,cmap='viridis') #,norm = LogNorm())
ax.scatter(x,y, color='red')
#y=np.log10(y)
cb= fig.colorbar(axim)
ax.set_title('Contour plot of CO_g.txt at -2V')
ax.set_xlabel('Pressure(atm)')
ax.set_ylabel('pH(unit)')
plt.show() 

