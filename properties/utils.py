#!/usr/bin/python3

"""
Low-level caching for Property QuerySet
"""



from django.core.cache import cache
from .models import Property


def get_all_properties(request):
    """
    cache the Property queryset
    in Redis for one hour
    """
    all_properties = cache.get('all_properties')
    if not all_properties:
        all_properties = list(Property.objects.all().values())
        cache.set('all_properties', query_set, 3600)
    return all_properties

