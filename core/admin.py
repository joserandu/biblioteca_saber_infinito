from django.contrib import admin
from .models import Livro, CopiaDeLivro, Membro, Emprestimo, ISBN, EnderecoMembro, PeriodoEmprestimo

admin.site.register(Livro)
admin.site.register(CopiaDeLivro)
admin.site.register(Membro)
admin.site.register(Emprestimo)
admin.site.register(ISBN)
admin.site.register(EnderecoMembro)
admin.site.register(PeriodoEmprestimo)
