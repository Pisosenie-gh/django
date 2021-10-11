# Generated by Django 3.2.7 on 2021-09-16 11:38

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0017_abstract_user_fio'),
    ]

    operations = [
        migrations.CreateModel(
            name='Holiday',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(default=None, max_length=250, verbose_name='Название праздника')),
                ('description', models.TextField(default=None, null=True, verbose_name='Описание праздника')),
                ('text', models.TextField(default=None, null=True, verbose_name='Текст праздника')),
                ('user_fio', models.CharField(default=None, max_length=250, null=True, verbose_name='ФИО автора')),
                ('user_image', models.ImageField(default=None, null=True, upload_to='abstract_user/', verbose_name='Фото профиля создателя')),
                ('date', models.DateTimeField(auto_now=True, verbose_name='Дата публикации')),
                ('theme', models.ForeignKey(default=None, null=True, on_delete=django.db.models.deletion.CASCADE, to='main.abstractcategory', verbose_name='Тема конспекта')),
            ],
            options={
                'verbose_name': 'Праздник',
                'verbose_name_plural': 'Праздники',
            },
        ),
        migrations.CreateModel(
            name='HolidayCategory',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(default=None, max_length=250, verbose_name='Название темы праздника')),
                ('description', models.CharField(default=None, max_length=250, verbose_name='Описание темы праздника')),
            ],
            options={
                'verbose_name': 'Категория праздника',
                'verbose_name_plural': 'Категории праздников',
            },
        ),
        migrations.CreateModel(
            name='HolidaytImage',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('image', models.FileField(blank=True, upload_to='abstract/', verbose_name='Картинка')),
                ('task', models.ForeignKey(default=None, on_delete=django.db.models.deletion.CASCADE, to='main.holiday')),
            ],
            options={
                'verbose_name': 'Праздник фото',
                'verbose_name_plural': 'праздники фото',
            },
        ),
    ]