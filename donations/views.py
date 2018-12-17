from django.shortcuts import render, reverse, redirect
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from django.conf import settings
from .models import Donation
from .forms import DonationForm, PaymentForm
import stripe


stripe.api_key = settings.STRIPE_SECRET

@login_required()
def make_donation(request):
    
    if request.method=="POST":
        donation_form = DonationForm(request.POST, instance=request.user)
        payment_form = PaymentForm(request.POST)
        
        if donation_form.is_valid() and payment_form.is_valid():
            donation_form.save(commit=False)
            donation_amount = donation_form.cleaned_data["donation_amount"]
            
            try:
                customer = stripe.Charge.create(
                    amount = int(donation_amount * 100),
                    currency = "GBP",
                    description = request.user.email,
                    source = request.POST["stripe_id"],
                )
            except stripe.error.CardError:
                messages.error(request, "Your card was declined.")
                
            if customer.paid:
                donation_form.save()
                messages.success(request, "Donation successful. Thank You")
                return redirect(reverse('index'))
            else:
                messages.error(request, "Unable to take payment.")
        else:
            messages.error(request, "We were unable to take a payment with that card.")
    else:
        donation_form = DonationForm(instance=request.user)
        payment_form = PaymentForm()
        
    return render(request, "donation.html", {'donation_form': donation_form, 'payment_form': payment_form, 'publishable': settings.STRIPE_PUBLISHABLE})