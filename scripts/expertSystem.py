#from naiveBayesClassifier import NaiveBayesClassifier
from exceptions.ClassifierNotFoundException import ClassifierNotFoundException
import constants
from sklearn.naive_bayes import GaussianNB
import os
import pickle
from sklearn.model_selection import train_test_split
from sklearn.metrics import confusion_matrix, ConfusionMatrixDisplay
from sklearn.metrics import accuracy_score, precision_score, recall_score, f1_score
import numpy as np



class ExpertSystem():
    __model = None
    __modelType = None
    __scoreOption = None

    def __init__(self):
        pass

    def buildModel(self):
        self.__model = self.__buildModel()

    def getModelType(self):
        return self.__modelType

    def setModelType(self, modelType):
        self.__modelType = modelType

    def getScoreOption(self):
        return self.__scoreOption

    def setScoreOption(self, scoreOption):
        self.__scoreOption = scoreOption
    '''
    def setClassifier(self, classifier):
        if classifier.lower() == constants.NAIVE_BAYES:
            self._classifier = NaiveBayesClassifier()
        else:
            raise ClassifierNotFoundException()
        pass

    def divideData(self, dataframe, xCols, yCols, testSize, randomState):
        X, y = dataframe.values[:,0:xCols], dataframe.values[:,yCols]
        self._classifier.divideData(X, y, testSize, randomState)
        pass

    def fitData(self):
        self._classifier.fitData()
        pass

    def createConfusionMatrix(self, classNames):
        return self._classifier.createConfusionMatrix(classNames)
        
    def predict(self):
        return self._classifier.predict()
    
    def getPrecisionScore(self, y_pred):
        return self._classifier.getPrecisionScore(y_pred)

    def getRecallScore(self, y_pred):
        return self._classifier.getRecallScore(y_pred)

    def getAccuracyScore(self, y_pred):
        return self._classifier.getAccuracyScore(y_pred)

    def getF1Score(self, y_pred):
        return self._classifier.getF1Score(y_pred)

    def getPScore(self, selectedScore, y_pred, numRepetitions):
        return self._classifier.getPScore(selectedScore, y_pred, numRepetitions)
    '''

    def divideDatasetTrainingTesting(self, dataframe):
        numberColumns = len(dataframe.columns) 

        X, y = dataframe.values[:,0:(numberColumns - 1)], dataframe.values[:,(numberColumns - 1)]
        X_train, X_test, y_train, y_test = train_test_split(X, 
                                                            y, 
                                                            test_size=constants.TESTING_DATASET_SIZE, 
                                                            random_state=1, 
                                                            stratify=y)   
        return (X_train, X_test, y_train, y_test)

    def trainModel(self, dataframe):

        if self.__modelType is None:
            raise ValueError('Training process error: Model type not specified.\n\n' + '\n'.join(constants.MODEL_TYPES) + '\n')
        
        if self.__scoreOption is None:
            raise ValueError('Training process error: Score type not specified for testing.\n\n' + '\n'.join(constants.SCORE_OPTIONS) + '\n')

        print('Entrenando el modelo...') 

        X_train, X_test, y_train, y_test = self.divideDatasetTrainingTesting(dataframe)

        modelForTest = self.__model

        self.__model.fit(X_train, y_train)

        print('Modelo entrenado exitosamente\n')

        self.saveModel()

        print('Testeando entrenamiento realizado...')
        #y_pred = self.predict(X_test)

        (p_valor, Cont) = self.testModel(modelForTest, X_train, y_train, X_test, y_test)
        print('Testeo realizado con éxito')
        print('('+ str(p_valor) + ',' + str(Cont) +')')

    def predict(self, X_data):
        return self.__model.predict(X_data)
    
    def plotConfusionMatrix(self, y_test, y_pred, classNames):
        #classNames = df['Desenlace']

        cm = confusion_matrix(y_test, y_pred, labels=classNames)
        disp = ConfusionMatrixDisplay(confusion_matrix=cm,
                                      display_labels=classNames)
        return disp

    def saveModel(self):
        print('Guardando modelo...')
        filename = self.__getConfigModelFilename()
        if os.path.exists(constants.FILEPATH) == False:
            os.mkdir(constants.FILEPATH)

        # Guardamos el modelo en un archivo .pickle
        pickle.dump(self.__model, open(filename, 'wb'))
        print('Modelo guardado\n')

    def testModel(self, modelForTest, X_train, y_train, X_test, y_test):
        if self.__modelType is None:
            raise ValueError('Model type not specified.')
        
        if self.__model is None:
            raise ValueError('Model not specified.')

        if self.__scoreOption is None:
            raise ValueError('Score type not set.')

        clf_NB = modelForTest
        clf_NB.fit(X_train, y_train)
        y_pred = clf_NB.predict(X_test)
        ACC_Ini = self.getScore(y_test, y_pred)
        print('Score elegido: ' + self.__scoreOption + ' = %.3f' % ACC_Ini)

        NumRepeticiones = 100 # hacemos 100 muestras con bootstrap
        NumMuestras = X_train.shape[0] # el número de muestras totales en X_train
        NumMuestrasTest = X_test.shape[0]
        indices = np.arange(X_train.shape[0]) # un listado con los índices de X_train 1,2,...,NumMuestras
        indicesTest = np.arange(X_test.shape[0])
        clf_Boot = modelForTest
        Cont = 0

        #i=0

        for rep in np.arange(NumRepeticiones):
            indicesNew = np.random.choice(indices,NumMuestras,replace=True) #nuevos indices cogidos al azar
            indicesNewTest = np.random.choice(indicesTest, NumMuestrasTest, replace=True)
            X_train_Boot = X_train[indicesNew] # tomamos los datos X de esos indices
            y_train_Boot = y_train[indicesNew] # y sus categorías

            X_test_Boot = X_test[indicesNewTest]
            y_test_Boot = y_test[indicesNewTest]
            
            clf_Boot.fit(X_train_Boot, y_train_Boot)

            y_pred_Boot = clf_Boot.predict(X_test_Boot)
            
            #i+=1
            
            if self.getScore(y_test_Boot, y_pred_Boot) > ACC_Ini:
                Cont +=1

        p_valor = (Cont+1)/(NumRepeticiones + 1)

        return (p_valor, Cont)

    def getScore(self, y_test, y_pred):
        score = 0

        if self.__scoreOption == 'accuracy':
             score = accuracy_score(y_true=y_test, y_pred=y_pred)
        elif self.__scoreOption == 'precision':
             score = precision_score(y_true=y_test, y_pred=y_pred, average='micro')
        elif self.__scoreOption == 'recall':
             score = recall_score(y_true=y_test, y_pred=y_pred, average='micro')
        elif self.__scoreOption == 'f1_score':
             score = f1_score(y_true=y_test, y_pred=y_pred, average='micro')
             
        return score

    def __buildModel(self):
        filename = self.__getConfigModelFilename()

        # Si existe un modelo previamente guardado, se carga, sino, se crea uno nuevo
        if os.path.exists(filename):
            print('Existe un modelo anterior')
            clf_NB = pickle.load(open(filename, 'rb'))
            print('Modelo cargado\n')
        else:
            print('No existe un modelo anterior.\n Creando nuevo modelo\n')
            clf_NB = GaussianNB()

        return clf_NB

    def __getConfigModelFilename(self):
        return constants.FILEPATH + 'model_' + self.__modelType + constants.MODEL_FILETYPE

    pass


