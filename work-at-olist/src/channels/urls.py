# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from rest_framework_extensions.routers import ExtendedSimpleRouter

from src.channels.views import ChannelViewSet, CategoryViewSet

router = ExtendedSimpleRouter()
(
    router.register(r'api/channels', ChannelViewSet, base_name='api-channel')
          .register(r'api/categories',
                    CategoryViewSet,
                    base_name='api-category',
                    parents_query_lookups=['channel'])
)
urlpatterns = router.urls
