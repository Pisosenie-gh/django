# Generated by Django 3.2.7 on 2021-09-20 08:07

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0020_auto_20210916_1201'),
    ]

    operations = [
        migrations.CreateModel(
            name='Reviews_Contests',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('user_name', models.CharField(blank=True, max_length=5000, verbose_name='USER NAME')),
                ('name', models.CharField(max_length=500, verbose_name='ФИО')),
                ('user_photo', models.CharField(max_length=500, verbose_name='Ссылка на фото ')),
                ('text', models.TextField(verbose_name='Комментарий')),
                ('task', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='main.contests', verbose_name='Конкурс')),
            ],
            options={
                'verbose_name': 'Конкурс комментарий',
                'verbose_name_plural': 'Конкурсы комментарий',
            },
        ),
    ]
