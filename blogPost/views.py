from django.shortcuts import render
from django.http import HttpResponse
from django.template import loader
from .models import BlogPost


def blog(request):
    allBlog = BlogPost.objects.all().values()
    template = loader.get_template('blog.html')
    context = {
        'blogList': allBlog
    }
    return HttpResponse(template.render(context, request))


def singleBlog(request, id):
    blog = BlogPost.objects.get(id=id)
    template = loader.get_template('blogSingle.html')
    context = {
        'blog': blog,
    }
    return HttpResponse(template.render(context, request))


def main(request):
    template = loader.get_template('main.html')
    return HttpResponse(template.render())
