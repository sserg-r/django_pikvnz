from django.db.models.query import QuerySet
from django.shortcuts import render
from django.http import HttpResponse
from djgeojson.serializers import Serializer
from django.views.generic import ListView, TemplateView
from . import models
from django.utils.safestring import mark_safe

class HomePageView (ListView):    
    model=models.Shapes    
    queryset1 = model.objects.raw('SELECT distinct 1 id, name from testapp_Shapes order by name')
    queryset2 = mark_safe(Serializer().serialize(model.objects.all()))
    queryset={
            "base": queryset1,
            "polyg": queryset2,
    }

    template_name = 'home.html'
    context_object_name = 'hpv'
    
class MapView (ListView):
    template_name = 'map.html'
    # model=models.Shapes 
    # queryset = Serializer().serialize(model.objects.all())
    # queryset = model.objects.all()
    # queryset = mark_safe(Serializer().serialize(model.objects.all()))
    # context_object_name = 'polyg'    

class ListView (ListView):
    template_name = 'list.html'
    
# AJAX
def load_subname(request):
    name_id = request.GET.get('name')
    model=models.Shapes
    queryset = model.objects.raw(f'SELECT id, subname from testapp_Shapes where name like "{name_id}"')
    return render(request, 'sublist.html', {'subnames': queryset})
    