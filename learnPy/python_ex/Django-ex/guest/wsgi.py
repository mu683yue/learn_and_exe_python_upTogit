"""
WSGI config for guest project.

It exposes the WSGI callable as a module-level variable named ``application``.

For more information on this file, see
https://docs.djangoproject.com/en/2.2/howto/deployment/wsgi/
"""
"""
与WSGI兼容的Web服务器为你的项目提供服务的入口点
"""

import os

from django.core.wsgi import get_wsgi_application

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'guest.settings')

application = get_wsgi_application()
