import sys
import pandas as pd
import analyze_mosquito_data_lib as mosquito_lib 


filename = sys.argv[1]

print 'analyze data', filename

#read the data
data = pd.read_csv(filename)

#convert temperature to celsius
data['temperature']=mosquito_lib.fahr_to_celsius(data['temperature'])

#analyze data
parameters = mosquito_lib.analyze(data,filename.replace('csv','png'))

#save parameters to file
parameters.to_csv(filename.replace('data','parameters'))

print parameters

