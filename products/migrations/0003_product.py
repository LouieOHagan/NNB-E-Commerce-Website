# Generated by Django 3.0.6 on 2020-05-12 15:08

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0002_auto_20200511_2008'),
    ]

    operations = [
        migrations.CreateModel(
            name='Product',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=254)),
                ('product_code', models.CharField(max_length=254)),
                ('product_description', models.TextField()),
                ('price_original', models.DecimalField(blank=True, decimal_places=2, max_digits=6, null=True)),
                ('price_current', models.DecimalField(decimal_places=2, max_digits=6)),
                ('availability', models.BooleanField(default=False)),
                ('stock', models.PositiveIntegerField(blank=True, default=0, null=True)),
                ('image_1', models.ImageField(blank=True, default='default.png', upload_to='')),
                ('image_2', models.ImageField(blank=True, upload_to='')),
                ('image_3', models.ImageField(blank=True, upload_to='')),
                ('image_4', models.ImageField(blank=True, upload_to='')),
                ('image_5', models.ImageField(blank=True, upload_to='')),
                ('category', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='products.ProductType')),
            ],
        ),
    ]
