from django.conf.urls import patterns, include, url
from django.contrib import admin

urlpatterns = patterns('',

    url(r'^$', 'global_development.views.welcome_page', name='welcome_page'),

    url(r'^admin/', include(admin.site.urls)),
)