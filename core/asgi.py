"""
ASGI configuration for the core project.

This module exposes the ASGI callable as a module-level variable named
`application`.

ASGI allows Django to handle asynchronous protocols such as WebSockets,
background tasks, and long-lived connections.

For more information, see:
https://docs.djangoproject.com/en/5.2/howto/deployment/asgi/
"""

import os
import django

from django.core.asgi import get_asgi_application


# Set the default Django settings module for the ASGI application

os.environ.setdefault("DJANGO_SETTINGS_MODULE", "core.settings")

# --------------------------------------------------------------------
# Initialize Django
# --------------------------------------------------------------------
django.setup()

# --------------------------------------------------------------------
# Get the ASGI application callable
# --------------------------------------------------------------------
application = get_asgi_application()
