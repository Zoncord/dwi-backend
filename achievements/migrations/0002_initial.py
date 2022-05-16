# Generated by Django 3.2.13 on 2022-05-15 16:54

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('achievements', '0001_initial'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.AddField(
            model_name='achievement',
            name='likes',
            field=models.ManyToManyField(blank=True, help_text='users who liked', related_name='achievement_likes', to=settings.AUTH_USER_MODEL, verbose_name='likes'),
        ),
        migrations.AddField(
            model_name='achievement',
            name='main_achievement',
            field=models.ForeignKey(blank=True, help_text='The achievement from which it was created. If unique, then black', null=True, on_delete=django.db.models.deletion.SET_NULL, to='achievements.achievement', verbose_name='main achievement'),
        ),
        migrations.AddField(
            model_name='achievement',
            name='owners',
            field=models.ManyToManyField(related_name='achievements', to=settings.AUTH_USER_MODEL, verbose_name='achievement creators'),
        ),
        migrations.AddField(
            model_name='achievement',
            name='tags',
            field=models.ManyToManyField(blank=True, related_name='achievements', to='achievements.Tag', verbose_name='tags'),
        ),
    ]
