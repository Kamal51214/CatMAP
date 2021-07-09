from catmap import ReactionModel
from catmap import analyze

mkm_file = 'catmap_CO2R_template.log'

model = ReactionModel(setup_file=mkm_file)

tof=model.turnover_frequency_map

names=model.output_labels['turnover_frequency']




