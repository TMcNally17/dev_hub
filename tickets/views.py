from django.shortcuts import render, reverse, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from .forms import TicketForm
from .models import Ticket


def all_tickets(request):
    
    tickets = Ticket.objects.order_by("-upvotes")
    
    return render(request, "tickets.html", {"tickets": tickets})
    
@login_required
def create_ticket(request):
    
    context = "Create Ticket"
    
    if request.method == "POST":
        
        bug_ticket_form = TicketForm(request.POST)
        
        if bug_ticket_form.is_valid():
            ticket = bug_ticket_form.save(commit=False)
            ticket.created_by = request.user
            ticket.save()
            messages.success(request, "Bug Ticket was successfully posted.")
            
            
            return redirect(reverse("tickets")) 
    else:
        bug_ticket_form = TicketForm()
    
    return render(request, "ticket_form.html", {"bug_ticket_form": bug_ticket_form, "context": context})
    
@login_required
def edit_ticket(request, id):
    
    context = "Edit Ticket"
    
    ticket = Ticket.objects.get(id=id)
    if request.user == ticket.created_by or request.user.is_staff:
    
        if request.method == "POST":
            
            bug_ticket_form = TicketForm(request.POST, instance=Ticket.objects.get(id=id))
            
            if bug_ticket_form.is_valid():
                bug_ticket_form.save()
                messages.success(request, "Bug Ticket was successfully edited.")
                return redirect(reverse("tickets")) 
        else:
            bug_ticket_form = TicketForm(instance=Ticket.objects.get(id=id))
    else:
        return redirect(reverse("tickets"))
    
    return render(request, "ticket_form.html", {"bug_ticket_form": bug_ticket_form, "context": context})
    
@login_required
def upvote_ticket(request, id):
    
    ticket = get_object_or_404(Ticket, id=id)
    
    ticket.upvotes += 1
    ticket.save()
    messages.success(request, "Thank you for upvoting.")
    
    return redirect(reverse("tickets"))