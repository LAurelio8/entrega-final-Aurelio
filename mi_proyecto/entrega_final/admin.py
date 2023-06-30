from django.contrib import admin
from .models import Photo, Text
from django.contrib.admin import ModelAdmin

class CustomModelAdmin(ModelAdmin):
    def has_add_permission(self, request):
        # Solo los usuarios con permisos de administrador pueden agregar fotos y textos
        return request.user.is_superuser
    
    def has_delete_permission(self, request, obj=None):
        # Solo los usuarios con permisos de administrador pueden eliminar fotos y textos
        return request.user.is_superuser


@admin.register(Photo)
class PhotoAdmin(CustomModelAdmin):
    pass

@admin.register(Text)
class TextAdmin(CustomModelAdmin):
    pass
