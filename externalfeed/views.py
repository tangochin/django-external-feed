from django.views.generic.base import TemplateView

from externalfeed.utils import feeds, feeditem


class Index(TemplateView):
    """Index of feed items.
    """
    template_name = 'externalfeed/index.html'

    def get_context_data(self, **kwargs):
        data = super(Index, self).get_context_data(**kwargs)
        data['feeds'] = feeds()
        return data


class List(Index):
    """Simple list of feed items.

    Just an ul/li list.
    """
    template_name = 'externalfeed/list.html'


class Entry(TemplateView):
    """Display a feed entry.
    """
    template_name = 'externalfeed/entry.html'

    def get_context_data(self, **kwargs):
        data = super(Entry, self).get_context_data(**kwargs)
        path = kwargs['path']
        if '/' in path:
            # Split the path into a key (to know which feed source to
            # query) and the rest of the path.
            key, path = path.split('/', 1)
            entry = feeditem(key, path)
        else:
            entry = None
        # We could show a 404 error here, if wanted:
        # if entry is None:
        #     from django.http import Http404
        #     raise Http404
        data['entry'] = entry
        return data
