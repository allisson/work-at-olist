# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.contrib import admin

from mptt.admin import MPTTModelAdmin

from src.channels.models import Channel, Category


class ChannelAdmin(admin.ModelAdmin):

    list_display = ('name', 'created_at', 'updated_at')


class CategoryAdmin(MPTTModelAdmin):

    list_display = ('name', 'channel', 'created_at', 'updated_at')
    list_filter = ('channel', )
    mptt_level_indent = 20


admin.site.register(Channel, ChannelAdmin)
admin.site.register(Category, CategoryAdmin)
