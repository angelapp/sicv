# Generated by Django 3.0.6 on 2020-05-29 04:32

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('web', '0017_auto_20200529_0430'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='cursosemestre',
            name='curso',
        ),
        migrations.AddField(
            model_name='cursosemestre',
            name='semestre',
            field=models.IntegerField(default=1, verbose_name='Semestre'),
        ),
    ]
