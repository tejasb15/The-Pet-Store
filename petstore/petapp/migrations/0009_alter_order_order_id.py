# Generated by Django 4.1.4 on 2024-01-10 08:34

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('petapp', '0008_order'),
    ]

    operations = [
        migrations.AlterField(
            model_name='order',
            name='order_id',
            field=models.CharField(max_length=100, null=True),
        ),
    ]
