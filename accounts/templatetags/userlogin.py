from django import template
register = template.Library()
@register.inclusion_tag('accounts/userdetails.html',takes_context=True)
def userlogin(context):
    pass