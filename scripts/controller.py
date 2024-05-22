import checker

import sys
import pandas as pd
import os
import pickle
# Own created classes and modules
from expertSystem import ExpertSystem
from exceptions.ClassifierNotFoundException import ClassifierNotFoundException
from exceptions.ApplicationException import ApplicationException
from exceptions.CommandLineException import CommandLineException
from exceptions.ScoreNotFoundException import ScoreNotFoundException
from exceptions.FormatException import FormatException
import constants
import decoder
from datetime import datetime, timedelta

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

                print('Model type of the Expert System: ' + str(modelType))
            else:
                modelType = sys.argv[2]
                setModelType(modelType)
        elif option =='-st':

            if len(sys.argv) <= 2:
                scoreType = getScoreType(config)
                if scoreType is None:
                    scoreType = 'None'

                print('Score type of the Expert System: ' + str(scoreType))
            else:
                scoreType = sys.argv[2]
                setScoreType(scoreType)
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
        '''
        elif option =='-ptst':
            if len(sys.argv) <= 2:
                raise CommandLineException('Dataset not specified.\n\n' + getHelpMessage())
            
            modelType = getModelType(config)
            
            expertSystem.setModel(modelType)

            dataset = sys.argv[2]

            if os.path.exists(dataset) == False:
                raise FileNotFoundError('Dataset not found. Type the whole path correctly.')
            
            df = pd.read_csv(dataset)
            newDF = codeDataset(df)

            X_train, X_test, y_train, y_test = expertSystem.divideDatasetTrainingTesting(newDF)

            y_pred = expertSystem.predict(X_test)
            return y_pred
        elif option =='-pm':
            if len(sys.argv) <= 2:
                raise CommandLineException('Dataset not specified.\n\n' + getHelpMessage())
            
            dataset = sys.argv[2]

            if os.path.exists(dataset) == False:
                raise FileNotFoundError('Dataset not found. Type the whole path correctly.')

            df = pd.read_csv(dataset)
            newDF = codeDataset(df)
            y_pred = expertSystem.predict(newDF)
            print(expertSystem.plotConfusionMatrix(newDF['Desenlace'], y_pred))
        elif option =='-tst':
            if len(sys.argv) <= 2:
                raise CommandLineException('Dataset not specified.\n\n' + getHelpMessage())
            
            dataset = sys.argv[2]

            if os.path.exists(dataset) == False:
                raise FileNotFoundError('Dataset not found. Type the whole path correctly.')

            df = pd.read_csv(dataset)
            newDF = codeDataset(df)
            y_pred = expertSystem.predict(newDF)
            
            (p_valor, Cont) = expertSystem.testModel()
            print('('+ str(p_valor) + ',' + str(Cont) +')')
        elif option == '-ls':
            printAvailableScores()
        elif option == '-ld':
            loadFile()
        elif option == '--conf':
            try:
                controller, df, charIndex, tagIndex, testSize = config(sys.argv[2:6])
                checker.checkActionParameter(sys.argv[7])

                actionData = {}

                if sys.argv[8] == '--pscore':
                    checker.checkScoreParameter(sys.argv[8])
                    checker.checkNumSamplesParameter(sys.argv[9])

                    selectedScore = setScoreOption(sys.argv[8])
                    numSamples = sys.argv[10]

                    actionData['selectedScore'] = selectedScore
                    actionData['numSamples'] = numSamples
                elif sys.argv[8] == '--confusion':
                    checker.checkClassNamesParameter(sys.argv[8])
                    classNames = sys.argv[9]
                    actionData['classNames'] = classNames
                else:
                    raise CommandLineException('Action not found')

                configData = {
                    'df': df,
                    'charIndex': charIndex,
                    'tagIndex': tagIndex,
                    'testSize': testSize,
                }
                
                action(controller, sys.argv[8], configData, actionData)
                
            
            except ApplicationException as ie:
                raise CommandLineException('Error with config parameters.\n'+ ie.message +'\nFor any doubt, check help command.')
            '''

    except (ApplicationException) as e:
        return 'Script error: ' + str(e.message)

