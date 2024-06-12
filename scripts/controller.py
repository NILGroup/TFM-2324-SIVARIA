import pandas as pd
import os
import numpy as np
import matplotlib.pyplot as plt
# Own created classes and modules
import constants
from decoder import Decoder
from checker import Checker
from fileManager import FileManager
from configurator import Configurator
from expertSystem import ExpertSystem
from exceptions.ApplicationException import ApplicationException
from exceptions.CommandLineException import CommandLineException
from exceptions.ModelNotFoundException import ModelNotFoundException
from exceptions.PredictionErrorException import PredictionErrorException
from exceptions.ModelTrainingException import ModelTrainingException


class Controller():
    
    def execute(self, args):
        try:
            if(len(args) <= 1):
                raise CommandLineException('Not enough parameters.\n\n' + self.getHelpMessage())
            
            option = args[1]
            
            if option == '-h':
                return self.getHelpMessage()
            elif option =='-mt':
                config = Configurator()
                
                if len(args) <= 2:
                    modelType = config.getModelType()
                    if modelType is None:
                        modelType = 'None'
                else:
                    modelType = args[2]
                    config.setModelType(modelType)

                config.saveConfig()

                output = 'Model type of the Expert System: ' + str(modelType) + '\n'
                output += 'Possible values: [\n' + ',\n'.join(constants.MODEL_TYPES) + '\n]'

                return output
            
            elif option =='-st':
                config = Configurator()

                if len(args) <= 2:
                    scoreType = config.getScoreType()
                    if scoreType is None:
                        scoreType = 'None'
                else:
                    scoreType = args[2]
                    config.setScoreType(scoreType)
                
                config.saveConfig()

                output = 'Score type of the Expert System: ' + str(scoreType) + '\n'
                output += 'Possible values: [\n' + ',\n'.join(constants.SCORE_OPTIONS) + '\n]'

                return output
            elif option == '-lst':
                fileManager = FileManager()

                output = {}
                total = 0
                if len(args) <= 2:
                    for modelType in constants.MODEL_TYPES:
                        totalFilesDir, files = fileManager.getFilesDir(modelType)
                        total += totalFilesDir
                        output[modelType] = files
                        
                else:
                    modelType = args[2]
                    total, files = fileManager.getFilesDir(modelType)
                    output[modelType] = files

                output['total'] = total
                return output
            elif option == '-fs':
                fileManager = FileManager()

                if len(args) <= 2:
                    raise CommandLineException('Filename not provided.\n\n' + self.getHelpMessage())

                filename = args[2]
                
                Checker.checkSAVParameter(filename)
                
                output = {}

                modelType = filename.split('_')[1]
                output[modelType] = []
                output[modelType].append(fileManager.getFileStats(constants.FILEPATH + modelType + '/' + filename))

                return output
            elif option == '-rm':
                fileManager = FileManager()

                if len(args) <= 2:
                    raise CommandLineException('Filename not provided.\n\n' + self.getHelpMessage())
                
                filename = args[2]
                
                Checker.checkSAVParameter(filename)

                fileManager.removeSaveFile(filename)

                return 'File removed successfully'
            elif option =='-t':
                expertSystem = ExpertSystem()
                config = Configurator()
                fileManager = FileManager()

                if len(args) <= 2:
                    raise CommandLineException('Dataset not specified.\n\n' + self.getHelpMessage())

                dataset = args[2]

                Checker.checkConfig(config)
                Checker.checkDatasetParameter(dataset)
                
                modelType = config.getModelType()
                scoreType = config.getScoreType()

                if os.path.exists(dataset) == False:
                    raise FileNotFoundError('Dataset not found. Type the whole path correctly.\n\n' + self.getHelpMessage())

                # Code Dataset
                df = pd.read_csv(dataset)
                newDF = Decoder.codeDataset(df)

                expertSystem.setModelType(modelType)
                expertSystem.setScoreOption(scoreType)

                mostRecentFilename = fileManager.getMostRecentFile(modelType)
                
                if mostRecentFilename is not None:
                    print(fileManager.getFileInfo(mostRecentFilename))

                # Building Model
                expertSystem.buildModel(mostRecentFilename)
                
                # Training Model
                print('Training the model...') 
                X_train, X_test, y_train, y_test = expertSystem.divideDatasetTrainingTesting(newDF)
                classNames = np.unique(newDF['Desenlace'].to_numpy())

                try:
                    modelForTest = expertSystem.trainModel(X_train, y_train, classNames)
                except Exception:
                    raise ModelTrainingException('Error during model training.')
                
                print('Model trained successfully\n')

                y_pred = expertSystem.predict(X_test)
                cm = expertSystem.getConfusionMatrix(y_test, y_pred, classNames)
                # Plot Confusion Matrix
                '''
                print('Showing confusion matrix...')
                disp = expertSystem.getConfusionMatrixDisplay(cm, classNames)
                disp.plot()
                plt.show()
                '''

                # Testing Model
                print('Testing trained model...')
                (p_valor, Cont) = expertSystem.testModel(modelForTest, y_pred, X_train, y_train, X_test, y_test)
                print('Model tested successfully')
                #print('('+ str(p_valor) + ',' + str(Cont) +')')

                # Saving model
                print('Saving model...')
                filePath, filename = fileManager.getConfigModelFilename(expertSystem.getModelType())

                expertSystem.saveModel(filePath, filename)
                print('Model saved\n')

                print(fileManager.getFileInfo(filename))

                # Preparing data to return 
                cm = expertSystem.getConfusionMatrix(y_test, y_pred, classNames, False)
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
                expertSystem = ExpertSystem()
                config = Configurator()
                fileManager = FileManager()
                
                if len(args) <= 2:
                    raise CommandLineException('Dataset not specified.\n\n' + self.getHelpMessage())
                
                dataset = args[2]
                
                Checker.checkConfig(config)
                Checker.checkDatasetParameter(dataset)

                modelType = config.getModelType()
                print('Model type saved in configuration: ' + modelType + '\n')

                if os.path.exists(dataset) == False:
                    raise FileNotFoundError('Dataset not found. Type the whole path correctly.\n\n' + self.getHelpMessage())
                
                df = pd.read_csv(dataset)
                newDF = Decoder.codeDataset(df)

                expertSystem.setModelType(modelType)
                
                mostRecentFilename = fileManager.getMostRecentFile(modelType)
                
                if mostRecentFilename is not None:
                    print(fileManager.getFileInfo(mostRecentFilename))
                else:
                    raise ModelNotFoundException('Save model file of ' + modelType + ' model not found.')

                expertSystem.buildModel(mostRecentFilename)

                if 'Desenlace' in newDF.columns:
                    newDF = newDF.drop('Desenlace', axis=1)

                try:
                    y_pred = expertSystem.predict(newDF.values)
                except Exception:
                    raise PredictionErrorException('Error during prediction.')
                
                return y_pred
            
            else:
                raise CommandLineException('Some parameters that do not exist were introduced.\n\n' + self.getHelpMessage())

        except (ApplicationException, FileNotFoundError, ValueError) as e:
            errorTitle = 'Script error: '
            if isinstance(e, ApplicationException):
                log = errorTitle + str(e.message)
            else:
                log = errorTitle + str(e)
            
            return log

    def getHelpMessage(self):
        helpMessage = 'main.py [OPTION] [DATASET|MODEL TYPE|MODEL SAVE FILENAME]\n\n'

        helpMessage += 'OPTION\n'
        helpMessage += '\t-h\tPrints the help message.\n\n'
        helpMessage += '\t-mt\tPrint the current model type selected.\n'
        helpMessage += '\t\tIf the following parameter [MODEL TYPE] is a model type, \n'
        helpMessage += '\t\tthe configuration will be modified to this new model type.\n'
        helpMessage += '\t\tThe possible values are: ' + ', '.join(constants.MODEL_TYPES) + '\n\n'
        helpMessage += '\t\tExample: python main.py -mt autoinforme\n\n'
        helpMessage += '\t-st\tPrint the current score type selected. \n'
        helpMessage += '\t\tIf the following parameter [MODEL TYPE] is a score type, \n'
        helpMessage += '\t\tthe configuration will be modified to this new score type.\n'
        helpMessage += '\t\tThe possible values are: ' + ', '.join(constants.SCORE_OPTIONS) + '\n\n'
        helpMessage += '\t\tExample: python main.py -st accuracy\n\n'
        helpMessage += '\t-lst\tReturn an object of list of save files. If a model type [MODEL TYPE] is provided,\n'
        helpMessage += '\t\tit returns all the save files of that model.\n'
        helpMessage += '\t\tOtherwise, it returns an object with all the save files of all model types.\n\n'
        helpMessage += '\t\tExample: python main.py -lst autoinforme\n\n'
        helpMessage += '\t-fs\tReturn an object with the stats of a given save file name in [MODEL SAVE FILENAME].\n\n'
        helpMessage += '\t\tExample: python main.py -fs model_autoinforme_20240607181100.sav\n\n'
        helpMessage += '\t-rm\tRemove a save filename of a model given its name in [MODEL SAVE FILENAME].\n\n'
        helpMessage += '\t\tExample: python main.py -rm model_autoinforme_20240607181100.sav\n\n'
        helpMessage += '\t-t\tTrain a model, that can be "autoinforme", "familia" and "profesional" given a dataset [DATASET].\n'
        helpMessage += '\t\tIn order to train the model correctly, a model type and a score type previously.\n'
        helpMessage += '\t\tIf not, the training will not work.\n\n'
        helpMessage += '\t\tExample: python main.py -t datasets/autoinforme/dataset1.csv\n\n'
        helpMessage += '\t-p\tReturn a list of predicted results given a dataset [DATASET].\n\n'
        helpMessage += '\t\tExample: python main.py -p datasets/autoinforme/dataset5.csv\n\n'

        return helpMessage