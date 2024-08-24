import { useState, useRef, useEffect } from "react";
import { View, ScrollView, Pressable, StyleSheet, Text, Dimensions } from "react-native";
import { createNativeStackNavigator } from "@react-navigation/native-stack";
import { Step1, Step2, Step3 } from "../../screens/logged-users/forms/professional-multi-step-form/steps";
import axiosInstance from "../../utils/axios-config-web";
import { useToast } from "react-native-toast-notifications";
import LoadingScreen from "../../screens/loading-screen";
import { getItemLocalStorage } from "../../utils/general-local-storage";

const ProfessionalsStack = createNativeStackNavigator();

const steps = [
  { name: 'Step1', component: Step1 },
  { name: 'Step2', component: Step2 },
  { name: 'Step3', component: Step3 },
];

export const ProfessionalsStackNavigator = ({navigation}) => {

    const [currentStep, setCurrentStep] = useState(0);
    const scrollViewRef = useRef(null);
    
    const [isLoading, setIsLoading] = useState(false);
    
    const toast = useToast();


    //const [stepData, setStepData] = useState({});
    
    const [stepData, setStepData] = useState({
        step1: {
            idPatient: '',
            course: '',
            previousPsychiatricTreatment: '',
        },
        step2: {
            family12: '',
            family13: '',
            jobSituationFather: '',
            jobSituationMother: '',
            academicLevelFather: '',
            academicLevelMother: '',
            family1: '',
            family2: '',
            family3: '',
        },
        step3: {
            family4: '',
            family5: '',
            family6: '',
            family7: '',
            family8: '',
            family9: '',
            family10: '',
            family11: '',
            family14: '',
        },
    });

    const [validations, setValidations] = useState({
        step1: {
            idPatient: false,
            course: false,
            previousPsychiatricTreatment: false,
        },
        step2: {
            family12: false,
            family13: false,
            jobSituationFather: false,
            jobSituationMother: false,
            academicLevelFather: false,
            academicLevelMother: false,
            family1: false,
            family2: false,
            family3: false,
        },
        step3: {
            family4: false,
            family5: false,
            family6: false,
            family7: false,
            family8: false,
            family9: false,
            family10: false,
            family11: false,
            family14: false,
        },
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
        const { idPatient, course, previousPsychiatricTreatment } = stepData.step1;
        const { family12, family13, jobSituationFather, jobSituationMother, 
            academicLevelFather, academicLevelMother, family1, family2, family3 } = stepData.step2;
        const { family4, family5, family6, family7, 
            family8, family9, family10, family11, family14 } = stepData.step3;

        const newValidationsStep1 = {
            idPatient: idPatient === '',
            course: course === '',
            previousPsychiatricTreatment: previousPsychiatricTreatment === '',
        };
        const newValidationsStep2 = {
            family12: family12 === '',
            family13: family13 === '',
            jobSituationFather: jobSituationFather === '',
            jobSituationMother: jobSituationMother === '',
            academicLevelFather: academicLevelFather === '',
            academicLevelMother: academicLevelMother === '',
            family1: family1 === '',
            family2: family2 === '',
            family3: family3 === '',
        };
        const newValidationsStep3 = {
            family4: family4 === '',
            family5: family5 === '',
            family6: family6 === '',
            family7: family7 === '',
            family8: family8 === '',
            family9: family9 === '',
            family10: family10 === '',
            family11: family11 === '',
            family14: family14 === '',
        };

        const newValidations = {
            step1: newValidationsStep1,
            step2: newValidationsStep2,
            step3: newValidationsStep3,
        }

        setValidations(newValidations);

        return newValidations;
    }

    const validateForm = () => {

        const newValidations = validateFormByStep();

        const { step1, step2, step3 } = newValidations;

        let step1Valid = (
            !step1.idPatient &&
            !step1.course &&
            !step1.previousPsychiatricTreatment
        );
        let step2Valid = (
            !step2.family12 &&
            !step2.family13 &&
            !step2.jobSituationFather &&
            !step2.jobSituationMother &&
            !step2.academicLevelFather &&
            !step2.academicLevelMother &&
            !step2.family1 &&
            !step2.family2 &&
            !step2.family3
        );
        let step3Valid = (
            !step3.family4 &&
            !step3.family5 &&
            !step3.family6 &&
            !step3.family7 &&
            !step3.family8 &&
            !step3.family9 &&
            !step3.family10 &&
            !step3.family11 &&
            !step3.family14
        );

        return {
            step1Valid: step1Valid,
            step2Valid: step2Valid, 
            step3Valid: step3Valid,       
        };

    }

    async function handleSubmit() {
        // Maneja el envío del formulario
        //const errors = validateStep(stepData);

        let { 
            step1Valid,
            step2Valid, 
            step3Valid
        } = validateForm();
        if (step1Valid &&
            step2Valid && 
            step3Valid) 
        {

            setIsLoading(true);
            let base64_stepData = btoa(JSON.stringify(stepData));
            console.log(base64_stepData);
            let data = {
                email: await getItemLocalStorage('email'),
                user_data_sivaria: base64_stepData
            };
            
            await axiosInstance.post("/sivaria/v1/expertSystem/predict", data)
            .then(async function (response) {
                console.log('Formulario enviado', stepData);
                
                let message = 'Cuestionario enviado correctamente.\nLe llegará una notificación con los resultados y se le enviará por correo, tanto a usted como a los padres.'
                toast.show('Cuestionario enviado correctamente',{type: 'success'});
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
            setIsLoading(false);
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
                {/*<YoungstersStack.Navigator screenOptions={ { headerShown:false}}>*/}
                    {/*
                        <YoungstersStack.Screen name={steps[currentStep].name} component={steps[currentStep].component} />
                    */}
                    {/*steps.map((step, index) => (
                        <YoungstersStack.Screen key={index} name={step.name}>
                            {() => <step.component stepData={stepData} setStepData={setStepData} />}
                        </YoungstersStack.Screen>
                    ))*/}
                {/*</YoungstersStack.Navigator>*/}
                <CurrentStepComponent stepData={stepData} setStepData={setStepData} validations={validations}/>
            </ScrollView>
            <View style={styles.navigationButtons}>
                {/*
                <Pressable onPress={prevStep} disabled={currentStep === 0} >
                    <Text>VOLVER</Text>
                </Pressable>
                <Pressable onPress={nextStep} disabled={currentStep === steps.length - 1}>
                    <Text>CONTINUAR</Text>    
                </Pressable>
                */}
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
      backgroundColor: '#6e3b6e'
    },


    stepText: {
        color: '#000',
        fontWeight: 'bold'
    },

    navigationButtons: {
      flexDirection: 'row',
      justifyContent: 'space-between',
      padding: 20
    },

    button: {
        padding: 10,
        backgroundColor: '#007bff',
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
  