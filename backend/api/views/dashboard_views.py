from django.shortcuts import render
from ..models import Queue

def dashboard_view(request):
    fila_atendimento = Queue.objects.filter(status='geral').order_by('created_at')
    fila_triagem = Queue.objects.filter(status='triagem').order_by('created_at')
    fila_pos_atendimento = Queue.objects.filter(status='pos_atendimento').order_by('created_at')
    fila_em_atendimento = Queue.objects.filter(status='em_atendimento').order_by('created_at')

    context = {
        'fila_atendimento': fila_atendimento,
        'fila_triagem': fila_triagem,
        'fila_pos_atendimento': fila_pos_atendimento,
        'fila_em_atendimento': fila_em_atendimento,
    }

    return render(request, 'dashboard.html', context)
