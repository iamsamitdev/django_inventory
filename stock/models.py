from django.db import models

# stock product 
class Product(models.Model):
    product_name = models.CharField(max_length=128)
    product_detail = models.TextField()
    product_barcode = models.CharField(max_length=13)
    product_qty = models.IntegerField()
    product_price = models.DecimalField(max_digits=7, decimal_places=2)
    product_image = models.CharField(max_length=128)
    product_status = models.IntegerField()
