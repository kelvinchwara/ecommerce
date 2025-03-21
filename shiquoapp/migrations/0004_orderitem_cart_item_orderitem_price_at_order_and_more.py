# Generated by Django 5.1.5 on 2025-02-25 22:33

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('shiquoapp', '0003_order_email'),
    ]

    operations = [
        migrations.AddField(
            model_name='orderitem',
            name='cart_item',
            field=models.CharField(default='default_cart_item', max_length=255),
        ),
        migrations.AddField(
            model_name='orderitem',
            name='price_at_order',
            field=models.DecimalField(decimal_places=2, default=0.0, max_digits=10),
        ),
        migrations.AlterField(
            model_name='orderitem',
            name='product',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='shiquoapp.product'),
        ),
        migrations.AlterField(
            model_name='orderitem',
            name='quantity',
            field=models.PositiveIntegerField(),
        ),
    ]
