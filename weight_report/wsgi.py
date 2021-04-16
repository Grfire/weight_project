# -*- coding: utf-8 -*-
"""
create on 2021-04-16 10:17 上午

author @guorui
"""
import os

from django.core.wsgi import get_wsgi_application

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'weight_report.settings')

application = get_wsgi_application()

