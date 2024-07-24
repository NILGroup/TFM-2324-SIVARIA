from django.db import models
from django.contrib.auth.models import AbstractUser
from .api.managers.managers import AppUserManager
from .validators.validators import SpanishPhoneValidator

# Create your models here.
class Post(models.Model):
    title = models.CharField(max_length=200)
    body = models.TextField()

    def __str__(self) -> str:
        return f"Post: {self.title}"
    

class Rol(models.Model):
    slug = models.CharField(max_length=200, unique=True)
    description = models.CharField(max_length=200)
    code = models.CharField(max_length=2, unique=True)

    def __str__(self) -> str:
        return f'Rol: {self.slug}'

class AppUser(AbstractUser): 
    username = models.CharField(max_length=50, unique=False, null=False, blank=True)
    email = models.EmailField(unique=True)
    password = models.CharField(max_length=255, null=True)
    #In production, phone must be unique
    phone = models.CharField(max_length=9, null=True, validators=[SpanishPhoneValidator()], help_text='The phone number must contain only digits and must be a Spanish number.')
    first_name = models.CharField(max_length=255)
    last_name = models.CharField(max_length=255)
    rol = models.ForeignKey(Rol, on_delete=models.SET_NULL, null=True)
    # In production, the token must be unique and cannot be null
    expo_token = models.CharField(max_length=200, null=True)
    is_staff = models.BooleanField(default=False)
    is_superuser = models.BooleanField(default=False)
    is_active = models.BooleanField(default=True)

    code = models.CharField(max_length=30, unique=True, null=True, blank=True)
    birth_date = models.DateField(blank=True, null=True, default=None)
    assigned_to = models.CharField(max_length=15, unique=True, null=True, blank=True)

    USERNAME_FIELD = 'email'  # Establece el campo de email para la autenticación
    REQUIRED_FIELDS = ['first_name', 'last_name']

    objects = AppUserManager()

    def __str__(self) -> str:
        return f'User: {self.first_name} {self.last_name} - {self.email}'

class UserHasParent(models.Model):
    son = models.ForeignKey(AppUser, on_delete=models.CASCADE)
    #id_parent_1 = models.ForeignKey(AppUser, on_delete=models.SET_NULL, allow_null=True)
    #id_parent_2 = models.ForeignKey(AppUser, on_delete=models.SET_NULL, allow_null=True)
    email_parent_1 = models.EmailField(null=True, default=None, blank=True)
    email_parent_2 = models.EmailField(null=True, default=None, blank=True)

    def __str__(self) -> str: 
        return f'UserHasParent: {self.son.id} - {self.son.first_name} {self.son.last_name}'

class PushNotificationType(models.Model):
    slug = models.CharField(max_length=50, unique=True, null=False)
    title = models.CharField(max_length=80)
    body = models.TextField(max_length=255, null=True, default=None, blank=True)
    data = models.TextField(max_length=255, null=True, default=None, blank=True)

    def __str__(self) -> str:
        return f'PushNotificationType: {self.slug}'

class EmailTemplate(models.Model):
    code = models.CharField(max_length=50)
    subject = models.CharField(max_length=80)
    message = models.TextField(max_length=512, null=True, default=None, blank=True)

    def __str__(self) -> str:
        return f'EmailTemplate: {self.code}'

class SenaForm(models.Model):
    code = models.CharField(max_length=30, unique=True, null=True, blank=True)
    sena19 = models.IntegerField(blank=True, null=True, default=None)
    sena23 = models.IntegerField(blank=True, null=True, default=None)
    sena69 = models.IntegerField(blank=True, null=True, default=None)
    sena99 = models.IntegerField(blank=True, null=True, default=None)
    sena103 = models.IntegerField(blank=True, null=True, default=None)
    sena111 = models.IntegerField(blank=True, null=True, default=None)
    sena112 = models.IntegerField(blank=True, null=True, default=None)
    sena115 = models.IntegerField(blank=True, null=True, default=None)
    sena117 = models.IntegerField(blank=True, null=True, default=None)
    sena129 = models.IntegerField(blank=True, null=True, default=None)
    sena137 = models.IntegerField(blank=True, null=True, default=None)
    sena139 = models.IntegerField(blank=True, null=True, default=None)
    sena141 = models.IntegerField(blank=True, null=True, default=None)
    sena146 = models.IntegerField(blank=True, null=True, default=None)    
    sena150 = models.IntegerField(blank=True, null=True, default=None)
    sena188 = models.IntegerField(blank=True, null=True, default=None)

    def __str__(self) -> str:
        return f'SENA: {self.id}'

