from django.db import models
from datetime import datetime
from realtors.models import Realtor

PROPERTY_TYPE = (
    ('Commercial', 'Commercial'),
    ('Residential', 'Residential'),
    ('Industrial', 'Industrial')
    )

class Listing(models.Model):
    realtor = models.ForeignKey(Realtor, on_delete=models.DO_NOTHING)
    property_type = models.CharField(choices=PROPERTY_TYPE,max_length=200)
    title = models.CharField(max_length=200)
    address = models.CharField(max_length=200)
    city = models.CharField(max_length=100)
    state = models.CharField(max_length=100)
    zipcode = models.BigIntegerField()
    description = models.TextField(blank=True)
    price = models.CharField(max_length=100)
    kitchen = models.PositiveIntegerField(default=1)
    hall = models.PositiveIntegerField(default=1)
    bedrooms = models.PositiveIntegerField()
    bathrooms = models.PositiveIntegerField(default=1)
    balcony = models.PositiveIntegerField(default=0)
    garage = models.PositiveIntegerField(default=0)
    sqft = models.PositiveIntegerField()
    lot_size = models.DecimalField(max_digits=5, decimal_places=1)
  
    photo_main = models.ImageField(upload_to='photos/%Y/%m/%d/')
    photo_1 = models.ImageField(upload_to='photos/%Y/%m/%d/')
    photo_2 = models.ImageField(upload_to='photos/%Y/%m/%d/', blank=True)
    photo_3 = models.ImageField(upload_to='photos/%Y/%m/%d/', blank=True)
    photo_4 = models.ImageField(upload_to='photos/%Y/%m/%d/', blank=True)
    photo_5 = models.ImageField(upload_to='photos/%Y/%m/%d/', blank=True)
    photo_6 = models.ImageField(upload_to='photos/%Y/%m/%d/', blank=True)
    
    is_published = models.BooleanField(default=True)
    list_date = models.DateTimeField(default=datetime.now, blank=True)
    def __str__(self):
        return self.title