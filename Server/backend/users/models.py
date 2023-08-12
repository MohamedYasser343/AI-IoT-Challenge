from django.db import models
from django.contrib.auth.models import AbstractUser

    
class CustomUser(AbstractUser):
    ROLE_CHOICES = (
        ('administrator', 'Administrator'),
        ('manager', 'Manager'),
        ('data_analyst', 'Data Analyst'),
        ('farmer', 'Farmer'),
    )
    
    role = models.CharField(max_length=20, choices=ROLE_CHOICES, null=True)
    birthdate = models.DateField(null=True, blank=True)
    
    def __str__(self):
        return self.username

class Profile(models.Model):
    user = models.OneToOneField(CustomUser, on_delete=models.CASCADE)
    profile_photo = models.ImageField(upload_to='profile_photos/', blank=True, null=True)
    
    def __str__(self):
        return self.user.username
