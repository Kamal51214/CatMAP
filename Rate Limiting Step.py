
from catmap import ReactionModel
from catmap import analyze
mkm_file='catmap_CO2R_template.mkm'
model = ReactionModel(setup_file=mkm_file)
model.output_variables += ['rate_control']
model.run()
mm = analyze.MatrixMap(model)
mm.plot_variable = 'rate_control'
mm.log_scale = False
mm.min = -2
mm.max = 2
mm.plot(save='rate_control.pdf')