class InqForm(models.Model):
    code = models.CharField(max_length=30, unique=True, null=True, blank=True)
    inq1 = models.IntegerField(null=True, blank=True, default=None)
    inq2 = models.IntegerField(null=True, blank=True, default=None)
    inq3 = models.IntegerField(null=True, blank=True, default=None)
    inq4 = models.IntegerField(null=True, blank=True, default=None)
    inq5 = models.IntegerField(null=True, blank=True, default=None)
    inq6 = models.IntegerField(null=True, blank=True, default=None)
    inq7 = models.IntegerField(null=True, blank=True, default=None)
    inq8 = models.IntegerField(null=True, blank=True, default=None)
    inq9 = models.IntegerField(null=True, blank=True, default=None)
    inq10= models.IntegerField(null=True, blank=True, default=None)
    inq11 = models.IntegerField(null=True, blank=True, default=None)
    inq12 = models.IntegerField(null=True, blank=True, default=None)
    inq13 = models.IntegerField(null=True, blank=True, default=None)
    inq14 = models.IntegerField(null=True, blank=True, default=None)
    inq15 = models.IntegerField(null=True, blank=True, default=None)

    def __str__(self) -> str:
        return f'INQ: {self.id}'
    
class RrssForm(models.Model):
    code = models.CharField(max_length=30, unique=True, null=True, blank=True)
    rrss1 = models.CharField(max_length=2, null=True, blank=True, default=None)
    rrss2 = models.CharField(max_length=2, null=True, blank=True, default=None)
    rrss3 = models.CharField(max_length=2, null=True, blank=True, default=None)
    rrss4 = models.CharField(max_length=2, null=True, blank=True, default=None)
    rrss5 = models.CharField(max_length=2, null=True, blank=True, default=None)
    rrss6 = models.CharField(max_length=2, null=True, blank=True, default=None)
    rrss7 = models.CharField(max_length=2, null=True, blank=True, default=None)
    
    def __str__(self) -> str:
        return f'RRSS: {self.id}'
    
class MulticageCad4Form(models.Model):
    code = models.CharField(max_length=30, unique=True, null=True, blank=True)
    code = models.CharField(max_length=30, unique=True, null=True, blank=True)
    mcad1 = models.CharField(max_length=2,null=True, blank=True, default=None)
    mcad2 = models.CharField(max_length=2, null=True, blank=True, default=None)
    mcad3 = models.CharField(max_length=2, null=True, blank=True, default=None)
    mcad4 = models.CharField(max_length=2, null=True, blank=True, default=None)
    mcad5 = models.CharField(max_length=2, null=True, blank=True, default=None)
    mcad6 = models.CharField(max_length=2, null=True, blank=True, default=None)
    mcad7 = models.CharField(max_length=2, null=True, blank=True, default=None)
    mcad8 = models.CharField(max_length=2, null=True, blank=True, default=None)
    mcad9 = models.CharField(max_length=2, null=True, blank=True, default=None)
    mcad10= models.CharField(max_length=2, null=True, blank=True, default=None)
    mcad11 = models.CharField(max_length=2, null=True, blank=True, default=None)
    mcad12 = models.CharField(max_length=2, null=True, blank=True, default=None)

    def __str__(self) -> str:
        return f'MULTICAGE CAD-4: {self.id}'
    
