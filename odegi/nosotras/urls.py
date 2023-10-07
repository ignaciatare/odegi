from django.urls import path
from . import views

app_name = "nosotras"
urlpatterns = [
    path('nosotras/', views.equipoodegi, name="nosotras"),
]
