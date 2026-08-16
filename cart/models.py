from django.db import models

from accounts.views import User

# Create your models here.


class Cart(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    paid = models.BooleanField(default=False)

    def __str__(self):
        return f"{self.user.username}"
    
    def total_price(self):
        return sum(item.item_total() for item in self.items.all())
    
    def total(self):
        return self.total_price() + 10  # Assuming a flat shipping fee of $10
    
    
    
    
class CartItem(models.Model):
    cart = models.ForeignKey(Cart, on_delete=models.CASCADE, related_name='items')
    product = models.ForeignKey('product_app.Product', on_delete=models.CASCADE, related_name='cart_items')
    quantity = models.PositiveIntegerField(default=1)
    
    def item_total(self):
        return self.product.price * self.quantity

    def __str__(self):
        return f"{self.product.name} - {self.quantity}"