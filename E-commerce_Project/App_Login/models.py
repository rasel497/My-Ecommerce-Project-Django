from django.db import models

# To create a custom user model and Admin pannel
from django.contrib.auth.models import BaseUserManager, BaseUserManager, AbstractBaseUser, PermissionsMixin
from django.utils.translation import ugettext_lazy

# Create your models here.

class MyUserManager(BaseUserManager):
    """A custom Manager to deal with emails as unnique identifer"""
    def _create_user(self, email, password, **extra_fields):
        """Create and save a user with a given email and password"""

        if not email:
            raise ValueError("The E-mail must be set")

        email = self.normalize_email(email)
        user = self.model(email=email, **extra_fields)
        user.set_password(password)
        user.save(using=self._db)
        return user

    # create superuser for admin pannel

    def create_superuser(self, email, password, **extra_fields):
        extra_fields.setdefault('is_staff', True)
        extra_fields.setdefault('is_superuser', True)
        extra_fields.setdefault('is_active', True)


        if extra_fields.get('is_staff') is not True:
            raise ValueError('Superuser must have is_staff-True')
        if extra_fields.get('is_superuser') is not True:
            raise ValueError('Superuser must have is_superuser-True')
        return self._create_user(email, password, **extra_fields)

    # New class for staff user or employee
class User(AbstractBaseUser, PermissionsMixin):
    email = models.EmailField(unique=True, null=False)
    is_staff = models.BooleanField(
        ugettext_lazy('staff status'),
        default=False,
        help_text= ugettext_lazy('Designates whether the user can log in this site')
    )

    is_active = models.BooleanField{
        ugettext_lazy('active'),
        default=True,
        help_text=ugettext_lazy('Designates whether this user should be treated as active. Unselect this instead of deleting accounts')
    }

    USERNAME_FIELD = 'email'
    objects = MyUserManager()

    def __str__(self):
        return self.email

    def get_full_name(self):
        return self.email

    def get_short_name(self):
        return self.email

#when customer buye product tokhon automatically create profile account

class Profile(models.Model):
    user = models.OneToOneField(User, on_delete-models.CASCADE, reletaed_name='profile')
    username = models.CharField(max_length=264, blank=True)
    
