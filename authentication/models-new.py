# This is an auto-generated Django model module.
# You'll have to do the following manually to clean this up:
#   * Rearrange models' order
#   * Make sure each model has one field with primary_key=True
#   * Make sure each ForeignKey and OneToOneField has `on_delete` set to the desired behavior
#   * Remove `managed = False` lines if you wish to allow Django to create, modify, and delete the table
# Feel free to rename the models, but don't rename db_table values or field names.
from django.db import models


class Account(models.Model):
    account = models.OneToOneField('AuthUser', models.DO_NOTHING, db_column='ACCOUNT_ID', primary_key=True)  # Field name made lowercase.
    is_private = models.CharField(db_column='IS_PRIVATE', max_length=1, blank=True, null=True)  # Field name made lowercase.
    bio = models.CharField(db_column='BIO', max_length=250, blank=True, null=True)  # Field name made lowercase.
    profile_background_colour = models.CharField(db_column='PROFILE_BACKGROUND_COLOUR', max_length=7, blank=True, null=True)  # Field name made lowercase.
    profile_picture = models.TextField(db_column='PROFILE_PICTURE', blank=True, null=True)  # Field name made lowercase.
    tos_accepted = models.CharField(db_column='TOS_ACCEPTED', max_length=1)  # Field name made lowercase.
    banned_until = models.DateTimeField(db_column='BANNED_UNTIL', blank=True, null=True)  # Field name made lowercase.
    banned_permanently = models.CharField(db_column='BANNED_PERMANENTLY', max_length=1, blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'account'


class AuthGroup(models.Model):
    name = models.CharField(unique=True, max_length=150)

    class Meta:
        managed = False
        db_table = 'auth_group'


class AuthGroupPermissions(models.Model):
    id = models.BigAutoField(primary_key=True)
    group = models.ForeignKey(AuthGroup, models.DO_NOTHING)
    permission = models.ForeignKey('AuthPermission', models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'auth_group_permissions'
        unique_together = (('group', 'permission'),)


class AuthPermission(models.Model):
    name = models.CharField(max_length=255)
    content_type = models.ForeignKey('DjangoContentType', models.DO_NOTHING)
    codename = models.CharField(max_length=100)

    class Meta:
        managed = False
        db_table = 'auth_permission'
        unique_together = (('content_type', 'codename'),)


class AuthUser(models.Model):
    password = models.CharField(max_length=128)
    last_login = models.DateTimeField(blank=True, null=True)
    is_superuser = models.IntegerField()
    username = models.CharField(unique=True, max_length=150)
    first_name = models.CharField(max_length=150)
    last_name = models.CharField(max_length=150)
    email = models.CharField(max_length=254)
    is_staff = models.IntegerField()
    is_active = models.IntegerField()
    date_joined = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'auth_user'


class AuthUserGroups(models.Model):
    id = models.BigAutoField(primary_key=True)
    user = models.ForeignKey(AuthUser, models.DO_NOTHING)
    group = models.ForeignKey(AuthGroup, models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'auth_user_groups'
        unique_together = (('user', 'group'),)


class AuthUserUserPermissions(models.Model):
    id = models.BigAutoField(primary_key=True)
    user = models.ForeignKey(AuthUser, models.DO_NOTHING)
    permission = models.ForeignKey(AuthPermission, models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'auth_user_user_permissions'
        unique_together = (('user', 'permission'),)


class AuthenticationPost(models.Model):
    id = models.BigAutoField(primary_key=True)
    title = models.CharField(max_length=200)
    description = models.TextField()
    created_at = models.DateTimeField()
    update_at = models.DateTimeField()
    author = models.ForeignKey(AuthUser, models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'authentication_post'


class Blog(models.Model):
    account = models.OneToOneField(Account, models.DO_NOTHING, db_column='ACCOUNT_ID', primary_key=True)  # Field name made lowercase.
    window_colour = models.CharField(db_column='WINDOW_COLOUR', max_length=7, blank=True, null=True)  # Field name made lowercase.
    border_colour = models.CharField(db_column='BORDER_COLOUR', max_length=7, blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'blog'


class Category(models.Model):
    name = models.CharField(db_column='NAME', primary_key=True, max_length=64)  # Field name made lowercase.
    account = models.ForeignKey(Account, models.DO_NOTHING, db_column='ACCOUNT_ID')  # Field name made lowercase.
    account_id2 = models.OneToOneField(Blog, models.DO_NOTHING, db_column='ACCOUNT_ID2')  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'category'


class Comment(models.Model):
    text_content = models.CharField(db_column='TEXT_CONTENT', max_length=255, blank=True, null=True)  # Field name made lowercase.
    date_of_publication = models.DateTimeField(db_column='DATE_OF_PUBLICATION')  # Field name made lowercase.
    account = models.ForeignKey(Account, models.DO_NOTHING, db_column='ACCOUNT_ID')  # Field name made lowercase.
    post = models.OneToOneField('Post', models.DO_NOTHING, db_column='POST_ID', primary_key=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'comment'


class DjangoAdminLog(models.Model):
    action_time = models.DateTimeField()
    object_id = models.TextField(blank=True, null=True)
    object_repr = models.CharField(max_length=200)
    action_flag = models.PositiveSmallIntegerField()
    change_message = models.TextField()
    content_type = models.ForeignKey('DjangoContentType', models.DO_NOTHING, blank=True, null=True)
    user = models.ForeignKey(AuthUser, models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'django_admin_log'


class DjangoContentType(models.Model):
    app_label = models.CharField(max_length=100)
    model = models.CharField(max_length=100)

    class Meta:
        managed = False
        db_table = 'django_content_type'
        unique_together = (('app_label', 'model'),)


class DjangoMigrations(models.Model):
    id = models.BigAutoField(primary_key=True)
    app = models.CharField(max_length=255)
    name = models.CharField(max_length=255)
    applied = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'django_migrations'


class DjangoSession(models.Model):
    session_key = models.CharField(primary_key=True, max_length=40)
    session_data = models.TextField()
    expire_date = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'django_session'


class FollowerRequest(models.Model):
    request_accepted = models.CharField(db_column='REQUEST_ACCEPTED', max_length=1, blank=True, null=True)  # Field name made lowercase.
    account = models.ForeignKey(Account, models.DO_NOTHING, db_column='ACCOUNT_ID')  # Field name made lowercase.
    account_id1 = models.ForeignKey(Account, models.DO_NOTHING, db_column='ACCOUNT_ID1')  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'follower_request'


class Image(models.Model):
    image = models.TextField(db_column='IMAGE', blank=True, null=True)  # Field name made lowercase.
    number_in_post = models.IntegerField(db_column='NUMBER_IN_POST', primary_key=True)  # Field name made lowercase.
    description = models.CharField(db_column='DESCRIPTION', max_length=80, blank=True, null=True)  # Field name made lowercase.
    post = models.ForeignKey('Post', models.DO_NOTHING, db_column='POST_ID')  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'image'
        unique_together = (('number_in_post', 'post'),)


class Likes(models.Model):
    account_account = models.OneToOneField(Account, models.DO_NOTHING, db_column='ACCOUNT_ACCOUNT_ID', primary_key=True)  # Field name made lowercase.
    post_post = models.ForeignKey('Post', models.DO_NOTHING, db_column='POST_POST_ID')  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'likes'
        unique_together = (('account_account', 'post_post'),)


class Post(models.Model):
    post_id = models.AutoField(db_column='POST_ID', primary_key=True)  # Field name made lowercase.
    text_header = models.CharField(db_column='TEXT_HEADER', max_length=64, blank=True, null=True)  # Field name made lowercase.
    text_content = models.CharField(db_column='TEXT_CONTENT', max_length=64, blank=True, null=True)  # Field name made lowercase.
    number_in_blog = models.IntegerField(db_column='NUMBER_IN_BLOG')  # Field name made lowercase.
    is_private = models.CharField(db_column='IS_PRIVATE', max_length=1, blank=True, null=True)  # Field name made lowercase.
    comments_enabled = models.CharField(db_column='COMMENTS_ENABLED', max_length=1, blank=True, null=True)  # Field name made lowercase.
    date_of_publication = models.DateTimeField(db_column='DATE_OF_PUBLICATION')  # Field name made lowercase.
    date_of_last_edit = models.DateTimeField(db_column='DATE_OF_LAST_EDIT', blank=True, null=True)  # Field name made lowercase.
    account = models.ForeignKey(Blog, models.DO_NOTHING, db_column='ACCOUNT_ID')  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'post'
