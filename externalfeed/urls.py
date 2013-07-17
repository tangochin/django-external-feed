from django.conf.urls import patterns, url

from externalfeed.views import Index

urlpatterns = patterns('',
    url(r'^$', Index.as_view(), name='externalfeed-index'),
    )
