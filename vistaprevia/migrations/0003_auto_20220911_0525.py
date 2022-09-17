# Generated by Django 3.2.15 on 2022-09-11 05:25

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('vistaprevia', '0002_producto_imagen'),
    ]

    operations = [
        migrations.CreateModel(
            name='Categoria',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.CharField(db_index=True, max_length=100)),
                ('slug', models.SlugField(max_length=100)),
            ],
        ),
        migrations.AddField(
            model_name='producto',
            name='categoria',
            field=models.ManyToManyField(to='vistaprevia.Categoria'),
        ),
    ]
