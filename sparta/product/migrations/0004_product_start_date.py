# Generated by Django 4.0.5 on 2022-06-26 13:27

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('product', '0003_alter_product_title_review'),
    ]

    operations = [
        migrations.AddField(
            model_name='product',
            name='start_date',
            field=models.DateField(default=django.utils.timezone.now, verbose_name='노출 시작 일자'),
        ),
    ]