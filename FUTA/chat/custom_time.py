# custom_time.py

from django import template
from django.utils.timesince import timesince
from django.utils.timezone import localtime, now

register = template.Library()

@register.filter
def time_since(value):
    """
    Custom template filter to display a human-readable time difference.
    """
    if not value:
        return ''

    # Calculate the time difference
    diff = now() - localtime(value)

    # Convert the time difference to a human-readable format
    return timesince(value).split(', ')[0]
