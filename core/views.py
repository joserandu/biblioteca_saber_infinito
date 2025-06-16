from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse
from .models import Livro, Membro, Emprestimo


def listar_livros(request):
    livros = Livro.objects.all()
    return render(request, 'core/listar_livros.html', {'livros': livros})


def detalhes_livro(request, livro_id):
    livro = get_object_or_404(Livro, id=livro_id)
    return render(request, 'core/detalhes_livro.html', {'livro': livro})


def listar_membros(request):
    membros = Membro.objects.all()
    return render(request, 'core/listar_membros.html', {'membros': membros})


def emprestimos_por_membro(request, membro_id):
    membro = get_object_or_404(Membro, id_membro=membro_id)
    emprestimos = Emprestimo.objects.filter(membro=membro)
    return render(request, 'core/emprestimos_por_membro.html', {'membro': membro, 'emprestimos': emprestimos})
