# Generated by Django 4.1.6 on 2023-02-28 23:35

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Home', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='cliente_potencial',
            name='phone',
            field=models.CharField(max_length=10),
        ),
    ]
