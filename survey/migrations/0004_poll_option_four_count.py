# Generated by Django 3.0.7 on 2020-07-03 16:19

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('survey', '0003_auto_20200703_2125'),
    ]

    operations = [
        migrations.AddField(
            model_name='poll',
            name='option_four_count',
            field=models.IntegerField(default=0),
        ),
    ]