# Generated by Django 2.2.1 on 2019-06-08 04:14

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('usuario', '0002_auto_20190607_1137'),
        ('viagem', '0009_auto_20190608_0103'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='patrocinio',
            name='patreon',
        ),
        migrations.AddField(
            model_name='patrocinio',
            name='patrocinador',
            field=models.ForeignKey(default='', on_delete=django.db.models.deletion.PROTECT, related_name='patrocinador_opened', to='usuario.Usuario'),
        ),
    ]
