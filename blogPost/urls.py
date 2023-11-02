from django.urls import path
from . import views

urlpatterns = [
    path('', views.main, name='main'),
    path('blog/', views.blog, name='blog'),
    path('blog/<int:id>', views.singleBlog, name='singleBlog'),
]
