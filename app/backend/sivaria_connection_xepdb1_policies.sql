/* Creación de las políticas de enmascaramiento */
BEGIN

    DBMS_REDACT.ADD_POLICY(
        object_schema => 'SIVARIA_BACKEND',
        object_name => 'AUTHTOKEN_TOKEN',
        policy_name => 'AUTHTOKEN_TOKEN_POLICY',
        expression => 'SYS_CONTEXT(''USERENV'', ''SESSION_USER'') != ''SYSTEM'' and SYS_CONTEXT(''USERENV'', ''SESSION_USER'') != ''SIVARIA_BACKEND'''
    );
    
    /* User tables */
    DBMS_REDACT.ADD_POLICY(
        object_schema => 'SIVARIA_BACKEND',
        object_name => 'SIVARIA_APPUSER',
        policy_name => 'SIVARIA_APPUSER_POLICY',
        expression => 'SYS_CONTEXT(''USERENV'', ''SESSION_USER'') != ''SYSTEM'' and SYS_CONTEXT(''USERENV'', ''SESSION_USER'') != ''SIVARIA_BACKEND'''
    );
    
    DBMS_REDACT.ADD_POLICY(
        object_schema => 'SIVARIA_BACKEND',
        object_name => 'SIVARIA_USERHASPARENT',
        policy_name => 'SIVARIA_USERHASPARENT_POLICY',
        expression => 'SYS_CONTEXT(''USERENV'', ''SESSION_USER'') != ''SYSTEM'' and SYS_CONTEXT(''USERENV'', ''SESSION_USER'') != ''SIVARIA_BACKEND'''
    );
    
    /* Questionnaires tables */
    
    DBMS_REDACT.ADD_POLICY (
        object_schema           => 'SIVARIA_BACKEND',
        object_name             => 'SIVARIA_YOUNGFORM',
        policy_name             => 'SIVARIA_YOUNGFORM_POLICY',
        expression => 'SYS_CONTEXT(''USERENV'', ''SESSION_USER'') != ''SYSTEM'' and SYS_CONTEXT(''USERENV'', ''SESSION_USER'') != ''SIVARIA_BACKEND'''
    );
    
    DBMS_REDACT.ADD_POLICY (
        object_schema           => 'SIVARIA_BACKEND',
        object_name             => 'SIVARIA_FAMILYFORM',
        policy_name             => 'SIVARIA_FAMILYFORM_POLICY',
        expression => 'SYS_CONTEXT(''USERENV'', ''SESSION_USER'') != ''SYSTEM'' and SYS_CONTEXT(''USERENV'', ''SESSION_USER'') != ''SIVARIA_BACKEND'''
    );
    
    DBMS_REDACT.ADD_POLICY (
        object_schema           => 'SIVARIA_BACKEND',
        object_name             => 'SIVARIA_PROFESSIONALFORM',
        policy_name             => 'SIVARIA_PROFESSIONALFORM_POLICY',
        expression => 'SYS_CONTEXT(''USERENV'', ''SESSION_USER'') != ''SYSTEM'' and SYS_CONTEXT(''USERENV'', ''SESSION_USER'') != ''SIVARIA_BACKEND'''
    );
    
    /* Subform questionnaires */
  
    DBMS_REDACT.ADD_POLICY (
        object_schema           => 'SIVARIA_BACKEND',
        object_name             => 'SIVARIA_SOCIALDATAFORM',
        policy_name             => 'SIVARIA_SOCIALDATAFORM_POLICY',
        expression              => 'SYS_CONTEXT(''USERENV'', ''SESSION_USER'') != ''SYSTEM'' and SYS_CONTEXT(''USERENV'', ''SESSION_USER'') != ''SIVARIA_BACKEND'''
    );
    
    DBMS_REDACT.ADD_POLICY (
        object_schema           => 'SIVARIA_BACKEND',
        object_name             => 'SIVARIA_FAMILYSUBFORM',
        policy_name             => 'SIVARIA_FAMILYSUBFORM_POLICY',
        expression              => 'SYS_CONTEXT(''USERENV'', ''SESSION_USER'') != ''SYSTEM'' and SYS_CONTEXT(''USERENV'', ''SESSION_USER'') != ''SIVARIA_BACKEND'''
    );
    
    DBMS_REDACT.ADD_POLICY (
        object_schema           => 'SIVARIA_BACKEND',
        object_name             => 'SIVARIA_INJURYFORM',
        policy_name             => 'SIVARIA_INJURYFORM_POLICY',
        expression              => 'SYS_CONTEXT(''USERENV'', ''SESSION_USER'') != ''SYSTEM'' and SYS_CONTEXT(''USERENV'', ''SESSION_USER'') != ''SIVARIA_BACKEND'''
    );
    
    DBMS_REDACT.ADD_POLICY (
        object_schema           => 'SIVARIA_BACKEND',
        object_name             => 'SIVARIA_ATEFORM',
        policy_name             => 'SIVARIA_ATEFORM_POLICY',
        expression              => 'SYS_CONTEXT(''USERENV'', ''SESSION_USER'') != ''SYSTEM'' and SYS_CONTEXT(''USERENV'', ''SESSION_USER'') != ''SIVARIA_BACKEND'''
    );
    
    DBMS_REDACT.ADD_POLICY (
        object_schema           => 'SIVARIA_BACKEND',
        object_name             => 'SIVARIA_ATIFORM',
        policy_name             => 'SIVARIA_ATIFORM_POLICY',
        expression              => 'SYS_CONTEXT(''USERENV'', ''SESSION_USER'') != ''SYSTEM'' and SYS_CONTEXT(''USERENV'', ''SESSION_USER'') != ''SIVARIA_BACKEND'''
    );
    
    DBMS_REDACT.ADD_POLICY (
        object_schema           => 'SIVARIA_BACKEND',
        object_name             => 'SIVARIA_CERQSFORM',
        policy_name             => 'SIVARIA_CERQSFORM_POLICY',
        expression              => 'SYS_CONTEXT(''USERENV'', ''SESSION_USER'') != ''SYSTEM'' and SYS_CONTEXT(''USERENV'', ''SESSION_USER'') != ''SIVARIA_BACKEND'''
    );
    
    DBMS_REDACT.ADD_POLICY (
        object_schema           => 'SIVARIA_BACKEND',
        object_name             => 'SIVARIA_EBIPQECIPQFORM',
        policy_name             => 'SIVARIA_EBIPQECIPQFORM_POLICY',
        expression              => 'SYS_CONTEXT(''USERENV'', ''SESSION_USER'') != ''SYSTEM'' and SYS_CONTEXT(''USERENV'', ''SESSION_USER'') != ''SIVARIA_BACKEND'''
    );
    
    DBMS_REDACT.ADD_POLICY (
        object_schema           => 'SIVARIA_BACKEND',
        object_name             => 'SIVARIA_EDFORM',
        policy_name             => 'SIVARIA_EDFORM_POLICY',
        expression              => 'SYS_CONTEXT(''USERENV'', ''SESSION_USER'') != ''SYSTEM'' and SYS_CONTEXT(''USERENV'', ''SESSION_USER'') != ''SIVARIA_BACKEND'''
    );
    
    DBMS_REDACT.ADD_POLICY (
        object_schema           => 'SIVARIA_BACKEND',
        object_name             => 'SIVARIA_ERFORM',
        policy_name             => 'SIVARIA_ERFORM_POLICY',
        expression              => 'SYS_CONTEXT(''USERENV'', ''SESSION_USER'') != ''SYSTEM'' and SYS_CONTEXT(''USERENV'', ''SESSION_USER'') != ''SIVARIA_BACKEND'''
    );
    
    DBMS_REDACT.ADD_POLICY (
        object_schema           => 'SIVARIA_BACKEND',
        object_name             => 'SIVARIA_INQFORM',
        policy_name             => 'SIVARIA_INQFORM_POLICY',
        expression              => 'SYS_CONTEXT(''USERENV'', ''SESSION_USER'') != ''SYSTEM'' and SYS_CONTEXT(''USERENV'', ''SESSION_USER'') != ''SIVARIA_BACKEND'''
    );
    
    DBMS_REDACT.ADD_POLICY (
        object_schema           => 'SIVARIA_BACKEND',
        object_name             => 'SIVARIA_MULTICAGECAD4FORM',
        policy_name             => 'SIVARIA_MULTICAGECAD4FORM_POLICY',
        expression              => 'SYS_CONTEXT(''USERENV'', ''SESSION_USER'') != ''SYSTEM'' and SYS_CONTEXT(''USERENV'', ''SESSION_USER'') != ''SIVARIA_BACKEND'''
    );
    
    DBMS_REDACT.ADD_POLICY (
        object_schema           => 'SIVARIA_BACKEND',
        object_name             => 'SIVARIA_PARQFORM',
        policy_name             => 'SIVARIA_PARQFORM_POLICY',
        expression              => 'SYS_CONTEXT(''USERENV'', ''SESSION_USER'') != ''SYSTEM'' and SYS_CONTEXT(''USERENV'', ''SESSION_USER'') != ''SIVARIA_BACKEND'''
    );
    
    DBMS_REDACT.ADD_POLICY (
        object_schema           => 'SIVARIA_BACKEND',
        object_name             => 'SIVARIA_RRSSFORM',
        policy_name             => 'SIVARIA_RRSSFORM_POLICY',
        expression              => 'SYS_CONTEXT(''USERENV'', ''SESSION_USER'') != ''SYSTEM'' and SYS_CONTEXT(''USERENV'', ''SESSION_USER'') != ''SIVARIA_BACKEND'''
    );
    
    DBMS_REDACT.ADD_POLICY (
        object_schema           => 'SIVARIA_BACKEND',
        object_name             => 'SIVARIA_SENAFAMILYFORM',
        policy_name             => 'SIVARIA_SENAFAMILYFORM_POLICY',
        expression              => 'SYS_CONTEXT(''USERENV'', ''SESSION_USER'') != ''SYSTEM'' and SYS_CONTEXT(''USERENV'', ''SESSION_USER'') != ''SIVARIA_BACKEND'''
    );
    
    DBMS_REDACT.ADD_POLICY (
        object_schema           => 'SIVARIA_BACKEND',
        object_name             => 'SIVARIA_SENAFORM',
        policy_name             => 'SIVARIA_SENAFORM_POLICY',
        expression              => 'SYS_CONTEXT(''USERENV'', ''SESSION_USER'') != ''SYSTEM'' and SYS_CONTEXT(''USERENV'', ''SESSION_USER'') != ''SIVARIA_BACKEND'''
    );
    
