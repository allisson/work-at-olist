# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from rest_framework import serializers

from src.channels.models import Channel, Category


class ChannelSerializer(serializers.ModelSerializer):

    class Meta:
        model = Channel


class SimpleCategorySerializer(serializers.ModelSerializer):

    class Meta:
        model = Category
        fields = ('id', 'created_at', 'updated_at', 'name')


class CategorySerializer(serializers.ModelSerializer):

    parent = SimpleCategorySerializer(many=False, read_only=True)
    children = SimpleCategorySerializer(many=True, read_only=True)

    class Meta:
        model = Category
        fields = (
            'id', 'created_at', 'updated_at', 'name', 'parent', 'children'
        )
