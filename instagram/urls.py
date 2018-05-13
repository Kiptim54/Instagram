from django.conf.urls import url, include
from . import views
from django.conf import settings
from django.conf.urls.static import static


urlpatterns = [
   url(r'^$', views.home_page, name='index'),
   url(r'^accounts/profile/edit', views.user_profile_edit, name='profile'),
   url(r'^logout/', views.logout, {"next_page": '/'}),
   url(r'^upload/', views.user_upload_images, name="uploadphotos" ),
   url(r'^accounts/profile/', views.user_profile, name="userprofile"),
   url(r'^photo/(\d+)/comment', views.add_comment, name='addcomment'),
]
if settings.DEBUG:
    urlpatterns+= static(settings.MEDIA_URL, document_root = settings.MEDIA_ROOT)