# Generated by Django 4.2.1 on 2023-05-22 17:13

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('publicaciones', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='edicionpublicacion',
            name='imagen_nueva',
            field=models.ImageField(default='publicaciones/img/default-public.jpg', upload_to='publicaciones/'),
        ),
        migrations.AddField(
            model_name='edicionpublicacion',
            name='titulo_nuevo',
            field=models.CharField(default='Valor predeterminado', max_length=200),
        ),
    ]