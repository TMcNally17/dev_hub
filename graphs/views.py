import json
from django.shortcuts import render
from django.db.models import Count, Q
from tickets.models import Ticket


def graphs(request):
    
    
    # Most Upvoted Bug Ticket Chart
    most_upvoted = Ticket.objects.all().order_by("-upvotes")[:5]
    
    data = list()
    titles = list()
    
    for entry in most_upvoted:
        titles.append(entry.title)
        data.append(entry.upvotes)
    
    chart = {
        "chart": {"type": "column"},
        "title": {"text": "Bug Tickets by upvote"},
        "plotOptions": {
            "series": {
                "colorByPoint": "true"
            },
        },
        "xAxis": {"categories": titles},
        "yAxis": {
            "min": 0,
            "title": {
                "text": "No of Upvotes"
            }
        },
        "series": [{ 
            "name": "Tickets",
            "data": data
        }]
    }

    upvote_chart = json.dumps(chart)
    
    
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
   
    
    chart = {
        "chart": {"type": "pie"},
        "title": {"text": "Bug Tickets by status "},
        "series": [{
            "name": 'Status',
            "colorByPoint": "true",
            "data": [{ 
                "name": "Not Started",
                "y": not_started_count
            }, { 
                "name": "Started",
                "y": started_count
            }, { 
                "name": "Done",
                "y": done_count
            }]
        }]
    }

    status_chart = json.dumps(chart)

    return render(request, "graphs.html", {"upvote_chart": upvote_chart, "status_chart": status_chart})