# Generated by Django 4.2.13 on 2024-07-07 15:16

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('tarification', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='transaction',
            name='payment_token',
            field=models.CharField(max_length=500),
        ),
        migrations.AlterField(
            model_name='transaction',
            name='transaction_id',
            field=models.CharField(max_length=500, unique=True),
        ),
    ]