class EbipqEcipqForm(models.Model):
    code = models.CharField(max_length=30, unique=True, null=True, blank=True)
    vb1 = models.IntegerField(null=True, blank=True, default=None)
    vb2 = models.IntegerField(null=True, blank=True, default=None)
    vb4 = models.IntegerField(null=True, blank=True, default=None)
    ab1 = models.IntegerField(null=True, blank=True, default=None)
    ab2 = models.IntegerField(null=True, blank=True, default=None)
    ab4 = models.IntegerField(null=True, blank=True, default=None)
    cybv1 = models.IntegerField(null=True, blank=True, default=None)
    cybv2 = models.IntegerField(null=True, blank=True, default=None)
    cybv3 = models.IntegerField(null=True, blank=True, default=None)
    cybb1= models.IntegerField(null=True, blank=True, default=None)
    cybb2 = models.IntegerField(null=True, blank=True, default=None)
    cybb3 = models.IntegerField(null=True, blank=True, default=None)

    def __str__(self) -> str:
        return f'EBIPQ y ECIPQ: {self.id}'
    
class CerqsForm(models.Model):
    code = models.CharField(max_length=30, unique=True, null=True, blank=True)
    cerqs1 = models.IntegerField(null=True, blank=True, default=None)
    cerqs2 = models.IntegerField(null=True, blank=True, default=None)
    cerqs3 = models.IntegerField(null=True, blank=True, default=None)
    cerqs4 = models.IntegerField(null=True, blank=True, default=None)
    cerqs5 = models.IntegerField(null=True, blank=True, default=None)
    cerqs6 = models.IntegerField(null=True, blank=True, default=None)
    cerqs7 = models.IntegerField(null=True, blank=True, default=None)
    cerqs8 = models.IntegerField(null=True, blank=True, default=None)
    cerqs9 = models.IntegerField(null=True, blank=True, default=None)
    cerqs10= models.IntegerField(null=True, blank=True, default=None)
    cerqs11 = models.IntegerField(null=True, blank=True, default=None)
    cerqs12 = models.IntegerField(null=True, blank=True, default=None)
    cerqs13 = models.IntegerField(null=True, blank=True, default=None)
    cerqs14 = models.IntegerField(null=True, blank=True, default=None)
    cerqs15 = models.IntegerField(null=True, blank=True, default=None)
    cerqs16 = models.IntegerField(null=True, blank=True, default=None)
    cerqs17 = models.IntegerField(null=True, blank=True, default=None)
    cerqs18 = models.IntegerField(null=True, blank=True, default=None)

    def __str__(self) -> str:
        return f'CERQ-S: {self.id}'
    
class AtiForm(models.Model):
    code = models.CharField(max_length=30, unique=True, null=True, blank=True)
    ati1 = models.IntegerField(null=True, blank=True, default=None)
    ati2 = models.IntegerField(null=True, blank=True, default=None)
    ati3 = models.IntegerField(null=True, blank=True, default=None)
    ati4 = models.IntegerField(null=True, blank=True, default=None)
    ati5 = models.IntegerField(null=True, blank=True, default=None)
    ati6 = models.IntegerField(null=True, blank=True, default=None)

    def __str__(self) -> str:
        return f'ATI: {self.id}'
    
class AteForm(models.Model):
    code = models.CharField(max_length=30, unique=True, null=True, blank=True)
    ate1 = models.IntegerField(null=True, blank=True, default=None)
    ate2 = models.IntegerField(null=True, blank=True, default=None)
    ate3 = models.IntegerField(null=True, blank=True, default=None)
    ate4 = models.IntegerField(null=True, blank=True, default=None)
    ate5 = models.IntegerField(null=True, blank=True, default=None)
    ate6 = models.IntegerField(null=True, blank=True, default=None)
    ate7 = models.IntegerField(null=True, blank=True, default=None)
    ate8 = models.IntegerField(null=True, blank=True, default=None)
    ate9 = models.IntegerField(null=True, blank=True, default=None)
    ate10= models.IntegerField(null=True, blank=True, default=None)

    def __str__(self) -> str:
        return f'ATE: {self.id}'
    
