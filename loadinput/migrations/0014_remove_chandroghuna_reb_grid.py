# Generated by Django 4.1.3 on 2022-11-26 10:39

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('loadinput', '0013_chandroghuna_reb_grid'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='chandroghuna_reb',
            name='grid',
        ),
    ]