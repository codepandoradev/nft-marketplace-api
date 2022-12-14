# Generated by Django 4.0.7 on 2022-10-29 13:24

import django.core.validators
import django.db.models.deletion
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('collections', '0002_alter_collection_options_remove_collection_id_and_more'),
    ]

    operations = [
        migrations.CreateModel(
            name='Nft',
            fields=[
                ('slug', models.SlugField(primary_key=True, serialize=False)),
                (
                    'network',
                    models.TextField(
                        choices=[
                            ('BSC', 'Binance Smart Chain'),
                            ('SOL', 'Solana'),
                            ('POLYGON', 'Polygon'),
                            ('ETH', 'Ethereum'),
                            ('TON', 'The Open Network'),
                        ]
                    ),
                ),
                (
                    'content',
                    models.FileField(
                        upload_to='nft/content',
                        validators=[
                            django.core.validators.FileExtensionValidator(
                                {'mp4', 'mp3', 'gif', 'webp', 'png'}
                            )
                        ],
                    ),
                ),
                (
                    'title',
                    models.CharField(
                        max_length=30,
                        validators=[
                            django.core.validators.RegexValidator('^[a-zA-Z ]+$')
                        ],
                    ),
                ),
                ('description', models.TextField(blank=True, default='')),
                (
                    'collection',
                    models.ForeignKey(
                        blank=True,
                        null=True,
                        on_delete=django.db.models.deletion.CASCADE,
                        to='collections.collection',
                    ),
                ),
                (
                    'creator',
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        related_name='nfts_by_creator',
                        to=settings.AUTH_USER_MODEL,
                    ),
                ),
                (
                    'owner',
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        related_name='nfts_by_owner',
                        to=settings.AUTH_USER_MODEL,
                    ),
                ),
            ],
            options={
                'ordering': ['pk'],
                'abstract': False,
            },
        ),
    ]
