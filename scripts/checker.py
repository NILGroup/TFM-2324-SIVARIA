from exceptions.FormatException import FormatException
from exceptions.CommandLineException import CommandLineException
import constants

class Checker(object):
    
    @staticmethod
    def checkIntValue(value):
        if value is None:
            return False
        
        try:
            int_value = int(value)
            return True
        except ValueError:
            return False
    
    @staticmethod    
    def checkStrValue(value):
        return isinstance(value, str) and value is not None
    
    @staticmethod
    def checkFloatValue(value):
        if value is None:
            return False
        
        try:
            float_value = float(value)
            return True
        except ValueError:
            return False
    
    @staticmethod
    def checkCSVValue(value):
        if value is None:
            return False
        if isinstance(value, str):
            if value.endswith('.csv'):
                return True
        return False
    
    @staticmethod
    def checkSAVValue(value):
        if value is None:
            return False
        if isinstance(value, str):
            if value.endswith('.sav'):
                return True
        return False
    
    @staticmethod
    def checkClassifierParameter(argument):
        if Checker.checkStrValue(argument) == False:
            raise FormatException('Format error in the classifier parameter. A string is expected.')
    
    @staticmethod
    def checkScoreParameter(argument):
        if Checker.checkStrValue(argument) == False:
            raise FormatException('Format error in the score parameter. A string is expected.')
    
    @staticmethod
    def checkDatasetParameter(argument):
        if Checker.checkCSVValue(argument) == False:
            raise FormatException('Format error in the dataset parameter. A csv file is expected.')
        
    @staticmethod
    def checkSAVParameter(argument):
        if Checker.checkSAVValue(argument) == False:
            raise FormatException('Format error in the sav file parameter. A sav file is expected.')
    
    @staticmethod    
    def checkCharIndexParameter(argument):
        if Checker.checkIntValue(argument) == False:
            raise FormatException('Format error in the tagIndex parameter. An integer is expected.')
    
    @staticmethod
    def checkTagIndexParameter(argument):
        if Checker.checkStrValue(argument) == False:
            raise FormatException('Format error in the score parameter. A string is expected.')
    
    @staticmethod  
    def checkActionParameter(argument):
        if Checker.checkStrValue(argument) == False:
            raise FormatException('Format error in the action parameter. A string is expected.')
    
    @staticmethod
    def checkClassNamesParameter(argument):
        if Checker.checkStrValue(argument) == False:
            raise FormatException('Format error in the classNames parameter. A string is expected.')
    
    @staticmethod    
    def checkTestSizeParameter(argument):
        if Checker.checkFloatValue(argument) == False:
            raise FormatException('Format error in the testsize parameter. An integer or decimal is expected.')
    
    @staticmethod
    def checkNumSamplesParameter(argument):
        if Checker.checkIntValue(argument) == False:
            raise FormatException('Format error in the number of samples parameter. An integer or decimal is expected.')

    @staticmethod
    def checkConfig(config):
        if config is None:
            raise CommandLineException('System configuration not found.\n')

        if config.getModelType() is None:
            raise CommandLineException('Model type not found in the configuration. Possible values: [\n' + ',\n'.join(constants.MODEL_TYPES) + '\n]')
        '''
        if config.getScoreType() is None:
            raise CommandLineException('Score type not found in the configuration. Possible values: [\n' + ',\n'.join(constants.SCORE_OPTIONS) + '\n]')
        '''