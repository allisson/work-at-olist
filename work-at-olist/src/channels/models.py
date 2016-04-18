# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.db import models
from django.utils.encoding import python_2_unicode_compatible

from mptt.models import MPTTModel, TreeForeignKey
import uuid


class CreateUpdateModel(models.Model):

    created_at = models.DateTimeField(
        'created at',
        auto_now_add=True
    )
    updated_at = models.DateTimeField(
        'updated at',
        auto_now=True
    )

    class Meta:
        abstract = True


@python_2_unicode_compatible
class Channel(CreateUpdateModel):

    id = models.UUIDField(
        primary_key=True,
        default=uuid.uuid4,
        editable=False
    )

    name = models.CharField(
        'name',
        max_length=100
    )

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'channel'
        verbose_name_plural = 'channels'
        ordering = ['name']


@python_2_unicode_compatible
class Category(MPTTModel, CreateUpdateModel):

    id = models.UUIDField(
        primary_key=True,
        default=uuid.uuid4,
        editable=False
    )

    channel = models.ForeignKey(
        'Channel',
        verbose_name='channel',
        related_name='categories'
    )

    parent = TreeForeignKey(
        'self',
        null=True,
        blank=True,
        related_name='children',
        db_index=True
    )

    name = models.CharField(
        'name',
        max_length=100
    )

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'category'
        verbose_name_plural = 'categories'
        ordering = ['name']

    class MPTTMeta:
        order_insertion_by = ['name']
