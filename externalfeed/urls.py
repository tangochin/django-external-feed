from django.conf.urls import patterns, url

from externalfeed.views import Index, Entry

urlpatterns = patterns('',
    url(r'^$', Index.as_view(), name='externalfeed-index'),
    url(r'^(?P<path>.*)$', Entry.as_view(), name='externalfeed-entry'),
    )
