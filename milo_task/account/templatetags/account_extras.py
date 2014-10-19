from django import template
from datetime import date
from milo_task.account.utils import get_eligible, get_bizzfuzz

register = template.Library()

@register.filter
def eligible(born):
    return get_eligible(born)

@register.filter
def bizzfuzz(random):
    return get_bizzfuzz(random)