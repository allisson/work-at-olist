# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.core.wsgi import get_wsgi_application
from whitenoise.django import DjangoWhiteNoise

import os
os.environ.setdefault("DJANGO_SETTINGS_MODULE", "workatolist.settings")

application = get_wsgi_application()
application = DjangoWhiteNoise(application)
