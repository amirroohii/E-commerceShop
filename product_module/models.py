from django.db import models

# Create your models here.
class ProductCategory(models.Model):
    title = models.CharField(max_length=300, db_index=True)
    url_title = models.CharField(max_length=300, db_index=True)
    is_active = models.BooleanField(default=True,)
    is_deleted = models.BooleanField(default=False,)

    def __str__(self):
        return self.title


class Product(models.Model):
    title = models.CharField(max_length=300, db_index=True)
    category = models.ManyToManyField(ProductCategory, related_name='product_category')
    image = models.ImageField(upload_to='images/products', null=True, blank=True)
    price = models.IntegerField()
    short_description = models.TextField(db_index=True, null=True)
    description = models.TextField(db_index=True)
    slug = models.SlugField(default='', unique=True, null=False, db_index=True, max_length=300)
    is_active = models.BooleanField(default=True, )
    is_deleted = models.BooleanField(default=False, )

    def __str__(self):
        return self.title


class ProductGallery(models.Model):
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    image = models.ImageField(upload_to='images/products', null=True, blank=True)

    def __str__(self):
        return self.product.title