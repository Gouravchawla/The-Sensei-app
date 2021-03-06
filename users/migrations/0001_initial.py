# Generated by Django 3.0.8 on 2020-07-07 18:01

from django.db import migrations, models
import django.db.models.deletion
import users.utils


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('auth', '0011_update_proxy_permissions'),
        ('schools', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='User',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('password', models.CharField(max_length=128, verbose_name='password')),
                ('last_login', models.DateTimeField(blank=True, null=True, verbose_name='last login')),
                ('is_superuser', models.BooleanField(default=False, help_text='Designates that this user has all permissions without explicitly assigning them.', verbose_name='superuser status')),
                ('role', models.SmallIntegerField(choices=[(1, 'Teacher')], default=1)),
                ('email', models.CharField(max_length=255, unique=True)),
                ('first_name', models.CharField(max_length=255)),
                ('last_name', models.CharField(db_index=True, default='', max_length=255)),
                ('phone', models.CharField(default='', max_length=25)),
                ('room_number', models.CharField(default='', max_length=10)),
                ('subjects', models.TextField(default='', help_text='List of subject assigned to a teacher')),
                ('profile_picture', models.FileField(blank=True, null=True, upload_to=users.utils.get_filename)),
                ('date_registered', models.DateTimeField(auto_now_add=True)),
                ('groups', models.ManyToManyField(blank=True, help_text='The groups this user belongs to. A user will get all permissions granted to each of their groups.', related_name='user_set', related_query_name='user', to='auth.Group', verbose_name='groups')),
                ('school', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='schools.School')),
                ('user_permissions', models.ManyToManyField(blank=True, help_text='Specific permissions for this user.', related_name='user_set', related_query_name='user', to='auth.Permission', verbose_name='user permissions')),
            ],
            options={
                'verbose_name': 'User',
                'verbose_name_plural': 'Users',
                'ordering': ['last_name'],
            },
        ),
    ]
