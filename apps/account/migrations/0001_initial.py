# -*- coding: utf-8 -*-
# Generated by Django 1.10.5 on 2022-10-08 14:56
from __future__ import unicode_literals

from django.conf import settings
import django.contrib.auth.models
import django.contrib.auth.validators
from django.db import migrations, models
import django.db.models.deletion
import django.utils.timezone


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('auth', '0008_alter_user_username_max_length'),
    ]

    operations = [
        migrations.CreateModel(
            name='User',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('password', models.CharField(max_length=128, verbose_name='password')),
                ('last_login', models.DateTimeField(blank=True, null=True, verbose_name='last login')),
                ('is_superuser', models.BooleanField(default=False, help_text='Designates that this user has all permissions without explicitly assigning them.', verbose_name='superuser status')),
                ('username', models.CharField(error_messages={'unique': 'A user with that username already exists.'}, help_text='Required. 150 characters or fewer. Letters, digits and @/./+/-/_ only.', max_length=150, unique=True, validators=[django.contrib.auth.validators.UnicodeUsernameValidator()], verbose_name='username')),
                ('first_name', models.CharField(blank=True, max_length=30, verbose_name='first name')),
                ('last_name', models.CharField(blank=True, max_length=30, verbose_name='last name')),
                ('email', models.EmailField(blank=True, max_length=254, verbose_name='email address')),
                ('is_staff', models.BooleanField(default=False, help_text='Designates whether the user can log into this admin site.', verbose_name='staff status')),
                ('is_active', models.BooleanField(default=True, help_text='Designates whether this user should be treated as active. Unselect this instead of deleting accounts.', verbose_name='active')),
                ('date_joined', models.DateTimeField(default=django.utils.timezone.now, verbose_name='date joined')),
                ('avatar', models.URLField(blank=True, verbose_name='头像')),
                ('creditrank', models.IntegerField(default=100, verbose_name='信用级别')),
                ('usertype', models.IntegerField(choices=[(0, '商家'), (1, '用户')], default=1, verbose_name='用户类型')),
                ('phonenumber', models.CharField(blank=True, max_length=11, verbose_name='联系方式')),
                ('truename', models.CharField(blank=True, max_length=30, verbose_name='真实姓名')),
                ('can_order', models.BooleanField(default=True, verbose_name='是否能订餐')),
                ('date_ban', models.DateTimeField(blank=True, null=True, verbose_name='开始封禁的时间')),
                ('banday', models.IntegerField(default=0, verbose_name='封禁天数')),
                ('groups', models.ManyToManyField(blank=True, help_text='The groups this user belongs to. A user will get all permissions granted to each of their groups.', related_name='user_set', related_query_name='user', to='auth.Group', verbose_name='groups')),
                ('user_permissions', models.ManyToManyField(blank=True, help_text='Specific permissions for this user.', related_name='user_set', related_query_name='user', to='auth.Permission', verbose_name='user permissions')),
            ],
            options={
                'verbose_name': 'user',
                'verbose_name_plural': 'users',
                'abstract': False,
            },
            managers=[
                ('objects', django.contrib.auth.models.UserManager()),
            ],
        ),
        migrations.CreateModel(
            name='Accesstoken',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('access_token', models.CharField(max_length=200)),
                ('date_create', models.DateTimeField(auto_now_add=True)),
            ],
            options={
                'ordering': ['-date_create'],
            },
        ),
        migrations.CreateModel(
            name='OAuthQQProfile',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('qq_openid', models.CharField(blank=True, max_length=100)),
                ('access_token', models.CharField(blank=True, max_length=100)),
                ('nickname', models.CharField(blank=True, max_length=256, verbose_name='昵称')),
                ('sex', models.IntegerField(choices=[(1, '男'), (2, '女'), (0, '未知')], default=0, verbose_name='性别')),
                ('stuid', models.CharField(blank=True, max_length=20, verbose_name='学号')),
                ('user', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL, verbose_name='用户')),
            ],
            options={
                'verbose_name': 'QQ个人信息',
                'verbose_name_plural': 'QQ个人信息',
            },
        ),
    ]
