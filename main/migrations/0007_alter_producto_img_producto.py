# Generated by Django 5.0.6 on 2024-06-26 16:46

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0006_alter_detalle_carro_options_alter_orden_options_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='producto',
            name='img_producto',
            field=models.ImageField(blank=True, upload_to='productos'),
        ),
    ]
