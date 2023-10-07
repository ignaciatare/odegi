from django.db import models


ESTATUS = (
    (0, "Borrador"),
    (1, "Publicado")
)

class Glosario(models.Model):
    termino = models.CharField(max_length=200, unique=True)
    slug = models.SlugField(max_length=200, unique=True)
    definicion = models.TextField()
    estatus = models.IntegerField(choices=ESTATUS, default=0)

    def __str__(self):
        return f"{self.termino}"


class Meta:
    ordering = ['-termino']
    db_table = 'Glosario'

