from django.contrib import admin
from .models import Hall, Booking
from django.utils.html import format_html

# Register your models here.
class HallAdmin(admin.ModelAdmin):
    list_display = ('name', 'capacity', 'price', 'image_preview')

    def image_preview(self, obj):
        if obj.image:
            return format_html('<img src="{}" width="100" />', obj.image.url)
        return "No Image"
    image_preview.short_description = 'Image'
admin.site.register(Hall, HallAdmin)
admin.site.register(Booking)
