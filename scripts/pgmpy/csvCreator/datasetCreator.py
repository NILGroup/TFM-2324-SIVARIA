import csv
import sys
import random
import constants

def main():            
    # Add column names in this writerow
    for i in range(5): 
        with open('datasets/autoinforme/dataset' + str(i + 1) + '.csv', 'w', newline='') as file:
            writer = csv.DictWriter(file, fieldnames=constants.FIELDS)
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
                singleData['Nivel promedio del rendimiento academico'] = constants.ACADEMIC_PERFORMANCES[random.randint(0, len(constants.ACADEMIC_PERFORMANCES) - 1)]
                singleData['Situacion laboral madre'] = constants.JOB_SITUATIONS[random.randint(0, len(constants.JOB_SITUATIONS) - 1)]
                singleData['Situacion laboral padre'] = constants.JOB_SITUATIONS[random.randint(0, len(constants.JOB_SITUATIONS) - 1)]
                singleData['Nivel profesional madre'] = constants.LEVELS[random.randint(0, len(constants.LEVELS) - 1)]
                singleData['Nivel profesional padre'] = constants.LEVELS[random.randint(0, len(constants.LEVELS) - 1)]
                singleData['Nivel de autopercepcion masculina'] = random.randint(0, 6)
                singleData['Nivel de autopercepcion femenina'] = random.randint(0, 6)
                singleData['Nivel de heteropercepcion masculina'] = random.randint(0, 6)
                singleData['Nivel de heteropercepcion femenina'] = random.randint(0, 6)
                
                singleData['Tratamiento psiquiatrico previo'] = constants.YES_NO_ANSWERS[random.randint(0,len(constants.YES_NO_ANSWERS) - 1)] 
                singleData['Presenta enfermedad cronica'] = constants.YES_NO_ANSWERS[random.randint(0,len(constants.YES_NO_ANSWERS) - 1)]
                
                singleData['Bullying victima'] = constants.YES_NO_ANSWERS[random.randint(0,len(constants.YES_NO_ANSWERS) - 1)]
                singleData['Bullying perpetrador'] = constants.YES_NO_ANSWERS[random.randint(0,len(constants.YES_NO_ANSWERS) - 1)]
                singleData['Cyberbullying victima'] = constants.YES_NO_ANSWERS[random.randint(0,len(constants.YES_NO_ANSWERS) - 1)]
                singleData['Cyberbullying perpetrador'] = constants.YES_NO_ANSWERS[random.randint(0,len(constants.YES_NO_ANSWERS) - 1)]
                
                singleData['Adiccion/abuso alcohol'] = constants.YES_NO_ANSWERS[random.randint(0,len(constants.YES_NO_ANSWERS) - 1)]
                singleData['Adiccion/abuso sustancias'] = constants.YES_NO_ANSWERS[random.randint(0,len(constants.YES_NO_ANSWERS) - 1)]
                singleData['Adiccion/abuso Internet'] = constants.YES_NO_ANSWERS[random.randint(0,len(constants.YES_NO_ANSWERS) - 1)]
                
                singleData['Problemas interiorizados'] = constants.YES_NO_ANSWERS[random.randint(0,len(constants.YES_NO_ANSWERS) - 1)]
                singleData['Problemas exteriorizados'] = constants.YES_NO_ANSWERS[random.randint(0,len(constants.YES_NO_ANSWERS) - 1)]
                singleData['Problemas de contexto'] = constants.YES_NO_ANSWERS[random.randint(0,len(constants.YES_NO_ANSWERS) - 1)]
                singleData['Problemas recursos psicologicos'] = constants.YES_NO_ANSWERS[random.randint(0,len(constants.YES_NO_ANSWERS) - 1)]
                
                singleData['Percepcion de discriminacion'] = constants.YES_NO_ANSWERS[random.randint(0,len(constants.YES_NO_ANSWERS) - 1)]
                singleData['Fuente de discriminacion'] = constants.DISCRIMINATION_SOURCE[random.randint(0,len(constants.DISCRIMINATION_SOURCE) - 1)]

                singleData['Nivel de resistencia/resiliencia'] = random.randint(1, 5)
                singleData['Nivel de regulacion positiva'] = random.randint(1, 5)
                singleData['Nivel de regulacion negativa'] = random.randint(1, 5)

                singleData['Atrapamiento interno'] = constants.YES_NO_ANSWERS[random.randint(0,len(constants.YES_NO_ANSWERS) - 1)]
                singleData['Atrapamiento externo'] = constants.YES_NO_ANSWERS[random.randint(0,len(constants.YES_NO_ANSWERS) - 1)]
                singleData['Nivel percibido de derrota o fracaso'] = constants.LEVELS[random.randint(0,len(constants.LEVELS) - 1)]
                singleData['Sentido de pertenencia frustada'] = constants.YES_NO_ANSWERS[random.randint(0,len(constants.YES_NO_ANSWERS) - 1)]
                singleData['Percepcion de ser una carga'] = constants.YES_NO_ANSWERS[random.randint(0,len(constants.YES_NO_ANSWERS) - 1)]
                singleData['Autoeficiencia para el suicidio'] = constants.YES_NO_ANSWERS[random.randint(0,len(constants.YES_NO_ANSWERS) - 1)]

                singleData['Madre adolescente'] = constants.YES_NO_ANSWERS[random.randint(0,len(constants.YES_NO_ANSWERS) - 1)]
                singleData['Padre adolescente'] = constants.YES_NO_ANSWERS[random.randint(0,len(constants.YES_NO_ANSWERS) - 1)]
                singleData['Padres divorciados'] = constants.YES_NO_ANSWERS[random.randint(0,len(constants.YES_NO_ANSWERS) - 1)]
                singleData['Familia monoparental'] = constants.YES_NO_ANSWERS[random.randint(0,len(constants.YES_NO_ANSWERS) - 1)]
                singleData['Tratamiento psicologico padre/madre'] = constants.YES_NO_ANSWERS[random.randint(0,len(constants.YES_NO_ANSWERS) - 1)]
                singleData['Adiccion padre/madre'] = constants.YES_NO_ANSWERS[random.randint(0,len(constants.YES_NO_ANSWERS) - 1)]
                singleData['Relaciones conflictivas hijo-padre/madre'] = constants.YES_NO_ANSWERS[random.randint(0,len(constants.YES_NO_ANSWERS) - 1)]
                singleData['Familia reconstruida'] = constants.YES_NO_ANSWERS[random.randint(0,len(constants.YES_NO_ANSWERS) - 1)]

                singleData['Busqueda informacion autolesion'] = constants.YES_NO_ANSWERS[random.randint(0,len(constants.YES_NO_ANSWERS) - 1)]
                singleData['Compartir en RRSS pensamiento autolesion'] = constants.YES_NO_ANSWERS[random.randint(0,len(constants.YES_NO_ANSWERS) - 1)]
                singleData['Peticion ayuda en Internet'] = constants.YES_NO_ANSWERS[random.randint(0,len(constants.YES_NO_ANSWERS) - 1)]
                singleData['Contagio'] = constants.YES_NO_ANSWERS[random.randint(0,len(constants.YES_NO_ANSWERS) - 1)]
                singleData['Tener conocidos que comparten autolesion en Internet'] = constants.YES_NO_ANSWERS[random.randint(0,len(constants.YES_NO_ANSWERS) - 1)]
                singleData['Via de contacto para RRSS'] = constants.YES_NO_ANSWERS[random.randint(0,len(constants.YES_NO_ANSWERS) - 1)]
                singleData['Contacto informacion autolesion'] = constants.YES_NO_ANSWERS[random.randint(0,len(constants.YES_NO_ANSWERS) - 1)]
                singleData['Denuncia autolesion Internet'] = constants.YES_NO_ANSWERS[random.randint(0,len(constants.YES_NO_ANSWERS) - 1)]

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

