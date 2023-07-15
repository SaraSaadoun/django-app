from django.db import models
from datetime import datetime
# Create your models here.

class Product(models.Model):
    categories = [
        ('phone', 'phone'),
        #admin panel, in db
        ('computer', 'computer')
    ]
    name = models.CharField(max_length=50, default='default', verbose_name='title')
    # verbose_name -> change its name in admin panel
    content = models.TextField(default='content', null=True, blank=True)
    # null -> u can save this field empty
    # blank -> optional field
    price = models.DecimalField(max_digits=5, decimal_places=2, default='10.0')
    image = models.ImageField(upload_to='photos/%y/%m/%d', default='photos/23/07/14/sara.png')
    active = models.BooleanField(default=True)
    category = models.CharField(max_length=50, null=True, blank=True, choices=categories)
    # category
    # content

    def __str__(self):
        return self.name
    
    class Meta:
        verbose_name='products'
        ordering = ['-price', 'name'] 
        # مش صح لان ممكن فى صفحه عاوز ترتيب معين وصفحه اخرى بترتيب اخر

class Test(models.Model):
    date = models.DateField()
    time = models.TimeField(null=True)
    created = models.DateTimeField(null=True, default=datetime.now)