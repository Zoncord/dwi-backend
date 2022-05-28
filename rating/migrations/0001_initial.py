# Generated by Django 3.2.13 on 2022-05-28 15:32

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='AchievementRating',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
            ],
            options={
                'verbose_name': 'оценка достижения',
                'verbose_name_plural': 'оценки достижений',
            },
        ),
        migrations.CreateModel(
            name='PostRating',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
            ],
            options={
                'verbose_name': 'оценка поста',
                'verbose_name_plural': 'оценки постов',
            },
        ),
        migrations.CreateModel(
            name='UserRating',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
            ],
            options={
                'verbose_name': 'оценка пользователя',
                'verbose_name_plural': 'оценки пользователей',
            },
        ),
    ]
