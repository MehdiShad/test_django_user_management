# Generated by Django 4.0.7 on 2024-02-08 12:01

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0004_baseuser_type'),
    ]

    operations = [
        migrations.AlterField(
            model_name='baseuser',
            name='type',
            field=models.CharField(choices=[('1', 'staff'), ('2', 'customer'), ('3', 'supervisor')], default='2', max_length=50),
        ),
    ]
