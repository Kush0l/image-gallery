# gallery/urls.py
from django.urls import path
from . import views
from .views import admin_login, admin_logout, admin_upload, delete_image

urlpatterns = [
    path('', views.image_gallery, name='image_gallery'),  # URL to the gallery view
    path('admin-login/', admin_login, name='admin_login'),
    path('admin-logout/', admin_logout, name='admin_logout'),
    path('cadmin/upload/', admin_upload, name='admin_upload'),
    path('cadmin/delete/<int:image_id>/', delete_image, name='delete_image'),
]
