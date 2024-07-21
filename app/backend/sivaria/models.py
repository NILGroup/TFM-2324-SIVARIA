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

class SENA(models.Model):
    user = models.ForeignKey(AppUser, on_delete=models.CASCADE)
    code = models.CharField(max_length=20)
    date = models.DateTimeField(blank=True, null=True, default=None)
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


class INQ(models.Model):
    user = models.ForeignKey(AppUser, on_delete=models.CASCADE)
    code = models.CharField(max_length=20)
    date = models.DateTimeField(blank=True, null=True, default=None)
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

class RRSS(models.Model):
    user = models.ForeignKey(AppUser, on_delete=models.CASCADE)
    code = models.CharField(max_length=20)
    date = models.DateTimeField(blank=True, null=True, default=None)
    rrss1 = models.IntegerField(null=True, blank=True, default=None)
    rrss2 = models.IntegerField(null=True, blank=True, default=None)
    rrss3 = models.IntegerField(null=True, blank=True, default=None)
    rrss4 = models.IntegerField(null=True, blank=True, default=None)
    rrss5 = models.IntegerField(null=True, blank=True, default=None)
    rrss6 = models.IntegerField(null=True, blank=True, default=None)
    rrss7 = models.IntegerField(null=True, blank=True, default=None)
    
class MULTICAGE_CAD_4(models.Model):
    user = models.ForeignKey(AppUser, on_delete=models.CASCADE)
    code = models.CharField(max_length=20)
    date = models.DateTimeField(blank=True, null=True, default=None)
    mcad1 = models.IntegerField(null=True, blank=True, default=None)
    mcad2 = models.IntegerField(null=True, blank=True, default=None)
    mcad3 = models.IntegerField(null=True, blank=True, default=None)
    mcad4 = models.IntegerField(null=True, blank=True, default=None)
    mcad5 = models.IntegerField(null=True, blank=True, default=None)
    mcad6 = models.IntegerField(null=True, blank=True, default=None)
    mcad7 = models.IntegerField(null=True, blank=True, default=None)
    mcad8 = models.IntegerField(null=True, blank=True, default=None)
    mcad9 = models.IntegerField(null=True, blank=True, default=None)
    mcad10= models.IntegerField(null=True, blank=True, default=None)
    mcad11 = models.IntegerField(null=True, blank=True, default=None)
    mcad12 = models.IntegerField(null=True, blank=True, default=None)

class EBIPQ_ECIPQ(models.Model):
    user = models.ForeignKey(AppUser, on_delete=models.CASCADE)
    code = models.CharField(max_length=20)
    date = models.DateTimeField(blank=True, null=True, default=None)
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

class CERQS(models.Model):
    user = models.ForeignKey(AppUser, on_delete=models.CASCADE)
    code = models.CharField(max_length=20)
    date = models.DateTimeField(blank=True, null=True, default=None)
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

class ED(models.Model):
    user = models.ForeignKey(AppUser, on_delete=models.CASCADE)
    code = models.CharField(max_length=20)
    date = models.DateTimeField(blank=True, null=True, default=None)
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

class ER(models.Model):
    user = models.ForeignKey(AppUser, on_delete=models.CASCADE)
    code = models.CharField(max_length=20)
    date = models.DateTimeField(blank=True, null=True, default=None)
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

class FAMILY(models.Model):
    user = models.ForeignKey(AppUser, on_delete=models.CASCADE)
    code = models.CharField(max_length=20)
    date = models.DateTimeField(blank=True, null=True, default=None)
    family1 = models.IntegerField(null=True, blank=True, default=None)
    family2 = models.IntegerField(null=True, blank=True, default=None)
    family3 = models.IntegerField(null=True, blank=True, default=None)
    family4 = models.IntegerField(null=True, blank=True, default=None)
    family5 = models.IntegerField(null=True, blank=True, default=None)
    family6 = models.IntegerField(null=True, blank=True, default=None)
    family7 = models.IntegerField(null=True, blank=True, default=None)
    family8 = models.IntegerField(null=True, blank=True, default=None)
    family9 = models.IntegerField(null=True, blank=True, default=None)
    family10= models.IntegerField(null=True, blank=True, default=None)
    family11 = models.IntegerField(null=True, blank=True, default=None)
    family12 = models.IntegerField(null=True, blank=True, default=None)
    family13 = models.IntegerField(null=True, blank=True, default=None)

class INJURY(models.Model):
    user = models.ForeignKey(AppUser, on_delete=models.CASCADE)
    code = models.CharField(max_length=20)
    date = models.DateTimeField(blank=True, null=True, default=None)
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

class PARQ(models.Model):
    user = models.ForeignKey(AppUser, on_delete=models.CASCADE)
    code = models.CharField(max_length=20)
    date = models.DateTimeField(blank=True, null=True, default=None)
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

class SOCIAL_DATA(models.Model):
    user = models.ForeignKey(AppUser, on_delete=models.CASCADE)
    code = models.CharField(max_length=20)
    date = models.DateTimeField(blank=True, null=True, default=None)
    course = models.CharField(max_length=30, null=True, blank=True, default=None)
    age = models.IntegerField(null=True, blank=True, default=None)
    gender = models.CharField(max_length=30, null=True, blank=True, default=None)
    trans = models.CharField(max_length=10, null=True, blank=True, default=None)
    job_situation_father = models.CharField(max_length=30, null=True, blank=True, default=None)
    job_situation_mother = models.CharField(max_length=30, null=True, blank=True, default=None)
    academic_level_father = models.CharField(max_length=30, null=True, blank=True, default=None)
    academic_level_mother = models.CharField(max_length=30, null=True, blank=True, default=None)
    academic_performance = models.CharField(max_length=30, null=True, blank=True, default=None)
    previous_psychiatric_treatment= models.IntegerField(null=True, blank=True, default=None)
    chronic_disease = models.IntegerField(null=True, blank=True, default=None)
    female_self_perception = models.IntegerField(null=True, blank=True, default=None)
    male_self_perception = models.IntegerField(null=True, blank=True, default=None)
    female_others_perception = models.IntegerField(null=True, blank=True, default=None)
    male_others_perception = models.IntegerField(null=True, blank=True, default=None)
    weight = models.FloatField(null=True, blank=True, default=None)
    height = models.FloatField(null=True, blank=True, default=None)
    discrimination_type = models.CharField(max_length=30, null=True, blank=True, default=None)