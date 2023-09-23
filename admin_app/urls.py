from django.urls import path
from . import views

urlpatterns = [
    path('', views.home),
    path('authors', views.authors),
    path('blogs', views.blogs),
    path('hide_blog/<int:id>', views.hide_blog),
    path('unhide_blog/<int:id>', views.unhide_blog),
    path('search', views.results),
]