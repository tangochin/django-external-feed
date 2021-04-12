from django.conf.urls import url

from externalfeed import views


urlpatterns = [
    url(r'^$', views.Index.as_view(), name='externalfeed-index'),
    url(r'^list/$', views.List.as_view(), name='externalfeed-list'),
    url(r'^(?P<path>.*)$', views.Entry.as_view(), name='externalfeed-entry'),
]
