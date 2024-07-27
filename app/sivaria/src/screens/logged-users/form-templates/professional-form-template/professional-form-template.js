import React from 'react';
import { View, Text, StyleSheet } from 'react-native';


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

export const ProfessionalFormTemplate = ({ formData }) => {
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
                <View style={{padding:5}}>
                    <Text style={{fontWeight:'bold'}}>
                        ¿Situación económica familiar precaria? {yesNoData[formData.family.situacion_economica_precaria]}
                    </Text>
                </View>
                <View style={{padding:5}}>
                    <Text style={{fontWeight:'bold'}}>
                        Ingreso familiar mensual (aproximado): {formData.family.ingreso_familiar_mensual}€
                    </Text>
                </View>
                <View style={{padding:5}}>
                    <Text style={{fontWeight:'bold'}}>Situación laboral actual del padre: {parentsJobSituationData[formData.social_data.job_situation_father]}</Text>
                </View>
                <View style={{padding:5}}>
                    <Text style={{fontWeight:'bold'}}>Situación laboral actual de la madre: {parentsJobSituationData[formData.social_data.job_situation_mother]}</Text>
                </View>
                <View style={{padding:5}}>
                    <Text style={{fontWeight:'bold'}}>Estudios del padre o figura parental 1: {parentsAcademicLevel[formData.social_data.academic_level_father]}</Text>
                </View>
                <View style={{padding:5}}>
                    <Text style={{fontWeight:'bold'}}>Estudios de la madre o figura parental 2: {parentsAcademicLevel[formData.social_data.academic_level_mother]}</Text>
                </View>
                <View style={{padding:5}}>
                    <Text style={{fontWeight:'bold'}}>Edad del padre al momento del nacimiento del hijo/a: (en años): {formData.family.padre_adolescente}</Text>
                </View>
                <View style={{padding:5}}>
                    <Text style={{fontWeight:'bold'}}>Edad de la madre al momento del nacimiento del hijo/a: (en años): {formData.family.madre_adolescente}</Text>
                </View>
                <View style={{padding:5}}>
                    <Text style={{fontWeight:'bold'}}>Hogar monoparental: {yesNoData[formData.family.familia_monoparental]}</Text>
                </View>
                <View style={{padding:5}}>
                    <Text style={{fontWeight:'bold'}}>Indique si los padres están separados o divorciados: {yesNoData[formData.family.padres_divorciados]}</Text>
                </View>
                <View style={{padding:5}}>
                    <Text style={{fontWeight:'bold'}}>¿Existen antecedentes de tratamiento de salud mental en cualquiera de sus figuras parentales? {yesNoData[formData.family.tratamiento_psicologico_padre_madre]}</Text>
                </View>
                <View style={{padding:5}}>
                    <Text style={{fontWeight:'bold'}}>¿Alguno de los padres/madres ha sido tratado por problemas de drogas y alcohol? {yesNoData[formData.family.adiccion_padre_madre]}</Text>
                </View>
                <View style={{padding:5}}>
                    <Text style={{fontWeight:'bold'}}>Hogar reconstruido: {yesNoData[formData.family.familia_reconstruida]}</Text>
                </View>
                <View style={{padding:5}}>
                    <Text style={{fontWeight:'bold'}}>Supervisión parental insuficiente: {yesNoData[formData.family.supervision_parental_insuficiente]}</Text>
                </View>
                <View style={{padding:5}}>
                    <Text style={{fontWeight:'bold'}}>Relaciones conflictivas o problemáticas con los padres (tensión, negligencia, desinterés, peleas frecuentes): {yesNoData[formData.family.relaciones_conflictivas_hijo_padre_madre]}</Text>
                </View>
                <View style={{padding:5}}>
                    <Text style={{fontWeight:'bold'}}>Problemas interparentales (discusiones de pareja, apatía, insatisfacción o mala comunicación entre padres/madres): {yesNoData[formData.family.maltrato_a_la_pareja]}</Text>
                </View>
                <View style={{padding:5}}>
                    <Text style={{fontWeight:'bold'}}>Existencia de Maltrato (Abuso físico, abuso sexual del niño por parte de un familiar, negligencia o abandono, explotación, ...): {yesNoData[formData.family.maltrato_al_adolescente]}</Text>
                </View>
                <View style={{padding:5}}>
                    <Text style={{fontWeight:'bold'}}>Acontecimientos de Pérdida/duelo: p. ej., muerte de un padre, hermano o amigo, separación de los padres: {yesNoData[formData.family.duelo]}</Text>
                </View>
            </View>
        </>
    );
};
