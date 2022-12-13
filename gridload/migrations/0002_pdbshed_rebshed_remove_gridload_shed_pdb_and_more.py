# Generated by Django 4.1.3 on 2022-11-17 05:03

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('gridload', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='PDBShed',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('shed_pdb', models.CharField(max_length=20)),
            ],
        ),
        migrations.CreateModel(
            name='REBShed',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('shed_reb', models.CharField(max_length=20)),
            ],
        ),
        migrations.RemoveField(
            model_name='gridload',
            name='shed_pdb',
        ),
        migrations.RemoveField(
            model_name='gridload',
            name='shed_preb',
        ),
    ]