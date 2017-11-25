"""Views for urlshortener."""
from django.shortcuts import get_object_or_404, redirect, reverse, render

from django.views.generic import ListView
from django.views.generic.edit import ModelFormMixin

from .forms import UrlsForm
from .utils import decode_base62
from .models  import Urls


class UrlsListAndFormView(ModelFormMixin, ListView):
    """ListView that shows all urls of the user ordered by date, paginate and handle form."""

    model = Urls
    paginate_by = 10
    template_name = 'a.html'
    context_object_name = 'urls'
    form_class = UrlsForm

    def get(self, request, *args, **kwargs):
        """Get 10 user links if authenticated and call `super`."""
        self.object = None
        self.form = self.get_form(self.form_class)
        if request.user.is_authenticated:
            self.queryset = self.request.user.user_links.all()
            #TODO: This must be in `User` :model: logic, probably.

            self.paginator = self.get_paginator(self.queryset, 10)
        return super(UrlsListAndFormView, self).get(request, *args, **kwargs)

    def post(self, request, *args, **kwargs):
        """Handle post request for the form.

        And add user to the model if user is authenticated
        after validating the form using the `UrlsForm` :ModelForm:.
        """
        self.form = self.get_form(self.form_class)
        if self.form.is_valid():
            self.object = self.form.save(commit=False) #Don't save now. Add user if authenticated.
            if request.user.is_authenticated:
                self.object.created_by = request.user
                self.object.save()
        return self.get(request, *args, **kwargs) #resend them to listview.

    def get_context_data(self, *args, **kwargs):
        """Add `form`, an instance of `UrlsForm` :ModelForm: to the context response."""
        context = super(UrlsListAndFormView, self).get_context_data(*args, **kwargs)
        context['form'] = self.form
        return context

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