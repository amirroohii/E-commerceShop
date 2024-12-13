from django.db import models
from django.contrib.auth.models import AbstractUser
# Create your models here.

class User(AbstractUser):
    email = models.EmailField(unique=True)
    avatar = models.ImageField(upload_to='images/avatars')
    user_bio = models.TextField(blank=True, null=True)
    address = models.TextField(blank=True, null=True)

    def __str__(self):
        if self.first_name is not '' and self.last_name is not '':
            return self.get_full_name()
        return self.email
