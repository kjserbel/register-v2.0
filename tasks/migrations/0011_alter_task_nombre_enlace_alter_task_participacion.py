# Generated by Django 5.0.3 on 2024-03-16 19:48

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('tasks', '0010_alter_task_estado_alter_task_municipio_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='task',
            name='nombre_enlace',
            field=models.CharField(choices=[('Vasti_Arana', 'Vasti Arana'), ('Israel_', 'Isrrael'), ('Omar_Castellanos', 'Omar Castellanos'), ('Esther_Castellanos', 'Esther Castellanos')], max_length=250),
        ),
        migrations.AlterField(
            model_name='task',
            name='participacion',
            field=models.CharField(choices=[('Representante de Casilla', 'Representante de Casilla'), ('Representante General', 'Representante General'), ('Movilizador', 'Movilizador'), ('Simpatizante', 'Simpatizante')], max_length=100),
        ),
    ]
