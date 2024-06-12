# abstract base class work
from sklearn.metrics import f1_score, accuracy_score, recall_score, precision_score
from pgmpy.metrics import correlation_score
from pgmpy.models import BayesianNetwork
from pgmpy.estimators import BayesianEstimator
import constants

class ExpertSystem():

    _model = None
    _modelAutoinforme = None
    _modelFamily = None
    _modelProfessional = None
    _modelType = None

    def __init__(self):
        pass

    def reset(self):
        self.buildModel()
        pass

    def getModel(self, type):
        if type == 'autoinforme':
            return self._modelAutoinforme
        elif type == 'family':
            return self._modelFamily
        elif type == 'professional':
            return self._modelProfessional
          
        pass

    def setModel(self, model, type):
        if type == 'autoinforme':
            self._modelAutoinforme = model
        elif type == 'family':
            self._modelFamily = model
        elif type == 'professional':
            self._modelProfessional = model
          
        pass

    def setModelType(self, type):
        self._modelType = type
        pass

    def buildModel(self, type):
        if self.__checkModelType(type) is False:
            raise ValueError('Model type does not exist')

        model=BayesianNetwork()
        variables = None
        edges = None

        if type == 'autoinforme':
            variables = constants.BAYES_NETWORK_VARIABLES_AUTOINFORME
            edges = constants.BAYES_NETWORK_EDGES_AUTOINFORME
        elif type == 'family':
            variables = constants.BAYES_NETWORK_VARIABLES_FAMILY
            edges = constants.BAYES_NETWORK_EDGES_FAMILY
        elif type == 'professional':
            variables = constants.BAYES_NETWORK_VARIABLES_PROFESSIONAL
            edges = constants.BAYES_NETWORK_EDGES_PROFESSIONAL

        model.add_nodes_from(variables)
        model.add_edges_from(edges)
        
        self.setModel(model, type=type)
        self.setModelType(type)
        print('Model built successfully.\n')
            
        return model

    def loadModel(self, type):
        if self.__checkModelType(type) is False:
            raise ValueError('Model type does not exist')

        fileName = None        

        if type == 'autoinforme':
            fileName = constants.AUTOINFORME_MODEL_FILENAME
        elif type == 'family':
            fileName = constants.FAMILY_MODEL_FILENAME
        elif type == 'professional':
            fileName = constants.PROFESSIONAL_MODEL_FILENAME
        
        modelLoaded = BayesianNetwork.load(filename=fileName, 
                                           filetype=constants.MODEL_FILETYPE)
        
        self.setModel(model=modelLoaded, type=type)
        self.setModelType(type)

        return modelLoaded 

    def saveModel(self):
        modelType = self._modelType
        
        if self.__checkModelType(modelType) is False:
            raise ValueError('Model type does not exist')
        
        model = self.getModel(modelType)
        model.check_model()

        #self.__checkModelByType(modelType)
        filename = self.__getModelFileName(modelType)
        
        print('Starting model save process.\n')
        print(modelType)
        model.save(filename=filename, 
                   filetype=constants.MODEL_FILETYPE)
        
        print('Model saved successfully\n')
        pass

    def trainModel(self, data):
        #print(data.head())
        modelType = self._modelType
        
        print(modelType)
        model = self.getModel(modelType)
        #if model is not None:
            #self.__checkModelByType(modelType)

        #fitData = data
        #fitUpdateData = data
        # iterating the columns
        '''
        for col in data.columns:
            if model.get_cpds(col) is None:
                fitUpdateData = data.drop(col, axis=1)
            else:
                fitData = data.drop(col, axis=1)
        '''

        '''
        if (len(self._model.get_cpds()) == 0):
            self._model.fit(data=data, 
                            estimator=BayesianEstimator, 
                            prior_type=constants.MODEL_PRIOR_TYPE, 
                            state_names=constants.BAYES_NETWORK_STATE_NAMES)
            
        else:
            self._model.fit_update(data=data)
        '''
        #print(fitData.head())
        #self._model.check_model()
        print('Training model. This process may take some minutes...')
        if  len(model.get_cpds()) == 0:
            #stateNames = {key: value for key, value in constants.BAYES_NETWORK_STATE_NAMES.items() if key in data.columns}
            #print(stateNames)
            model.fit(data, 
                      estimator=BayesianEstimator, 
                      prior_type=constants.MODEL_PRIOR_TYPE) 
                      #state_names=stateNames)

        else:
            model.fit_update(data)

        self.setModel(model, modelType)

        print('Model trained successfully\n')
        self.saveModel()

        pass

    def predict(self, predictData):
        modelType = self._modelType
        model = self.getModel(modelType)
        return model.predict(predictData)
    
    def getFScore(self, testSet):
        return correlation_score(model=self._model, 
                                 data=testSet, 
                                 test=constants.CORRELATION_SCORE_STATISTICAL_TEST, 
                                 score=f1_score, 
                                 significance_level=constants.CORRELATION_SCORE_SIGNIFICANCE_LEVEL)


    def getAccuracyScore(self, testSet):
        return correlation_score(model=self._model, 
                                 data=testSet, 
                                 test=constants.CORRELATION_SCORE_STATISTICAL_TEST, 
                                 score=accuracy_score, 
                                 significance_level=constants.CORRELATION_SCORE_SIGNIFICANCE_LEVEL)

    def getRecallScore(self, testSet):
        return correlation_score(model=self._model, 
                                 data=testSet, 
                                 test=constants.CORRELATION_SCORE_STATISTICAL_TEST, 
                                 score=recall_score, 
                                 significance_level=constants.CORRELATION_SCORE_SIGNIFICANCE_LEVEL)

    def getPrecisionScore(self, testSet):
        return correlation_score(model=self._model, 
                                 data=testSet, 
                                 test=constants.CORRELATION_SCORE_STATISTICAL_TEST, 
                                 score=precision_score, 
                                 significance_level=constants.CORRELATION_SCORE_SIGNIFICANCE_LEVEL)
    
    def __checkModelType(self, type):
        return (type == 'autoinforme' or type == 'family' or type == 'professional')

    def __checkModelByType(self, type):
        if type == 'autoinforme':
            return self._modelAutoinforme is not None and self._modelAutoinforme.check_model()
        elif type == 'family':
            return self._modelFamily is not None and self._modelFamily.check_model()
        elif type == 'professional':
            return self._modelProfessional is not None and self._modelProfessional.check_model()
        
    def __getModelFileName(self, type):
        if type == 'autoinforme':
            return constants.AUTOINFORME_MODEL_FILENAME
        elif type == 'family':
            return constants.FAMILY_MODEL_FILENAME
        elif type == 'professional':
            return constants.PROFESSIONAL_MODEL_FILENAME
        else:
            return None

    pass