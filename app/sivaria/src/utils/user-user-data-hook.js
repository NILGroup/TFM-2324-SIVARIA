// hooks/useModal.js
import { useContext, useState } from 'react';
import { UserContext } from '../context/user-context';
import { AuthContext } from '../context/auth-context';
import { getItemLocalStorage } from './general-local-storage';

const useUserData = () => {
    const user = useContext(UserContext);
    const userAuth = useContext(AuthContext);

    async function updateUserStateVariables() {
        //console.log(AuthContext);
        //console.log(userAuth);
        if(userAuth.isAuthenticated) {
            let userIdLocal = await getItemLocalStorage('userId');
            let emailLocal = await getItemLocalStorage('email');
            let firstNameLocal = await getItemLocalStorage('firstName');
            let lastNameLocal = await getItemLocalStorage('lastName');
            let phoneNumberLocal = await getItemLocalStorage('phoneNumber');
            let rolLocal = await getItemLocalStorage('rol');
            let rolSlugLocal = await getItemLocalStorage('rolSlug');
            let emailParent1Local = await getItemLocalStorage('emailParent1');
            let emailParent2Local = await getItemLocalStorage('emailParent2');
            
            if(userIdLocal) {
                user.setUserId(userIdLocal);
            }
            if(emailLocal) {
                user.setEmail(emailLocal);
            }
            if(firstNameLocal) {
                user.setFirstName(firstNameLocal);
            }
            if(lastNameLocal) {
                user.setLastName(lastNameLocal);
            }
            if(phoneNumberLocal) {
                user.setPhoneNumber(phoneNumberLocal);
            }
            if(rolLocal) {
                user.setRol(rolLocal);
            }
            if(rolSlugLocal) {
                user.setRolSlug(rolSlugLocal);
            }
            if(emailParent1Local) {
                user.setEmailParent1(emailParent1Local);
            }
            if(emailParent2Local) {
                user.setEmailParent2(emailParent2Local);
            }
        }
    }

    async function removeUserStateVariables() {
        setUserId(0);
        setEmail('');
        setFirstName('');
        setLastName('');
        setPhoneNumber('');
        setRol('');
        setRolSlug('');
        setEmailParent1('');
        setEmailParent2('');
    }

    return {
        //modalType,
        //modalTitle,
        //modalMessage,
        //isVisible,
        //setModalVisible,
        updateUserStateVariables,
        removeUserStateVariables,
    };
};

export default useUserData;
