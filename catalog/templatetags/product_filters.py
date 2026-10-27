from django import template

register = template.Library()


@register.filter
def euro(price):
    if price is None:
        return '-'

    return f'{price:.2f} €'
