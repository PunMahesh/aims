from django import template

register = template.Library()

@register.filter
def get_file_extension(file_name):
    return file_name.split('.')[-1]