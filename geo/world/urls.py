# Import django modules
from django.conf.urls.defaults import *
from geo.world.views import *

urlpatterns = patterns('geo.world.views',
    url(r'^$', 'index', name='world-index'),
    (r'^postgps/(\d{1,2})/(\d{2,20})/(\d{2,20})/$',postgps),
)
