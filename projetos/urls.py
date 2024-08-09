from django.urls import path

from projetos.views import home

urlpatterns = [
    path("", home),
]
