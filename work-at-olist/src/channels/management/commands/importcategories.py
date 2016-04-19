# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.core.management.base import BaseCommand

from src.channels.models import import_categories_from_csv


class Command(BaseCommand):
    help = 'Import categories from a csv file'

    def add_arguments(self, parser):
        parser.add_argument('channel')
        parser.add_argument('csvfile')

    def handle(self, *args, **options):
        import_categories_from_csv(options['channel'], options['csvfile'])
        self.stdout.write(
            self.style.SUCCESS('Categories imported successfully')
        )
