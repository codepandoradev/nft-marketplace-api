# Generated by Django 4.1.3 on 2022-12-02 16:09

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0009_user_first_score_user_second_score_user_third_score'),
    ]

    operations = [
        migrations.AddField(
            model_name='user',
            name='first_top',
            field=models.IntegerField(blank=True, null=True),
        ),
    ]
