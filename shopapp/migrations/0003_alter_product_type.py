# Generated by Django 5.0.1 on 2024-01-26 11:40

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('shopapp', '0002_product_type'),
    ]

    operations = [
        migrations.AlterField(
            model_name='product',
            name='type',
            field=models.CharField(default='set', max_length=50),
        ),
    ]
