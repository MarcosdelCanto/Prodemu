# Generated by Django 5.0.6 on 2024-06-20 00:15

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0002_alter_producto_descri_producto'),
    ]

    operations = [
        migrations.AlterField(
            model_name='producto',
            name='img_producto',
            field=models.ImageField(upload_to='static/imagenes'),
        ),
    ]
