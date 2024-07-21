from django.contrib.auth.base_user import BaseUserManager
import datetime

class AppUserManager(BaseUserManager):
    
    def create_user(self, email, password, **extra_fields):
        if not email:
            raise ValueError('The email field must be set')
        email = self.normalize_email(email)
        user = self.model(email=email, **extra_fields)
        user.set_password(password)
        user.username = user.first_name + user.last_name
        user.save(using=self._db)
        return user
    
    def create_superuser(self, email, password, **extra_fields):        
        """
        Create and save a SuperUser with the given email and password.
        """
        if not email:
            raise ValueError("User must have an email")
        if not password:
            raise ValueError("User must have a password")
        
        #extra_fields.setdefault('username', str(datetime.now()))
        #random_phone_number = random.randint() 
        extra_fields.setdefault('phone', None) 
        extra_fields.setdefault('is_staff', True)
        extra_fields.setdefault('is_superuser', True)
        extra_fields.setdefault('is_active', True) 

        if extra_fields.get('is_superuser') is not True:
            raise ValueError('Superuser must have is_active=True.')
        if extra_fields.get('is_staff') is not True:
            raise ValueError('Superuser must have is_staff=True.')
        if extra_fields.get('is_superuser') is not True:
            raise ValueError('Superuser must have is_superuser=True.')
    

        return self.create_user(email,  
                                password,
                                **extra_fields)
        #user.is_admin = True
        #user.save(using=self._db)
        #return user