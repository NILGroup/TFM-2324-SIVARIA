# abstract base class work
from sklearn.metrics import f1_score, accuracy_score, recall_score, precision_score
from pgmpy.metrics import correlation_score
from pgmpy.models import BayesianNetwork
from pgmpy.estimators import BayesianEstimator
import constants

class OldExpertSystem():

    _model = None

    def __init__(self):
        pass

    def reset(self):
        self.buildModel()
        pass

    def setModel(self, model):
        self._model = model
        pass

    def buildModel(self):
        self.setModel(model=BayesianNetwork())
        '''
        -------------------------------------------------------
        En este apartado se debe empezar a construir el modelo
        '''
        self._model.add_nodes_from(
            constants.BAYES_NETWORK_VARIABLES
        )
        
        self._model.add_edges_from(
            constants.BAYES_NETWORK_EDGES
        )
        '''
        -------------------------------------------------------
        '''
        print('Model built successfully.\n')
            
        #self.saveModel()
        return self._model

    def loadModel(self):
        model = self.setModel(model=BayesianNetwork.load(filename=constants.MODEL_FILENAME, 
                                                         filetype=constants.MODEL_FILETYPE))
        
        self.setModel(model)
        return model 

    def saveModel(self):
        if self._model is None:
            raise ValueError('Model not defined')
        
        print('Starting model save process.\n')
        
        self._model.save(filename=constants.MODEL_FILENAME, 
                         filetype=constants.MODEL_FILETYPE)
        
        print('Model saved successfully\n')
        pass

    def trainModel(self, data):
        print(data.head())
        fitData = data
        fitUpdateData = data
        # iterating the columns
        for col in data.columns:
            if self._model.get_cpds(col) is None:
                fitUpdateData = data.drop(col, axis=1)
            else:
                fitData = data.drop(col, axis=1)

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
        if fitData.empty is False:
            stateNames = {key: value for key, value in constants.BAYES_NETWORK_STATE_NAMES.items() if key in fitData.columns}
            print(stateNames)
            self._model.fit(data=fitData, 
                            estimator=BayesianEstimator, 
                            prior_type=constants.MODEL_PRIOR_TYPE, 
                            state_names=stateNames)

        if fitUpdateData.empty is False:
            self._model.fit_update(data=fitUpdateData)


        if self._model.check_model() is True:
            print('Model trained successfully\n')
            self.saveModel()

        pass

    def predict(self, predictData):
        return self._model.predict(predictData)
    
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

    pass