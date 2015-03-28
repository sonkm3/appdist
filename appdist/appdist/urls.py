from django.conf.urls import patterns, include, url
from django.contrib import admin

from application import views

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'appdist.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),

    url(r'^admin/', include(admin.site.urls)),

    url(r'^$', views.root_view),
    url(r'^list/', views.list_view),
    url(r'^plistgen/(?P<app_id>[0-9]+)/(?P<updated>.+)',views.plistgen_view),
)
