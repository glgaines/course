from django.conf.urls import patterns
# Uncomment the next two lines to enable the admin:
from testing.views import AboutView
urlpatterns = patterns('',
    (r'^', AboutView.as_view()),
)
