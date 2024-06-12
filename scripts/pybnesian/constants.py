TRAINING_PERCENTAGE_DATASET = 0.75

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

BAYES_NETWORK_VARIABLES_AUTOINFORME = [
    'Curso', 
    'Sexo asignado', 
    'Transgenero', 
    'Edad', 
    'Situacion laboral padre', 
    'Situacion laboral madre', 
    'Nivel profesional padre', 
    'Nivel profesional madre',
    'Nivel promedio del rendimiento academico',
    'Nivel de autopercepcion masculina',
    'Nivel de autopercepcion femenina',
    'Nivel de heteropercepcion masculina',
    'Nivel de heteropercepcion femenina',
    'Altura',
    'Peso',
    'Tratamiento psiquiatrico previo',
    'Presenta enfermedad cronica',
    'Bullying victima',
    'Bullying perpetrador',
    'Cyberbullying victima',
    'Cyberbullying perpetrador',
    'Adiccion/abuso alcohol',
    'Adiccion/abuso sustancias',
    'Adiccion/abuso Internet',
    'Problemas interiorizados',
    'Problemas exteriorizados',
    'Problemas de contexto',
    'Problemas recursos psicologicos',
    'Percepcion de discriminacion',
    'Fuente de discriminacion',
    'Nivel de resistencia/resiliencia',
    'Nivel de regulacion positiva',
    'Nivel de regulacion negativa',
    'Atrapamiento interno',
    'Atrapamiento externo',
    'Nivel percibido de derrota o fracaso',
    'Sentido de pertenencia frustada',
    'Percepcion de ser una carga',
    'Autoeficiencia para el suicidio',
    'Madre adolescente',
    'Padre adolescente',
    'Padres divorciados',
    'Familia monoparental',
    'Tratamiento psicologico padre/madre',
    'Adiccion padre/madre',
    'Relaciones conflictivas hijo-padre/madre',
    'Familia reconstruida',
    'Busqueda informacion autolesion',
    'Compartir en RRSS pensamiento autolesion',
    'Peticion ayuda en Internet',
    'Contagio', 
    'Tener conocidos que comparten autolesion en Internet',
    'Via de contacto para RRSS',
    'Contacto informacion autolesion',
    'Denuncia autolesion Internet',
    'Desenlace'
]

BAYES_NETWORK_VARIABLES_FAMILY = [
    'Curso', 
    'Sexo asignado', 
    'Transgenero', 
    'Edad',
    'Altura',
    'Peso',
    'Problemas interiorizados',
    'Problemas exteriorizados',
    'Problemas de contexto',
    'Problemas recursos psicologicos',
    'Madre adolescente',
    'Padre adolescente',
    'Padres divorciados',
    'Familia monoparental',
    'Tratamiento psicologico padre/madre',
    'Adiccion padre/madre',
    'Relaciones conflictivas hijo-padre/madre',
    'Familia reconstruida',
    'Aceptacion/rechazo parental',
    'Control parental',
    'Desenlace'
]

BAYES_NETWORK_VARIABLES_PROFESSIONAL = [
    'Curso', 
    'Sexo asignado', 
    'Transgenero', 
    'Edad', 
    'Altura',
    'Peso',
    'Madre adolescente',
    'Padre adolescente',
    'Padres divorciados',
    'Familia monoparental',
    'Tratamiento psicologico padre/madre',
    'Adiccion padre/madre',
    'Relaciones conflictivas hijo-padre/madre',
    'Familia reconstruida',
    'Situacion economica familiar precaria',
    'Estudios de la madre',
    'Estudios del padre',
    'Supervision parental insuficiente',
    'Maltrato al adolescente',
    'Duelo',
    'Ingreso familiar mensual',
    'Desenlace'
]

