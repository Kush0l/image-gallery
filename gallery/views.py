from django.shortcuts import render
from .models import ImageUpload

def image_gallery(request):
    images = ImageUpload.objects.all()
    return render(request, 'image_list.html', {'images': images})
