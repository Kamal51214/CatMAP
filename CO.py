
import numpy as np 
import matplotlib.pyplot as plt 
import scipy.interpolate 

N = 1000 #number of points for plotting/interpolation 
fig= plt.figure(figsize=(6,5))
left, buttom, width, height =0.1, 0.1, 0.8, 0.8
ax=fig.add_axes([left, buttom, width, height])

x, y, z = np.genfromtxt(r'CO_g.txt', unpack=True) 
xi = np.linspace(x.min(), x.max(), N) 
yi = np.linspace(y.min(), y.max(), N) 
zi = scipy.interpolate.griddata((x, y), z, (xi[None,:], yi[:,None]), method='linear') 


X,Y =np.meshgrid(xi, yi)
cp= plt.contourf(X,Y,zi)
plt.colorbar(cp,ax=ax)
fig=plt.figure()
ax.scatter(x,y, color='red')
ax.set_xscale('log')

ax.set_title('Contour plot of CO_g.txt at -1V')
ax.set_xlabel('Pressure(atm')
ax.set_ylabel('pH(unit)')
plt.show() 

