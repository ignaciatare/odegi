from django.urls import path
from . import views

app_name = "glosario"
urlpatterns = [
    path('', views.glosario, name="nuestro_trabajo"),
]
