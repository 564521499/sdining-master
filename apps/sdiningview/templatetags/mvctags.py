from django import template

from operation.models import Order

register = template.Library()

from sdiningview.models import Banner
from business.models import Business, Food


@register.simple_tag
def business_type_filter(obj_list, type):
    if type == 1:
        return obj_list.filter(type=1)
    elif type == 2:
        return obj_list.filter(type=2)
    else:
        return obj_list



@register.simple_tag
def get_banner():
    return Banner.objects.all()


@register.simple_tag
def get_pending_order_list(business_obj):
    try:
        return Order.objects.filter(food__business=business_obj, is_accept=False, is_abnormal=False)
    except:
        return None


@register.simple_tag
def get_done_order_list(business_obj):
    try:
        return Order.objects.filter(food__business=business_obj, is_done=True, is_abnormal=False)[:5]
    except:
        return None

@register.filter
def crenumlist(value):
    try:
        return range(value)
    except (TypeError, ValueError):
        return [0]


@register.filter
def is_business_or_food(obj):
    return isinstance(obj, Business)


@register.filter
def is_collect(user, business):
    try:
        if business in user.mycollect.business.all():
            return True
    except:
        return False
