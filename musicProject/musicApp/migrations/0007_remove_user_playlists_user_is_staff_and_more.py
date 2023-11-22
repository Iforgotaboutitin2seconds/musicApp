# Generated by Django 4.2.7 on 2023-11-22 17:43

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('musicApp', '0006_remove_user_groups_remove_user_is_superuser_and_more'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='user',
            name='playlists',
        ),
        migrations.AddField(
            model_name='user',
            name='is_staff',
            field=models.BooleanField(default=False),
        ),
        migrations.AlterField(
            model_name='user',
            name='password',
            field=models.CharField(max_length=128, verbose_name='password'),
        ),
    ]
