# Generated by Django 3.2.7 on 2021-09-16 11:33

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0014_alter_abstract_user_fio'),
    ]

    operations = [
        migrations.AlterField(
            model_name='abstract',
            name='user_image',
            field=models.ImageField(default=None, upload_to='abstract_user/', verbose_name='Фото профиля создателя'),
        ),
    ]
