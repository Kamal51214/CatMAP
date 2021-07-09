# importing the required module
import catmap
import numpy as np
from catmap.model import ReactionModel
from catmap.analyze import VectorMap
log_file='catmap_CO2R_template.log'
model = ReactionModel(setup_file=log_file)
import pylab as plt


labels = model.output_labels['rate']
xc= [float(a[0][0]) for a in model.turnover_frequency_map]
yc = [float(a[1][2]) for a in model.turnover_frequency_map]

x=[i+0.059*13 for i in xc]

e=1.602e-19

asd=0.169061707523246#0.002505965914042128 #sites/sqAng
asd*=(1./100.**2*1e10**2)# sites/sqcm
asd*=e #C/sqcm
asd*=1000. #mC/sqcm
asd*=2 #multiply by number of electrons, divide by number of CO2
#y3=[i*2.505965914042128173e-19*12*1000*154.623397436e-16 for i in yc]
y3=[i*asd for i in yc]
y=np.log10(y3)

plt.xlim([-1.2,-0.0])
plt.ylim([-4,2])

# plotting the points
plt.plot(x,y)
#naming the axis
plt.xlabel('Voltage vs RHE(V)')
# naming the y axis
plt.ylabel('Current density log(j(mA/cm2)')
# giving a title to my graph
plt.title('Simulated polarization curves for CO2_g coverage at pH=13, Partial pressure=0.035')
# function to show the plot
plt.show()
