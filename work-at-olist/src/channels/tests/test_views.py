# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.core.urlresolvers import reverse

from rest_framework.test import APITestCase

from src.channels.models import Channel, Category


class TestChannelViewSet(APITestCase):

    def setUp(self):
        for i in range(10):
            Channel.objects.create(name='Channel {0}'.format(i))

    def test_list(self):
        url = reverse('channels:api-channel-list')
        response = self.client.get(url, format='json').json()
        self.assertEqual(response['count'], 10)

    def test_detail(self):
        channel = Channel.objects.all()[0]
        response = self.client.get(channel.get_api_url(), format='json').json()
        self.assertEqual(response['id'], str(channel.pk))


class TestCategoryViewSet(APITestCase):

    def setUp(self):
        self.channel = Channel.objects.create(name='Channel 0')
        for i in range(10):
            Category.objects.create(
                name='Category {0}'.format(i), channel=self.channel
            )

    def test_list(self):
        url = reverse('channels:api-category-list', args=[self.channel.pk])
        response = self.client.get(url, format='json').json()
        self.assertEqual(response['count'], 10)

    def test_detail(self):
        category = Category.objects.all()[0]
        response = self.client.get(
            category.get_api_url(), format='json'
        ).json()
        self.assertEqual(response['id'], str(category.pk))