def loadFile():
    pass


def config(argv):
    try:
        checker.checkClassifierParameter(argv[0])
        controller = ExpertSystem()       
        setClassifierOption(controller, argv[0])
        checker.checkDatasetParameter(argv[1])
        df = pd.read_csv(argv[1])
        checker.checkCharIndexParameter(argv[2])
        charIndex = argv[2]
        checker.checkTagIndexParameter(argv[3])
        tagIndex = argv[3]
        checker.checkTestSizeParameter(argv[4])
        testSize = argv[4]

        return (controller, df, charIndex, tagIndex, testSize)
    except (FormatException, ScoreNotFoundException, ClassifierNotFoundException, IndexError, FileNotFoundError) as e:
        raise ApplicationException(str(e))

def action(controller, actionCommand, configData, actionData):

    actionCommands = [
        '--pscore',
        '--confusion',
        '--predict'
    ]

    if actionCommand in actionCommands:
        controller.divideData(dataframe=configData['df'], 
                              xCols=configData['charIndex'], 
                              yCols=configData['tagIndex'], 
                              testSize=configData['testSize'], 
                              randomState=1)
        controller.fitData()

        if actionCommand == '--pscore':
            y_pred = controller.predict()
            pScore, Cont = controller.getPScore(actionData['selectedScore'], 
                                                y_pred, 
                                                actionData['numSamples'])
            print('(P-Score, Cont) = (' + pScore + ',' + Cont + ')')
        elif actionCommand == '--confusion':
            confusionMatrix = controller.createConfusionMatrix(actionData['classNames'])
            print(confusionMatrix)
        elif actionCommand == '--predict':
            y_pred = controller.predict()
            print(y_pred)
        else:
            raise CommandLineException()
    else:
        raise CommandLineException()


def setScoreOption(score):
    if score == '-ps':
        selectedScore = constants.PRECISION_SCORE
    elif score == '-rs':
        selectedScore = constants.RECALL_SCORE
    elif score == '-as':
        selectedScore = constants.ACCURACY_SCORE
    elif score == '-fones':
        selectedScore = constants.F1_SCORE
    else:
        raise ScoreNotFoundException()
    
    return selectedScore

def setClassifierOption(controller, classifier):
    if classifier == '-nv':
        controller.setClassifier(constants.NAIVE_BAYES)
    else:
        raise ClassifierNotFoundException()
        

