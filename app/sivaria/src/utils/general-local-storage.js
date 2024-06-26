import { Platform } from "react-native";
import { setItem, getItem, removeItem, clear, getAllKeys, getAllItems } from "./async-storage";

export const setItemLocalStorage = async (key, value) => {
    Platform.OS === 'web' ? localStorage.setItem(key, value) : await setItem(key, value);
};
  
export const getItemLocalStorage = async (key) => {
    const item = Platform.OS === 'web' ? localStorage.getItem(key) : await getItem(key);
    return item;
};

export const removeItemLocalStorage = async (key) => {
    Platform.OS === 'web' ? localStorage.removeItem(key) : await removeItem(key);
};
  
export const clearLocalStorage = async () => {
    Platform.OS === 'web' ? localStorage.clear() : await clear();
};

export const getAllKeysLocalStorage = async () => {
    if(Platform.OS === 'web') {
        const keys = [];
        for (i=0; i<localStorage.length; i++)  
        {  
            const key = localStorage.key(i); 
            keys.push(key); 
        } 
    }
    else {
        return await getAllKeys();
    }
    
};

export const getAllItemsLocalStorage = async () => {
    if(Platform.OS === 'web') {
        var items = {}, // Notice change here
        keys = Object.keys(localStorage),
        i = keys.length;

        while ( i-- ) {
            items[ keys[i] ] = localStorage.getItem( keys[i] );
        }

        return items;
    }
    else {
        return await getAllItems();
    }
};