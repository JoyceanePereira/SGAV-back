from django.db import models
from django.contrib.auth.models import User

<<<<<<< HEAD
from django.conf import settings


class Perfil(models.Model):
    nome = models.CharField(max_length=200, verbose_name='Nome do usuário')
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
=======
#class Login(models.Model):
    #user = models.ForeignKey(User, on_delete=models.CASCADE)
>>>>>>> bcbc6c0f90a7058cc511579e7829f8a0fb4899da

