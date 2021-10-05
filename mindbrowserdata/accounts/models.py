from django.db import models
from django.contrib.auth.models import AbstractBaseUser, BaseUserManager

# Create your models here.

class MyAccountManager(BaseUserManager):
    def create_user(self, email, password=None):
        if not email:
            raise ValueError("Manager must have an email address.")
        user = self.model(
                    email=self.normalize_email(email)
                    )
        user.set_password(password)
        user.save(using=self._db)
        return user 
    
    def create_superuser(self,email, password):
        user = self.create_user(
            email=self.normalize_email(email),
            password=password,
        )
        user.is_admin = True
        user.is_staff = True
        user.is_superuser = True

class ManagerModel(AbstractBaseUser):
    email = models.EmailField(verbose_name="email", 
                                max_length=60, 
                                unique=True,
                                error_messages={
                                    'unique': ("A user with that username already exists."),
                                    },
                            )
    firstname = models.CharField(max_length=20)
    lastname = models.CharField(max_length=30)
    password = models.CharField(max_length=10)
    address = models.CharField(max_length=80)
    dob = models.DateField(null=False, max_length=8)
    company_name = models.CharField(max_length=60)

    objects = MyAccountManager()
    
    USERNAME_FIELD = 'email'
    
    def __str__(self):
        return self.email
