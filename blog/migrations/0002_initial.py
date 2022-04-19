# Generated by Django 3.2.13 on 2022-04-19 13:41

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('blog', '0001_initial'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.AddField(
            model_name='comment',
            name='likes',
            field=models.ManyToManyField(help_text='users who liked', related_name='comment_likes', to=settings.AUTH_USER_MODEL, verbose_name='likes'),
        ),
        migrations.AddField(
            model_name='comment',
            name='post',
            field=models.ForeignKey(help_text='post commented on', on_delete=django.db.models.deletion.CASCADE, to='blog.post', verbose_name='post'),
        ),
        migrations.AddField(
            model_name='comment',
            name='user',
            field=models.ForeignKey(help_text='the user who left the comment', on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL, verbose_name='user'),
        ),
        migrations.AddField(
            model_name='answers',
            name='comment',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='answers', to='blog.comment', verbose_name='comment'),
        ),
        migrations.AddField(
            model_name='answers',
            name='likes',
            field=models.ManyToManyField(help_text='users who liked', related_name='answer_likes', to=settings.AUTH_USER_MODEL, verbose_name='likes'),
        ),
        migrations.AddField(
            model_name='answers',
            name='post',
            field=models.ForeignKey(help_text='post commented on', on_delete=django.db.models.deletion.CASCADE, to='blog.post', verbose_name='post'),
        ),
        migrations.AddField(
            model_name='answers',
            name='user',
            field=models.ForeignKey(help_text='the user who left the comment', on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL, verbose_name='user'),
        ),
    ]
