# Establecer nombre del dataset y el tipo de modelo para las pruebas
# Posibles valores: autoinforme, familia o profesional
source = 'autoinforme'
datasetName = 'dataset3.csv'

import pandas as pd
df = pd.read_csv('datasetsOld/' + source + '/' + datasetName)

df

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

import constants
import numpy as np

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

df = codeDataset(df)
df

from sklearn.model_selection import train_test_split

numberColumns = len(df.columns) 

X, y = df.values[:,0:(numberColumns - 1)], df.values[:,(numberColumns - 1)]
X_train, X_test, y_train, y_test =train_test_split(X, y, test_size=0.2, random_state=1, stratify=y)


from sklearn.naive_bayes import GaussianNB
import pickle
import os  

filePath = 'configFilesJupyter/'
filename = filePath + 'model_' + source + '.sav'

# Si existe un modelo previamente guardado, se carga, sino, se crea uno nuevo
if os.path.exists(filename):
    print('Existe un modelo anterior')
    clf_NB = pickle.load(open(filename, 'rb'))
    print('Modelo cargado')
else:
    print('Nuevo modelo')
    clf_NB = GaussianNB()

classNames = np.unique(df['Desenlace'].to_numpy())
clf_NB.partial_fit(X_train, y_train, classNames)

if os.path.exists(filePath) == False:
    os.mkdir(filePath)
    
#clf_NB = GaussianNB()
#clf_NB.fit(X_train, y_train)
# Guardamos el modelo en un archivo .pickle
pickle.dump(clf_NB, open(filename, 'wb'))

# Hacemos una prediccion de los datos de testing
y_pred = clf_NB.predict(X_test)

compareDF = pd.DataFrame()

compareDF['Real Result'] = y_test
compareDF['Predicted Result'] = y_pred
compareDF.head()

from sklearn.metrics import confusion_matrix, ConfusionMatrixDisplay
import matplotlib.pyplot as plt

classNames = np.unique(df['Desenlace'].to_numpy())
cm = confusion_matrix(y_test, y_pred, labels=classNames, normalize='all')
disp = ConfusionMatrixDisplay(confusion_matrix=cm,
                              display_labels=classNames)
disp.plot()
plt.show()


from sklearn.metrics import accuracy_score
from sklearn.metrics import precision_score
from sklearn.metrics import recall_score, f1_score
print('Exactitud - Accuracy: %.3f' % accuracy_score(y_true=y_test, y_pred=y_pred))
print('Precision: %.3f' % precision_score(y_true=y_test, y_pred=y_pred, average='micro'))
print('Sensibilidad - Recall: %.3f' % recall_score(y_true=y_test, y_pred=y_pred, average='micro'))
print('F1: %.3f' % f1_score(y_true=y_test, y_pred=y_pred, average='micro'))