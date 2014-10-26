from django.conf.urls import patterns, include, url

from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns('',
    url(r'^$', 'logintest.views.root', name='root'),
    url(r'^login/$', 'logintest.views.root'),
    url(r'^logout/$', 'logintest.views.logout'),
    url(r'^home/$', 'logintest.views.done', name='done'),

    url('', include('social.apps.django_app.urls', namespace='social')),

    url(r'^admin/', include(admin.site.urls)),
)
