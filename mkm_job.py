
from catmap import ReactionModel
 
mkm_file = 'catmap_CO2R_template.mkm'
model = ReactionModel(setup_file=mkm_file)
model.output_variables+= ['turnover_frequency']
model.run()
from catmap import analyze
vm = analyze.VectorMap(model)
vm.plot_variable = 'rate' #tell the model which output to plot
vm.log_scale = True #rates should be plotted on a log-scale
vm.min = 1e-25 #minimum rate to plot
vm.max = 1e3 #maximum rate to plot

vm.plot(save='rate.png') #draw the plot and save it as "rate.pdf"
vm.descriptor_labels = ['voltage', 'temperature', ]
vm.threshold = 1e-25 #anything below this is considered to be 0
vm.subplots_adjust_kwargs = {'left':0.2,'right':0.8,'bottom':0.15}
vm.plot(save='pretty_production_rate.pdf')
ma = analyze.MechanismAnalysis(model)
ma.energy_type = 'free_energy' #can also be free_energy/potential_energy
ma.include_labels = False #way too messy with labels
ma.pressure_correction = False #assume all pressures are 1 bar (so that energies are the same as from DFT)
ma.include_labels = True
fig = ma.plot(plot_variants=['Pt'], save='FED.png')
print(ma.data_dict)  # contains [energies, barriers] for each rxn_mechanism defined
model.model_summary()  # generate a LaTeX summary of the model.  Useful for quick debugging.
