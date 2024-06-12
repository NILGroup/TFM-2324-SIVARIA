import sys
from sklearn.datasets import load_iris
import pandas as pd
import constants
from expertSystem import ExpertSystem
import numpy as np

def main():

    modelType = 'family'

    expertSystem = ExpertSystem()
    expertSystem.buildModel(modelType)

    df = loadDataset(modelType)
    #df.info(verbose=True)
    if df is False:
        raise ValueError('Error loading the dataset\n')
    
    numRows = round(constants.TRAINING_PERCENTAGE_DATASET * len(df))
    numRowsTrain = numRows - 1

    trainingDF = df[:numRowsTrain]
    testDF = df[numRows:]
    predictData = testDF.drop('Desenlace', axis=1)
    
    #print(testDF.dtypes)
    #print(trainingDF.head())
    df.info()
    trainingDF.info()

    expertSystem.trainModel(trainingDF)
    y_pred = expertSystem.predict(predictData)
    print(y_pred)
    
    pass

def loadDataset(type):
    if type != 'autoinforme' and type != 'family' and type != 'professional':
        return False

    filePath = constants.DATASET_BASEPATH + '/' + type + '/dataset1.csv'
    df = pd.read_csv(filePath)

    newDF = None
    if type == 'autoinforme':
        newDF = decodeDataframeAutoinforme(df)
    elif type == 'family':
        newDF = decodeDataframeFamily(df)
    elif type == 'professional':
        newDF = decodeDataframeProfessional(df)
    else:
        return False
    
    #print(newDF['Curso'].head())

    return decodeDataset(newDF)

def decodeDataset(df):
    newData = df

    for key, values in constants.BAYES_NETWORK_STATE_NAMES_2.items():
        if key in newData:
            column = newData[key]
            newData[key] = column.apply(lambda x: values.index(x))

    #print(newData.head())
    #print(newData.dtypes)
    #newData.info()
    newData = newData.astype(np.int8)
    #newData['Desenlace'] = newData['Desenlace'].apply(lambda x: constants.BAYES_NETWORK_STATE_NAMES['Desenlace'][x])
    #print(newData.dtypes)
    #newData.info()
    #print(newData.head())
    return newData

def decodeDataframeAutoinforme(data):
    newData = data

    newData.drop(['Index', 'Nombre'], axis=1, inplace=True)
    
    ageColumn = newData['Edad']
    heightColumn = newData['Altura']
    weightColumn = newData['Peso']

    newData['Edad'] = ageColumn.apply(decodeAgeColumn).astype(object)
    newData['Altura'] = heightColumn.apply(decodeHeightColumn).astype(object)
    newData['Peso'] = weightColumn.apply(decodeWeightColumn).astype(object)

    return newData.apply(lambda x: x.astype(str).str.upper())

def decodeDataframeFamily(data):
    newData = data

    newData.drop(['Index', 'Nombre'], axis=1, inplace=True)

    ageColumn = newData['Edad']
    heightColumn = newData['Altura']
    weightColumn = newData['Peso']

    newData['Edad'] = ageColumn.apply(decodeAgeColumn)
    newData['Altura'] = heightColumn.apply(decodeHeightColumn)
    newData['Peso'] = weightColumn.apply(decodeWeightColumn)

    newData = newData.apply(lambda x: x.astype(str).str.upper())
    return newData.astype(str)

def decodeDataframeProfessional(data):
    newData = data

    newData.drop(['Index', 'Nombre'], axis=1, inplace=True)

    ageColumn = newData['Edad']
    heightColumn = newData['Altura']
    weightColumn = newData['Peso']
    monthlyFamiliarIncomeColumn = newData['Ingreso familiar mensual']

    newData['Edad'] = ageColumn.apply(decodeAgeColumn)
    newData['Altura'] = heightColumn.apply(decodeHeightColumn)
    newData['Peso'] = weightColumn.apply(decodeWeightColumn)
    newData['Ingreso familiar mensual'] = monthlyFamiliarIncomeColumn.apply(decodeMonthlyFamiliarIncome)

    return newData.apply(lambda x: x.astype(str).str.upper())

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

if __name__ == "__main__":
    sys.exit(main())