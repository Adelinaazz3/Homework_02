from django.db import models
from django.core.validators import MinValueValidator
from django.core.validators import MaxValueValidator
from django.utils import timezone


class Category(models.Model):
    name = models.CharField(max_length=255)
    def __str__(self):
        return self.name
    

class Product(models.Model):
    title = models.CharField(max_length=300)
    description = models.TextField()
    price = models.DecimalField(max_digits=20, decimal_places=5)
    image = models.ImageField(upload_to='products/', null=True, blank=True)
    category = models.ForeignKey(
        Category,
        on_delete=models.CASCADE,
        related_name='products',
        null=True
    )

    def __str__(self):
        return self.title
    


class Review(models.Model):
    text = models.TextField()
    product = models.ForeignKey(Product, on_delete=models.CASCADE, related_name='reviews')
    text = models.TextField()
    stars = models.IntegerField(
        default=1,
        validators=[MinValueValidator(1), MaxValueValidator(5)]
    )
    created_at = models.DateTimeField(auto_now_add=True)

    
    
    def __str__(self):
        return f"{self.product.title} - {self.stars}"
