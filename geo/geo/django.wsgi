import os
import sys

sys.path.append('/var/www/geo')
os.environ['DJANGO_SETTINGS_MODULE'] = 'geo.settings'

import django.core.handlers.wsgi
application = django.core.handlers.wsgi.WSGIHandler()
