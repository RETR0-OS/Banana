# Generated by Django 4.0.4 on 2022-05-26 02:40

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('ecommerce', '0020_rename_preproccessing_order_preproccessed'),
    ]

    operations = [
        migrations.AddField(
            model_name='order',
            name='Paid_price',
            field=models.FloatField(default=0),
        ),
    ]
