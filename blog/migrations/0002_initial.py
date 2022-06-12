# Generated by Django 3.2.13 on 2022-06-06 14:02

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
            model_name='post',
            name='author',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to=settings.AUTH_USER_MODEL, verbose_name='author'),
        ),
        migrations.AddField(
            model_name='comment',
            name='author',
            field=models.ForeignKey(help_text='the user who left the comment', on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL, verbose_name='user'),
        ),
        migrations.AddField(
            model_name='comment',
            name='post',
            field=models.ForeignKey(help_text='post commented on', on_delete=django.db.models.deletion.CASCADE, to='blog.post', verbose_name='post'),
        ),
        migrations.AddField(
            model_name='answer',
            name='author',
            field=models.ForeignKey(help_text='the user who left the comment', on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL, verbose_name='user'),
        ),
        migrations.AddField(
            model_name='answer',
            name='comment',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='answers', to='blog.comment', verbose_name='comment'),
        ),
        migrations.AddField(
            model_name='answer',
            name='post',
            field=models.ForeignKey(help_text='post commented on', on_delete=django.db.models.deletion.CASCADE, to='blog.post', verbose_name='post'),
        ),
    ]
