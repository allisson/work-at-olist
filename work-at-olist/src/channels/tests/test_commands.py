# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.test import TestCase
from django.core.management import call_command
from django.apps import apps as django_apps

import os.path

from src.channels.models import Channel, Category


class TestImportCategories(TestCase):

    def setUp(self):
        self.csv_path = os.path.join(
            django_apps.get_app_config('channels').path, 'tests/testdata.csv'
        )

    def test_command(self):
        call_command(
            'importcategories', 'wallmart', self.csv_path,  verbosity=3,
            interactive=False
        )
        channel = Channel.objects.get(name='wallmart')
        self.assertEqual(Category.objects.filter(channel=channel).count(), 23)
