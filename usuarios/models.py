from django.db import models
from django.contrib.auth.models import User

from django.conf import settings


class Perfil(models.Model):
    nome = models.CharField(max_length=200, verbose_name='Nome do usuário')
    colocacao = models.IntegerField(verbose_name='Colocação')
    tempo_empresa = models.CharField(max_length=100, verbose_name='Tempo de empresa')
    telefone = models.CharField(max_length=20, verbose_name='Telefone')
    cargo = models.CharField(max_length=50, verbose_name='Cargo')
    foto_perfil = models.ImageField(verbose_name='Foto de Perfil', upload_to='fotos/', blank=True)
    user = models.OneToOneField(
        settings.AUTH_USER_MODEL,
        on_delete=models.CASCADE,
        default=None,
        null=True,
    )

    def __str__(self):
        return self.nome

class Tarefas(models.Model):
    tarefa = models.TextField()
    user = models.ForeignKey(Perfil, on_delete=models.CASCADE)

