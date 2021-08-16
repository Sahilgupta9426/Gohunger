from django.db import models


CATEGORY_CHOICES = (
 ('V', 'Veg'),
 ('N', 'Non Veg'),
 ('SE','Sweet') )
# Create your models here.
class Menu(models.Model):
    id=models.AutoField
    
    food_name = models.CharField(max_length=50)
    category = models.CharField( choices=CATEGORY_CHOICES, max_length=2)
    price = models.IntegerField(default=0)
    desc = models.CharField(max_length=300)
    pub_date = models.DateField()
    image = models.ImageField(upload_to='shop/images', default="")
    
class Contact(models.Model):
    name=models.CharField(max_length=30)
    email=models.EmailField(max_length=100)
    number=models.CharField(max_length=10)
    details=models.TextField()
   