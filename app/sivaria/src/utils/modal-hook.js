// hooks/useModal.js
import { useState } from 'react';

const useModal = () => {
    const [modalType, setModalType] = useState('');
    const [modalTitle, setModalTitle] = useState('');
    const [modalMessage, setModalMessage] = useState('');
    const [isVisible, setModalVisible] = useState(false);

    function setVisibleModal(modalType, title, message) {
        setModalType(modalType);
        setModalTitle(title);
        setModalMessage(message);
        setModalVisible(true);
    }

    return {
        modalType,
        modalTitle,
        modalMessage,
        isVisible,
        setModalVisible,
        setVisibleModal
    };
};

export default useModal;
