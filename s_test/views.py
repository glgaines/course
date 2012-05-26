# some_app/views.py
from django.views.generic import RedirectView
from django.http import Http404, HttpResponse, HttpResponseRedirect
from django.template import RequestContext
from django.shortcuts import render_to_response
from django.conf import settings

from website.views import Page
from s_test_code import get_test_info

from s_test.models import Test

def page(request):
    if Test.objects.all():
        if 'q' not in request.GET.keys() and Test.objects.all()[0].get_busy_name() in request.session.keys():
            del request.session[Test.objects.all()[0].get_busy_name()]

    if Test.objects.all():
        test_info = get_test_info(request)
        if test_info['redirect']:
            return HttpResponseRedirect('')
    else:
        test_info = {'is_new' : True}

    return render_to_response( 'test.html', {
        'test' : test_info,
        'menu': Page.objects.filter(level__lte=1),
        'PROJECT_TITLE':settings.PROJECT_TITLE,
    },

        context_instance=RequestContext(request))


#    def post(self, request, *args, **kwargs):
#        page = self.get_page(request)
#        request.page = page
#        self.context['ancestors'] = list(page.get_ancestors()) + [page]
#        self.context['page'] = page
#
#        if Test.objects.all():
#            if 'q' not in request.GET.keys() and Test.objects.all()[0].get_busy_name() in request.session.keys():
#                del request.session[Test.objects.all()[0].get_busy_name()]
#
#        if Test.objects.all():
#            test_info = get_test_info(request)
#            if test_info['redirect']:
#                self.url=''
#        else:
#            test_info = {'is_new' : True}
#        render = super(BaseView, self).post(request, *args, **kwargs)
#        self.context['test'] = get_test_info(request)
#        return render