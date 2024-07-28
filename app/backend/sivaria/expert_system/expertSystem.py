import os
import pickle
import numpy as np
from sklearn.naive_bayes import GaussianNB
from sklearn.model_selection import train_test_split, GridSearchCV
from sklearn.metrics import confusion_matrix, ConfusionMatrixDisplay
from sklearn.metrics import accuracy_score, precision_score, recall_score, f1_score
import copy
# Own created modules
from ..expert_system import constants

class ExpertSystem():
    __model = None
    __modelType = None
    #__scoreOption = None

    def __init__(self):
        pass

    def buildModel(self, filename):
        self.__model = self.__buildModel(filename)

    def getModelType(self):
        return self.__modelType

    def setModelType(self, modelType):
        self.__modelType = modelType
    '''
    def getScoreOption(self):
        return self.__scoreOption

    def setScoreOption(self, scoreOption):
        self.__scoreOption = scoreOption
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

    def trainModel(self, X_train, y_train, classNames):
        if self.__modelType is None:
            raise ValueError('Training process error: Model type not specified.\n\n' + '\n'.join(constants.MODEL_TYPES) + '\n')
    
        #if self.__scoreOption is None:
            #raise ValueError('Training process error: Score type not specified for testing.\n\n' + '\n'.join(constants.SCORE_OPTIONS) + '\n')

        modelForTest = copy.deepcopy(self.__model)

        param_grid = {
            'var_smoothing': np.logspace(0, -9, num=100)
        }
        grid_search = GridSearchCV(estimator=self.__model, param_grid=param_grid, cv=5, verbose=1, scoring='accuracy')
        grid_search.fit(X_train, y_train)

        # Mejor parámetro encontrado por GridSearchCV
        best_params = grid_search.best_params_

        # Mejor modelo encontrado por GridSearchCV
        best_model = grid_search.best_estimator_
        #print(best_params)
        print(best_model)

        self.__model = best_model

        #self.__model.partial_fit(X_train, y_train, classes=classNames)

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

    def saveModel(self, filePathByModelType, filename, metrics):

        if os.path.exists(constants.FILEPATH) == False:
            os.mkdir(constants.FILEPATH)

        if os.path.exists(filePathByModelType) == False:
            os.mkdir(filePathByModelType)

        # We save the file in a .pickle file
        data = {
            'model': self.__model,
            'metrics': metrics,
        }
        pickle.dump(data, open(filename, 'wb'))

    def testModel(self, modelForTest, y_pred, X_train, y_train, X_test, y_test):
        if not self.__modelType:
            raise ValueError('Model type not specified.')
        
        if not self.__model:
            raise ValueError('Model not specified.')

        #if not self.__scoreOption:
            #raise ValueError('Score type not set.')

        accuracy = accuracy_score(y_true=y_test, y_pred=y_pred)
        precision = precision_score(y_true=y_test, y_pred=y_pred, average='weighted')
        recall = recall_score(y_true=y_test, y_pred=y_pred, average='weighted')
        f1 = f1_score(y_true=y_test, y_pred=y_pred, average='weighted')
        
        print('\n')
        print('Accuracy = ' + str(accuracy))
        print('Precision = ' + str(precision))
        print('Recall = ' + str(recall))
        print('F1 Score = ' + str(f1))
        print('\n')

        return {
            'accuracy': accuracy,
            'precision': precision,
            'recall': recall,
            'f1_score': f1
        }
    '''
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
    '''
    def __buildModel(self, filename):

        # Si existe un modelo previamente guardado, se carga, sino, se crea uno nuevo
        if filename is not None and os.path.exists(filename):
            print('There exists a previously created model')
            print('Loading the model...')
            data = pickle.load(open(filename, 'rb'))
            clf_NB = data.get('model', None)
            print('Model loaded\n')
            metrics = data.get('metrics', {})
            print('Metrics:')
            #print(metrics)
            for name, metric in metrics.items():
                print('\t'+str(name) + '= ' + str(metric))
            print('\n')
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


