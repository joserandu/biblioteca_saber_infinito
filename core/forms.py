from django import forms
from .models import Livro, Membro


class LivroForm(forms.ModelForm):
    class Meta:
        model = Livro
        fields = ['titulo', 'autores', 'isbn', 'numero_copias']


class MembroForm(forms.ModelForm):
    class Meta:
        model = Membro
        fields = ['nome', 'cpf', 'email', 'contato', 'endereco']