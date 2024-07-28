import React, { useState, useEffect } from 'react';
import { View, Text, StyleSheet, TextInput } from 'react-native';
import Dropdown from '../../../../components/dropdown';
import SivariaInput from '../../../../components/sivaria-input';
import SivariaRadioButton from '../../../../components/sivaria-radio-button';


const courses = {
    ninguno: 'Ninguno',
    primaria: 'Primaria',
    eso: 'ESO',
    bachillerato: 'Bachillerato',
    universidad: 'Universidad',
    otro: 'Otro',
};
const genderData = {
    hombre:'Hombre', 
    mujer:'Mujer',     
    otro:'Otro',
};
const transData = {
    si:'Sí',
    no:'No',
    no_se:'No estoy seguro/a de ser transgénero'
};
const parentsJobSituationData = {
    no_trabaja:'No trabaja',
    trabaja:'Trabaja', 
    pensionado:'Pensionado (recibe una paga o ayuda del Estado)', 
};
const parentsAcademicLevel = {
    ninguno:'Ninguno',
    bachillerato:'Bachillerato',
    formacion_profesional:'Formación Profesional',
    universidad:'Universidad',
    otro:'Otro',
};

const academicPerformanceData = {
    insuficiente:'Insuficiente',
    suficiente:'Suficiente',
    notable:'Notable',
    sobresaliente:'Sobresaliente',
    extraordinario:'Extraordinario',
};
const yesNoData = {
    si:'Sí',
    no:'No',
};
const discriminationTypes = {
    ninguno: 'Ninguno',
    genero: 'Género',
    raza: 'Raza',
    orientacion_sexual: 'Orientación sexual',
    otro: 'Otro', 
};

