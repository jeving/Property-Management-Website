from django.shortcuts import get_object_or_404, render
from django.core.paginator import EmptyPage, PageNotAnInteger, Paginator
from .choices import  city_choices, price_choices, bedroom_choices, state_choices
from django.db import OperationalError, ProgrammingError

from .models import Listing
from addproperty.models import AddProperty

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
   
    return render(request, 'listings/listings.html', context)

def properties(request):
  return render(request, 'property_view/properties.html')

def listing(request, listing_id):
  
    listings = Listing.objects.order_by('-list_date').filter(is_published=True)

    paginator = Paginator(listings, 3)
    page = request.GET.get('page')
    paged_listings = paginator.get_page(page)
    
    listing = get_object_or_404(Listing, pk=listing_id)

    context = {
        'listings': paged_listings,
        'listing': listing
    }
    return render(request, 'listings/listing.html', context)

def search(request):    
    addpropertys = AddProperty.objects.order_by('-list_date')

    queryset_list = Listing.objects.order_by('-list_date')

    # Keywords
    if 'keywords' in request.GET:
      keywords = request.GET['keywords']
      if keywords:
        queryset_list = queryset_list.filter(description__icontains=keywords)  
        addpropertys = addpropertys.filter(description__icontains=keywords)  

    # City
    if 'city' in request.GET:
      city = request.GET['city']
      if city:
        queryset_list = queryset_list.filter(city__iexact=city)
        addpropertys = addpropertys.filter(city__iexact=city)

    # State
    if 'state' in request.GET:
      state = request.GET['state']
      if state:
        queryset_list = queryset_list.filter(state__iexact=state) 
        addpropertys = addpropertys.filter(state__iexact=state) 

    # Bedrooms
    if 'bedrooms' in request.GET:
      bedrooms = request.GET['bedrooms']
      if bedrooms:
        queryset_list = queryset_list.filter(bedrooms__iexact=bedrooms)
        addpropertys = addpropertys.filter(bedrooms__iexact=bedrooms)

    # Price
    if 'price' in request.GET:
      price = request.GET['price']
      if price:
        queryset_list = queryset_list.filter(price__lte=price)            
        addpropertys = addpropertys.filter(price__lte=price)            

    context = {
        'state_choices': state_choices,
        'city_choices' : city_choices,
        'bedroom_choices': bedroom_choices,
        'price_choices': price_choices,
        'listings': queryset_list,
        'values': request.GET,
        'addpropertys': addpropertys,
    }
    return render(request, 'listings/search.html', context)

