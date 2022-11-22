from blogApp import views
from django.urls import path

urlpatterns = [
    path('',views.list_blog, name="blogs"),
    path('create/', views.add_blog, name ="create_blogs"),
    path('blog_detail/<str:id>/', views.blog_detail, name ="blog_detail"),
    path('update_blog/<pk>/', views.update_items, name='update_blogs'),
    path('delete_blog/<pk>/', views.delete_items, name='delete_blogs'),
    
    path('login/', views.log_user, name='signin'),
    path('register/', views.signup, name='signup'),
    path('logout/', views.signout, name='signout'),
]
