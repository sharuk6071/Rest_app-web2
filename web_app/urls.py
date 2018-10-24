from django.conf.urls import url
from web_app import views as web_app_views

urlpatterns = [
    url(r'^$',web_app_views.home , name='web_app-home'),
    ]
