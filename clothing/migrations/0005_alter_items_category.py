# Generated by Django 4.0.3 on 2022-04-12 04:31

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('clothing', '0004_category_items_delete_clothing'),
    ]

    operations = [
        migrations.AlterField(
            model_name='items',
            name='category',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='clothing.category'),
        ),
    ]
