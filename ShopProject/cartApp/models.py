from django.db import models
from ShopApp.models import Product
# Create your models here.
class Cart(models.Model):
    product=models.ForeignKey(Product,on_delete=models.CASCADE)
    quantity=models.IntegerField()
    user_id=models.IntegerField()