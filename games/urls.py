from django.conf.urls import patterns, url

from games import views

urlpatterns = patterns('',
    url(r'^$', views.index, name='index'),
    url(r'^all$', views.all_games, name='all'),
    url(r'^deals$', views.deals, name='deals'),
    url(r'^contact$', views.contact, name='contact'),
    url(r'^login$', 'django.contrib.auth.views.login', { 'template_name': 'login.html' }),
    url(r'^logout$', 'django.contrib.auth.views.logout', { 'next_page': '/games/' }),
)
