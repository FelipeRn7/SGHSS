# Generated by Django 5.2.2 on 2025-06-06 00:51

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Paciente',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('cpf', models.CharField(max_length=14, unique=True)),
                ('data_nascimente', models.DateField()),
                ('endereco', models.TextField()),
            ],
        ),
    ]
