# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.test import TestCase
from django.utils.encoding import smart_text
from django.apps import apps as django_apps

import os.path

from src.channels.models import Channel, Category, import_categories_from_csv


class TestChannel(TestCase):

    def test_create_model(self):
        channel = Channel.objects.create(name='Channel 1')
        self.assertEqual(smart_text(channel), channel.name)


class TestCategory(TestCase):

    def test_create_model(self):
        channel = Channel.objects.create(name='Channel 1')
        category = Category.objects.create(channel=channel, name='Category 1')
        self.assertEqual(smart_text(category), category.name)


class TestImportCategoriesFromCsv(TestCase):

    def setUp(self):
        self.csv_path = os.path.join(
            django_apps.get_app_config('channels').path, 'tests/testdata.csv'
        )

    def test_import(self):
        import_categories_from_csv('wallmart', self.csv_path)
        channel = Channel.objects.get(name='wallmart')
        self.assertEqual(Category.objects.filter(channel=channel).count(), 23)
        books = Category.objects.get(channel=channel, name='Books')
        national_literature = Category.objects.get(name='National Literature')
        science_fiction = Category.objects.get(name='Science Fiction')
        self.assertIn(national_literature, books.children.all())
        self.assertIn(science_fiction, national_literature.children.all())
        self.assertEqual(science_fiction.parent, national_literature)
        self.assertEqual(national_literature.parent, books)
