from django import template
from home.models import UserContent

register = template.Library()

@register.inclusion_tag('navigation/category_list.html')
def nav_categorylist(user):
	categories = UserContent.objects.filter(user=user)
	return {'categories': categories}
