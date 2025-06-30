from django.db import models

from django.contrib.auth.models import AbstractUser
from django.utils import timezone


USER_TYPE = (
    ('Vendor', 'Vendor'),
    ('Customer', 'Customer'),
)

# Create your models here.

class User(AbstractUser):
    username = models.CharField(max_length=255, null=True, blank=True)
    email = models.EmailField(unique=True)

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['username']

    def __str__(self):
        return self.email
    
    def save(self, *args, **kwargs):
        email_usernmae, _ = self.email.split('@')
        if not self.username:
            self.username = email_usernmae
        super(User, self).save(*args, **kwargs)


class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)        
    image = models.ImageField(upload_to='images', default="default-user.jpg", null=True, blank=True)
    full_name = models.CharField(max_length=255, null=True, blank=True)
    mobile = models.CharField(max_length=255, null=True, blank=True)
    user_Type = models.CharField(max_length=255, choices=USER_TYPE, null=True, blank=True, default=None)

    def __str__(self):
        # return str(self.user)
        return self.user.username
    
    def save(self, *args, **kwargs):
        # email_usernmae, _ = set.email.split('@')
        if not self.full_name:
            self.full_name = self.user.username
        super(Profile, self).save(*args, **kwargs)