from django import template
from core.models import *
register = template.Library()
import re


@register.filter(name="Brflen")
def Brflen(value, arg):
    pattern = re.compile('<.+?>')
    value=pattern.sub('', value)
    p=re.compile('&.+?;')
    l=p.findall(value)
    for x in l:
        value = value.replace(x, ' ')
    return value[:arg] + '...' if len(value) > arg else value[:arg]
@register.filter(name="imgurl")
def Brflen(value):
    if value.upLoadImg1.name!='':
        return value.upLoadImg1.name[4:]
    r = re.compile('src="(.+?)"')
    a = r.search(value.newsDetail)
    if a:
        a=a.groups()

    if a:
        return a[0].replace('&amp;','&')
    else:

        return ""

@register.filter(name="split_movie")
def split_movie(value):
    return value.split(' ')


@register.filter(name="ispwd")
def ispwd(value):
    try:
        return '<li class="list-group-item">百度网盘全集<a href='+value[0]+' target="_blank" >'+value[0]+'</a>'+value[1]+'</li>' if 'http://pan.' in value[0] else '<li class="list-group-item"><a href='+value[0]+' target="_blank" >'+value[1]+'</a></li>'
    except:
        return ''
@register.filter(name="movietags")
def ispwd(value):
    try:
        return "/".join([x.tag_name for x in value.tags.all()])
    except:
        return ''

@register.filter(name="ispwdtv")
def ispwd(value):
    try:
        return '<li class="list-group-item">百度网盘全集<a href='+value[0]+' target="_blank" >'+value[0]+'</a>'+value[1]+'</li>' if 'http://pan.' in value[0] else '<li class="list-group-item"><a href='+value[0]+' target="_blank" >'+value[1]+'</a></li>'
    except:
        return ''


@register.filter(name="cimg")
def cimg(value):
    if value.Image.name != '':
        return value.Image.name[4:]
    else:
        return ""