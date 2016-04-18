# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from rest_framework import viewsets
from rest_framework_extensions.mixins import NestedViewSetMixin

from src.channels.models import Channel, Category
from src.channels.serializers import ChannelSerializer, CategorySerializer


class ChannelViewSet(NestedViewSetMixin, viewsets.ReadOnlyModelViewSet):

    queryset = Channel.objects.all()
    serializer_class = ChannelSerializer


class CategoryViewSet(NestedViewSetMixin, viewsets.ReadOnlyModelViewSet):

    queryset = Category.objects.all()
    serializer_class = CategorySerializer
