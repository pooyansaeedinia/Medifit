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
    
    

class Order(models.Model):
    cart = models.OneToOneField(Cart, on_delete=models.CASCADE)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    email = models.EmailField()
    order_date = models.DateTimeField(auto_now_add=True)
    phone_number = models.CharField(max_length=11)
    shipping_address = models.TextField()
    city = models.CharField(max_length=100)
    postal_code = models.CharField(max_length=20)
    payment_method = models.CharField(max_length=50, choices=[('credit_card', 'Credit Card'), ('paypal', 'PayPal'), ('cash_on_delivery', 'Cash on Delivery')])
    
    
    def __str__(self):
        return f"Order #{self.id} - {self.cart.user.username}"
    
    
    def save(self, *args, **kwargs):
        if self.cart.paid:
            raise ValueError("Cannot create an order for an already paid cart.")

        self.user = self.cart.user
        self.email = self.cart.user.email

        super().save(*args, **kwargs)

        self.cart.paid = True
        self.cart.save(update_fields=['paid'])