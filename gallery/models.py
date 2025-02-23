# gallery/models.py
from django.db import models

class ImageUpload(models.Model):
    image = models.ImageField(upload_to='images/')  # Define where to store uploaded images
    uploaded_at = models.DateTimeField(auto_now_add=True)  # Timestamp for when the image was uploaded

    def __str__(self):
        return str(self.image)
