import React from 'react';
import { StyleSheet, ScrollView, Text, View } from 'react-native';

const PrivacyPolicy = () => {
  return (
    <ScrollView style={styles.container}>
      <Text style={styles.title}>Política de Privacidad</Text>

      <View style={styles.section}>
        <Text style={styles.sectionTitle}>Introducción</Text>
        <Text style={styles.sectionText}>
          Esta política de privacidad describe cómo la aplicación móvil y web de la UNED (Universidad Nacional de Educación a Distancia) recopila, utiliza y protege la información personal de los usuarios. Esta aplicación está diseñada para evaluar la salud mental de jóvenes entre 12 y 21 años en España. La UNED es responsable del tratamiento de los datos personales.
        </Text>
      </View>

      <View style={styles.section}>
        <Text style={styles.sectionTitle}>Información Recopilada</Text>
        <Text style={styles.sectionText}>
          Para poder utilizar nuestra aplicación, recopilamos la siguiente información:
        </Text>
        <Text style={styles.listItem}>• Nombres y Apellidos</Text>
        <Text style={styles.listItem}>• Email</Text>
        <Text style={styles.listItem}>• Número de teléfono del usuario</Text>
        <Text style={styles.listItem}>• Fecha de nacimiento</Text>
        <Text style={styles.listItem}>• Email de los padres y del responsable (para jóvenes de entre 12 y 21 años)</Text>
        <Text style={styles.listItem}>• Email del hijo/a (en caso de que el usuario sea un padre o una madre)</Text>
        <Text style={styles.sectionText}>
          Además, se recopila información sensible a través de cuestionarios realizados por jóvenes, familiares y profesionales, incluyendo:
        </Text>
        <Text style={styles.listItem}>• Información sobre la salud mental</Text>
        <Text style={styles.listItem}>• Orientación sexual</Text>
        <Text style={styles.listItem}>• Otros datos identificativos</Text>
      </View>

      <View style={styles.section}>
        <Text style={styles.sectionTitle}>Finalidad del Tratamiento</Text>
        <Text style={styles.sectionText}>
          Los datos personales se recopilan y tratan con fines de investigación científica sobre la salud mental de los jóvenes. Estos datos son esenciales para mejorar la comprensión y el apoyo en este campo.
        </Text>
      </View>

      <View style={styles.section}>
        <Text style={styles.sectionTitle}>Duración del Tratamiento</Text>
        <Text style={styles.sectionText}>
          • Los datos personales serán conservados durante 10 años para fines de investigación.
        </Text>
        <Text style={styles.sectionText}>
          • Cualquier documento generado a partir de estos datos será eliminado después de 3 años.
        </Text>
      </View>

      <View style={styles.section}>
        <Text style={styles.sectionTitle}>Protección de Datos</Text>
        <Text style={styles.sectionText}>
          La UNED se compromete a proteger la información personal de los usuarios y a cumplir con la normativa vigente de protección de datos personales en España. Implementamos medidas técnicas y organizativas adecuadas para garantizar la seguridad de los datos.
        </Text>
      </View>

      <View style={styles.section}>
        <Text style={styles.sectionTitle}>Derechos de los Usuarios</Text>
        <Text style={styles.sectionText}>
          Los usuarios tienen derecho a acceder, rectificar y suprimir sus datos personales, así como otros derechos, según lo establecido en la normativa vigente. Para ejercer estos derechos, pueden contactarnos en:
        </Text>
        <Text style={styles.listItem}>• Email: privacidad@uned.es</Text>
        <Text style={styles.listItem}>• Dirección: Calle Juan del Rosal, 14, 28040 Madrid, España</Text>
      </View>

      <View style={styles.section}>
        <Text style={styles.sectionTitle}>Contacto</Text>
        <Text style={styles.sectionText}>
          Si tiene alguna pregunta o inquietud sobre esta política de privacidad o sobre cómo manejamos la información personal, no dude en ponerse en contacto con nosotros.
        </Text>
      </View>

      <View style={styles.section}>
        <Text style={styles.sectionText}>UNED</Text>
        <Text style={styles.sectionText}>Universidad Nacional de Educación a Distancia</Text>
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
  sectionTitle: {
    fontSize: 18,
    fontWeight: 'bold',
    marginBottom: 10,
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
});

export default PrivacyPolicy;
