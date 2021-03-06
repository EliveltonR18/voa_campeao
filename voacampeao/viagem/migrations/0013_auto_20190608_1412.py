# Generated by Django 2.2.1 on 2019-06-08 17:12

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('viagem', '0012_auto_20190608_1358'),
    ]

    operations = [
        migrations.AlterField(
            model_name='patrocinio',
            name='status_pat',
            field=models.CharField(choices=[('1', 'PENDENTE'), ('2', 'ENVIADO'), ('3', 'CONFIRMADO'), ('4', 'RECUSADO')], default=1, max_length=1),
        ),
        migrations.AlterField(
            model_name='viagem',
            name='status',
            field=models.CharField(choices=[('1', 'EM AVALIAÇÃO'), ('2', 'ABERTO'), ('3', 'EM PATROCINIO'), ('4', 'PATROCINADA'), ('5', 'VENCIDA')], default=1, max_length=1),
        ),
    ]
