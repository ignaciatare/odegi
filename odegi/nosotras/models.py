from django.db import models


class Nosotras(models.Model):
    nombre = models.CharField(max_length=200)
    cargo = models.CharField(max_length=200)
    grado = models.CharField(max_length=200)
    voluntaria = models.BooleanField()


class Meta:
    ordering = ['-nombre']
    db_table = 'Nosotras'
    app_label = 'nosotras'

    def __str__(self):
        return f"{self.nombre}"
