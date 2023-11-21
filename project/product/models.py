from django.db import models

class Product(models.Model):
    id = models.IntegerField(primary_key=True)
    name = models.CharField(max_length=255)
    description = models.TextField()
    location = models.CharField(max_length=50)
    price = models.IntegerField()
    color = models.CharField(max_length=50)
    
    def __str__(self):
        return self.name
