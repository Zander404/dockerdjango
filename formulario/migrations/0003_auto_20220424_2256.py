# Generated by Django 3.1.2 on 2022-04-24 22:56

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('formulario', '0002_auto_20220424_2123'),
    ]

    operations = [
        migrations.AlterField(
            model_name='agencia',
            name='tipo_telefone',
            field=models.CharField(choices=[('1', 'Fixo'), ('0', 'Celular')], max_length=1),
        ),
    ]
