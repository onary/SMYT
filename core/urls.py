from django.conf.urls import patterns, include, url
from django.contrib import admin
from apps.dynamic.views import index, entity, switch_data

urlpatterns = patterns('',
    url(r'^$', index, name='index'),
    url(r'^entity/(?P<model_name>[\w.-]+)$', entity, name='entity'),
    url(r'^switch_data/$', switch_data, name='switch_data'),

    url(r'^admin/', include(admin.site.urls)),
)
