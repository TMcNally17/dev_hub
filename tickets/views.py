from django.shortcuts import render, reverse, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from .forms import TicketForm
from .models import Ticket


def all_tickets(request):
    
    tickets = Ticket.objects.all()
    return render(request, "tickets.html", {"tickets": tickets})
    
@login_required
def create_ticket(request):
    
    if request.method == "POST":
        
        bug_ticket_form = TicketForm(request.POST)
        
        if bug_ticket_form.is_valid():
            bug_ticket_form.save(commit=False)
            bug_ticket_form.created_by = request.user.username
            bug_ticket_form.save()
            messages.success(request, "Bug Ticket was successfully posted.")
            return redirect(reverse("tickets")) 
    else:
        bug_ticket_form = TicketForm()
    
    return render(request, "ticket_form.html", {"bug_ticket_form": bug_ticket_form})
    
@login_required
def edit_ticket(request, pk):
    
    ticket = Ticket.objects.get(pk=pk)
    if request.user != ticket.created_by:
        return redirect(reverse("tickets"))
    
    if request.method == "POST":
        
        bug_ticket_form = TicketForm(request.POST, instance=Ticket.objects.get(pk=pk))
        
        if bug_ticket_form.is_valid():
            bug_ticket_form.save()
            messages.success(request, "Bug Ticket was successfully edited.")
            return redirect(reverse("tickets")) 
    else:
        bug_ticket_form = TicketForm(instance=Ticket.objects.get(pk=pk))
    
    return render(request, "edit_ticket_form.html", {"bug_ticket_form": bug_ticket_form})
    
@login_required
def upvote(request, pk):
    
    ticket = get_object_or_404(Ticket, pk=pk)
    
    ticket.upvotes += 1
    ticket.save()
    
    return redirect(reverse("tickets"))