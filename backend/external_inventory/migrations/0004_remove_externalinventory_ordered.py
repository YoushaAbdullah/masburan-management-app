# Generated by Django 4.2.20 on 2025-05-09 16:19

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('external_inventory', '0003_externalinventory_ordered'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='externalinventory',
            name='ordered',
        ),
    ]
