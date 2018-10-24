from django.conf.urls import url
from web_users import views as web_users_views

urlpatterns = [
    url(r'^register/',web_users_views.register,name='register'),
    url(r'^profile/',web_users_views.profile,name='profile'),
    url(r'^activate/(?P<uidb64>[0-9A-Za-z_\-]+)/(?P<token>[0-9A-Za-z]{1,13}-[0-9A-Za-z]{1,20})/$',
        web_users_views.activate, name='activate'),
]
