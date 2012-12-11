from django.conf.urls import patterns, url, include
from django.contrib.gis import admin
from world.view import *
import os
admin.autodiscover()

urlpatterns = patterns('',
    url(r'^admin/', include(admin.site.urls)),
    #(r'', include('geo.world.urls')),
    (r'^postgps/(\d{1,2})/(-\d+\.\d+)/(-\d+\.\d+)/$',postgps),
    (r'^informe/(\d{1,2})/$',informe),
    (r'^reporte/$',reporte),
    (r'^report/$',report),
    (r'^valusr/(\S+)$',valUsr),
    (r'^testarea/$',testArea),
    (r'^testdist/$',testDist),
    (r'^site_media/(?P<path>.*)$','django.views.static.serve',
        {'document_root':'/var/www/geo/media'}),
    (r'^static/(?P<path>.*)$','django.views.static.serve',
        {'document_root': '/var/www/geo/media'})
)
