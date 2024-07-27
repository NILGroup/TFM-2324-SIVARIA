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

export const YoungFormTemplate = ({ formData }) => {
    return (
        <View style={{padding: 20, backgroundColor: 'white'}}>
            <View style={{padding: 5}}>
                <Text style={{fontWeight:'bold'}}>Código del cuestionario: {formData.code}</Text>
                <Text style={{fontWeight:'bold'}}>Fecha y Hora: {formData.datetime_str}</Text>
                <Text style={{fontWeight:'bold'}}>Cuestionario realizado por: {formData.user}</Text>
                <Text style={{fontWeight:'bold'}}>Predicción final: {formData.result}</Text>
            </View>
            <View style={{padding: 5}}>
                <Text style={{fontWeight:'bold'}}>Curso: {courses[formData.social_data.course]}</Text>
            </View>
            <View style={{padding:5}}>
                <Text style={{fontWeight:'bold'}}>Edad (en años): {formData.social_data.age}</Text>
            </View>
            <View style={{padding:5}}>
                <Text style={{fontWeight:'bold'}}>Sexo: {genderData[formData.social_data.gender]}</Text>
            </View>
            <View style={{padding:5}}>
                <Text style={{fontWeight:'bold'}}>¿Te consideras una persona trans?: {transData[formData.social_data.trans]}</Text>
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
                <Text style={{fontWeight:'bold'}}>Señala cuál crees que es tu rendimiento académico en los dos últimos años: {academicPerformanceData[formData.social_data.academic_performance]}</Text>
            </View>
            <View style={{padding:5}}>
                <Text style={{fontWeight:'bold'}}>
                    Señala si tienes en la actualidad o has tenido previamente tratamiento psiquiátrico y/o psicológico 
                    (por ejemplo, me han diagnosticado depresión o ansiedad): {yesNoData[formData.social_data.previous_psychiatric_treatment]}
                </Text>
            </View>
            <View style={{padding:5}}>
                <Text style={{fontWeight:'bold'}}>
                    Indica si padeces alguna enfermedad crónica desde hace por lo menos un año 
                    (por ejemplo: me han diagnosticado, diabetes, epilepsia...): {yesNoData[formData.social_data.chronic_disease]}
                </Text>
            </View>
            <View style={{padding:5}}>
                <Text style={{fontWeight:'bold'}}>En general, ¿cómo te ves a ti mismo/a? (responde a ambas escalas: masculino y femenina). Evalúe de 0 a 6,
                donde 0 significa Nada en absoluto y 6 completamente:</Text>
                <Text>Femenina: {formData.social_data.female_self_perception}</Text>
                <Text>Masculino: {formData.social_data.male_self_perception}</Text>
            </View>
            <View style={{padding:5}}>
                <Text style={{fontWeight:'bold'}}>En general, ¿cómo crees que te ve la mayoría de la gente? (responde a ambas escalas: masculino y femenina). Evalúe de 0 a 6,
                donde 0 significa Nada en absoluto y 6 completamente:</Text>
                <Text>Femenina: {formData.social_data.female_others_perception}</Text>
                <Text>Masculino: {formData.social_data.male_others_perception}</Text>
            </View>
            <View style={{padding:5}}>
                <Text style={{fontWeight:'bold'}}>Cuánto pesas? (poner valor aproximado en kg): {formData.social_data.weight}</Text>                             
            </View>
            <View style={{padding:5}}>
                <Text style={{fontWeight:'bold'}}>Cuánto mides? (poner valor aproximado en cm): {formData.social_data.height}</Text>                 
            </View>
            <View style={{padding:5}}>
                <Text style={{fontWeight:'bold'}}>Indica el tipo de discriminación sufrido. Si no has sufrido ninguno, pon Ninguno: {discriminationTypes[formData.social_data.discrimination_type]}</Text>
            </View>
            <Text style={{fontWeight:'bold'}}>
                EBIP-Q y del ECIP-Q
            </Text>
            <View style={{padding:5}}>
                <Text>VB1. Alguien me ha golpeado, me ha pateado o me ha empujado: {formData.ebipq_ecipq.vb1}</Text>
            </View>
            <View style={{padding:5}}>
                <Text>VB2. Alguien me ha insultado: {formData.ebipq_ecipq.vb2}</Text>
            </View>
            <View style={{padding:5}}>
                <Text>VB4. Alguien me ha amenazado: {formData.ebipq_ecipq.vb4}</Text>
            </View>
            <View style={{padding:5}}>
                <Text>AB1. He golpeado, pateado o empujado a alguien: {formData.ebipq_ecipq.ab1}</Text>
            </View>
            <View style={{padding:5}}>
                <Text>AB2. He insultado he dicho palabras malsonantes a alguien porque quería hacerle daño: {formData.ebipq_ecipq.ab2}</Text>
            </View>
            <View style={{padding:5}}>
                <Text>AB4. He amenazado a alguien: {formData.ebipq_ecipq.ab4}</Text>
            </View>
            <View style={{padding:5}}>
                <Text>CybV1. Alguien me ha dicho palabras malsonantes o me ha insultado usando el email o SMS: {formData.ebipq_ecipq.cybv1}</Text>
            </View>
            <View style={{padding:5}}>
                <Text>CybV2. Alguien le ha dicho a otros palabras malsonantes sobre mí usando Internet o SMS: {formData.ebipq_ecipq.cybv2}</Text>
            </View>
            <View style={{padding:5}}>
                <Text>CybV3. Alguien me ha amenazado a través de mensajes en Interne o SMS: {formData.ebipq_ecipq.cybv3}</Text>
            </View>
            <View style={{padding:5}}>
                <Text>CybB1. He dicho palabras malsonantes a alguien o le he insultado usando SMS o mensajes en Internet: {formData.ebipq_ecipq.cybb1}</Text>
            </View>
            <View style={{padding:5}}>
                <Text>CybB2. He dicho palabras malsonantes sobre alguien a otras personas en mensajes por Internet o por SMS: {formData.ebipq_ecipq.cybb2}</Text>
            </View>
            <View style={{padding:5}}>
                <Text>CybB3. He amenazado a alguien a través de SMS o mensajes en Internet: {formData.ebipq_ecipq.cybb3}</Text>
            </View>
            <Text style={{fontWeight:'bold'}}>
                RRSS
            </Text>
            <View style={{padding:5}}>
                <Text>1. ¿Has visto imágenes o leído últimamente sobre autolesión o suicidio en algún medio audiovisual? {yesNoData[formData.rrss.rrss1]}</Text>
            </View>
            <View style={{padding:5}}>
                <Text>2. ¿Has buscado alguna vez información o te has metido en un foro sobre el suicidio y/o autolesión en Internet? {yesNoData[formData.rrss.rrss2]}</Text>
            </View>
            <View style={{padding:5}}>
                <Text>3. ¿Alguna vez has sentido la necesidad de hacerte daño y has compartido tu pensamiento a través de alguna red social o Internet? {yesNoData[formData.rrss.rrss3]}</Text>
            </View>
            <View style={{padding:5}}>
                <Text>4. ¿Alguna vez has sentido angustia, tristeza, desesperación, o te has sentido solo, lo has compartido o has buscado ayuda en Internet? {formData.rrss.rrss4}</Text>
            </View>
            <View style={{padding:5}}>
                <Text>5. ¿Alguna vez has sentido la tentación de hacerte daño después de ver algún tipo de contenido en Internet? {yesNoData[formData.rrss.rrss5]}</Text>
            </View>
            <View style={{padding:5}}>
                <Text>6. ¿Alguna vez has sentido la tentación de hacerte daño y has buscado ayuda en Internet? {yesNoData[formData.rrss.rrss6]}</Text>
            </View>
            <View style={{padding:5}}>
                <Text>7. ¿Conoces a alguien que haya compartido alguna foto, pensamiento o comportamiento autolesivo en Internet? {yesNoData[formData.rrss.rrss7]}</Text>
            </View>
            <Text style={{fontWeight:'bold'}}>
                MULTICAGE CAD-4
            </Text>
            <Text style={{fontWeight:'bold'}}>
                Por favor, responde Sí/No a las siguientes preguntas
            </Text>
            <View style={{padding:5}}>
                <Text>1. ¿Has pensado alguna vez que deberías beber menos alcohol? {yesNoData[formData.mcad.mcad1]}</Text>
            </View>
            <View style={{padding:5}}>
                <Text>2. ¿Te has sentido molesto/a cuando alguna persona te ha criticado tu manera o forma de beber alcohol? {yesNoData[formData.mcad.mcad2]}</Text>
            </View>
            <View style={{padding:5}}>
                <Text>3. ¿Te has sentido culpable alguna vez por tu manera o forma de beber alcohol? {yesNoData[formData.mcad.mcad3]}</Text>
            </View>
            <View style={{padding:5}}>
                <Text>4. ¿Alguna vez lo primero que has hecho por la mañana es beber alguna bebida alcohólica para relajarte o para eliminar la resaca? {yesNoData[formData.mcad.mcad4]}</Text>
            </View>
            <View style={{padding:5}}>
                <Text>5. ¿Has pensado alguna vez que deberías consumir menos drogas? {yesNoData[formData.mcad.mcad5]}</Text>
            </View>
            <View style={{padding:5}}>
                <Text>6. ¿Niegas el consumo de drogas a familiares, amigos o compañeros para evitar que te critiquen? {yesNoData[formData.mcad.mcad6]}</Text>
            </View>
            <View style={{padding:5}}>
                <Text>7. ¿Has tenido problemas psicológicos, económicos, laborales o familiares a causa del consumo de drogas? {yesNoData[formData.mcad.mcad7]}</Text>
            </View>
            <View style={{padding:5}}>
                <Text>8. ¿Te sientes a veces impulsado a consumir drogas aunque hayas decidido no hacerlo? {yesNoData[formData.mcad.mcad8]}</Text>
            </View>
            <View style={{padding:5}}>
                <Text>9. ¿Dedicas más tiempo del que crees que deberías a estar conectado a Internet con objetivos distintos a los de tu trabajo? {yesNoData[formData.mcad.mcad9]}</Text>
            </View>
            <View style={{padding:5}}>
                <Text>10. ¿Se han quejado tus familiares de las horas que dedicas a Internet? {yesNoData[formData.mcad.mcad10]}</Text>
            </View>
            <View style={{padding:5}}>
                <Text>11. ¿Te resulta duro permanecer alejado/a de Internet varios días seguidos? {yesNoData[formData.mcad.mcad11]}</Text>
            </View>
            <View style={{padding:5}}>
                <Text>12. ¿Tienes problemas para controlar el impulso de conectarte a Internet o has intentado sin éxito reducir el tiempo que dedicas a estar conectado/a? {yesNoData[formData.mcad.mcad12]}</Text>
            </View>
            <Text style={{fontWeight:'bold'}}>
                CERQ-S
            </Text>
            <Text style={{fontWeight:'bold'}}>
                De 1 a 5, donde 1 significa casi nunca y 5 casi siempre.
            </Text>
            <View style={{padding:5}}>
                <Text>1. Siento que soy el único culpable de lo que ha pasado: {formData.cerqs.cerqs1}</Text>
            </View>
            <View style={{padding:5}}>
                <Text>2. Creo que tengo que acpear lo que ha pasado: {formData.cerqs.cerqs2}</Text>
            </View>
            <View style={{padding:5}}>
                <Text>3. Pienso a menudo en cómo me siento en relación con lo que me ha pasado: {formData.cerqs.cerqs3}</Text>
            </View>
            <View style={{padding:5}}>
                <Text>4. Me parece que otros son culpables de lo ocurrido: {formData.cerqs.cerqs4}</Text>
            </View>
            <View style={{padding:5}}>
                <Text>5. Me siento único/a responsable de lo ocurrido: {formData.cerqs.cerqs5}</Text>
            </View>
            <View style={{padding:5}}>
                <Text>6. Creo que tengo que aceptar la situación: {formData.cerqs.cerqs6}</Text>
            </View>
            <View style={{padding:5}}>
                <Text>7. Me preocupa lo que piense y sienta sobre lo que me ha pasado: {formData.cerqs.cerqs7}</Text>
            </View>
            <View style={{padding:5}}>
                <Text>8. Pienso en cosas agradables que nada tienen que ver con lo que me ha pasado: {formData.cerqs.cerqs8}</Text>
            </View>
            <View style={{padding:5}}>
                <Text>9. Pienso en cuál sería la mejor forma de enfrentarme a la situación: {formData.cerqs.cerqs9}</Text>
            </View>
            <View style={{padding:5}}>
                <Text>10. Sigo pensando en lo terrible que ha sido lo que me ha pasado: {formData.cerqs.cerqs10}</Text>
            </View>
            <View style={{padding:5}}>
                <Text>11. Me parece que otros son responsables de lo que ha ocurrido: {formData.cerqs.cerqs11}</Text>
            </View>
            <View style={{padding:5}}>
                <Text>12. Pienso en algo agradable en vez de pensar en lo ocurrido: {formData.cerqs.cerqs12}</Text>
            </View>
            <View style={{padding:5}}>
                <Text>13. Creo que la situación tiene también su lado positivo: {formData.cerqs.cerqs13}</Text>
            </View>
            <View style={{padding:5}}>
                <Text>14. Creo que no ha sido tan malo en comparación a otras cosas: {formData.cerqs.cerqs14}</Text>
            </View>
            <View style={{padding:5}}>
                <Text>15. Pienso en un plan acerca de lo mejor que podría hacer: {formData.cerqs.cerqs15}</Text>
            </View>
            <View style={{padding:5}}>
                <Text>16. Busco los aspectos positivos de la cuestión: {formData.cerqs.cerqs16}</Text>
            </View>
            <View style={{padding:5}}>
                <Text>17. Me digo que hay cosas peores en la vida: {formData.cerqs.cerqs17}</Text>
            </View>
            <View style={{padding:5}}>
                <Text>18. Pienso continuamente en lo horrible que ha sido la situación: {formData.cerqs.cerqs18}</Text>
            </View>
            <Text style={{fontWeight: 'bold'}}>
                Escalas ATD
            </Text>
            <Text style={{fontWeight: 'bold'}}>
                0 "No se corresponden en absoluto"
            </Text>
            <Text style={{fontWeight: 'bold'}}>
                1 "Se corresponden un poco"
            </Text>
            <Text style={{fontWeight: 'bold'}}>
                2 "Se corresponden moderadamente"
            </Text>
            <Text style={{fontWeight: 'bold'}}>
                3 "Se corresponden bastante"
            </Text>
            <Text style={{fontWeight: 'bold'}}>            
                4 "Se corresponden extremadamente"
            </Text>
            <Text style={{fontWeight: 'bold'}}>
                ATI
            </Text>
            <View style={{padding:5}}>
                <Text>1. Quiero escapar de mí mismo/a: {formData.ati.ati1}</Text>
            </View>
            <View style={{padding:5}}>
                <Text>2. Me siento impotente para cambiarme a mí mismo/a: {formData.ati.ati2}</Text>
            </View>
            <View style={{padding:5}}>
                <Text>3. Me gustaría escapar de mis pensamientos y sentimientos: {formData.ati.ati3}</Text>
            </View>
            <View style={{padding:5}}>
                <Text>4. Me siento atrapado dentro de mí mismo/a: {formData.ati.ati4}</Text>
            </View>
            <View style={{padding:5}}>
                <Text>5. Me gustaría huir de lo que soy y empezar de nuevo: {formData.ati.ati5}</Text>
            </View>
            <View style={{padding:5}}>
                <Text>6. Siento que estoy en un pozo del que no puedo salir: {formData.ati.ati6}</Text>
            </View>
            <Text style={{fontWeight:'bold'}}>
                ATE
            </Text>
            <View style={{padding:5}}>
                <Text>1. Estoy en una situación en la que me siento atrapado/a: {formData.ate.ate1}</Text>
            </View>
            <View style={{padding:5}}>
                <Text>2. Deseo con todas mis fuerzas escapar de mi vida: {formData.ate.ate2}</Text>
            </View>
            <View style={{padding:5}}>
                <Text>3. Estoy en una relación de la que no puedo salir/ Mantengo un tipo de relaciones en mi vida de las que no puedo salir: {formData.ate.ate3}</Text>
            </View>
            <View style={{padding:5}}>
                <Text>4. A menudo tengo la sensación de que me gustaría huir: {formData.ate.ate4}</Text>
            </View>
            <View style={{padding:5}}>
                <Text>5. Me siento importante para cambiar las cosas: {formData.ate.ate5}</Text>
            </View>
            <View style={{padding:5}}>
                <Text>6. Me siento atrapado por mis obligaciones: {formData.ate.ate6}</Text>
            </View>
            <View style={{padding:5}}>
                <Text>7. No veo forma de salir de mi situación actual: {formData.ate.ate7}</Text>
            </View>
            <View style={{padding:5}}>
                <Text>8. Me gustaría alejarme de las personas más importantes de mi vida: {formData.ate.ate8}</Text>
            </View>
            <View style={{padding:5}}>
                <Text>9. Tengo un fuerte deseo de alejarme y mantenerme alejado de donde estoy: {formData.ate.ate9}</Text>
            </View>
            <View style={{padding:5}}>
                <Text>10. Me siento atrapado por otras personas: {formData.ate.ate10}</Text>
            </View>
            <Text style={{fontWeight: 'bold'}}>
                ED
            </Text>
            <Text style={{fontWeight: 'bold'}}>
                0 "Nunca"
            </Text>
            <Text style={{fontWeight: 'bold'}}>
                1 "Casi nunca"
            </Text>
            <Text style={{fontWeight: 'bold'}}>
                2 "A veces"
            </Text>
            <Text style={{fontWeight: 'bold'}}>
                3 "Muchas veces"
            </Text>
            <Text style={{fontWeight: 'bold'}}>            
                4 "Siempre o todo el tiempo"
            </Text>
            <View style={{padding:5}}>
                <Text>1. Siento que he fracasado en la vida: {formData.ed.ed1}</Text>
            </View>
            <View style={{padding:5}}>
                <Text>2. Siento que soy una persona exitosa: {formData.ed.ed2}</Text>
            </View>
            <View style={{padding:5}}>
                <Text>3. Me siento derrotado por la vida: {formData.ed.ed3}</Text>
            </View>
            <View style={{padding:5}}>
                <Text>4. Siento que básicamente soy un/a ganador/a: {formData.ed.ed4}</Text>
            </View>
            <View style={{padding:5}}>
                <Text>5. Siento que he perdido mi lugar en el mundo: {formData.ed.ed5}</Text>
            </View>
            <View style={{padding:5}}>
                <Text>6. Siento que la vida me ha tratado como un saco de boxeo: {formData.ed.ed6}</Text>
            </View>
            <View style={{padding:5}}>
                <Text>7. Me siento impotente: {formData.ed.ed7}</Text>
            </View>
            <View style={{padding:5}}>
                <Text>8. Siento que me han arrebatado la confianza en mí mismo/a: {formData.ed.ed8}</Text>
            </View>
            <View style={{padding:5}}>
                <Text>9. Me siento capaz de afrontar lo que la vida me depare: {formData.ed.ed9}</Text>
            </View>
            <View style={{padding:5}}>
                <Text>10. Siento que he tocado fondo: {formData.ed.ed10}</Text>
            </View>
            <View style={{padding:5}}>
                <Text>11. Me siento completamente anulado/a: {formData.ed.ed11}</Text>
            </View>
            <View style={{padding:5}}>
                <Text>12. Siento que soy un/a perdedor/a en la vida: {formData.ed.ed12}</Text>
            </View>
            <View style={{padding:5}}>
                <Text>13. Siento que me he rendido: {formData.ed.ed13}</Text>
            </View>
            <View style={{padding:5}}>
                <Text>14. Me siento acabado/a: {formData.ed.ed14}</Text>
            </View>
            <View style={{padding:5}}>
                <Text>15. Siento que he perdido batallas importantes en la vida: {formData.ed.ed15}</Text>
            </View>
            <View style={{padding:5}}>
                <Text>16. Siento que no hay nada por lo que luchar en la vida: {formData.ed.ed16}</Text>
            </View>
            <Text style={{fontWeight: 'bold'}}>
                ER
            </Text>
            <Text style={{fontWeight: 'bold'}}> 
                0 = Totalmente en desacuerdo y 4 = Totalmente de acuerdo
            </Text>
            <View style={{padding:5}}>
                <Text>1. Sé adaptarme a los cambios: {formData.er.er1}</Text>
            </View>
            <View style={{padding:5}}>
                <Text>2. Puedo manejar cualquier situación: {formData.er.er2}</Text>
            </View>
            <View style={{padding:5}}>
                <Text>3. Veo el lado positivo de las cosas: {formData.er.er3}</Text>
            </View>
            <View style={{padding:5}}>
                <Text>4. Me puedo manejar bien a pesar de la presión o el estrés: {formData.er.er4}</Text>
            </View>
            <View style={{padding:5}}>
                <Text>5. Después de un grave contratiempo: {formData.er.er5}</Text>
            </View>
            <View style={{padding:5}}>
                <Text>6. Consigo alcanzar mis metas a pesar de las dificultades: {formData.er.er6}</Text>
            </View>
            <View style={{padding:5}}>
                <Text>7. Puedo mantener la concentración bajo presión: {formData.er.er7}</Text>
            </View>
            <View style={{padding:5}}>
                <Text>8. Dificílmente me desanimo por los fracasos: {formData.er.er8}</Text>
            </View>
            <View style={{padding:5}}>
                <Text>9. Me defino como una persona fuerte: {formData.er.er9}</Text>
            </View>
            <View style={{padding:5}}>
                <Text>10. Puedo manejar los sentimientos desagradables: {formData.er.er10}</Text>
            </View>
            <Text style={{fontWeight: 'bold'}}>
                INQ
            </Text>
            <Text style={{fontWeight: 'bold'}}>
                1 "Nada en absoluto"
            </Text>
            <Text style={{fontWeight: 'bold'}}>
                2 "Casi nada"
            </Text>
            <Text style={{fontWeight: 'bold'}}>
                3 "Un poco"
            </Text>
            <Text style={{fontWeight: 'bold'}}>
                4 "No estoy seguro/a"
            </Text>
            <Text style={{fontWeight: 'bold'}}>            
                5 "Moderadamente"
            </Text>
            <Text style={{fontWeight: 'bold'}}>            
                6 "Bastante"
            </Text>
            <Text style={{fontWeight: 'bold'}}>            
                7 "Extremadamente"
            </Text>
            <View style={{padding:5}}>
                <Text>1. Los que me rodean estarían mejor si me fuera: {formData.inq.inq1}</Text>
            </View>
            <View style={{padding:5}}>
                <Text>2. Los que me rodean serían más felices sin mí: {formData.inq.inq2}</Text>
            </View>
            <View style={{padding:5}}>
                <Text>3. Creo que soy una carga para la sociedad: {formData.inq.inq3}</Text>
            </View>
            <View style={{padding:5}}>
                <Text>4. Creo que mi muerte sería un alivio para los demás: {formData.inq.inq4}</Text>
            </View>
            <View style={{padding:5}}>
                <Text>5. Creo que los que me rodean, desearían deshacerse de mí: {formData.inq.inq5}</Text>
            </View>
            <View style={{padding:5}}>
                <Text>6. Creo que empeoro las cosas para los que me rodean: {formData.inq.inq6}</Text>
            </View>
            <View style={{padding:5}}>
                <Text>7. Los demás se preocupan por mí: {formData.inq.inq7}</Text>
            </View>
            <View style={{padding:5}}>
                <Text>8. Siento que encajo, que he encontrado mi lugar en el mundo: {formData.inq.inq8}</Text>
            </View>
            <View style={{padding:5}}>
                <Text>9. Me relaciono muy poco con mis seres queridos: {formData.inq.inq9}</Text>
            </View>
            <View style={{padding:5}}>
                <Text>10. Tengo la suerte de tener muchos/as amigos/as que me cuidan y apoyan: {formData.inq.inq10}</Text>
            </View>
            <View style={{padding:5}}>
                <Text>11. Me siento desconectado de los demás: {formData.inq.inq11}</Text>
            </View>
            <View style={{padding:5}}>
                <Text>12. A menudo me siento como un extraño cuando quedo con gente: {formData.inq.inq12}</Text>
            </View>
            <View style={{padding:5}}>
                <Text>13. Siento que hay personas a las que puedo recurrir en momentos de necesidad: {formData.inq.inq13}</Text>
            </View>
            <View style={{padding:5}}>
                <Text>14. Me siento cerca de otras personas: {formData.inq.inq14}</Text>
            </View>
            <View style={{padding:5}}>
                <Text>15. Cada día tengo al menos una interacción (con alguien) que puede considerarse satisfactoria: {formData.inq.inq15}</Text>
            </View>
            <Text style={{fontWeight: 'bold'}}>
                SENA
            </Text>
            <Text style={{fontWeight: 'bold'}}>
                1 "Nunca o casi nunca"
            </Text>
            <Text style={{fontWeight: 'bold'}}>
                2 "Pocas veces"
            </Text>
            <Text style={{fontWeight: 'bold'}}>
                3 "Algunas veces"
            </Text>
            <Text style={{fontWeight: 'bold'}}>
                4 "Muchas veces"
            </Text>
            <Text style={{fontWeight: 'bold'}}>            
                5 "Siempre o casi siempre"
            </Text>
            <View style={{padding:5}}>
                <Text>19. Mis padres me pegan: {formData.sena.sena19}</Text>
            </View>
            <View style={{padding:5}}>
                <Text>23. Grito cuando me enfado o enojo: {formData.sena.sena23}</Text>
            </View>
            <View style={{padding:5}}>
                <Text>69. Me cuesta controlar mis emociones: {formData.sena.sena89}</Text>
            </View>
            <View style={{padding:5}}>
                <Text>99. Tengo problemas en casa: {formData.sena.sena99}</Text>
            </View>
            <View style={{padding:5}}>
                <Text>103. Amenazo a otros para conseguir lo que quiero: {formData.sena.sena103}</Text>
            </View>
            <View style={{padding:5}}>
                <Text>111. Tengo ganas de llorar: {formData.sena.sena111}</Text>
            </View>
            <View style={{padding:5}}>
                <Text>112. Tengo ataques de nervios o de ansiedad: {formData.sena.sena112}</Text>
            </View>
            <View style={{padding:5}}>
                <Text>115. Me insultan en el colegio, instituto o universidad: {formData.sena.sena115}</Text>
            </View>
            <View style={{padding:5}}>
                <Text>117. Me cuesta concentrarme: {formData.sena.sena117}</Text>
            </View>
            <View style={{padding:5}}>
                <Text>129. Me angustian o agobian mis problemas: {formData.sena.sena129}</Text>
            </View>
            <View style={{padding:5}}>
                <Text>137. Me siento solo/a: {formData.sena.sena137}</Text>
            </View>
            <View style={{padding:5}}>
                <Text>139. Pego a otros cuando me enfado o enojo: {formData.sena.sena139}</Text>
            </View>
            <View style={{padding:5}}>
                <Text>141. Pienso que mi vida no tiene sentido: {formData.sena.sena141}</Text>
            </View>
            <View style={{padding:5}}>
                <Text>146. Hago locuras para divertirme: {formData.sena.sena146}</Text>
            </View>
            <View style={{padding:5}}>
                <Text>150. Mis profesores dicen que no presto atención en clase: {formData.sena.sena150}</Text>
            </View>
            <View style={{padding:5}}>
                <Text>188. Tengo amigos de verdad: {formData.sena.sena188}</Text>
            </View>
            <Text style={{fontWeight: 'bold'}}>
                Información sobre autolesión
            </Text>
            <View style={{padding:5}}>
                <Text>1. ¿Durante el último año te has implicado intencionadamente daño (por ejemplo: cortarte o arañarte la piel, golpearte o morderte a ti mismo,...)?: {yesNoData[formData.injury.injury1]}</Text>
            </View>
            <View style={{padding:5}}>
                <Text>1. Indique la edad de tu padre en el momento de tu nacimiento (años): {formData.family.padre_adolescente}</Text>
            </View>
            <View style={{padding:5}}>
                <Text>2. Indique la edad de tu madre en el momento de tu nacimiento (años): {formData.family.madre_adolescente}</Text>
            </View>
            <View style={{padding:5}}>
                <Text>3. Convives con tus padres en la misma casa habitualmente: {yesNoData[formData.family.familia_monoparental]}</Text>
            </View>
            <View style={{padding:5}}>
                <Text>4. Indica si tus padres están separados o divorciados: {yesNoData[formData.family.padres_divorciados]}</Text>
            </View>
            <View style={{padding:5}}>
                <Text>5. Indica si alguno de tus padres ha recibido tratamiento psicológico o psiquiátrico: {yesNoData[formData.family.tratamiento_psicologico_padre_madre]}</Text>
            </View>
            <View style={{padding:5}}>
                <Text>6. Indica si alguno de tus padres ha recibido tratamiento por consumo de drogas o alcohol: {yesNoData[formData.family.adiccion_padre_madre]}</Text>
            </View>
            <View style={{padding:5}}>
                <Text>7. Indica si las relaciones con tus padres son conflictivas o problemáticas (tensión, rechazo, desinterés, peleas frecuentes...): {yesNoData[formData.family.relaciones_conflictivas_hijo_padre_madre]}</Text>
            </View>
            <View style={{padding:5}}>
                <Text>8. Consideras que tu familia está reconstruida: {yesNoData[formData.family.familia_reconstruida]}</Text>
            </View>
        </View>
    );
};
