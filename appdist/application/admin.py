from django.contrib import admin

from .models import DistApp


class DistAppAdmin(admin.ModelAdmin):
    list_display = ('id', 'title', 'detail', 'display', 'package_file', )
    readonly_fields = ('bundle_identifier', 'bundle_version')

admin.site.register(DistApp, DistAppAdmin)
