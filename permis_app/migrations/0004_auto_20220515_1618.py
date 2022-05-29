# Generated by Django 3.2 on 2022-05-15 16:18

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('permis_app', '0003_alter_demande_employeur'),
    ]

    operations = [
        migrations.AlterField(
            model_name='demande',
            name='avis',
            field=models.CharField(blank=True, max_length=250, null=True),
        ),
        migrations.AlterField(
            model_name='demande',
            name='dateDeDelivrance',
            field=models.DateTimeField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='demande',
            name='dateExpiration',
            field=models.DateTimeField(blank=True, null=True),
        ),
    ]