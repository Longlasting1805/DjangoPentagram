from django.db import models


# Create your models here.

class Owner(models.Model):
    username = models.CharField(max_length=20, unique=True)
    email = models.EmailField()
    bio = models.TextField(null=True)
    phone_number = models.CharField(max_length=15)
    profile_picture = models.ImageField(default='user..png', upload_to="user_images")
    date_crated = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.username
