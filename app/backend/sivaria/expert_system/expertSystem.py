import os
import pickle
import numpy as np
from sklearn.naive_bayes import GaussianNB
from sklearn.model_selection import train_test_split
from sklearn.metrics import confusion_matrix, ConfusionMatrixDisplay
from sklearn.metrics import accuracy_score, precision_score, recall_score, f1_score
import copy
# Own created modules
from ..expert_system import constants

class ExpertSystem():
    __model = None
    __modelType = None
    __scoreOption = None

    def __init__(self):
        pass

    def buildModel(self, filename):
        self.__model = self.__buildModel(filename)

    def getModelType(self):
        return self.__modelType

    def setModelType(self, modelType):
        self.__modelType = modelType

    def getScoreOption(self):
        return self.__scoreOption

    def setScoreOption(self, scoreOption):
        self.__scoreOption = scoreOption

    def divideDatasetTrainingTesting(self, dataframe):
        numberColumns = len(dataframe.columns) 

        X, y = dataframe.values[:,0:(numberColumns - 1)], dataframe.values[:,(numberColumns - 1)]
        X_train, X_test, y_train, y_test = train_test_split(X, 
                                                            y, 
                                                            test_size=constants.TESTING_DATASET_SIZE, 
                                                            random_state=1, 
                                                            stratify=y)   
        return (X_train, X_test, y_train, y_test)

    def trainModel(self, X_train, y_train, classNames):
        #try:
        if not self.__modelType:
            raise ValueError('Training process error: Model type not specified.\n\n' + '\n'.join(constants.MODEL_TYPES) + '\n')
    
        if not self.__scoreOption:
            raise ValueError('Training process error: Score type not specified for testing.\n\n' + '\n'.join(constants.SCORE_OPTIONS) + '\n')

        modelForTest = copy.deepcopy(self.__model)

        self.__model.partial_fit(X_train, y_train, classes=classNames)
        #except Exception as e:
            #print(str(e))
        return modelForTest
    
    def predict(self, X_data):
        return self.__model.predict(X_data)
    
    def getConfusionMatrix(self, y_test, y_pred, classNames, toNormalize = True):
        if toNormalize == True:
            cm = confusion_matrix(y_test, y_pred, labels=classNames, normalize='all')
        else:
            cm = confusion_matrix(y_test, y_pred, labels=classNames)
            
        return cm
    
    def getConfusionMatrixDisplay(self, cm, classNames):
        return ConfusionMatrixDisplay(confusion_matrix=cm,
                                      display_labels=classNames)

    def saveModel(self, filePathByModelType, filename):

        if not os.path.exists(constants.FILEPATH):
            os.mkdir(constants.FILEPATH)

        if not os.path.exists(filePathByModelType):
            os.mkdir(filePathByModelType)

        # We save the file in a .pickle file
        
        pickle.dump(self.__model, open(filename, 'wb'))

    def testModel(self, modelForTest, y_pred, X_train, y_train, X_test, y_test):
        if not self.__modelType:
            raise ValueError('Model type not specified.')
        
        if not self.__model:
            raise ValueError('Model not specified.')

        if not self.__scoreOption:
            raise ValueError('Score type not set.')

        #clf_NB = modelForTest
        #clf_NB.fit(X_train, y_train)
        #y_pred = clf_NB.predict(X_test)
        Score_Ini = self.getScore(y_test, y_pred)
        print('Selected score: ' + self.__scoreOption + ' = %.3f' % Score_Ini)

        NumRepeticiones = 200 # hacemos 200 muestras con bootstrap
        NumMuestras = X_train.shape[0] # el número de muestras totales en X_train
        NumMuestrasTest = X_test.shape[0]
        indices = np.arange(X_train.shape[0]) # un listado con los índices de X_train 1,2,...,NumMuestras
        indicesTest = np.arange(X_test.shape[0])
        clf_Boot = modelForTest
        Cont = 0

        #i=0

        for _ in np.arange(NumRepeticiones):
            indicesNew = np.random.choice(indices,NumMuestras,replace=True) #nuevos indices cogidos al azar
            indicesNewTest = np.random.choice(indicesTest, NumMuestrasTest, replace=True)
            X_train_Boot = X_train[indicesNew] # tomamos los datos X de esos indices
            y_train_Boot = y_train[indicesNew] # y sus categorías

            X_test_Boot = X_test[indicesNewTest]
            y_test_Boot = y_test[indicesNewTest]
            
            clf_Boot.fit(X_train_Boot, y_train_Boot)

            y_pred_Boot = clf_Boot.predict(X_test_Boot)
            
            #i+=1
            
            if self.getScore(y_test_Boot, y_pred_Boot) > Score_Ini:
                Cont +=1

        p_valor = (Cont+1)/(NumRepeticiones + 1)

        return (p_valor, Cont)

    def getScore(self, y_test, y_pred):
        score = 0
        
        if self.__scoreOption == 'accuracy':
             score = accuracy_score(y_true=y_test, y_pred=y_pred)
        elif self.__scoreOption == 'precision':
             score = precision_score(y_true=y_test, y_pred=y_pred, average='weighted')
        elif self.__scoreOption == 'recall':
             score = recall_score(y_true=y_test, y_pred=y_pred, average='weighted')
        elif self.__scoreOption == 'f1_score':
             score = f1_score(y_true=y_test, y_pred=y_pred, average='weighted')
             
        return score

    def __buildModel(self, filename):

        # Si existe un modelo previamente guardado, se carga, sino, se crea uno nuevo
        if filename and os.path.exists(filename):
            print('There exists a previously created model')
            print('Loading the model...')
            clf_NB = pickle.load(open(filename, 'rb'))
            print('Model loaded\n')
        else:
            print('It does not exist a previous model.\nCreating a new model\n')
            clf_NB = GaussianNB()

        return clf_NB
    '''
    def __getFileStats(filename):
        fileInfoStr = 'Archivo: ' + filename + '\n'

        fileStats = os.stat(filename)
        mostRecentAccess = str(datetime.timedelta(seconds = fileStats.st_atime))
        mostRecentContentChange = str(datetime.timedelta(seconds = fileStats.st_atime))
        mostRecentMetadataChange = str(datetime.timedelta(seconds = fileStats.st_atime))

        fileInfoStr += 'Tamaño del archivo (Bytes): ' + str(fileStats.st_size) + '\n'
        fileInfoStr += 'Último acceso: ' + str(mostRecentAccess) + '\n'
        fileInfoStr += 'Última modificación del contenido del archivo: ' + str(mostRecentContentChange) + '\n'
        fileInfoStr += 'Última modificación de los metadatos del archivo: ' + str(mostRecentMetadataChange) + '\n'

        return fileInfoStr

    def __getConfigModelFilename(self, filename = None):
        #filename = 'error.sav'
           
        now = datetime.now()
        versionDateTime = now.strftime("%Y%m%d%H%M%S")
        filename = constants.FILEPATH + self.__modelType + '/' + 'model_' + self.__modelType + '_' + versionDateTime + constants.MODEL_FILETYPE

        return filename
    '''


