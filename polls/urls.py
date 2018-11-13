from django.conf.urls import patterns, url
from . import views


polls_urls = patterns (
    '',
    url(r'^$',views.index),
)
