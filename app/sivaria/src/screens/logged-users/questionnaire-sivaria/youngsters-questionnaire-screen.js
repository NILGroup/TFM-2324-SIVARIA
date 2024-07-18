import React, { useState } from "react";
import { View, Text, ActivityIndicator, StyleSheet, ScrollView, Pressable } from "react-native";
import Dropdown from "../../../components/dropdown";
import SivariaInput from "../../../components/sivaria-input";
import Container from "../../../components/component-containers/container";
import { ProgressSteps, ProgressStep } from 'react-native-progress-steps';
import SivariaRadioButton from "../../../components/sivaria-radio-button";

const CustomProgressSteps = ({ steps, currentStep, setCurrentStep }) => {
    return (
        <ScrollView horizontal style={styles.horizontalScrollView}>
            <View style={styles.stepContainer}>
                {steps.map((step, index) => (
                    <Pressable key={index} style={styles.stepButton} onPress={() => setCurrentStep(index)}>
                        <Text style={currentStep === index ? styles.activeStep : styles.inactiveStep}>{step}</Text>
                    </Pressable>
                ))}
            </View>
        </ScrollView>
    );
};

const YoungstersQuestionnaireSivariaScreen = () => {

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


    const [step1Data, setStep1Data] = useState({ 
        course: '', 
        age: '', 
        gender: '', 
        trans: ''
    });
    const [step2Data, setStep2Data] = useState({ 
        jobSituationFather: '', 
        jobSituationMother: '', 
        academicPerformance: '',
        previousPsychiatricTreatment: '',
        chronicDisease: '',
    });
    const [step3Data, setStep3Data] = useState({ 
        femaleSelfPerception: '', 
        maleSelfPerception: '',
        femaleOthersPerception: '',
        maleOthersPerception: '',
        weight: '',
        height: '',
        discriminationType: '',
    });
    
    const [step4Data, setStep4Data] = useState({ 
        vb1: '', 
        vb2: '',
        vb4: '',
        ab1: '',
        ab2: '',
        ab4: '',
        cybv1: '',
        cybv2: '',
        cybv3: '',
        cybb1: '',
        cybb2: '',
        cybb3: '',
    });

    const [step5Data, setStep5Data] = useState({ 
        rrss1: '', 
        rrss2: '',
        rrss3: '',
        rrss4: '',
        rrss5: '',
        rrss6: '',
        rrss7: '',
    });

    const [step6Data, setStep6Data] = useState({ 
        mcad1: '', 
        mcad2: '',
        mcad3: '',
        mcad4: '',
        mcad5: '',
        mcad6: '',
        mcad7: '',
        mcad8: '',
        mcad9: '',
        mcad10: '',
        mcad11: '',
        mcad12: '',
    });

    const [step7Data, setStep7Data] = useState({ 
        cerqs1: '', 
        cerqs2: '',
        cerqs3: '',
        cerqs4: '',
        cerqs5: '',
        cerqs6: '',
        cerqs7: '',
        cerqs8: '',
        cerqs9: '',
        cerqs10: '',
        cerqs11: '',
        cerqs12: '',
        cerqs13: '',
        cerqs14: '',
        cerqs15: '',
        cerqs16: '',
        cerqs17: '',
        cerqs18: '',
    });

    
    const [currentStep, setCurrentStep] = useState(0);
    /*
    const previousFunction = () => {
        console.log('ON PREVIOUS FUNCTION');
        console.log(currentStep);
        setCurrentStep(currentStep - 1);
        console.log(currentStep);
    }
    const nextFunction = () => {
        console.log('ON NEXT FUNCTION');
        console.log(currentStep);
        setCurrentStep(currentStep + 1);
        console.log(currentStep);
    }*/
   
    const previousFunction = () => {
        setCurrentStep(prevStep => Math.max(prevStep - 1, 0));
    };

    const nextFunction = () => {
        setCurrentStep(prevStep => prevStep + 1);
    };

    return(
        <View style={{ flex: 1 }}>
            <CustomProgressSteps 
                steps={['Paso 1', 'Paso 2', 'Paso 3', 'Paso 4', 'Paso 5', 'Paso 6', 'Paso 7', 'Paso 8', 'Paso 9']}
                currentStep={currentStep}
                setCurrentStep={setCurrentStep}
            />
                {console.log('CurrentStep = '+currentStep)}
            <ProgressSteps 
                borderWidth={0}
                labelFontSize={0}
                marginBottom={0}
                activeStep={currentStep}
                borderStyle="none"
                activeStepIconColor="transparent"
                activeStepIconBorderColor="transparent"
                completedProgressBarColor="transparent"
                disabledStepIconBorderColor="transparent"
                progressBarColor="transparent"
                completedCheckColor="transparent"
                completedStepNumColor="transparent"
                activeStepNumColor="transparent"
                disabledStepNumColor="transparent"
                completedLabelColor="transparent"
                activeLabelColor="transparent"
                labelColor="transparent"
                disabledStepIconColor="transparent"
                completedStepIconColor="transparent"
            >
                <ProgressStep label="Paso 1" nextBtnText="CONTINUAR" previousBtnText="VOLVER" onNext={nextFunction}>
                    <View style={{padding: 20, backgroundColor: 'white'}}>
                        <View style={{padding: 5}}>
                            <Text style={{fontWeight:'bold'}}>Curso:</Text>
                            <Dropdown 
                                items={courses}
                                placeholder={{ label: 'Selecciona un curso...', value: 'ninguno' }}
                                value={step1Data.course}
                                onValueChange={text => setStep1Data({ ...step1Data, course: text })}
                            />
                        </View>
                        <View style={{padding:5}}>
                            <Text style={{fontWeight:'bold'}}>Edad (en años):</Text>
                            <SivariaInput 
                                placeholder={'Edad'}
                                value={step1Data.age}
                                onChangeText={text => setStep1Data({ ...step1Data, age: text })}
                                autoCorrect={false}
                                autoCapitalize={'none'} 
                                inputMode={'numeric'}
                            />
                        </View>
                        <View style={{padding:5}}>
                            <Text style={{fontWeight:'bold'}}>Sexo:</Text>
                            <SivariaRadioButton data={genderData} option={step1Data.gender} onSelect={text => setStep1Data({...step1Data, gender: text})}/>
                        </View>
                        <View style={{padding:5}}>
                            <Text style={{fontWeight:'bold'}}>¿Te consideras una persona trans?:</Text>
                            <SivariaRadioButton data={transData} option={step1Data.trans} onSelect={text => setStep1Data({...step1Data, trans: text})}/>
                        </View>
                    </View>
                </ProgressStep>
                <ProgressStep label="Paso 2" nextBtnText="CONTINUAR" previousBtnText="VOLVER" onPrevious={previousFunction} onNext={nextFunction}>
                    <View style={{padding:20, backgroundColor: 'white'}}>
                        <View style={{padding:5}}>
                            <Text style={{fontWeight:'bold'}}>Indica la situación laboral actual de tu padre:</Text>
                            <SivariaRadioButton option={step2Data.jobSituationFather} data={parentsJobSituationData} onSelect={text => setStep2Data({...step2Data, jobSituationFather: text})}/>
                        </View>
                        <View style={{padding:5}}>
                            <Text style={{fontWeight:'bold'}}>Indica la situación laboral actual de tu madre:</Text>
                            <SivariaRadioButton option={step2Data.jobSituationMother} data={parentsJobSituationData} onSelect={text => setStep2Data({...step2Data, jobSituationMother: text})}/>
                        </View>
                        <View style={{padding:5}}>
                            <Text style={{fontWeight:'bold'}}>Señala cuál crees que es tu rendimiento académico en los dos últimos años:</Text>
                            <SivariaRadioButton option={step2Data.academicPerformance} data={academicPerformanceData} onSelect={text => setStep2Data({...step2Data, academicPerformance: text})}/>
                        </View>
                        <View style={{padding:5}}>
                            <Text style={{fontWeight:'bold'}}>
                                Señala si tienes en la actualidad o has tenido previamente tratamiento psiquiátrico y/o psicológico 
                                (por ejemplo, me han diagnosticado depresión o ansiedad):
                            </Text>
                            <SivariaRadioButton data={yesNoData} option={step2Data.previousPsychiatricTreatment} onSelect={text => setStep2Data({...step2Data, previousPsychiatricTreatment: text})}/>
                        </View>
                        <View style={{padding:5}}>
                            <Text style={{fontWeight:'bold'}}>
                                Indica si padeces alguna enfermedad crónica desde hace por lo menos un año 
                                (por ejemplo: me han diagnosticado, diabetes, epilepsia...):
                            </Text>
                            <SivariaRadioButton data={yesNoData} option={step2Data.chronicDisease} onSelect={text => setStep2Data({...step2Data, chronicDisease: text})}/>
                        </View>
                    </View>
                </ProgressStep>
                <ProgressStep label="Paso 3" nextBtnText="CONTINUAR" previousBtnText="VOLVER" onPrevious={previousFunction} onNext={nextFunction}>
                    <View style={{padding:20, backgroundColor: 'white'}}>
                        <View style={{padding:5}}>
                            <Text style={{fontWeight:'bold'}}>En general, ¿cómo te ves a ti mismo/a? (responde a ambas escalas: masculino y femenina). Evalúe de 0 a 6,
                            donde 0 significa Nada en absoluto y 6 completamente:</Text>
                            <Text>Femenina</Text>
                            <SivariaRadioButton data={selfPerceptionData} option={step3Data.femaleSelfPerception} onSelect={text => setStep3Data({...step3Data, femaleSelfPerception: text})}/>
                            <Text>Masculino</Text>
                            <SivariaRadioButton data={selfPerceptionData} option={step3Data.maleSelfPerception} onSelect={text => setStep3Data({...step3Data, maleSelfPerception: text})}/>
                        </View>
                        <View style={{padding:5}}>
                            <Text style={{fontWeight:'bold'}}>En general, ¿cómo crees que te ve la mayoría de la gente? (responde a ambas escalas: masculino y femenina). Evalúe de 0 a 6,
                            donde 0 significa Nada en absoluto y 6 completamente:</Text>
                            <Text>Femenina</Text>
                            <SivariaRadioButton data={selfPerceptionData} option={step3Data.femaleOthersPerception} onSelect={text => setStep3Data({...step3Data, femaleOthersPerception: text})}/>
                            <Text>Masculino</Text>
                            <SivariaRadioButton data={selfPerceptionData} option={step3Data.maleOthersPerception} onSelect={text => setStep3Data({...step3Data, maleOthersPerception: text})}/>
                        </View>
                        <View style={{padding:5}}>
                            <Text style={{fontWeight:'bold'}}>Cuánto pesas? (poner valor aproximado en kg):</Text>
                            <SivariaInput 
                                placeholder={'Peso'}
                                value={step3Data.weight}
                                onChangeText={text => setStep3Data({ ...step3Data, weight: text })}
                                autoCorrect={false}
                                autoCapitalize={'none'} 
                                inputMode={'numeric'}
                            />                             
                        </View>
                        <View style={{padding:5}}>
                            <Text style={{fontWeight:'bold'}}>Cuánto mides? (poner valor aproximado en cm):</Text>
                            <SivariaInput 
                                placeholder={'Altura'}
                                value={step3Data.height}
                                onChangeText={text => setStep3Data({ ...step3Data, height: text })}
                                autoCorrect={false}
                                autoCapitalize={'none'} 
                                inputMode={'numeric'}
                            />                        
                        </View>
                        <View style={{padding:5}}>
                            <Text style={{fontWeight:'bold'}}>Indica el tipo de discriminación sufrido. Si no has sufrido ninguno, pon Ninguno:</Text>
                            <Dropdown 
                                items={discriminationTypes}
                                placeholder={{ label: 'Selecciona una opción...', value: 'ninguno' }}
                                value={step3Data.discriminationType}
                                onValueChange={text => setStep3Data({ ...step3Data, discriminationType: text })}
                            />                        
                        </View>
                    </View>
                </ProgressStep>
                <ProgressStep label="Paso 4" nextBtnText="CONTINUAR" previousBtnText="VOLVER">
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
                            <SivariaRadioButton data={zeroToFourOptions} option={step4Data.vb1} onSelect={text => setStep4Data({...step4Data, vb1: text})}/>
                        </View>
                        <View style={{padding:5}}>
                            <Text>VB2. Alguien me ha insultado</Text>
                            <SivariaRadioButton data={zeroToFourOptions} option={step4Data.vb2} onSelect={text => setStep4Data({...step4Data, vb2: text})}/>
                        </View>
                        <View style={{padding:5}}>
                            <Text>VB4. Alguien me ha amenazado</Text>
                            <SivariaRadioButton data={zeroToFourOptions} option={step4Data.vb4} onSelect={text => setStep4Data({...step4Data, vb4: text})}/>
                        </View>
                        <View style={{padding:5}}>
                            <Text>AB1. He golpeado, pateado o empujado a alguien</Text>
                            <SivariaRadioButton data={zeroToFourOptions} option={step4Data.ab1} onSelect={text => setStep4Data({...step4Data, ab1: text})}/>
                        </View>
                        <View style={{padding:5}}>
                            <Text>AB2. He insultado he dicho palabras malsonantes a alguien porque quería hacerle daño</Text>
                            <SivariaRadioButton data={zeroToFourOptions} option={step4Data.ab2} onSelect={text => setStep4Data({...step4Data, ab2: text})}/>                
                        </View>
                        <View style={{padding:5}}>
                            <Text>AB4. He amenazado a alguien</Text>
                            <SivariaRadioButton data={zeroToFourOptions} option={step4Data.ab4} onSelect={text => setStep4Data({...step4Data, ab4: text})}/>                
                        </View>
                        <View style={{padding:5}}>
                            <Text>CybV1. Alguien me ha dicho palabras malsonantes o me ha insultado usando el email o SMS</Text>
                            <SivariaRadioButton data={zeroToFourOptions} option={step4Data.cybv1} onSelect={text => setStep4Data({...step4Data, cybv1: text})}/>                
                        </View>
                        <View style={{padding:5}}>
                            <Text>CybV2. Alguien le ha dicho a otros palabras malsonantes sobre mí usando Internet o SMS</Text>
                            <SivariaRadioButton data={zeroToFourOptions} option={step4Data.cybv2} onSelect={text => setStep4Data({...step4Data, cybv2: text})}/>                
                        </View>
                        <View style={{padding:5}}>
                            <Text>CybV3. Alguien me ha amenazado a través de mensajes en Interne o SMS</Text>
                            <SivariaRadioButton data={zeroToFourOptions} option={step4Data.cybv3} onSelect={text => setStep4Data({...step4Data, cybv3: text})}/>                
                        </View>
                        <View style={{padding:5}}>
                            <Text>CybB1. He dicho palabras malsonantes a alguien o le he insultado usando SMS o mensajes en Internet</Text>
                            <SivariaRadioButton data={zeroToFourOptions} option={step4Data.cybb1} onSelect={text => setStep4Data({...step4Data, cybb1: text})}/>                
                        </View>
                        <View style={{padding:5}}>
                            <Text>CybB2. He dicho palabras malsonantes sobre alguien a otras personas en mensajes por Internet o por SMS</Text>
                            <SivariaRadioButton data={zeroToFourOptions} option={step4Data.cybb2} onSelect={text => setStep4Data({...step4Data, cybb2: text})}/>                
                        </View>
                        <View style={{padding:5}}>
                            <Text>CybB3. He amenazado a alguien a través de SMS o mensajes en Internet</Text>
                            <SivariaRadioButton data={zeroToFourOptions} option={step4Data.cybb3} onSelect={text => setStep4Data({...step4Data, cybb3: text})}/>                
                        </View>
                    </View>
                </ProgressStep>
                
                <ProgressStep label="Paso 5" nextBtnText="CONTINUAR" previousBtnText="VOLVER">
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
                            <SivariaRadioButton data={yesNoData} option={step5Data.rrss1} onSelect={text => setStep5Data({...step5Data, rrss1: text})}/>
                        </View>
                        <View style={{padding:5}}>
                            <Text>2. ¿Has buscado alguna vez información o te has metido en un foro sobre el suicidio y/o autolesión en Internet?</Text>
                            <SivariaRadioButton data={yesNoData} option={step5Data.rrss2} onSelect={text => setStep5Data({...step5Data, rrss2: text})}/>
                        </View>
                        <View style={{padding:5}}>
                            <Text>3. ¿Alguna vez has sentido la necesidad de hacerte daño y has compartido tu pensamiento a través de alguna red social o Internet?</Text>
                            <SivariaRadioButton data={yesNoData} option={step5Data.rrss3} onSelect={text => setStep5Data({...step5Data, rrss3: text})}/>
                        </View>
                        <View style={{padding:5}}>
                            <Text>4. ¿Alguna vez has sentido angustia, tristeza, desesperación, o te has sentido solo, lo has compartido o has buscado ayuda en Internet?</Text>
                            <SivariaRadioButton data={yesNoData} option={step5Data.rrss4} onSelect={text => setStep5Data({...step5Data, rrss4: text})}/>
                        </View>
                        <View style={{padding:5}}>
                            <Text>5. ¿Alguna vez has sentido la tentación de hacerte daño después de ver algún tipo de contenido en Internet?</Text>
                            <SivariaRadioButton data={yesNoData} option={step5Data.rrss5} onSelect={text => setStep5Data({...step5Data, rrss5: text})}/>                
                        </View>
                        <View style={{padding:5}}>
                            <Text>6. ¿Alguna vez has sentido la tentación de hacerte daño y has buscado ayuda en Internet?</Text>
                            <SivariaRadioButton data={yesNoData} option={step5Data.rrss6} onSelect={text => setStep5Data({...step5Data, rrss6: text})}/>                
                        </View>
                        <View style={{padding:5}}>
                            <Text>7. ¿Conoces a alguien que haya compartido alguna foto, pensamiento o comportamiento autolesivo en Internet?</Text>
                            <SivariaRadioButton data={yesNoData} option={step5Data.rrss7} onSelect={text => setStep5Data({...step5Data, rrss7: text})}/>                
                        </View>
                    </View>
                </ProgressStep>

                <ProgressStep label="Paso 6"  nextBtnText="CONTINUAR" previousBtnText="VOLVER">
                    <View style={{padding:20, backgroundColor: 'white'}}>
                        <Text style={{fontWeight:'bold'}}>
                            MULTICAGE CAD-4
                        </Text>
                        <Text style={{fontWeight:'bold'}}>
                            Por favor, responde Sí/No a las siguientes preguntas
                        </Text>
                        <View style={{padding:5}}>
                            <Text>1. ¿Has pensado alguna vez que deberías beber menos alcohol?</Text>
                            <SivariaRadioButton data={yesNoData} option={step6Data.mcad1} onSelect={text => setStep6Data({...step6Data, mcad1: text})}/>
                        </View>
                        <View style={{padding:5}}>
                            <Text>2. ¿Te has sentido molesto/a cuando alguna persona te ha criticado tu manera o forma de beber alcohol?</Text>
                            <SivariaRadioButton data={yesNoData} option={step6Data.mcad2} onSelect={text => setStep6Data({...step6Data, mcad2: text})}/>
                        </View>
                        <View style={{padding:5}}>
                            <Text>3. ¿Te has sentido culpable alguna vez por tu manera o forma de beber alcohol?</Text>
                            <SivariaRadioButton data={yesNoData} option={step6Data.mcad3} onSelect={text => setStep6Data({...step6Data, mcad3: text})}/>
                        </View>
                        <View style={{padding:5}}>
                            <Text>4. ¿Alguna vez lo primero que has hecho por la mañana es beber alguna bebida alcohólica para relajarte o para eliminar la resaca?</Text>
                            <SivariaRadioButton data={yesNoData} option={step6Data.mcad4} onSelect={text => setStep6Data({...step6Data, mcad4: text})}/>
                        </View>
                        <View style={{padding:5}}>
                            <Text>5. ¿Has pensado alguna vez que deberías consumir menos drogas?</Text>
                            <SivariaRadioButton data={yesNoData} option={step6Data.mcad5} onSelect={text => setStep5Data({...step6Data, mcad5: text})}/>
                        </View>
                        <View style={{padding:5}}>
                            <Text>6. ¿Niegas el consumo de drogas a familiares, amigos o compañeros para evitar que te critiquen?</Text>
                            <SivariaRadioButton data={yesNoData} option={step6Data.mcad6} onSelect={text => setStep6Data({...step6Data, mcad6: text})}/>
                        </View>
                        <View style={{padding:5}}>
                            <Text>7. ¿Has tenido problemas psicológicos, económicos, laborales o familiares a causa del consumo de drogas?</Text>
                            <SivariaRadioButton data={yesNoData} option={step6Data.mcad7} onSelect={text => setStep6Data({...step6Data, mcad7: text})}/>
                        </View>
                        <View style={{padding:5}}>
                            <Text>8. ¿Te sientes a veces impulsado a consumir drogas aunque hayas decidido no hacerlo?</Text>
                            <SivariaRadioButton data={yesNoData} option={step6Data.mcad8} onSelect={text => setStep6Data({...step6Data, mcad8: text})}/>
                        </View>
                        <View style={{padding:5}}>
                            <Text>9. ¿Dedicas más tiempo del que crees que deberías a estar conectado a Internet con objetivos distintos a los de tu trabajo?</Text>
                            <SivariaRadioButton data={yesNoData} option={step6Data.mcad9} onSelect={text => setStep6Data({...step6Data, mcad9: text})}/>
                        </View>
                        <View style={{padding:5}}>
                            <Text>10. ¿Se han quejado tus familiares de las horas que dedicas a Internet?</Text>
                            <SivariaRadioButton data={yesNoData} option={step6Data.mcad10} onSelect={text => setStep6Data({...step6Data, mcad10: text})}/>
                        </View>
                        <View style={{padding:5}}>
                            <Text>11. ¿Te resulta duro permanecer alejado/a de Internet varios días seguidos?</Text>
                            <SivariaRadioButton data={yesNoData} option={step6Data.mcad11} onSelect={text => setStep6Data({...step6Data, mcad11: text})}/>
                        </View>
                        <View style={{padding:5}}>
                            <Text>12. ¿Tienes problemas para controlar el impulso de conectarte a Internet o has intentado sin éxito reducir el tiempo que dedicas a estar conectado/a?</Text>
                            <SivariaRadioButton data={yesNoData} option={step6Data.mcad12} onSelect={text => setStep6Data({...step6Data, mcad12: text})}/>
                        </View>
                    </View>
                </ProgressStep>

                <ProgressStep label="Paso 7" nextBtnText="CONTINUAR" previousBtnText="VOLVER">
                    <View style={{padding:20, backgroundColor: 'white'}}>
                        <Text style={{fontWeight:'bold'}}>
                            CERQ-S
                        </Text>
                        <Text style={{fontWeight:'bold'}}>
                            Todos nos enfrentamos en algún moento con acontacimiento que resultan negativos o desagradables,
                            y cada uno de nosotros responde ante ellos de una forma personal. 
                            En las siguientes frases te pedimos que indiques lo que piensas habitualmente cuando
                            te enfrentas a una experiencia negativa o desagradable. 
                            Por favor, señala la opción que más se aproxime a tus pensamientos habituales en esos momentos.
                            Evalúe de 1 a 5, donde 1 significa casi nunca y 5 casi siempre.
                        </Text>
                        <View style={{padding:5}}>
                            <Text>1. Siento que soy el único culpable de lo que ha pasado</Text>
                            <SivariaRadioButton data={oneToFiveOptions} option={step7Data.cerqs1} onSelect={text => setStep7Data({...step7Data, cerqs1: text})}/>
                        </View>
                        <View style={{padding:5}}>
                            <Text>2. Creo que tengo que acpear lo que ha pasado</Text>
                            <SivariaRadioButton data={oneToFiveOptions} option={step7Data.cerqs2} onSelect={text => setStep7Data({...step7Data, cerqs2: text})}/>
                        </View>
                        <View style={{padding:5}}>
                            <Text>3. Pienso a menudo en cómo me siento en relación con lo que me ha pasado</Text>
                            <SivariaRadioButton data={oneToFiveOptions} option={step7Data.cerqs3} onSelect={text => setStep7Data({...step7Data, cerqs3: text})}/>
                        </View>
                        <View style={{padding:5}}>
                            <Text>4. Me parece que otros son culpables de lo ocurrido</Text>
                            <SivariaRadioButton data={oneToFiveOptions} option={step7Data.cerqs4} onSelect={text => setStep7Data({...step7Data, cerqs4: text})}/>
                        </View>
                        <View style={{padding:5}}>
                            <Text>5. Me siento único/a responsable de lo ocurrido</Text>
                            <SivariaRadioButton data={oneToFiveOptions} option={step7Data.cerqs5} onSelect={text => setStep7Data({...step7Data, cerqs5: text})}/>                
                        </View>
                        <View style={{padding:5}}>
                            <Text>6. Creo que tengo que aceptar la situación</Text>
                            <SivariaRadioButton data={oneToFiveOptions} option={step7Data.cerqs6} onSelect={text => setStep7Data({...step7Data, cerqs6: text})}/>                
                        </View>
                        <View style={{padding:5}}>
                            <Text>7. Me preocupa lo que piense y sienta sobre lo que me ha pasado</Text>
                            <SivariaRadioButton data={oneToFiveOptions} option={step7Data.cerqs7} onSelect={text => setStep7Data({...step7Data, cerqs7: text})}/>                
                        </View>
                        <View style={{padding:5}}>
                            <Text>8. Pienso en cosas agradables que nada tienen que ver con lo que me ha pasado</Text>
                            <SivariaRadioButton data={oneToFiveOptions} option={step7Data.cerqs8} onSelect={text => setStep5Data({...step7Data, cerqs8: text})}/>                
                        </View>
                        <View style={{padding:5}}>
                            <Text>9. Pienso en cuál sería la mejor forma de enfrentarme a la situación</Text>
                            <SivariaRadioButton data={oneToFiveOptions} option={step7Data.cerqs9} onSelect={text => setStep5Data({...step7Data, cerqs9: text})}/>                
                        </View>
                        <View style={{padding:5}}>
                            <Text>10. Sigo pensando en lo terrible que ha sido lo que me ha pasado</Text>
                            <SivariaRadioButton data={oneToFiveOptions} option={step7Data.cerqs10} onSelect={text => setStep5Data({...step7Data, cerqs10: text})}/>                
                        </View>
                        <View style={{padding:5}}>
                            <Text>11. Me parece que otros son responsables de lo que ha ocurrido</Text>
                            <SivariaRadioButton data={oneToFiveOptions} option={step7Data.cerqs11} onSelect={text => setStep5Data({...step7Data, cerqs11: text})}/>                
                        </View>
                        <View style={{padding:5}}>
                            <Text>12. Pienso en algo agradable en vez de pensar en lo ocurrido</Text>
                            <SivariaRadioButton data={oneToFiveOptions} option={step7Data.cerqs12} onSelect={text => setStep5Data({...step7Data, cerqs12: text})}/>                
                        </View>
                        <View style={{padding:5}}>
                            <Text>13. Creo que la situación tiene también su lado positivo</Text>
                            <SivariaRadioButton data={oneToFiveOptions} option={step7Data.cerqs13} onSelect={text => setStep5Data({...step7Data, cerqs13: text})}/>                
                        </View>
                        <View style={{padding:5}}>
                            <Text>14. Creo que no ha sido tan malo en comparación a otras cosas</Text>
                            <SivariaRadioButton data={oneToFiveOptions} option={step7Data.cerqs14} onSelect={text => setStep5Data({...step7Data, cerqs14: text})}/>                
                        </View>
                        <View style={{padding:5}}>
                            <Text>15. Pienso en un plan acerca de lo mejor que podría hacer</Text>
                            <SivariaRadioButton data={oneToFiveOptions} option={step7Data.cerqs15} onSelect={text => setStep5Data({...step7Data, cerqs15: text})}/>                
                        </View>
                        <View style={{padding:5}}>
                            <Text>16. Busco los aspectos positivos de la cuestión</Text>
                            <SivariaRadioButton data={oneToFiveOptions} option={step7Data.cerqs16} onSelect={text => setStep5Data({...step7Data, cerqs16: text})}/>                
                        </View>
                        <View style={{padding:5}}>
                            <Text>17. Me digo que hay cosas peores en la vida</Text>
                            <SivariaRadioButton data={oneToFiveOptions} option={step7Data.cerqs17} onSelect={text => setStep5Data({...step7Data, cerqs17: text})}/>                
                        </View>
                        <View style={{padding:5}}>
                            <Text>18. Pienso continuamente en lo horrible que ha sido la situación</Text>
                            <SivariaRadioButton data={oneToFiveOptions} option={step7Data.cerqs18} onSelect={text => setStep5Data({...step7Data, cerqs18: text})}/>                
                        </View>
                    </View>
                </ProgressStep>
                <ProgressStep label="FINAL">

                </ProgressStep>

            </ProgressSteps>
        </View>
    );
}
/*
const styles = StyleSheet.create({
    container: {
        flex: 1,
        alignItems: 'center',
        justifyContent: 'center',
        margin: 20,
    },
    containerButtonStyle:{
        display: 'flex',
        flexDirection: 'row',
        justifyContent: 'flex-end',
        paddingLeft: 10,
        paddingRight: 30,
    }
});
*/
const styles = StyleSheet.create({
    container: {
        flex: 1,
    },
    horizontalScrollView: {
        flexGrow: 0,
    },
    stepContainer: {
        flexDirection: 'row',
    },
    stepButton: {
        marginHorizontal: 10,
        padding: 10,
    },
    activeStep: {
        color: 'blue',
        fontWeight: 'bold',
    },
    inactiveStep: {
        color: 'gray',
    },
});
export default YoungstersQuestionnaireSivariaScreen;