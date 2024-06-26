"""ASGI config for config project.

It exposes the ASGI callable as a module-level variable named ``application``.

For more information on this file, see
https://docs.djangoproject.com/en/4.2/howto/deployment/asgi/
"""

import os

from django.core.asgi import get_asgi_application

from config.utils import get_target_settings

os.environ.setdefault("DJANGO_SETTINGS_MODULE", get_target_settings())

application = get_asgi_application()
