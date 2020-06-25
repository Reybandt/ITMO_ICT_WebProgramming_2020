# Generated by Django 3.0.4 on 2020-06-23 22:10

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('flight_board', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='airlinecompany',
            name='logo',
        ),
        migrations.AlterField(
            model_name='employee',
            name='flight',
            field=models.ManyToManyField(related_name='passengers', to='flight_board.Flight', verbose_name='Рейс(-ы)'),
        ),
    ]