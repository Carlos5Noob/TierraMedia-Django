from django import template

register = template.Library()

@register.filter
def cambiar_color(texto, color="blue"):
    return f"<span style='color: {color}'>{texto}</span>"

