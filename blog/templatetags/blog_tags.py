# -*- coding: utf-8 -*-
from django import template
from django.db.models import Count

register = template.Library()
from ..models import Post


@register.simple_tag()
def total_posts():
    return Post.objects.all().count()


@register.filter
def rupluralize(value, arg="дурак,дурака,дураков"):
    args = arg.split(",")
    number = abs(int(value))
    a = number % 10
    b = number % 100

    if (a == 1) and (b != 11):
        return args[0]
    elif (a >= 2) and (a <= 4) and ((b < 10) or (b >= 20)):
        return args[1]
    else:
        return args[2]


@register.inclusion_tag('blog/post/latest_posts.html')
def show_latest_posts(count=5):
    latest_posts = Post.objects.all().order_by('-publish')[:count]
    return {'latest_posts': latest_posts}


@register.simple_tag
def get_most_commented_posts(count=5):
    return Post.objects.all().annotate(total_comments=Count('comments')).order_by('-total_comments')[:count]
