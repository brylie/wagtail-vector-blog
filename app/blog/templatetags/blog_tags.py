from django import template
from blog.models import BlogIndexPage

register = template.Library()


@register.simple_tag
def blogindex_url():
    try:
        return BlogIndexPage.objects.live().first().url
    except AttributeError:
        return None  # Return None if BlogIndexPage doesn't exist
