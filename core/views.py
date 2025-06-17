from django.shortcuts import render, get_object_or_404, redirect
# from django.http import HttpResponse
# from django.http import HttpResponseRedirect
# from django.urls import reverse
# from .models import Livro, Membro, Emprestimo
from .forms import LivroForm, MembroForm
from django.shortcuts import render, get_object_or_404, redirect
from django.utils import timezone
from datetime import timedelta
from .models import Livro, CopiaDeLivro, Membro, PeriodoEmprestimo, Emprestimo


def index(request):
    return render(request, 'core/index.html')


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


def cadastrar_livro(request):
    if request.method == 'POST':
        form = LivroForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('listar_livros')
    else:
        form = LivroForm()
    return render(request, 'core/cadastrar_livro.html', {'form': form})


def cadastrar_membro(request):
    if request.method == 'POST':
        form = MembroForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('listar_membros')
    else:
        form = MembroForm()
    return render(request, 'core/cadastrar_membro.html', {'form': form})


def listar_emprestimos(request):
    emprestimos = Emprestimo.objects.all()
    return render(request, 'core/listar_emprestimos.html', {'emprestimos': emprestimos})


def detalhes_livro(request, livro_id):
    livro = get_object_or_404(Livro, id=livro_id)
    return render(request, 'core/detalhes_livro.html', {'livro': livro})


def pedir_emprestimo(request, livro_id):
    livro = get_object_or_404(Livro, id=livro_id)
    membros = Membro.objects.all()

    # Buscar cópias do livro que não estão com empréstimo ativo
    copias_disponiveis = [
        copia for copia in CopiaDeLivro.objects.filter(livro=livro)
        if not Emprestimo.objects.filter(copia=copia, status='ativo').exists()
    ]

    if request.method == 'POST':
        membro_id = request.POST.get('membro')
        membro = get_object_or_404(Membro, id=membro_id)

        if copias_disponiveis:
            copia = copias_disponiveis[0]

            periodo = PeriodoEmprestimo.objects.create(
                data_inicio=timezone.now().date(),
                data_fim=timezone.now().date() + timedelta(days=7)  # Exemplo: 7 dias de prazo
            )

            Emprestimo.objects.create(
                membro=membro,
                copia=copia,
                periodo=periodo,
                status='ativo'  # Lembre de ter um campo status no modelo Emprestimo
            )

            return redirect('listar_emprestimos')
        else:
            return render(request, 'core/pedir_emprestimo.html', {
                'livro': livro,
                'membros': membros,
                'erro': 'Nenhuma cópia disponível.'
            })

    return render(request, 'core/pedir_emprestimo.html', {
        'livro': livro,
        'membros': membros
    })
