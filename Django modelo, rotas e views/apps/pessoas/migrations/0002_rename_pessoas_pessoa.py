# Generated by Django 4.0.4 on 2022-06-14 21:40

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('receitas', '0001_initial'),
        ('pessoas', '0001_initial'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='Pessoas',
            new_name='Pessoa',
        ),
    ]
