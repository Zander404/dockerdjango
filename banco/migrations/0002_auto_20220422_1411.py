# Generated by Django 3.1.2 on 2022-04-22 14:11

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('banco', '0001_initial'),
    ]

    operations = [
        migrations.DeleteModel(
            name='Agencia',
        ),
        migrations.RemoveField(
            model_name='banco',
            name='pk_banco',
        ),
        migrations.AddField(
            model_name='banco',
            name='cep',
            field=models.SmallIntegerField(default=0),
        ),
        migrations.AddField(
            model_name='banco',
            name='cod',
            field=models.SmallIntegerField(default=0),
        ),
        migrations.AddField(
            model_name='banco',
            name='name',
            field=models.TextField(default='', max_length=100),
        ),
    ]
