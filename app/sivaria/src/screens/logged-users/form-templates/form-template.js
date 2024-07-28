import { Text } from "react-native";
import { YoungFormTemplate } from "./young-form-template/young-form-template";
import { FamilyFormTemplate } from "./family-form-template/family-form-template";
import { ProfessionalFormTemplate } from "./professional-form-template/professional-form-template";

export const FormTemplate = ({ isData, formData }) => {

    
    if(isData && formData.form_code === 'Y') {
        return (<YoungFormTemplate formData={formData} />);

    }
    if(isData && (formData.form_code === 'P' || formData.form_code === 'M')) {
        return (<FamilyFormTemplate formData={formData} />);

    }
    if(isData && formData.form_code === 'PR') {
       return (<ProfessionalFormTemplate formData={formData} />);

    }
    return (
        <>
            <Text>Sin información</Text>
        </>
    );
};

