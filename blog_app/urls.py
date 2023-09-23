from django.urls import path
from . import views

urlpatterns = [
    path('', views.home),
    path('blogs', views.all_blogs),
    path('blog/<int:id>', views.single_blog),
    path('login', views.login),
    path('signup', views.signup),
    path('logout', views.logout),
    path('author_reg', views.register_author),
    path('dashboard', views.user_dashboard),    
    path('add_blog', views.add_blog),
    path('delete_blog/<int:id>', views.delete_blog),
    path('category/<str:name>', views.category_wise),
    path('add_comment/<int:id>', views.add_comment),
]
