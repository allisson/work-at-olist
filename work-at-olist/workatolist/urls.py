# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.conf.urls import url, include
from django.contrib import admin
from django.conf.urls.static import static
from django.conf import settings

urlpatterns = [
    # django.contrib.admin
    url(r'^admin/', admin.site.urls),

    # src.channels
    url(r'^', include('src.channels.urls', namespace='channels')),

    # api docs by swagger
    url(r'^rest-api-docs/', include('rest_framework_swagger.urls')),

] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
