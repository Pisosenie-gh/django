# Generated by Django 3.2.7 on 2021-09-16 11:07

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0011_alter_abstract_text'),
    ]

    operations = [
        migrations.AlterField(
            model_name='abstract',
            name='theme',
            field=models.ForeignKey(default=None, null=True, on_delete=django.db.models.deletion.CASCADE, to='main.abstractcategory', verbose_name='Тема конспекта'),
        ),
    ]
