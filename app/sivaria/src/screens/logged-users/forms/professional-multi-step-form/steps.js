import React, { useState, useEffect } from 'react';
import { View, Text, StyleSheet, TextInput } from 'react-native';
import Dropdown from '../../../../components/dropdown';
import SivariaInput from '../../../../components/sivaria-input';
import SivariaRadioButton from '../../../../components/sivaria-radio-button';


const courses = [
    { label: 'Ninguno', value: 'ninguno'},
    { label: 'Primaria', value: 'primaria' },
    { label: 'ESO', value: 'eso'},
    { label: 'Bachillerato', value: 'bachillerato'},
    { label: 'Universidad', value: 'universidad'},
    { label: 'Otro', value: 'otro' },
];
const genderData = [
    { label:'Hombre', value: 'hombre' },
    { label:'Mujer', value: 'mujer' },
    { label:'Otro', value: 'otro' },
];
const transData = [
    { label:'Sí', value: 'si' },
    { label:'No', value: 'no' },
    { label:'No estoy seguro/a de ser transgénero', value: 'no_se' },
];
const parentsJobSituationData = [
    { label:'No trabaja', value: 'no_trabaja' },
    { label:'Trabaja', value: 'trabaja' },
    { label:'Pensionado (recibe una paga o ayuda del Estado)', value: 'pensionado' },
];
const parentsAcademicLevel = [
    { label:'Ninguno', value: 'ninguno' },
    { label:'Bachillerato', value: 'bachillerato' },
    { label:'Formación Profesional', value: 'formacion_profesional' },
    { label:'Universidad', value: 'universidad' },
    { label:'Otro', value: 'otro' },
];

const academicPerformanceData = [
    { label:'Insuficiente', value: 'insuficiente' },
    { label:'Suficiente', value: 'suficiente' },
    { label:'Notable', value: 'notable' },
    { label:'Sobresaliente', value: 'sobresaliente' },
    { label:'Extraordinario', value: 'extraordinario' },
];
const yesNoData = [
    { label:'Sí', value: 'si' },
    { label:'No', value: 'no' },
];
const selfPerceptionData = [
    { label:'0', value: '0' },
    { label:'1', value: '1' },
    { label:'2', value: '2' },
    { label:'3', value: '3' },
    { label:'4', value: '4' },
    { label:'5', value: '5' },
    { label:'6', value: '6' },
];
const discriminationTypes = [
    { label: 'Ninguno', value: 'ninguno'},
    { label: 'Género', value: 'genero' },
    { label: 'Raza', value: 'raza'},
    { label: 'Orientación sexual', value: 'orientacion_sexual'},
    { label: 'Otro', value: 'otro' },
];
const zeroToFourOptions = [
    { label:'0', value: '0' },
    { label:'1', value: '1' },
    { label:'2', value: '2' },
    { label:'3', value: '3' },
    { label:'4', value: '4' },
];

const oneToFiveOptions = [
    { label:'1', value: '1' },
    { label:'2', value: '2' },
    { label:'3', value: '3' },
    { label:'4', value: '4' },
    { label:'5', value: '5' },
];

const oneToSevenOptions = [
    { label:'1', value: '1' },
    { label:'2', value: '2' },
    { label:'3', value: '3' },
    { label:'4', value: '4' },
    { label:'5', value: '5' },
    { label:'6', value: '6' },
    { label:'7', value: '7' },
];

