# Generated by Django 5.0 on 2024-01-04 07:41

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('petapp', '0005_cart_user'),
    ]

    operations = [
        migrations.AddField(
            model_name='product',
            name='img1',
            field=models.ImageField(null=True, upload_to='media'),
        ),
        migrations.AddField(
            model_name='product',
            name='img2',
            field=models.ImageField(null=True, upload_to='media'),
        ),
        migrations.AddField(
            model_name='product',
            name='img3',
            field=models.ImageField(null=True, upload_to='media'),
        ),
    ]
