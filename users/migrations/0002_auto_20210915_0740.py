# Generated by Django 3.2.7 on 2021-09-15 07:40

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='newuser',
            name='subscription',
            field=models.BooleanField(default=False),
        ),
        migrations.AlterField(
            model_name='newuser',
            name='is_active',
            field=models.BooleanField(default=True),
        ),
    ]
