# Generated by Django 4.1.3 on 2022-11-19 14:53

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('messenger', '0001_initial'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='message',
            options={'ordering': ['-sent_at']},
        ),
    ]
