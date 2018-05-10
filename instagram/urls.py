from django.conf.urls import url, include
from . import views
from django.conf import settings
from django.conf.urls.static import static


urlpatterns = [
   url(r'^$', views.home_page, name='index'),
   url(r'^profile/', views.user_profile, name='profile'),
   url(r'^logout/', views.logout, {"next_page": '/'}),
]
if settings.DEBUG:
    urlpatterns+= static(settings.MEDIA_URL, document_root = settings.MEDIA_ROOT)