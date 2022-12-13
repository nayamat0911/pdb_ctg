# Generated by Django 4.1.3 on 2022-11-26 10:12

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('loadinput', '0010_alter_madunaghatgrid_grid_load_and_more'),
    ]

    operations = [
        migrations.CreateModel(
            name='Chandroghuna_reb',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('shed_pdb', models.PositiveIntegerField()),
                ('reb_shed', models.PositiveIntegerField()),
            ],
        ),
        migrations.AlterField(
            model_name='chandroghunagrid',
            name='grid_load',
            field=models.PositiveIntegerField(),
        ),
        migrations.AlterField(
            model_name='chandroghunagrid',
            name='reb_shed',
            field=models.PositiveIntegerField(),
        ),
        migrations.AlterField(
            model_name='chandroghunagrid',
            name='shed_pdb',
            field=models.PositiveIntegerField(),
        ),
        migrations.AlterField(
            model_name='madunaghat_reb',
            name='grid',
            field=models.ForeignKey(default=True, on_delete=django.db.models.deletion.CASCADE, to='loadinput.madunaghatgrid'),
        ),
    ]
