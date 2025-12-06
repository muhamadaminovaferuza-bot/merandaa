from django.urls import path
from .views import home, about, contact, categories, index, blog_single


urlpatterns = [
    path('', home, name='home'),
    path('about/', about, name='about'),
    path('blog_single/', blog_single, name='blog_single'),
    path('categories/', categories, name='categories'),
    path('contact/', contact, name='contact'),
    path('index/', index, name='index'),
]