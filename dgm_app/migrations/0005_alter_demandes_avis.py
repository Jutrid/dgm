# Generated by Django 4.1.7 on 2024-07-23 16:53

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('dgm_app', '0004_alter_demandes_avis'),
    ]

    operations = [
        migrations.AlterField(
            model_name='demandes',
            name='avis',
            field=models.CharField(max_length=1),
        ),
    ]
