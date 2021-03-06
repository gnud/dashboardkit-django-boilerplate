# Generated by Django 3.2.3 on 2021-05-24 00:39

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0003_product_poster'),
    ]

    operations = [
        migrations.AddField(
            model_name='product',
            name='detail',
            field=models.TextField(blank=True, max_length=250, null=True, verbose_name='Detail'),
        ),
        migrations.AlterField(
            model_name='product',
            name='poster',
            field=models.ImageField(blank=True, null=True, upload_to='', verbose_name='Image'),
        ),
    ]