class EdForm(models.Model):
    code = models.CharField(max_length=30, unique=True, null=True, blank=True)
    ed1 = models.IntegerField(null=True, blank=True, default=None)
    ed2 = models.IntegerField(null=True, blank=True, default=None)
    ed3 = models.IntegerField(null=True, blank=True, default=None)
    ed4 = models.IntegerField(null=True, blank=True, default=None)
    ed5 = models.IntegerField(null=True, blank=True, default=None)
    ed6 = models.IntegerField(null=True, blank=True, default=None)
    ed7 = models.IntegerField(null=True, blank=True, default=None)
    ed8 = models.IntegerField(null=True, blank=True, default=None)
    ed9 = models.IntegerField(null=True, blank=True, default=None)
    ed10= models.IntegerField(null=True, blank=True, default=None)
    ed11 = models.IntegerField(null=True, blank=True, default=None)
    ed12 = models.IntegerField(null=True, blank=True, default=None)
    ed13 = models.IntegerField(null=True, blank=True, default=None)
    ed14 = models.IntegerField(null=True, blank=True, default=None)
    ed15 = models.IntegerField(null=True, blank=True, default=None)
    ed16 = models.IntegerField(null=True, blank=True, default=None)

    def __str__(self) -> str:
        return f'ED: {self.id}'
    
class ErForm(models.Model):
    code = models.CharField(max_length=30, unique=True, null=True, blank=True)
    er1 = models.IntegerField(null=True, blank=True, default=None)
    er2 = models.IntegerField(null=True, blank=True, default=None)
    er3 = models.IntegerField(null=True, blank=True, default=None)
    er4 = models.IntegerField(null=True, blank=True, default=None)
    er5 = models.IntegerField(null=True, blank=True, default=None)
    er6 = models.IntegerField(null=True, blank=True, default=None)
    er7 = models.IntegerField(null=True, blank=True, default=None)
    er8 = models.IntegerField(null=True, blank=True, default=None)
    er9 = models.IntegerField(null=True, blank=True, default=None)
    er10= models.IntegerField(null=True, blank=True, default=None)

    def __str__(self) -> str:
        return f'ER: {self.id}'
    
class FamilySubForm(models.Model):
    code = models.CharField(max_length=30, unique=True, null=True, blank=True)
    padre_adolescente = models.CharField(max_length=2, null=True, blank=True, default=None)
    madre_adolescente = models.CharField(max_length=2, null=True, blank=True, default=None)
    familia_monoparental = models.CharField(max_length=2, null=True, blank=True, default=None)
    padres_divorciados = models.CharField(max_length=2, null=True, blank=True, default=None)
    tratamiento_psicologico_padre_madre = models.CharField(max_length=2, null=True, blank=True, default=None)
    adiccion_padre_madre = models.CharField(max_length=2, null=True, blank=True, default=None)
    relaciones_conflictivas_hijo_padre_madre = models.CharField(max_length=2, null=True, blank=True, default=None)
    familia_reconstruida = models.CharField(max_length=2, null=True, blank=True, default=None)
    supervision_parental_insuficiente = models.CharField(max_length=2, null=True, blank=True, default=None)
    maltrato_al_adolescente = models.CharField(max_length=2, null=True, blank=True, default=None)
    maltrato_a_la_pareja = models.CharField(max_length=2, null=True, blank=True, default=None)
    ingreso_familiar_mensual = models.FloatField(null=True, blank=True, default=None)
    situacion_economica_precaria = models.CharField(max_length=2, null=True, blank=True, default=None)
    duelo = models.CharField(max_length=2, null=True, blank=True, default=None)

    def __str__(self) -> str:
        return f'FAMILY: {self.id}'
    
class InjuryForm(models.Model):
    code = models.CharField(max_length=30, unique=True, null=True, blank=True)
    injury1 = models.CharField(max_length=2, null=True, blank=True, default=None)

    def __str__(self) -> str:
        return f'INJURY: {self.id}'
    
