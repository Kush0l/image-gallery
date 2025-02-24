from django.contrib import admin
from django.utils.html import format_html
from .models import CustomUser, ImageUpload

# Display Images in Django Admin
class ImageUploadAdmin(admin.ModelAdmin):
    list_display = ('id', 'image_preview', 'uploaded_at')
    search_fields = ('image',)
    list_filter = ('uploaded_at',)

    def image_preview(self, obj):
        return format_html('<img src="{}" width="100" height="100"/>', obj.image.url)
    
    image_preview.short_description = 'Image Preview'

# Register models
admin.site.register(CustomUser)
admin.site.register(ImageUpload, ImageUploadAdmin)
