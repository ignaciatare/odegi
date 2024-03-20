from django.shortcuts import render
from odegi.odegiblog.models import Publicacion, Categoria, Autora

def homepage(request):
    destacado = Publicacion.objects.filter(estatus=1).filter(destacado=True).order_by('-fecha_publicacion')[:1]
    publicaciones = Publicacion.objects.filter(estatus=1).order_by('-fecha_publicacion')[:6]
    colores = ['#ECA0ED', '#B5D2EA', '#FFDBBC', '#FF895A']
    context = {
        'destacado': destacado,
        'publicaciones': publicaciones,
        'colores': colores,
    }
    return render(request, "home.html", context)

def datoteca(request):
    # Consulta para obtener el último post
    fila1 = Publicacion.objects.filter(estatus=1).filter(seccion=1).order_by('-fecha_publicacion')[:1]
    # Consulta para obtener el penúltimo y antepenúltimo post
    fila2 = Publicacion.objects.filter(estatus=1).filter(seccion=1).order_by('-fecha_publicacion')[1:3]
    # Consulta para obtener el resto de los posts (fila 3 en adelante)
    filax = Publicacion.objects.filter(estatus=1).filter(seccion=1).order_by('-fecha_publicacion')[3:]

    lista_categorias = Categoria.objects.all()
    colores_datoteca = ['#ECA0ED', '#B5D2EA', '#FFDBBC', '#FF895A']
    num_publicaciones_por_carga = 6

    start = request.GET.get('start')
    if start is not None:
        try:
            start = int(start)
        except ValueError:
            # Manejar el caso en el que start no sea un número válido
            start = 0  # O cualquier otro valor predeterminado que desees
    else:
        start = 0  # Establece un valor predeterminado si start no se proporciona en la URL

    end = start + num_publicaciones_por_carga
    fila3_en_adelante = filax[start:end]

    context = {
        'fila1': fila1,
        'fila2': fila2,
        'filax': filax,
        'fila3_en_adelante': fila3_en_adelante,
        'lista_categorias': lista_categorias,
        'colores': colores_datoteca,
    }

    return render(request, "datoteca.html", context)

def publicacion(request, slug):
    publicacion = Publicacion.objects.filter(estatus=1).get(slug=slug)
    odegi_blog = Publicacion.objects.filter(estatus=1)[:3]
    colores = ['#ECA0ED', '#B5D2EA', '#FFDBBC', '#FF895A']

    context = {
        'publicacion': publicacion,
        'odegi_blog': odegi_blog,
        'colores': colores,
    }
    return render(request, 'publicacion.html', context)



def nuestra_historia(request):
    colores = ['#ECA0ED', '#B5D2EA', '#FFDBBC', '#FF895A']
    context = {
        'colores': colores,
    }
    return render(request, 'nuestra_historia.html', context)


def posts_por_categoria(request, categoria_nombre):
    categoria = Categoria.objects.get(nombre=categoria_nombre)
    posts = Publicacion.objects.filter(categoria=categoria, estatus=1).order_by('-fecha_publicacion')

    context = {
        'categoria': categoria,
        'posts': posts,
    }

    return render(request, 'posts_por_categoria.html', context)

def blog(request):
    odegi_blog = Publicacion.objects.filter(estatus=1).filter(seccion=0).order_by('-fecha_publicacion')
    lista_categorias = Categoria.objects.all()
    colores = ['#ECA0ED', '#B5D2EA', '#FFDBBC', '#FF895A']

    context = {
        'odegi_blog': odegi_blog,
        'lista_categorias': lista_categorias,
        'colores': colores,
    }
    return render(request, "blog.html", context)

def proyectos(request):
    nuestros_proyectos = Publicacion.objects.filter(estatus=1).filter(seccion=3).order_by('-fecha_publicacion')[:3]
    herramientas = Publicacion.objects.filter(estatus=1).filter(seccion=2).order_by('-fecha_publicacion')
    context = {
        'proyectos': nuestros_proyectos,
        'herramientas': herramientas,
    }
    return render(request, "nuestro_trabajo.html", context)

def buscar_publicaciones(request):
    query = request.GET.get('q')  # Obtener la consulta del usuario desde la URL
    resultados = Publicacion.objects.filter(titulo__icontains=query)  # Realizar la búsqueda

    context = {
        'resultados': resultados,
        'query': query,
    }

    return render(request, 'buscar.html', context)


def transparencia(request):
    return render(request, 'transparencia.html')
