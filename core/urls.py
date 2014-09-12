from django.conf.urls import patterns, include, url
from django.contrib import admin
from apps.dinamic.views import index

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'core.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),
    url(r'^$', index, name='index'),
    url(r'^admin/', include(admin.site.urls)),
)
