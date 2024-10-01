from django.db import models

# Create your models here.
class Brand(models.Model):
    name=models.CharField(max_length=50)


    def __str__(self):
        return self.name

class Color(models.Model):
    color=models.CharField(max_length=50)


    def __str__(self):
        return self.color

class Car(models.Model):
    name=models.CharField(max_length=50)
    content=models.TextField()
    color=models.ForeignKey(Color,on_delete=models.CASCADE)
    brand=models.ForeignKey(Brand,on_delete=models.CASCADE)


    def __str__(self):
        return self.name,self.content



