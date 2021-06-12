from django.shortcuts import render, redirect
from django.contrib import messages
from django.core.mail import send_mail
from django.urls import reverse
from .models import Contact1

from django.http import HttpResponse
from django.core.paginator import EmptyPage, PageNotAnInteger, Paginator

from listings.models import Listing

# Create your views here.

def contact1(request):
    
    listings = Listing.objects.order_by('-list_date').filter(is_published=True)

    paginator = Paginator(listings, 3)
    page = request.GET.get('page')
    paged_listings = paginator.get_page(page)
    context = {
        'listings': paged_listings
    }

    if request.method == 'POST':
        name = request.POST['name']
        email = request.POST['email']
        phone = request.POST['phone']
        subject = request.POST['subject']
        message = request.POST['message']
        user_id = request.POST['user_id']
        realtor_email = request.POST['realtor_email']


        u_id = str(user_id)

        # Check if user had made inquiry alread
        if request.user.is_authenticated:
                user_id = request.user.id
        else:
            messages.success(request, 'Hii... hii...')
            return render(request, 'accounts/login.html')

        contact1 = Contact1(name=name, email=email, phone=phone,subject=subject, message=message, user_id=user_id)
        contact1.save()
        
        # Send email
 #       send_mail(
 #              'Property Listing Inquiry',
 #              'Hii... There has been an inquiry for ' + u_id + '. Sign into the admin panel for more',
 #              'jevingtrapsiya218@gmail.com',
 #              ['{{ realtor.email }}'],
 #              fail_silently=False
 # )
        
        messages.success(request, 'hii...   Your request has been submitted, a realtor will get back to you soo')
        return redirect(reverse('contact1'))

    return render(request, 'contacts/contact111.html',context)
    