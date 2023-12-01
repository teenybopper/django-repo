from django.contrib.auth.models import User
from django.db import models

# Create your models here.
class Category(models.Model):
    name = models.CharField(max_length=50)
    
    class Meta:
        verbose_name_plural = 'Categories'
    
    def __str__(self):
        return self.name
    

class Items(models.Model):
    Category = models.ForeignKey(Category, related_name='items', on_delete=models.CASCADE)
    Name = models.CharField(max_length=50)
    description = models.TextField(blank = True, null = True)
    price = models.DecimalField(decimal_places=2, max_digits=5)
    image = models.ImageField(upload_to='items_images', blank=True, null=True)
    is_sold = models.BooleanField()
    created_at = models.DateTimeField(auto_now_add=True)
    created_by = models.ForeignKey(User, related_name='items', on_delete=models.CASCADE)
    
    def __str__(self):
        return self.Name