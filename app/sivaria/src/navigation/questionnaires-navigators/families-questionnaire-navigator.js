import { useState, useRef, useEffect } from "react";
import { View, ScrollView, Pressable, StyleSheet, Text, Dimensions } from "react-native";
import { createNativeStackNavigator } from "@react-navigation/native-stack";
import { Step1, Step2, Step3, Step4, Step5,Step6,Step7,Step8,Step9,Step10, Step11, Step12 } from "../../screens/logged-users/forms/family-multi-step-form/steps";
import axiosInstance from "../../utils/axios-config-web";
import { useToast } from "react-native-toast-notifications";
import LoadingScreen from "../../screens/loading-screen";
import { getItemLocalStorage } from "../../utils/general-local-storage";

const FamiliesStack = createNativeStackNavigator();

const steps = [
  { name: 'Step1', component: Step1 },
  { name: 'Step2', component: Step2 },
  { name: 'Step3', component: Step3 },
  { name: 'Step4', component: Step4 },
  { name: 'Step5', component: Step5 },
];

export const FamiliesStackNavigator = ({navigation}) => {

    const [currentStep, setCurrentStep] = useState(0);
    const scrollViewRef = useRef(null);
    
    const [isLoading, setIsLoading] = useState(false);
    
    const toast = useToast();
    
    const [stepData, setStepData] = useState({
        step1: {
            idChild: '',
            course: '',
        },
        step2: {
            sena104: '',
            sena117: '',
            sena118: '',
            sena121: '',
            sena123: '',
            sena124: '',
            sena125: '',
            sena135: '',
            sena137: '',
            sena138: '',
            sena139: '',
            sena140: '',
            sena145: '',
            sena146: '',    
            sena148: '',
            sena154: ''
        },
        step3: {
            family12: '',
            family13: '',
            jobSituationFather: '', 
            jobSituationMother: '', 
            academicLevelFather: '', 
            academicLevelMother: '',
            family1: '',
            family2: '',
            family3: '',
            family4: '',
            family5: '',
            family6: '',
            family7: '',
            family8: '',
        },
        step4: {
            parq1: '',
            parq2: '',
            parq3: '',
            parq4: '',
            parq5: '',
            parq6: '',
            parq7: '',
            parq8: '',
            parq9: '',
            parq10: '',
            parq11: '',
            parq12: '',
            parq13: '',
            parq14: '',
        },
        step5: {
            parq15: '',
            parq16: '',
            parq17: '',
            parq18: '',
            parq19: '',
            parq20: '',
            parq21: '',
            parq22: '',
            parq23: '',
            parq24: '',
            parq25: '',
            parq26: '',
            parq27: '',
            parq28: '',
            parq29: '',
        }
    });

    const [validations, setValidations] = useState({
        step1: {
            idChild: false,
            course: false,
        },
        step2: {
            sena104: false,
            sena117: false,
            sena118: false,
            sena121: false,
            sena123: false,
            sena124: false,
            sena125: false,
            sena135: false,
            sena137: false,
            sena138: false,
            sena139: false,
            sena140: false,
            sena145: false,
            sena146: false,    
            sena148: false,
            sena154: false
        },
        step3: {
            family12: false,
            family13: false,
            jobSituationFather: false, 
            jobSituationMother: false, 
            academicLevelFather: false, 
            academicLevelMother: false,
            family1: false,
            family2: false,
            family3: false,
            family4: false,
            family5: false,
            family6: false,
            family7: false,
            family8: false,
        },
        step4: {
            parq1: false,
            parq2: false,
            parq3: false,
            parq4: false,
            parq5: false,
            parq6: false,
            parq7: false,
            parq8: false,
            parq9: false,
            parq10: false,
            parq11: false,
            parq12: false,
            parq13: false,
            parq14: false,
        },
        step5: {
            parq15: false,
            parq16: false,
            parq17: false,
            parq18: false,
            parq19: false,
            parq20: false,
            parq21: false,
            parq22: false,
            parq23: false,
            parq24: false,
            parq25: false,
            parq26: false,
            parq27: false,
            parq28: false,
            parq29: false,
        }
    });

    useEffect(() => {
        scrollViewRef.current?.scrollTo({
            x: currentStep * (screenWidth / steps.length), // Desplaza el ScrollView al paso actual
            animated: true
        });
    }, [currentStep]);

    const nextStep = () => {
        if (currentStep < steps.length - 1) {
            setCurrentStep(currentStep + 1);
        }
    };

    const prevStep = () => {
        if (currentStep > 0) {
            setCurrentStep(currentStep - 1);
        }
    };

    const goToStep = (index) => {
        setCurrentStep(index);
    };
    
    const validateFormByStep = () => {
        const { idChild, course } = stepData.step1;

        const { sena104, sena117, sena118, sena121, sena123,
            sena124, sena125, sena135, sena137, sena138, sena139,
            sena140, sena145, sena146, sena148, sena154 } = stepData.step2;

        const { family12, family13, jobSituationFather, jobSituationMother, 
            academicLevelFather, academicLevelMother, family1, family2, family3, family4, family5, family6, family7, family8 } = stepData.step3;
        
        const { parq1, parq2, parq3, parq4, parq5, parq6, parq7, parq8,
            parq9, parq10, parq11, parq12, parq13, parq14 } = stepData.step4;

        const { parq15, parq16, parq17, parq18, parq19, parq20, parq21, parq22,
            parq23, parq24, parq25, parq26, parq27, parq28, parq29 } = stepData.step5;


        const newValidationsStep1 = {
            idChild: idChild === '',
            course: course === '',
        };
        const newValidationsStep2 = {
            sena104: sena104 === '',
            sena117: sena117 === '',
            sena118: sena118 === '',
            sena121: sena121 === '',
            sena123: sena123 === '',
            sena124: sena124 === '',
            sena125: sena125 === '',
            sena135: sena135 === '',
            sena137: sena137 === '',
            sena138: sena138 === '',
            sena139: sena139 === '',
            sena140: sena140 === '',
            sena145: sena145 === '',
            sena146: sena146 === '',    
            sena148: sena148 === '',
            sena154: sena154 === ''
        };
        const newValidationsStep3 = {
            family12: family12 === '', 
            family13: family13 === '', 
            jobSituationFather: jobSituationFather === '', 
            jobSituationMother: jobSituationMother === '', 
            academicLevelFather: academicLevelFather === '', 
            academicLevelMother: academicLevelMother === '', 
            family1: family1 === '', 
            family2: family2 === '', 
            family3: family3 === '', 
            family4: family4 === '', 
            family5: family5 === '', 
            family6: family6 === '', 
            family7: family7 === '', 
            family8: family8 === ''
        };

        const newValidationsStep4 = {
            parq1: parq1 === '',
            parq2: parq2 === '',
            parq3: parq3 === '',
            parq4: parq4 === '',
            parq5: parq5 === '',
            parq6: parq6 === '',
            parq7: parq7 === '',
            parq8: parq8 === '',
            parq9: parq9 === '',
            parq10: parq10 === '',
            parq11: parq11 === '',
            parq12: parq12 === '',
            parq13: parq13 === '',
            parq14: parq14 === '',
        };

        const newValidationsStep5 = {
            parq15: parq15 === '',
            parq16: parq16 === '',
            parq17: parq17 === '',
            parq18: parq18 === '',
            parq19: parq19 === '',
            parq20: parq20 === '',
            parq21: parq21 === '',
            parq22: parq22 === '',
            parq23: parq23 === '',
            parq24: parq24 === '',
            parq25: parq25 === '',
            parq26: parq26 === '',
            parq27: parq27 === '',
            parq28: parq28 === '',
            parq29: parq29 === '',
        };

        const newValidations = {
            step1: newValidationsStep1,
            step2: newValidationsStep2,
            step3: newValidationsStep3,
            step4: newValidationsStep4,
            step5: newValidationsStep5,
        }

        setValidations(newValidations);

        return newValidations;
    }

    const validateForm = () => {

        const newValidations = validateFormByStep();

        const { step1, step2, 
            step3, step4, step5 } = newValidations;

        let step1Valid = (
            !step1.idChild &&
            !step1.course
        );
        let step2Valid = (
            !step2.sena104 &&
            !step2.sena117 &&
            !step2.sena118 &&
            !step2.sena121 &&
            !step2.sena123 &&
            !step2.sena124 &&
            !step2.sena125 &&
            !step2.sena135 &&
            !step2.sena137 &&
            !step2.sena138 &&
            !step2.sena139 &&
            !step2.sena140 &&
            !step2.sena145 &&
            !step2.sena146 &&    
            !step2.sena148 &&
            !step2.sena154
        );
        let step3Valid = (
            !step3.family12 &&
            !step3.family13 &&
            !step3.jobSituationFather &&
            !step3.jobSituationMother &&
            !step3.academicLevelFather &&
            !step3.academicLevelMother &&
            !step3.family1 &&
            !step3.family2 &&
            !step3.family3 &&
            !step3.family4 &&
            !step3.family5 &&
            !step3.family6 &&
            !step3.family7 &&
            !step3.family8
        );
        let step4Valid = (
            !step4.parq1 &&
            !step4.parq2 &&
            !step4.parq3 &&
            !step4.parq4 &&
            !step4.parq5 &&
            !step4.parq6 &&
            !step4.parq7 &&
            !step4.parq8 &&
            !step4.parq9 &&
            !step4.parq10 &&
            !step4.parq11 &&
            !step4.parq12 &&
            !step4.parq13 &&
            !step4.parq14
        );
        let step5Valid = (
            !step5.parq15 &&
            !step5.parq16 &&
            !step5.parq17 &&
            !step5.parq18 &&
            !step5.parq19 &&
            !step5.parq20 &&
            !step5.parq21 &&
            !step5.parq22 &&
            !step5.parq23 &&
            !step5.parq24 &&
            !step5.parq25 &&
            !step5.parq26 &&
            !step5.parq27 &&
            !step5.parq28 &&
            !step5.parq29
        );

        return {
            step1Valid: step1Valid,
            step2Valid: step2Valid, 
            step3Valid: step3Valid, 
            step4Valid: step4Valid, 
            step5Valid: step5Valid,          
        };
    }

    async function handleSubmit() {
        // Maneja el envío del formulario
        //const errors = validateStep(stepData);

        let { 
            step1Valid,
            step2Valid, 
            step3Valid, 
            step4Valid, 
            step5Valid
        } = validateForm();
        
        if (step1Valid &&
            step2Valid && 
            step3Valid && 
            step4Valid && 
            step5Valid) 
        {

            setIsLoading(true);
            let base64_stepData = btoa(JSON.stringify(stepData));
            console.log(base64_stepData);
            let data = {
                email: await getItemLocalStorage('email'),
                user_data_sivaria: base64_stepData
            };

            console.log('Formulario enviado', stepData);
            
            await axiosInstance.post("/sivaria/v1/expertSystem/predict", data)
            .then(async function (response) {
                console.log('Formulario enviado', stepData);
                let message = 'Cuestionario enviado correctamente.\nLe llegará una notificación con los resultados y se le enviará por correo, tanto a usted como a al profesional a cargo.'
                toast.show(message,{type: 'success'});
                setIsLoading(false);
                navigation.navigate('Dashboard');
            })
            .catch(function (error) {
                setIsLoading(false);
                toast.show('Error en el envío y procesamiento del cuestionario. ' + error.response.data.data,{type: 'danger'});
            });
            setIsLoading(false);
        }
        else {
            let message = 'Hay campos vacíos en las siguientes páginas del formulario:\n';
            
            if(!step1Valid) {
                message += 'Página 1\n';
            }
            if(!step2Valid) {
                message += 'Página 2\n';
            }
            if(!step3Valid) {
                message += 'Página 3\n';
            }
            if(!step4Valid) {
                message += 'Página 4\n';
            }
            if(!step5Valid) {
                message += 'Página 5';
            }

            toast.show(
                message,
                {
                    type: 'danger'
                }
            );
        }
      };

    const CurrentStepComponent = steps[currentStep].component;

    if (isLoading) {
        return (
            <LoadingScreen />
        );
    }

    return (
        <View style={{ flex: 1 }}>
            <View style={styles.progressBarContainer}>
                <ScrollView             
                    ref={scrollViewRef}
                    horizontal 
                    showsHorizontalScrollIndicator={false} 
                    contentContainerStyle={styles.progressBar}
                >
                    {steps.map((step, index) => (
                        /*
                        <View key={index} style={[styles.step, currentStep === index && styles.currentStep]}>
                            <Text>{step.name}</Text>
                        </View>*/
                        <Pressable key={index} onPress={() => goToStep(index)} style={[styles.step, currentStep === index && styles.currentStep]}>
                            <Text style={styles.stepText}>{step.name}</Text>
                        </Pressable>
                    ))}
                </ScrollView>
            </View>
            <ScrollView style={{ flex: 1 }}>
                <CurrentStepComponent stepData={stepData} setStepData={setStepData} validations={validations} />
            </ScrollView>
            <View style={styles.navigationButtons}>
                {currentStep > 0 ? 
                    (
                        <Pressable onPress={prevStep} style={styles.button}>
                            <Text style={styles.buttonText}>VOLVER</Text>
                        </Pressable>
                    ) : <View style={styles.placeholder} />
                } 
                {currentStep < steps.length - 1 ? 
                    (
                        <Pressable onPress={nextStep} style={styles.button}>
                            <Text style={styles.buttonText}>CONTINUAR</Text>
                        </Pressable>
                    ) : 
                    (
                        <Pressable onPress={handleSubmit} style={styles.button}>
                            <Text style={styles.buttonText}>ENVIAR</Text>
                        </Pressable> 
                    )
                }
            </View>
        </View>
    );
};

const screenWidth = Dimensions.get('window').width;

const styles = StyleSheet.create({
    progressBarContainer: {
        alignItems: 'center', // Centra el contenedor de la barra de progreso
        marginVertical: 20
    },



    progressBar: {
      flexDirection: 'row',
      padding: 10,
      backgroundColor: '#eee',



      minWidth: screenWidth,
      justifyContent: 'center', // Asegura que el contenido esté centrado horizontalmente
    },
    step: {
      padding: 10,
      marginHorizontal: 5,
      borderRadius: 5,
      backgroundColor: '#ccc',
      justifyContent: 'center',
      alignItems: 'center'
    },
    currentStep: {
      backgroundColor: '#006E51'
    },


    stepText: {
        color: '#fff',
        fontWeight: 'bold'
    },

    navigationButtons: {
      flexDirection: 'row',
      justifyContent: 'space-between',
      padding: 20
    },

    button: {
        padding: 10,
        backgroundColor: '#006E51',
        borderRadius: 5,

        width: 125,
    },
    buttonText: {
        color: '#fff',
        fontWeight: 'bold',
        textAlign:'center',
    },
    placeholder: {
        width: 100, // Ajusta según sea necesario para que coincida con el tamaño de los botones
    }
  });
  