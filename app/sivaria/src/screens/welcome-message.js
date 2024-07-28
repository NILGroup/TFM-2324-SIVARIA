import React from 'react';
import { StyleSheet, ScrollView, Text, View, Linking } from 'react-native';

const WelcomeMessage = () => {
  return (
    <ScrollView style={styles.container}>
      <Text style={styles.title}>Bienvenido a SIVARIA</Text>

      <View style={styles.section}>
        <Text style={styles.sectionText}>
          Estimado usuario, le damos la bienvenida a <Text style={styles.bold}>SIVARIA</Text>. En esta aplicación podrá realizar cuestionarios acerca de la salud mental. Dentro de la aplicación se encuentran 4 tipos de roles:
        </Text>
        <Text style={styles.listItem}>• Joven: de entre 12 y 21 años.</Text>
        <Text style={styles.listItem}>• Padre</Text>
        <Text style={styles.listItem}>• Madre</Text>
        <Text style={styles.listItem}>• Profesional</Text>
        <Text style={styles.sectionText}>
          Los roles de padre y madre son similares. La distinción es principalmente a la hora de almacenar los datos en bases de datos.
        </Text>
        <Text style={styles.sectionText}>
          Dichos cuestionarios estarán enfocados de distinta forma, dependiendo de si el usuario es un joven, familiar o profesional.
        </Text>
        <Text style={styles.sectionText}>
          Al rellenar los cuestionarios, estos se almacenarán en la aplicación y se procesarán para obtener una predicción basada en un Sistema Experto entrenado para dicho propósito.
        </Text>
        <Text style={styles.sectionText}>
          Este modelo otorgará una predicción sobre el posible desenlace del joven basado en las preguntas de los cuestionarios.
        </Text>
        <Text style={styles.sectionText}>
          Las respuestas de los cuestionarios y el resultado de las predicciones pueden ser monitorizados por los profesionales y los padres a través de un apartado exclusivo llamado Historial.
        </Text>
        <Text style={styles.sectionText}>
          En caso de duda, tiene a su disposición la página oficial de <Text style={styles.bold}>SIVARIA</Text> para <Text style={styles.link} onPress={() => Linking.openURL('https://blogs.uned.es/investigacioninfantojuvenil/sivaria-gestion-del-suicidio/')}>contactarles</Text>.
        </Text>
        <Text style={styles.sectionText}>
          Dicha página también contiene una versión extendida de los cuestionarios para los 3 tipos de usuarios, además de información extra acerca del proyecto.
        </Text>
        <Text style={styles.sectionText}>
          También proporciona una serie de guías para ayudar a los jóvenes y familiares de poder identificar y prevenir cualquier problema de salud mental.
        </Text>
      </View>
    </ScrollView>
  );
};

const styles = StyleSheet.create({
  container: {
    flex: 1,
    padding: 20,
    backgroundColor: '#fff',
  },
  title: {
    fontSize: 24,
    fontWeight: 'bold',
    marginBottom: 20,
    textAlign: 'center',
  },
  section: {
    marginBottom: 20,
  },
  sectionText: {
    fontSize: 16,
    marginBottom: 10,
  },
  listItem: {
    fontSize: 16,
    marginLeft: 20,
    marginBottom: 5,
  },
  bold: {
    fontWeight: 'bold',
  },
  link: {
    color: 'blue',
  },
});

export default WelcomeMessage;
