from django.urls import path
from . import views

urlpatterns = [
    path('nuestro_trabajo/', views.glosario, name="nuestro_trabajo"),
]
