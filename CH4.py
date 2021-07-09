
import numpy as np 
import matplotlib.pyplot as plt 
import scipy.interpolate 
from matplotlib.colors import LogNorm

N = 1000 #number of points for plotting/interpolation 
fig= plt.figure(figsize=(6,5))
left, buttom, width, height =0.1, 0.1, 0.8, 0.8
ax=fig.add_axes([left, buttom, width, height])

x, y, z = np.genfromtxt(r'CH4_g.txt', unpack=True) 

x=np.log10(x)
z=np.log10(z)

xi = np.linspace(x.min(), x.max(), N) 
yi = np.linspace(y.min(), y.max(), N) 
zi = scipy.interpolate.griddata((x, y), z, (xi[None,:], yi[:,None]), method='linear')

X,Y =np.meshgrid(xi, yi)
#axim = ax.imshow(Z, norm = LogNorm())
#axim   = ax.contourf(X,Y,Z,levels=[1e-3,1e-2,1e-1,1e0],cmap=plt.cm.jet,norm =LogNorm())

axim= ax.contourf(X,Y,zi,100,cmap='viridis') #,norm = LogNorm())
ax.scatter(x,y, color='red')

cb= fig.colorbar(axim)

ax.set_title('Contour plot of CH4_g.txt at -1V')
ax.set_xlabel('Pressure(atm')
ax.set_ylabel('pH(unit)')
plt.show() 


