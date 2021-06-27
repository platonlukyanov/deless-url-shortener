from django.views.generic import RedirectView, CreateView, DetailView
from django.urls import reverse_lazy
from analytics.rq_jobs import record_link_request
from .forms import LinkCreateForm
from .models import Link


class ShortLinkRedirect(RedirectView):
    def get_redirect_url(self, *args, **kwargs):
        code = self.kwargs["code"]
        link_obj = Link.objects.get(shorted_link_code=code)
        record_link_request(self.request, link_obj)
        return link_obj.original


class CreateLinkView(CreateView):
    template_name = 'shortener/index.html'
    model = Link
    form_class = LinkCreateForm

    def get_context_data(self, **kwargs):
        request = self.request
        print(request)
        return super(CreateLinkView, self).get_context_data(**kwargs)

    def get_success_url(self):
        obj = self.object
        return reverse_lazy('link_created', args=[obj.pk, obj.shorted_link_code])


class LinkCreatedView(DetailView):
    template_name = "shortener/link_created.html"
    model = Link
    slug_field = "shorted_link_code"
    slug_url_kwarg = "code"
    context_object_name = "link"

    def get_context_data(self, **kwargs):
        context = super(LinkCreatedView, self).get_context_data(**kwargs)
        context["url"] = self.request.build_absolute_uri(self.object.get_absolute_url())
        return context
