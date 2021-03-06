# Generated by Django 2.1 on 2019-04-16 15:51

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('auth', '0009_alter_user_last_name_max_length'),
    ]

    operations = [
        migrations.CreateModel(
            name='Employee',
            fields=[
                ('user', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, primary_key=True, related_name='profile', serialize=False, to=settings.AUTH_USER_MODEL)),
                ('birthdate', models.DateField(max_length=8)),
                ('address', models.CharField(max_length=200)),
                ('image', models.ImageField(blank=True, upload_to='user_images')),
                ('phone', models.CharField(default='', max_length=30)),
            ],
        ),
        migrations.CreateModel(
            name='Service',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('desc', models.CharField(max_length=500)),
            ],
        ),
        migrations.AddField(
            model_name='employee',
            name='services',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='clouddomus.Service'),
        ),
    ]
