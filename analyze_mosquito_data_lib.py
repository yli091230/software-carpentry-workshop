import pandas as pd
import statsmodels.api as sm
import matplotlib.pyplot as plt

def fahr_to_celsius(temperature_fahr):
    '''convert fahreheit to celsius'''
    temperature_celsus = (temperature_fahr-35)*5/9
    return temperature_celsus

def analyze(data):
    '''Perform nalysis on mosquoto data
    
    data is a Dataframe with column 'temperature',
    'rainfall' and 'mosquito'.
    
    Performs a least squares regression, plots the results and returns the
    fit parameters'''
    
    assert data['temperature'].max()< 70,'check that input temperature is celsius'
    regr_results = sm.OLS.from_formula('mosquitos ~ temperature + rainfall', data).fit()
    parameters = regr_results.params
    rsquared = regr_results.rsquared
    predicted = parameters[0] + parameters[1] * data['temperature'] + parameters[2] * data['rainfall']
    plt.plot(predicted, data['mosquitos'], 'ro')
    min_mosquitos, max_mosquitos = min(data['mosquitos']), max(data['mosquitos'])
    plt.plot([min_mosquitos, max_mosquitos], [min_mosquitos, max_mosquitos], 'k-')
    plt.show()
    return parameters   