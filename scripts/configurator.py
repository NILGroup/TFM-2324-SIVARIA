import constants
import os
import pickle

class Configurator(object):
    __modelType = None
    __scoreType = None

    def __init__(self):
        config = self.loadConfig()

        try:
            modelType = config['modelType']
        except Exception:
            modelType = None

        try:
            scoreType = config['scoreType']
        except Exception:
            scoreType = None

        self.__modelType = modelType
        self.__scoreType = scoreType

    def loadConfig(self):
        config = None

        filename = constants.FILEPATH + constants.CONFIG_FILENAME + constants.CONFIG_FILETYPE

        if os.path.exists(filename):
            config = pickle.load(open(filename, 'rb'))

        return config
    
    def saveConfig(self):
        if os.path.exists(constants.FILEPATH) == False:
            os.mkdir(constants.FILEPATH)

        filename = constants.FILEPATH + constants.CONFIG_FILENAME + constants.CONFIG_FILETYPE

        config = {
            'modelType': self.__modelType,
            'scoreType': self.__scoreType
        }
        pickle.dump(config, open(filename, 'wb'))


    def getModelType(self):
        return self.__modelType

    def setModelType(self, modelType):
        
        if modelType not in constants.MODEL_TYPES:
            raise ValueError('Given model type is not valid. Possible values:\n\n' + '\n'.join(constants.MODEL_TYPES))

        self.__modelType = modelType

    def getScoreType(self):
        return self.__scoreType

    def setScoreType(self, scoreType):

        if scoreType not in constants.SCORE_OPTIONS:
            raise ValueError('Given score type is not valid. Possible values:\n\n' + '\n'.join(constants.SCORE_OPTIONS))

        self.__scoreType = scoreType