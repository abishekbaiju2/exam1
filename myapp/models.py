from django.db import models

class Product(models.Model):
    product_name=models.CharField(max_length=100)
    description=models.CharField(max_length=100)
    price=models.DecimalField(max_digits=5,decimal_places=2)
    
    def __str__(self):
        return self.product_name

class Review(models.Model):
    
    product_name=models.ForeignKey(Product,on_delete=models.CASCADE)
    reviewer_name=models.CharField(max_length=100)
    RATING_CHOICES = []
    for i in range(1, 11):
        RATING_CHOICES.append((i, str(i)))
    rating=models.PositiveIntegerField(choices=RATING_CHOICES)
    comments=models.CharField(max_length=100)
    review_date=models.DateField(auto_now_add=True)