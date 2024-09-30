from django.db import models
from django.contrib.auth.models import User

# Create your models here.

class Profile(models.Model):
    full_name = models.CharField('full name', max_length=64, blank=True, null=True)
    dob = models.DateField('date of birth', blank=True, null=True)
    user = models.OneToOneField(User, on_delete=models.CASCADE)

    def __str__(self):
        return self.full_name if self.full_name else self.user.username
