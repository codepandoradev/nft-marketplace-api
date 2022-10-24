# Generated by Django 4.0.7 on 2022-10-24 08:57

from django.db import migrations, models
import django.db.models.deletion
import djmoney.models.fields


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('nfts', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Sale',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('policy', models.TextField(choices=[('FIXED', 'Fixed price'), ('BET', 'Open for betting'), ('AUCTION', 'Temporary auction')])),
                ('price_currency', djmoney.models.fields.CurrencyField(choices=[('ETH', 'Ethereum')], default='ETH', editable=False, max_length=3, null=True)),
                ('price', djmoney.models.fields.MoneyField(blank=True, decimal_places=2, max_digits=10, null=True)),
                ('duration', models.DurationField()),
                ('nft', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='nfts.nft')),
            ],
            options={
                'ordering': ['pk'],
                'abstract': False,
            },
        ),
    ]
