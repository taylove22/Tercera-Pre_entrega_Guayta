# Generated by Django 4.2.4 on 2023-09-01 06:31

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Trainingzone', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Profesores',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.CharField(max_length=50)),
                ('Email', models.EmailField(max_length=254)),
            ],
        ),
        migrations.DeleteModel(
            name='Entrenadores',
        ),
    ]