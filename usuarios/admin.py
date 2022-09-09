from django.contrib import admin

from usuarios.models import Perfil, Tarefas

# Register your models here.
admin.site.register(Perfil) 
admin.site.register(Tarefas)
