from catmap import ReactionModel
from catmap import analyze

mkm_file = 'catmap_CO2R_template.log'
model = ReactionModel(setup_file=mkm_file)
vm = analyze.VectorMap(model)
vm.plot_variable='turnover_frequency'
vm.log_scale=True
vm.min=1e-20
vm.max=1e10
vm.plot(save='production_rate.png')



