from django.db import models

class Product(models.Model):
   name = models.CharField(max_length=100, verbose_name="Produto")
   price = models.DecimalField(max_digits=8, decimal_places=2, verbose_name="Preço")
   quantity = models.PositiveIntegerField(default=1, verbose_name="Quantidade")
   purchased = models.BooleanField(default=False, verbose_name="Comprado")
   created_at = models.DateTimeField(auto_now_add=True)

   class Meta:
      ordering = ['purchased', '-created_at']
   
   def __str__(self):
      return self.name
   
   @property
   def total_price(self):
      return self.price * self.quantity