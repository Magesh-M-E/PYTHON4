# Generated by Django 3.2.15 on 2022-12-21 16:14

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('cart', '0005_alter_cart_options'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='cart',
            options={'ordering': ['date_added']},
        ),
    ]
