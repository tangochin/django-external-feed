from django.conf import settings
from django.core.cache import cache
import feedparser


def load_feeds():
    """Load feeds and entries.
    """
    results = {}
    for key, source, prefix in settings.FEED_SOURCES:
        results[key] = feedparser.parse(source)
    return results


def feeds():
    """Get feeds and entries.

    Possibly we get this from the cache.
    """
    if not settings.FEED_SOURCES:
        return {}
    arguments = None
    cache_key = 'feeds'  # possibly add arguments
    timeout = 60*10  # 10 minutes
    result = grab(cache_key, load_feeds, arguments, timeout)
    return result


def grab(key, loader, arguments=None, timeout=None):
    # Grab the vlue of a key from the django cache.  If there is no
    # such key, add it with as value the result of calling the
    # 'loader' function, possibly with arguments and return the value.
    val = cache.get(key)
    if val is None:
        if arguments is None:
            val = loader()
        else:
            val = loader(*arguments)
        cache.set(key, val, timeout)
    return val
