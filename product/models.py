from django.db import models



class Category(models.Model):
    name = models.CharField(max_length=255)
    def __str__(self):
        return self.name
    

class Product(models.Model):
    title = models.CharField(max_length=300)    
    description = models.TextField()
    price = models.DecimalField(max_digits=20, decimal_places=5)
    image = models.ImageField(upload_to='products/', null=True, blank=True)

    def __str__(self):
        return self.title
    


class Review(models.Model):
    text = models.TextField()
    product = models.ForeignKey(Product, on_delete=models.CASCADE, related_name='reviews')
