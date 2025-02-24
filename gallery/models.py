from django.db import models
from django.contrib.auth.models import AbstractUser, Group, Permission

# Custom User Model to Identify Admins
class CustomUser(AbstractUser):
    is_admin = models.BooleanField(default=False)  # Flag for admin users

    # Avoid conflicts by setting unique related names
    groups = models.ManyToManyField(Group, related_name="customuser_groups", blank=True)
    user_permissions = models.ManyToManyField(Permission, related_name="customuser_permissions", blank=True)

    def __str__(self):
        return self.username

# Model to Store Uploaded Images
class ImageUpload(models.Model):
    image = models.ImageField(upload_to='images/')
    uploaded_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return str(self.image)
    

