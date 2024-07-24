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

const Step1 = ({ stepData, setStepData }) => {
    //const [localState, setLocalState] = useState(stepData.step1 || '');
    const [localState, setLocalState] = useState({
        course: stepData.step1.course || '',
        age: stepData.step1.age || '',
        gender: stepData.step1.gender || '',
        trans: stepData.step1.trans || '',
    });

    useEffect(() => {
        setLocalState({
            course: stepData.step1.course || '',
            age: stepData.step1.age || '',
            gender: stepData.step1.gender || '',
            trans: stepData.step1.trans || '',
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
            {/*
            <View>
                <Text>Step 1</Text>
                <TextInput
                    style={styles.input}
                    value={localState}
                    onChangeText={handleInputChange}
                />
            </View>
            */}
            <View style={{padding: 20, backgroundColor: 'white'}}>
                <View style={{padding: 5}}>
                    <Text style={{fontWeight:'bold'}}>Curso:</Text>
                    {/*<Dropdown 
                        items={courses}
                        placeholder={{ label: 'Selecciona un curso...', value: 'ninguno' }}
                        value={stepData.step1.course}
                        onValueChange={text => handleInputChange( 'course', text )}
                    />*/}
                    <SivariaRadioButton 
                        data={courses} 
                        option={stepData.step1.course} 
                        onSelect={text => handleInputChange('course', text)}
                    />
                </View>
                <View style={{padding:5}}>
                    <Text style={{fontWeight:'bold'}}>Edad (en años):</Text>
                    <SivariaInput 
                        placeholder={'Edad'}
                        value={stepData.step1.age}
                        onChangeText={text => handleInputChange('age', text )}
                        autoCorrect={false}
                        autoCapitalize={'none'} 
                        inputMode={'numeric'}
                    />
                </View>
                <View style={{padding:5}}>
                    <Text style={{fontWeight:'bold'}}>Sexo:</Text>
                    <SivariaRadioButton 
                        data={genderData} 
                        option={stepData.step1.gender} 
                        onSelect={text => handleInputChange('gender', text)}
                    />
                </View>
                <View style={{padding:5}}>
                    <Text style={{fontWeight:'bold'}}>¿Te consideras una persona trans?:</Text>
                    <SivariaRadioButton 
                        data={transData} 
                        option={stepData.step1.trans} 
                        onSelect={text => handleInputChange('trans', text)}
                    />
                </View>
            </View>
        </>
    );
};

const Step2 = ({ stepData, setStepData }) => {
    const [localState, setLocalState] = useState({
        jobSituationFather: stepData.step2.jobSituationFather || '',
        jobSituationMother: stepData.step2.jobSituationMother || '',
        academicLevelFather: stepData.step2.academicLevelFather || '',
        academicLevelMother: stepData.step2.academicLevelMother || '',
        academicPerformance: stepData.step2.academicPerformance || '',
        previousPsychiatricTreatment: stepData.step2.previousPsychiatricTreatment || '',
        chronicDisease: stepData.step2.chronicDisease || '',
    });

    useEffect(() => {
        setLocalState({
            jobSituationFather: stepData.step2.jobSituationFather || '',
            jobSituationMother: stepData.step2.jobSituationMother || '',
            academicLevelFather: stepData.step2.academicLevelFather || '',
            academicLevelMother: stepData.step2.academicLevelMother || '',
            academicPerformance: stepData.step2.academicPerformance || '',
            previousPsychiatricTreatment: stepData.step2.previousPsychiatricTreatment || '',
            chronicDisease: stepData.step2.chronicDisease || '',
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
                <Text style={{fontWeight:'bold'}}>Indica la situación laboral actual de tu padre:</Text>
                <SivariaRadioButton option={stepData.step2.jobSituationFather} data={parentsJobSituationData} onSelect={text => handleInputChange('jobSituationFather', text)}/>
            </View>
            <View style={{padding:5}}>
                <Text style={{fontWeight:'bold'}}>Indica la situación laboral actual de tu madre:</Text>
                <SivariaRadioButton option={stepData.step2.jobSituationMother} data={parentsJobSituationData} onSelect={text => handleInputChange('jobSituationMother', text)}/>
            </View>
            <View style={{padding:5}}>
                <Text style={{fontWeight:'bold'}}>Indica los estudios de tu padre o figura parental 1:</Text>
                <SivariaRadioButton option={stepData.step2.academicLevelFather} data={parentsAcademicLevel} onSelect={text => handleInputChange('academicLevelFather', text)}/>
            </View>
            <View style={{padding:5}}>
                <Text style={{fontWeight:'bold'}}>Indica los estudios de tu madre o figura parental 2:</Text>
                <SivariaRadioButton option={stepData.step2.academicLevelMother} data={parentsAcademicLevel} onSelect={text => handleInputChange('academicLevelMother', text)}/>
            </View>
            <View style={{padding:5}}>
                <Text style={{fontWeight:'bold'}}>Señala cuál crees que es tu rendimiento académico en los dos últimos años:</Text>
                <SivariaRadioButton option={stepData.step2.academicPerformance} data={academicPerformanceData} onSelect={text => handleInputChange('academicPerformance', text)}/>
            </View>
            <View style={{padding:5}}>
                <Text style={{fontWeight:'bold'}}>
                    Señala si tienes en la actualidad o has tenido previamente tratamiento psiquiátrico y/o psicológico 
                    (por ejemplo, me han diagnosticado depresión o ansiedad):
                </Text>
                <SivariaRadioButton data={yesNoData} option={stepData.step2.previousPsychiatricTreatment} onSelect={text => handleInputChange('previousPsychiatricTreatment', text)}/>
            </View>
            <View style={{padding:5}}>
                <Text style={{fontWeight:'bold'}}>
                    Indica si padeces alguna enfermedad crónica desde hace por lo menos un año 
                    (por ejemplo: me han diagnosticado, diabetes, epilepsia...):
                </Text>
                <SivariaRadioButton data={yesNoData} option={stepData.step2.chronicDisease} onSelect={text => handleInputChange('chronicDisease', text)}/>
            </View>
        </View>
    );
};

const Step3 = ({ stepData, setStepData }) => {
    const [localState, setLocalState] = useState({
        femaleSelfPerception: stepData.step3.femaleSelfPerception || '',
        maleSelfPerception: stepData.step3.maleSelfPerception || '',
        femaleOthersPerception: stepData.step3.femaleOthersPerception || '',
        maleOthersPerception: stepData.step3.maleOthersPerception || '',
        weight: stepData.step3.weight || '',
        height: stepData.step3.height || '',
        discriminationType: stepData.step3.discriminationType || '',
    });

    useEffect(() => {
        setLocalState({
            femaleSelfPerception: stepData.step3.femaleSelfPerception || '',
            maleSelfPerception: stepData.step3.maleSelfPerception || '',
            femaleOthersPerception: stepData.step3.femaleOthersPerception || '',
            maleOthersPerception: stepData.step3.maleOthersPerception || '',
            weight: stepData.step3.weight || '',
            height: stepData.step3.height || '',
            discriminationType: stepData.step3.discriminationType || '',
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
                <Text style={{fontWeight:'bold'}}>En general, ¿cómo te ves a ti mismo/a? (responde a ambas escalas: masculino y femenina). Evalúe de 0 a 6,
                donde 0 significa Nada en absoluto y 6 completamente:</Text>
                <Text>Femenina</Text>
                <SivariaRadioButton data={selfPerceptionData} option={stepData.step3.femaleSelfPerception} onSelect={text => handleInputChange('femaleSelfPerception', text)}/>
                <Text>Masculino</Text>
                <SivariaRadioButton data={selfPerceptionData} option={stepData.step3.maleSelfPerception} onSelect={text => handleInputChange('maleSelfPerception', text)}/>
            </View>
            <View style={{padding:5}}>
                <Text style={{fontWeight:'bold'}}>En general, ¿cómo crees que te ve la mayoría de la gente? (responde a ambas escalas: masculino y femenina). Evalúe de 0 a 6,
                donde 0 significa Nada en absoluto y 6 completamente:</Text>
                <Text>Femenina</Text>
                <SivariaRadioButton data={selfPerceptionData} option={stepData.step3.femaleOthersPerception} onSelect={text => handleInputChange('femaleOthersPerception', text)}/>
                <Text>Masculino</Text>
                <SivariaRadioButton data={selfPerceptionData} option={stepData.step3.maleOthersPerception} onSelect={text => handleInputChange('maleOthersPerception', text)}/>
            </View>
            <View style={{padding:5}}>
                <Text style={{fontWeight:'bold'}}>Cuánto pesas? (poner valor aproximado en kg):</Text>
                <SivariaInput 
                    placeholder={'Peso'}
                    value={stepData.step3.weight}
                    onChangeText={text => handleInputChange('weight', text )}
                    autoCorrect={false}
                    autoCapitalize={'none'} 
                    inputMode={'numeric'}
                />                             
            </View>
            <View style={{padding:5}}>
                <Text style={{fontWeight:'bold'}}>Cuánto mides? (poner valor aproximado en cm):</Text>
                <SivariaInput 
                    placeholder={'Altura'}
                    value={stepData.step3.height}
                    onChangeText={text => handleInputChange('height', text )}
                    autoCorrect={false}
                    autoCapitalize={'none'} 
                    inputMode={'numeric'}
                />                        
            </View>
            <View style={{padding:5}}>
                <Text style={{fontWeight:'bold'}}>Indica el tipo de discriminación sufrido. Si no has sufrido ninguno, pon Ninguno:</Text>
                {/*<Dropdown 
                    items={discriminationTypes}
                    placeholder={{ label: 'Selecciona una opción...', value: 'ninguno' }}
                    value={stepData.step3.discriminationType}
                    onValueChange={text => handleInputChange('discriminationType', text )}
                /> */}
                <SivariaRadioButton data={discriminationTypes} option={stepData.step3.discriminationType} onSelect={text => handleInputChange('discriminationType', text)}/>
            </View>
        </View>
    );
};

const Step4 = ({ stepData, setStepData }) => {
    const [localState, setLocalState] = useState({
        vb1: stepData.step4.vb1 || '', 
        vb2: stepData.step4.vb2 || '',
        vb4: stepData.step4.vb4 || '',
        ab1: stepData.step4.ab1 || '',
        ab2: stepData.step4.ab2 || '',
        ab4: stepData.step4.ab4 || '',
        cybv1: stepData.step4.cybv1 || '',
        cybv2: stepData.step4.cybv2 || '',
        cybv3: stepData.step4.cybv3 || '',
        cybb1: stepData.step4.cybb1 || '',
        cybb2: stepData.step4.cybb2 || '',
        cybb3: stepData.step4.cybb3 || '',
    });

    useEffect(() => {
        setLocalState({
            vb1: stepData.step4.vb1 || '', 
            vb2: stepData.step4.vb2 || '',
            vb4: stepData.step4.vb4 || '',
            ab1: stepData.step4.ab1 || '',
            ab2: stepData.step4.ab2 || '',
            ab4: stepData.step4.ab4 || '',
            cybv1: stepData.step4.cybv1 || '',
            cybv2: stepData.step4.cybv2 || '',
            cybv3: stepData.step4.cybv3 || '',
            cybb1: stepData.step4.cybb1 || '',
            cybb2: stepData.step4.cybb2 || '',
            cybb3: stepData.step4.cybb3 || '',
        });
    }, [stepData.step4]);

    const handleInputChange = (field, value) => {
        // Change function to handleInputChange(text)
        //setLocalState(text);
        //setStepData((prevData) => ({ ...prevData, step1: text }));
        const updatedState = { ...localState, [field]: value };
        setLocalState(updatedState);
        setStepData((prevData) => ({ ...prevData, step4: updatedState }));
    };

    return (
        <View style={{padding:20, backgroundColor: 'white'}}>
            <Text style={{fontWeight:'bold'}}>
                EBIP-Q y del ECIP-Q
            </Text>
            <Text style={{fontWeight:'bold'}}>
                A continuación, le pediremos que identifique 
                con qué frecuencia ha tenido alguna de 
                estas experiencias en los últimos dos (2) meses, evalúe de 0 a 4,
                donde 0 significa nunca y 4 siempre.
            </Text>
            <View style={{padding:5}}>
                <Text>VB1. Alguien me ha golpeado, me ha pateado o me ha empujado</Text>
                <SivariaRadioButton data={zeroToFourOptions} option={stepData.step4.vb1} onSelect={text => handleInputChange('vb1', text)}/>
            </View>
            <View style={{padding:5}}>
                <Text>VB2. Alguien me ha insultado</Text>
                <SivariaRadioButton data={zeroToFourOptions} option={stepData.step4.vb2} onSelect={text => handleInputChange('vb2', text)}/>
            </View>
            <View style={{padding:5}}>
                <Text>VB4. Alguien me ha amenazado</Text>
                <SivariaRadioButton data={zeroToFourOptions} option={stepData.step4.vb4} onSelect={text => handleInputChange('vb4', text)}/>
            </View>
            <View style={{padding:5}}>
                <Text>AB1. He golpeado, pateado o empujado a alguien</Text>
                <SivariaRadioButton data={zeroToFourOptions} option={stepData.step4.ab1} onSelect={text => handleInputChange('ab1', text)}/>
            </View>
            <View style={{padding:5}}>
                <Text>AB2. He insultado he dicho palabras malsonantes a alguien porque quería hacerle daño</Text>
                <SivariaRadioButton data={zeroToFourOptions} option={stepData.step4.ab2} onSelect={text => handleInputChange('ab2', text)}/>                
            </View>
            <View style={{padding:5}}>
                <Text>AB4. He amenazado a alguien</Text>
                <SivariaRadioButton data={zeroToFourOptions} option={stepData.step4.ab4} onSelect={text => handleInputChange('ab4', text)}/>                
            </View>
            <View style={{padding:5}}>
                <Text>CybV1. Alguien me ha dicho palabras malsonantes o me ha insultado usando el email o SMS</Text>
                <SivariaRadioButton data={zeroToFourOptions} option={stepData.step4.cybv1} onSelect={text => handleInputChange('cybv1', text)}/>                
            </View>
            <View style={{padding:5}}>
                <Text>CybV2. Alguien le ha dicho a otros palabras malsonantes sobre mí usando Internet o SMS</Text>
                <SivariaRadioButton data={zeroToFourOptions} option={stepData.step4.cybv2} onSelect={text => handleInputChange('cybv2', text)}/>                
            </View>
            <View style={{padding:5}}>
                <Text>CybV3. Alguien me ha amenazado a través de mensajes en Interne o SMS</Text>
                <SivariaRadioButton data={zeroToFourOptions} option={stepData.step4.cybv3} onSelect={text => handleInputChange('cybv3', text)}/>                
            </View>
            <View style={{padding:5}}>
                <Text>CybB1. He dicho palabras malsonantes a alguien o le he insultado usando SMS o mensajes en Internet</Text>
                <SivariaRadioButton data={zeroToFourOptions} option={stepData.step4.cybb1} onSelect={text => handleInputChange('cybb1', text)}/>                
            </View>
            <View style={{padding:5}}>
                <Text>CybB2. He dicho palabras malsonantes sobre alguien a otras personas en mensajes por Internet o por SMS</Text>
                <SivariaRadioButton data={zeroToFourOptions} option={stepData.step4.cybb2} onSelect={text => handleInputChange('cybb2', text)}/>                
            </View>
            <View style={{padding:5}}>
                <Text>CybB3. He amenazado a alguien a través de SMS o mensajes en Internet</Text>
                <SivariaRadioButton data={zeroToFourOptions} option={stepData.step4.cybb3} onSelect={text => handleInputChange('cybb3', text)}/>                
            </View>
        </View>
    );
};
const Step5 = ({ stepData, setStepData }) => {
    const [localState, setLocalState] = useState({
        rrss1: stepData.step5.rrss1 || '', 
        rrss2: stepData.step5.rrss2 || '', 
        rrss3: stepData.step5.rrss3 || '', 
        rrss4: stepData.step5.rrss4 || '', 
        rrss5: stepData.step5.rrss5 || '', 
        rrss6: stepData.step5.rrss6 || '', 
        rrss7: stepData.step5.rrss7 || '', 
    });

    useEffect(() => {
        setLocalState({
            rrss1: stepData.step5.rrss1 || '', 
            rrss2: stepData.step5.rrss2 || '', 
            rrss3: stepData.step5.rrss3 || '', 
            rrss4: stepData.step5.rrss4 || '', 
            rrss5: stepData.step5.rrss5 || '', 
            rrss6: stepData.step5.rrss6 || '', 
            rrss7: stepData.step5.rrss7 || '', 
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
            <Text style={{fontWeight:'bold'}}>
                RRSS
            </Text>
            <Text style={{fontWeight:'bold'}}>
                A continuación, encontrarás un serie de preguntas relacionadas con las nuevas tecnologías. 
                Contesta de la forma más sincera posible.
            </Text>
            <View style={{padding:5}}>
                <Text>1. ¿Has visto imágenes o leído últimamente sobre autolesión o suicidio en algún medio audiovisual?</Text>
                <SivariaRadioButton data={yesNoData} option={stepData.step5.rrss1} onSelect={text => handleInputChange('rrss1', text)}/>
            </View>
            <View style={{padding:5}}>
                <Text>2. ¿Has buscado alguna vez información o te has metido en un foro sobre el suicidio y/o autolesión en Internet?</Text>
                <SivariaRadioButton data={yesNoData} option={stepData.step5.rrss2} onSelect={text => handleInputChange('rrss2', text)}/>
            </View>
            <View style={{padding:5}}>
                <Text>3. ¿Alguna vez has sentido la necesidad de hacerte daño y has compartido tu pensamiento a través de alguna red social o Internet?</Text>
                <SivariaRadioButton data={yesNoData} option={stepData.step5.rrss3} onSelect={text => handleInputChange('rrss3', text)}/>
            </View>
            <View style={{padding:5}}>
                <Text>4. ¿Alguna vez has sentido angustia, tristeza, desesperación, o te has sentido solo, lo has compartido o has buscado ayuda en Internet?</Text>
                <SivariaRadioButton data={yesNoData} option={stepData.step5.rrss4} onSelect={text => handleInputChange('rrss4', text)}/>
            </View>
            <View style={{padding:5}}>
                <Text>5. ¿Alguna vez has sentido la tentación de hacerte daño después de ver algún tipo de contenido en Internet?</Text>
                <SivariaRadioButton data={yesNoData} option={stepData.step5.rrss5} onSelect={text => handleInputChange('rrss5', text)}/>                
            </View>
            <View style={{padding:5}}>
                <Text>6. ¿Alguna vez has sentido la tentación de hacerte daño y has buscado ayuda en Internet?</Text>
                <SivariaRadioButton data={yesNoData} option={stepData.step5.rrss6} onSelect={text => handleInputChange('rrss6', text)}/>                
            </View>
            <View style={{padding:5}}>
                <Text>7. ¿Conoces a alguien que haya compartido alguna foto, pensamiento o comportamiento autolesivo en Internet?</Text>
                <SivariaRadioButton data={yesNoData} option={stepData.step5.rrss7} onSelect={text => handleInputChange('rrss7', text)}/>                
            </View>
        </View>
    );
};
const Step6 = ({ stepData, setStepData }) => {
    
    const [localState, setLocalState] = useState({
        mcad1: stepData.step6.mcad1 || '', 
        mcad2: stepData.step6.mcad2 || '',
        mcad3: stepData.step6.mcad3 || '',
        mcad4: stepData.step6.mcad4 || '',
        mcad5: stepData.step6.mcad5 || '',
        mcad6: stepData.step6.mcad6 || '',
        mcad7: stepData.step6.mcad7 || '',
        mcad8: stepData.step6.mcad8 || '',
        mcad9: stepData.step6.mcad9 || '',
        mcad10: stepData.step6.mcad10 || '',
        mcad11: stepData.step6.mcad11 || '',
        mcad12: stepData.step6.mcad12 || '',
    });

    useEffect(() => {
        setLocalState({
            mcad1: stepData.step6.mcad1 || '', 
            mcad2: stepData.step6.mcad2 || '',
            mcad3: stepData.step6.mcad3 || '',
            mcad4: stepData.step6.mcad4 || '',
            mcad5: stepData.step6.mcad5 || '',
            mcad6: stepData.step6.mcad6 || '',
            mcad7: stepData.step6.mcad7 || '',
            mcad8: stepData.step6.mcad8 || '',
            mcad9: stepData.step6.mcad9 || '',
            mcad10: stepData.step6.mcad10 || '',
            mcad11: stepData.step6.mcad11 || '',
            mcad12: stepData.step6.mcad12 || '',
        });
    }, [stepData.step6]);

    const handleInputChange = (field, value) => {
        // Change function to handleInputChange(text)
        //setLocalState(text);
        //setStepData((prevData) => ({ ...prevData, step1: text }));
        const updatedState = { ...localState, [field]: value };
        setLocalState(updatedState);
        setStepData((prevData) => ({ ...prevData, step6: updatedState }));
    };

    return (
        <View style={{padding:20, backgroundColor: 'white'}}>
            <Text style={{fontWeight:'bold'}}>
                MULTICAGE CAD-4
            </Text>
            <Text style={{fontWeight:'bold'}}>
                Por favor, responde Sí/No a las siguientes preguntas
            </Text>
            <View style={{padding:5}}>
                <Text>1. ¿Has pensado alguna vez que deberías beber menos alcohol?</Text>
                <SivariaRadioButton data={yesNoData} option={stepData.step6.mcad1} onSelect={text => handleInputChange('mcad1', text)}/>
            </View>
            <View style={{padding:5}}>
                <Text>2. ¿Te has sentido molesto/a cuando alguna persona te ha criticado tu manera o forma de beber alcohol?</Text>
                <SivariaRadioButton data={yesNoData} option={stepData.step6.mcad2} onSelect={text => handleInputChange('mcad2', text)}/>
            </View>
            <View style={{padding:5}}>
                <Text>3. ¿Te has sentido culpable alguna vez por tu manera o forma de beber alcohol?</Text>
                <SivariaRadioButton data={yesNoData} option={stepData.step6.mcad3} onSelect={text => handleInputChange('mcad3', text)}/>
            </View>
            <View style={{padding:5}}>
                <Text>4. ¿Alguna vez lo primero que has hecho por la mañana es beber alguna bebida alcohólica para relajarte o para eliminar la resaca?</Text>
                <SivariaRadioButton data={yesNoData} option={stepData.step6.mcad4} onSelect={text => handleInputChange('mcad4', text)}/>
            </View>
            <View style={{padding:5}}>
                <Text>5. ¿Has pensado alguna vez que deberías consumir menos drogas?</Text>
                <SivariaRadioButton data={yesNoData} option={stepData.step6.mcad5} onSelect={text => handleInputChange('mcad5', text)}/>
            </View>
            <View style={{padding:5}}>
                <Text>6. ¿Niegas el consumo de drogas a familiares, amigos o compañeros para evitar que te critiquen?</Text>
                <SivariaRadioButton data={yesNoData} option={stepData.step6.mcad6} onSelect={text => handleInputChange('mcad6', text)}/>
            </View>
            <View style={{padding:5}}>
                <Text>7. ¿Has tenido problemas psicológicos, económicos, laborales o familiares a causa del consumo de drogas?</Text>
                <SivariaRadioButton data={yesNoData} option={stepData.step6.mcad7} onSelect={text => handleInputChange('mcad7', text)}/>
            </View>
            <View style={{padding:5}}>
                <Text>8. ¿Te sientes a veces impulsado a consumir drogas aunque hayas decidido no hacerlo?</Text>
                <SivariaRadioButton data={yesNoData} option={stepData.step6.mcad8} onSelect={text => handleInputChange('mcad8', text)}/>
            </View>
            <View style={{padding:5}}>
                <Text>9. ¿Dedicas más tiempo del que crees que deberías a estar conectado a Internet con objetivos distintos a los de tu trabajo?</Text>
                <SivariaRadioButton data={yesNoData} option={stepData.step6.mcad9} onSelect={text => handleInputChange('mcad9', text)}/>
            </View>
            <View style={{padding:5}}>
                <Text>10. ¿Se han quejado tus familiares de las horas que dedicas a Internet?</Text>
                <SivariaRadioButton data={yesNoData} option={stepData.step6.mcad10} onSelect={text => handleInputChange('mcad10', text)}/>
            </View>
            <View style={{padding:5}}>
                <Text>11. ¿Te resulta duro permanecer alejado/a de Internet varios días seguidos?</Text>
                <SivariaRadioButton data={yesNoData} option={stepData.step6.mcad11} onSelect={text => handleInputChange('mcad11', text)}/>
            </View>
            <View style={{padding:5}}>
                <Text>12. ¿Tienes problemas para controlar el impulso de conectarte a Internet o has intentado sin éxito reducir el tiempo que dedicas a estar conectado/a?</Text>
                <SivariaRadioButton data={yesNoData} option={stepData.step6.mcad12} onSelect={text => handleInputChange('mcad12', text)}/>
            </View>
        </View>
    );
};
const Step7 = ({ stepData, setStepData }) => {
    const [localState, setLocalState] = useState({
        cerqs1: stepData.step7.cerqs1 || '', 
        cerqs2: stepData.step7.cerqs2 || '',
        cerqs3: stepData.step7.cerqs3 || '',
        cerqs4: stepData.step7.cerqs4 || '',
        cerqs5: stepData.step7.cerqs5 || '',
        cerqs6: stepData.step7.cerqs6 || '',
        cerqs7: stepData.step7.cerqs7 || '',
        cerqs8: stepData.step7.cerqs8 || '',
        cerqs9: stepData.step7.cerqs9 || '',
        cerqs10: stepData.step7.cerqs10 || '',
        cerqs11: stepData.step7.cerqs11 || '',
        cerqs12: stepData.step7.cerqs12 || '',
        cerqs13: stepData.step7.cerqs13 || '',
        cerqs14: stepData.step7.cerqs14 || '',
        cerqs15: stepData.step7.cerqs15 || '',
        cerqs16: stepData.step7.cerqs16 || '',
        cerqs17: stepData.step7.cerqs17 || '',
        cerqs18: stepData.step7.cerqs18 || '',
    });

    useEffect(() => {
        setLocalState({
            cerqs1: stepData.step7.cerqs1 || '', 
            cerqs2: stepData.step7.cerqs2 || '',
            cerqs3: stepData.step7.cerqs3 || '',
            cerqs4: stepData.step7.cerqs4 || '',
            cerqs5: stepData.step7.cerqs5 || '',
            cerqs6: stepData.step7.cerqs6 || '',
            cerqs7: stepData.step7.cerqs7 || '',
            cerqs8: stepData.step7.cerqs8 || '',
            cerqs9: stepData.step7.cerqs9 || '',
            cerqs10: stepData.step7.cerqs10 || '',
            cerqs11: stepData.step7.cerqs11 || '',
            cerqs12: stepData.step7.cerqs12 || '',
            cerqs13: stepData.step7.cerqs13 || '',
            cerqs14: stepData.step7.cerqs14 || '',
            cerqs15: stepData.step7.cerqs15 || '',
            cerqs16: stepData.step7.cerqs16 || '',
            cerqs17: stepData.step7.cerqs17 || '',
            cerqs18: stepData.step7.cerqs18 || '',
        });
    }, [stepData.step7]);

    const handleInputChange = (field, value) => {
        // Change function to handleInputChange(text)
        //setLocalState(text);
        //setStepData((prevData) => ({ ...prevData, step1: text }));
        const updatedState = { ...localState, [field]: value };
        setLocalState(updatedState);
        setStepData((prevData) => ({ ...prevData, step7: updatedState }));
    };

    return (
        <View style={{padding:20, backgroundColor: 'white'}}>
            <Text style={{fontWeight:'bold'}}>
                CERQ-S
            </Text>
            <Text style={{fontWeight:'bold'}}>
                Todos nos enfrentamos en algún momento con acontacimiento que resultan negativos o desagradables,
                y cada uno de nosotros responde ante ellos de una forma personal. 
                En las siguientes frases te pedimos que indiques lo que piensas habitualmente cuando
                te enfrentas a una experiencia negativa o desagradable. 
                Por favor, señala la opción que más se aproxime a tus pensamientos habituales en esos momentos.
                Evalúe de 1 a 5, donde 1 significa casi nunca y 5 casi siempre.
            </Text>
            <View style={{padding:5}}>
                <Text>1. Siento que soy el único culpable de lo que ha pasado</Text>
                <SivariaRadioButton data={oneToFiveOptions} option={stepData.step7.cerqs1} onSelect={text => handleInputChange('cerqs1', text)}/>
            </View>
            <View style={{padding:5}}>
                <Text>2. Creo que tengo que acpear lo que ha pasado</Text>
                <SivariaRadioButton data={oneToFiveOptions} option={stepData.step7.cerqs2} onSelect={text => handleInputChange('cerqs2', text)}/>
            </View>
            <View style={{padding:5}}>
                <Text>3. Pienso a menudo en cómo me siento en relación con lo que me ha pasado</Text>
                <SivariaRadioButton data={oneToFiveOptions} option={stepData.step7.cerqs3} onSelect={text => handleInputChange('cerqs3', text)}/>
            </View>
            <View style={{padding:5}}>
                <Text>4. Me parece que otros son culpables de lo ocurrido</Text>
                <SivariaRadioButton data={oneToFiveOptions} option={stepData.step7.cerqs4} onSelect={text => handleInputChange('cerqs4', text)}/>
            </View>
            <View style={{padding:5}}>
                <Text>5. Me siento único/a responsable de lo ocurrido</Text>
                <SivariaRadioButton data={oneToFiveOptions} option={stepData.step7.cerqs5} onSelect={text => handleInputChange('cerqs5', text)}/>                
            </View>
            <View style={{padding:5}}>
                <Text>6. Creo que tengo que aceptar la situación</Text>
                <SivariaRadioButton data={oneToFiveOptions} option={stepData.step7.cerqs6} onSelect={text => handleInputChange('cerqs6', text)}/>                
            </View>
            <View style={{padding:5}}>
                <Text>7. Me preocupa lo que piense y sienta sobre lo que me ha pasado</Text>
                <SivariaRadioButton data={oneToFiveOptions} option={stepData.step7.cerqs7} onSelect={text => handleInputChange('cerqs7', text)}/>                
            </View>
            <View style={{padding:5}}>
                <Text>8. Pienso en cosas agradables que nada tienen que ver con lo que me ha pasado</Text>
                <SivariaRadioButton data={oneToFiveOptions} option={stepData.step7.cerqs8} onSelect={text => handleInputChange('cerqs8', text)}/>                
            </View>
            <View style={{padding:5}}>
                <Text>9. Pienso en cuál sería la mejor forma de enfrentarme a la situación</Text>
                <SivariaRadioButton data={oneToFiveOptions} option={stepData.step7.cerqs9} onSelect={text => handleInputChange('cerqs9', text)}/>                
            </View>
            <View style={{padding:5}}>
                <Text>10. Sigo pensando en lo terrible que ha sido lo que me ha pasado</Text>
                <SivariaRadioButton data={oneToFiveOptions} option={stepData.step7.cerqs10} onSelect={text => handleInputChange('cerqs10', text)}/>                
            </View>
            <View style={{padding:5}}>
                <Text>11. Me parece que otros son responsables de lo que ha ocurrido</Text>
                <SivariaRadioButton data={oneToFiveOptions} option={stepData.step7.cerqs11} onSelect={text => handleInputChange('cerqs11', text)}/>                
            </View>
            <View style={{padding:5}}>
                <Text>12. Pienso en algo agradable en vez de pensar en lo ocurrido</Text>
                <SivariaRadioButton data={oneToFiveOptions} option={stepData.step7.cerqs12} onSelect={text => handleInputChange('cerqs12', text)}/>                
            </View>
            <View style={{padding:5}}>
                <Text>13. Creo que la situación tiene también su lado positivo</Text>
                <SivariaRadioButton data={oneToFiveOptions} option={stepData.step7.cerqs13} onSelect={text => handleInputChange('cerqs13', text)}/>                
            </View>
            <View style={{padding:5}}>
                <Text>14. Creo que no ha sido tan malo en comparación a otras cosas</Text>
                <SivariaRadioButton data={oneToFiveOptions} option={stepData.step7.cerqs14} onSelect={text => handleInputChange('cerqs14', text)}/>                
            </View>
            <View style={{padding:5}}>
                <Text>15. Pienso en un plan acerca de lo mejor que podría hacer</Text>
                <SivariaRadioButton data={oneToFiveOptions} option={stepData.step7.cerqs15} onSelect={text => handleInputChange('cerqs15', text)}/>                
            </View>
            <View style={{padding:5}}>
                <Text>16. Busco los aspectos positivos de la cuestión</Text>
                <SivariaRadioButton data={oneToFiveOptions} option={stepData.step7.cerqs16} onSelect={text => handleInputChange('cerqs16', text)}/>                
            </View>
            <View style={{padding:5}}>
                <Text>17. Me digo que hay cosas peores en la vida</Text>
                <SivariaRadioButton data={oneToFiveOptions} option={stepData.step7.cerqs17} onSelect={text => handleInputChange('cerqs17', text)}/>                
            </View>
            <View style={{padding:5}}>
                <Text>18. Pienso continuamente en lo horrible que ha sido la situación</Text>
                <SivariaRadioButton data={oneToFiveOptions} option={stepData.step7.cerqs18} onSelect={text => handleInputChange('cerqs18', text)}/>                
            </View>
        </View>
    );
};
const Step8 = ({ stepData, setStepData }) => {
    const [localState, setLocalState] = useState({
        ati1: stepData.step8.ati1 || '',
        ati2: stepData.step8.ati2 || '',
        ati3: stepData.step8.ati3 || '',
        ati4: stepData.step8.ati4 || '',
        ati5: stepData.step8.ati5 || '',
        ati6: stepData.step8.ati6 || '',
        ate1: stepData.step8.ate1 || '',
        ate2: stepData.step8.ate2 || '',
        ate3: stepData.step8.ate3 || '',
        ate4: stepData.step8.ate4 || '',
        ate5: stepData.step8.ate5 || '',
        ate6: stepData.step8.ate6 || '',
        ate7: stepData.step8.ate7 || '',
        ate8: stepData.step8.ate8 || '',
        ate9: stepData.step8.ate9 || '',
        ate10: stepData.step8.ate10 || '',
    });

    useEffect(() => {
        setLocalState({
            ati1: stepData.step8.ati1 || '',
            ati2: stepData.step8.ati2 || '',
            ati3: stepData.step8.ati3 || '',
            ati4: stepData.step8.ati4 || '',
            ati5: stepData.step8.ati5 || '',
            ati6: stepData.step8.ati6 || '',
            ate1: stepData.step8.ate1 || '',
            ate2: stepData.step8.ate2 || '',
            ate3: stepData.step8.ate3 || '',
            ate4: stepData.step8.ate4 || '',
            ate5: stepData.step8.ate5 || '',
            ate6: stepData.step8.ate6 || '',
            ate7: stepData.step8.ate7 || '',
            ate8: stepData.step8.ate8 || '',
            ate9: stepData.step8.ate9 || '',
            ate10: stepData.step8.ate10 || '',
        });
    }, [stepData.step8]);

    const handleInputChange = (field, value) => {
        const updatedState = { ...localState, [field]: value };
        setLocalState(updatedState);
        setStepData((prevData) => ({ ...prevData, step8: updatedState }));
    };

    return (
        <View style={{padding:20, backgroundColor: 'white'}}>
            <Text style={{fontWeight: 'bold'}}>
                Escalas ATD
            </Text>
            <Text style={{fontWeight: 'bold'}}>
                A continuación, te pedimos que indiques en una escala del 0 al 4 en qué medida
                las frases siguientes se corresponden con tus pensamientos y sentimientos.
                Señala la opción de respuesta según la siguiente escala:
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
                <Text>1. Quiero escapar de mí mismo/a</Text>
                <SivariaRadioButton data={zeroToFourOptions} option={stepData.step8.ati1} onSelect={text => handleInputChange('ati1', text)}/>
            </View>
            <View style={{padding:5}}>
                <Text>2. Me siento impotente para cambiarme a mí mismo/a</Text>
                <SivariaRadioButton data={zeroToFourOptions} option={stepData.step8.ati2} onSelect={text => handleInputChange('ati2', text)}/>
            </View>
            <View style={{padding:5}}>
                <Text>3. Me gustaría escapar de mis pensamientos y sentimientos</Text>
                <SivariaRadioButton data={zeroToFourOptions} option={stepData.step8.ati3} onSelect={text => handleInputChange('ati3', text)}/>
            </View>
            <View style={{padding:5}}>
                <Text>4. Me siento atrapado dentro de mí mismo/a</Text>
                <SivariaRadioButton data={zeroToFourOptions} option={stepData.step8.ati4} onSelect={text => handleInputChange('ati4', text)}/>
            </View>
            <View style={{padding:5}}>
                <Text>5. Me gustaría huir de lo que soy y empezar de nuevo</Text>
                <SivariaRadioButton data={zeroToFourOptions} option={stepData.step8.ati5} onSelect={text => handleInputChange('ati5', text)}/>
            </View>
            <View style={{padding:5}}>
                <Text>6. Siento que estoy en un pozo del que no puedo salir</Text>
                <SivariaRadioButton data={zeroToFourOptions} option={stepData.step8.ati6} onSelect={text => handleInputChange('ati6', text)}/>
            </View>
            <Text style={{fontWeight:'bold'}}>
                ATE
            </Text>
            <View style={{padding:5}}>
                <Text>1. Estoy en una situación en la que me siento atrapado/a</Text>
                <SivariaRadioButton data={zeroToFourOptions} option={stepData.step8.ate1} onSelect={text => handleInputChange('ate1', text)}/>
            </View>
            <View style={{padding:5}}>
                <Text>2. Deseo con todas mis fuerzas escapar de mi vida</Text>
                <SivariaRadioButton data={zeroToFourOptions} option={stepData.step8.ate2} onSelect={text => handleInputChange('ate2', text)}/>
            </View>
            <View style={{padding:5}}>
                <Text>3. Estoy en una relación de la que no puedo salir/ Mantengo un tipo de relaciones en mi vida de las que no puedo salir</Text>
                <SivariaRadioButton data={zeroToFourOptions} option={stepData.step8.ate3} onSelect={text => handleInputChange('ate3', text)}/>
            </View>
            <View style={{padding:5}}>
                <Text>4. A menudo tengo la sensación de que me gustaría huir</Text>
                <SivariaRadioButton data={zeroToFourOptions} option={stepData.step8.ate4} onSelect={text => handleInputChange('ate4', text)}/>
            </View>
            <View style={{padding:5}}>
                <Text>5. Me siento importante para cambiar las cosas</Text>
                <SivariaRadioButton data={zeroToFourOptions} option={stepData.step8.ate5} onSelect={text => handleInputChange('ate5', text)}/>
            </View>
            <View style={{padding:5}}>
                <Text>6. Me siento atrapado por mis obligaciones</Text>
                <SivariaRadioButton data={zeroToFourOptions} option={stepData.step8.ate6} onSelect={text => handleInputChange('ate6', text)}/>
            </View>
            <View style={{padding:5}}>
                <Text>7. No veo forma de salir de mi situación actual</Text>
                <SivariaRadioButton data={zeroToFourOptions} option={stepData.step8.ate7} onSelect={text => handleInputChange('ate7', text)}/>
            </View>
            <View style={{padding:5}}>
                <Text>8. Me gustaría alejarme de las personas más importantes de mi vida</Text>
                <SivariaRadioButton data={zeroToFourOptions} option={stepData.step8.ate8} onSelect={text => handleInputChange('ate8', text)}/>
            </View>
            <View style={{padding:5}}>
                <Text>9. Tengo un fuerte deseo de alejarme y mantenerme alejado de donde estoy</Text>
                <SivariaRadioButton data={zeroToFourOptions} option={stepData.step8.ate9} onSelect={text => handleInputChange('ate9', text)}/>
            </View>
            <View style={{padding:5}}>
                <Text>10. Me siento atrapado por otras personas</Text>
                <SivariaRadioButton data={zeroToFourOptions} option={stepData.step8.ate10} onSelect={text => handleInputChange('ate10', text)}/>
            </View>
        </View>
    );
};

const Step9 = ({ stepData, setStepData }) => {
    const [localState, setLocalState] = useState({
        ed1: stepData.step9.ed1 || '',
        ed2: stepData.step9.ed2 || '',
        ed3: stepData.step9.ed3 || '',
        ed4: stepData.step9.ed4 || '',
        ed5: stepData.step9.ed5 || '',
        ed6: stepData.step9.ed6 || '',
        ed7: stepData.step9.ed7 || '',
        ed8: stepData.step9.ed8 || '',
        ed9: stepData.step9.ed9 || '',
        ed10: stepData.step9.ed10 || '',
        ed11: stepData.step9.ed11 || '',
        ed12: stepData.step9.ed12 || '',
        ed13: stepData.step9.ed13 || '',
        ed14: stepData.step9.ed14 || '',
        ed15: stepData.step9.ed15 || '',
        ed16: stepData.step9.ed16 || '',
        er1: stepData.step9.er1 || '',
        er2: stepData.step9.er2 || '',
        er3: stepData.step9.er3 || '',
        er4: stepData.step9.er4 || '',
        er5: stepData.step9.er5 || '',
        er6: stepData.step9.er6 || '',
        er7: stepData.step9.er7 || '',
        er8: stepData.step9.er8 || '',
        er9: stepData.step9.er9 || '',
        er10: stepData.step9.er10 || '',
    });

    useEffect(() => {
        setLocalState({
            ed1: stepData.step9.ed1 || '',
            ed2: stepData.step9.ed2 || '',
            ed3: stepData.step9.ed3 || '',
            ed4: stepData.step9.ed4 || '',
            ed5: stepData.step9.ed5 || '',
            ed6: stepData.step9.ed6 || '',
            ed7: stepData.step9.ed7 || '',
            ed8: stepData.step9.ed8 || '',
            ed9: stepData.step9.ed9 || '',
            ed10: stepData.step9.ed10 || '',
            ed11: stepData.step9.ed11 || '',
            ed12: stepData.step9.ed12 || '',
            ed13: stepData.step9.ed13 || '',
            ed14: stepData.step9.ed14 || '',
            ed15: stepData.step9.ed15 || '',
            ed16: stepData.step9.ed16 || '',
            er1: stepData.step9.er1 || '',
            er2: stepData.step9.er2 || '',
            er3: stepData.step9.er3 || '',
            er4: stepData.step9.er4 || '',
            er5: stepData.step9.er5 || '',
            er6: stepData.step9.er6 || '',
            er7: stepData.step9.er7 || '',
            er8: stepData.step9.er8 || '',
            er9: stepData.step9.er9 || '',
            er10: stepData.step9.er10 || '',
        });
    }, [stepData.step9]);

    const handleInputChange = (field, value) => {
        const updatedState = { ...localState, [field]: value };
        setLocalState(updatedState);
        setStepData((prevData) => ({ ...prevData, step9: updatedState }));
    };

    
    return (
        <View style={{padding:20, backgroundColor: 'white'}}>
            <Text style={{fontWeight: 'bold'}}>
                ED
            </Text>
            <Text style={{fontWeight: 'bold'}}>
                A continuación, te pedimos que que respondas a cada una de las afirmaciones
                siguientes señalando la opción de respuestas que mejor se acerque a cómo te has sentido
                en los últimos siete días. Para ello señala la opción de respuesta según la siguiente escala:
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
                <Text>1. Siento que he fracasado en la vida:</Text>
                <SivariaRadioButton data={zeroToFourOptions} option={stepData.step9.ed1} onSelect={text => handleInputChange('ed1', text)}/>
            </View>
            <View style={{padding:5}}>
                <Text>2. Siento que soy una persona exitosa:</Text>
                <SivariaRadioButton data={zeroToFourOptions} option={stepData.step9.ed2} onSelect={text => handleInputChange('ed2', text)}/>
            </View>
            <View style={{padding:5}}>
                <Text>3. Me siento derrotado por la vida:</Text>
                <SivariaRadioButton data={zeroToFourOptions} option={stepData.step9.ed3} onSelect={text => handleInputChange('ed3', text)}/>
            </View>
            <View style={{padding:5}}>
                <Text>4. Siento que básicamente soy un/a ganador/a:</Text>
                <SivariaRadioButton data={zeroToFourOptions} option={stepData.step9.ed4} onSelect={text => handleInputChange('ed4', text)}/>
            </View>
            <View style={{padding:5}}>
                <Text>5. Siento que he perdido mi lugar en el mundo:</Text>
                <SivariaRadioButton data={zeroToFourOptions} option={stepData.step9.ed5} onSelect={text => handleInputChange('ed5', text)}/>
            </View>
            <View style={{padding:5}}>
                <Text>6. Siento que la vida me ha tratado como un saco de boxeo:</Text>
                <SivariaRadioButton data={zeroToFourOptions} option={stepData.step9.ed6} onSelect={text => handleInputChange('ed6', text)}/>
            </View>
            <View style={{padding:5}}>
                <Text>7. Me siento impotente:</Text>
                <SivariaRadioButton data={zeroToFourOptions} option={stepData.step9.ed7} onSelect={text => handleInputChange('ed7', text)}/>
            </View>
            <View style={{padding:5}}>
                <Text>8. Siento que me han arrebatado la confianza en mí mismo/a:</Text>
                <SivariaRadioButton data={zeroToFourOptions} option={stepData.step9.ed8} onSelect={text => handleInputChange('ed8', text)}/>
            </View>
            <View style={{padding:5}}>
                <Text>9. Me siento capaz de afrontar lo que la vida me depare:</Text>
                <SivariaRadioButton data={zeroToFourOptions} option={stepData.step9.ed9} onSelect={text => handleInputChange('ed9', text)}/>
            </View>
            <View style={{padding:5}}>
                <Text>10. Siento que he tocado fondo:</Text>
                <SivariaRadioButton data={zeroToFourOptions} option={stepData.step9.ed10} onSelect={text => handleInputChange('ed10', text)}/>
            </View>
            <View style={{padding:5}}>
                <Text>11. Me siento completamente anulado/a:</Text>
                <SivariaRadioButton data={zeroToFourOptions} option={stepData.step9.ed11} onSelect={text => handleInputChange('ed11', text)}/>
            </View>
            <View style={{padding:5}}>
                <Text>12. Siento que soy un/a perdedor/a en la vida:</Text>
                <SivariaRadioButton data={zeroToFourOptions} option={stepData.step9.ed12} onSelect={text => handleInputChange('ed12', text)}/>
            </View>
            <View style={{padding:5}}>
                <Text>13. Siento que me he rendido:</Text>
                <SivariaRadioButton data={zeroToFourOptions} option={stepData.step9.ed13} onSelect={text => handleInputChange('ed13', text)}/>
            </View>
            <View style={{padding:5}}>
                <Text>14. Me siento acabado/a:</Text>
                <SivariaRadioButton data={zeroToFourOptions} option={stepData.step9.ed14} onSelect={text => handleInputChange('ed14', text)}/>
            </View>
            <View style={{padding:5}}>
                <Text>15. Siento que he perdido batallas importantes en la vida:</Text>
                <SivariaRadioButton data={zeroToFourOptions} option={stepData.step9.ed15} onSelect={text => handleInputChange('ed15', text)}/>
            </View>
            <View style={{padding:5}}>
                <Text>16. Siento que no hay nada por lo que luchar en la vida:</Text>
                <SivariaRadioButton data={zeroToFourOptions} option={stepData.step9.ed16} onSelect={text => handleInputChange('ed16', text)}/>
            </View>
            <Text style={{fontWeight: 'bold'}}>
                ER
            </Text>
            <Text style={{fontWeight: 'bold'}}>
                Por favor. lea cada frase e indica en qué medida está de acuerdo con cada una de ellas
                antes de la intervención psicológica y en el momento actual según la siguiente escala: 
                0 = Totalmente en desacuerdo y 4 = Totalmente de acuerdo
            </Text>
            <View style={{padding:5}}>
                <Text>1. Sé adaptarme a los cambios</Text>
                <SivariaRadioButton data={zeroToFourOptions} option={stepData.step9.er1} onSelect={text => handleInputChange('er1', text)}/>
            </View>
            <View style={{padding:5}}>
                <Text>2. Puedo manejar cualquier situación</Text>
                <SivariaRadioButton data={zeroToFourOptions} option={stepData.step9.er2} onSelect={text => handleInputChange('er2', text)}/>
            </View>
            <View style={{padding:5}}>
                <Text>3. Veo el lado positivo de las cosas</Text>
                <SivariaRadioButton data={zeroToFourOptions} option={stepData.step9.er3} onSelect={text => handleInputChange('er3', text)}/>
            </View>
            <View style={{padding:5}}>
                <Text>4. Me puedo manejar bien a pesar de la presión o el estrés</Text>
                <SivariaRadioButton data={zeroToFourOptions} option={stepData.step9.er4} onSelect={text => handleInputChange('er4', text)}/>
            </View>
            <View style={{padding:5}}>
                <Text>5. Después de un grave contratiempo</Text>
                <SivariaRadioButton data={zeroToFourOptions} option={stepData.step9.er5} onSelect={text => handleInputChange('er5', text)}/>
            </View>
            <View style={{padding:5}}>
                <Text>6. Consigo alcanzar mis metas a pesar de las dificultades</Text>
                <SivariaRadioButton data={zeroToFourOptions} option={stepData.step9.er6} onSelect={text => handleInputChange('er6', text)}/>
            </View>
            <View style={{padding:5}}>
                <Text>7. Puedo mantener la concentración bajo presión</Text>
                <SivariaRadioButton data={zeroToFourOptions} option={stepData.step9.er7} onSelect={text => handleInputChange('er7', text)}/>
            </View>
            <View style={{padding:5}}>
                <Text>8. Dificílmente me desanimo por los fracasos</Text>
                <SivariaRadioButton data={zeroToFourOptions} option={stepData.step9.er8} onSelect={text => handleInputChange('er8', text)}/>
            </View>
            <View style={{padding:5}}>
                <Text>9. Me defino como una persona fuerte</Text>
                <SivariaRadioButton data={zeroToFourOptions} option={stepData.step9.er9} onSelect={text => handleInputChange('er9', text)}/>
            </View>
            <View style={{padding:5}}>
                <Text>10. Puedo manejar los sentimientos desagradables</Text>
                <SivariaRadioButton data={zeroToFourOptions} option={stepData.step9.er10} onSelect={text => handleInputChange('er10', text)}/>
            </View>
        </View>
    );
};

const Step10 = ({ stepData, setStepData }) => {
    const [localState, setLocalState] = useState({
        inq1: stepData.step10.inq1 || '',
        inq2: stepData.step10.inq2 || '',
        inq3: stepData.step10.inq3 || '',
        inq4: stepData.step10.inq4 || '',
        inq5: stepData.step10.inq5 || '',
        inq6: stepData.step10.inq6 || '',
        inq7: stepData.step10.inq7 || '',
        inq8: stepData.step10.inq8 || '',
        inq9: stepData.step10.inq9 || '',
        inq10: stepData.step10.inq10 || '',
        inq11: stepData.step10.inq11 || '',
        inq12: stepData.step10.inq12 || '',
        inq13: stepData.step10.inq13 || '',
        inq14: stepData.step10.inq14 || '',
        inq15: stepData.step10.inq15 || '',
    });

    useEffect(() => {
        setLocalState({
            inq1: stepData.step10.inq1 || '',
            inq2: stepData.step10.inq2 || '',
            inq3: stepData.step10.inq3 || '',
            inq4: stepData.step10.inq4 || '',
            inq5: stepData.step10.inq5 || '',
            inq6: stepData.step10.inq6 || '',
            inq7: stepData.step10.inq7 || '',
            inq8: stepData.step10.inq8 || '',
            inq9: stepData.step10.inq9 || '',
            inq10: stepData.step10.inq10 || '',
            inq11: stepData.step10.inq11 || '',
            inq12: stepData.step10.inq12 || '',
            inq13: stepData.step10.inq13 || '',
            inq14: stepData.step10.inq14 || '',
            inq15: stepData.step10.inq15 || '',
        });
    }, [stepData.step10]);

    const handleInputChange = (field, value) => {
        const updatedState = { ...localState, [field]: value };
        setLocalState(updatedState);
        setStepData((prevData) => ({ ...prevData, step10: updatedState }));
    };

    
    return (
        <View style={{padding:20, backgroundColor: 'white'}}>
            <Text style={{fontWeight: 'bold'}}>
                INQ
            </Text>
            <Text style={{fontWeight: 'bold'}}>
                Por favor responde a cada una de las siguientes preguntas de acuerdo con lo que tú
                crees en este momento de tu vida y según tu propia experiencia, no con lo que debería o
                podría ser cierto en general o para los demás. Responde basándote en cómo te has sentido en estos
                momentos de tu vida, señalando el número de la escala que mejor coincida con lo que sientes. 
                No hay respuestas correctas ni incorrectas, la mejor respuesta es la que mejor refleje lo que
                tú sientes y piensas.
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
                <Text>1. Los que me rodean estarían mejor si me fuera</Text>
                <SivariaRadioButton data={oneToSevenOptions} option={stepData.step10.inq1} onSelect={text => handleInputChange('inq1', text)}/>
            </View>
            <View style={{padding:5}}>
                <Text>2. Los que me rodean serían más felices sin mí</Text>
                <SivariaRadioButton data={oneToSevenOptions} option={stepData.step10.inq2} onSelect={text => handleInputChange('inq2', text)}/>
            </View>
            <View style={{padding:5}}>
                <Text>3. Creo que soy una carga para la sociedad</Text>
                <SivariaRadioButton data={oneToSevenOptions} option={stepData.step10.inq3} onSelect={text => handleInputChange('inq3', text)}/>
            </View>
            <View style={{padding:5}}>
                <Text>4. Creo que mi muerte sería un alivio para los demás</Text>
                <SivariaRadioButton data={oneToSevenOptions} option={stepData.step10.inq4} onSelect={text => handleInputChange('inq4', text)}/>
            </View>
            <View style={{padding:5}}>
                <Text>5. Creo que los que me rodean, desearían deshacerse de mí</Text>
                <SivariaRadioButton data={oneToSevenOptions} option={stepData.step10.inq5} onSelect={text => handleInputChange('inq5', text)}/>
            </View>
            <View style={{padding:5}}>
                <Text>6. Creo que empeoro las cosas para los que me rodean</Text>
                <SivariaRadioButton data={oneToSevenOptions} option={stepData.step10.inq6} onSelect={text => handleInputChange('inq6', text)}/>
            </View>
            <View style={{padding:5}}>
                <Text>7. Los demás se preocupan por mí</Text>
                <SivariaRadioButton data={oneToSevenOptions} option={stepData.step10.inq7} onSelect={text => handleInputChange('inq7', text)}/>
            </View>
            <View style={{padding:5}}>
                <Text>8. Siento que encajo, que he encontrado mi lugar en el mundo</Text>
                <SivariaRadioButton data={oneToSevenOptions} option={stepData.step10.inq8} onSelect={text => handleInputChange('inq8', text)}/>
            </View>
            <View style={{padding:5}}>
                <Text>9. Me relaciono muy poco con mis seres queridos</Text>
                <SivariaRadioButton data={oneToSevenOptions} option={stepData.step10.inq9} onSelect={text => handleInputChange('inq9', text)}/>
            </View>
            <View style={{padding:5}}>
                <Text>10. Tengo la suerte de tener muchos/as amigos/as que me cuidan y apoyan</Text>
                <SivariaRadioButton data={oneToSevenOptions} option={stepData.step10.inq10} onSelect={text => handleInputChange('inq10', text)}/>
            </View>
            <View style={{padding:5}}>
                <Text>11. Me siento desconectado de los demás</Text>
                <SivariaRadioButton data={oneToSevenOptions} option={stepData.step10.inq11} onSelect={text => handleInputChange('inq11', text)}/>
            </View>
            <View style={{padding:5}}>
                <Text>12. A menudo me siento como un extraño cuando quedo con gente</Text>
                <SivariaRadioButton data={oneToSevenOptions} option={stepData.step10.inq12} onSelect={text => handleInputChange('inq12', text)}/>
            </View>
            <View style={{padding:5}}>
                <Text>13. Siento que hay personas a las que puedo recurrir en momentos de necesidad</Text>
                <SivariaRadioButton data={oneToSevenOptions} option={stepData.step10.inq13} onSelect={text => handleInputChange('inq13', text)}/>
            </View>
            <View style={{padding:5}}>
                <Text>14. Me siento cerca de otras personas</Text>
                <SivariaRadioButton data={oneToSevenOptions} option={stepData.step10.inq14} onSelect={text => handleInputChange('inq14', text)}/>
            </View>
            <View style={{padding:5}}>
                <Text>15. Cada día tengo al menos una interacción (con alguien) que puede considerarse satisfactoria</Text>
                <SivariaRadioButton data={oneToSevenOptions} option={stepData.step10.inq15} onSelect={text => handleInputChange('inq15', text)}/>
            </View>
        </View>
    );
};

const Step11 = ({ stepData, setStepData }) => {
    const [localState, setLocalState] = useState({
        sena19: stepData.step11.sena19 || '',
        sena23: stepData.step11.sena23 || '',
        sena69: stepData.step11.sena69 || '',
        sena99: stepData.step11.sena99 || '',
        sena103: stepData.step11.sena103 || '',
        sena111: stepData.step11.sena111 || '',
        sena112: stepData.step11.sena112 || '',
        sena115: stepData.step11.sena115 || '',
        sena117: stepData.step11.sena117 || '',
        sena129: stepData.step11.sena129 || '',
        sena137: stepData.step11.sena137 || '',
        sena139: stepData.step11.sena139 || '',
        sena141: stepData.step11.sena141 || '',
        sena146: stepData.step11.sena146 || '',    
        sena150: stepData.step11.sena150 || '',
        sena188: stepData.step11.sena188 || '',
        injury1: stepData.step11.injury1 || '',

    });

    useEffect(() => {
        setLocalState({
            sena19: stepData.step11.sena19 || '',
            sena23: stepData.step11.sena23 || '',
            sena69: stepData.step11.sena69 || '',
            sena99: stepData.step11.sena99 || '',
            sena103: stepData.step11.sena103 || '',
            sena111: stepData.step11.sena111 || '',
            sena112: stepData.step11.sena112 || '',
            sena115: stepData.step11.sena115 || '',
            sena117: stepData.step11.sena117 || '',
            sena129: stepData.step11.sena129 || '',
            sena137: stepData.step11.sena137 || '',
            sena139: stepData.step11.sena139 || '',
            sena141: stepData.step11.sena141 || '',
            sena146: stepData.step11.sena146 || '',    
            sena150: stepData.step11.sena150 || '',
            sena188: stepData.step11.sena188 || '',
            injury1: stepData.step11.injury1 || '',
        });
    }, [stepData.step11]);

    const handleInputChange = (field, value) => {
        const updatedState = { ...localState, [field]: value };
        setLocalState(updatedState);
        setStepData((prevData) => ({ ...prevData, step11: updatedState }));
    };

    
    return (
        <View style={{padding:20, backgroundColor: 'white'}}>
            <Text style={{fontWeight: 'bold'}}>
                SENA
            </Text>
            <Text style={{fontWeight: 'bold'}}>
                Encontrarás varias frases sobre pensamientos y sentimientos que puedes 
                tener y también sobre cosas que haces o te han pasado. 
                Nos gustaría que leyeras detenidamente cada una de ellas y nos dijeras si lo que dice la frase te pasa a ti.
                Evalúa las frases siguiendo la siguiente escala
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
                <Text>19. Mis padres me pegan</Text>
                <SivariaRadioButton data={oneToFiveOptions} option={stepData.step11.sena19} onSelect={text => handleInputChange('sena19', text)}/>
            </View>
            <View style={{padding:5}}>
                <Text>23. Grito cuando me enfado o enojo</Text>
                <SivariaRadioButton data={oneToFiveOptions} option={stepData.step11.sena23} onSelect={text => handleInputChange('sena23', text)}/>
            </View>
            <View style={{padding:5}}>
                <Text>69. Me cuesta controlar mis emociones</Text>
                <SivariaRadioButton data={oneToFiveOptions} option={stepData.step11.sena69} onSelect={text => handleInputChange('sena69', text)}/>
            </View>
            <View style={{padding:5}}>
                <Text>99. Tengo problemas en casa</Text>
                <SivariaRadioButton data={oneToFiveOptions} option={stepData.step11.sena99} onSelect={text => handleInputChange('sena99', text)}/>
            </View>
            <View style={{padding:5}}>
                <Text>103. Amenazo a otros para conseguir lo que quiero</Text>
                <SivariaRadioButton data={oneToFiveOptions} option={stepData.step11.sena103} onSelect={text => handleInputChange('sena103', text)}/>
            </View>
            <View style={{padding:5}}>
                <Text>111. Tengo ganas de llorar</Text>
                <SivariaRadioButton data={oneToFiveOptions} option={stepData.step11.sena111} onSelect={text => handleInputChange('sena111', text)}/>
            </View>
            <View style={{padding:5}}>
                <Text>112. Tengo ataques de nervios o de ansiedad</Text>
                <SivariaRadioButton data={oneToFiveOptions} option={stepData.step11.sena112} onSelect={text => handleInputChange('sena112', text)}/>
            </View>
            <View style={{padding:5}}>
                <Text>115. Me insultan en el colegio, instituto o universidad</Text>
                <SivariaRadioButton data={oneToFiveOptions} option={stepData.step11.sena115} onSelect={text => handleInputChange('sena115', text)}/>
            </View>
            <View style={{padding:5}}>
                <Text>117. Me cuesta concentrarme</Text>
                <SivariaRadioButton data={oneToFiveOptions} option={stepData.step11.sena117} onSelect={text => handleInputChange('sena117', text)}/>
            </View>
            <View style={{padding:5}}>
                <Text>129. Me angustian o agobian mis problemas</Text>
                <SivariaRadioButton data={oneToFiveOptions} option={stepData.step11.sena129} onSelect={text => handleInputChange('sena129', text)}/>
            </View>
            <View style={{padding:5}}>
                <Text>137. Me siento solo/a</Text>
                <SivariaRadioButton data={oneToFiveOptions} option={stepData.step11.sena137} onSelect={text => handleInputChange('sena137', text)}/>
            </View>
            <View style={{padding:5}}>
                <Text>139. Pego a otros cuando me enfado o enojo</Text>
                <SivariaRadioButton data={oneToFiveOptions} option={stepData.step11.sena139} onSelect={text => handleInputChange('sena139', text)}/>
            </View>
            <View style={{padding:5}}>
                <Text>141. Pienso que mi vida no tiene sentido</Text>
                <SivariaRadioButton data={oneToFiveOptions} option={stepData.step11.sena141} onSelect={text => handleInputChange('sena141', text)}/>
            </View>
            <View style={{padding:5}}>
                <Text>146. Hago locuras para divertirme</Text>
                <SivariaRadioButton data={oneToFiveOptions} option={stepData.step11.sena146} onSelect={text => handleInputChange('sena146', text)}/>
            </View>
            <View style={{padding:5}}>
                <Text>150. Mis profesores dicen que no presto atención en clase</Text>
                <SivariaRadioButton data={oneToFiveOptions} option={stepData.step11.sena150} onSelect={text => handleInputChange('sena150', text)}/>
            </View>
            <View style={{padding:5}}>
                <Text>188. Tengo amigos de verdad</Text>
                <SivariaRadioButton data={oneToFiveOptions} option={stepData.step11.sena188} onSelect={text => handleInputChange('sena188', text)}/>
            </View>
            <Text style={{fontWeight: 'bold'}}>
                Información sobre autolesión
            </Text>
            <View style={{padding:5}}>
                <Text>1. ¿Durante el último año te has implicado intencionadamente daño (por ejemplo: cortarte o arañarte la piel, golpearte o morderte a ti mismo,...)?:</Text>
                <SivariaRadioButton data={yesNoData} option={stepData.step11.injury1} onSelect={text => handleInputChange('injury1', text)}/>
            </View>
        </View>
    );
};

const Step12 = ({ stepData, setStepData }) => {
    const [localState, setLocalState] = useState({
        family1: stepData.step12.family1 || '',
        family2: stepData.step12.family2 || '',
        family3: stepData.step12.family3 || '',
        family4: stepData.step12.family4 || '',
        family5: stepData.step12.family5 || '',
        family6: stepData.step12.family6 || '',
        family7: stepData.step12.family7 || '',
        family8: stepData.step12.family8 || '',
        /*
        fatherAge: stepData.step12.fatherAge || '',
        motherAge: stepData.step12.motherAge || '',
        divorcedParents: stepData.step12.divorcedParents || '',
        singleParentFamily: stepData.step12.singleParentFamily || '',
        psiquiatricTreatmentParent: stepData.step12.psiquiatricTreatmentParent || '',
        addictionParent: stepData.step12.addictionParent || '',
        conflictingRelationshipsChildParents: stepData.step12.conflictingRelationshipsChildParents || '',
        reconstructedFamily: stepData.step12.reconstructedFamily || '',
        */
    });

    useEffect(() => {
        setLocalState({
            family1: stepData.step12.family1 || '',
            family2: stepData.step12.family2 || '',
            family3: stepData.step12.family3 || '',
            family4: stepData.step12.family4 || '',
            family5: stepData.step12.family5 || '',
            family6: stepData.step12.family6 || '',
            family7: stepData.step12.family7 || '',
            family8: stepData.step12.family8 || '',
            /*
            fatherAge: stepData.step12.fatherAge || '',
            motherAge: stepData.step12.motherAge || '',
            divorcedParents: stepData.step12.divorcedParents || '',
            singleParentFamily: stepData.step12.singleParentFamily || '',
            psiquiatricTreatmentParent: stepData.step12.psiquiatricTreatmentParent || '',
            addictionParent: stepData.step12.addictionParent || '',
            conflictingRelationshipsChildParents: stepData.step12.conflictingRelationshipsChildParents || '',
            reconstructedFamily: stepData.step12.reconstructedFamily || '',
            */
        });
    }, [stepData.step12]);

    const handleInputChange = (field, value) => {
        // Change function to handleInputChange(text)
        //setLocalState(text);
        //setStepData((prevData) => ({ ...prevData, step1: text }));
        const updatedState = { ...localState, [field]: value };
        setLocalState(updatedState);
        setStepData((prevData) => ({ ...prevData, step12: updatedState }));
    };

    return (
        <View style={{padding:20, backgroundColor: 'white'}}>
            <Text style={{fontWeight:'bold'}}>
                A continuación, nos gustaría que respondas algunas preguntas sobre tu familia.
            </Text>
            <View style={{padding:5}}>
                <Text>1. Indique la edad de tu padre en el momento de tu nacimiento (años):</Text>
                <SivariaInput 
                    placeholder={'Edad padre'}
                    value={stepData.step12.family1}
                    onChangeText={text => handleInputChange('family1', text )}
                    autoCorrect={false}
                    autoCapitalize={'none'} 
                    inputMode={'numeric'}
                />
            </View>
            <View style={{padding:5}}>
                <Text>2. Indique la edad de tu madre en el momento de tu nacimiento (años):</Text>
                <SivariaInput 
                    placeholder={'Edad madre'}
                    value={stepData.step12.family2}
                    onChangeText={text => handleInputChange('family2', text )}
                    autoCorrect={false}
                    autoCapitalize={'none'} 
                    inputMode={'numeric'}
                />
            </View>
            <View style={{padding:5}}>
                <Text>3. Convives con tus padres en la misma casa habitualmente:</Text>
                <SivariaRadioButton data={yesNoData} option={stepData.step7.family3} onSelect={text => handleInputChange('family3', text)}/>
            </View>
            <View style={{padding:5}}>
                <Text>4. Indica si tus padres están separados o divorciados:</Text>
                <SivariaRadioButton data={yesNoData} option={stepData.step12.family4} onSelect={text => handleInputChange('family4', text)}/>
            </View>
            <View style={{padding:5}}>
                <Text>5. Indica si alguno de tus padres ha recibido tratamiento psicológico o psiquiátrico:</Text>
                <SivariaRadioButton data={yesNoData} option={stepData.step12.family5} onSelect={text => handleInputChange('family5', text)}/>                
            </View>
            <View style={{padding:5}}>
                <Text>6. Indica si alguno de tus padres ha recibido tratamiento por consumo de drogas o alcohol</Text>
                <SivariaRadioButton data={yesNoData} option={stepData.step12.family6} onSelect={text => handleInputChange('family6', text)}/>                
            </View>
            <View style={{padding:5}}>
                <Text>7. Indica si las relaciones con tus padres son conflictivas o problemáticas (tensión, rechazo, desinterés, peleas frecuentes...):</Text>
                <SivariaRadioButton data={yesNoData} option={stepData.step12.family7} onSelect={text => handleInputChange('family7', text)}/>                
            </View>
            <View style={{padding:5}}>
                <Text>8. Consideras que tu familia está reconstruida:</Text>
                <SivariaRadioButton data={yesNoData} option={stepData.step12.family8} onSelect={text => handleInputChange('family8', text)}/>                
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

export { Step1, Step2, Step3, Step4, Step5, Step6, Step7, Step8, Step9, Step10, Step11, Step12 };