# Generated by Django 4.0.7 on 2024-02-08 17:18

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('inventory', '0001_initial'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='product',
            options={'permissions': [('can_add_new_product', 'can add new product')]},
        ),
    ]