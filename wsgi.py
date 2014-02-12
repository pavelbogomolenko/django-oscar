__author__ = 'pavelbogomolenko'

import os
import sys

path = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

# we check for path because we're told to at the tail end of
# http://code.google.com/p/modwsgi/wiki/ConfigurationDirectives#WSGIReloadMechanism
if path not in sys.path:
	sys.path.append(path)

os.environ.setdefault("DJANGO_SETTINGS_MODULE", "sites.icon.settings.prod")

from django.core.wsgi import get_wsgi_application
from dj_static import Cling

application = Cling(get_wsgi_application())
