from django import template

register = template.Library()

@register.filter    
def add_class_and_placeholder(field, place_holder_text):
    return field.as_widget(attrs={
        "class": "form-control", 
        "placeholder": place_holder_text
    })