django-external-feed
====================

Show content from an XML feed on your own site. This allows you to use
a commercial weblog service, yet you can still integrate the news
articles within your site.


Quick start
-----------

1. Add "externalfeed" to your INSTALLED_APPS setting like this::

      INSTALLED_APPS = (
          ...
          'externalfeed',
      )

2. Configure the feeds in your settings::

      FEED_SOURCES = (
          # (key, source, prefix to strip from the url)
          ('bbc',
           'http://feeds.bbci.co.uk/news/rss.xml',
           'http://www.bbc.co.uk/news'),
      )

   Note: not all external sources may allow you to embed their content
   like this.  You should check their terms of service.

   - The key is a text of your choosing that will end up in the url on
     your website.

   - The source is the url to an rss, atom or other syndication feed.
     We use [feedparser](https://pypi.python.org/pypi/feedparser/) to
     parse this.

   - The feed will have a url for each item.  The prefix is the part
     that we strip from this url.  The remainder of the url will end
     up in the url that makes this item available on your website.

3. Include the externalfeed URLconf in your project urls.py like this::

      url(r'^news/', include('externalfeed.urls')),
