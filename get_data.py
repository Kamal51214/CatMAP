import numpy as np
import pickle

class Object(object):
    pass

def get_data(pickle_file,model):
    a = pickle.load(open(pickle_file,'rb'))
    data = Object()
    #COVERAGES
    data.coverage_names = model.output_labels['coverage']
    coverage_map = np.array(a['coverage_map'])
    data.voltage = []
    scaler_array = coverage_map[:,0]
    for s in scaler_array:
        data.voltage.append(s[0])
    coverage_mpf = coverage_map[:,1]
    data.coverage = np.zeros((len(coverage_mpf),len(data.coverage_names)))    
    for i in range(0,len(coverage_mpf)):
        for j in range(0,len(coverage_mpf[i])):
            float_rate = float(coverage_mpf[i][j])
            data.coverage[i][j]=float_rate
    #PRODUCT NAMES
    data.prod_names = model.output_labels['production_rate']
    data.cons_names = model.output_labels['consumption_rate']
    data.turnover_frequency_names = model.output_labels['turnover_frequency']
    data.rate_control_names=model.output_labels['rate_control']

    production_rate_map = np.array(a['production_rate_map'])
    consumption_rate_map = np.array(a['consumption_rate_map'])
    turnover_frequency_map = np.array(a['turnover_frequency_map'])
    rate_control_map=np.array(a['rate_control_map'])

    production_rate_mpf = production_rate_map[:,1]
    consumption_rate_mpf = consumption_rate_map[:,1]
    turnover_frequency_mpf = turnover_frequency_map[:,1]
    rate_control_mpf = rate_control_map[:,1]

    data.production_rate = np.zeros((len(production_rate_mpf),len(data.prod_names)))
    data.consumption_rate = np.zeros((len(consumption_rate_mpf),len(data.cons_names)))
    data.turnover_frequency = np.zeros((len(turnover_frequency_mpf),len(data.turnover_frequency_names)))
    data.rate_control = np.zeros((len(rate_control_mpf),len(data.rate_control_names[0]),len(data.rate_control_names[1])))

    data.voltage = np.zeros((len(production_rate_mpf),1))
    for i in range(0,len(production_rate_mpf)):
        data.voltage[i][0] = production_rate_map[:,0][i][0]
        for j in range(0,len(data.prod_names)):
            float_rate = float(production_rate_mpf[i][j])
            data.production_rate[i][j]=float_rate
    for i in range(0,len(consumption_rate_mpf)):
        for j in range(0,len(data.cons_names)):
            float_rate = float(consumption_rate_mpf[i][j])
            data.consumption_rate[i][j]=float_rate
            float_rate = float(turnover_frequency_mpf[i][j])
            data.turnover_frequency[i][j]=float_rate
    for i in range(0,len(turnover_frequency_mpf)):
        for j in range(0,len(data.turnover_frequency_names)):
            B
            float_rate = float(turnover_frequency_mpf[i][j])
            data.turnover_frequency[i][j]=float_rate
    #rate control is
        #2nd index: products
        #3rd index: controlling states
    for i in range(0,len(rate_control_mpf)):
        for j in range(0,len(data.rate_control_names[0])):
            for k in range(0,len(data.rate_control_names[1])):
                rate_control = float(rate_control_mpf[i][j][k])
                data.rate_control[i][j][k]=rate_control

    #RATES
    data.rate_names = model.output_labels['rate']
    rate_map = np.array(a['rate_map'])
    rate_mpf = rate_map[:,1]
    data.rate = np.zeros((len(rate_mpf),len(data.rate_names)))
    for i in range(0,len(rate_mpf)):
        for j in range(0,len(rate_mpf[i])):
            float_rate = float(rate_mpf[i][j])
            data.rate[i][j]=float_rate
    return data
