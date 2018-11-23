from django.shortcuts import render, reverse, redirect
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from .forms import TicketForm
from .models import Ticket


def all_tickets(request):
    
    
    tickets = Ticket.objects.all()
    return render(request, "tickets.html", {"tickets": tickets})
    
def create_ticket(request):
    
    if request.method == "POST":
        
        bug_ticket_form = TicketForm(request.POST)
        
        if bug_ticket_form.is_valid():
            bug_ticket_form.save(commit=False)
            bug_ticket_form.created_by = request.user
            bug_ticket_form.save()
            messages.success(request, "Bug Ticket was successfully posted.")
            return redirect(reverse("tickets")) 
    else:
        bug_ticket_form = TicketForm()
    
    return render(request, "ticket_form.html", {"bug_ticket_form": bug_ticket_form})
        
