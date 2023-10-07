from django.contrib import admin
from .models import Nosotras


class NosotrasAdmin(admin.ModelAdmin):
    list_display = ['nombre', 'cargo']
    list_filter = ['nombre', 'voluntaria']
    search_fields = ['nombre', 'cargo', 'grado']
admin.site.register(Nosotras, NosotrasAdmin)



