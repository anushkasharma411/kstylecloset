from django.db import models
from cloudinary.models import CloudinaryField

class Product(models.Model):
    name = models.CharField(max_length=100)
    price = models.IntegerField()
    image = CloudinaryField('image')  # ✅ FIXED
    category = models.CharField(max_length=100, default="fashion")
    drama_name = models.CharField(max_length=100, default="K-drama")

    def __str__(self):
        return self.name