class ParqForm(models.Model):
    code = models.CharField(max_length=30, unique=True, null=True, blank=True)
    parq1 = models.IntegerField(null=True, blank=True, default=None)
    parq2 = models.IntegerField(null=True, blank=True, default=None)
    parq3 = models.IntegerField(null=True, blank=True, default=None)
    parq4 = models.IntegerField(null=True, blank=True, default=None)
    parq5 = models.IntegerField(null=True, blank=True, default=None)
    parq6 = models.IntegerField(null=True, blank=True, default=None)
    parq7 = models.IntegerField(null=True, blank=True, default=None)
    parq8 = models.IntegerField(null=True, blank=True, default=None)
    parq9 = models.IntegerField(null=True, blank=True, default=None)
    parq10= models.IntegerField(null=True, blank=True, default=None)
    parq11 = models.IntegerField(null=True, blank=True, default=None)
    parq12 = models.IntegerField(null=True, blank=True, default=None)
    parq13 = models.IntegerField(null=True, blank=True, default=None)
    parq14 = models.IntegerField(null=True, blank=True, default=None)
    parq15 = models.IntegerField(null=True, blank=True, default=None)
    parq16 = models.IntegerField(null=True, blank=True, default=None)
    parq17 = models.IntegerField(null=True, blank=True, default=None)
    parq18 = models.IntegerField(null=True, blank=True, default=None)
    parq19 = models.IntegerField(null=True, blank=True, default=None)
    parq20 = models.IntegerField(null=True, blank=True, default=None)
    parq21 = models.IntegerField(null=True, blank=True, default=None)
    parq22 = models.IntegerField(null=True, blank=True, default=None)
    parq23 = models.IntegerField(null=True, blank=True, default=None)
    parq24 = models.IntegerField(null=True, blank=True, default=None)
    parq25 = models.IntegerField(null=True, blank=True, default=None)
    parq26 = models.IntegerField(null=True, blank=True, default=None)
    parq27 = models.IntegerField(null=True, blank=True, default=None)
    parq28 = models.IntegerField(null=True, blank=True, default=None)
    parq29 = models.IntegerField(null=True, blank=True, default=None)

    def __str__(self) -> str:
        return f'PARQ: {self.id}'
    
class SocialDataForm(models.Model):
    code = models.CharField(max_length=30, unique=True, null=True, blank=True)
    course = models.CharField(max_length=30, null=True, blank=True, default=None)
    age = models.IntegerField(null=True, blank=True, default=None)
    gender = models.CharField(max_length=30, null=True, blank=True, default=None)
    trans = models.CharField(max_length=10, null=True, blank=True, default=None)
    job_situation_father = models.CharField(max_length=30, null=True, blank=True, default=None)
    job_situation_mother = models.CharField(max_length=30, null=True, blank=True, default=None)
    academic_level_father = models.CharField(max_length=30, null=True, blank=True, default=None)
    academic_level_mother = models.CharField(max_length=30, null=True, blank=True, default=None)
    academic_performance = models.CharField(max_length=30, null=True, blank=True, default=None)
    previous_psychiatric_treatment= models.CharField(max_length=2, null=True, blank=True, default=None)
    chronic_disease = models.CharField(max_length=2, null=True, blank=True, default=None)
    female_self_perception = models.IntegerField(null=True, blank=True, default=None)
    male_self_perception = models.IntegerField(null=True, blank=True, default=None)
    female_others_perception = models.IntegerField(null=True, blank=True, default=None)
    male_others_perception = models.IntegerField(null=True, blank=True, default=None)
    weight = models.FloatField(null=True, blank=True, default=None)
    height = models.FloatField(null=True, blank=True, default=None)
    discrimination_type = models.CharField(max_length=30, null=True, blank=True, default=None)

    def __str__(self) -> str:
        return f'SOCIAL DATA: {self.id}'
    
class SenaFamilyForm(models.Model):    
    code = models.CharField(max_length=30, unique=True, null=True, blank=True)
    sena104 = models.IntegerField(blank=True, null=True, default=None)
    sena117 = models.IntegerField(blank=True, null=True, default=None)
    sena118 = models.IntegerField(blank=True, null=True, default=None)
    sena121 = models.IntegerField(blank=True, null=True, default=None)
    sena123 = models.IntegerField(blank=True, null=True, default=None)
    sena124 = models.IntegerField(blank=True, null=True, default=None)
    sena125 = models.IntegerField(blank=True, null=True, default=None)
    sena135 = models.IntegerField(blank=True, null=True, default=None)
    sena137 = models.IntegerField(blank=True, null=True, default=None)
    sena138 = models.IntegerField(blank=True, null=True, default=None)
    sena139 = models.IntegerField(blank=True, null=True, default=None)
    sena140 = models.IntegerField(blank=True, null=True, default=None)
    sena145 = models.IntegerField(blank=True, null=True, default=None)
    sena146 = models.IntegerField(blank=True, null=True, default=None)    
    sena148 = models.IntegerField(blank=True, null=True, default=None)
    sena154 = models.IntegerField(blank=True, null=True, default=None)

    def __str__(self) -> str:
        return f'SENA FAMILY: {self.id}'

