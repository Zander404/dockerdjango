# Generated by Django 3.1.2 on 2022-04-25 00:58

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('formulario', '0003_auto_20220424_2256'),
    ]

    operations = [
        migrations.AlterField(
            model_name='agencia',
            name='tipo_telefone',
            field=models.CharField(choices=[('0', 'Celular'), ('1', 'Fixo')], max_length=1),
        ),
    ]