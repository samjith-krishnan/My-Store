from django.db import models
from django.contrib.auth.models import User
from django.core.validators import MinValueValidator,MaxValueValidator

# Create your models here.

class Products(models.Model):
    name = models.CharField(max_length=30)
    price = models.IntegerField()
    description = models.CharField(max_length=50)
    category = models.CharField(max_length=30)
    image = models.ImageField(null=True)

    def avg_rating(self):

        ratings = self.review_set.all().values_list('rating',flat=True)
        if ratings:
            return sum(ratings)/len(ratings)
        else:
            return 0
        
    def count_review(self):

        reviews = self.review_set.all().values_list('comments',flat=True)
        count = len(reviews)
        return count
        

    def __str__(self):

        return self.name
    

    
class Carts(models.Model):
    user = models.ForeignKey(User,on_delete=models.CASCADE)
    product = models.ForeignKey(Products,on_delete=models.CASCADE)
    date = models.DateTimeField(auto_now_add=True)

class Review(models.Model):
    product = models.ForeignKey(Products,on_delete=models.CASCADE)
    user =models.ForeignKey(User,on_delete=models.CASCADE)
    rating = models.IntegerField(validators=[MinValueValidator(1),MaxValueValidator(5)])
    comments = models.CharField(max_length=200)

    def __str__(self):
        return self.comments