END;
/

/* Modificación de las políticas para añadir el enmascaramiento de las columnas seleccionadas */
BEGIN

    DBMS_REDACT.ALTER_POLICY (
        object_schema           => 'SIVARIA_BACKEND',
        object_name             => 'AUTHTOKEN_TOKEN',
        policy_name             => 'AUTHTOKEN_TOKEN_POLICY',
        function_type           => DBMS_REDACT.FULL,
        column_name             => 'USER_ID'
    );
    
    DBMS_REDACT.ALTER_POLICY (
        object_schema           => 'SIVARIA_BACKEND',
        object_name             => 'AUTHTOKEN_TOKEN',
        policy_name             => 'AUTHTOKEN_TOKEN_POLICY',
        function_type           => DBMS_REDACT.FULL,
        action                  => DBMS_REDACT.ADD_COLUMN,
        column_name             => 'CREATED'
    );
    
    DBMS_REDACT.ALTER_POLICY (
        object_schema           => 'SIVARIA_BACKEND',
        object_name             => 'AUTHTOKEN_TOKEN',
        policy_name             => 'AUTHTOKEN_TOKEN_POLICY',
        function_type           => DBMS_REDACT.RANDOM,
        action                  => DBMS_REDACT.ADD_COLUMN,
        column_name             => 'KEY'
    );
    
    /* SIVARIA_APPUSER table */
    DBMS_REDACT.ALTER_POLICY (
        object_schema           => 'SIVARIA_BACKEND',
        object_name             => 'SIVARIA_APPUSER',
        policy_name             => 'SIVARIA_APPUSER_POLICY',
        function_type           => DBMS_REDACT.REGEXP,
        action                  => DBMS_REDACT.ADD_COLUMN,
        regexp_pattern          => DBMS_REDACT.RE_PATTERN_EMAIL_ADDRESS,
        regexp_replace_string   => DBMS_REDACT.RE_REDACT_EMAIL_ENTIRE,            
        column_name             => 'EMAIL'
    );
    DBMS_REDACT.ALTER_POLICY (
        object_schema           => 'SIVARIA_BACKEND',
        object_name             => 'SIVARIA_APPUSER',
        policy_name             => 'SIVARIA_APPUSER_POLICY',
        function_type           => DBMS_REDACT.FULL,
        column_name             => 'PHONE'
    );
    DBMS_REDACT.ALTER_POLICY (
        object_schema           => 'SIVARIA_BACKEND',
        object_name             => 'SIVARIA_APPUSER',
        policy_name             => 'SIVARIA_APPUSER_POLICY',
        function_type           => DBMS_REDACT.FULL,
        column_name             => 'ROL_ID'
    );
    DBMS_REDACT.ALTER_POLICY (
        object_schema           => 'SIVARIA_BACKEND',
        object_name             => 'SIVARIA_APPUSER',
        policy_name             => 'SIVARIA_APPUSER_POLICY',
        function_type           => DBMS_REDACT.RANDOM,
        action                  => DBMS_REDACT.ADD_COLUMN,
        column_name             => 'USERNAME'
    );
    
    DBMS_REDACT.ALTER_POLICY (
        object_schema           => 'SIVARIA_BACKEND',
        object_name             => 'SIVARIA_APPUSER',
        policy_name             => 'SIVARIA_APPUSER_POLICY',
        function_type           => DBMS_REDACT.RANDOM,
        action                  => DBMS_REDACT.ADD_COLUMN,
        column_name             => 'FIRST_NAME'
    );
    
    DBMS_REDACT.ALTER_POLICY (
        object_schema           => 'SIVARIA_BACKEND',
        object_name             => 'SIVARIA_APPUSER',
        policy_name             => 'SIVARIA_APPUSER_POLICY',
        function_type           => DBMS_REDACT.RANDOM,
        action                  => DBMS_REDACT.ADD_COLUMN,
        column_name             => 'LAST_NAME'
    );
    
    DBMS_REDACT.ALTER_POLICY (
        object_schema           => 'SIVARIA_BACKEND',
        object_name             => 'SIVARIA_APPUSER',
        policy_name             => 'SIVARIA_APPUSER_POLICY',
        function_type           => DBMS_REDACT.RANDOM,
        action                  => DBMS_REDACT.ADD_COLUMN,
        column_name             => 'EXPO_TOKEN'
    );
    
    DBMS_REDACT.ALTER_POLICY (
        object_schema           => 'SIVARIA_BACKEND',
        object_name             => 'SIVARIA_APPUSER',
        policy_name             => 'SIVARIA_APPUSER_POLICY',
        function_type           => DBMS_REDACT.RANDOM,
        expression              => '1=1',
        column_name             => 'CODE'
    );

    DBMS_REDACT.ALTER_POLICY (
        object_schema           => 'SIVARIA_BACKEND',
        object_name             => 'SIVARIA_APPUSER',
        policy_name             => 'SIVARIA_APPUSER_POLICY',
        function_type           => DBMS_REDACT.FULL,
        action                  => DBMS_REDACT.ADD_COLUMN,
        column_name             => 'BIRTH_DATE'
    );
    
    DBMS_REDACT.ALTER_POLICY (
        object_schema           => 'SIVARIA_BACKEND',
        object_name             => 'SIVARIA_APPUSER',
        policy_name             => 'SIVARIA_APPUSER_POLICY',
        function_type           => DBMS_REDACT.FULL,
        action                  => DBMS_REDACT.ADD_COLUMN,
        column_name             => 'DATE_JOINED'
    );
    
    /* SIVARIA_USERHASPARENT table */
    
    DBMS_REDACT.ALTER_POLICY (
        object_schema           => 'SIVARIA_BACKEND',
        object_name             => 'SIVARIA_USERHASPARENT',
        policy_name             => 'SIVARIA_USERHASPARENT_POLICY',
        function_type           => DBMS_REDACT.REGEXP,
        action                  => DBMS_REDACT.ADD_COLUMN,
        regexp_pattern          => DBMS_REDACT.RE_PATTERN_EMAIL_ADDRESS,
        regexp_replace_string   => DBMS_REDACT.RE_REDACT_EMAIL_ENTIRE,            
        column_name             => 'EMAIL_PARENT_1'
    );
    
    DBMS_REDACT.ALTER_POLICY (
        object_schema           => 'SIVARIA_BACKEND',
        object_name             => 'SIVARIA_USERHASPARENT',
        policy_name             => 'SIVARIA_USERHASPARENT_POLICY',
        function_type           => DBMS_REDACT.REGEXP,
        action                  => DBMS_REDACT.ADD_COLUMN,
        regexp_pattern          => DBMS_REDACT.RE_PATTERN_EMAIL_ADDRESS,
        regexp_replace_string   => DBMS_REDACT.RE_REDACT_EMAIL_ENTIRE,            
        column_name             => 'EMAIL_PARENT_2'
    );
    
    DBMS_REDACT.ALTER_POLICY (
        object_schema           => 'SIVARIA_BACKEND',
        object_name             => 'SIVARIA_USERHASPARENT',
        policy_name             => 'SIVARIA_USERHASPARENT_POLICY',
        function_type           => DBMS_REDACT.FULL,
        column_name             => 'RESPONSIBLE_ID'
    );
    
    DBMS_REDACT.ALTER_POLICY (
        object_schema           => 'SIVARIA_BACKEND',
        object_name             => 'SIVARIA_USERHASPARENT',
        policy_name             => 'SIVARIA_USERHASPARENT_POLICY',
        function_type           => DBMS_REDACT.FULL,
        column_name             => 'CHILD_ID'
    );
    
    /* YOUNG FORM */
    
    DBMS_REDACT.ALTER_POLICY (
        object_schema           => 'SIVARIA_BACKEND',
        object_name             => 'SIVARIA_YOUNGFORM',
        policy_name             => 'SIVARIA_YOUNGFORM_POLICY',
        function_type           => DBMS_REDACT.FULL,
        column_name             => 'ATE_ID'
    );
    
    DBMS_REDACT.ALTER_POLICY (
        object_schema           => 'SIVARIA_BACKEND',
        object_name             => 'SIVARIA_YOUNGFORM',
        policy_name             => 'SIVARIA_YOUNGFORM_POLICY',
        function_type           => DBMS_REDACT.FULL,
        column_name             => 'ATI_ID'
    );
    
    DBMS_REDACT.ALTER_POLICY (
        object_schema           => 'SIVARIA_BACKEND',
        object_name             => 'SIVARIA_YOUNGFORM',
        policy_name             => 'SIVARIA_YOUNGFORM_POLICY',
        function_type           => DBMS_REDACT.FULL,
        column_name             => 'CERQS_ID'
    );
    
    DBMS_REDACT.ALTER_POLICY (
        object_schema           => 'SIVARIA_BACKEND',
        object_name             => 'SIVARIA_YOUNGFORM',
        policy_name             => 'SIVARIA_YOUNGFORM_POLICY',
        function_type           => DBMS_REDACT.FULL,
        column_name             => 'EBIPQ_ECIPQ_ID'
    );
    
    DBMS_REDACT.ALTER_POLICY (
        object_schema           => 'SIVARIA_BACKEND',
        object_name             => 'SIVARIA_YOUNGFORM',
        policy_name             => 'SIVARIA_YOUNGFORM_POLICY',
        function_type           => DBMS_REDACT.FULL,
        column_name             => 'ED_ID'
    );
    
    DBMS_REDACT.ALTER_POLICY (
        object_schema           => 'SIVARIA_BACKEND',
        object_name             => 'SIVARIA_YOUNGFORM',
        policy_name             => 'SIVARIA_YOUNGFORM_POLICY',
        function_type           => DBMS_REDACT.FULL,
        column_name             => 'ER_ID'
    );
    
    DBMS_REDACT.ALTER_POLICY (
        object_schema           => 'SIVARIA_BACKEND',
        object_name             => 'SIVARIA_YOUNGFORM',
        policy_name             => 'SIVARIA_YOUNGFORM_POLICY',
        function_type           => DBMS_REDACT.FULL,
        column_name             => 'FAMILY_ID'
    );
    
    DBMS_REDACT.ALTER_POLICY (
        object_schema           => 'SIVARIA_BACKEND',
        object_name             => 'SIVARIA_YOUNGFORM',
        policy_name             => 'SIVARIA_YOUNGFORM_POLICY',
        function_type           => DBMS_REDACT.FULL,
        column_name             => 'INJURY_ID'
    );
    
    DBMS_REDACT.ALTER_POLICY (
        object_schema           => 'SIVARIA_BACKEND',
        object_name             => 'SIVARIA_YOUNGFORM',
        policy_name             => 'SIVARIA_YOUNGFORM_POLICY',
        function_type           => DBMS_REDACT.FULL,
        column_name             => 'INQ_ID'
    );
    
    DBMS_REDACT.ALTER_POLICY (
        object_schema           => 'SIVARIA_BACKEND',
        object_name             => 'SIVARIA_YOUNGFORM',
        policy_name             => 'SIVARIA_YOUNGFORM_POLICY',
        function_type           => DBMS_REDACT.FULL,
        column_name             => 'MCAD_ID'
    );
    
    DBMS_REDACT.ALTER_POLICY (
        object_schema           => 'SIVARIA_BACKEND',
        object_name             => 'SIVARIA_YOUNGFORM',
        policy_name             => 'SIVARIA_YOUNGFORM_POLICY',
        function_type           => DBMS_REDACT.FULL,
        column_name             => 'PARTICIPANT_YOUNG_FORM_ID'
    );
    
    DBMS_REDACT.ALTER_POLICY (
        object_schema           => 'SIVARIA_BACKEND',
        object_name             => 'SIVARIA_YOUNGFORM',
        policy_name             => 'SIVARIA_YOUNGFORM_POLICY',
        function_type           => DBMS_REDACT.FULL,
        column_name             => 'RRSS_ID'
    );
    
    DBMS_REDACT.ALTER_POLICY (
        object_schema           => 'SIVARIA_BACKEND',
        object_name             => 'SIVARIA_YOUNGFORM',
        policy_name             => 'SIVARIA_YOUNGFORM_POLICY',
        function_type           => DBMS_REDACT.FULL,
        column_name             => 'SENA_ID'
    );
    
    DBMS_REDACT.ALTER_POLICY (
        object_schema           => 'SIVARIA_BACKEND',
        object_name             => 'SIVARIA_YOUNGFORM',
        policy_name             => 'SIVARIA_YOUNGFORM_POLICY',
        function_type           => DBMS_REDACT.FULL,
        column_name             => 'SOCIAL_DATA_ID'
    );
    
    DBMS_REDACT.ALTER_POLICY (
        object_schema           => 'SIVARIA_BACKEND',
        object_name             => 'SIVARIA_YOUNGFORM',
        policy_name             => 'SIVARIA_YOUNGFORM_POLICY',
        function_type           => DBMS_REDACT.RANDOM,
        column_name             => 'CODE'
    );
    
    DBMS_REDACT.ALTER_POLICY (
        object_schema           => 'SIVARIA_BACKEND',
        object_name             => 'SIVARIA_YOUNGFORM',
        policy_name             => 'SIVARIA_YOUNGFORM_POLICY',
        function_type           => DBMS_REDACT.RANDOM,
        column_name             => 'PREDICTION'
    );
    
    /* FAMILY FORM */
    DBMS_REDACT.ALTER_POLICY (
        object_schema           => 'SIVARIA_BACKEND',
        object_name             => 'SIVARIA_FAMILYFORM',
        policy_name             => 'SIVARIA_FAMILYFORM_POLICY',
        function_type           => DBMS_REDACT.FULL,
        column_name             => 'TO_USER_FAMILY_FORM_ID'
    );
    DBMS_REDACT.ALTER_POLICY (
        object_schema           => 'SIVARIA_BACKEND',
        object_name             => 'SIVARIA_FAMILYFORM',
        policy_name             => 'SIVARIA_FAMILYFORM_POLICY',
        function_type           => DBMS_REDACT.FULL,
        column_name             => 'PARTICIPANT_FAMILY_FORM_ID'
    );
    
    DBMS_REDACT.ALTER_POLICY (
        object_schema           => 'SIVARIA_BACKEND',
        object_name             => 'SIVARIA_FAMILYFORM',
        policy_name             => 'SIVARIA_FAMILYFORM_POLICY',
        function_type           => DBMS_REDACT.FULL,
        column_name             => 'SENA_FAMILY_ID'
    );
    
    DBMS_REDACT.ALTER_POLICY (
        object_schema           => 'SIVARIA_BACKEND',
        object_name             => 'SIVARIA_FAMILYFORM',
        policy_name             => 'SIVARIA_FAMILYFORM_POLICY',
        function_type           => DBMS_REDACT.FULL,
        column_name             => 'PARQ_ID'
    );
    
    DBMS_REDACT.ALTER_POLICY (
        object_schema           => 'SIVARIA_BACKEND',
        object_name             => 'SIVARIA_FAMILYFORM',
        policy_name             => 'SIVARIA_FAMILYFORM_POLICY',
        function_type           => DBMS_REDACT.FULL,
        column_name             => 'FAMILY_ID'
    );
    DBMS_REDACT.ALTER_POLICY (
        object_schema           => 'SIVARIA_BACKEND',
        object_name             => 'SIVARIA_FAMILYFORM',
        policy_name             => 'SIVARIA_FAMILYFORM_POLICY',
        function_type           => DBMS_REDACT.FULL,
        column_name             => 'SOCIAL_DATA_ID'
    );
    
    DBMS_REDACT.ALTER_POLICY (
        object_schema           => 'SIVARIA_BACKEND',
        object_name             => 'SIVARIA_FAMILYFORM',
        policy_name             => 'SIVARIA_FAMILYFORM_POLICY',
        function_type           => DBMS_REDACT.RANDOM,
        column_name             => 'CODE'
    );
    
    DBMS_REDACT.ALTER_POLICY (
        object_schema           => 'SIVARIA_BACKEND',
        object_name             => 'SIVARIA_FAMILYFORM',
        policy_name             => 'SIVARIA_FAMILYFORM_POLICY',
        function_type           => DBMS_REDACT.RANDOM,
        column_name             => 'PREDICTION'
    );
    /* PROFESSIONAL FORM */
    DBMS_REDACT.ALTER_POLICY (
        object_schema           => 'SIVARIA_BACKEND',
        object_name             => 'SIVARIA_PROFESSIONALFORM',
        policy_name             => 'SIVARIA_PROFESSIONALFORM_POLICY',
        function_type           => DBMS_REDACT.FULL,
        column_name             => 'TO_USER_PROFESSIONAL_FORM_ID'
    );
    DBMS_REDACT.ALTER_POLICY (
        object_schema           => 'SIVARIA_BACKEND',
        object_name             => 'SIVARIA_PROFESSIONALFORM',
        policy_name             => 'SIVARIA_PROFESSIONALFORM_POLICY',
        function_type           => DBMS_REDACT.FULL,
        column_name             => 'PARTICIPANT_PROFESSIONAL_F8138'
    );
    DBMS_REDACT.ALTER_POLICY (
        object_schema           => 'SIVARIA_BACKEND',
        object_name             => 'SIVARIA_PROFESSIONALFORM',
        policy_name             => 'SIVARIA_PROFESSIONALFORM_POLICY',
        function_type           => DBMS_REDACT.FULL,
        column_name             => 'FAMILY_ID'
    );
    DBMS_REDACT.ALTER_POLICY (
        object_schema           => 'SIVARIA_BACKEND',
        object_name             => 'SIVARIA_PROFESSIONALFORM',
        policy_name             => 'SIVARIA_PROFESSIONALFORM_POLICY',
        function_type           => DBMS_REDACT.FULL,
        column_name             => 'SOCIAL_DATA_ID'
    );
    
    DBMS_REDACT.ALTER_POLICY (
        object_schema           => 'SIVARIA_BACKEND',
        object_name             => 'SIVARIA_PROFESSIONALFORM',
        policy_name             => 'SIVARIA_PROFESSIONALFORM_POLICY',
        function_type           => DBMS_REDACT.RANDOM,
        column_name             => 'CODE'
    );
    
    DBMS_REDACT.ALTER_POLICY (
        object_schema           => 'SIVARIA_BACKEND',
        object_name             => 'SIVARIA_PROFESSIONALFORM',
        policy_name             => 'SIVARIA_PROFESSIONALFORM_POLICY',
        function_type           => DBMS_REDACT.RANDOM,
        column_name             => 'PREDICTION'
    );
    
    /* Subform questionnaires  */
    
    /* SOCIAL DATA FORM */
    DBMS_REDACT.ALTER_POLICY (
        object_schema           => 'SIVARIA_BACKEND',
        object_name             => 'SIVARIA_SOCIALDATAFORM',
        policy_name             => 'SIVARIA_SOCIALDATAFORM_POLICY',
        function_type           => DBMS_REDACT.RANDOM,
        column_name             => 'COURSE'
    );
    
    DBMS_REDACT.ALTER_POLICY (
        object_schema           => 'SIVARIA_BACKEND',
        object_name             => 'SIVARIA_SOCIALDATAFORM',
        policy_name             => 'SIVARIA_SOCIALDATAFORM_POLICY',
        function_type           => DBMS_REDACT.FULL,
        column_name             => 'AGE'
    );
    
    DBMS_REDACT.ALTER_POLICY (
        object_schema           => 'SIVARIA_BACKEND',
        object_name             => 'SIVARIA_SOCIALDATAFORM',
        policy_name             => 'SIVARIA_SOCIALDATAFORM_POLICY',
        function_type           => DBMS_REDACT.RANDOM,
        column_name             => 'GENDER'
    );
    
    DBMS_REDACT.ALTER_POLICY (
        object_schema           => 'SIVARIA_BACKEND',
        object_name             => 'SIVARIA_SOCIALDATAFORM',
        policy_name             => 'SIVARIA_SOCIALDATAFORM_POLICY',
        function_type           => DBMS_REDACT.RANDOM,
        column_name             => 'TRANS'
    );
    
    DBMS_REDACT.ALTER_POLICY (
        object_schema           => 'SIVARIA_BACKEND',
        object_name             => 'SIVARIA_SOCIALDATAFORM',
        policy_name             => 'SIVARIA_SOCIALDATAFORM_POLICY',
        function_type           => DBMS_REDACT.RANDOM,
        column_name             => 'JOB_SITUATION_FATHER'
    );
    
    DBMS_REDACT.ALTER_POLICY (
        object_schema           => 'SIVARIA_BACKEND',
        object_name             => 'SIVARIA_SOCIALDATAFORM',
        policy_name             => 'SIVARIA_SOCIALDATAFORM_POLICY',
        function_type           => DBMS_REDACT.RANDOM,
        column_name             => 'JOB_SITUATION_MOTHER'
    );
    
    DBMS_REDACT.ALTER_POLICY (
        object_schema           => 'SIVARIA_BACKEND',
        object_name             => 'SIVARIA_SOCIALDATAFORM',
        policy_name             => 'SIVARIA_SOCIALDATAFORM_POLICY',
        function_type           => DBMS_REDACT.RANDOM,
        column_name             => 'ACADEMIC_LEVEL_FATHER'
    );
    
    DBMS_REDACT.ALTER_POLICY (
        object_schema           => 'SIVARIA_BACKEND',
        object_name             => 'SIVARIA_SOCIALDATAFORM',
        policy_name             => 'SIVARIA_SOCIALDATAFORM_POLICY',
        function_type           => DBMS_REDACT.RANDOM,
        column_name             => 'ACADEMIC_LEVEL_MOTHER'
    );
    
    DBMS_REDACT.ALTER_POLICY (
        object_schema           => 'SIVARIA_BACKEND',
        object_name             => 'SIVARIA_SOCIALDATAFORM',
        policy_name             => 'SIVARIA_SOCIALDATAFORM_POLICY',
        function_type           => DBMS_REDACT.RANDOM,
        column_name             => 'ACADEMIC_PERFORMANCE'
    );
    
    DBMS_REDACT.ALTER_POLICY (
        object_schema           => 'SIVARIA_BACKEND',
        object_name             => 'SIVARIA_SOCIALDATAFORM',
        policy_name             => 'SIVARIA_SOCIALDATAFORM_POLICY',
        function_type           => DBMS_REDACT.RANDOM,
        column_name             => 'PREVIOUS_PSYCHIATRIC_TREATMENT'
    );
    
    DBMS_REDACT.ALTER_POLICY (
        object_schema           => 'SIVARIA_BACKEND',
        object_name             => 'SIVARIA_SOCIALDATAFORM',
        policy_name             => 'SIVARIA_SOCIALDATAFORM_POLICY',
        function_type           => DBMS_REDACT.RANDOM,
        column_name             => 'CHRONIC_DISEASE'
    );
    
    DBMS_REDACT.ALTER_POLICY (
        object_schema           => 'SIVARIA_BACKEND',
        object_name             => 'SIVARIA_SOCIALDATAFORM',
        policy_name             => 'SIVARIA_SOCIALDATAFORM_POLICY',
        function_type           => DBMS_REDACT.FULL,
        action                  => DBMS_REDACT.ADD_COLUMN,
        column_name             => 'WEIGHT'
    );
    
    DBMS_REDACT.ALTER_POLICY (
        object_schema           => 'SIVARIA_BACKEND',
        object_name             => 'SIVARIA_SOCIALDATAFORM',
        policy_name             => 'SIVARIA_SOCIALDATAFORM_POLICY',
        function_type           => DBMS_REDACT.FULL,
        action                  => DBMS_REDACT.ADD_COLUMN,
        column_name             => 'HEIGHT'
    );
    
    DBMS_REDACT.ALTER_POLICY (
        object_schema           => 'SIVARIA_BACKEND',
        object_name             => 'SIVARIA_SOCIALDATAFORM',
        policy_name             => 'SIVARIA_SOCIALDATAFORM_POLICY',
        function_type           => DBMS_REDACT.RANDOM,
        column_name             => 'DISCRIMINATION_TYPE'
    );
    
    DBMS_REDACT.ALTER_POLICY (
        object_schema           => 'SIVARIA_BACKEND',
        object_name             => 'SIVARIA_SOCIALDATAFORM',
        policy_name             => 'SIVARIA_SOCIALDATAFORM_POLICY',
        function_type           => DBMS_REDACT.RANDOM,
        column_name             => 'CODE'
    );
    
    /* FAMILY SUBFORM */
    
    DBMS_REDACT.ALTER_POLICY (
        object_schema           => 'SIVARIA_BACKEND',
        object_name             => 'SIVARIA_FAMILYSUBFORM',
        policy_name             => 'SIVARIA_FAMILYSUBFORM_POLICY',
        function_type           => DBMS_REDACT.RANDOM,
        column_name             => 'ADICCION_PADRE_MADRE'
    );
    
    DBMS_REDACT.ALTER_POLICY (
        object_schema           => 'SIVARIA_BACKEND',
        object_name             => 'SIVARIA_FAMILYSUBFORM',
        policy_name             => 'SIVARIA_FAMILYSUBFORM_POLICY',
        function_type           => DBMS_REDACT.FULL,
        column_name             => 'MADRE_ADOLESCENTE'
    );
    
    DBMS_REDACT.ALTER_POLICY (
        object_schema           => 'SIVARIA_BACKEND',
        object_name             => 'SIVARIA_FAMILYSUBFORM',
        policy_name             => 'SIVARIA_FAMILYSUBFORM_POLICY',
        function_type           => DBMS_REDACT.FULL,
        column_name             => 'PADRE_ADOLESCENTE'
    );
    
    DBMS_REDACT.ALTER_POLICY (
        object_schema           => 'SIVARIA_BACKEND',
        object_name             => 'SIVARIA_FAMILYSUBFORM',
        policy_name             => 'SIVARIA_FAMILYSUBFORM_POLICY',
        function_type           => DBMS_REDACT.RANDOM,
        column_name             => 'MALTRATO_A_LA_PAREJA'
    );
    
    DBMS_REDACT.ALTER_POLICY (
        object_schema           => 'SIVARIA_BACKEND',
        object_name             => 'SIVARIA_FAMILYSUBFORM',
        policy_name             => 'SIVARIA_FAMILYSUBFORM_POLICY',
        function_type           => DBMS_REDACT.RANDOM,
        column_name             => 'MALTRATO_AL_ADOLESCENTE'
    );
    
    DBMS_REDACT.ALTER_POLICY (
        object_schema           => 'SIVARIA_BACKEND',
        object_name             => 'SIVARIA_FAMILYSUBFORM',
        policy_name             => 'SIVARIA_FAMILYSUBFORM_POLICY',
        function_type           => DBMS_REDACT.RANDOM,
        column_name             => 'PADRES_DIVORCIADOS'
    );
    
    DBMS_REDACT.ALTER_POLICY (
        object_schema           => 'SIVARIA_BACKEND',
        object_name             => 'SIVARIA_FAMILYSUBFORM',
        policy_name             => 'SIVARIA_FAMILYSUBFORM_POLICY',
        function_type           => DBMS_REDACT.RANDOM,
        column_name             => 'RELACIONES_CONFLICTIVAS_HIA657'
    );
    
    DBMS_REDACT.ALTER_POLICY (
        object_schema           => 'SIVARIA_BACKEND',
        object_name             => 'SIVARIA_FAMILYSUBFORM',
        policy_name             => 'SIVARIA_FAMILYSUBFORM_POLICY',
        function_type           => DBMS_REDACT.RANDOM,
        column_name             => 'SITUACION_ECONOMICA_PRECARIA'
    );
    
    DBMS_REDACT.ALTER_POLICY (
        object_schema           => 'SIVARIA_BACKEND',
        object_name             => 'SIVARIA_FAMILYSUBFORM',
        policy_name             => 'SIVARIA_FAMILYSUBFORM_POLICY',
        function_type           => DBMS_REDACT.RANDOM,
        column_name             => 'SUPERVISION_PARENTAL_INSUFF8E6'
    );
    
    DBMS_REDACT.ALTER_POLICY (
        object_schema           => 'SIVARIA_BACKEND',
        object_name             => 'SIVARIA_FAMILYSUBFORM',
        policy_name             => 'SIVARIA_FAMILYSUBFORM_POLICY',
        function_type           => DBMS_REDACT.RANDOM,
        column_name             => 'DUELO'
    );
    
    DBMS_REDACT.ALTER_POLICY (
        object_schema           => 'SIVARIA_BACKEND',
        object_name             => 'SIVARIA_FAMILYSUBFORM',
        policy_name             => 'SIVARIA_FAMILYSUBFORM_POLICY',
        function_type           => DBMS_REDACT.RANDOM,
        column_name             => 'FAMILIA_MONOPARENTAL'
    );
    
    DBMS_REDACT.ALTER_POLICY (
        object_schema           => 'SIVARIA_BACKEND',
        object_name             => 'SIVARIA_FAMILYSUBFORM',
        policy_name             => 'SIVARIA_FAMILYSUBFORM_POLICY',
        function_type           => DBMS_REDACT.FULL,
        column_name             => 'INGRESO_FAMILIAR_MENSUAL'
    );
    
    DBMS_REDACT.ALTER_POLICY (
        object_schema           => 'SIVARIA_BACKEND',
        object_name             => 'SIVARIA_FAMILYSUBFORM',
        policy_name             => 'SIVARIA_FAMILYSUBFORM_POLICY',
        function_type           => DBMS_REDACT.RANDOM,
        column_name             => 'FAMILIA_RECONSTRUIDA'
    );
    
    DBMS_REDACT.ALTER_POLICY (
        object_schema           => 'SIVARIA_BACKEND',
        object_name             => 'SIVARIA_FAMILYSUBFORM',
        policy_name             => 'SIVARIA_FAMILYSUBFORM_POLICY',
        function_type           => DBMS_REDACT.RANDOM,
        column_name             => 'CODE'
    );
    
    DBMS_REDACT.ALTER_POLICY (
        object_schema           => 'SIVARIA_BACKEND',
        object_name             => 'SIVARIA_FAMILYSUBFORM',
        policy_name             => 'SIVARIA_FAMILYSUBFORM_POLICY',
        function_type           => DBMS_REDACT.RANDOM,
        column_name             => 'TRATAMIENTO_PSICOLOGICO_PA4D02'
    );
    
    /* INJURY FORM */
    
    DBMS_REDACT.ALTER_POLICY (
        object_schema           => 'SIVARIA_BACKEND',
        object_name             => 'SIVARIA_INJURYFORM',
        policy_name             => 'SIVARIA_INJURYFORM_POLICY',
        function_type           => DBMS_REDACT.RANDOM,
        column_name             => 'INJURY1'
    );
    
    DBMS_REDACT.ALTER_POLICY (
        object_schema           => 'SIVARIA_BACKEND',
        object_name             => 'SIVARIA_INJURYFORM',
        policy_name             => 'SIVARIA_INJURYFORM_POLICY',
        function_type           => DBMS_REDACT.RANDOM,
        column_name             => 'CODE'
    );
    
    /* ATE FORM */
    
    DBMS_REDACT.ALTER_POLICY (
        object_schema           => 'SIVARIA_BACKEND',
        object_name             => 'SIVARIA_ATEFORM',
        policy_name             => 'SIVARIA_ATEFORM_POLICY',
        function_type           => DBMS_REDACT.RANDOM,
        column_name             => 'CODE'
    );
    /* ATI FORM */
    
    DBMS_REDACT.ALTER_POLICY (
        object_schema           => 'SIVARIA_BACKEND',
        object_name             => 'SIVARIA_ATIFORM',
        policy_name             => 'SIVARIA_ATIFORM_POLICY',
        function_type           => DBMS_REDACT.RANDOM,
        column_name             => 'CODE'
    );
    
    /* EBIPQ ECIPQ FORM */
    
    DBMS_REDACT.ALTER_POLICY (
        object_schema           => 'SIVARIA_BACKEND',
        object_name             => 'SIVARIA_EBIPQECIPQFORM',
        policy_name             => 'SIVARIA_EBIPQECIPQFORM_POLICY',
        function_type           => DBMS_REDACT.RANDOM,
        column_name             => 'CODE'
    );
    
    /* ED FORM */
    
    DBMS_REDACT.ALTER_POLICY (
        object_schema           => 'SIVARIA_BACKEND',
        object_name             => 'SIVARIA_EDFORM',
        policy_name             => 'SIVARIA_EDFORM_POLICY',
        function_type           => DBMS_REDACT.RANDOM,
        column_name             => 'CODE'
    );
    
    /* ER FORM */
    
    DBMS_REDACT.ALTER_POLICY (
        object_schema           => 'SIVARIA_BACKEND',
        object_name             => 'SIVARIA_ERFORM',
        policy_name             => 'SIVARIA_ERFORM_POLICY',
        function_type           => DBMS_REDACT.RANDOM,
        column_name             => 'CODE'
    );
    
    /* INQ FORM */
    
    DBMS_REDACT.ALTER_POLICY (
        object_schema           => 'SIVARIA_BACKEND',
        object_name             => 'SIVARIA_INQFORM',
        policy_name             => 'SIVARIA_INQFORM_POLICY',
        function_type           => DBMS_REDACT.RANDOM,
        column_name             => 'CODE'
    );
    
    /* MULTICAGE CAD 4 FORM */
    
    DBMS_REDACT.ALTER_POLICY (
        object_schema           => 'SIVARIA_BACKEND',
        object_name             => 'SIVARIA_MULTICAGECAD4FORM',
        policy_name             => 'SIVARIA_MULTICAGECAD4FORM_POLICY',
        function_type           => DBMS_REDACT.RANDOM,
        column_name             => 'CODE'
    );
    
    /* PARQ FORM */
    
    DBMS_REDACT.ALTER_POLICY (
        object_schema           => 'SIVARIA_BACKEND',
        object_name             => 'SIVARIA_PARQFORM',
        policy_name             => 'SIVARIA_PARQFORM_POLICY',
        function_type           => DBMS_REDACT.RANDOM,
        column_name             => 'CODE'
    );
    
    /* RRSS FORM */
    
    DBMS_REDACT.ALTER_POLICY (
        object_schema           => 'SIVARIA_BACKEND',
        object_name             => 'SIVARIA_RRSSFORM',
        policy_name             => 'SIVARIA_RRSSFORM_POLICY',
        function_type           => DBMS_REDACT.RANDOM,
        column_name             => 'CODE'
    );
    
    /* SENA FAMILY FORM */
    DBMS_REDACT.ALTER_POLICY (
        object_schema           => 'SIVARIA_BACKEND',
        object_name             => 'SIVARIA_SENAFAMILYFORM',
        policy_name             => 'SIVARIA_SENAFAMILYFORM_POLICY',
        function_type           => DBMS_REDACT.RANDOM,
        column_name             => 'CODE'
    );
    
    /* SENA FAMILY FORM */
    DBMS_REDACT.ALTER_POLICY (
        object_schema           => 'SIVARIA_BACKEND',
        object_name             => 'SIVARIA_SENAFORM',
        policy_name             => 'SIVARIA_SENAFORM_POLICY',
        function_type           => DBMS_REDACT.RANDOM,
        column_name             => 'CODE'
    );
