# Generated by Django 4.2.6 on 2023-11-08 23:25

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('crypto', '0005_crypto_rank'),
    ]

    operations = [
        migrations.RenameField(
            model_name='crypto',
            old_name='icon',
            new_name='iconUrl',
        ),
    ]
