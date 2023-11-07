from django.db import models

# Create your models here.

def upload_location(instance, filename):
    return f'fotos/{filename}'

class Integrante(models.Model):
    nome = models.CharField(max_length=100)
    TIPO_CHOICES = (
        ('Iniciação Científica', 'Iniciação Científica'),
        ('Mestrando', 'Mestrando'),
        ('Doutorando', 'Doutorando'),
        ('Pós-doutorando', 'Pós-doutorando'),
        ('Professor', 'Professor'),
    )
    tipo = models.CharField(max_length=20, choices=TIPO_CHOICES)
    foto = models.ImageField(upload_to=upload_location)

    def __str__(self):
        return self.nome

class Publicacao(models.Model):
    integrante = models.ForeignKey(Integrante, on_delete=models.CASCADE, related_name='publicacoes')
    titulo = models.CharField(max_length=200)
    ano_publicacao = models.PositiveIntegerField()
    onde_publicado = models.CharField(max_length=200)
    autores = models.TextField()

    class Meta:
        verbose_name_plural = "Publicações"

    def __str__(self):
        return f"{self.titulo} ({self.ano_publicacao})"

    def get_autores_list(self):
        return self.autores.split(',')

    def autores_as_string(self):
        return ", ".join(self.get_autores_list())


class GrupoPesquisa(models.Model):
    nome = models.CharField(max_length=100)
    descricao = models.TextField()
    
    
    
