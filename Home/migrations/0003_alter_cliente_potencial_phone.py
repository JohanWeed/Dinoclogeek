# Generated by Django 4.1.6 on 2023-03-01 00:12

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Home', '0002_alter_cliente_potencial_phone'),
    ]

    operations = [
        migrations.AlterField(
            model_name='cliente_potencial',
            name='phone',
            field=models.CharField(max_length=20),
        ),
    ]