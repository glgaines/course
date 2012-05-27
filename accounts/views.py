# Create your views here.
from django.http import HttpResponseRedirect
from django.utils.decorators import method_decorator
from django.contrib.auth.decorators import login_required
from django.views.generic.edit import FormView

from accounts.forms import ProfileForm
from accounts.models import UserProfile



class ProfileUpdate(FormView):
    form_class = ProfileForm
    template_name = 'account_profile.html'
    success_url = '/accounts/profile/'

#    @method_decorator(login_required)
#    def dispatch(self, request, *args, **kwargs):
#        super(ProfileUpdate, self).dispatch(request, *args, **kwargs)

    def get_form_kwargs(self):

        profile = self.request.user.get_profile()
        self.initial.update({
            'first_name': self.request.user.first_name,
            'last_name': self.request.user.last_name,
            'study_group': profile.study_group,
        })
        kwargs = super(ProfileUpdate, self).get_form_kwargs()
        return kwargs

    def form_valid(self, form):
        cleaned_data = form.cleaned_data
        self.request.user.first_name = cleaned_data['first_name']
        self.request.user.last_name = cleaned_data['last_name']
        self.request.user.save()
        profile = self.request.user.get_profile()
        profile.study_group = cleaned_data['study_group']
        profile.save()
        return HttpResponseRedirect(self.get_success_url())