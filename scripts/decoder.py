import constants
import pandas as pd

def codeAgeColumn(age):
    if age < 12:
        return 'MENOR DE 12'
    elif age > 21:
        return 'MAYOR DE 21'
    else:
        return str(age)

def codeHeightColumn(height):
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

def codeWeightColumn(weight):
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

def codeMonthlyFamiliarIncome(income):
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

def changeValuesToNumeric(df):
    newData = df.apply(lambda x: x.astype(str).str.upper())

    for key, values in constants.BAYES_NETWORK_STATE_NAMES.items():
        if key in newData and key != 'Desenlace':
            newData[key] = newData[key].apply(lambda x: values.index(x))

    
    return newData

def codeDataset(df):
    newDF = df

    # Eliminamos las columnas Index y Nombre, que no son necesarios
    newDF = newDF.drop(['Index', 'Nombre'], axis=1)

    # Metemos los valores dentro de rangos
    newDF['Edad'] = newDF['Edad'].apply(codeAgeColumn)
    newDF['Altura'] = newDF['Altura'].apply(codeHeightColumn)
    newDF['Peso'] = newDF['Peso'].apply(codeWeightColumn)

    # La columna 'Ingreso familiar mensual' sólo se encuentra en los datasets de profesionales
    if 'Ingreso familiar mensual' in newDF:
        newDF['Ingreso familiar mensual'] = newDF['Ingreso familiar mensual'].apply(codeMonthlyFamiliarIncome)
    
    # Codificamos los valores de todas las columnas a vlores numéricos
    newDF = changeValuesToNumeric(newDF)

    return newDF