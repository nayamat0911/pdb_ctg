# Generated by Django 4.1.3 on 2022-11-27 17:15

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('loadinput', '0017_khulshigrid_time'),
    ]

    operations = [
        migrations.CreateModel(
            name='Julda_REB',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Julda_reb', models.PositiveIntegerField()),
            ],
        ),
    ]
