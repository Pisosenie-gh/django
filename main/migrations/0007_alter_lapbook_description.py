# Generated by Django 3.2.7 on 2021-09-15 16:42

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0006_auto_20210915_1639'),
    ]

    operations = [
        migrations.AlterField(
            model_name='lapbook',
            name='description',
            field=models.TextField(default=None, null=True, verbose_name='Описание Лэпбука'),
        ),
    ]
