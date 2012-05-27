from django.conf.urls import patterns, include, url
from accounts.views import ProfileUpdate
from accounts.forms import ProfileRegistrationForm

urlpatterns = patterns('',

    url(r'register/$', 'registration.views.register', {'form_class': ProfileRegistrationForm, 'backend': 'registration.backends.default.DefaultBackend'}, name='registration_register'),
    ('', include('registration.urls')),
    url(r'^profile/$', ProfileUpdate.as_view(),{'menu': 'qwe'}, name="logout"),
#    url(r'^logout/$', LogoutView.as_view(), name="logout"),
#    url(r'^register/$', LogoutView.as_view(), name="register"),
#    url(r'^login/$', LoginView.as_view(), name="login"),
)