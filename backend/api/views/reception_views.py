from django.shortcuts import render, redirect, get_object_or_404
from django.http import JsonResponse
from rest_framework import viewsets
from ..models import Reception, Queue
from ..serializers import ReceptionSerializer
from ..forms import TriagemForm

class ReceptionViewSet(viewsets.ModelViewSet):
    queryset = Reception.objects.all()
    serializer_class = ReceptionSerializer

def pre_triagem_view(request):
    """Renderiza a página com a lista de pacientes aguardando pré-triagem."""
    if request.method == "GET":
        # Busca todos os objetos Queue com status 'pre_triagem'
        queues = Queue.objects.filter(status='pre_triagem').order_by('-date_created')

        # Renderiza o template e passa os dados como contexto
        return render(request, "pre_triagem.html", {"queues": queues})
    else:
        # Para outros métodos, retornar erro
        return JsonResponse({"error": "Método não permitido."}, status=405)
    
def iniciar_triagem_view(request):
    senha = request.GET.get('senha')  # Pega a senha passada na URL
    queue = Queue.objects.get(senha=senha)
    queue.status = 'triagem'  # Altera o status para "triagem"
    queue.save()
    
    # Redireciona para a página de triagem com o ID da fila
    return redirect('ficha_triagem', senha=queue.senha)

def formulario_triagem_view(request, senha):
    queue = get_object_or_404(Queue, senha=senha)
    paciente = queue.pacient  # Obtém o paciente associado à senha
    
    # Se o formulário for enviado, processa os dados
    if request.method == 'POST':
        form = TriagemForm(request.POST)
        if form.is_valid():
            reception = form.save(commit=False)
            reception.queue = queue
            reception.save()

            # Atualiza o status da fila para 'pre-atendimento'
            queue.status = 'pre-atendimento'
            queue.save()

            reception.triagem_finalizada = True
            reception.save()

            return redirect('pre-triagem')  # Redireciona para a dashboard após finalizar triagem
    else:
        form = TriagemForm()

    return render(request, 'ficha_triagem.html', {'form': form, 'paciente': paciente})