# Generated by Django 3.2.7 on 2021-09-10 06:32

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0002_auto_20210910_0628'),
    ]

    operations = [
        migrations.CreateModel(
            name='Abstract',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(default=None, max_length=250, verbose_name='Название Конспекта')),
                ('description', models.CharField(default=None, max_length=250, verbose_name='Описание Лэпбука')),
                ('image_1', models.ImageField(default=None, upload_to='lapbook/', verbose_name='Картинка 1')),
                ('image_2', models.ImageField(default=None, null=True, upload_to='lapbook/', verbose_name='Картинка 2')),
                ('image_3', models.ImageField(default=None, null=True, upload_to='lapbook/', verbose_name='Картинка 3')),
            ],
            options={
                'verbose_name': 'Лэпбук',
                'verbose_name_plural': 'Лэпбуки',
            },
        ),
        migrations.AlterField(
            model_name='imagechapter',
            name='description',
            field=models.TextField(default=None, verbose_name='Описание раздела картинок'),
        ),
        migrations.AlterField(
            model_name='images',
            name='description',
            field=models.TextField(default=None, verbose_name='Описание картинки'),
        ),
        migrations.AlterField(
            model_name='lapbook',
            name='description',
            field=models.TextField(default=None, verbose_name='Описание Лэпбука'),
        ),
    ]