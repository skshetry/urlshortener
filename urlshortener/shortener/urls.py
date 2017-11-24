from django.conf.urls import url

urlpatterns = [
    url(r'^(?P<hashed_url>[0-9A-Za-z]{1,})$', url_expand),
]