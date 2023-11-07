# Generated by Django 4.2.6 on 2023-11-07 01:20

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('assets', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='crypto',
            name='id',
        ),
        migrations.RemoveField(
            model_name='crypto',
            name='title',
        ),
        migrations.AddField(
            model_name='crypto',
            name='change',
            field=models.FloatField(default=0.0),
        ),
        migrations.AddField(
            model_name='crypto',
            name='key',
            field=models.CharField(default='Qwsogvtv82FCd', max_length=20, primary_key=True, serialize=False),
        ),
        migrations.AddField(
            model_name='crypto',
            name='marketCap',
            field=models.FloatField(default=0.0),
        ),
        migrations.AddField(
            model_name='crypto',
            name='name',
            field=models.CharField(default='', max_length=30),
        ),
        migrations.AddField(
            model_name='crypto',
            name='price',
            field=models.FloatField(default=0.0),
        ),
        migrations.AddField(
            model_name='crypto',
            name='volume',
            field=models.FloatField(default=0.0),
        ),
        migrations.AlterField(
            model_name='crypto',
            name='symbol',
            field=models.CharField(default='', max_length=10),
        ),
    ]
