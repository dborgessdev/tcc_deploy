# Generated by Django 5.1.2 on 2024-11-17 21:07

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0004_remove_nurse_registration_number_nurse_coren_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='nurse',
            name='coren',
            field=models.CharField(max_length=20),
        ),
        migrations.AlterField(
            model_name='nurse',
            name='disponivel',
            field=models.BooleanField(default=True),
        ),
        migrations.AlterField(
            model_name='nurse',
            name='sector',
            field=models.CharField(blank=True, max_length=100, null=True),
        ),
    ]
