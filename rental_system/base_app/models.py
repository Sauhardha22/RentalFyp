from django.db import models

from django.contrib.auth.models import AbstractUser

class ApplicationUser(AbstractUser):
    phone_no = models.CharField(max_length=14)
    # is_renter = models.BooleanField(default=False)
    # profile_picture = models.ImageField(upload_to='uploads')