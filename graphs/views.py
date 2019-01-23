import json
from django.shortcuts import render
from django.db.models import Count, Q, Sum
from tickets.models import Ticket
from donations.models import Donation


def graphs(request):
    
    
    # Most Upvoted Bug Ticket Chart
    most_upvoted = Ticket.objects.all().order_by("-upvotes")[:5]
    
    data = list()
    titles = list()
    
    for entry in most_upvoted:
        titles.append(entry.title)
        data.append(entry.upvotes)
    
    upvote_chart = {
        "chart": {"type": "bar"},
        "title": {"text": "Bug Tickets By Upvote"},
        "colors": ["#DADFE5", "#39393A", "#A5C1B7", "#A6B990", "#628193"],
        "plotOptions": {
            "series": {
                "colorByPoint": "true"
            },
        },
        "xAxis": {
            "categories": titles},
        "yAxis": {
            "min": 0,
            "title": {
                "text": "No of Upvotes"
            },
            "tickInterval": 2
        },
        "series": [{ 
            "name": "Upvotes",
            "data": data
        }]
    }

    upvote_chart = json.dumps(upvote_chart)
    
    
    # Bug Tickets By Status
    ticket_status = Ticket.objects \
        .values("title") \
        .annotate(not_started_count=Count('title', filter=Q(status="Not Started")),
                  started_count=Count('title', filter=Q(status="Started")),
                  done_count=Count('title', filter=Q(status="Done"))) \
    
    not_started_count = 0
    started_count = 0
    done_count = 0
    
    for entry in ticket_status:
        not_started_count += (entry["not_started_count"])
        started_count += (entry["started_count"])
        done_count += (entry["done_count"])
   
    
    status_chart = {
        "chart": {"type": "pie"},
        "title": {"text": "Bug Tickets By Status "},
        "series": [{
            "name": 'Statuses',
            "colorByPoint": "true",
            "data": [{ 
                "name": "Not Started",
                "y": not_started_count,
                "color": "#39393A"
            }, { 
                "name": "Started",
                "y": started_count,
                "color": "#628193"
            }, { 
                "name": "Done",
                "y": done_count,
                "color": "#A6B990"
            }]
        }]
    }

    status_chart = json.dumps(status_chart)
    
    
    # Donation Amount By Date 
    data = Donation.objects \
        .values("date") \
        .annotate(amount=Sum('donation_amount'))

    donations = list()
    
    for entry in data:
        donation = [(entry["date"].strftime("%Y-%m-%d")), entry["amount"] / 100]
        donations.append(donation)
    
    donation_chart = {
        "chart": {"type": "column"},
        "title": {"text": "Donations"},
        "colors": ["#DADFE5", "#39393A", "#A5C1B7", "#A6B990", "#628193"],
        "plotOptions": {
            "series": {
                "colorByPoint": "true"
            },
        },
        "xAxis": {
            "type": "category",
            "labels": {
                "rotation": -45
            },
            "title": {
                "text": 'Date'
            }
        },
        "yAxis": {
            "title": {
                "text": "Amount in £s"
            },
            "min": 0
        },
        "series": [{
            "name": 'Donations',
            "data": donations,
        }]
    }
    
    donation_chart = json.dumps(donation_chart)

    return render(request, "graphs.html", {"upvote_chart": upvote_chart, "status_chart": status_chart, "donation_chart": donation_chart})