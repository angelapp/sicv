# Generated by Django 3.0.6 on 2020-05-27 04:10

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('web', '0006_auto_20200527_0326'),
    ]

    operations = [
        migrations.AlterField(
            model_name='programa',
            name='codigo',
            field=models.CharField(default='1', max_length=30, verbose_name='Código'),
            preserve_default=False,
        ),
    ]
