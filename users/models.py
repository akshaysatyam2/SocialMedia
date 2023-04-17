import datetime

from django.db import models
from django.contrib.auth.models import User
from PIL import Image

# Create your models here.
dob = '2000-01-01'


class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    image = models.ImageField(default='Default.jpg', upload_to='profile_pics')
    bio = models.CharField(max_length=255, default=" ")
    dob = models.DateField(max_length=25, default=dob)
    gender = models.CharField(max_length=6, default=' ')

    def __str__(self):
        return f'{self.user.username} Profile'

    def save(self):
        super().save()

        img = Image.open(self.image.path)

        if img.height > 450 or img.width > 450:
            output_size =(450, 450)
            img.thumbnail(output_size)
            img.save(self.image.path)
