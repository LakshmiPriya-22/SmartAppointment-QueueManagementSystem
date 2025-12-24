"""
WSGI config for queue_system project.
"""

import os
from django.core.wsgi import get_wsgi_application

# Set the default settings module
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'queue_system.settings')

# Get the WSGI application
application = get_wsgi_application()
