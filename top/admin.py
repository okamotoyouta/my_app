from django.contrib import admin

from .models import Update, UpdateDetail

class DetailInline(admin.StackedInline):
    model = UpdateDetail
    extra = 0

class DetailInline(admin.StackedInline):
    model = UpdateDetail
    extra = 0

class UpdateAdmin(admin.ModelAdmin):
    inlines = [DetailInline]
    list_display = ("id", "title")
    list_display_links = ("id", "title")



admin.site.register(Update, UpdateAdmin)

admin.site.register(UpdateDetail)
