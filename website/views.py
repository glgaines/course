from django.conf import settings
from django.views.generic import TemplateView
from django.views.generic.detail import DetailView
from pages.models import Page
#from django.http import HttpResponse
#import os, sys
class BaseView(TemplateView):
    template_name = 'base.html'
    context = {
        'menu': Page.objects.filter(level__lte=1),
        'PROJECT_TITLE':settings.PROJECT_TITLE,
    }

    def get_page(self, request):
        try:
            page = Page.objects.get(path = request.path[1:-1])
        except Page.DoesNotExist:
            page = Page()
        return page

    def get(self, request, *args, **kwargs):
        page = self.get_page(request)
        request.page = page
        self.context['ancestors'] = list(page.get_ancestors()) + [page]
        self.context['page'] = page
        render = super(BaseView, self).get(request, *args, **kwargs)
        return render

    def get_context_data(self, **kwargs):
        context = super(BaseView, self).get_context_data(**kwargs)
        context.update(self.context)
        return context

class IndexView(BaseView):
    template_name = 'index.html'

class PageView(BaseView):
    model = Page
    context_object_name = 'page'
    template_name = 'base.html'
    context = {
        'menu': Page.objects.filter(level__lte=1)
    }
#def music(request):
#    template = 'music.html'
#    context = {}
#    return render(request, template, context)
#
#from django.views.generic import ListView
