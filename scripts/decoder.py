import constants
from pandas.api.types import is_string_dtype
from pandas.api.types import is_numeric_dtype
from sklearn.preprocessing import LabelEncoder
import numpy as np

class Decoder(object):

    @staticmethod
    def codeDataset(df, newFlag = 1):
        newDF = df

        # Eliminamos las columnas Index y Nombre, que no son necesarios
        newDF = newDF.drop(['id'], axis=1)

        if newFlag == 0:
            # Metemos los valores dentro de rangos
            newDF['Edad'] = newDF['Edad'].apply(Decoder.codeAgeColumn)
            newDF['Altura'] = newDF['Altura'].apply(Decoder.codeHeightColumn)
            newDF['Peso'] = newDF['Peso'].apply(Decoder.codeWeightColumn)

            # La columna 'Ingreso familiar mensual' sólo se encuentra en los datasets de profesionales
            if 'Ingreso familiar mensual' in newDF:
                newDF['Ingreso familiar mensual'] = newDF['Ingreso familiar mensual'].apply(Decoder.codeMonthlyFamiliarIncome)
        else:
            
            newDF = Decoder.removeWhiteSpaces(newDF)

            if 'edad' in newDF.columns and is_numeric_dtype(newDF['edad']):
                newDF['edad'] = newDF['edad'].apply(Decoder.newCodeAgeColumn)
            if 'altura' in newDF.columns and is_numeric_dtype(newDF['altura']):
                newDF['altura'] = newDF['altura'].apply(Decoder.newCodeHeightColumn)
            if 'peso' in newDF.columns and is_numeric_dtype(newDF['peso']):
                newDF['peso'] = newDF['peso'].apply(Decoder.newCodeWeightColumn)
        
        # Codificamos los valores de todas las columnas a vlores numéricos
        newDF = Decoder.changeValuesToNumeric(newDF, newFlag)

        return newDF

    @staticmethod
    def removeWhiteSpaces(df):
        
        for index, row in df.iterrows():
            for key in row.keys():
                if isinstance(row[key], str) and not row[key].isnumeric():
                    row[key] = row[key].strip()
                    if key == 'edad':
                        numeric_age = False
                    if  key == 'altura':
                        numeric_height = False
                    if  key == 'peso':
                        numeric_weight = False
        '''
        if numeric_age:
            df['edad'] = df.to_numeric(df['edad'])        
        if numeric_height:
            df['altura'] = df.to_numeric(df['altura'])
        if numeric_weight:
            df['peso'] = df.to_numeric(df['peso'])
        '''
        return df
    
    @staticmethod
    def codeAgeColumn(age):
        if age < 12:
            return 'MENOR DE 12'
        elif age > 21:
            return 'MAYOR DE 21'
        else:
            return str(age)
        
    @staticmethod
    def newCodeAgeColumn(age):
        if age >= 12 and age <= 16:
            return '12-16'
        elif age == 17 or age == 18:
            return '17-18'
        elif age >=19 and age <= 21:
            return '19-21'
        else:
            return False
    
    @staticmethod    
    def codeHeightColumn(height):
        if height <= 149:
            return "MENOS DE 149"
        elif height >= 150 or height < 160:
            return "150-159"
        elif height >= 160 or height < 170:
            return "160-169"
        elif height >= 170 or height < 180:
            return "170-179"
        elif height >= 180 or height < 190:
            return "180-189"
        elif height >= 190:
            return "MAS DE 190"
        else:
            return False
    
    @staticmethod    
    def newCodeHeightColumn(height):
        if height <= 149:
            return "x<=149".upper()
        elif height >= 150 or height < 170:
            return "150-169"
        elif height >= 170 or height < 190:
            return "180-189"
        elif height >= 190:
            return "x>=190".upper()
        else:
            return False
    
    @staticmethod    
    def codeWeightColumn(weight):
        if weight <= 49:
            return "MENOS DE 49"
        elif weight >= 50 or weight < 60:
            return "50-59"
        elif weight >= 60 or weight < 70:
            return "60-69"
        elif weight >= 70 or weight < 80:
            return "70-79"
        elif weight >= 80 or weight < 90:
            return "80-89"
        elif weight >= 90:
            return "MAS DE 90"
        else:
            return False
        
    @staticmethod    
    def newCodeWeightColumn(weight):
        if weight <= 49:
            return "x<=49".upper()
        elif weight >= 50 or weight < 70:
            return "50-69"
        elif weight >= 70 or weight < 90:
            return "80-89"
        elif weight >= 90:
            return "x>=90".upper()
        else:
            return False
    
    @staticmethod
    def codeMonthlyFamiliarIncome(income):
        if income <= 499:
            return "MENOS DE 499"
        elif income >= 500 or income < 1000:
            return "500-999"
        elif income >= 1000 or income < 1500:
            return "1000-1499"
        elif income >= 1500 or income < 2000:
            return "1500-1999"
        elif income >= 2000 or income < 2500:
            return "2000-2499"
        elif income >= 2500:
            return "MAS DE 2500"
        else:
            return False
    
    @staticmethod   
    def changeValuesToNumeric(df, newFlag = 1):
        '''
        label_encoder = LabelEncoder()
        for column in df.columns:
            if df[column].dtype == object:
                df[column] = label_encoder.fit_transform(df[column])
        '''
        '''
        state_names = constants.BAYES_NETWORK_STATE_NAMES_NEW_VERSION_V2 if newFlag == 1 else constants.BAYES_NETWORK_STATE_NAMES
        newData = df.apply(lambda x: x.astype(str).str.upper())

        label_encoder = LabelEncoder()
        '''
        '''
        for column in newData.columns:
            if column.lower() != 'desenlace' and df[column].dtype == object:
                print(state_names[column])
                print(np.unique(newData[column]))
                tmp1 = label_encoder.fit_transform(state_names[column])
                print(tmp1)
                tmp2 = label_encoder.fit_transform(newData[column])
                print(tmp2)
                items = constants.BAYES_NETWORK_STATE_NAMES_NEW_VERSION_V2[column]
                tmp3 = newData[column].apply(lambda x: items.index(x.strip()))
                #print(tmp1 == tmp2)
                print(tmp3)
        '''
        newData = df.apply(lambda x: x.astype(str).str.upper())

        items = constants.BAYES_NETWORK_STATE_NAMES_NEW_VERSION_V2.items() if newFlag == 1 else constants.BAYES_NETWORK_STATE_NAMES
        #print(items)
        for key, values in items:
            #print(key)
            if key in newData and key.lower() != 'desenlace':
                #print(newData[key][0].strip())
                #print(newData[key])
                #print(key)
                newData[key] = newData[key].apply(lambda x: values.index(x.strip()))

        #print(newData.get('bullying_victima'))
        return newData