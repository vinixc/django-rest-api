from django.http import JsonResponse
from escola.models import Aluno

def alunos(request):
    if request.method == 'GET':
        alunos = Aluno.objects.all()
        return JsonResponse(alunos)