export const FamilyFormTemplate = ({ formData }) => {
    return (
        <>
            <View style={{padding: 20, backgroundColor: 'white'}}>
                <View style={{padding: 5}}>                
                    <Text style={{fontWeight:'bold'}}>Código del cuestionario: {formData.code}</Text>
                    <Text style={{fontWeight:'bold'}}>Fecha y Hora: {formData.datetime_str}</Text>
                    <Text style={{fontWeight:'bold'}}>Cuestionario realizado por: {formData.user}</Text>
                    <Text style={{fontWeight:'bold'}}>Identificador (ID) Participante: {formData.to_user}</Text>
                    <Text style={{fontWeight:'bold'}}>Predicción final: {formData.result}</Text>
                </View>
                <View style={{padding: 5}}>
                    <Text style={{fontWeight:'bold'}}>Curso: {courses[formData.social_data.course]}</Text>
                </View>
                <Text style={{fontWeight:'bold'}}>
                    SENA
                </Text>
                <Text style={{fontWeight:'bold'}}>
                    1. Su hijo/a o familiar NUNCA o CASI NUNCA muestra esa conducta.
                </Text>
                <Text style={{fontWeight:'bold'}}>
                    2. Su hijo/a o familiar POCAS VECES muestra esa conducta.                
                </Text>
                <Text style={{fontWeight:'bold'}}>
                    3. Su hijo/a o familiar ALGUNAS VECES muestra esa conducta.
                </Text>
                <Text style={{fontWeight:'bold'}}>
                    4. Su hijo/a o familiar MUCHAS VECES muestra esa conducta.
                </Text>
                <Text style={{fontWeight:'bold'}}>
                    5. Su hijo/a o familiar SIEMPRE o CASI SIEMPRE muestra esa conducta.
                </Text>
                <View style={{padding:5}}>
                    <Text>104. Sus compañeros de clase le aíslan: {formData.sena_family.sena104}</Text>
                </View>
                <View style={{padding:5}}>
                    <Text>117. Se mete en peleas: {formData.sena_family.sena117}</Text>
                </View>
                <View style={{padding:5}}>
                    <Text>118. Se queja de estar enfermo aunque el médico dice que todo está bien: {formData.sena_family.sena118}</Text>
                </View>
                <View style={{padding:5}}>
                    <Text>121. Creo que consume drogas: {formData.sena_family.sena121}</Text>
                </View>
                <View style={{padding:5}}>
                    <Text>
                        123. Se divierte molestando a otros: {formData.sena_family.sena123}
                    </Text>
                </View>
                <View style={{padding:5}}>
                    <Text>
                        124. Hace cosas ilegales: {formData.sena_family.sena124}   
                    </Text>
                </View>
                <View style={{padding:5}}>
                    <Text>
                        125. Se integra con facilidad en los grupos: {formData.sena_family.sena125}    
                    </Text>
                </View>
                <View style={{padding:5}}>
                    <Text>
                        135. Se preocupa por cosas sin importancia: {formData.sena_family.sena135}    
                    </Text>
                </View>
                <View style={{padding:5}}>
                    <Text>
                        137. Se esfuerza en sus estudios: {formData.sena_family.sena137}    
                    </Text>
                </View>
                <View style={{padding:5}}>
                    <Text>
                        138. Su mirada es triste, sin brillo: {formData.sena_family.sena138}    
                    </Text>
                </View>
                <View style={{padding:5}}>
                    <Text>
                        139. Es sociable: {formData.sena_family.sena139}
                    </Text>
                </View>
                <View style={{padding:5}}>
                    <Text>
                        140. Le cuesta controlar sus emociones: {formData.sena_family.sena140}
                    </Text>
                </View>
                <View style={{padding:5}}>
                    <Text>
                        145. Le da demasiadas vueltas a las cosas: {formData.sena_family.sena145}
                    </Text>
                </View>
                <View style={{padding:5}}>
                    <Text>
                        146. Se obsesionan con adelgazar: {formData.sena_family.sena146}
                    </Text>
                </View>
                <View style={{padding:5}}>
                    <Text>
                        148. Dice que tiene náuseas o ganas de vomitar: {formData.sena_family.sena148}
                    </Text>
                </View>
                <View style={{padding:5}}>
                    <Text>
                        154. Es simpático con los que le rodean: {formData.sena_family.sena154}
                    </Text>
                </View>
                <View style={{padding:5}}>
                    <Text style={{fontWeight: 'bold'}}>
                        Indique los ingresos familiares familiares mensuales en euros (aproximado): {formData.family.ingreso_familiar_mensual}€
                    </Text>
                </View>
                <View style={{padding:5}}>
                    <Text style={{fontWeight:'bold'}}>
                        ¿Considera que poseen una situación económica familiar precaria? {yesNoData[formData.family.situacion_economica_precaria]}
                    </Text>
                </View>
                <View style={{padding:5}}>
                    <Text style={{fontWeight:'bold'}}>Indica la situación laboral actual de tu padre: {parentsJobSituationData[formData.social_data.job_situation_father]}</Text>
                </View>
                <View style={{padding:5}}>
                    <Text style={{fontWeight:'bold'}}>Indica la situación laboral actual de tu madre: {parentsJobSituationData[formData.social_data.job_situation_mother]}</Text>
                </View>
                <View style={{padding:5}}>
                    <Text style={{fontWeight:'bold'}}>Indica los estudios de tu padre o figura parental 1: {parentsAcademicLevel[formData.social_data.academic_level_father]}</Text>
                </View>
                <View style={{padding:5}}>
                    <Text style={{fontWeight:'bold'}}>Indica los estudios de tu madre o figura parental 2: {parentsAcademicLevel[formData.social_data.academic_level_mother]}</Text>
                </View>
                <View style={{padding:5}}>
                    <Text style={{fontWeight: 'bold'}}>Indique la edad de tu padre en el momento de tu nacimiento (años): {formData.family.padre_adolescente}</Text>
                </View>
                <View style={{padding:5}}>
                    <Text style={{fontWeight: 'bold'}}>Indique la edad de tu madre en el momento de tu nacimiento (años): {formData.family.madre_adolescente}</Text>
                </View>
                <View style={{padding:5}}>
                    <Text style={{fontWeight: 'bold'}}>Conviven padre y madre en el hogar habitual con su hijo/a: {yesNoData[formData.family.familia_monoparental]}</Text>
                </View>
                <View style={{padding:5}}>
                    <Text style={{fontWeight: 'bold'}}>Indique si los padres están separados o divorciados: {yesNoData[formData.family.padres_divorciados]}</Text>
                </View>
                <View style={{padding:5}}>
                    <Text style={{fontWeight: 'bold'}}>Indica si alguna de las figuras parentales ha recibido tratamiento psicológico o psiquiátrico: {yesNoData[formData.family.tratamiento_psicologico_padre_madre]}</Text>
                </View>
                <View style={{padding:5}}>
                    <Text style={{fontWeight: 'bold'}}>Indica si alguna de las figuras parentales ha recibido tratamiento por consumo de drogas o alcohol: {yesNoData[formData.family.adiccion_padre_madre]}</Text>
                </View>
                <View style={{padding:5}}>
                    <Text style={{fontWeight: 'bold'}}>Indica si las relaciones con su hijo/a son conflictivas o problemáticas (tensión, rechazo, desinterés, peleas frecuentes...): {yesNoData[formData.family.relaciones_conflictivas_hijo_padre_madre]}</Text>
                </View>
                <View style={{padding:5}}>
                    <Text style={{fontWeight: 'bold'}}>Indica si la familia ha sido reconstruida: {yesNoData[formData.family.familia_reconstruida]}</Text>
                </View>
                <Text style={{fontWeight:'bold'}}>
                    PARQ
                </Text>
                <Text style={{fontWeight:'bold'}}>
                    1. Básicamente incierto ("Casi nunca verdad").
                    2. Cierto ocasionalmente ("A veces verdad").
                    3. Cierto frecuentemente ("Muchas veces verdad"). 
                    4. Cierto ("casi siempre verdad").
                </Text>
                <View style={{padding:5}}>
                    <Text>1. Digo cosas buenas sobre mi hijo/a: {formData.parq.parq1}</Text>
                </View>
                <View style={{padding:5}}>
                    <Text>2. Presto atención a mi hijo/a: {formData.parq.parq2}</Text>
                </View>
                <View style={{padding:5}}>
                    <Text>3. Me preocupo de que mi hijo/a sepa exactamente lo que puede o no puede hacer: {formData.parq.parq3}</Text>
                </View>
                <View style={{padding:5}}>
                    <Text>4. Hago que mi hijo/a confíe en mí: {formData.parq.parq4}</Text>
                </View>
                <View style={{padding:5}}>
                    <Text>5. Pego a mi hijo/a cuando se lo merece: {formData.parq.parq5}</Text>
                </View>
                <View style={{padding:5}}>
                    <Text>6. Mi hijo/a es un gran incordio para mí: {formData.parq.parq6}</Text>
                </View>
                <View style={{padding:5}}>
                    <Text>7. Siempre le digo a mi hijo/a cómo debe comportarse: {formData.parq.parq7}</Text>
                </View>
                <View style={{padding:5}}>
                    <Text>8. Castigo a mi hijo/a serveramente cuando estoy enfadado/a: {formData.parq.parq8}</Text>
                </View>
                <View style={{padding:5}}>
                    <Text>9. Estoy demasiado ocupado/a para contestar las preguntas a mi hijo/a: {formData.parq.parq9}</Text>
                </View>
                <View style={{padding:5}}>
                    <Text>10. No le gusto a mi hijo/a: {formData.parq.parq10}</Text>
                </View>
                <View style={{padding:5}}>
                    <Text>11. Estoy realmente interesado/A en los asuntos de mi hijo/a: {formData.parq.parq11}</Text>
                </View>
                <View style={{padding:5}}>
                    <Text>12. Digo muchas cosas desagradables a mi hijo/a: {formData.parq.parq12}</Text>
                </View>
                <View style={{padding:5}}>
                    <Text>13. Presto atención a mi hijo/a cuando me pide ayuda: {formData.parq.parq13}</Text>
                </View>
                <View style={{padding:5}}>
                    <Text>14. Insisto en que mi hijo/a haga exactamente lo que le digo: {formData.parq.parq14}</Text>
                </View>
                <View style={{padding:5}}>
                    <Text>15. Hago que mi hijo/a sienta que le quiero y le necesito: {formData.parq.parq15}</Text>
                </View>
                <View style={{padding:5}}>
                    <Text>16. Presto muchísima atención a mi hijo/a: {formData.parq.parq16}</Text>
                </View>
                <View style={{padding:5}}>
                    <Text>17. Daño los sentimientos de mi hijo/a: {formData.parq.parq17}</Text>
                </View>
                <View style={{padding:5}}>
                    <Text>18. Olvido cosas importantes de mi hijo/a que debería recordar: {formData.parq.parq18}</Text>
                </View>
                <View style={{padding:5}}>
                    <Text>19. Cuando mi hijo/a se comporta mal le hago sentir que no le quiero: {formData.parq.parq19}</Text>
                </View>
                <View style={{padding:5}}>
                    <Text>20. Dejo que mi hijo/a haga lo que quiera: {formData.parq.parq20}</Text>
                </View>
                <View style={{padding:5}}>
                    <Text>21. Hago que mi hijo/a se sienta importante: {formData.parq.parq21}</Text>
                </View>
                <View style={{padding:5}}>
                    <Text>22. Atemorizo o amenazo a mi hijo/a para hablar sobre ello: {formData.parq.parq22}</Text>
                </View>
                <View style={{padding:5}}>
                    <Text>23. Me preocupo sobre lo que piensa y le gusta a mi hijo/a para hablar sobre ello: {formData.parq.parq23}</Text>
                </View>
                <View style={{padding:5}}>
                    <Text>24. Siento que los demás niños/as son mejores que mi hijo/a: {formData.parq.parq24}</Text>
                </View>
                <View style={{padding:5}}>
                    <Text>25. Hago saber a mi hijo/a que no es querido: {formData.parq.parq25}</Text>
                </View>
                <View style={{padding:5}}>
                    <Text>26. Quiero controlar cualquier cosa que mi hijo/a haga: {formData.parq.parq26}</Text>
                </View>
                <View style={{padding:5}}>
                    <Text>27. Hago saber a mi hijo/a cuando hace algo que me molesta: {formData.parq.parq27}</Text>
                </View>
                <View style={{padding:5}}>
                    <Text>28. Sólo presto atención a mi hijo7a cuando hace algo que me molesta: {formData.parq.parq28}</Text>
                </View>
                <View style={{padding:5}}>
                    <Text>29. Trato a mi hijo/a amablemente y con cariño: {formData.parq.parq29}</Text>
                </View>
            </View>
        </>
    );
};
