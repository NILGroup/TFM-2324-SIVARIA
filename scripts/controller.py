import sys
import pandas as pd
import os
import pickle
from datetime import datetime
import math
# Own created classes and modules
import constants
import decoder
from expertSystem import ExpertSystem
from exceptions.ApplicationException import ApplicationException
from exceptions.CommandLineException import CommandLineException

def main():
    try:
        if(len(sys.argv) <= 1):
            raise CommandLineException('Not enough parameters.\n\n' + getHelpMessage())
        
        option = sys.argv[1]
        expertSystem = ExpertSystem()
        config = getConfig()

        if option == '-h':
            print(getHelpMessage())
        elif option =='-mt':
            
            if len(sys.argv) <= 2:
                modelType = getModelType(config)
                if modelType is None:
                    modelType = 'None'
            else:
                modelType = sys.argv[2]
                setModelType(modelType)

            print('Model type of the Expert System: ' + str(modelType))
            print('Possible values:\n\n' + '\n'.join(constants.MODEL_TYPES))
        elif option =='-st':

            if len(sys.argv) <= 2:
                scoreType = getScoreType(config)
                if scoreType is None:
                    scoreType = 'None'
            else:
                scoreType = sys.argv[2]
                setScoreType(scoreType)
                
            print('Score type of the Expert System: ' + str(scoreType))
            print('Possible values:\n\n' + '\n'.join(constants.SCORE_OPTIONS))
        elif option =='-t':
            if len(sys.argv) <= 2:
                raise CommandLineException('Dataset not specified.\n\n' + getHelpMessage())
            
            modelType = getModelType(config)
            scoreType = getScoreType(config)

            if modelType is None or scoreType is None:
                checkErrors(config)
            
            dataset = sys.argv[2]

            if os.path.exists(dataset) == False:
                raise FileNotFoundError('Dataset not found. Type the whole path correctly.\n\n' + getHelpMessage())

            # Code Dataset
            df = pd.read_csv(dataset)
            newDF = decoder.codeDataset(df)

            expertSystem.setModelType(modelType)
            expertSystem.setScoreOption(scoreType)

            mostRecentFilename = getMostRecentFile(modelType)
            
            if mostRecentFilename is not None:
                print(getFileStats(mostRecentFilename))

            # Building the model
            expertSystem.buildModel(mostRecentFilename)
            
            # Training Model
            X_train, X_test, y_train, y_test = expertSystem.divideDatasetTrainingTesting(newDF)

            modelForTest = expertSystem.trainModel(X_train, y_train)

            # Saving model
            filePath, filename = getConfigModelFilename(expertSystem.getModelType())

            expertSystem.saveModel(filePath, filename)

            print(getFileStats(filename))

            print('Testing trained model ...')

            (p_valor, Cont) = expertSystem.testModel(modelForTest, X_train, y_train, X_test, y_test)
            print('Model tested successfully')
            print('('+ str(p_valor) + ',' + str(Cont) +')')

        elif option =='-p':
            if len(sys.argv) <= 2:
                raise CommandLineException('Dataset not specified.\n\n' + getHelpMessage())
            
            modelType = getModelType(config)

            if modelType is None:
                checkErrors(config)

            dataset = sys.argv[2]

            if os.path.exists(dataset) == False:
                raise FileNotFoundError('Dataset not found. Type the whole path correctly.\n\n' + getHelpMessage())
            
            df = pd.read_csv(dataset)
            newDF = decoder.codeDataset(df)

            expertSystem.setModelType(modelType)
            
            mostRecentFilename = getMostRecentFile(modelType)
            
            if mostRecentFilename is not None:
                print(getFileStats(mostRecentFilename))

            expertSystem.buildModel(mostRecentFilename)

            if 'Desenlace' in newDF.columns:
                newDF = newDF.drop('Desenlace', axis=1)

            y_pred = expertSystem.predict(newDF.values)
            return y_pred
        
        else:
            raise CommandLineException('Some parameters that do not exist were introduced.\n\n' + getHelpMessage())

    except (ApplicationException) as e:
        return 'Script error: ' + str(e.message)


def getHelpMessage():
    helpMessage = 'controller.py [OPTION] [DATASET|TYPE]\n\n'

    helpMessage += 'OPTION\n'
    helpMessage += '\t-h\tPrints the help message.n\n'
    helpMessage += '\t-mt\tPrint the current model type selected.\n'
    helpMessage += '\t\tIf the following parameter [TYPE] is a model type, \n'
    helpMessage += '\t\tthe configuration will be modified to this new model type.\n'
    helpMessage += '\t\tThe possible values are: ' + ', '.join(constants.MODEL_TYPES) + '\n\n'
    helpMessage += '\t\tExample: python controller.py -mt autoinforme\n\n'
    helpMessage += '\t-st\tPrint the current score type selected. \n'
    helpMessage += '\t\tIf the following parameter [TYPE] is a score type, \n'
    helpMessage += '\t\tthe configuration will be modified to this new score type.\n'
    helpMessage += '\t\tThe possible values are: ' + ', '.join(constants.SCORE_OPTIONS) + '\n\n'
    helpMessage += '\t\tExample: python controller.py -st accuracy\n\n'
    helpMessage += '\t-t\tTrain a model, that can be "autoinforme", "familia" and "profesional" given a dataset [DATASET].\n'
    helpMessage += '\t\tIn order to train the model correctly, a model type and a score type previously.\n'
    helpMessage += '\t\tIf not, the training will not work.\n\n'
    helpMessage += '\t-p\tReturn a list of predicted results given a dataset [DATASET].\n'

    return helpMessage

