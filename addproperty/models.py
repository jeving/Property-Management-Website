from django.db import models
from datetime import datetime

PROPERTY_TYPE = (
    ('Residential', 'Residential'),
    ('Commercial', 'Commercial'),
    ('Industrial', 'Industrial')
    )

class AddProperty(models.Model):
    property_type = models.CharField(choices=PROPERTY_TYPE,max_length=200)
    property_owner = models.CharField(max_length=200)
    email = models.CharField(max_length=200)
    phone = models.CharField(max_length=100)
    title = models.CharField(max_length=200)
    address = models.CharField(max_length=200)
    city = models.CharField(max_length=100)
    state = models.CharField(max_length=100)
    zipcode = models.PositiveIntegerField()
    description = models.TextField(blank=True)
    price = models.PositiveIntegerField()
    kitchen = models.PositiveIntegerField(default=1)
    hall = models.PositiveIntegerField(default=1)
    bedrooms = models.PositiveIntegerField(default=0)
    bathrooms = models.PositiveIntegerField(default=1)
    balcony = models.PositiveIntegerField(default=0)
    garage = models.PositiveIntegerField(default=0)
    sqft = models.PositiveIntegerField()
    lot_size = models.DecimalField(max_digits=5, decimal_places=1)
    user_id = models.IntegerField(default=1,blank=True)


    photo_main = models.ImageField(upload_to='photos/%Y/%m/%d/')

    
    is_published = models.BooleanField(default=True)
    list_date = models.DateTimeField(default=datetime.now, blank=True)
    def __str__(self):
        return self.title