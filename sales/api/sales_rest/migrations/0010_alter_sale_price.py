# Generated by Django 4.0.3 on 2023-09-06 23:46

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('sales_rest', '0009_automobilevo_import_href_alter_sale_customer_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='sale',
            name='price',
            field=models.IntegerField(null=True),
        ),
    ]