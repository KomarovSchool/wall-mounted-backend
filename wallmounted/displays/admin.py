from django.contrib import admin
from django.contrib.contenttypes.admin import GenericTabularInline

from .models import Screen, SlideShow, Slide, ScreenContent


@admin.register(Screen)
class ScreenAdmin(admin.ModelAdmin):
    list_display = ('id', 'code')
    search_fields = ('code',)


class SlideInline(admin.TabularInline):
    model = Slide
    extra = 1
    ordering = ('order',)


@admin.register(SlideShow)
class SlideShowAdmin(admin.ModelAdmin):
    list_display = ('id', 'name')
    search_fields = ('name',)
    inlines = [SlideInline]


@admin.register(ScreenContent)
class ScreenContentAdmin(admin.ModelAdmin):
    list_display = ('screen', 'priority', 'time_range')
    list_filter = ('priority', 'time_range')
    search_fields = ('screen__code',)
