from django.conf.urls import patterns, include, url
from website.views import IndexView, PageView
from filebrowser.sites import site
from django.contrib import admin
admin.autodiscover()


# Includes
urlpatterns = patterns('',
    (r'^accounts/', include('accounts.urls')),
    #(r'^test/', include('s_test.urls')),
    (r'^tinymce/', include('tinymce.urls')),
    (r'^grappelli/', include('grappelli.urls')),
    url(r'^admin/filebrowser/', include(site.urls)),
    url(r'^admin/doc/', include('django.contrib.admindocs.urls')),
    url(r'^admin/', include(admin.site.urls)),
)


urlpatterns += patterns('',
    url(r'^$', IndexView.as_view(), name='index'),
    #    url(r'^music/?$', 'views.music', name='music'),
    #url(r'^music/Media/[\w.]*$', redirect_to, {'url': '/media/filtersourcesound.mp3'}),
    # url(r'^study/', include('study.foo.urls')),

    (r'^(?P<page_url>.*?)[/]?$', PageView.as_view()),
)

##includes
#urlpatterns += patterns('testing.views',
#    (r'^testing/', include('testing.urls')),
#)
