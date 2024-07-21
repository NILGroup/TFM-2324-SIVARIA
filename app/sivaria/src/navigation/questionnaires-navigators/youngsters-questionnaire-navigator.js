import { useState, useRef, useEffect } from "react";
import { View, ScrollView, Pressable, StyleSheet, Text, Dimensions } from "react-native";
import { createNativeStackNavigator } from "@react-navigation/native-stack";
import { Step1, Step2, Step3, Step4, Step5,Step6,Step7,Step8,Step9,Step10, Step11, Step12 } from "../../screens/logged-users/forms/youngsters-multi-step-form/steps";
import axiosInstance from "../../utils/axios-config-web";
import { useToast } from "react-native-toast-notifications";
import LoadingScreen from "../../screens/loading-screen";
import { getItemLocalStorage } from "../../utils/general-local-storage";

const YoungstersStack = createNativeStackNavigator();

const steps = [
  { name: 'Step1', component: Step1 },
  { name: 'Step2', component: Step2 },
  { name: 'Step3', component: Step3 },
  { name: 'Step4', component: Step4 },
  { name: 'Step5', component: Step5 },
  { name: 'Step6', component: Step6 },
  { name: 'Step7', component: Step7 },
  { name: 'Step8', component: Step8 },
  { name: 'Step9', component: Step9 },
  { name: 'Step10', component: Step10 },
  { name: 'Step11', component: Step11 },
  { name: 'Step12', component: Step12 },
];

