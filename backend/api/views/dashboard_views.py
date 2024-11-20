from django.shortcuts import render
from ..models import Queue

def dashboard_view(request):
    # Filtrando as filas por status
    fila_triagem = Queue.objects.filter(status__in=['pre_triagem', 'triagem']).order_by('date_created')
    fila_atendimento = Queue.objects.filter(status__in=['pre_atendimento', 'em_atendimento']).order_by('date_created')
    fila_pos_atendimento = Queue.objects.filter(status='pos_atendimento').order_by('date_created')

    # Depuração
    print(f"Fila de Triagem: {fila_triagem}")
    print(f"Fila de Atendimento: {fila_atendimento}")
    print(f"Fila de Pós-Atendimento: {fila_pos_atendimento}")

    # Contexto para o template
    context = {
        'fila_triagem': fila_triagem,
        'fila_atendimento': fila_atendimento,
        'fila_pos_atendimento': fila_pos_atendimento,
    }

    return render(request, 'dashboard.html', context)
