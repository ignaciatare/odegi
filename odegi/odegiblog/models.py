from django.db import models


class Autora(models.Model):
    nombre = models.CharField(max_length=200)
    descripcion = models.TextField(blank=True)
    avatar = models.ImageField(blank=True)
    link = models.URLField(blank=True)

    def __str__(self):
        return f"{self.nombre}"

class Categoria(models.Model):
    nombre = models.CharField(max_length=200)
    descripcion = models.TextField(blank=True)

    def __str__(self):
        return f"{self.nombre}"


ESTATUS = (
    (0,"Borrador"),
    (1,"Publicado")
)
SECCION = (
    (0, "Blog"),
    (1, "Datoteca"),
    (2, "Heramientas"),
    (3, "Proyectos"),
)


class Publicacion(models.Model):
    titulo = models.CharField(max_length=200, unique=True)
    slug = models.SlugField(max_length=200, unique=True)
    autora = models.ManyToManyField(Autora)
    extracto = models.TextField()
    categoria = models.ManyToManyField(Categoria)
    contenido = models.TextField()
    fecha_publicacion = models.DateTimeField(auto_now_add=True)
    estatus = models.IntegerField(choices=ESTATUS, default=0)
    destacado = models.BooleanField()
    seccion = models.IntegerField(choices=SECCION, default=0)
    link = models.URLField(blank=True)
    imagen_principal = models.ImageField()
    imagen2 = models.ImageField(blank=True)
    imagen3 = models.ImageField(blank=True)
    imagen4 = models.ImageField(blank=True)
    imagen5 = models.ImageField(blank=True)

class Meta:
    ordering = ['-fecha_publicacion']
    db_table = 'Publicacion'

    def __str__(self):
        return f"{self.titulo}"
