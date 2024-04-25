# abstract base class work
from abc import ABC, abstractmethod
import numpy as np
from sklearn.naive_bayes import GaussianNB
from sklearn.model_selection import train_test_split
from sklearn.metrics import plot_confusion_matrix
from classifier import Classifier

class NaiveBayesClassifier(Classifier):

    # Override
    def __init__(self):
        self._classifier = GaussianNB()
        pass

    # Override
    def initClassifier(self):
        pass
    
    # Override
    def divideData(self, X, y, testSize, randomState):
        self._X_train, self._X_test, self._y_train, self._y_test=train_test_split(X, y, test_size=testSize, random_state=randomState, stratify=y)
        pass

    # Override
    def fitData(self):
        self._classifier.fit(self._X_train, self._y_train)
        pass

    # Override
    def createConfusionMatrix(self, classNames):
        return plot_confusion_matrix(self._classifier, self._X_test, self._y_test, display_labels=classNames) 

    # Override
    def predict(self):
        return self._classifier.predict(self._X_test)
    
    # Override
    def getPScore(self, selectedScore, y_pred, numRepetitions):
        #self._classifier.fit(self._X_train, self._y_train)
        #y_pred=self._classifier.predict(self._X_test)
        initScore = self.getSelectedScore(selectedScore, y_pred)
        print('Selected score: '+ selectedScore +'\nInitial Score: %.3f' % initScore)

        ## Hacemos el entrenamiento de los clasificadores
        NumRepeticiones = numRepetitions # hacemos 100 muestras con bootstrap
        NumMuestras = self._X_train.shape[0] # el número de muestras totales en X_train
        indices = np.arange(self._X_train.shape[0]) # un listado con los índices de X_train 1,2,...,NumMuestras
        clf_Boot = GaussianNB()
        Cont = 0

        #i=0

        for rep in np.arange(NumRepeticiones):
            indicesNew = np.random.choice(indices,NumMuestras,replace=True) #nuevos indices cogidos al azar
            X_train_Boot = self._X_train[indicesNew] # tomamos los datos X de esos indices
            y_train_Boot = self._y_train[indicesNew] # y sus categorías
            '''
            Usado para mostrar los indices y conjuntos X e y escogidos en las 2 primeras muestras 
            if i<2: 
                print(indicesNew)
                print(X_train_Boot)
                print(y_train_Boot)
            '''
            clf_Boot.fit(X_train_Boot, y_train_Boot)
            
            #i+=1
            
            if clf_Boot.score(self._X_test, self._y_test) > initScore:
                Cont +=1

        p_valor = (Cont+1)/(NumRepeticiones + 1)
        
        return str(p_valor), str(Cont)


    pass