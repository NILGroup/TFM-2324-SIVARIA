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

const oneToFourOptions = [
    { label:'1', value: '1' },
    { label:'2', value: '2' },
    { label:'3', value: '3' },
    { label:'4', value: '4' },
];

const Step1 = ({ stepData, setStepData }) => {
    //const [localState, setLocalState] = useState(stepData.step1 || '');
    const [localState, setLocalState] = useState({ 
        idChild: stepData.step1.idChild || '',
        course: stepData.step1.course || '',
    });

    useEffect(() => {
        setLocalState({
            idChild: stepData.step1.idChild || '',
            course: stepData.step1.course || '',
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
                    <Text style={{fontWeight:'bold'}}>Identificador (ID) Participante:</Text>
                    <SivariaInput 
                        placeholder={'ID Participante'}
                        value={stepData.step1.idChild}
                        onChangeText={text => handleInputChange('idChild', text )}
                        autoCorrect={false}
                        autoCapitalize={'none'} 
                        inputMode={'text'}
                    />
                </View>
                <View style={{padding: 5}}>
                    <Text style={{fontWeight:'bold'}}>Curso:</Text>
                    <SivariaRadioButton 
                        data={courses} 
                        option={stepData.step1.course} 
                        onSelect={text => handleInputChange('course', text)}
                    />
                </View>
            </View>
        </>
    );
};

const Step2 = ({ stepData, setStepData }) => {
    const [localState, setLocalState] = useState({
        sena104: stepData.step2.sena104 || '',
        sena117: stepData.step2.sena117 || '',
        sena118: stepData.step2.sena118 || '',
        sena121: stepData.step2.sena121 || '',
        sena123: stepData.step2.sena123 || '',
        sena124: stepData.step2.sena124 || '',
        sena125: stepData.step2.sena125 || '',
        sena135: stepData.step2.sena135 || '',
        sena137: stepData.step2.sena137 || '',
        sena138: stepData.step2.sena138 || '',
        sena139: stepData.step2.sena139 || '',
        sena140: stepData.step2.sena140 || '',
        sena145: stepData.step2.sena145 || '',
        sena146: stepData.step2.sena146 || '',    
        sena148: stepData.step2.sena148 || '',
        sena154: stepData.step2.sena154 || '',
    });

    useEffect(() => {
        setLocalState({
            sena104: stepData.step2.sena104 || '',
            sena117: stepData.step2.sena117 || '',
            sena118: stepData.step2.sena118 || '',
            sena121: stepData.step2.sena121 || '',
            sena123: stepData.step2.sena123 || '',
            sena124: stepData.step2.sena124 || '',
            sena125: stepData.step2.sena125 || '',
            sena135: stepData.step2.sena135 || '',
            sena137: stepData.step2.sena137 || '',
            sena138: stepData.step2.sena138 || '',
            sena139: stepData.step2.sena139 || '',
            sena140: stepData.step2.sena140 || '',
            sena145: stepData.step2.sena145 || '',
            sena146: stepData.step2.sena146 || '',    
            sena148: stepData.step2.sena148 || '',
            sena154: stepData.step2.sena154 || '',
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
            <Text style={{fontWeight:'bold'}}>
                SENA
            </Text>
            <Text style={{fontWeight:'bold'}}>
                A continuación encontrará varias frases que describen comportamientos o conductas que pueden
                mostrar los adolescentes. Por favor, lea detenidamente cada una de ellas e indique con qué 
                frecuencia su hijo/a o familiar ha mostrado esos comportamientos durante los últimos 6 meses
            </Text>
            <Text style={{fontWeight:'bold'}}>
                Para responder tendrá que elegir en cada frase una de las 5 opciones siguientes y marcarla:
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
                <Text style={{fontWeight:'bold'}}>104. Sus compañeros de clase le aíslan.</Text>
                <SivariaRadioButton option={stepData.step2.sena104} data={oneToFiveOptions} onSelect={text => handleInputChange('sena104', text)}/>
            </View>
            <View style={{padding:5}}>
                <Text style={{fontWeight:'bold'}}>117. Se mete en peleas.</Text>
                <SivariaRadioButton option={stepData.step2.sena117} data={oneToFiveOptions} onSelect={text => handleInputChange('sena117', text)}/>
            </View>
            <View style={{padding:5}}>
                <Text style={{fontWeight:'bold'}}>118. Se queja de estar enfermo aunque el médico dice que todo está bien.</Text>
                <SivariaRadioButton option={stepData.step2.sena118} data={oneToFiveOptions} onSelect={text => handleInputChange('sena118', text)}/>
            </View>
            <View style={{padding:5}}>
                <Text style={{fontWeight:'bold'}}>121. Creo que consume drogas.</Text>
                <SivariaRadioButton option={stepData.step2.sena121} data={oneToFiveOptions} onSelect={text => handleInputChange('sena121', text)}/>
            </View>
            <View style={{padding:5}}>
                <Text style={{fontWeight:'bold'}}>
                    123. Se divierte molestando a otros.
                </Text>
                <SivariaRadioButton data={oneToFiveOptions} option={stepData.step2.sena123} onSelect={text => handleInputChange('sena123', text)}/>
            </View>
            <View style={{padding:5}}>
                <Text style={{fontWeight:'bold'}}>
                    124. Hace cosas ilegales.    
                </Text>
                <SivariaRadioButton data={oneToFiveOptions} option={stepData.step2.sena124} onSelect={text => handleInputChange('sena124', text)}/>
            </View>
            <View style={{padding:5}}>
                <Text style={{fontWeight:'bold'}}>
                    125. Se integra con facilidad en los grupos.    
                </Text>
                <SivariaRadioButton data={oneToFiveOptions} option={stepData.step2.sena125} onSelect={text => handleInputChange('sena125', text)}/>
            </View>
            <View style={{padding:5}}>
                <Text style={{fontWeight:'bold'}}>
                    135. Se preocupa por cosas sin importancia.    
                </Text>
                <SivariaRadioButton data={oneToFiveOptions} option={stepData.step2.sena135} onSelect={text => handleInputChange('sena135', text)}/>
            </View>
            <View style={{padding:5}}>
                <Text style={{fontWeight:'bold'}}>
                    137. Se esfuerza en sus estudios.    
                </Text>
                <SivariaRadioButton data={oneToFiveOptions} option={stepData.step2.sena137} onSelect={text => handleInputChange('sena137', text)}/>
            </View>
            <View style={{padding:5}}>
                <Text style={{fontWeight:'bold'}}>
                    138. Su mirada es triste, sin brillo.    
                </Text>
                <SivariaRadioButton data={oneToFiveOptions} option={stepData.step2.sena138} onSelect={text => handleInputChange('sena138', text)}/>
            </View>
            <View style={{padding:5}}>
                <Text style={{fontWeight:'bold'}}>
                    139. Es sociable.
                </Text>
                <SivariaRadioButton data={oneToFiveOptions} option={stepData.step2.sena139} onSelect={text => handleInputChange('sena139', text)}/>
            </View>
            <View style={{padding:5}}>
                <Text style={{fontWeight:'bold'}}>
                    140. Le cuesta controlar sus emociones.
                </Text>
                <SivariaRadioButton data={oneToFiveOptions} option={stepData.step2.sena140} onSelect={text => handleInputChange('sena140', text)}/>
            </View>
            <View style={{padding:5}}>
                <Text style={{fontWeight:'bold'}}>
                    145. Le da demasiadas vueltas a las cosas.
                </Text>
                <SivariaRadioButton data={oneToFiveOptions} option={stepData.step2.sena145} onSelect={text => handleInputChange('sena145', text)}/>
            </View>
            <View style={{padding:5}}>
                <Text style={{fontWeight:'bold'}}>
                    146. Se obsesionan con adelgazar.
                </Text>
                <SivariaRadioButton data={oneToFiveOptions} option={stepData.step2.sena146} onSelect={text => handleInputChange('sena146', text)}/>
            </View>
            <View style={{padding:5}}>
                <Text style={{fontWeight:'bold'}}>
                    148. Dice que tiene náuseas o ganas de vomitar.
                </Text>
                <SivariaRadioButton data={oneToFiveOptions} option={stepData.step2.sena148} onSelect={text => handleInputChange('sena148', text)}/>
            </View>
            <View style={{padding:5}}>
                <Text style={{fontWeight:'bold'}}>
                    154. Es simpático con los que le rodean.
                </Text>
                <SivariaRadioButton data={oneToFiveOptions} option={stepData.step2.sena154} onSelect={text => handleInputChange('sena154', text)}/>
            </View>
        </View>
    );
};

const Step3 = ({ stepData, setStepData }) => {
    const [localState, setLocalState] = useState({
        family12: stepData.step3.family12 || '',
        family13: stepData.step3.family13 || '',
        jobSituationFather: stepData.step3.jobSituationFather || '',
        jobSituationMother: stepData.step3.jobSituationMother || '',
        academicLevelFather: stepData.step3.academicLevelFather || '',
        academicLevelMother: stepData.step3.academicLevelMother || '',
        family1: stepData.step3.family1 || '',
        family2: stepData.step3.family2 || '',
        family3: stepData.step3.family3 || '',
        family4: stepData.step3.family4 || '',
        family5: stepData.step3.family5 || '',
        family6: stepData.step3.family6 || '',
        family7: stepData.step3.family7 || '',
        family8: stepData.step3.family8 || '',
    });

    useEffect(() => {
        setLocalState({
            family12: stepData.step3.family12 || '',
            family13: stepData.step3.family13 || '',
            jobSituationFather: stepData.step3.jobSituationFather || '',
            jobSituationMother: stepData.step3.jobSituationMother || '',
            academicLevelFather: stepData.step3.academicLevelFather || '',
            academicLevelMother: stepData.step3.academicLevelMother || '',
            family1: stepData.step3.family1 || '',
            family2: stepData.step3.family2 || '',
            family3: stepData.step3.family3 || '',
            family4: stepData.step3.family4 || '',
            family5: stepData.step3.family5 || '',
            family6: stepData.step3.family6 || '',
            family7: stepData.step3.family7 || '',
            family8: stepData.step3.family8 || '',
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
            <Text style={{fontWeight:'bold'}}>
                Por favor, conteste o señale la casilla correspondiente en cada una de las cuestiones
                formluadas a continuación:
            </Text>
            <View style={{padding:5}}>
                <Text>
                    Indique los ingresos familiares familiares mensuales en euros (aproximado):
                </Text>
                <SivariaInput 
                    placeholder={'Ingreso familiar mensual'}
                    value={stepData.step3.family12}
                    onChangeText={text => handleInputChange('family12', text )}
                    autoCorrect={false}
                    autoCapitalize={'none'} 
                    inputMode={'numeric'}
                />    
            </View>
            <View style={{padding:5}}>
                <Text style={{fontWeight:'bold'}}>
                    ¿Considera que poseen una situación económica familiar precaria?
                </Text>
                <SivariaRadioButton data={yesNoData} option={stepData.step3.femaleSelfPerception} onSelect={text => handleInputChange('family13', text)}/>
            </View>
            <View style={{padding:5}}>
                <Text style={{fontWeight:'bold'}}>Indica la situación laboral actual de tu padre:</Text>
                <SivariaRadioButton option={stepData.step3.jobSituationFather} data={parentsJobSituationData} onSelect={text => handleInputChange('jobSituationFather', text)}/>
            </View>
            <View style={{padding:5}}>
                <Text style={{fontWeight:'bold'}}>Indica la situación laboral actual de tu madre:</Text>
                <SivariaRadioButton option={stepData.step3.jobSituationMother} data={parentsJobSituationData} onSelect={text => handleInputChange('jobSituationMother', text)}/>
            </View>
            <View style={{padding:5}}>
                <Text style={{fontWeight:'bold'}}>Indica los estudios de tu padre o figura parental 1:</Text>
                <SivariaRadioButton option={stepData.step3.academicLevelFather} data={parentsAcademicLevel} onSelect={text => handleInputChange('academicLevelFather', text)}/>
            </View>
            <View style={{padding:5}}>
                <Text style={{fontWeight:'bold'}}>Indica los estudios de tu madre o figura parental 2:</Text>
                <SivariaRadioButton option={stepData.step3.academicLevelMother} data={parentsAcademicLevel} onSelect={text => handleInputChange('academicLevelMother', text)}/>
            </View>
            <View style={{padding:5}}>
                <Text>Indique la edad de tu padre en el momento de tu nacimiento (años):</Text>
                <SivariaInput 
                    placeholder={'Edad padre'}
                    value={stepData.step3.family1}
                    onChangeText={text => handleInputChange('family1', text )}
                    autoCorrect={false}
                    autoCapitalize={'none'} 
                    inputMode={'numeric'}
                />
            </View>
            <View style={{padding:5}}>
                <Text>Indique la edad de tu madre en el momento de tu nacimiento (años):</Text>
                <SivariaInput 
                    placeholder={'Edad madre'}
                    value={stepData.step3.family2}
                    onChangeText={text => handleInputChange('family2', text )}
                    autoCorrect={false}
                    autoCapitalize={'none'} 
                    inputMode={'numeric'}
                />
            </View>
            <View style={{padding:5}}>
                <Text>Conviven padre y madre en el hogar habitual con su hijo/a</Text>
                <SivariaRadioButton data={yesNoData} option={stepData.step3.family3} onSelect={text => handleInputChange('family3', text)}/>
            </View>
            <View style={{padding:5}}>
                <Text>Indique si los padres están separados o divorciados</Text>
                <SivariaRadioButton data={yesNoData} option={stepData.step3.family4} onSelect={text => handleInputChange('family4', text)}/>
            </View>
            <View style={{padding:5}}>
                <Text>Indica si alguna de las figuras parentales ha recibido tratamiento psicológico o psiquiátrico:</Text>
                <SivariaRadioButton data={yesNoData} option={stepData.step3.family5} onSelect={text => handleInputChange('family5', text)}/>                
            </View>
            <View style={{padding:5}}>
                <Text>Indica si alguna de las figuras parentales ha recibido tratamiento por consumo de drogas o alcohol</Text>
                <SivariaRadioButton data={yesNoData} option={stepData.step3.family6} onSelect={text => handleInputChange('family6', text)}/>                
            </View>
            <View style={{padding:5}}>
                <Text>Indica si las relaciones con su hijo/a son conflictivas o problemáticas (tensión, rechazo, desinterés, peleas frecuentes...):</Text>
                <SivariaRadioButton data={yesNoData} option={stepData.step3.family7} onSelect={text => handleInputChange('family7', text)}/>                
            </View>
            <View style={{padding:5}}>
                <Text>Indica si la familia ha sido reconstruida</Text>
                <SivariaRadioButton data={yesNoData} option={stepData.step3.family8} onSelect={text => handleInputChange('family8', text)}/>                
            </View>
        </View>
    );
};

const Step4 = ({ stepData, setStepData }) => {
    const [localState, setLocalState] = useState({
        parq1: stepData.step4.parq1 || '', 
        parq2: stepData.step4.parq2 || '',
        parq3: stepData.step4.parq3 || '',
        parq4: stepData.step4.parq4 || '',
        parq5: stepData.step4.parq5 || '',
        parq6: stepData.step4.parq6 || '',
        parq7: stepData.step4.parq7 || '',
        parq8: stepData.step4.parq8 || '',
        parq9: stepData.step4.parq9 || '',
        parq10: stepData.step4.parq10 || '',
        parq11: stepData.step4.parq11 || '',
        parq12: stepData.step4.parq12 || '',
        parq13: stepData.step4.parq13 || '',
        parq14: stepData.step4.parq14 || '',
    });

    useEffect(() => {
        setLocalState({
            parq1: stepData.step4.parq1 || '', 
            parq2: stepData.step4.parq2 || '',
            parq3: stepData.step4.parq3 || '',
            parq4: stepData.step4.parq4 || '',
            parq5: stepData.step4.parq5 || '',
            parq6: stepData.step4.parq6 || '',
            parq7: stepData.step4.parq7 || '',
            parq8: stepData.step4.parq8 || '',
            parq9: stepData.step4.parq9 || '',
            parq10: stepData.step4.parq10 || '',
            parq11: stepData.step4.parq11 || '',
            parq12: stepData.step4.parq12 || '',
            parq13: stepData.step4.parq13 || '',
            parq14: stepData.step4.parq14 || '',
        });
    }, [stepData.step4]);

    const handleInputChange = (field, value) => {
        const updatedState = { ...localState, [field]: value };
        setLocalState(updatedState);
        setStepData((prevData) => ({ ...prevData, step4: updatedState }));
    };

    return (
        <View style={{padding:20, backgroundColor: 'white'}}>
            <Text style={{fontWeight:'bold'}}>
                PARQ
            </Text>
            <Text style={{fontWeight:'bold'}}>
                Hay cuatro casillas después de cada frase. Responda en función de si en su caso el enunciado
                es básicamente:
                1. Básicamente incierto ("Casi nunca verdad").
                2. Cierto ocasionalmente ("A veces verdad").
                3. Cierto frecuentemente ("Muchas veces verdad"). 
                4. Cierto ("casi siempre verdad").
            </Text>
            <View style={{padding:5}}>
                <Text>1. Digo cosas buenas sobre mi hijo/a</Text>
                <SivariaRadioButton data={oneToFourOptions} option={stepData.step4.parq1} onSelect={text => handleInputChange('parq1', text)}/>
            </View>
            <View style={{padding:5}}>
                <Text>2. Presto atención a mi hijo/a</Text>
                <SivariaRadioButton data={oneToFourOptions} option={stepData.step4.parq2} onSelect={text => handleInputChange('parq2', text)}/>
            </View>
            <View style={{padding:5}}>
                <Text>3. Me preocupo de que mi hijo/a sepa exactamente lo que puede o no puede hacer</Text>
                <SivariaRadioButton data={oneToFourOptions} option={stepData.step4.parq3} onSelect={text => handleInputChange('parq3', text)}/>
            </View>
            <View style={{padding:5}}>
                <Text>4. Hago que mi hijo/a confíe en mí</Text>
                <SivariaRadioButton data={oneToFourOptions} option={stepData.step4.parq4} onSelect={text => handleInputChange('parq4', text)}/>
            </View>
            <View style={{padding:5}}>
                <Text>5. Pego a mi hijo/a cuando se lo merece</Text>
                <SivariaRadioButton data={oneToFourOptions} option={stepData.step4.parq5} onSelect={text => handleInputChange('parq5', text)}/>                
            </View>
            <View style={{padding:5}}>
                <Text>6. Mi hijo/a es un gran incordio para mí</Text>
                <SivariaRadioButton data={oneToFourOptions} option={stepData.step4.parq6} onSelect={text => handleInputChange('parq6', text)}/>                
            </View>
            <View style={{padding:5}}>
                <Text>7. Siempre le digo a mi hijo/a cómo debe comportarse</Text>
                <SivariaRadioButton data={oneToFourOptions} option={stepData.step4.parq7} onSelect={text => handleInputChange('parq7', text)}/>                
            </View>
            <View style={{padding:5}}>
                <Text>8. Castigo a mi hijo/a serveramente cuando estoy enfadado/a</Text>
                <SivariaRadioButton data={oneToFourOptions} option={stepData.step4.parq8} onSelect={text => handleInputChange('parq8', text)}/>                
            </View>
            <View style={{padding:5}}>
                <Text>9. Estoy demasiado ocupado/a para contestar las preguntas a mi hijo/a</Text>
                <SivariaRadioButton data={oneToFourOptions} option={stepData.step4.parq9} onSelect={text => handleInputChange('parq9', text)}/>                
            </View>
            <View style={{padding:5}}>
                <Text>10. No le gusto a mi hijo/a</Text>
                <SivariaRadioButton data={oneToFourOptions} option={stepData.step4.parq10} onSelect={text => handleInputChange('parq10', text)}/>                
            </View>
            <View style={{padding:5}}>
                <Text>11. Estoy realmente interesado/A en los asuntos de mi hijo/a</Text>
                <SivariaRadioButton data={oneToFourOptions} option={stepData.step4.parq11} onSelect={text => handleInputChange('parq11', text)}/>                
            </View>
            <View style={{padding:5}}>
                <Text>12. Digo muchas cosas desagradables a mi hijo/a</Text>
                <SivariaRadioButton data={oneToFourOptions} option={stepData.step4.parq12} onSelect={text => handleInputChange('parq12', text)}/>                
            </View>
            <View style={{padding:5}}>
                <Text>13. Presto atención a mi hijo/a cuando me pide ayuda</Text>
                <SivariaRadioButton data={oneToFourOptions} option={stepData.step4.parq13} onSelect={text => handleInputChange('parq13', text)}/>                
            </View>
            <View style={{padding:5}}>
                <Text>14. Insisto en que mi hijo/a haga exactamente lo que le digo</Text>
                <SivariaRadioButton data={oneToFourOptions} option={stepData.step4.parq14} onSelect={text => handleInputChange('parq14', text)}/>                
            </View>
        </View>
    );
};
const Step5 = ({ stepData, setStepData }) => {
    const [localState, setLocalState] = useState({
        parq15: stepData.step5.parq15 ||  '',
        parq16: stepData.step5.parq16 ||  '',
        parq17: stepData.step5.parq17 ||  '',
        parq18: stepData.step5.parq18 ||  '',
        parq19: stepData.step5.parq19 ||  '',
        parq20: stepData.step5.parq20 ||  '',
        parq21: stepData.step5.parq21 ||  '',
        parq22: stepData.step5.parq22 ||  '',
        parq23: stepData.step5.parq23 ||  '',
        parq24: stepData.step5.parq24 ||  '',
        parq25: stepData.step5.parq25 ||  '',
        parq26: stepData.step5.parq26 ||  '',
        parq27: stepData.step5.parq27 ||  '',
        parq28: stepData.step5.parq28 ||  '',
        parq29: stepData.step5.parq29 ||  '',
    });

    useEffect(() => {
        setLocalState({
            parq15: stepData.step5.parq15 ||  '',
            parq16: stepData.step5.parq16 ||  '',
            parq17: stepData.step5.parq17 ||  '',
            parq18: stepData.step5.parq18 ||  '',
            parq19: stepData.step5.parq19 ||  '',
            parq20: stepData.step5.parq20 ||  '',
            parq21: stepData.step5.parq21 ||  '',
            parq22: stepData.step5.parq22 ||  '',
            parq23: stepData.step5.parq23 ||  '',
            parq24: stepData.step5.parq24 ||  '',
            parq25: stepData.step5.parq25 ||  '',
            parq26: stepData.step5.parq26 ||  '',
            parq27: stepData.step5.parq27 ||  '',
            parq28: stepData.step5.parq28 ||  '',
            parq29: stepData.step5.parq29 ||  '',
        });
    }, [stepData.step5]);

    const handleInputChange = (field, value) => {
        // Change function to handleInputChange(text)
        //setLocalState(text);
        //setStepData((prevData) => ({ ...prevData, step1: text }));
        const updatedState = { ...localState, [field]: value };
        setLocalState(updatedState);
        setStepData((prevData) => ({ ...prevData, step5: updatedState }));
    };

    return (
        <View style={{padding:20, backgroundColor: 'white'}}>
            <View style={{padding:5}}>
                <Text>15. Hago que mi hijo/a sienta que le quiero y le necesito</Text>
                <SivariaRadioButton data={oneToFourOptions} option={stepData.step5.parq15} onSelect={text => handleInputChange('parq15', text)}/>
            </View>
            <View style={{padding:5}}>
                <Text>16. Presto muchísima atención a mi hijo/a</Text>
                <SivariaRadioButton data={oneToFourOptions} option={stepData.step5.parq16} onSelect={text => handleInputChange('parq16', text)}/>
            </View>
            <View style={{padding:5}}>
                <Text>17. Daño los sentimientos de mi hijo/a</Text>
                <SivariaRadioButton data={oneToFourOptions} option={stepData.step5.parq17} onSelect={text => handleInputChange('parq17', text)}/>
            </View>
            <View style={{padding:5}}>
                <Text>18. Olvido cosas importantes de mi hijo/a que debería recordar</Text>
                <SivariaRadioButton data={oneToFourOptions} option={stepData.step5.parq18} onSelect={text => handleInputChange('parq18', text)}/>
            </View>
            <View style={{padding:5}}>
                <Text>19. Cuando mi hijo/a se comporta mal le hago sentir que no le quiero</Text>
                <SivariaRadioButton data={oneToFourOptions} option={stepData.step5.parq19} onSelect={text => handleInputChange('parq19', text)}/>                
            </View>
            <View style={{padding:5}}>
                <Text>20. Dejo que mi hijo/a haga lo que quiera</Text>
                <SivariaRadioButton data={oneToFourOptions} option={stepData.step5.parq20} onSelect={text => handleInputChange('parq20', text)}/>                
            </View>
            <View style={{padding:5}}>
                <Text>21. Hago que mi hijo/a se sienta importante</Text>
                <SivariaRadioButton data={oneToFourOptions} option={stepData.step5.parq21} onSelect={text => handleInputChange('parq21', text)}/>                
            </View>
            <View style={{padding:5}}>
                <Text>22. Atemorizo o amenazo a mi hijo/a para hablar sobre ello</Text>
                <SivariaRadioButton data={oneToFourOptions} option={stepData.step5.parq22} onSelect={text => handleInputChange('parq22', text)}/>
            </View>
            <View style={{padding:5}}>
                <Text>23. Me preocupo sobre lo que piensa y le gusta a mi hijo/a para hablar sobre ello</Text>
                <SivariaRadioButton data={oneToFourOptions} option={stepData.step5.parq23} onSelect={text => handleInputChange('parq23', text)}/>
            </View>
            <View style={{padding:5}}>
                <Text>24. Siento que los demás niños/as son mejores que mi hijo/a</Text>
                <SivariaRadioButton data={oneToFourOptions} option={stepData.step5.parq24} onSelect={text => handleInputChange('parq24', text)}/>
            </View>
            <View style={{padding:5}}>
                <Text>25. Hago saber a mi hijo/a que no es querido</Text>
                <SivariaRadioButton data={oneToFourOptions} option={stepData.step5.parq25} onSelect={text => handleInputChange('parq25', text)}/>
            </View>
            <View style={{padding:5}}>
                <Text>26. Quiero controlar cualquier cosa que mi hijo/a haga</Text>
                <SivariaRadioButton data={oneToFourOptions} option={stepData.step5.parq26} onSelect={text => handleInputChange('parq26', text)}/>                
            </View>
            <View style={{padding:5}}>
                <Text>27. Hago saber a mi hijo/a cuando hace algo que me molesta</Text>
                <SivariaRadioButton data={oneToFourOptions} option={stepData.step5.parq27} onSelect={text => handleInputChange('parq27', text)}/>                
            </View>
            <View style={{padding:5}}>
                <Text>28. Sólo presto atención a mi hijo7a cuando hace algo que me molesta</Text>
                <SivariaRadioButton data={oneToFourOptions} option={stepData.step5.parq28} onSelect={text => handleInputChange('parq28', text)}/>                
            </View>
            <View style={{padding:5}}>
                <Text>29. Trato a mi hijo/a amablemente y con cariño</Text>
                <SivariaRadioButton data={oneToFourOptions} option={stepData.step5.parq29} onSelect={text => handleInputChange('parq29', text)}/>                
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

export { Step1, Step2, Step3, Step4, Step5 };