from django.conf.urls import url

from . import views

urlpatterns = [
    # index pattern
    url(r'^$', views.index, name='index'),
    # details pattern
    url(r'^(?P<offer_id>[0-9]+)/$', views.detail, name='detail'),
    # url(r'^detail/', views.detail, name='detail'),
    # compare pattern
    url(r'^(?P<offer_id>[0-9]+)/compare/$', views.compare, name='compare'),
    # Results page pattern
    # url(r'^results/', views.results, name='results'),
    # new offer pattern
    url(r'^newoffer/', views.newoffer, name='newoffer'),
    # comparison page
    # url(r'^compare/', views.compare, name='compare'),
]