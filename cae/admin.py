# -*- coding: utf-8 -*-
from django.contrib import admin

from .models import Section, Division, CAE


@admin.register(Section)
class SectionAdmin(admin.ModelAdmin):
    list_display = ['code', 'name']
    ordering = ['code']
    search_fields = ['code', 'name']


@admin.register(Division)
class DivisionAdmin(admin.ModelAdmin):
    list_display = ['code', 'formatted_code', 'name', 'section']
    ordering = ['code']
    search_fields = ['code', 'name', 'section']
    list_filter = ['section']


@admin.register(CAE)
class CAEAdmin(admin.ModelAdmin):
    list_display = ['code', 'formatted_code', 'name', 'level']
    ordering = ['code']
    search_fields = ['code', 'name', 'level']
    list_filter = ['level']
