from django.contrib import admin
from .models import SpiceGallery, SpiceMix

class SpiceGalleryAdmin(admin.ModelAdmin):
    fields = ['name', 'color', 'basic_description', 'extended_description']

class SpiceMixAdmin(admin.ModelAdmin):
    fields = ['name', 'color', 'origin', 'spices', 'dishes']

admin.site.register(SpiceGallery, SpiceGalleryAdmin)
admin.site.register(SpiceMix, SpiceMixAdmin)
