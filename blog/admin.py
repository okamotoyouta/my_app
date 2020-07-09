from django.contrib import admin

from .models import Post, PostContent

class ContentInline(admin.StackedInline):
    model = PostContent
    extra = 1

class PostAdmin(admin.ModelAdmin):
    inlines = [ContentInline]
    list_display = ("id", "title")
    list_display_links = ("id", "title")



admin.site.register(Post, PostAdmin)

admin.site.register(PostContent)
