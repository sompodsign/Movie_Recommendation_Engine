# Generated by Django 3.1.5 on 2021-01-26 03:58

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('movie', '0010_auto_20210125_1437'),
    ]

    operations = [
        migrations.AddField(
            model_name='movie',
            name='watch',
            field=models.CharField(choices=[('Watched', 'Watched'), ('To watch', 'To watch')], default='', max_length=20),
            preserve_default=False,
        ),
    ]
