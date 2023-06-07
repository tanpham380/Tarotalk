from django import template

register = template.Library()

@register.filter
def get_star_range(value):
    try:
        num_votes = int(value)
        return range(num_votes)
    except ValueError:
        return []