END; 
/

/* SELECT de las tablas enmascaradas. 
Ejecutar en otra conexión distinta de SYSTEM y SIVARIA_BACKEND para ver el resultado 
*/
/*
SELECT * FROM sivaria_backend.SIVARIA_APPUSER;
SELECT * FROM sivaria_backend.SIVARIA_USERHASPARENT;
SELECT * FROM sivaria_backend.SIVARIA_YOUNGFORM;
SELECT * FROM sivaria_backend.SIVARIA_FAMILYFORM;
SELECT * FROM sivaria_backend.SIVARIA_PROFESSIONALFORM;
SELECT * FROM sivaria_backend.AUTHTOKEN_TOKEN;
SELECT * FROM sivaria_backend.SIVARIA_SOCIALDATAFORM;
SELECT * FROM sivaria_backend.SIVARIA_FAMILYSUBFORM;
SELECT * FROM sivaria_backend.SIVARIA_INJURYFORM;
SELECT * FROM sivaria_backend.SIVARIA_ATEFORM;
SELECT * FROM sivaria_backend.SIVARIA_EBIPQECIPQFORM;
SELECT * FROM sivaria_backend.SIVARIA_EDFORM;
SELECT * FROM sivaria_backend.SIVARIA_INQFORM;
SELECT * FROM sivaria_backend.SIVARIA_MULTICAGECAD4FORM;
SELECT * FROM sivaria_backend.SIVARIA_PARQFORM;
SELECT * FROM sivaria_backend.SIVARIA_RRSSFORM;
SELECT * FROM sivaria_backend.SIVARIA_SENAFAMILYFORM;
SELECT * FROM sivaria_backend.SIVARIA_SENAFORM;
*/

