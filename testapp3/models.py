from django.db import models
from django.contrib.auth.models import User
from django.contrib.auth.models import BaseUserManager, AbstractBaseUser
from django import forms
from django.contrib import admin
from django.utils import timezone



class Recipes(models.Model):
    food_item=models.CharField(max_length=20)
    ingredients=models.CharField(max_length=50)
    food_process=models.TextField(max_length=20)
    recipe_Img= models.ImageField(upload_to='images/', blank=True, null=True, default=0)


def __str__(self):
    return self.food_item


class MyUserManager(BaseUserManager):
    def create_user(self, email, date_of_birth, password=None):
        """
        Creates and saves a User with the given email, date of
        birth and password.
        """
        if not email:
            raise ValueError('Users must have an email address')

        user = self.model(email=self.normalize_email(email), date_of_birth=date_of_birth,)

        user.set_password(password)
        user.save(using=self._db)
        return user

class MyUser(AbstractBaseUser):
    email = models.EmailField(verbose_name='email address',max_length=255,unique=True,)
    date_of_birth = models.DateField()
    f_name = models.CharField(max_length=50, blank=True ,null=True)
    first_name = models.CharField(max_length=25)
    last_name = models.CharField(max_length=30)
    is_active = models.BooleanField(default=True)
    is_admin = models.BooleanField(default=False)

    objects = MyUserManager()

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['date_of_birth']

def __str__(self):
    return self.email

def has_perm(self, perm, obj=None):
    "Does the user have a specific permission?"
        # Simplest possible answer: Yes, always
    return True

def has_module_perms(self, app_label):
    "Does the user have permissions to view the app `app_label`?"
        # Simplest possible answer: Yes, always
    return True

@property
def is_staff(self):
    "Is the user a member of staff?"
        # Simplest possible answer: All admins are staff
    return self.is_admin


