import pandas as pd
import analyze_mosquito_data_lib as mosquito_lib 

filename = 'A1_mosquito_data.csv'

#read the data
data = pd.read_csv(filename)
print data.head()

#convert temperature to celsius
data['temperature']=mosquito_lib.fahr_to_celsius(data['temperature'])
print data.head()
#analyze data
parameters = mosquito_lib.analyze(data,filename)

#save parameters to file
parameters.to_csv('parameters.csv')

print parameters

