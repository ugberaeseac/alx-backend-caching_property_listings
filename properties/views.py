from django.shortcuts import render
from django.views.decorators.cache import cache_page
from django.http import JsonResponse
from .models import Property


# Create your views here

@cache_page(60 * 15)
def property_list(request):
    properties = list(Property.objects.values())
    return JsonResponse({'data': properties})
