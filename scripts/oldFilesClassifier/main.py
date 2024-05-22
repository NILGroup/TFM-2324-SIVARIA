import sys
from scripts.expertSystem import ExpertSystem
from sklearn.datasets import load_iris
import pandas as pd
from exceptions.ClassifierNotFoundException import ClassifierNotFoundException
from exceptions.ApplicationException import ApplicationException
from exceptions.CommandLineException import CommandLineException
from exceptions.ScoreNotFoundException import ScoreNotFoundException
from exceptions.FormatException import FormatException
import checker
import constants

def main():
    try:
        if(len(sys.argv) <= 1):
            raise CommandLineException('Not enough parameters.\n\n' + getHelpMessage())
             
        option = sys.argv[1]

        if option == '-h':
            print(getHelpMessage())
        elif option =='-l':
            printAvailableClassifiers()
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


                '''
                controller.divideData(dataframe=df, xCols=charIndex, yCols=tagIndex, testSize=testSize, randomState=1)
                controller.fitData()
                controller.createConfusionMatrix(classNames)

                y_pred = controller.predict()
                controller.getPScore(selectedScore, y_pred, numSamples)
                '''

                configData = {
                    'df': df,
                    'charIndex': charIndex,
                    'tagIndex': tagIndex,
                    'testSize': testSize,
                }
                
                action(controller, sys.argv[8], configData, actionData)
            
            except ApplicationException as ie:
                raise CommandLineException('Error with config parameters.\n'+ ie.message +'\nFor any doubt, check help command.')
        else:
            raise CommandLineException('Non-existing parameter(s) inserted.\n\n' + getHelpMessage())

    except (ApplicationException) as e:
        return 'Error in the script! ' + str(e.message)

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

def printAvailableClassifiers():
    availableClassifiersStr = '\tShortcut\tClassifier\n\n'

    availableClassifiers = {
        '-nv': 'GaussianNB'
    }

    for shortcut in availableClassifiers:
        availableClassifiersStr += '\t'+ str(shortcut) +'\t\t'+ str(availableClassifiers[shortcut]) +'\n'
    '''
    from sklearn.utils import all_estimators

    estimators = all_estimators()

    for name, class_ in estimators:
        if hasattr(class_, 'predict_proba'):
            print(name)
            '''

    print(availableClassifiersStr)

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
