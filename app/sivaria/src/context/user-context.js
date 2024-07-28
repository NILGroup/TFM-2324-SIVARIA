// src/context/AuthContext.js
import { useRef, useState, createContext } from 'react';

// NOT USED (NOT NOW)
export const UserContext = createContext();

export const UserProvider = ({children}) => {

    const [userId, setUserId] = useState(0);
    const [firstName, setFirstName] = useState('');
    const [lastName, setLastName] = useState('');
    const [password, setPassword] = useState('');
    const [email, setEmail] = useState('');
    const [phoneNumber, setPhoneNumber] = useState('');
    const [rol, setRol] = useState('');
    const [rolSlug, setRolSlug] = useState('');
    const [emailParent1, setEmailParent1] = useState('');
    const [emailParent2, setEmailParent2] = useState('');

    const userIdRef = useRef(0);
    const firstNameRef = useRef('');
    const lastNameRef = useRef('');
    const passwordRef = useRef('');
    const emailRef = useRef('');
    const phoneNumberRef = useRef('');
    const rolRef = useRef('');
    const rolSlugRef = useRef('');
    const emailParent1Ref = useRef('');
    const emailParent2Ref = useRef('');

    userIdRef.current = userId;
    firstNameRef.current = firstName;
    lastNameRef.current = lastName;
    passwordRef.current = password;
    emailRef.current = email;
    phoneNumberRef.current = phoneNumber;
    rolRef.current = rol;
    rolSlugRef.current = rolSlug;
    emailParent1Ref.current = emailParent1;
    emailParent2Ref.current = emailParent2;

    const insertUserData = (data) => {
        //console.log(data);
        setUserId(data.id);
        setFirstName(data.first_name ?? '');
        setLastName(data.last_name?? '');
        setEmail(data.email ?? '');
        setPhoneNumber(data.phone ?? '');
        let rolDescription = '' ? data.rol === null : data.rol.description;
        setRol(rolDescription);
        let rolSlug = '' ? data.rol === null : data.rol.slug;
        setRolSlug(rolSlug);
        if(rolSlug === 'joven') {
            setEmailParent1(data.email_parent_1 ?? '');
            setEmailParent2(data.email_parent_2 ?? '');
        }
    };
    
    const removeUserData = () => {
        setUserId(0);
        setFirstName('');
        setLastName('');
        setPassword('');
        setEmail('');
        setPhoneNumber('');
        setRol('');
        setRolSlug('');
        setEmailParent1('');
        setEmailParent2('');

    };

    return (
        <UserContext.Provider value={{ 
            userId,
            firstName,
            lastName,
            password,
            email,
            phoneNumber,
            rol,
            rolSlug,
            emailParent1,
            emailParent2,
            insertUserData,
            removeUserData
        }}>
            { children }
        </UserContext.Provider>
    );
}