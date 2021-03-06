# Generated by Django 4.0.2 on 2022-02-04 13:28

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Category',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('category_name', models.CharField(max_length=25, verbose_name='category_name')),
                ('okpo', models.IntegerField(unique=True, verbose_name='ОКПО код')),
            ],
        ),
        migrations.CreateModel(
            name='Product',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('product_name', models.CharField(max_length=50, verbose_name='product_name')),
                ('model', models.CharField(max_length=50, verbose_name='model')),
                ('year', models.IntegerField(verbose_name='year')),
                ('description', models.TextField(max_length=300, verbose_name='description')),
                ('image', models.ImageField(upload_to='', verbose_name='image')),
                ('category', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='product_category', to='main.category', verbose_name='category')),
            ],
        ),
    ]
