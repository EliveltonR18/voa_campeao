# Generated by Django 2.2.1 on 2019-06-08 03:33

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('viagem', '0004_auto_20190607_2047'),
    ]

    operations = [
        migrations.AlterField(
            model_name='viagem',
            name='patrocinador',
            field=models.ForeignKey(default='', on_delete=django.db.models.deletion.PROTECT, related_name='patrocinador_conf', to='usuario.Usuario'),
        ),
    ]
