import pandas as pd
import constants
import numpy as np
from pgmpy.models import BayesianNetwork

from pybnesian import GaussianNetwork

def decodeDataset(df):
    newData = df

    for key, values in constants.BAYES_NETWORK_STATE_NAMES.items():
        if key in newData:
            column = newData[key]
            newData[key] = column.apply(lambda x: values.index(x))

    #print(newData.head())
    #print(newData.dtypes)
    #newData.info()
    newData = newData.astype(np.float32)
    #newData['Desenlace'] = newData['Desenlace'].apply(lambda x: constants.BAYES_NETWORK_STATE_NAMES['Desenlace'][x])
    #print(newData.dtypes)
    #newData.info()
    #print(newData.head())
    return newData

def decodeAgeColumn(age):
    if age < 12:
        return 'MENOR DE 12'
    elif age > 21:
        return 'MAYOR DE 21'
    else:
        return str(age)

def decodeHeightColumn(height):
    if height <= 149:
        return "MENOS DE 149"
    elif height >= 150 or height < 160:
        return "150-159"
    elif height >= 160 or height < 170:
        return "160-169"
    elif height >= 170 or height < 180:
        return "170-179"
    elif height >= 180 or height < 190:
        return "180-189"
    elif height >= 190:
        return "MAS DE 190"
    else:
        return False

def decodeWeightColumn(weight):
    if weight <= 49:
        return "MENOS DE 49"
    elif weight >= 50 or weight < 60:
        return "50-59"
    elif weight >= 60 or weight < 70:
        return "60-69"
    elif weight >= 70 or weight < 80:
        return "70-79"
    elif weight >= 80 or weight < 90:
        return "80-89"
    elif weight >= 90:
        return "MAS DE 90"
    else:
        return False

def decodeMonthlyFamiliarIncome(income):
    if income <= 499:
        return "MENOS DE 499"
    elif income >= 500 or income < 1000:
        return "500-999"
    elif income >= 1000 or income < 1500:
        return "1000-1499"
    elif income >= 1500 or income < 2000:
        return "1500-1999"
    elif income >= 2000 or income < 2500:
        return "2000-2499"
    elif income >= 2500:
        return "MAS DE 2500"
    else:
        return False

modelType = 'autoinforme'

df = pd.read_csv('datasets/' + modelType + '/dataset1.csv')

newData = df
# Modificamos el df para obtener el dataframe que queremos
newData.drop(['Index', 'Nombre'], axis=1, inplace=True)

ageColumn = newData['Edad']
heightColumn = newData['Altura']
weightColumn = newData['Peso']

newData['Edad'] = ageColumn.apply(decodeAgeColumn).astype(object)
newData['Altura'] = heightColumn.apply(decodeHeightColumn).astype(object)
newData['Peso'] = weightColumn.apply(decodeWeightColumn).astype(object)

if 'Ingreso familiar mensual' in newData:
    col = newData['Ingreso familiar mensual']
    newData['Ingreso familiar mensual'] = col.apply(decodeMonthlyFamiliarIncome).astype(object)


newData = newData.apply(lambda x: x.astype(str).str.upper())

df = decodeDataset(newData)

numRows = round(constants.TRAINING_PERCENTAGE_DATASET * len(df))
numRowsTrain = numRows - 1

trainingDF = df[:numRowsTrain]
testDF = df[numRows:]
predictData = testDF.drop('Desenlace', axis=1)


# CREAMOS LA RED DE BAYES GAUSIANA
model = GaussianNetwork(constants.BAYES_NETWORK_VARIABLES_AUTOINFORME,
                        constants.BAYES_NETWORK_EDGES_AUTOINFORME)

#for arc in constants.BAYES_NETWORK_EDGES_AUTOINFORME:
    #model.add_arc(arc[0], arc[1])
print(model.num_nodes())
print(model.fitted())
model.fit(trainingDF)
print(model.fitted())
print(model.cpd('Desenlace'))
print(model.cpd('Edad'))
print(model.cpd('Sexo asignado'))
print(model.cpd('Transgenero'))

model.save('pybnesianFile', include_cpd=True)

sample = model.sample(50)

print(sample)
ll = model.logl(sample)
print(ll)
print(ll.sum())
sll = model.slogl(sample)
print(sll)
print(np.isclose(ll.sum(), sll))
# Predecir valores
'''
predicted_data = model.predict(predictData)

print(predicted_data)
'''
# INTENTO DE COMBINACION CON PGMPY. NO FUNCIONA
'''
newModel = BayesianNetwork.load('pybnesianFile.pickle', filetype='pickle')
print(newModel.get_cpds())
'''