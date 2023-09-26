from django.urls import path
from . import views

urlpatterns = [
    path('', views.principal, name='principal'),
    path('livros', views.livros, name='livros'),  #linha adicionada
    path('tccs', views.tccs, name='tccs'),
    path('tccs/detalhes/<int:id>', views.tcc_detalhes, name='tcc_detalhes'),# linha adicionado
]