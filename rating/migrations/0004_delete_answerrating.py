# Generated by Django 3.2.13 on 2022-07-15 17:30

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('rating', '0003_auto_20220715_1644'),
    ]

    operations = [
        migrations.DeleteModel(
            name='AnswerRating',
        ),
    ]