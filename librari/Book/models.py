from django.db import models
from Cart.models import Cart
# Create your models here.
class Book(models.Model):
    cart = models.ManyToManyField(Cart)
    viti = models.IntegerField(null=True)
    titulli = models.CharField(max_length=255)
    autori = models.CharField(max_length=255)
    cmimi = models.CharField(max_length=255)
    img_src = models.CharField(max_length=255)