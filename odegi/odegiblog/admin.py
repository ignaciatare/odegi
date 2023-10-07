from django.contrib import admin
from .models import Publicacion, Autora, Categoria


class PublicacionAdmin(admin.ModelAdmin):
    list_display = ('titulo', 'estatus', 'fecha_publicacion')
    list_filter = ("seccion", "estatus", "destacado")
    search_fields = ['titulo', 'contenido']
    prepopulated_fields = {'slug': ('titulo',)}
admin.site.register(Publicacion, PublicacionAdmin)


class AutoraAdmin(admin.ModelAdmin):
    list_display = ['nombre']
    search_fields = ['nombre', 'descripcion']
admin.site.register(Autora, AutoraAdmin)

class CategoriaAdmin(admin.ModelAdmin):
    list_display = ['nombre']
    search_fields = ['nombre', 'descripcion']
admin.site.register(Categoria, CategoriaAdmin)
