#run with
#python contour_v2.py  CO2R_kamal

from units import *
import re
from get_data import get_data
from glob import glob
from string import Template
from catmap.model import ReactionModel
import matplotlib.pyplot as plt
import numpy as np
from matplotlib import cm
import mpl_toolkits.mplot3d.axes3d as p3
import sys
import os

property='tof' #tof or coverage

#############
#PARAMETERS
#############
### this should be in principle coded, but i put it here as "hard-coded" in the limit of time
nprod_dict={'CH3CH2OH_g':1,'CH4_g':1,'CO_g':1,'H2_g':1} #stoichiometric factor of products
nel_dict={'CH3CH2OH_g':12,'CH4_g':8,'CO_g':2,'H2_g':2} #stoichiometric factor of electrons
###
active_site_density=1
#############

def cleanup():
    files=glob('*.pkl')+glob('*.log')
    for f in files:
        os.remove(f)

mkm_file=sys.argv[1]

fig=plt.figure()
ax=fig.add_subplot(111)

x = np.logspace(-5,1,20)
y = np.linspace(7,14,20)


###create mkm file from template
mkm_template = Template(open('catmap_'+sys.argv[1]+'_template.mkm').read())

mkm_text = mkm_template.substitute(pH_new = 14)
mkm_file = 'catmap_'+sys.argv[1]+'.mkm'
with open(mkm_file,'w') as f:
    f.write(mkm_text)
model = ReactionModel(setup_file = mkm_file,max_log_line_length=0)   
model.output_variables+=['production_rate', 'free_energy', 'selectivity', 'interacting_energy','coverage','rate_control','consumption_rate','turnover_frequency']
###

###cleanup old txt files
for f in ['H2_g.txt','CO_g.txt','CH3CH2OH_g.txt','CH4_g.txt']:
    if os.path.exists(f):
        os.remove(f)
###

for i,xx in enumerate(x):
    for j,yy in enumerate(y):
#        if i==0 and not yy>11.421052631578947:
#            continue
        ###cleanup and run model with the current parameters
        cleanup()
        model = ReactionModel(setup_file = mkm_file,max_log_line_length=0)   
        model.output_variables+=['production_rate', 'free_energy', 'selectivity', 'interacting_energy','coverage','rate_control','consumption_rate','turnover_frequency']
        model.species_definitions['CO2_g']['pressure']=xx
        model.pH=yy
        print('running',xx,yy)
        model.run()
        print('finished run')
        ###
        log_file='catmap_'+sys.argv[1]+'.log'
        pickle_file='catmap_'+sys.argv[1]+'.pkl'
        print('log file = ',log_file)
        model_after_run = ReactionModel(setup_file = log_file)
        data = get_data(pickle_file,model_after_run)
        for prod in data.turnover_frequency_names:
            if prod in ['CO2_g','H2O_g','OH_g','ele_g']:
                continue
            with open(prod+'.txt','a') as of:
                idx=data.turnover_frequency_names.index(prod)
                tof=data.turnover_frequency[:,idx]
                data_ref=np.column_stack((data.voltage, tof))
                voltages=data_ref[np.argsort(data_ref[:, 0])][:,0]
                nprod=nprod_dict[prod]
                nel=nel_dict[prod]
                rates=data_ref[np.argsort(data_ref[:, 0])][:,1]#*active_site_density
                #current_densities=rates*nel*unit_F/nprod #current density in [A/m^2]
                current_densities=rates
                #current_densities/=10. #convert A/m^2 to mA/cm^2
                for ii in range(len(current_densities)):
                    current_density=current_densities[ii] #select which of the voltages you want to plot
                    if prod=='CH3CH2OH_g':
                        print('current {}'.format(current_density))
                    of.write('{} {} {} {}\n'.format(voltages[ii],np.log10(xx),yy,current_density))

