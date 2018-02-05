from django.db import models
from django.contrib.auth.models import AbstractBaseUser
from django.contrib.auth.models import PermissionsMixin
from django.contrib.auth.models import BaseUserManager
# Create your models here.

class UserProfileManager(BaseUserManager): # needs to match what was called at the objects line below in base user
    '''
    Helps django work with our custom user model
    '''
    def create_user(self, email, name, password=None):
        '''
        Create a new user profile object
        '''
        if not email:
            raise ValueError("Users must have an email address")
        
        email = self.normalize_email(email)
        user = self.model(email=email, name=name)

        user.set_password(password) # encrypts the password for us
        user.save(using=self._db)

        return user

    def create_superuser(self, email, name, password):
        '''
        Create a new superuser with given details
        '''
        user = self.create_user(email, name, password)
        user.is_superuser = True
        user.is_staff = True
        user.save(using=self._db)

        return user

class UserProfile(AbstractBaseUser, PermissionsMixin):
    '''
    Represents a user profile within our system
    '''
    email = models.EmailField(max_length=255, unique=True) # defaults to required
    name = models.CharField(max_length=255)
    ###
    #required when making a custom user
    is_active = models.BooleanField(default=True)
    is_staff = models.BooleanField(default=True)

    objects = UserProfileManager()
    ###
    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['name']

    def get_full_name(self):
        '''
        Required to be used with django admin
        Used to get a users full name
        '''
        return self.name

    def get_short_name(self):
        '''
        Used to get  a users short name
        also required?
        '''

        return self.name

    def __str__(self):
        '''
        django uses this when in needs to conver the object to a string
        '''
        return self.email

class ProfileFeedItem(models.Model):
    '''profile status update'''

    user_profile = models.ForeignKey('UserProfile', on_delete=models.CASCADE) #if user deletes profile, delte status fields too (cascade)
    status_text = models.CharField(max_length=255)
    created_on = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        '''return the model as a string'''

        return self.status_text