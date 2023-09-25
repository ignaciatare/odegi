from django.db import models
from django.contrib.auth.models import User


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
CATEGORIAS = (
    ('violencia', 'Violencia'),
    ('derechos_repr', 'Derechos Reproductivos'),
    ('deportes', 'Deportes'),
    ('moda', 'Moda'),
    ('ddhh', 'Derechos Humanos'),
    ('interseccionalidad', 'Interseccionalidad'),
    ('trabajo', 'Trabajo'),
    ('educacion', 'Educación'),
    ('salud', 'Salud'),
    ('seguridad', 'Seguridad'),
    ('tecnologia', 'Tecnología'),
    ('economia', 'Economía'),
    ('participacion', 'Participación política'),
)


class Publicacion(models.Model):
    titulo = models.CharField(max_length=200, unique=True)
    slug = models.SlugField(max_length=200, unique=True)
    #author = models.ForeignKey(User, on_delete= models.CASCADE, related_name='publicaciones')
    extracto = models.TextField()
    categoria = models.CharField(
    max_length=20,
    choices=CATEGORIAS,
    default='tecnologia',
        )
    contenido = models.TextField()
    fecha_publicacion = models.DateTimeField(auto_now_add=True)
    estatus = models.IntegerField(choices=ESTATUS, default=0)
    destacado = models.BooleanField()
    seccion = models.IntegerField(choices=SECCION, default=0)
    imagen_principal = models.ImageField()
    imagen2 = models.ImageField(blank=True)
    imagen3 = models.ImageField(blank=True)
    imagen4 = models.ImageField(blank=True)
    imagen5 = models.ImageField(blank=True)


class Meta:
    ordering = ['-fecha_publicacion']
    db_table = 'Publicacion'
