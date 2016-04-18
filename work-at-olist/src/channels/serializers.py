# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from rest_framework import serializers

from src.channels.models import Channel, Category


class ChannelSerializer(serializers.ModelSerializer):

    class Meta:
        model = Channel


class CategorySerializer(serializers.ModelSerializer):

    class Meta:
        model = Category
        exclude = ('channel', 'lft', 'rght', 'tree_id', 'level')
