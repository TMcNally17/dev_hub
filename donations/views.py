from django.shortcuts import render, reverse, redirect
from django.contrib.auth.decorators import login_required
from django.db.models import Sum
from django.contrib import messages
from django.conf import settings
from .models import Donation
import stripe


stripe.api_key = settings.STRIPE_SECRET

def donations(request):
    
    target = 500
    donation_width = donation_target(target)
    total_donations = donation_amount()
    
    
    return render(request, "donation.html", {"publishable": settings.STRIPE_PUBLISHABLE, 
                                            "total_donations": total_donations, 
                                            "donation_width": donation_width,
                                            "target": target})

@login_required()
def donate(request, amount):
    
    if request.method=="POST":
            
        try:
            donation = stripe.Charge.create(
                source = request.POST["stripeToken"],
                amount = amount,
                currency = "GBP",
                description = "Donation from {0}".format(request.user.email)
            )
        except stripe.error.CardError:
            messages.error(request, "Your card was declined.")
            
        if donation.paid:
            donation = Donation(
                first_name = request.user.first_name,
                last_name = request.user.last_name,
                email = request.user.email,
                donation_amount = amount
                )
            donation.save()
            messages.success(request, "Donation successful. Thank You")
            return redirect(reverse('donations'))
        else:
            messages.error(request, "Unable to take payment.")
        
    return render(request, "donation.html", {'publishable': settings.STRIPE_PUBLISHABLE})
    
def donation_amount():
    
    donations =  Donation.objects.all().aggregate(amount=Sum('donation_amount'))
    if donations["amount"] == None:
        total_donations = 0
    else:
        total_donations = int(donations["amount"] / 100)
    
    return total_donations
    
def donation_target(target):
    
    total_donations = donation_amount()
    
    total_percentage = int(total_donations / target * 100)
    
    return total_percentage
    
    
    