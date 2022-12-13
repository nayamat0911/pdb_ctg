# Generated by Django 4.1.3 on 2022-11-25 04:12

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('loadinput', '0005_bakliagrid_halishahorgrid_hathazarigrid_and_more'),
    ]

    operations = [
        migrations.CreateModel(
            name='Chandroghuna',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('grid_load', models.CharField(max_length=20)),
                ('shed_pdb', models.CharField(max_length=20)),
                ('reb_shed', models.CharField(max_length=20)),
            ],
        ),
        migrations.CreateModel(
            name='CoxBazar',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('grid_load', models.CharField(max_length=20)),
                ('shed_pdb', models.CharField(max_length=20)),
                ('reb_shed', models.CharField(max_length=20)),
            ],
        ),
        migrations.CreateModel(
            name='Duhazari',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('grid_load', models.CharField(max_length=20)),
                ('shed_pdb', models.CharField(max_length=20)),
                ('reb_shed', models.CharField(max_length=20)),
            ],
        ),
        migrations.CreateModel(
            name='Matarbari',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('grid_load', models.CharField(max_length=20)),
                ('shed_pdb', models.CharField(max_length=20)),
                ('reb_shed', models.CharField(max_length=20)),
            ],
        ),
        migrations.AlterField(
            model_name='khulshigrid',
            name='BSRM',
            field=models.CharField(max_length=20),
        ),
        migrations.AlterField(
            model_name='khulshigrid',
            name='grid_load',
            field=models.CharField(max_length=20),
        ),
        migrations.AlterField(
            model_name='khulshigrid',
            name='shed_pdb',
            field=models.CharField(max_length=20),
        ),
    ]
