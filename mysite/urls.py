from django.conf.urls import patterns, include, url

from django.contrib import admin
from polls.urls import polls_urls
admin.autodiscover()

urlpatterns = patterns('',
    url(r'^$', 'polls.views.index'),
    url(r'^admin/', include(admin.site.urls)),
    url(r'^polls/', include(polls_urls)),
)
