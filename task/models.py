from django.db import models
from .validators import validate_file_extension
from django.utils import timezone
from django.conf import settings
from django.utils.translation import ugettext_lazy as _ 
from django.contrib.auth.models import BaseUserManager
from django.contrib.auth.models import AbstractBaseUser
from django.contrib.auth.models import PermissionsMixin
#from django.contrib.auth.models import User
from django.forms import ModelForm

class Article(models.Model):
	DRAFT='draft'
	PUBLISHED='published'
	
	STATUS_CHOICES = (
		(DRAFT,_("Draft")),
		(PUBLISHED,_("Published")),
		)

	author=models.ForeignKey(settings.AUTH_USER_MODEL,on_delete=models.CASCADE)
	title=models.CharField(max_length=100,)
	body=models.TextField()
	status=models.CharField(choices=STATUS_CHOICES,default=DRAFT, max_length=10,)
	#file = models.FileField(upload_to="documents/%Y/%m/%d", validators=[validate_file_extension])

	def __str__(self):
		return self.title

class Art(models.Model):
    DRAFT='draft'
    PUBLISHED='published'
    
    STATUS_CHOICES = (
        (DRAFT,_("Draft")),
        (PUBLISHED,_("Published")),
        )

    author=models.ForeignKey(settings.AUTH_USER_MODEL,on_delete=models.CASCADE)
    title=models.CharField(max_length=100,)
    body=models.TextField()
    status=models.CharField(choices=STATUS_CHOICES,default=DRAFT, max_length=10,)
    #file = models.FileField(upload_to="documents/%Y/%m/%d", validators=[validate_file_extension])

    def __str__(self):
        return self.title


class Img(models.Model):
    image=models.ImageField(null=True, blank=True, upload_to='images/')
    




class MyUserManager(BaseUserManager):

    def _create_user(self, email, password, **extra_fields):
        if not email:
            raise ValueError('The Email must be set')
        email = self.normalize_email(email)
        user = self.model(email=email, **extra_fields)
        user.set_password(password)
        user.save()
        return user

    def create_superuser(self, email, password, **extra_fields):
        extra_fields.setdefault('is_staff', True)
        extra_fields.setdefault('is_superuser', True)
        extra_fields.setdefault('is_active', True)

        if extra_fields.get('is_staff') is not True:
            raise ValueError('Superuser must have is_staff=True.')
        if extra_fields.get('is_superuser') is not True:
            raise ValueError('Superuser must have is_superuser=True.')
        return self._create_user(email, password, **extra_fields)

class User(AbstractBaseUser, PermissionsMixin):
    email = models.EmailField(unique=True, null=True)
    is_staff = models.BooleanField(
        _('staff status'),
        default=False,
        help_text=_('Designates whether the user can log into this site.'),
    )
    is_active = models.BooleanField(
        _('active'),
        default=True,
        help_text=_(
            'Designates whether this user should be treated as active. '
            'Unselect this instead of deleting accounts.'
        ),
    )
    USERNAME_FIELD = 'email'
    objects = MyUserManager()

    def __str__(self):
        return self.email

    def get_full_name(self):
        return self.email

    def get_short_name(self):
        return self.email
