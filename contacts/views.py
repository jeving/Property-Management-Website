from django.shortcuts import render, redirect
from django.contrib import messages
from django.core.mail import send_mail
from .models import Contact, ContactAdd

def contact(request):
    if request.method == 'POST':
        listing_id = request.POST['listing_id']
        listing = request.POST['listing']
        name = request.POST['name']
        email = request.POST['email']
        phone = request.POST['phone']
        message = request.POST['message']
        user_id = request.POST['user_id']
        realtor_email = request.POST['realtor_email']


        # Check if user had made inquiry alread
        if request.user.is_authenticated:
                user_id = request.user.id
                has_contacted = Contact.objects.all().filter(listing_id=listing_id, user_id=user_id)
                if has_contacted:
                        messages.error(request, 'You have already made an inquiry for this listing')
                        return redirect('/listings/'+listing_id)

        else:
            return render(request, 'accounts/login.html')

        contact = Contact(listing=listing, listing_id=listing_id, name=name, email=email, phone=phone, message=message, user_id=user_id)
        contact.save()
        
        # Send email
#        send_mail(
 #               'Property Listing Inquiry',
  #              'There has been an inquiry for ' + listing + '. Sign into the admin panel for more',
   #            ['{{ realtor.email }}'],
    #            fail_silently=False
     #   )

        messages.success(request, 'Your request has been submitted, a realtor will get back to you soo')
        return redirect('/listings/'+listing_id)
        

def contactadd(request):
    if request.method == 'POST':
        addproperty1 = request.POST['addproperty1']
        addproperty1_id = request.POST['addproperty1_id']
        name = request.POST['name']
        email = request.POST['email']
        phone = request.POST['phone']
        message = request.POST['message']
        user_id = request.POST['user_id']
        realtor_email = request.POST['realtor_email']


        # Check if user had made inquiry alread
        if request.user.is_authenticated:
                user_id = request.user.id
                has_contacted = ContactAdd.objects.all().filter(addproperty1_id=addproperty1_id, user_id=user_id)
                if has_contacted:
                        messages.error(request, 'You have already made an inquiry for this listing')
                        return redirect('/addproperty/'+addproperty1_id)

        else:
            return render(request, 'accounts/login.html')

        contact = ContactAdd(addproperty1=addproperty1, addproperty1_id=addproperty1_id, name=name, email=email, phone=phone, message=message, user_id=user_id)
        contact.save()
        

        messages.success(request, 'Your request has been submitted, a realtor will get back to you soo')
        return redirect('/addproperty/'+addproperty1_id)
