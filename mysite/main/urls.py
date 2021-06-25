from django.conf.urls import url
from django.urls import path, include

from . import views

urlpatterns = [
    path('', views.main, name='main'),
    path('main/', views.main, name='main'),
    path('category/<str:category_name>/', views.category, name='category'),
    path('more/<int:event_id>/', views.more, name='more'),
    path('signup/', views.signup, name='signup'),
    url(r"^accounts/", include("django.contrib.auth.urls")),
    path('test/', views.test, name='test'),
]