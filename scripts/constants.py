# Classifiers
NAIVE_BAYES = 'naive_bayes'

# Model Types
MODEL_TYPES = [
    'autoinforme',
    'familia',
    'profesional'
]

SCORE_OPTIONS = [
    'accuracy',
    'precision',
    'recall',
    'f1_score'
]

ACTION_MODES = [
    'prod',
    'train'
]

FILEPATH = 'configFiles/'
CONFIG_FILENAME = 'configModel'
CONFIG_FILETYPE = '.sav'
MODEL_FILETYPE = '.sav'

TESTING_DATASET_SIZE = 0.75

# Scores
PRECISION_SCORE = 'precision'
ACCURACY_SCORE = 'accuracy'
F1_SCORE = 'f1'
RECALL_SCORE = 'recall'

BAYES_NETWORK_STATE_NAMES = {
    'Curso':['COLEGIO', 'ESO', 'BACHILLERATO', 'UNIVERSIDAD', 'FORMACION PROFESIONAL'], 
    'Sexo asignado':['HOMBRE', 'MUJER', 'OTRO'], 
    'Transgenero':['SI','NO','NO ESTOY SEGURO DE SER TRANS', 'NO ESTOY SEGURO DE LO QUE SE PREGUNTA'], 
    'Edad':['MENOR DE 12', '12', '13', '14', '15', '16', '17', '18', '19', '20', '21', 'MAYOR DE 21'], 
    'Situacion laboral padre':['NO TRABAJA', 'TRABAJA', 'PENSIONADO'], 
    'Situacion laboral madre': ['NO TRABAJA', 'TRABAJA', 'PENSIONADO'], 
    'Nivel profesional padre':['BAJO', 'MEDIO', 'ALTO'], 
    'Nivel profesional madre':['BAJO', 'MEDIO', 'ALTO'],
    'Nivel promedio del rendimiento academico':['INSUFICIENTE', 'SUFICIENTE', 'NOTABLE', 'SOBRESALIENTE', 'EXTRAORDINARIO'],
    'Nivel de autopercepcion masculina':['0','1','2','3','4','5','6'],
    'Nivel de autopercepcion femenina':['0','1','2','3','4','5','6'],
    'Nivel de heteropercepcion masculina':['0','1','2','3','4','5','6'],
    'Nivel de heteropercepcion femenina':['0','1','2','3','4','5','6'],
    'Altura':['MENOS DE 149', '150-159', '160-169','170-179','180-189','MAS DE 190'],
    'Peso':['MENOS DE 49', '50-59', '60-69','70-79','80-89','MAS DE 90'],
    'Tratamiento psiquiatrico previo':['SI','NO'],
    'Presenta enfermedad cronica':['SI','NO'],
    'Bullying victima':['SI','NO'],
    'Bullying perpetrador':['SI','NO'],
    'Cyberbullying victima':['SI','NO'],
    'Cyberbullying perpetrador':['SI','NO'],
    'Adiccion/abuso alcohol':['SI','NO'],
    'Adiccion/abuso sustancias':['SI','NO'],
    'Adiccion/abuso Internet':['SI','NO'],
    'Problemas interiorizados':['SI','NO'],
    'Problemas exteriorizados':['SI','NO'],
    'Problemas de contexto':['SI','NO'],
    'Problemas recursos psicologicos':['SI','NO'],
    'Percepcion de discriminacion':['SI','NO'],
    'Fuente de discriminacion':['EDAD','RAZA','DISCAPACIDAD','GENERO','ORIENTACION SEXUAL'],
    'Nivel de resistencia/resiliencia':['1','2','3','4','5'],
    'Nivel de regulacion positiva':['1','2','3','4','5'],
    'Nivel de regulacion negativa':['1','2','3','4','5'],
    'Atrapamiento interno':['SI','NO'],
    'Atrapamiento externo':['SI','NO'],
    'Nivel percibido de derrota o fracaso':['BAJO','MEDIO', 'ALTO'],
    'Sentido de pertenencia frustada':['SI','NO'],
    'Percepcion de ser una carga':['SI','NO'],
    'Autoeficiencia para el suicidio':['SI', 'NO'],
    'Madre adolescente':['SI', 'NO'],
    'Padre adolescente':['SI', 'NO'],
    'Padres divorciados':['SI', 'NO'],
    'Familia monoparental':['SI', 'NO'],
    'Tratamiento psicologico padre/madre':['SI', 'NO'],
    'Adiccion padre/madre':['SI', 'NO'],
    'Relaciones conflictivas hijo-padre/madre':['SI', 'NO'],
    'Familia reconstruida':['SI', 'NO'],
    'Busqueda informacion autolesion':['SI', 'NO'],
    'Compartir en RRSS pensamiento autolesion':['SI', 'NO'],
    'Peticion ayuda en Internet':['SI', 'NO'],
    'Contagio':['SI', 'NO'], 
    'Tener conocidos que comparten autolesion en Internet':['SI', 'NO'],
    'Via de contacto para RRSS':['SI', 'NO'],
    'Contacto informacion autolesion':['SI', 'NO'],
    'Denuncia autolesion Internet':['SI', 'NO'],
    'Aceptacion/rechazo parental':['ACEPTACION', 'RECHAZO'],
    'Control parental':['SI', 'NO'],
    'Situacion economica familiar precaria':['SI', 'NO'],
    'Estudios de la madre':['SI', 'NO'],
    'Estudios del padre':['SI', 'NO'],
    'Supervision parental insuficiente':['SI', 'NO'],
    'Maltrato al adolescente':['SI', 'NO'],
    'Duelo':['SI', 'NO'],
    'Ingreso familiar mensual':['MENOS DE 499', '500-999','1000-1499','2000-2499','MAS DE 2500'],
    'Desenlace':['COMUNICACION', 'DESEO','IDEACION','PLANIFICACION','INTENCION','FINALIDAD']
}