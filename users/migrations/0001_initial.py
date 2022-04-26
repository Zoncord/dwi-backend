# Generated by Django 3.2.13 on 2022-04-21 12:43

from django.conf import settings
import django.contrib.auth.models
import django.contrib.auth.validators
from django.db import migrations, models
import django.db.models.deletion
import django.utils.timezone


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('achievements', '0001_initial'),
        ('auth', '0012_alter_user_first_name_max_length'),
    ]

    operations = [
        migrations.CreateModel(
            name='User',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('password', models.CharField(max_length=128, verbose_name='password')),
                ('last_login', models.DateTimeField(blank=True, null=True, verbose_name='last login')),
                ('is_superuser', models.BooleanField(default=False, help_text='Designates that this user has all permissions without explicitly assigning them.', verbose_name='superuser status')),
                ('username', models.CharField(error_messages={'unique': 'A user with that username already exists.'}, help_text='Required. 150 characters or fewer. Letters, digits and @/./+/-/_ only.', max_length=150, unique=True, validators=[django.contrib.auth.validators.UnicodeUsernameValidator()], verbose_name='username')),
                ('first_name', models.CharField(blank=True, max_length=150, verbose_name='first name')),
                ('last_name', models.CharField(blank=True, max_length=150, verbose_name='last name')),
                ('email', models.EmailField(blank=True, max_length=254, verbose_name='email address')),
                ('is_staff', models.BooleanField(default=False, help_text='Designates whether the user can log into this admin site.', verbose_name='staff status')),
                ('is_active', models.BooleanField(default=True, help_text='Designates whether this user should be treated as active. Unselect this instead of deleting accounts.', verbose_name='active')),
                ('date_joined', models.DateTimeField(default=django.utils.timezone.now, verbose_name='date joined')),
                ('slug', models.SlugField(max_length=256, verbose_name='slug')),
                ('zoncord_access_token', models.CharField(help_text='access token to the main application', max_length=1024, verbose_name='access token')),
                ('favorite_achievements', models.ManyToManyField(related_name='followed_users', to='achievements.Achievement', verbose_name='user favorite achievements')),
                ('favorite_authors', models.ManyToManyField(related_name='followed_users', to=settings.AUTH_USER_MODEL, verbose_name='user favorite pages')),
                ('groups', models.ManyToManyField(blank=True, help_text='The groups this user belongs to. A user will get all permissions granted to each of their groups.', related_name='user_set', related_query_name='user', to='auth.Group', verbose_name='groups')),
                ('preferred_categories', models.ManyToManyField(help_text='categories that a user might like', to='achievements.Category', verbose_name='preferred categories')),
            ],
            options={
                'verbose_name': 'User',
                'verbose_name_plural': 'Users',
            },
            managers=[
                ('objects', django.contrib.auth.models.UserManager()),
            ],
        ),
        migrations.CreateModel(
            name='State',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('slug', models.SlugField(max_length=256, verbose_name='slug')),
                ('title', models.CharField(max_length=256, verbose_name='title')),
                ('description', models.CharField(max_length=4096, verbose_name='description')),
                ('date_time_of_creation', models.DateTimeField(auto_now_add=True, null=True, verbose_name='Date and time of creation')),
                ('date_time_of_last_edit', models.DateTimeField(auto_now=True, null=True, verbose_name='Date and time of last edit')),
                ('expiration_date_time', models.DateTimeField(help_text='if zero then time is unlimited', verbose_name="date and time when the user's status will change")),
                ('issued_by', models.ForeignKey(help_text='who issued the status', null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='issued_states', to=settings.AUTH_USER_MODEL, verbose_name='issued by')),
            ],
            options={
                'verbose_name': 'general information',
                'verbose_name_plural': 'generals information',
                'abstract': False,
            },
        ),
        migrations.AddField(
            model_name='user',
            name='state',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='users', to='users.state', verbose_name='user state'),
        ),
        migrations.AddField(
            model_name='user',
            name='user_permissions',
            field=models.ManyToManyField(blank=True, help_text='Specific permissions for this user.', related_name='user_set', related_query_name='user', to='auth.Permission', verbose_name='user permissions'),
        ),
    ]
