# Generated by Django 5.1.2 on 2024-11-17 13:38

import django.db.models.deletion
import django.utils.timezone
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0002_service_doctor_service_pacient_service_queue_and_more'),
    ]

    operations = [
        migrations.CreateModel(
            name='Consultation',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_at', models.DateTimeField(auto_now_add=True, verbose_name='Criado em')),
                ('updated_at', models.DateTimeField(auto_now=True, verbose_name='Atualizado em')),
                ('disponivel', models.BooleanField(default=True, verbose_name='Disponível')),
                ('start_time', models.DateTimeField(default=django.utils.timezone.now, verbose_name='Início do Atendimento')),
                ('end_time', models.DateTimeField(blank=True, null=True, verbose_name='Término do Atendimento')),
                ('final_status', models.CharField(blank=True, choices=[('alta', 'Alta'), ('enfermaria', 'Enfermaria'), ('internamento', 'Internamento')], max_length=20, null=True, verbose_name='Status Final')),
                ('observations', models.TextField(blank=True, null=True, verbose_name='Observações')),
                ('doctor', models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, related_name='consultations', to='api.doctor')),
                ('pacient', models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, related_name='consultations', to='api.pacient')),
                ('queue', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='consultations', to='api.queue')),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.DeleteModel(
            name='Service',
        ),
    ]