const Step1 = ({ stepData, setStepData, validations }) => {
    //const [localState, setLocalState] = useState(stepData.step1 || '');
    const [localState, setLocalState] = useState({
        idPatient: stepData.step1.idPatient || '',
        course: stepData.step1.course || '',
        previousPsychiatricTreatment: stepData.step1.previousPsychiatricTreatment || '',
    });

    useEffect(() => {
        setLocalState({
            idPatient: stepData.step1.idPatient || '',
            course: stepData.step1.course || '',
            previousPsychiatricTreatment: stepData.step1.previousPsychiatricTreatment || '',
        });
    }, [stepData.step1]);

    const handleInputChange = (field, value) => {
        // Change function to handleInputChange(text)
        //setLocalState(text);
        //setStepData((prevData) => ({ ...prevData, step1: text }));
        const updatedState = { ...localState, [field]: value };
        setLocalState(updatedState);
        setStepData((prevData) => ({ ...prevData, step1: updatedState }));
    };

    return (
        <>
            <View style={{padding: 20, backgroundColor: 'white'}}>
                <View style={{padding: 5}}>
                    <Text style={{fontWeight:'bold'}}>Identificador (ID) Participante 
                        (siglas de nombre y apellidos de su hijo/a seguida de su 
                        fecha de nacimiento en seis dígitos ddmmaa; por ejemplo Juan Antonio Mesa Rodríguez 
                        nacido el 25/07/2015 = JAMR25072015):</Text>
                    <Text>Identificador (ID) Participante:</Text>
                    <SivariaInput 
                        placeholder={'ID Participante'}
                        value={stepData.step1.idPatient}
                        onChangeText={text => handleInputChange('idPatient', text )}
                        autoCorrect={false}
                        autoCapitalize={'none'} 
                        inputMode={'text'}
                    />
                    {validations.step1.idPatient && <Text style={styles.errorText}>El campo está vacío.</Text>}
                </View>
                <View style={{padding: 5}}>
                    <Text style={{fontWeight:'bold'}}>Curso:</Text>
                    <SivariaRadioButton 
                        data={courses} 
                        option={stepData.step1.course} 
                        onSelect={text => handleInputChange('course', text)}
                    />
                    {validations.step1.course && <Text style={styles.errorText}>El campo está vacío.</Text>}
                </View>
                <View style={{padding: 5}}>
                    <Text style={{fontWeight:'bold'}}>Tratamiento farmacológico:</Text>
                    <SivariaRadioButton 
                        data={yesNoData} 
                        option={stepData.step1.previousPsychiatricTreatment} 
                        onSelect={text => handleInputChange('previousPsychiatricTreatment', text)}
                    />
                    {validations.step1.previousPsychiatricTreatment && <Text style={styles.errorText}>El campo está vacío.</Text>}
                </View>
            </View>
        </>
    );
};

