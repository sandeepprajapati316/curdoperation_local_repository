from django.db import models

class ProductData(models.Model):
    product_id=models.IntegerField(primary_key=True)
    product_name=models.CharField(max_length=100)
    product_cost=models.FloatField()
    product_color=models.CharField(max_length=100)
    product_class=models.CharField(max_length=100)
    customer_name=models.CharField(max_length=100)
    customer_mobile=models.BigIntegerField()
    customer_email=models.EmailField(max_length=100)
