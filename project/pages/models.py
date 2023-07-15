from django.db import models

class Login(models.Model):
    username = models.CharField(max_length=50)
    password = models.CharField(max_length=50)
    
# Create your models here.
class Female(models.Model):
    female_name = models.CharField(max_length=50, null=True)
    def __str__(self):
        return self.female_name

class Male(models.Model):
    male_name = models.CharField(max_length=50, null=True)
    my_female_name = models.OneToOneField(Female, on_delete=models.CASCADE)
    def __str__(self):
        return self.male_name
    
class Product(models.Model):
    title = models.CharField(max_length=50, null=True)
    def __str__(self):
        return self.title
class User(models.Model):
    name = models.CharField(max_length=50, null=True)
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    def __str__(self):
        return self.name
    
# many to many - videos and users
class Video(models.Model):
    title = models.CharField(max_length=50, null=True)
    def __str__(self):
        return self.title
class Watcher(models.Model):
    name = models.CharField(max_length=50, null=True)
    watch = models.ManyToManyField(Video)
    def __str__(self):
        return self.name