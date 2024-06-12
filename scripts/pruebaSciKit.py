import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.naive_bayes import GaussianNB
from sklearn.metrics import confusion_matrix, ConfusionMatrixDisplay
import matplotlib.pyplot as plt
import constants
import numpy as np

from sklearn.metrics import accuracy_score
from sklearn.metrics import precision_score
from sklearn.metrics import recall_score, f1_score

def decodeDataset(df):
    newData = df

    for key, values in constants.BAYES_NETWORK_STATE_NAMES.items():
        if key in newData:
            column = newData[key]
            newData[key] = column.apply(lambda x: values.index(x))

    #print(newData.head())
    #print(newData.dtypes)
    #newData.info()
    newData = newData.astype(np.int8)
    newData['Desenlace'] = newData['Desenlace'].apply(lambda x: constants.BAYES_NETWORK_STATE_NAMES['Desenlace'][x])
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

modelType = 'profesional'

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

# Dividimos el df entre la parte de training y la parte de test
numberColumns = len(df.columns) 
X, y = df.values[:, 0:(numberColumns - 1)], df.values[:, (numberColumns - 1)]
#print(df.head())
#print(X[0])
#print(y[0])
X_train, X_test, y_train, y_test =train_test_split(X, y, test_size=0.25, random_state=1, stratify=y)

clf_NB = GaussianNB()
clf_NB.fit(X_train, y_train)

# Hacemos una prediccion de los datos de testing
y_pred = clf_NB.predict(X_test)

# imprimimos la matriz de confusion
classNames = ['COMUNICACION', 'DESEO','IDEACION','PLANIFICACION','INTENCION','FINALIDAD']
#classNames = [0,1,2,3,4,5]
cm = confusion_matrix(y_test, y_pred, labels=classNames)
disp = ConfusionMatrixDisplay(confusion_matrix=cm,
                              display_labels=classNames)

disp.plot()
plt.show()

print('Exactitud - Accuracy: %.3f' % accuracy_score(y_true=y_test, y_pred=y_pred))
print('Precision: %.3f' % precision_score(y_true=y_test, y_pred=y_pred, average='micro'))
print('Sensibilidad - Recall: %.3f' % recall_score(y_true=y_test, y_pred=y_pred, average='micro'))
print('F1: %.3f' % f1_score(y_true=y_test, y_pred=y_pred, average='micro'))


ACC_Ini = accuracy_score(y_true=y_test, y_pred=y_pred)


NumRepeticiones = 100 # hacemos 100 muestras con bootstrap
NumMuestras = X_train.shape[0] # el número de muestras totales en X_train
indices = np.arange(X_train.shape[0]) # un listado con los índices de X_train 1,2,...,NumMuestras
clf_Boot = GaussianNB()
Cont = 0

i=0

for rep in np.arange(NumRepeticiones):
    indicesNew = np.random.choice(indices,NumMuestras,replace=True) #nuevos indices cogidos al azar
    X_train_Boot = X_train[indicesNew] # tomamos los datos X de esos indices
    y_train_Boot = y_train[indicesNew] # y sus categorías
    '''
    Usado para mostrar los indices y conjuntos X e y escogidos en las 2 primeras muestras 
    if i<2: 
        print(indicesNew)
        print(X_train_Boot)
        print(y_train_Boot)
    '''
    clf_Boot.fit(X_train_Boot, y_train_Boot)
    
    i+=1
    
    if clf_Boot.score(X_test, y_test) > ACC_Ini:
        Cont +=1

p_valor = (Cont+1)/(NumRepeticiones + 1)
print('(' + str(p_valor) + ',' + str(Cont) + ')')