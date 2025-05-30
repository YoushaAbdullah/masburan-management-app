# Generated by Django 4.2.20 on 2025-05-10 08:21

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('external_inventory', '0004_remove_externalinventory_ordered'),
    ]

    operations = [
        migrations.AddField(
            model_name='externalinventory',
            name='status',
            field=models.CharField(choices=[('requested', 'Requested'), ('ordered', 'Ordered'), ('delivered', 'Delivered'), ('in stock', 'In Stock'), ('in use', 'In Use'), ('returned', 'Returned')], default=1, max_length=50),
            preserve_default=False,
        ),
    ]
