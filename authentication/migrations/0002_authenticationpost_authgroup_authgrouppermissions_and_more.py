# Generated by Django 4.0.4 on 2022-06-02 15:03

import ckeditor.fields
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('authentication', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='AuthenticationPost',
            fields=[
                ('id', models.BigAutoField(primary_key=True, serialize=False)),
                ('title', models.CharField(max_length=200)),
                ('description', models.TextField()),
                ('created_at', models.DateTimeField()),
                ('update_at', models.DateTimeField()),
            ],
            options={
                'db_table': 'authentication_post',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='AuthGroup',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=150, unique=True)),
            ],
            options={
                'db_table': 'auth_group',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='AuthGroupPermissions',
            fields=[
                ('id', models.BigAutoField(primary_key=True, serialize=False)),
            ],
            options={
                'db_table': 'auth_group_permissions',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='AuthPermission',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255)),
                ('codename', models.CharField(max_length=100)),
            ],
            options={
                'db_table': 'auth_permission',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='AuthUser',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('password', models.CharField(max_length=128)),
                ('last_login', models.DateTimeField(blank=True, null=True)),
                ('is_superuser', models.IntegerField()),
                ('username', models.CharField(max_length=150, unique=True)),
                ('first_name', models.CharField(max_length=150)),
                ('last_name', models.CharField(max_length=150)),
                ('email', models.CharField(max_length=254)),
                ('is_staff', models.IntegerField()),
                ('is_active', models.IntegerField()),
                ('date_joined', models.DateTimeField()),
            ],
            options={
                'db_table': 'auth_user',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='AuthUserGroups',
            fields=[
                ('id', models.BigAutoField(primary_key=True, serialize=False)),
            ],
            options={
                'db_table': 'auth_user_groups',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='AuthUserUserPermissions',
            fields=[
                ('id', models.BigAutoField(primary_key=True, serialize=False)),
            ],
            options={
                'db_table': 'auth_user_user_permissions',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='Category',
            fields=[
                ('category_id', models.IntegerField(db_column='CATEGORY_ID', primary_key=True, serialize=False)),
                ('name', models.CharField(db_column='NAME', max_length=64)),
            ],
            options={
                'db_table': 'category',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='Comment',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('text_content', models.CharField(blank=True, db_column='TEXT_CONTENT', max_length=255, null=True)),
                ('date_of_publication', models.DateTimeField(db_column='DATE_OF_PUBLICATION')),
            ],
            options={
                'db_table': 'comment',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='DjangoAdminLog',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('action_time', models.DateTimeField()),
                ('object_id', models.TextField(blank=True, null=True)),
                ('object_repr', models.CharField(max_length=200)),
                ('action_flag', models.PositiveSmallIntegerField()),
                ('change_message', models.TextField()),
            ],
            options={
                'db_table': 'django_admin_log',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='DjangoContentType',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('app_label', models.CharField(max_length=100)),
                ('model', models.CharField(max_length=100)),
            ],
            options={
                'db_table': 'django_content_type',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='DjangoMigrations',
            fields=[
                ('id', models.BigAutoField(primary_key=True, serialize=False)),
                ('app', models.CharField(max_length=255)),
                ('name', models.CharField(max_length=255)),
                ('applied', models.DateTimeField()),
            ],
            options={
                'db_table': 'django_migrations',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='DjangoSession',
            fields=[
                ('session_key', models.CharField(max_length=40, primary_key=True, serialize=False)),
                ('session_data', models.TextField()),
                ('expire_date', models.DateTimeField()),
            ],
            options={
                'db_table': 'django_session',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='FollowerRequest',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('request_accepted', models.CharField(blank=True, db_column='REQUEST_ACCEPTED', max_length=1, null=True)),
            ],
            options={
                'db_table': 'follower_request',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='InterestedCategory',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
            ],
            options={
                'db_table': 'interested_category',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='Likes',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
            ],
            options={
                'db_table': 'likes',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='OfferCategory',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
            ],
            options={
                'db_table': 'offer_category',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='PostSettings',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('is_private', models.IntegerField(blank=True, db_column='IS_PRIVATE', null=True)),
                ('comments_blocked', models.IntegerField(blank=True, db_column='COMMENTS_BLOCKED', null=True)),
            ],
            options={
                'db_table': 'post_settings',
                'managed': False,
            },
        ),
        migrations.AlterField(
            model_name='post',
            name='description',
            field=ckeditor.fields.RichTextField(blank=True, null=True),
        ),
        migrations.CreateModel(
            name='AccBlogSettings',
            fields=[
                ('account', models.OneToOneField(db_column='ACCOUNT_ID', on_delete=django.db.models.deletion.DO_NOTHING, primary_key=True, serialize=False, to='authentication.authuser')),
                ('is_private', models.CharField(blank=True, db_column='IS_PRIVATE', max_length=1, null=True)),
                ('bio', models.CharField(blank=True, db_column='BIO', max_length=250, null=True)),
                ('profile_background_colour', models.CharField(blank=True, db_column='PROFILE_BACKGROUND_COLOUR', max_length=7, null=True)),
                ('profile_picture', models.TextField(blank=True, db_column='PROFILE_PICTURE', null=True)),
                ('tos_accepted', models.CharField(db_column='TOS_ACCEPTED', max_length=1)),
                ('banned_until', models.DateTimeField(blank=True, db_column='BANNED_UNTIL', null=True)),
                ('banned_permanently', models.CharField(blank=True, db_column='BANNED_PERMANENTLY', max_length=1, null=True)),
                ('window_colour', models.CharField(blank=True, db_column='WINDOW_COLOUR', max_length=7, null=True)),
                ('border_colour', models.CharField(blank=True, db_column='BORDER_COLOUR', max_length=7, null=True)),
            ],
            options={
                'db_table': 'acc_blog_settings',
                'managed': False,
            },
        ),
    ]