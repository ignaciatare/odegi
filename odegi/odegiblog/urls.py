from django.urls import path
from . import views

app_name = "odegiblog"
urlpatterns = [
    path('', views.homepage, name="home"),
    path('datoteca/', views.datoteca, name="datoteca"),
    path('buscar/', views.buscar_publicaciones, name='buscar_publicaciones'),
    path('categoria/<str:categoria_nombre>/', views.posts_por_categoria, name='posts_por_categoria'),
    path('publicacion/<slug:slug>/', views.publicacion, name='ver_publicacion'),
    path('transparencia', views.transparencia)
]
