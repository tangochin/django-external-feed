from django.views.generic.base import View
from django.views.generic.base import TemplateView

from externalfeed.utils import feeds


class Index(TemplateView):
    """Index of feed items.
    """
    template_name = 'externalfeed/index.html'

    def get_context_data(self, **kwargs):
        data = super(Index, self).get_context_data(**kwargs)
        data['feeds'] = feeds()
        return data
