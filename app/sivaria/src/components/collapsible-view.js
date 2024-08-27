import React, { useState } from 'react';
import { View, Text, Pressable, FlatList, StyleSheet } from 'react-native';
import { AntDesign } from '@expo/vector-icons';

const AccordionItem = ({ item, onPress, expanded }) => {
  return (
    <View style={styles.itemContainer}>
      <Pressable onPress={onPress} style={styles.header}>
        <Text style={styles.headerText}>{item.title}</Text>
        <AntDesign
          name={expanded ? 'up' : 'down'}
          size={20}
          color="#fff"
        />
      </Pressable>
      {expanded && (
        <View style={styles.content}>
          <View style={styles.contentSection}>
            <Text style={styles.boldText}>Padre o figura parental 1:</Text>
            <Text style={styles.contentText}>{item.content.parent_1}</Text>
          </View>
          <View style={styles.contentSection}>
            <Text style={styles.boldText}>Madre o figura parental 2:</Text>
            <Text style={styles.contentText}>{item.content.parent_2}</Text>
          </View>
          <View style={styles.contentSection}>
            <Text style={styles.boldText}>Psicólogo responsable:</Text>
            <Text style={styles.contentText}>{item.content.responsible}</Text>
          </View>
        </View>
      )}
    </View>
  );
};

export const AccordionList = ({ data }) => {
  const [expandedItemId, setExpandedItemId] = useState(null);

  const handlePress = (id) => {
    setExpandedItemId(id === expandedItemId ? null : id);
  };

  return (
    <FlatList
      data={data}
      keyExtractor={(item) => item.id.toString()}
      renderItem={({ item }) => (
        <AccordionItem
          item={item}
          onPress={() => handlePress(item.id)}
          expanded={item.id === expandedItemId}
        />
      )}
    />
  );
};

const styles = StyleSheet.create({
    container: {
      flex: 1,
      paddingTop: 50,
    },
    itemContainer: {
      marginVertical: 5,
      marginHorizontal: 10,
      borderRadius: 8,
      backgroundColor: '#f1f1f1',
      overflow: 'hidden',
    },
    header: {
      flexDirection: 'row',
      justifyContent: 'space-between',
      alignItems: 'center',
      padding: 15,
      backgroundColor: '#006E51',
    },
    headerText: {
      color: '#fff',
      fontSize: 16,
    },
    content: {
      padding: 15,
      backgroundColor: '#fff',
    },
    contentSection: {
      marginBottom: 15,
    },
    contentText: {
      fontSize: 14,
    },
    boldText: {
      fontWeight: 'bold',
      marginBottom: 5,
    },
  });