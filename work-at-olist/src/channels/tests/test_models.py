# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.test import TestCase
from django.utils.encoding import smart_text

from src.channels.models import Channel, Category


class TestChannel(TestCase):

    def test_create_model(self):
        channel = Channel.objects.create(name='Channel 1')
        self.assertEqual(smart_text(channel), channel.name)


class TestCategory(TestCase):

    def test_create_model(self):
        channel = Channel.objects.create(name='Channel 1')
        category = Category.objects.create(channel=channel, name='Category 1')
        self.assertEqual(smart_text(category), category.name)
