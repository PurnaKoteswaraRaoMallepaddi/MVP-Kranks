from django.conf.urls import url
from django.contrib import admin
from music import views
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    url(r'^$', views.log_in,name = 'log_in'),
    url(r'^check/',views.homepage,name = 'homepage')

]
