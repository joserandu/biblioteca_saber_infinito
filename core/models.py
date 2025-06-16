from django.db import models
from django.utils import timezone


# Objetos de valor
class ISBN(models.Model):
    numero = models.CharField(max_length=13, unique=True)

    def __str__(self):
        return self.numero


class EnderecoMembro(models.Model):
    rua = models.CharField(max_length=100)
    cidade = models.CharField(max_length=50)
    estado = models.CharField(max_length=30)
    cep = models.CharField(max_length=10)

    def __str__(self):
        return f"{self.rua}, {self.cidade} - {self.estado}, {self.cep}"


class PeriodoEmprestimo(models.Model):
    data_inicio = models.DateField()
    data_fim = models.DateField()

    def __str__(self):
        return f"{self.data_inicio} a {self.data_fim}"


# Entidades e agregados
class Livro(models.Model):
    titulo = models.CharField(max_length=200)
    autores = models.CharField(max_length=200)
    isbn = models.CharField(max_length=15, unique=True)
    numero_copias = models.PositiveIntegerField(default=1)

    def __str__(self):
        return f"{self.titulo} ({self.isbn})"

    def copias_disponiveis(self):
        return self.copiadelivro_set.filter(status='disponivel').count()


class CopiaDeLivro(models.Model):
    STATUS_CHOICES = [
        ('disponivel', 'Disponível'),
        ('emprestado', 'Emprestado'),
        ('manutencao', 'Em manutenção'),
    ]
    livro = models.ForeignKey(Livro, on_delete=models.CASCADE)
    status = models.CharField(max_length=20, choices=STATUS_CHOICES, default='disponivel')

    def __str__(self):
        return f"Cópia de {self.livro.titulo} - {self.get_status_display()}"


class Membro(models.Model):
    nome = models.CharField(max_length=100)
    cpf = models.CharField(max_length=11, unique=True)
    contato = models.CharField(max_length=100)
    endereco = models.CharField(max_length=200, null=True, blank=True)
    email = models.CharField(max_length=100)

    def __str__(self):
        return f"{self.nome} ({self.cpf})"


class Emprestimo(models.Model):
    membro = models.ForeignKey(Membro, on_delete=models.CASCADE)
    copia = models.ForeignKey(CopiaDeLivro, on_delete=models.CASCADE)
    periodo = models.OneToOneField(PeriodoEmprestimo, on_delete=models.CASCADE)
    data_devolucao_real = models.DateField(null=True, blank=True, default=timezone.now)

    def esta_atrasado(self):
        if not self.data_devolucao_real and timezone.now().date() > self.periodo.data_fim:
            return True
        return False

    def __str__(self):
        return f"{self.membro} -> {self.copia} ({self.periodo})"