class YoungForm(models.Model):
    participant_young_form = models.ForeignKey(AppUser, on_delete=models.CASCADE, related_name='participant_young_form')
    code = models.CharField(max_length=30, unique=True, null=True, blank=True)
    date = models.DateTimeField(blank=True, null=True)
    social_data = models.ForeignKey(SocialDataForm, default=None, null=True, blank=True, on_delete=models.CASCADE)
    ebipq_ecipq = models.ForeignKey(EbipqEcipqForm, default=None, null=True, blank=True, on_delete=models.CASCADE)
    rrss = models.ForeignKey(RrssForm, default=None, null=True, blank=True, on_delete=models.CASCADE)
    mcad = models.ForeignKey(MulticageCad4Form, default=None, null=True, blank=True, on_delete=models.CASCADE)
    cerqs = models.ForeignKey(CerqsForm, default=None, null=True, blank=True, on_delete=models.CASCADE)
    ati = models.ForeignKey(AtiForm, default=None, null=True, blank=True, on_delete=models.CASCADE)
    ate = models.ForeignKey(AteForm, default=None, null=True, blank=True, on_delete=models.CASCADE)
    ed = models.ForeignKey(EdForm, default=None, null=True, blank=True, on_delete=models.CASCADE)
    er = models.ForeignKey(ErForm, default=None, null=True, blank=True, on_delete=models.CASCADE)
    inq = models.ForeignKey(InqForm, default=None, null=True, blank=True, on_delete=models.CASCADE)
    sena = models.ForeignKey(SenaForm, default=None, null=True, blank=True, on_delete=models.CASCADE)
    injury = models.ForeignKey(InjuryForm, default=None, null=True, blank=True, on_delete=models.CASCADE)
    family = models.ForeignKey(FamilySubForm, default=None, null=True, blank=True, on_delete=models.CASCADE)
    prediction = models.CharField(max_length=30, null=True, blank=True, default=None)

    def __str__(self) -> str:
        return f'Formulario de jóvenes: {self.code}'
    
class FamilyForm(models.Model):
    participant_family_form = models.ForeignKey(AppUser, on_delete=models.CASCADE, related_name='participant_family_form')
    to_user_family_form = models.ForeignKey(AppUser, on_delete=models.CASCADE, related_name='to_user_family_form')
    code = models.CharField(max_length=30, unique=True, null=True, blank=True)
    date = models.DateTimeField(blank=True, null=True)
    social_data = models.ForeignKey(SocialDataForm, default=None, null=True, blank=True, on_delete=models.CASCADE)
    family = models.ForeignKey(FamilySubForm, default=None, null=True, blank=True, on_delete=models.CASCADE)
    sena_family = models.ForeignKey(SenaFamilyForm, default=None, null=True, blank=True, on_delete=models.CASCADE)
    parq = models.ForeignKey(ParqForm, default=None, null=True, blank=True, on_delete=models.CASCADE)
    prediction = models.CharField(max_length=30, null=True, blank=True, default=None)
    
    def __str__(self) -> str:
        return f'Formularios de familiares: {self.code}'
    
class ProfessionalForm(models.Model):
    participant_professional_form = models.ForeignKey(AppUser, on_delete=models.CASCADE, related_name='participant_professional_form')
    to_user_professional_form = models.ForeignKey(AppUser, on_delete=models.CASCADE, related_name='to_user_professional_form')
    code = models.CharField(max_length=30, unique=True, null=True, blank=True)
    date = models.DateTimeField(blank=True, null=True)
    social_data = models.ForeignKey(SocialDataForm, default=None, null=True, blank=True, on_delete=models.CASCADE) 
    family = models.ForeignKey(FamilySubForm, default=None, null=True, blank=True, on_delete=models.CASCADE)
    prediction = models.CharField(max_length=30, null=True, blank=True, default=None)
    
    def __str__(self) -> str:
        return f'Formulario profesionales: {self.code}'