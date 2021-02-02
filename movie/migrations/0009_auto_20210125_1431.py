# Generated by Django 3.1.5 on 2021-01-25 08:31

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('movie', '0008_auto_20210125_1426'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='movie',
            name='user',
        ),
        migrations.AddField(
            model_name='movie',
            name='author',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
        ),
    ]