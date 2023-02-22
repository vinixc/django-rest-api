from django.contrib import admin
from escola.models import Aluno,Curso

class Alunos(admin.ModelAdmin):
    list_display = ("id","nome",'rg','cpf','data_nascimento')
    list_display_links = ('id','nome')
    search_fields = ('nome',)
    list_per_page = 10

admin.site.register(Aluno, Alunos)


class Cursos(admin.ModelAdmin):
    list_display = ("id","codigo_curso",'descricao','nivel')
    list_display_links = ('id','descricao')
    search_fields = ('descricao',)
    list_per_page = 10

admin.site.register(Curso, Cursos)
