# Generated by Django 4.1.3 on 2022-12-04 14:13

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0010_user_first_top'),
    ]

    operations = [
        migrations.AlterField(
            model_name='user',
            name='second_score',
            field=models.IntegerField(default=None, null=True),
        ),
    ]