const Step2 = ({ stepData, setStepData, validations }) => {
    const [localState, setLocalState] = useState({
        family12: stepData.step2.family12 || '',
        family13: stepData.step2.family13 || '',
        jobSituationFather: stepData.step2.jobSituationFather || '',
        jobSituationMother: stepData.step2.jobSituationMother || '',
        academicLevelFather: stepData.step2.academicLevelFather || '',
        academicLevelMother: stepData.step2.academicLevelMother || '',
        family1: stepData.step2.family1 || '',
        family2: stepData.step2.family2 || '',
        family3: stepData.step2.family3 || '',
    });

    useEffect(() => {
        setLocalState({
            family12: stepData.step2.family12 || '',
            family13: stepData.step2.family13 || '',
            jobSituationFather: stepData.step2.jobSituationFather || '',
            jobSituationMother: stepData.step2.jobSituationMother || '',
            academicLevelFather: stepData.step2.academicLevelFather || '',
            academicLevelMother: stepData.step2.academicLevelMother || '',
            family1: stepData.step2.family1 || '',
            family2: stepData.step2.family2 || '',
            family3: stepData.step2.family3 || '',
        });
    }, [stepData.step2]);

    const handleInputChange = (field, value) => {
        // Change function to handleInputChange(text)
        //setLocalState(text);
        //setStepData((prevData) => ({ ...prevData, step1: text }));
        const updatedState = { ...localState, [field]: value };
        setLocalState(updatedState);
        setStepData((prevData) => ({ ...prevData, step2: updatedState }));
    };

    return (
        <View style={{padding:20, backgroundColor: 'white'}}>
            <View style={{padding:5}}>
                <Text>
                    Situación económica familiar precaria
                </Text>
                <SivariaInput 
                    placeholder={'Ingreso familiar mensual'}
                    value={stepData.step2.family12}
                    onChangeText={text => handleInputChange('family12', text )}
                    autoCorrect={false}
                    autoCapitalize={'none'} 
                    inputMode={'numeric'}
                />    
                {validations.step2.family12 && <Text style={styles.errorText}>El campo está vacío.</Text>}
            </View>
            <View style={{padding:5}}>
                <Text style={{fontWeight:'bold'}}>
                    Ingreso familiar mensual (aproximado)
                </Text>
                <SivariaRadioButton data={yesNoData} option={stepData.step2.family13} onSelect={text => handleInputChange('family13', text)}/>
                {validations.step2.family13 && <Text style={styles.errorText}>El campo está vacío.</Text>}
            </View>
            <View style={{padding:5}}>
                <Text style={{fontWeight:'bold'}}>Situación laboral actual del padre:</Text>
                <SivariaRadioButton option={stepData.step2.jobSituationFather} data={parentsJobSituationData} onSelect={text => handleInputChange('jobSituationFather', text)}/>
                {validations.step2.jobSituationFather && <Text style={styles.errorText}>El campo está vacío.</Text>}

            </View>
            <View style={{padding:5}}>
                <Text style={{fontWeight:'bold'}}>Situación laboral actual de la madre:</Text>
                <SivariaRadioButton option={stepData.step2.jobSituationMother} data={parentsJobSituationData} onSelect={text => handleInputChange('jobSituationMother', text)}/>
                {validations.step2.jobSituationMother && <Text style={styles.errorText}>El campo está vacío.</Text>}
            </View>
            <View style={{padding:5}}>
                <Text style={{fontWeight:'bold'}}>Estudios del padre o figura parental 1:</Text>
                <SivariaRadioButton option={stepData.step2.academicLevelFather} data={parentsAcademicLevel} onSelect={text => handleInputChange('academicLevelFather', text)}/>
                {validations.step2.academicLevelFather && <Text style={styles.errorText}>El campo está vacío.</Text>}
            </View>
            <View style={{padding:5}}>
                <Text style={{fontWeight:'bold'}}>Estudios de la madre o figura parental 2:</Text>
                <SivariaRadioButton option={stepData.step2.academicLevelMother} data={parentsAcademicLevel} onSelect={text => handleInputChange('academicLevelMother', text)}/>
                {validations.step2.academicLevelMother && <Text style={styles.errorText}>El campo está vacío.</Text>}

            </View>
            <View style={{padding:5}}>
                <Text>Edad del padre al momento del nacimiento del hijo/a (en años)</Text>
                <SivariaInput 
                    placeholder={'Edad padre'}
                    value={stepData.step2.family1}
                    onChangeText={text => handleInputChange('family1', text )}
                    autoCorrect={false}
                    autoCapitalize={'none'} 
                    inputMode={'numeric'}
                />
                {validations.step2.family1 && <Text style={styles.errorText}>El campo está vacío.</Text>}

            </View>
            <View style={{padding:5}}>
                <Text>Edad de la madre al momento del nacimiento del hijo/a (en años)</Text>
                <SivariaInput 
                    placeholder={'Edad madre'}
                    value={stepData.step2.family2}
                    onChangeText={text => handleInputChange('family2', text )}
                    autoCorrect={false}
                    autoCapitalize={'none'} 
                    inputMode={'numeric'}
                />
                {validations.step2.family2 && <Text style={styles.errorText}>El campo está vacío.</Text>}

            </View>
            <View style={{padding:5}}>
                <Text>Hogar monoparental</Text>
                <SivariaRadioButton data={yesNoData} option={stepData.step2.family3} onSelect={text => handleInputChange('family3', text)}/>
                {validations.step2.family3 && <Text style={styles.errorText}>El campo está vacío.</Text>}

            </View>
        </View>
    );
};

