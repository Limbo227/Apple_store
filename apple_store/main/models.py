from django.db import models

# Create your models here.


class Category(models.Model):
    category_name = models.CharField(verbose_name='category_name', max_length=25)
    okpo = models.IntegerField(verbose_name='ОКПО код', unique=True)

    def __str__(self):
        return self.category_name

class Product(models.Model):
    product_name = models.CharField(verbose_name='product_name', max_length=50)
    model = models.CharField(verbose_name='model', max_length=50)
    year = models.IntegerField(verbose_name='year')
    description = models.TextField(verbose_name='description', max_length=300)
    image = models.ImageField(verbose_name='image')
    category = models.ForeignKey(Category, on_delete=models.CASCADE, verbose_name='category', related_name='product_category')

    def __str__(self):
        return self.product_name

class Card(models.Model):
    product_name = models.ForeignKey(Product, on_delete=models.CASCADE, verbose_name='product_name', related_name='product_card')

    def __str__(self):
        return self.product_name
