"""
WSGI config for example project.

It exposes the WSGI callable as a module-level variable named ``application``.

For more information on this file, see
https://docs.djangoproject.com/en/3.2/howto/deployment/wsgi/

나중에 배포 작업할 때 사용한다
Web Server Gateway Interface
--> 파이썬 기반으로 웹서버를 만들게 되면 인터페이스를 이렇게 구성하자
"""

import os

from django.core.wsgi import get_wsgi_application

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'example.settings')

application = get_wsgi_application()
