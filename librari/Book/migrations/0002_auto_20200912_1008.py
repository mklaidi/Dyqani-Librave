# Generated by Django 3.1.1 on 2020-09-12 10:08

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('Cart', '0001_initial'),
        ('Book', '0001_initial'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='Book',
            new_name='Liber',
        ),
    ]
