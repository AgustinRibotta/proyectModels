# Generated by Django 4.2.2 on 2023-06-26 10:42

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('lector', '0002_alter_lectormodel_options'),
    ]

    operations = [
        migrations.AlterField(
            model_name='prestamomodel',
            name='fecha_devolucion',
            field=models.DateField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='prestamomodel',
            name='fecha_prstamo',
            field=models.DateField(),
        ),
    ]