/* Eliminación de las políticas. Creado sólo por razones de testeo */
/*BEGIN

  DBMS_REDACT.DROP_POLICY (
    object_schema           => 'SIVARIA_BACKEND',
    object_name             => 'AUTHTOKEN_TOKEN',
    policy_name             => 'AUTHTOKEN_TOKEN_POLICY'
  );
  
  DBMS_REDACT.DROP_POLICY (
    object_schema           => 'SIVARIA_BACKEND',
    object_name             => 'SIVARIA_APPUSER',
    policy_name             => 'SIVARIA_APPUSER_POLICY'
  );
  
  DBMS_REDACT.DROP_POLICY (
    object_schema           => 'SIVARIA_BACKEND',
    object_name             => 'SIVARIA_USERHASPARENT',
    policy_name             => 'SIVARIA_USERHASPARENT_POLICY'
  );


  DBMS_REDACT.DROP_POLICY (
    object_schema           => 'SIVARIA_BACKEND',
    object_name             => 'SIVARIA_YOUNGFORM',
    policy_name             => 'SIVARIA_YOUNGFORM_POLICY'
  );
  
  DBMS_REDACT.DROP_POLICY (
    object_schema           => 'SIVARIA_BACKEND',
    object_name             => 'SIVARIA_FAMILYFORM',
    policy_name             => 'SIVARIA_FAMILYFORM_POLICY'
  );
  
  DBMS_REDACT.DROP_POLICY (
    object_schema           => 'SIVARIA_BACKEND',
    object_name             => 'SIVARIA_PROFESSIONALFORM',
    policy_name             => 'SIVARIA_PROFESSIONALFORM_POLICY'
  );
  
  
  
  DBMS_REDACT.DROP_POLICY (
    object_schema           => 'SIVARIA_BACKEND',
    object_name             => 'SIVARIA_SOCIALDATAFORM',
    policy_name             => 'SIVARIA_SOCIALDATAFORM_POLICY'
  );
  
  DBMS_REDACT.DROP_POLICY (
    object_schema           => 'SIVARIA_BACKEND',
    object_name             => 'SIVARIA_FAMILYSUBFORM',
    policy_name             => 'SIVARIA_FAMILYSUBFORM_POLICY'
  );
  
  DBMS_REDACT.DROP_POLICY (
    object_schema           => 'SIVARIA_BACKEND',
    object_name             => 'SIVARIA_INJURYFORM',
    policy_name             => 'SIVARIA_INJURYFORM_POLICY'
  );
  
  DBMS_REDACT.DROP_POLICY (
    object_schema           => 'SIVARIA_BACKEND',
    object_name             => 'SIVARIA_ATEFORM',
    policy_name             => 'SIVARIA_ATEFORM_POLICY'
  );
  
  DBMS_REDACT.DROP_POLICY (
    object_schema           => 'SIVARIA_BACKEND',
    object_name             => 'SIVARIA_ATIFORM',
    policy_name             => 'SIVARIA_ATIFORM_POLICY'
  );
  
  DBMS_REDACT.DROP_POLICY (
    object_schema           => 'SIVARIA_BACKEND',
    object_name             => 'SIVARIA_CERQSFORM',
    policy_name             => 'SIVARIA_CERQSFORM_POLICY'    
  );
  
  DBMS_REDACT.DROP_POLICY (
    object_schema           => 'SIVARIA_BACKEND',
    object_name             => 'SIVARIA_EBIPQECIPQFORM',
    policy_name             => 'SIVARIA_EBIPQECIPQFORM_POLICY'
  );
  
  DBMS_REDACT.DROP_POLICY (
    object_schema           => 'SIVARIA_BACKEND',
    object_name             => 'SIVARIA_EDFORM',
    policy_name             => 'SIVARIA_EDFORM_POLICY'
  );
  
  DBMS_REDACT.DROP_POLICY (
    object_schema           => 'SIVARIA_BACKEND',
    object_name             => 'SIVARIA_ERFORM',
    policy_name             => 'SIVARIA_ERFORM_POLICY'
  );
END;
/
*/

COMMIT;