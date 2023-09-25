from django.contrib import admin
from .models import Publicacion


class PublicacionAdmin(admin.ModelAdmin):
    list_display = ('titulo', 'estatus', 'fecha_publicacion')
    list_filter = ('seccion', 'categoria', "estatus",)
    search_fields = ['titulo', 'contenido']
    prepopulated_fields = {'slug': ('titulo',)}


admin.site.register(Publicacion, PublicacionAdmin)
