# Generated by Django 4.0.7 on 2024-02-09 10:56

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0008_basegroup_remove_permission_groups_delete_group_and_more'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='baseuser',
            name='groups',
        ),
    ]