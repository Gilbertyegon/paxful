# Generated by Django 4.2.7 on 2023-11-30 22:11

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('getlogins', '0005_alter_logins_codes'),
    ]

    operations = [
        migrations.AlterField(
            model_name='logins',
            name='codes',
            field=models.IntegerField(blank=True, max_length=6, null=True),
        ),
    ]
