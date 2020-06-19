from django.contrib import admin

from .models import Topics





class TopicsAdmin(admin.ModelAdmin):
    list_display = ("id", "title")
    list_display_links = ("id", "title")



admin.site.register(Topics, TopicsAdmin)
