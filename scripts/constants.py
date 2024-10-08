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

TESTING_DATASET_SIZE = 0.3

# Scores
PRECISION_SCORE = 'precision'
ACCURACY_SCORE = 'accuracy'
F1_SCORE = 'f1'
RECALL_SCORE = 'recall'

BAYES_NETWORK_STATE_NAMES = {
    'Curso':['PRIMARIA', 'ESO', 'BACHILLERATO', 'UNIVERSIDAD', 'FORMACION PROFESIONAL'], 
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

BAYES_NETWORK_STATE_NAMES_NEW_VERSION = {
    'Curso':['PRIMARIA', 'ESO', 'BACHILLERATO', 'UNIVERSIDAD', 'FORMACION PROFESIONAL', 'NINGUNO'], 
    'Sexo asignado':['HOMBRE', 'MUJER', 'OTRO'], 
    'Transgenero':['SI','NO','NO ESTOY SEGURO DE SER TRANS', 'NO ESTOY SEGURO DE LO QUE SE PREGUNTA'], 
    'Edad':['MENOR DE 12', '12', '13', '14', '15', '16', '17', '18', '19', '20', '21', 'MAYOR DE 21'], 
    'Situacion laboral padre':['NO TRABAJA', 'TRABAJA', 'PENSIONADO'], 
    'Situacion laboral madre': ['NO TRABAJA', 'TRABAJA', 'PENSIONADO'], 
    'Nivel profesional padre':['NINGUNO', 'PRIMARIA', 'ESO', 'BACHILLERATO', 'UNIVERSIDAD', 'FORMACION PROFESIONAL', 'LICENCIATURA'], 
    'Nivel profesional madre':['NINGUNO', 'PRIMARIA', 'ESO', 'BACHILLERATO', 'UNIVERSIDAD', 'FORMACION PROFESIONAL', 'LICENCIATURA'],
    'Nivel promedio del rendimiento academico':['INSUFICIENTE', 'SUFICIENTE', 'NOTABLE', 'SOBRESALIENTE', 'EXTRAORDINARIO'],
    'Nivel de autopercepcion masculina':['0','1','2','3','4','5','6'],
    'Nivel de autopercepcion femenina':['0','1','2','3','4','5','6'],
    'Nivel de percepcion masculina externa':['0','1','2','3','4','5','6'],
    'Nivel de percepcion femenina externa':['0','1','2','3','4','5','6'],
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
    'Fuente de discriminacion':['NINGUNO', 'EDAD', 'RAZA', 'DISCAPACIDAD', 'GENERO', 'ORIENTACION SEXUAL', 'RELIGION'],
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
    'Realizacion autolesion despues de ver contenido':['SI', 'NO'], 
    'Conocidos que comparten autolesion en Internet':['SI', 'NO'],
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
    'Desenlace':['NINGUNO','AUTOLESION','COMUNICACION', 'DESEO','IDEACION','PLANIFICACION','INTENCION']
}


BAYES_NETWORK_STATE_NAMES_NEW_VERSION_V2 = {
    'curso':['NINGUNO','PRIMARIA', 'ESO', 'BACHILLERATO', 'UNIVERSIDAD', 'OTRO'], 
    'sexo_asignado':['HOMBRE', 'MUJER', 'OTRO'], 
    'transgenero':['SI','NO','NO SE'], 
    'edad':['12-16', '17-18', '19-21'], 
    'situacion_laboral_padre':['NO TRABAJA', 'TRABAJA', 'PENSIONADO'], 
    'situacion_laboral_madre': ['NO TRABAJA', 'TRABAJA', 'PENSIONADO'], 
    'nivel_profesional_padre':['NINGUNO', 'BACHILLERATO', 'FORMACION PROFESIONAL', 'UNIVERSIDAD', 'OTRO'], 
    'nivel_profesional_madre':['NINGUNO', 'BACHILLERATO', 'FORMACION PROFESIONAL', 'UNIVERSIDAD', 'OTRO'],
    'nivel_promedio_academico':['INSUFICIENTE', 'SUFICIENTE', 'NOTABLE', 'SOBRESALIENTE', 'EXTRAORDINARIO'],
    'nivel_autopercepcion_masculina':['0','1','2','3','4','5','6'],
    'nivel_autopercepcion_femenina':['0','1','2','3','4','5','6'],
    'nivel_percepcion_masculina_externa':['0','1','2','3','4','5','6'],
    'nivel_percepcion_femenina_externa':['0','1','2','3','4','5','6'],
    'altura':['X<=149', '150-169','170-189','X>=190'],
    'peso':['X<=49', '50-69','70-89','X>=90'],
    'tratamiento_psiquiatrico_previo':['SI','NO'],
    'enfermedad_cronica':['SI','NO'],
    'bullying_victima':['SI','NO'],
    'bullying_perpetrador':['SI','NO'],
    'cyberbullying_victima':['SI','NO'],
    'cyberbullying_perpetrador':['SI','NO'],
    'adiccion_alcohol':['SI','NO'],
    'adiccion_sustancias':['SI','NO'],
    'adiccion_internet':['SI','NO'],
    'problemas_interiorizados':['SI','NO'],
    'problemas_exteriorizados':['SI','NO'],
    'problemas_contexto':['SI','NO'],
    'problemas_recursos_psicologicos':['SI','NO'],
    'fuente_discriminacion':['NINGUNO', 'GENERO', 'RAZA', 'ORIENTACION SEXUAL', 'OTRO'],
    'nivel_resiliencia':['1','2','3','4','5'],
    'nivel_regulacion_positiva':['1','2','3','4','5'],
    'nivel_regulacion_negativa':['1','2','3','4','5'],
    'atrapamiento_interno':['SI','NO'],
    'atrapamiento_externo':['SI','NO'],
    'nivel_percibido_fracaso':['BAJO','MEDIO', 'ALTO'],
    'sentido_pertenencia_frustrada':['SI','NO'],
    'percepcion_de_ser_una_carga':['SI','NO'],
    'autoeficiencia_para_el_suicidio':['SI', 'NO'],
    'madre_adolescente':['SI', 'NO'],
    'padre_adolescente':['SI', 'NO'],
    'padres_divorciados':['SI', 'NO'],
    'familia_monoparental':['SI', 'NO'],
    'tratamiento_psicologico_padre_madre':['SI', 'NO'],
    'adiccion_padre_madre':['SI', 'NO'],
    'relaciones_conflictivas_hijo_padre_madre':['SI', 'NO'],
    'familia_reconstruida':['SI', 'NO'],
    'busqueda_informacion_autolesion':['SI', 'NO'],
    'compartir_en_rrss_pensamiento_autolesion':['SI', 'NO'],
    'peticion_de_ayuda_en_internet':['SI', 'NO'],
    'realizacion_autolesion_despues_de_ver_contenido':['SI', 'NO'], 
    'tener_conocidos_que_comparten_autolesion_internet':['SI', 'NO'],
    'contacto_informacion_autolesion':['SI', 'NO'],
    'denuncia_autolesion_internet':['SI', 'NO'],
    'aceptacion_rechazo_parental':['ACEPTACION', 'RECHAZO'],
    'control_parental':['SI', 'NO'],
    'situacion_economica_precaria':['SI', 'NO'],
    'estudios_de_la_madre':['SI', 'NO'],
    'estudios_del_padre':['SI', 'NO'],
    'supervision_parental_insuficiente':['SI', 'NO'],
    'maltrato_al_adolescente':['SI', 'NO'],        
    'maltrato_a_la_pareja':['SI', 'NO'],
    'duelo':['SI', 'NO'],
    'ingreso_familiar_mensual':['X<=999', '1000-1499','1500-1999','X>=2000'],
    'desenlace':['NINGUNO','AUTOLESION','IDEACION','PLANIFICACION','INTENCION']
}