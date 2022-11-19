from django import template
from shop_app.models import categ

register = template.Library()

@register.inclusion_tag('navbar.html', takes_context=True)
def category_navbar(context):
    context = {"categories": categ.objects.all()}
    # context.update(parent_context)  # Only necessary if you need any other context variables in `category_navbar.html`
    return context