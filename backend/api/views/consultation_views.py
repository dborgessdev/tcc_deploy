from django.http import JsonResponse
from django.shortcuts import get_object_or_404, redirect, render
from rest_framework import viewsets

from ..forms import ConsultaForm
from ..models import Consultation, Queue
from ..serializers import ConsultationSerializer

class ConsultationViewSet(viewsets.ModelViewSet):
    queryset = Consultation.objects.all()
    serializer_class = ConsultationSerializer

def pre_consulta_view(request):
    """Renderiza a página com a lista de pacientes aguardando atendimento."""
    if request.method == "GET":
        # Busca todos os objetos Queue com status 'pre_atendimento'
        queues = Queue.objects.filter(status='pre_atendimento').order_by('-date_created')

        # Renderiza o template e passa os dados como contexto
        return render(request, "pre_atendimento.html", {"queues": queues})
    else:
        # Para outros métodos, retornar erro
        return JsonResponse({"error": "Método não permitido."}, status=405)
    
def iniciar_consulta_view(request):
    senha = request.GET.get('senha')  # Pega a senha passada na URL
    queue = Queue.objects.get(senha=senha)
    queue.status = 'em_atendimento'  # Altera o status para "em_atendimento"
    queue.save()
    # Redireciona para a página de consulta com o ID da fila
    return redirect('ficha_consulta', senha=queue.senha)

def formulario_consulta_view(request, senha):
    queue = get_object_or_404(Queue, senha=senha)
    paciente = queue.pacient  # Obtém o paciente associado à senha
    
    # Se o formulário for enviado, processa os dados
    if request.method == 'POST':
        form = ConsultaForm(request.POST)
        if form.is_valid():
            consultation = form.save(commit=False)
            consultation.queue = queue
            consultation.save()

            # Atualiza o status da fila para 'pre-atendimento'
            queue.status = 'pos_atendimento'
            queue.save()
            consultation.consulta_finalizada = True
            consultation.save()

            return redirect('/api/pre-consulta/')  
    else:
        form = ConsultaForm()

    return render(request, 'ficha_consulta.html', {'form': form, 'paciente': paciente})