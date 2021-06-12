from django.urls import reverse
from django.contrib import messages
from django.http import HttpResponse
from django.core.mail import send_mail
from django.db import OperationalError, ProgrammingError
from django.shortcuts import render, redirect, get_object_or_404
from django.core.paginator import EmptyPage, PageNotAnInteger, Paginator

from .models import AddProperty
from realtors.models import Realtor
from listings.models import Listing


def index(request):
    listings = Listing.objects.order_by('-list_date').filter(is_published=True)

    paginator = Paginator(listings, 6)
    page = request.GET.get('page')
    paged_listings = paginator.get_page(page)
    
    addpropertys = AddProperty.objects.order_by('-list_date').filter(is_published=True)

    paginator = Paginator(addpropertys, 6)
    page = request.GET.get('page')
    paged_addpropertys = paginator.get_page(page)
    context = {
        'addpropertys': paged_addpropertys,
        'listings': paged_listings,
    }
    
    return render(request, 'add/listings1.html', context)

def properties1(request):
  return render(request, 'add/properties1.html')

def addproperty1(request, addproperty1_id):
    addproperty1 = get_object_or_404(AddProperty, pk=addproperty1_id)

    context = {
        'addproperty1': addproperty1
    }
    return render(request, 'add/properties1.html', context)

def addproperty(request):
    
    if request.method == 'POST':
        property_type = request.POST['property_type']
        property_owner = request.POST['property_owner']
        email = request.POST['email']
        phone = request.POST['phone']
        title = request.POST['title']
        address = request.POST['address']
        city = request.POST['city']
        state = request.POST['state']
        zipcode = request.POST['zipcode']
        description = request.POST['description']
        price = request.POST['price']
        bedrooms = request.POST['bedrooms']
        bathrooms = request.POST['bathrooms']
        garage = request.POST['garage']
        sqft = request.POST['sqft']
        lot_size = request.POST['lot_size']
        user_id = request.POST['user_id']

        photo_main = request.POST['photo_main']
        photo_1 = request.POST['photo_1']
        photo_2 = request.POST['photo_2']
        photo_3 = request.POST['photo_3']
        photo_4 = request.POST['photo_4']
        photo_5 = request.POST['photo_5']
        photo_6 = request.POST['photo_6']
        
        u_id = str(user_id)

        if request.user.is_authenticated:
                user_id = request.user.id
        else:
            messages.success(request, 'Hii... hii...')
            return render(request, 'accounts/login.html')

        addproperty = AddProperty(property_type=property_type, property_owner=property_owner, email=email, phone=phone, title=title, address=address, city=city,state=state,
                                zipcode=zipcode, description=description, price=price, bedrooms=bedrooms,bathrooms=bathrooms, garage=garage, 
                                sqft=sqft, lot_size=lot_size, user_id=user_id,
                                photo_main=photo_main, photo_1=photo_1, photo_3=photo_3, photo_4=photo_4, photo_5=photo_5, photo_6=photo_6,
                                )
        addproperty.save()

        messages.success(request, 'Hiii... Your request has been submitted, a realtor will get back to you soo')
        return redirect(reverse('addproperty'))
    listings = Listing.objects.order_by('-list_date').filter(is_published=True)

    paginator = Paginator(listings, 6)
    page = request.GET.get('page')
    paged_listings = paginator.get_page(page)
    
    addpropertys = AddProperty.objects.order_by('-list_date').filter(is_published=True)

    paginator = Paginator(addpropertys, 6)
    paged_addpropertys = paginator.get_page(page)
    context = {
        'addpropertys': paged_addpropertys,
        'listings': paged_listings,
    }
   
    return render(request, 'add/addproperty.html', context)
    
#   photo_1 = request.POST['photo_1']
#   photo_2 = request.POST['photo_2']
#   photo_3 = request.POST['photo_3']
#   photo_4 = request.POST['photo_4']
#   photo_5 = request.POST['photo_5']
#   photo_6 = request.POST['photo_6'] 
#   photo_main=photo_main, photo_1=photo_1, photo_3=photo_3, photo_4=photo_4, photo_5=photo_5, photo_6=photo_6,
