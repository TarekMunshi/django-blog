from django.contrib import admin
from .models import BlogPost


class BlogAdmin(admin.ModelAdmin):
    list_display = ('authorName', 'title')


admin.site.register(BlogPost, BlogAdmin)