const Step3 = ({ stepData, setStepData, validations }) => {
    const [localState, setLocalState] = useState({
        family4: stepData.step3.family4 || '',
        family5: stepData.step3.family5 || '',
        family6: stepData.step3.family6 || '',
        family7: stepData.step3.family7 || '',
        family8: stepData.step3.family8 || '',
        family9: stepData.step3.family9 || '',
        family10: stepData.step3.family10 || '',
        family11: stepData.step3.family11 || '',
        family14: stepData.step3.family14 || '',
    });

    useEffect(() => {
        setLocalState({
            family4: stepData.step3.family4 || '',
            family5: stepData.step3.family5 || '',
            family6: stepData.step3.family6 || '',
            family7: stepData.step3.family7 || '',
            family8: stepData.step3.family8 || '',
            family9: stepData.step3.family9 || '',
            family10: stepData.step3.family10 || '',
            family11: stepData.step3.family11 || '',
            family14: stepData.step3.family14 || '',
        });
    }, [stepData.step3]);

    const handleInputChange = (field, value) => {
        // Change function to handleInputChange(text)
        //setLocalState(text);
        //setStepData((prevData) => ({ ...prevData, step1: text }));
        const updatedState = { ...localState, [field]: value };
        setLocalState(updatedState);
        setStepData((prevData) => ({ ...prevData, step3: updatedState }));
    };

    return (
        <View style={{padding:20, backgroundColor: 'white'}}>
            <View style={{padding:5}}>
                <Text>Indique si los padres están separados o divorciados</Text>
                <SivariaRadioButton data={yesNoData} option={stepData.step3.family4} onSelect={text => handleInputChange('family4', text)}/>
                {validations.step3.family4 && <Text style={styles.errorText}>El campo está vacío.</Text>}

            </View>
            <View style={{padding:5}}>
                <Text>¿Existen antecedentes de tratamiento de salud mental en cualquiera de sus figuras parentales?</Text>
                <SivariaRadioButton data={yesNoData} option={stepData.step3.family5} onSelect={text => handleInputChange('family5', text)}/>                
                {validations.step3.family5 && <Text style={styles.errorText}>El campo está vacío.</Text>}

            </View>
            <View style={{padding:5}}>
                <Text>¿Alguno de los padres/madres ha sido tratado por problemas de drogas y alcohol?</Text>
                <SivariaRadioButton data={yesNoData} option={stepData.step3.family6} onSelect={text => handleInputChange('family6', text)}/>                
                {validations.step3.family6 && <Text style={styles.errorText}>El campo está vacío.</Text>}

            </View>
            <View style={{padding:5}}>
                <Text>Hogar reconstruido</Text>
                <SivariaRadioButton data={yesNoData} option={stepData.step3.family8} onSelect={text => handleInputChange('family8', text)}/>                
                {validations.step3.family8 && <Text style={styles.errorText}>El campo está vacío.</Text>}

            </View>
            <View style={{padding:5}}>
                <Text>Supervisión parental insuficiente</Text>
                <SivariaRadioButton data={yesNoData} option={stepData.step3.family9} onSelect={text => handleInputChange('family9', text)}/>                
                {validations.step3.family9 && <Text style={styles.errorText}>El campo está vacío.</Text>}

            </View>
            <View style={{padding:5}}>
                <Text>Relaciones conflictivas o problemáticas con los padres (tensión, negligencia, desinterés, peleas frecuentes)</Text>
                <SivariaRadioButton data={yesNoData} option={stepData.step3.family7} onSelect={text => handleInputChange('family7', text)}/>                
                {validations.step3.family7 && <Text style={styles.errorText}>El campo está vacío.</Text>}

            </View>
            <View style={{padding:5}}>
                <Text>Problemas interparentales (discusiones de pareja, apatía, insatisfacción o mala comunicación entre padres/madres)</Text>
                <SivariaRadioButton data={yesNoData} option={stepData.step3.family11} onSelect={text => handleInputChange('family11', text)}/>                
                {validations.step3.family11 && <Text style={styles.errorText}>El campo está vacío.</Text>}

            </View>
            <View style={{padding:5}}>
                <Text>Existencia de Maltrato (Abuso físico, abuso sexual del niño por parte de un familiar, negligencia o abandono, explotación, ...)</Text>
                <SivariaRadioButton data={yesNoData} option={stepData.step3.family10} onSelect={text => handleInputChange('family10', text)}/>                
                {validations.step3.family10 && <Text style={styles.errorText}>El campo está vacío.</Text>}

            </View>
            <View style={{padding:5}}>
                <Text>Acontecimientos de Pérdida/duelo: p. ej., muerte de un padre, hermano o amigo, separación de los padres</Text>
                <SivariaRadioButton data={yesNoData} option={stepData.step3.family14} onSelect={text => handleInputChange('family14', text)}/>                
                {validations.step3.family14 && <Text style={styles.errorText}>El campo está vacío.</Text>}

            </View>
        </View>
    );
};

const styles = StyleSheet.create({
    container: {
        flex: 1,
        justifyContent: 'center',
        alignItems: 'center',
        padding: 20,
        backgroundColor: '#f5f5f5'
    },
    text: {
        fontSize: 24,
        fontWeight: 'bold'
    },
    errorText: {
        color: 'red',
        marginTop: 5,
    },

    
    input: {
        width: '80%',
        padding: 10,
        borderColor: '#ccc',
        borderWidth: 1,
        borderRadius: 5,
        marginTop: 20
    }
});
// Repite esto para todos los componentes de tus pasos hasta Step10

export { Step1, Step2, Step3 };