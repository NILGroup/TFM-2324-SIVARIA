from naiveBayesClassifier import NaiveBayesClassifier
from exceptions.ClassifierNotFoundException import ClassifierNotFoundException
import constants

class ClassifierController:
    _classifier = None

    def __init__(self):
        pass

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
    
    pass