BAYES_NETWORK_EDGES_AUTOINFORME = [
    ('Curso', 'Desenlace'),
    ('Sexo asignado', 'Desenlace'),
    ('Transgenero', 'Desenlace'),
    ('Edad', 'Desenlace'),
    ('Situacion laboral padre', 'Desenlace'),
    ('Situacion laboral madre', 'Desenlace'),
    ('Nivel profesional padre', 'Desenlace'),
    ('Nivel profesional madre', 'Desenlace'),
    ('Nivel promedio del rendimiento academico', 'Desenlace'),
    ('Nivel de autopercepcion masculina', 'Desenlace'),
    ('Nivel de autopercepcion femenina', 'Desenlace'),
    ('Nivel de heteropercepcion masculina', 'Desenlace'),
    ('Nivel de heteropercepcion femenina', 'Desenlace'),
    ('Altura', 'Desenlace'),
    ('Peso', 'Desenlace'),
    ('Tratamiento psiquiatrico previo', 'Desenlace'),
    ('Presenta enfermedad cronica', 'Desenlace'),
    ('Bullying victima', 'Desenlace'),
    ('Bullying perpetrador', 'Desenlace'),
    ('Cyberbullying victima', 'Desenlace'),
    ('Cyberbullying perpetrador', 'Desenlace'),
    ('Adiccion/abuso alcohol', 'Desenlace'),
    ('Adiccion/abuso sustancias', 'Desenlace'),
    ('Adiccion/abuso Internet', 'Desenlace'),
    ('Problemas interiorizados', 'Desenlace'),
    ('Problemas exteriorizados', 'Desenlace'),
    ('Problemas de contexto', 'Desenlace'),
    ('Problemas recursos psicologicos', 'Desenlace'),
    ('Percepcion de discriminacion', 'Desenlace'),
    ('Fuente de discriminacion', 'Desenlace'),
    ('Nivel de resistencia/resiliencia', 'Desenlace'),
    ('Nivel de regulacion positiva', 'Desenlace'),
    ('Nivel de regulacion negativa', 'Desenlace'),
    ('Atrapamiento interno', 'Desenlace'),
    ('Atrapamiento externo', 'Desenlace'),
    ('Nivel percibido de derrota o fracaso', 'Desenlace'),
    ('Sentido de pertenencia frustada', 'Desenlace'),
    ('Percepcion de ser una carga', 'Desenlace'),
    ('Autoeficiencia para el suicidio', 'Desenlace'),
    ('Madre adolescente', 'Desenlace'),
    ('Padre adolescente', 'Desenlace'),
    ('Padres divorciados', 'Desenlace'),
    ('Familia monoparental', 'Desenlace'),
    ('Tratamiento psicologico padre/madre', 'Desenlace'),
    ('Adiccion padre/madre', 'Desenlace'),
    ('Relaciones conflictivas hijo-padre/madre', 'Desenlace'),
    ('Familia reconstruida', 'Desenlace'),
    ('Busqueda informacion autolesion', 'Desenlace'),
    ('Compartir en RRSS pensamiento autolesion', 'Desenlace'),
    ('Peticion ayuda en Internet', 'Desenlace'),
    ('Contagio', 'Desenlace'),
    ('Tener conocidos que comparten autolesion en Internet', 'Desenlace'),
    ('Via de contacto para RRSS', 'Desenlace'),
    ('Contacto informacion autolesion', 'Desenlace'),
    ('Denuncia autolesion Internet', 'Desenlace'),
]

BAYES_NETWORK_EDGES_FAMILY = [
    ('Curso', 'Desenlace'),
    ('Sexo asignado', 'Desenlace'),
    ('Transgenero', 'Desenlace'),
    ('Edad', 'Desenlace'),
    ('Peso', 'Desenlace'),
    ('Problemas interiorizados', 'Desenlace'),
    ('Problemas exteriorizados', 'Desenlace'),
    ('Problemas de contexto', 'Desenlace'),
    ('Problemas recursos psicologicos', 'Desenlace'),
    ('Madre adolescente', 'Desenlace'),
    ('Padre adolescente', 'Desenlace'),
    ('Padres divorciados', 'Desenlace'),
    ('Familia monoparental', 'Desenlace'),
    ('Tratamiento psicologico padre/madre', 'Desenlace'),
    ('Adiccion padre/madre', 'Desenlace'),
    ('Relaciones conflictivas hijo-padre/madre', 'Desenlace'),
    ('Familia reconstruida', 'Desenlace'),
    ('Aceptacion/rechazo parental', 'Desenlace'),
    ('Control parental', 'Desenlace')
]

BAYES_NETWORK_EDGES_PROFESSIONAL = [
    ('Curso', 'Desenlace'),
    ('Sexo asignado', 'Desenlace'),
    ('Transgenero', 'Desenlace'),
    ('Edad', 'Desenlace'),
    ('Altura', 'Desenlace'),
    ('Peso', 'Desenlace'),
    ('Madre adolescente', 'Desenlace'),
    ('Padre adolescente', 'Desenlace'),
    ('Padres divorciados', 'Desenlace'),
    ('Familia monoparental', 'Desenlace'),
    ('Tratamiento psicologico padre/madre', 'Desenlace'),
    ('Adiccion padre/madre', 'Desenlace'),
    ('Relaciones conflictivas hijo-padre/madre', 'Desenlace'),
    ('Familia reconstruida', 'Desenlace'),
    ('Situacion economica familiar precaria', 'Desenlace'),
    ('Estudios de la madre', 'Desenlace'),
    ('Estudios del padre', 'Desenlace'),
    ('Supervision parental insuficiente', 'Desenlace'),
    ('Maltrato al adolescente', 'Desenlace'),
    ('Duelo', 'Desenlace'),
    ('Ingreso familiar mensual', 'Desenlace')
]