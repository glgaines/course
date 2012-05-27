# -*- coding: utf-8 -*-
from django.conf import settings
from django.views.generic import TemplateView, RedirectView
from django.contrib.auth import REDIRECT_FIELD_NAME
from django.contrib import messages
from django import http


from pages.models import Page

from s_test_code import get_test_info

class BaseView(TemplateView):
    template_name = 'base.html'
    page = Page()

    def get_page(self, request):
        try:
            page = Page.objects.get(path = request.path[1:-1])
        except Page.DoesNotExist:
            page = Page()
        return page

##    def get(self, request, *args, **kwargs):
#    self.page = self.get_page(self.request)
##        render = super(BaseView, self).get(request, *args, **kwargs)
##        return render

    def get_context_data(self, **kwargs):
        context = super(BaseView, self).get_context_data()
        self.page = self.get_page(self.request)
        kwargs['ancestors'] = list(self.page.get_ancestors()) + [self.page]
        kwargs['page'] = self.page
        context.update(kwargs)
        context['menu'] = Page.objects.filter(level__lte=1)
        context['PROJECT_TITLE'] = settings.PROJECT_TITLE
        context['settings'] = settings
        context['redirect_field_name'] = REDIRECT_FIELD_NAME
        context['path'] = self.request.path
        return context

class IndexView(BaseView):
    template_name = 'index.html'

class PageView(BaseView, RedirectView ):
    redirect = False
    template_name = 'base.html'

    def get(self, request, *args, **kwargs):
        render = super(PageView, self).get(request, *args, **kwargs)
        if self.page.tests.count() > 0 and not self.request.user.is_authenticated():
            messages.error(self.request, u'Для прохождения тестирования необходимо войти в систему')
            return http.HttpResponseRedirect(settings.LOGIN_URL+'?'+REDIRECT_FIELD_NAME+'='+self.request.path)
        if self.redirect:
            return http.HttpResponseRedirect('')
        return render

    def get_context_data(self, **kwargs):
        context = super(PageView, self).get_context_data(**kwargs)
        if self.page.tests.all():
            if 'q' not in self.request.GET.keys() and self.page.tests.all()[0].get_busy_name() in self.request.session.keys():
                del self.request.session[self.page.tests.all()[0].get_busy_name()]
            test_info = get_test_info(self.request)
            if test_info['redirect']:
                self.redirect = True
        else:
            test_info = {'is_new' : True}
        context['test'] = test_info
        return context
