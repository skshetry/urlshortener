from django.conf.urls import url

from .views import url_expand, UrlsListAndFormView

urlpatterns = [
    url(r'^$', UrlsListAndFormView.as_view(), name='home'),
    url(r'^(?P<hashed_url>[0-9A-Za-z]{1,})$', url_expand),
]