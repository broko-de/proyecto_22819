from django.urls import path
from . import views

urlpatterns = [
    path('hola_mundo',views.hola_mundo),
]