from django.db import models
from django.urls import reverse

from users.models import User


class ProductCategory(models.Model):
    name = models.CharField(max_length=64, unique=True, verbose_name='название')
    slug = models.SlugField(max_length=254, unique=True)
    description = models.TextField(blank=True, verbose_name='описание')
    image = models.ImageField(
        upload_to="category",
        null=True,
        blank=True,
        default="static/vendor/img/categories/category_default.jpg",
    )

    class Meta:
        verbose_name = 'категория'
        verbose_name_plural = 'категории'

    def __str__(self):
        return self.name

    #
    def get_absolute_url(self):
        return reverse('products:category',
                       args=[self.id])


class Product(models.Model):
    name = models.CharField(max_length=256, verbose_name='название')
    slug = models.SlugField(max_length=200)  #
    image = models.ImageField(upload_to='products/%Y/%m/%d',
                              blank=True)  #
    description = models.TextField(blank=True, verbose_name='описание')
    short_description = models.CharField(max_length=64, blank=True, verbose_name='краткое описание')
    price = models.DecimalField(max_digits=8, decimal_places=2, verbose_name='цена')
    quantity = models.PositiveIntegerField(default=0, verbose_name='количество')
    category = models.ForeignKey(ProductCategory, on_delete=models.CASCADE)
    #
    available = models.BooleanField(default=True)
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)

    class Meta:
        ordering = ['name']  #
        verbose_name = 'продукт'
        verbose_name_plural = 'продукты'
        indexes = [
            models.Index(fields=['id', 'slug']),
            models.Index(fields=['name']),
            models.Index(fields=['-created']),
        ]

    def __str__(self):
        return f'{self.name} | {self.category.name}'

    def get_absolute_url(self):
        return reverse('products:product_detail',
                       args=[self.id, self.slug])


class Basket(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    quantity = models.PositiveIntegerField(default=0)
    created_timestamp = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f'Корзина для {self.user.username} | {self.product.name}'

    def sum(self):
        return self.product.price * self.quantity
