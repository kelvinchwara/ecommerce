# Generated by Django 5.1.5 on 2025-02-25 22:26

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('shiquoapp', '0002_remove_order_billing_address_remove_order_email_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='order',
            name='email',
            field=models.EmailField(default='example@example.com', max_length=254),
        ),
    ]
