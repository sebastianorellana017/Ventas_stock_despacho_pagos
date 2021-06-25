# Generated by Django 3.2.3 on 2021-06-21 12:19

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('cart', '0004_alter_product_available_sizes'),
    ]

    operations = [
        migrations.AlterField(
            model_name='colourvariation',
            name='name',
            field=models.CharField(max_length=50),
        ),
        migrations.AlterField(
            model_name='product',
            name='available_colours',
            field=models.ManyToManyField(to='cart.ColourVariation'),
        ),
    ]
