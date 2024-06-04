from exceptions.FormatException import FormatException

def checkIntValue(value):
    if value is None:
        return False
    
    try:
        int_value = int(value)
        return True
    except ValueError:
        return False
    
def checkStrValue(value):
    return isinstance(value, str) and value is not None

def checkFloatValue(value):
    if value is None:
        return False
    
    try:
        float_value = float(value)
        return True
    except ValueError:
        return False

def checkCSVValue(value):
    if value is None:
        return False
    if isinstance(value, str):
        if value.endswith('.csv'):
            return True
    return False


def checkClassifierParameter(argument):
    if checkStrValue(argument) == False:
        raise FormatException('Format error in the classifier parameter. A string is expected.')

def checkScoreParameter(argument):
    if checkStrValue(argument) == False:
        raise FormatException('Format error in the score parameter. A string is expected.')

def checkDatasetParameter(argument):
    if checkCSVValue(argument) == False:
        raise FormatException('Format error in the dataset parameter. A csv file is expected.')
    
def checkCharIndexParameter(argument):
    if checkIntValue(argument) == False:
        raise FormatException('Format error in the tagIndex parameter. An integer is expected.')
    
def checkTagIndexParameter(argument):
    if checkStrValue(argument) == False:
        raise FormatException('Format error in the score parameter. A string is expected.')
    
def checkActionParameter(argument):
    if checkStrValue(argument) == False:
        raise FormatException('Format error in the action parameter. A string is expected.')

def checkClassNamesParameter(argument):
    if checkStrValue(argument) == False:
        raise FormatException('Format error in the classNames parameter. A string is expected.')
    
def checkTestSizeParameter(argument):
    if checkFloatValue(argument) == False:
        raise FormatException('Format error in the testsize parameter. An integer or decimal is expected.')
    
def checkNumSamplesParameter(argument):
    if checkIntValue(argument) == False:
        raise FormatException('Format error in the number of samples parameter. An integer or decimal is expected.')

    