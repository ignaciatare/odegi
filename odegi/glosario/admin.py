from django.contrib import admin
from .models import Glosario

class GlosarioAdmin(admin.ModelAdmin):
    list_display = ('termino', 'estatus')
    list_filter = ('termino', "estatus")
    search_fields = ['termino', 'definicion']
    prepopulated_fields = {'slug': ('termino',)}
admin.site.register(Glosario, GlosarioAdmin)
