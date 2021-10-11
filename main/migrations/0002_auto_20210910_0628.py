# Generated by Django 3.2.7 on 2021-09-10 06:28

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Lapbook',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(default=None, max_length=250, verbose_name='Название Лэпбука')),
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
        migrations.AddField(
            model_name='images',
            name='image',
            field=models.ImageField(default=None, upload_to='images/', verbose_name='Картинка'),
        ),
    ]
