from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from .models import ImageUpload

def image_gallery(request):
    images = ImageUpload.objects.all()
    return render(request, 'image_list.html', {'images': images})



# Custom Admin Login
def admin_login(request):
    if request.method == "POST":
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(request, username=username, password=password)

        if user is not None and user.is_staff:  # Only staff (admins) can login
            login(request, user)
            return redirect('admin_upload')
        else:
            return render(request, 'admin_login.html', {'error': 'Invalid Credentials or Not an Admin'})

    return render(request, 'admin_login.html')

# Logout View
def admin_logout(request):
    logout(request)
    return redirect('admin_login')

@login_required
def admin_upload(request):
    if not request.user.is_staff:
        return redirect('admin_login')  # Restrict non-admin users

    if request.method == 'POST' and request.FILES.get('image'):
        image = request.FILES['image']
        ImageUpload.objects.create(image=image)

    images = ImageUpload.objects.all()
    return render(request, 'admin_upload.html', {'images': images})

@login_required
def delete_image(request, image_id):
    if not request.user.is_staff:
        return redirect('admin_login')

    ImageUpload.objects.filter(id=image_id).delete()
    return redirect('admin_upload')

