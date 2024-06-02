import sys
import pandas as pd
import os
import pickle
from datetime import datetime
import math
import numpy as np
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
            return getHelpMessage()
        elif option =='-mt':
            
            if len(sys.argv) <= 2:
                modelType = getModelType(config)
                if modelType is None:
                    modelType = 'None'
            else:
                modelType = sys.argv[2]
                setModelType(modelType)

            output = 'Model type of the Expert System: ' + str(modelType) + '\n'
            output += 'Possible values:\n\n' + '\n'.join(constants.MODEL_TYPES) + '\n'

            return output
        
        elif option =='-st':

            if len(sys.argv) <= 2:
                scoreType = getScoreType(config)
                if scoreType is None:
                    scoreType = 'None'
            else:
                scoreType = sys.argv[2]
                setScoreType(scoreType)
            
            output = 'Score type of the Expert System: ' + str(scoreType) + '\n'
            output += 'Possible values:\n\n' + '\n'.join(constants.SCORE_OPTIONS) + '\n'

            return output
        elif option == '-lst':
            output = {}
            total = 0
            if len(sys.argv) <= 2:
                for modelType in constants.MODEL_TYPES:
                    filePath = constants.FILEPATH + modelType
                    files = os.listdir(filePath)
                    total += len(files)
                    output[modelType] = files
                    
            else:
                modelType = sys.argv[2]
                filePath = constants.FILEPATH + modelType
                files = os.listdir(filePath)
                output[modelType] = files
                total = len(files)

            output['total'] = total
            return output
        elif option == '-fs':

            if len(sys.argv) <= 2:
                raise CommandLineException('Filename not provided.\n\n' + getHelpMessage())
            
            output = {}

            filename = sys.argv[2]

            modelType = filename.split('_')[1]
            output[modelType] = []
            output[modelType].append(getFileStats(constants.FILEPATH + modelType + '/' + filename))

            return output
        elif option == '-rm':

            if len(sys.argv) <= 2:
                raise CommandLineException('Filename not provided.\n\n' + getHelpMessage())
            
            filename = sys.argv[2]

            modelType = filename.split('_')[1]
            filePath = constants.FILEPATH + modelType + '/' + filename
            if os.path.exists(filePath) == False:
                raise FileNotFoundError('Filename not found. Type the name correctly.\n\n' + getHelpMessage())

            os.remove(filePath)
            return 'File removed successfully'
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
                print(getFileInfo(mostRecentFilename))

            # Building Model
            expertSystem.buildModel(mostRecentFilename)
            
            # Training Model
            print('Training the model...') 
            X_train, X_test, y_train, y_test = expertSystem.divideDatasetTrainingTesting(newDF)

            modelForTest = expertSystem.trainModel(X_train, y_train)
            print('Model trained successfully\n')

            # Testing Model
            print('Testing trained model ...')

            y_pred = expertSystem.predict(X_test)
            classNames = ['COMUNICACION', 'DESEO','IDEACION','PLANIFICACION','INTENCION','FINALIDAD']
            cm = expertSystem.getConfusionMatrix(y_test, y_pred, classNames)

            (p_valor, Cont) = expertSystem.testModel(modelForTest, y_pred, X_train, y_train, X_test, y_test)
            print('Model tested successfully')
            #print('('+ str(p_valor) + ',' + str(Cont) +')')

            # Saving model
            print('Saving model...')
            filePath, filename = getConfigModelFilename(expertSystem.getModelType())

            expertSystem.saveModel(filePath, filename)
            print('Model saved\n')

            print(getFileInfo(filename))

            # Preparing data to return 

            FP = cm.sum(axis=0) - np.diag(cm)  
            FN = cm.sum(axis=1) - np.diag(cm)
            TP = np.diag(cm)
            TN = cm.sum() - (FP + FN + TP)
            
            result = {
                'positive_negative_data': {
                    'total': {
                        'TP': sum(TP),
                        'TN': sum(TN),
                        'FP': sum(FP),
                        'FN': sum(FN)
                    }
                },
                'p_value_testing': {
                    'p_valor':p_valor,
                    'Cont': Cont
                }
            }
            
            index = 0
            for className in classNames:
                classNameLower = className.lower()
                predictionResults = {}
                predictionResults['TP'] = TP[index]
                predictionResults['TN'] = TN[index]
                predictionResults['FP'] = FP[index]
                predictionResults['FN'] = FN[index]
                result['positive_negative_data'][classNameLower] = predictionResults
                index += 1 

            return result

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
                print(getFileInfo(mostRecentFilename))

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
    helpMessage = 'controller.py [OPTION] [DATASET|MODEL TYPE|MODEL SAVE FILENAME]\n\n'

    helpMessage += 'OPTION\n'
    helpMessage += '\t-h\tPrints the help message.\n\n'
    helpMessage += '\t-mt\tPrint the current model type selected.\n'
    helpMessage += '\t\tIf the following parameter [MODEL TYPE] is a model type, \n'
    helpMessage += '\t\tthe configuration will be modified to this new model type.\n'
    helpMessage += '\t\tThe possible values are: ' + ', '.join(constants.MODEL_TYPES) + '\n\n'
    helpMessage += '\t\tExample: python controller.py -mt autoinforme\n\n'
    helpMessage += '\t-st\tPrint the current score type selected. \n'
    helpMessage += '\t\tIf the following parameter [MODEL TYPE] is a score type, \n'
    helpMessage += '\t\tthe configuration will be modified to this new score type.\n'
    helpMessage += '\t\tThe possible values are: ' + ', '.join(constants.SCORE_OPTIONS) + '\n\n'
    helpMessage += '\t\tExample: python controller.py -st accuracy\n\n'
    helpMessage += '\t-lst\tReturn an object of list of save files. If a model type [MODEL TYPE] is provided,\n'
    helpMessage += '\t\tit returns all the save files of that model.\n'
    helpMessage += '\t\tOtherwise, it returns an object with all the save files of all model types.\n\n'
    helpMessage += '\t\tExample: python controller.py -lst autoinforme\n\n'
    helpMessage += '\t-fs\tReturn an object with the stats of a given save file name in [MODEL SAVE FILENAME].\n\n'
    helpMessage += '\t-rm\tRemove a save filename of a model given its name in [MODEL SAVE FILENAME].\n\n'
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

def getFileInfo(filename):
    fileStats = getFileStats(filename)

    fileInfoStr = 'File: ' + filename + '\n'

    fileInfoStr += 'File size: ' + str(fileStats['st_size']) + '\n'
    fileInfoStr += 'Most recent access: ' + str(fileStats['st_atime']) + '\n'
    fileInfoStr += 'Most recent content change: ' + str(fileStats['st_mtime']) + '\n'
    fileInfoStr += 'Most recent metadata change: ' + str(fileStats['st_ctime']) + '\n'

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

def convertSecondsToDatetime(st_time):
    return datetime.fromtimestamp(st_time).strftime('%d-%m-%Y %H:%M:%S')

def getFileStats(filename):
    fileStats = os.stat(filename)

    return {
        'filename': filename,
        'st_atime': convertSecondsToDatetime(fileStats.st_atime),
        'st_mtime': convertSecondsToDatetime(fileStats.st_mtime),
        'st_ctime': convertSecondsToDatetime(fileStats.st_ctime),
        'st_size': convertSize(fileStats.st_size),
    }

if __name__ == "__main__":
    sys.exit(main())
