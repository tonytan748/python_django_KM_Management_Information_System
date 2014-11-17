from django import template
from man_power.models import 

register=template.Library()

@register.inclusion_tag('')
def get_category_list():
	return {'':}