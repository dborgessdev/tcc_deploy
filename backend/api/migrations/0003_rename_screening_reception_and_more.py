# Generated by Django 5.1.2 on 2024-11-05 15:53

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0002_doctor_alter_pacient_options_and_more'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='Screening',
            new_name='Reception',
        ),
        migrations.RenameField(
            model_name='reception',
            old_name='data_screening',
            new_name='data_reception',
        ),
    ]
