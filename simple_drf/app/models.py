from django.db import models

# Create your models here.


class Test(models.Model):
   name         = models.CharField( max_length=50)
   email        = models.CharField( max_length=50)
   create_at    = models.DateTimeField()
   
   def __str__(self):
       return self.name
   

class Book(models.Model):
    name    = models.CharField(max_length = 50)
    author  = models.CharField(max_length = 50)
    price   = models.IntegerField()
    
    def __str__(self) -> str:
        return self.name
