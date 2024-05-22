# abstract base class work
from abc import ABC, abstractmethod
from sklearn.metrics import accuracy_score
from sklearn.metrics import precision_score
from sklearn.metrics import recall_score, f1_score

class Classifier(ABC):

    _classifier = None
    _X_train = None
    _X_test = None
    _y_train = None
    _y_test = None

    @abstractmethod
    def __init__(self):
        pass

    @abstractmethod
    def initClassifier(self):
        pass
    
    @abstractmethod
    def divideData(self, X, y, testSize, randomState):
        pass

    @abstractmethod
    def fitData(self):
        pass

    @abstractmethod
    def createConfusionMatrix(self, classNames):
        pass

    @abstractmethod
    def predict(self):
        pass

    def getPrecisionScore(self, y_pred):
        return precision_score(y_true=self._y_test, y_pred=y_pred, average='micro')

    def getRecallScore(self, y_pred):
        return recall_score(y_true=self._y_test, y_pred=y_pred, average='micro')

    def getAccuracyScore(self, y_pred):
        return accuracy_score(y_true=self._y_test, y_pred=y_pred)

    def getF1Score(self, y_pred):
        return f1_score(y_true=self._y_test, y_pred=y_pred, average='micro')
    
    def getSelectedScore(self, selectedScore, y_pred):
        data = {
            'precision': self.getPrecisionScore(y_pred),
            'accuracy': self.getAccuracyScore(y_pred),
            'f1': self.getF1Score(y_pred),
            'recall': self.getRecallScore(y_pred)
        }

        return data[selectedScore]
    
    @abstractmethod
    def getPScore(self, selectedScore, y_pred):
        pass

    pass