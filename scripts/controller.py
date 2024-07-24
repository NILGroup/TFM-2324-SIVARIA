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
            
            #elif option =='-st':
                #config = Configurator()

                #if len(args) <= 2:
                    #scoreType = config.getScoreType()
                    #if scoreType is None:
                        #scoreType = 'None'
                #else:
                    #scoreType = args[2]
                    #config.setScoreType(scoreType)
                
                #config.saveConfig()

                #output = 'Score type of the Expert System: ' + str(scoreType) + '\n'
                #output += 'Possible values: [\n' + ',\n'.join(constants.SCORE_OPTIONS) + '\n]'

                #return output
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
                #scoreType = config.getScoreType()

                if os.path.exists(dataset) == False:
                    raise FileNotFoundError('Dataset not found. Type the whole path correctly.\n\n' + self.getHelpMessage())

                # Code Dataset
                df = pd.read_csv(dataset)
                newDF = Decoder.codeDataset(df)

                expertSystem.setModelType(modelType)
                #expertSystem.setScoreOption(scoreType)

                mostRecentFilename = fileManager.getMostRecentFile(modelType)
                
                if mostRecentFilename is not None:
                    print(fileManager.getFileInfo(mostRecentFilename))

                # Building Model
                expertSystem.buildModel(mostRecentFilename)
                
                # Training Model
                print('Training the model...') 
                X_train, X_test, y_train, y_test = expertSystem.divideDatasetTrainingTesting(newDF)
                str_desenlace = 'Desenlace' if 'Desenlace' in newDF.columns else 'desenlace'
                classNames = np.unique(newDF[str_desenlace].to_numpy())
                print(classNames)
                try:
                    #print(y_train)
                    modelForTest = expertSystem.trainModel(X_train, y_train, classNames)
                except Exception:
                    raise ModelTrainingException('Error during model training.')
                
                print('Model trained successfully\n')

                y_pred = expertSystem.predict(X_test)
                cm = expertSystem.getConfusionMatrix(y_test, y_pred, classNames)
                # Plot Confusion Matrix
                
                print('Showing confusion matrix...')
                disp = expertSystem.getConfusionMatrixDisplay(cm, classNames)
                disp.plot()
                plt.show()
                
                
                print(pd.DataFrame(data={'real': y_test, 'test': y_pred}))
                # Testing Model
                print('Testing trained model...')
                metrics = expertSystem.testModel(modelForTest, y_pred, X_train, y_train, X_test, y_test)
                print('Model tested successfully')
                #print('('+ str(p_valor) + ',' + str(Cont) +')')

                # Saving model
                print('Saving model...')
                filePath, filename = fileManager.getConfigModelFilename(expertSystem.getModelType())

                expertSystem.saveModel(filePath, filename, metrics)
                print('Model saved\n')

                print(fileManager.getFileInfo(filename))

                # Preparing data to return 
                cm = expertSystem.getConfusionMatrix(y_test, y_pred, classNames, False)
                #FP = cm.sum(axis=0) - np.diag(cm)  
                #FN = cm.sum(axis=1) - np.diag(cm)
                #TP = np.diag(cm)
                #TN = cm.sum() - (FP + FN + TP)
                TP, FP, TN, FN = self.__calculate_tp_fp_tn_fn(cm)
                
                result = {
                    'total': {
                        'TP': np.sum(TP),
                        'TN': np.sum(TN),
                        'FP': np.sum(FP),
                        'FN': np.sum(FN)
                    },
                    'per_class': {}
                    #'p_value_testing': {
                        #'p_valor':p_valor,
                        #'Cont': Cont
                    #}
                }
                '''
                index = 0
                for className in classNames:
                    classNameLower = className.lower()
                    predictionResults = {}
                    predictionResults['TP'] = TP[index]
                    predictionResults['TN'] = TN[index]
                    predictionResults['FP'] = FP[index]
                    predictionResults['FN'] = FN[index]
                    result['per_class'][classNameLower] = predictionResults
                    index += 1 
                '''
                for i, className in enumerate(classNames):
                    classnameLowered = className.lower()
                    result['per_class'][classnameLowered] = {
                        'TP': TP[i],
                        'FP': FP[i],
                        'TN': TN[i],
                        'FN': FN[i]
                    }

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

                if 'Desenlace' or 'desenlace' in newDF.columns:
                    str_desenlace = 'Desenlace' if 'Desenlace' in newDF.columns else 'desenlace'
                    newDF = newDF.drop(str_desenlace, axis=1)

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
    
    def __calculate_tp_fp_tn_fn(self, conf_matrix):
        num_classes = conf_matrix.shape[0]
        tp = np.diag(conf_matrix)
        fp = np.sum(conf_matrix, axis=0) - tp
        fn = np.sum(conf_matrix, axis=1) - tp
        tn = []
        for i in range(num_classes):
            temp_conf_matrix = np.delete(np.delete(conf_matrix, i, axis=0), i, axis=1)
            tn.append(np.sum(temp_conf_matrix))

        return tp, fp, tn, fn
