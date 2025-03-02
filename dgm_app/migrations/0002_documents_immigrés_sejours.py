# Generated by Django 4.1.7 on 2024-07-23 05:09

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('dgm_app', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Documents',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('num_visa', models.CharField(max_length=30)),
                ('num_carte_id', models.CharField(max_length=30)),
            ],
            options={
                'db_table': 'Documents',
            },
        ),
        migrations.CreateModel(
            name='Immigrés',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nom', models.CharField(max_length=30)),
                ('prenom', models.CharField(max_length=30)),
                ('postnom', models.CharField(max_length=30)),
                ('sexe', models.CharField(max_length=1)),
                ('date_nais', models.DateField()),
                ('nationalite', models.CharField(max_length=50)),
                ('pays_residence', models.CharField(max_length=50)),
                ('adress_residence', models.CharField(max_length=100)),
                ('profession', models.CharField(max_length=30)),
                ('provenance', models.CharField(max_length=30)),
                ('img', models.ImageField(upload_to='photo_immigré')),
            ],
            options={
                'db_table': 'Immigrés',
            },
        ),
        migrations.CreateModel(
            name='Sejours',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('but', models.CharField(max_length=50)),
                ('date_debut', models.DateField()),
                ('date_fin', models.DateField()),
                ('ville', models.CharField(max_length=20)),
            ],
            options={
                'db_table': 'Sejours',
            },
        ),
    ]
