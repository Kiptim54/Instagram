from django.conf.urls import url, include
from . import views


urlpatterns = [
   url(r'^$', views.home_page, name='index'),
   url(r'^profile/', views.user_profile, name='profile'),
   url(r'^logout/', views.logout, {"next_page": '/'}),
]