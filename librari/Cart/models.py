from django.db import models
from django.contrib.auth.models import User
from django.db.models.signals import post_save
from django.dispatch import receiver

# Create your models here.
class Cart(models.Model):
    cart = models.OneToOneField(
        User,
        on_delete=models.CASCADE,
        primary_key=True,
    )

    def get_total(self):
        total = 0
        for book in self.book_set.all():
            total += float(book.cmimi)
        return round(total,2)

@receiver(post_save, sender=User)
def create_cart(sender, instance, created, **kwargs):
    if created:
        Cart.objects.create(cart=instance)

@receiver(post_save, sender=User)
def save_cart(sender, instance, **kwargs):
    instance.cart.save()
