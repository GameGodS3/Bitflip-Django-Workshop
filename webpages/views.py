from django.shortcuts import render
from .forms import EventCreator

# Create your views here.

def index(request):
    return render(request, 'webpages/index.html')

def events(request):
    form = EventCreator(request.POST)
    if request.method == 'POST':
        if form.is_valid():
            evetitle = form.cleaned_data['eventtitle']
            evedesc = form.cleaned_data['eventdesc']
            print(evetitle, evedesc)
            return render(request, 'webpages/events.html', {'form':form})
    else:
        return render(request, 'webpages/events.html', {'form':form})
        