export const YoungstersStackNavigator = ({navigation}) => {

    const [currentStep, setCurrentStep] = useState(0);
    const scrollViewRef = useRef(null);
    
    const [isLoading, setIsLoading] = useState(false);
    
    const toast = useToast();


    //const [stepData, setStepData] = useState({});
    
    const [stepData, setStepData] = useState({
        step1: {
            course: '',
            age: '',
            gender: '',
            trans: '',
        },
        step2: {
            jobSituationFather: '', 
            jobSituationMother: '', 
            academicLevelFather: '', 
            academicLevelMother: '', 
            academicPerformance: '',
            previousPsychiatricTreatment: '',
            chronicDisease: '',
        },
        step3: {
            femaleSelfPerception: '', 
            maleSelfPerception: '',
            femaleOthersPerception: '',
            maleOthersPerception: '',
            weight: '',
            height: '',
            discriminationType: '',
        },
        step4: {
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
        },
        step5: {
            rrss1: '', 
            rrss2: '',
            rrss3: '',
            rrss4: '',
            rrss5: '',
            rrss6: '',
            rrss7: '',
        },
        step6: { 
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
        },
        step7: {
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
        },
        step8: {
            ati1:'',
            ati2:'',
            ati3:'',
            ati4:'',
            ati5:'',
            ati6:'',
            ate1:'',
            ate2:'',
            ate3:'',
            ate4:'',
            ate5:'',
            ate6:'',
            ate7:'',
            ate8:'',
            ate9:'',
            ate10:'',

        },
        step9: {
            ed1:'',
            ed2:'',
            ed3:'',
            ed4:'',
            ed5:'',
            ed6:'',
            ed7:'',
            ed8:'',
            ed9:'',
            ed10:'',
            ed11:'',
            ed12:'',
            ed13:'',
            ed14:'',
            ed15:'',
            ed16:'',
            er1:'',
            er2:'',
            er3:'',
            er4:'',
            er5:'',
            er6:'',
            er7:'',
            er8:'',
            er9:'',
            er10:'',
        },
        step10: {
            inq1:'',
            inq2:'',
            inq3:'',
            inq4:'',
            inq5:'',
            inq6:'',
            inq7:'',
            inq8:'',
            inq9:'',
            inq10:'',
            inq11:'',
            inq12:'',
            inq13:'',
            inq14:'',
            inq15:'',
        },
        step11: {
            sena19: '',
            sena23: '',
            sena69: '',
            sena99: '',
            sena103: '',
            sena111: '',
            sena112: '',
            sena115: '',
            sena117: '',
            sena129: '',
            sena137: '',
            sena139: '',
            sena141: '',
            sena146: '',    
            sena150: '',
            sena188: '',
            injury1:'',
            
        },
        step12: {
            family1: '',
            family2: '',
            family3: '',
            family4: '',
            family5: '',
            family6: '',
            family7: '',
            family8: '',
            /*
            fatherAge: '',
            motherAge: '',
            singleParentFamily: '',
            divorcedParents: '',
            psiquiatricTreatmentParent: '',
            addictionParent: '',
            conflictingRelationshipsChildParents: '',
            reconstructedFamily: '',
            */
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

    const validateForm = () => {
        const { step1, step2, 
            step3, step4, step5, 
            step6, step7, step8, 
            step9, step10, step11, step12 } = stepData;

        let step1Valid = (
            step1.age && 
            step1.course && 
            step1.gender && 
            step1.trans
        );
        let step2Valid = (
            step2.academicLevelFather &&
            step2.academicLevelMother &&
            step2.academicPerformance &&
            step2.chronicDisease &&
            step2.jobSituationFather &&
            step2.jobSituationMother &&
            step2.previousPsychiatricTreatment
        );
        let step3Valid = (
            step3.discriminationType &&
            step3.maleSelfPerception &&
            step3.femaleSelfPerception &&
            step3.maleOthersPerception &&
            step3.femaleOthersPerception &&
            step3.height &&
            step3.weight
        );
        let step4Valid = (
            step4.vb1 && 
            step4.vb2 &&
            step4.vb4 &&
            step4.ab1 &&
            step4.ab2 &&
            step4.ab4 &&
            step4.cybv1 &&
            step4.cybv2 &&
            step4.cybv3 &&
            step4.cybb1 &&
            step4.cybb2 &&
            step4.cybb3
        );
        let step5Valid = (
            step5.rrss1 && 
            step5.rrss2 && 
            step5.rrss3 && 
            step5.rrss4 && 
            step5.rrss5 && 
            step5.rrss6 && 
            step5.rrss7 
        );
        let step6Valid = (
            step6.mcad1 && 
            step6.mcad2 &&
            step6.mcad3 &&
            step6.mcad4 &&
            step6.mcad5 &&
            step6.mcad6 &&
            step6.mcad7 &&
            step6.mcad8 &&
            step6.mcad9 &&
            step6.mcad10 &&
            step6.mcad11 &&
            step6.mcad12
        );
        let step7Valid = (
            step7.cerqs1  && 
            step7.cerqs2  &&
            step7.cerqs3  &&
            step7.cerqs4  &&
            step7.cerqs5  &&
            step7.cerqs6  &&
            step7.cerqs7  &&
            step7.cerqs8  &&
            step7.cerqs9  &&
            step7.cerqs10 &&
            step7.cerqs11 &&
            step7.cerqs12 &&
            step7.cerqs13 &&
            step7.cerqs14 &&
            step7.cerqs15 &&
            step7.cerqs16 &&
            step7.cerqs17 &&
            step7.cerqs18
        );
        let step8Valid = (
            step8.ati1 &&
            step8.ati2 &&
            step8.ati3 &&
            step8.ati4 &&
            step8.ati5 &&
            step8.ati6 &&
            step8.ate1 &&
            step8.ate2 &&
            step8.ate3 &&
            step8.ate4 &&
            step8.ate5 &&
            step8.ate6 &&
            step8.ate7 &&
            step8.ate8 &&
            step8.ate9 &&
            step8.ate10 
        );
        let step9Valid = (
            step9.ed1 &&
            step9.ed2 &&
            step9.ed3 &&
            step9.ed4 &&
            step9.ed5 &&
            step9.ed6 &&
            step9.ed7 &&
            step9.ed8 &&
            step9.ed9 &&
            step9.ed10 &&
            step9.ed11 &&
            step9.ed12 &&
            step9.ed13 &&
            step9.ed14 &&
            step9.ed15 &&
            step9.ed16 &&
            step9.er1 &&
            step9.er2 &&
            step9.er3 &&
            step9.er4 &&
            step9.er5 &&
            step9.er6 &&
            step9.er7 &&
            step9.er8 &&
            step9.er9 &&
            step9.er10
        );
        let step10Valid = (
            step10.inq1 &&
            step10.inq2 &&
            step10.inq3 &&
            step10.inq4 &&
            step10.inq5 &&
            step10.inq6 &&
            step10.inq7 &&
            step10.inq8 &&
            step10.inq9 &&
            step10.inq10 &&
            step10.inq11 &&
            step10.inq12 &&
            step10.inq13 &&
            step10.inq14 &&
            step10.inq15
        );
        let step11Valid = (
            step11.sena19 &&
            step11.sena23 &&
            step11.sena69 &&
            step11.sena99 &&
            step11.sena103 &&
            step11.sena111 &&
            step11.sena112 &&
            step11.sena115 &&
            step11.sena117 &&
            step11.sena129 &&
            step11.sena137 &&
            step11.sena139 &&
            step11.sena141 &&
            step11.sena146 &&    
            step11.sena150 &&
            step11.sena188 &&
            step11.injury1
        );
        let step12Valid = (
            step12.family1 &&
            step12.family2 &&
            step12.family3 &&
            step12.family4 &&
            step12.family5 &&
            step12.family6 &&
            step12.family7 &&
            step12.family8
        );

        return {
            step1Valid: step1Valid,
            step2Valid: step2Valid, 
            step3Valid: step3Valid, 
            step4Valid: step4Valid, 
            step5Valid: step5Valid, 
            step6Valid: step6Valid, 
            step7Valid: step7Valid, 
            step8Valid: step8Valid, 
            step9Valid: step9Valid, 
            step10Valid: step10Valid,
            step11Valid: step11Valid, 
            step12Valid: step12Valid,           
        };
        /*
        return (step1Valid &&
            step2Valid && 
            step3Valid && 
            step4Valid && 
            step5Valid && 
            step6Valid && 
            step7Valid && 
            step8Valid && 
            step9Valid && 
            step10Valid && 
            step11Valid && 
            step12Valid
        );*/

    }

    async function handleSubmit() {
        // Maneja el envío del formulario
        //const errors = validateStep(stepData);

        let { 
            step1Valid,
            step2Valid, 
            step3Valid, 
            step4Valid, 
            step5Valid, 
            step6Valid, 
            step7Valid, 
            step8Valid, 
            step9Valid, 
            step10Valid, 
            step11Valid, 
            step12Valid
        } = validateForm();
        if (step1Valid &&
            step2Valid && 
            step3Valid && 
            step4Valid && 
            step5Valid && 
            step6Valid && 
            step7Valid && 
            step8Valid && 
            step9Valid && 
            step10Valid && 
            step11Valid && 
            step12Valid) 
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
                toast.show('Cuestionario enviado correctamente',{type: 'success'});
                navigation.navigate('Dashboard');
            })
            .catch(function (error) {
                toast.show('Error en el envío y procesamiento del cuestionario. ' + error.response.data.data,{type: 'danger'});
            });
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
            if(!step4Valid) {
                message += 'Página 4\n';
            }
            if(!step5Valid) {
                message += 'Página 5\n';
            }
            if(!step6Valid) {
                message += 'Página 6\n';
            }
            if(!step7Valid) {
                message += 'Página 7\n';
            }
            if(!step8Valid) {
                message += 'Página 8\n';
            }
            if(!step9Valid) {
                message += 'Página 9\n';
            }
            if(!step10Valid) {
                message += 'Página 10\n';
            }
            if(!step11Valid) {
                message += 'Página 11\n';
            }
            if(!step12Valid) {
                message += 'Página 12';
            }

            toast.show(
                message,
                {
                    type: 'danger'
                }
            );
            //console.log('Hay campos vacíos en el formulario. Por favor, vuelve a revisarlo.');
        }
        /*
        setIsLoading(true);
            email = await getItemLocalStorage('email');
            let data = {};
            if (firstName) {
                data['first_name'] = firstName;
            }
            if (lastName) {
                data['last_name'] = lastName;
            }
            if (phoneNumber) {
                data['phone'] = phoneNumber;
            }
            //console.log(data);
            await axiosInstance.post("/sivaria/v1/user/email/" + email, data)
            .then(async function (response) {
                //console.log(response);
                //console.log('Cuenta eliminada correctamente');
                //let rolDescription = (userData.rol) ? userData.rol.description : null;
                //await setItemLocalStorage('rol', rolDescription);  
                //let rolSlug = (userData.rol) ? userData.rol.slug : null;
                //await setItemLocalStorage('rolSlug', rolSlug); 
                //if(rolSlug === 'joven') {
                    //await setItemLocalStorage('emailParent1', userData.email_parent_1); 
                    //await setItemLocalStorage('emailParent2', userData.email_parent_2); 
                //}
            };
        */
       
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
                <CurrentStepComponent stepData={stepData} setStepData={setStepData} />
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
                            <Text style={styles.buttonText}>SUBMIT</Text>
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
  