# Generated by Django 4.1.3 on 2022-11-22 06:15

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('loadinput', '0003_allgrid_all_reb'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='allgrid',
            name='bsrm',
        ),
    ]
