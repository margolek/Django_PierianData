from django import template


register = template.Library()

@register.filter(name='cut_off')
def cut_off(value,arg):
	return value.replace(arg,'')

