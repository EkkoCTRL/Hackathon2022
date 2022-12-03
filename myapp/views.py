from django.shortcuts import get_list_or_404, render
from django.http import HttpResponse
from .models import Disaster, Content

# Create your views here.
def index(request):
    title = "Home"
    return render(request, "index.html", {
        "title": title
    })
    
def disaster(request):
    #disasters = list(Disaster.objects.values())
    disasters = Disaster.objects.all()
    return render(request, "disasters.html", {
        "disasters": disasters    
    })

def content(request):
    #contents = Content.objects.get(city=city)
    contents = Content.objects.all()
    return render(request, "content.html", {
        "contents": contents
    })