# Generated by Django 3.2 on 2022-05-26 13:30

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('permis_app', '0013_alter_permis_typepermis'),
    ]

    operations = [
        migrations.AlterField(
            model_name='demande',
            name='etatRetrait',
            field=models.CharField(blank=True, max_length=250),
        ),
    ]