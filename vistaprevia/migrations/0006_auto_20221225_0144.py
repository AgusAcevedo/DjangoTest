# Generated by Django 3.2.15 on 2022-12-25 01:44

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('vistaprevia', '0005_auto_20220913_0647'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='producto',
            name='categoria',
        ),
        migrations.DeleteModel(
            name='Categoria',
        ),
        migrations.DeleteModel(
            name='Producto',
        ),
    ]
