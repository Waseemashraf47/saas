from django.http import HttpResponse
from django.shortcuts import render
import pathlib
from visits.models import PageVisit

this_dir = pathlib.Path(__file__).parent


def home_view(request, *args, **kwargs):
    qs = PageVisit.objects.all()
    page_qs = PageVisit.objects.filter(path=request.path)
    page_title = "Home Page"
    context = {
        'page_title': page_title,
        'qs': qs,
        'page_visit_count': page_qs.count(),
        'percent_page_visits': (page_qs.count() / qs.count() * 100) if qs.count() > 0 else 0,
        'total_visit_count': qs.count(),
    }
    path = request.path
    # log the page visit
    print("Logging page visit for path:", path)
    PageVisit.objects.create(path=request.path)

    
    return render(request, "home.html", context)
    