def getHelpMessage():
    helpMessage = 'main.py [OPTION|CONF] [CLASSIFIER] [FILE [CHARINDEX] [TAGINDEX] [TESTSIZE]] [ACTION] [SCORE|CLASSNAMES] [NUMSAMPLES]\n\n'

    helpMessage += 'OPTION\n'
    helpMessage += '\t-h\tPrints the help message for the script.\n'
    helpMessage += '\t-l\tList the available classifiers.\n'
    helpMessage += '\t-ls\tList the available scores.\n'
    helpMessage += '\t-ld\tLoad a config file.\n'
    helpMessage += '\n'
    helpMessage += 'CONF\n'
    helpMessage += '\t--conf\tConfigure parameters for the classification.\n'
    helpMessage += '\t\tThe following parameters need to be configured: [CLASSIFIER] [FILE [CHARINDEX] [TAGINDEX] [TESTSIZE]]\n'
    helpMessage += 'CLASSIFIER\n'
    helpMessage += '\t-nv\tSet a Gaussian Naive Bayes classifier.\n'
    helpMessage += '\n'
    helpMessage += 'FILE\n'
    helpMessage += '\tDataset to be loaded for the classification\n'
    helpMessage += 'CHARINDEX\n'    
    helpMessage += '\tIndex of the columns with the characteristics of the dataset\n'
    helpMessage += 'TAGINDEX\n'
    helpMessage += '\tIndex of the column with the tags of the dataset\n'
    helpMessage += '\n'
    helpMessage += 'TESTSIZE\n'
    helpMessage += '\tPortion of the dataset in order to separate the train set from the test set.\n'
    helpMessage += '\tFor instance, if the given value is 25, the 25% of the dataset will be used for testing, the remaining 75% wil be for training.\n'
    helpMessage += 'ACTION\n'
    helpMessage += '\t--predict\tMake prediction according to the given parameters. It does not require extra parameters, as the other actions\n'
    helpMessage += '\t--pscore\tCalculate the P-Score from a classification of a dataset.\n'
    helpMessage += '\t\t\tThe parameters to set are: [SCORE] [NUMSAMPLES]\n'
    helpMessage += '\t--confusion\tCreate a confusion matrix from the obtained training.\n'
    helpMessage += '\t\t\tThe parameters to set are: [CLASSNAMES]\n'
    helpMessage += 'SCORE\n'
    helpMessage += '\t-ps\tSelect Precision Score.\n'
    helpMessage += '\t-rs\tSelect Recall Score.\n'
    helpMessage += '\t-as\tSelect Accuracy Score.\n'
    helpMessage += '\t-fones\tSelect F1 Score.\n'
    helpMessage += 'NUMSAMPLES.\n'
    helpMessage += '\tNumber of samples that will be used to get the P-Score.\n'
    helpMessage += 'CLASSNAMES\n'
    helpMessage += '\tColumn from the datatset to be set as the classname to divide the data\n'


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
        config.update(configLoaded)

    pickle.dump(config, open(filename, 'wb'))

    print('Model type correctly set: ' + modelType)

def getScoreType(config):
    try:
        return config['scoreType']
    except Exception:
        return None

def checkErrors(config):
    if config is None:
        raise CommandLineException('System configuration not found.\n\n' + '\n'.join(constants.MODEL_TYPES) + '\n')

    if 'modelType' not in config:
        raise CommandLineException('Model type not found in the configuration. Possible values:\n\n' + '\n'.join(constants.MODEL_TYPES) + '\n')

    if 'scoreType' not in config:
        raise CommandLineException('Score type not found in the configuration. Possible values:\n\n' + '\n'.join(constants.SCORE_OPTIONS) + '\n')


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
        config = config.update(configLoaded)

    pickle.dump(config, open(filename, 'wb'))

    print('Score type correctly set: ' + scoreType)

def getConfigModelFilename(modelType):
    now = datetime.now()
    versionDateTime = now.strftime("%Y%m%d%H%M%S")
    filePath = constants.FILEPATH + modelType
    filename = filePath + '/' + 'model_' + modelType + '_' + versionDateTime + constants.MODEL_FILETYPE

    return (filePath, filename)

def getFileStats(filename):
    fileInfoStr = 'File: ' + filename + '\n'

    fileStats = os.stat(filename)
    mostRecentAccess = str(timedelta(seconds = fileStats.st_atime))
    mostRecentContentChange = str(timedelta(seconds = fileStats.st_atime))
    mostRecentMetadataChange = str(timedelta(seconds = fileStats.st_atime))

    fileInfoStr += 'File size (Bytes): ' + str(fileStats.st_size) + ' bytes\n'
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
    

def printAvailableScores():
    availableScoresStr = '\tShortcut\tScore\n\n'

    availableScores = {
        '-ps'   : 'Precision Score',
        '-rs'   : 'Recall Score',
        '-as'   : 'Accuracy Score',
        '-fones': 'F1 Score'
    }

    for shortcut in availableScores:
        availableScoresStr += '\t'+ str(shortcut) +'\t\t'+ str(availableScores[shortcut]) +'\n'
        
    print(availableScoresStr)

if __name__ == "__main__":
    sys.exit(main())
