# gallery/urls.py
from django.urls import path
from . import views

urlpatterns = [
    path('', views.image_gallery, name='image_gallery'),  # URL to the gallery view
]
