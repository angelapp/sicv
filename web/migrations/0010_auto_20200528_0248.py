# Generated by Django 3.0.6 on 2020-05-28 02:48

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('web', '0009_usuario_edad'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='cursousuario',
            name='programa',
        ),
        migrations.AddField(
            model_name='cursousuario',
            name='curso',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='web.Curso', verbose_name='Curso'),
        ),
        migrations.AddField(
            model_name='programa',
            name='imagen',
            field=models.ImageField(help_text='80x80', max_length=255, null=True, upload_to='imagenes_programas/', verbose_name='Imagen del programa'),
        ),
    ]
