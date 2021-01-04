from django.shortcuts import render
from django.http import HttpResponse

from .models import Events

# Create your views here.

def indiv_registration(request):

    Event = Events.objects.filter(event_type="individual")
    content = {}
    content['Event']=Event

    return render(request,'indiv.html',content)
    
def group_registration(request):

    Event = Events.objects.filter(event_type="Group")
    content = {}
    content['Event']=Event

    return render(request,'group.html',content)
        

