from django import template
import re

register = template.Library()

@register.filter(name='phone_formatter')
def phone_formatter(value: str) -> str:
    """
    Format the given phone value.

    :return: str
    """
    phone_regex = re.compile(r'^(\d{2})(\d{1,})(\d{4})$')
    p1, p2, p3 = phone_regex.search(value).groups()
    
    return f'({p1}) {p2}-{p3}'