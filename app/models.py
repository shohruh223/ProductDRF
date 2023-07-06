from django.db import models


class Category(models.Model):
    title = models.CharField(max_length=155)

    def __str__(self):
        return self.title

    class Meta:
        db_table = 'category'
        verbose_name_plural = 'categories'


class Product(models.Model):
    image = models.ImageField(upload_to='product/%Y/%m/%d')
    title = models.CharField(max_length=255)
    description = models.TextField()
    price = models.DecimalField(max_digits=9, decimal_places=2)
    capacity = models.CharField(max_length=100)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    category_id = models.ForeignKey(to="app.Category", on_delete=models.CASCADE, related_name='product')

    def __str__(self):
        return self.title

    class Meta:
        db_table = 'product'
        ordering = ['-created_at',]

