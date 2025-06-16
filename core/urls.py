"""
URL configuration for biblioteca project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from core import views

urlpatterns = [
    path('', views.index, name='index'),
    path('livros/', views.listar_livros, name='listar_livros'),
    path('livros/cadastrar/', views.cadastrar_livro, name='cadastrar_livro'),
    path('livro/<int:livro_id>/', views.detalhes_livro, name='detalhes_livro'),
    path('membros/', views.listar_membros, name='listar_membros'),
    path('membros/cadastrar/', views.cadastrar_membro, name='cadastrar_membro'),
    path('emprestimos/', views.listar_emprestimos, name='listar_emprestimos'),
    path('membro/<str:membro_id>/emprestimos/', views.emprestimos_por_membro, name='emprestimos_por_membro'),
    path('livro/<int:livro_id>/emprestimo/', views.pedir_emprestimo, name='pedir_emprestimo'),
]
