import csv
import sys
import random
import constants

def main():            
    # Add column names in this writerow
    for i in range(5): 
        with open('datasets/family/dataset' + str(i + 1) + '.csv', 'w', newline='') as file:
            writer = csv.DictWriter(file, fieldnames=constants.FAMILY_FIELDS)
            writer.writeheader()
            data = []
            for csvIndex in range(25):
                singleData = {}

                singleData['Index'] = (csvIndex + 1)
                singleData['Nombre'] = generateName()
                singleData['Edad'] = random.randint(10,25)
                singleData['Curso'] = generateCourse(singleData['Edad'])
                singleData['Peso'] = generateWeight()
                singleData['Altura'] = generateHeight()
                
                singleData['Sexo asignado'] = constants.GENDERS[random.randint(0,len(constants.GENDERS) - 1)]
                singleData['Transgenero'] = constants.TRASGENDER[random.randint(0,len(constants.TRASGENDER) - 1)] 
                
                singleData['Problemas interiorizados'] = constants.YES_NO_ANSWERS[random.randint(0,len(constants.YES_NO_ANSWERS) - 1)]
                singleData['Problemas exteriorizados'] = constants.YES_NO_ANSWERS[random.randint(0,len(constants.YES_NO_ANSWERS) - 1)]
                singleData['Problemas de contexto'] = constants.YES_NO_ANSWERS[random.randint(0,len(constants.YES_NO_ANSWERS) - 1)]
                singleData['Problemas recursos psicologicos'] = constants.YES_NO_ANSWERS[random.randint(0,len(constants.YES_NO_ANSWERS) - 1)]
                
                singleData['Madre adolescente'] = constants.YES_NO_ANSWERS[random.randint(0,len(constants.YES_NO_ANSWERS) - 1)]
                singleData['Padre adolescente'] = constants.YES_NO_ANSWERS[random.randint(0,len(constants.YES_NO_ANSWERS) - 1)]
                singleData['Padres divorciados'] = constants.YES_NO_ANSWERS[random.randint(0,len(constants.YES_NO_ANSWERS) - 1)]
                singleData['Familia monoparental'] = constants.YES_NO_ANSWERS[random.randint(0,len(constants.YES_NO_ANSWERS) - 1)]
                singleData['Tratamiento psicologico padre/madre'] = constants.YES_NO_ANSWERS[random.randint(0,len(constants.YES_NO_ANSWERS) - 1)]
                singleData['Adiccion padre/madre'] = constants.YES_NO_ANSWERS[random.randint(0,len(constants.YES_NO_ANSWERS) - 1)]
                singleData['Relaciones conflictivas hijo-padre/madre'] = constants.YES_NO_ANSWERS[random.randint(0,len(constants.YES_NO_ANSWERS) - 1)]
                singleData['Familia reconstruida'] = constants.YES_NO_ANSWERS[random.randint(0,len(constants.YES_NO_ANSWERS) - 1)]
                
                singleData['Aceptacion/rechazo parental'] = constants.PARENT_BEHAVIOR[random.randint(0,len(constants.PARENT_BEHAVIOR) - 1)]
                singleData['Control parental'] = constants.YES_NO_ANSWERS[random.randint(0,len(constants.YES_NO_ANSWERS) - 1)]

                singleData['Desenlace'] = constants.FINAL_RESULT[random.randint(0, len(constants.FINAL_RESULT) - 1)]

                data.append(singleData)

            writer.writerows(data)



def generateName():
    indexName = random.randint(0, len(constants.NAMES)-1)
    indexSurname = random.randint(0,len(constants.SURNAMES)-1)

    return (constants.NAMES[indexName] + ' ' + constants.SURNAMES[indexSurname])

def generateCourse(age):
    min = 0
    max = len(constants.COURSES)
    if age < 12:
        min = 0
        max = 0
    elif age == 12 or age == 13:
        min = 0
        max = 1
    elif age == 14 or age == 15:
        min = 1
        max = 1
    elif age == 16 or age == 17:
        min = 1
        max = 2
    elif age == 18:
        min = 2
        max = 4
    elif age >= 19:
        min = 3
        max = 4

    return constants.COURSES[random.randint(min,max)]

def generateWeight():
    decimal = round(random.random(), 2)
    integer = random.randint(50,90)

    return (integer + decimal)

def generateHeight():
    decimal = round(random.random(), 2)
    integer = random.randint(110,200)

    return (integer + decimal)

if __name__ == "__main__":
    sys.exit(main())

