# Generated by Django 5.0.4 on 2024-05-01 16:59

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='libro',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('titulo', models.CharField(max_length=100, verbose_name='Titulo')),
                ('image', models.ImageField(null=True, upload_to='imagenes/', verbose_name='imagen')),
                ('description', models.TextField(null=True, verbose_name='Descripcion')),
            ],
        ),
    ]
