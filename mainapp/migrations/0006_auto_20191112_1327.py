# Generated by Django 2.2.6 on 2019-11-12 10:27

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('mainapp', '0005_product_image'),
    ]

    operations = [
        migrations.AlterField(
            model_name='product',
            name='price',
            field=models.DecimalField(decimal_places=0, default=0, max_digits=6, verbose_name='цена продукта'),
        ),
    ]