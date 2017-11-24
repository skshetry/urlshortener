"""Views for urlshortener."""
from django.shortcuts import get_object_or_404, redirect

from .helpers import decode_base62
from .models  import Urls

def url_expand(request, hashed_url):
    """Expand url.

    URL provided in `hashed_url` is expanded to the original url
    through :database: and redirect it to the long_url.
    """
    url = get_object_or_404(Urls, pk=decode_base62(hashed_url))

    url.analytics.add_one_view()
    #TODO: Not to add one when the url is visited by the same url creator.
    url.analytics.save()

    return redirect(url.long_url)