def getConfig():

    config = None
    filename = constants.FILEPATH + constants.CONFIG_FILENAME + constants.CONFIG_FILETYPE

    if os.path.exists(filename):
        config = pickle.load(open(filename, 'rb'))

    return config

def getModelType(config):
    try:
        return config['modelType']
    except Exception:
        return None

def setModelType(modelType):
    
    if modelType not in constants.MODEL_TYPES:
        raise ValueError('Given model type is not valid. Possible values:\n\n' + '\n'.join(constants.MODEL_TYPES))

    if os.path.exists(constants.FILEPATH) == False:
        os.mkdir(constants.FILEPATH)

    filename = constants.FILEPATH + constants.CONFIG_FILENAME + constants.CONFIG_FILETYPE

    config = {
        'modelType' : modelType
    }

    if os.path.exists(filename):
        configLoaded = pickle.load(open(filename, 'rb'))
        configLoaded.update(config)
        config = configLoaded

    pickle.dump(config, open(filename, 'wb'))

def getScoreType(config):
    try:
        return config['scoreType']
    except Exception:
        return None

def setScoreType(scoreType):
    if scoreType not in constants.SCORE_OPTIONS:
        raise ValueError('Given score type is not valid')

    if os.path.exists(constants.FILEPATH) == False:
        os.mkdir(constants.FILEPATH)

    filename = constants.FILEPATH + constants.CONFIG_FILENAME + constants.CONFIG_FILETYPE

    config = {
        'scoreType' : scoreType
    }

    if os.path.exists(filename):
        configLoaded = pickle.load(open(filename, 'rb'))
        configLoaded.update(config)
        config = configLoaded

    pickle.dump(config, open(filename, 'wb'))

def checkErrors(config):
    if config is None:
        raise CommandLineException('System configuration not found.\n\n' + '\n'.join(constants.MODEL_TYPES) + '\n')

    if 'modelType' not in config:
        raise CommandLineException('Model type not found in the configuration. Possible values:\n\n' + '\n'.join(constants.MODEL_TYPES) + '\n')

    if 'scoreType' not in config:
        raise CommandLineException('Score type not found in the configuration. Possible values:\n\n' + '\n'.join(constants.SCORE_OPTIONS) + '\n')


def getConfigModelFilename(modelType):
    now = datetime.now()
    versionDateTime = now.strftime("%Y%m%d%H%M%S")
    filePath = constants.FILEPATH + modelType
    filename = filePath + '/' + 'model_' + modelType + '_' + versionDateTime + constants.MODEL_FILETYPE

    return (filePath, filename)

def getFileStats(filename):
    fileInfoStr = 'File: ' + filename + '\n'

    fileStats = os.stat(filename)
    mostRecentAccess = datetime.fromtimestamp(fileStats.st_atime).strftime('%d-%m-%Y %H:%M:%S')
    mostRecentContentChange = datetime.fromtimestamp(fileStats.st_mtime).strftime("%d-%m-%Y %H:%M:%S")
    mostRecentMetadataChange = datetime.fromtimestamp(fileStats.st_ctime).strftime("%d-%m-%Y %H:%M:%S")

    fileInfoStr += 'File size (Bytes): ' + str(convertSize(fileStats.st_size)) + '\n'
    fileInfoStr += 'Most recent access: ' + str(mostRecentAccess) + '\n'
    fileInfoStr += 'Most recent content change: ' + str(mostRecentContentChange) + '\n'
    fileInfoStr += 'Most recent metadata change: ' + str(mostRecentMetadataChange) + '\n'

    return fileInfoStr

def getMostRecentFile(modelType):

    try:
        filePath = constants.FILEPATH + modelType + '/'
        listFiles = os.listdir(filePath)
        listFiles.sort(reverse=True)    

        return (filePath + listFiles[0])
    except Exception:
        return None
    

def convertSize(size_bytes):
   if size_bytes == 0:
       return "0B"
   size_name = ("B", "KiB", "MiB", "GiB", "TiB", "PiB", "EiB", "ZiB", "YiB")
   i = int(math.floor(math.log(size_bytes, 1024)))
   p = math.pow(1024, i)
   s = round(size_bytes / p, 2)
   return "%s %s" % (s, size_name[i])

if __name__ == "__main__":
    sys.exit(main())
