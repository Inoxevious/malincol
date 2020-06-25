from django.db import models
from django.contrib.auth.models import User
# Create your models here.

class Product(models.Model):
    name = models.CharField(max_length=255)
    description = models.TextField(null=True ,blank=True)
    unit_price = models.TextField(null=True ,blank=True)
    old_price = models.TextField(null=True ,blank=True)
    image = models.ImageField(null=True ,blank=True, upload_to='media/malin/vendor_images')
    time = models.DateTimeField()
    time_update = models.DateTimeField()
    visibility = models.IntegerField(null=True ,blank=True)
    shop_categorie = models.IntegerField(null=True ,blank=True)
    quantity = models.IntegerField(null=True ,blank=True)
    order_limits = models.IntegerField(null=True ,blank=True)
    unit_measurement = models.TextField(null=True ,blank=True)
    procurement = models.IntegerField(null=True ,blank=True)
    in_slider = models.IntegerField(null=True ,blank=True)
    url = models.URLField(null=True ,blank=True)
    virtual_products = models.IntegerField(null=True ,blank=True)
    brand_id = models.IntegerField(null=True ,blank=True)
    position = models.IntegerField(null=True ,blank=True)


    class Meta:
      verbose_name_plural = "products"

    def __str__(self):
        return self.name