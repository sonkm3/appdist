from django.contrib import admin

from .models import DistApp


class DistAppAdmin(admin.ModelAdmin):
    list_display = ('id', 'title', 'detail', 'package_file', )

admin.site.register(DistApp, DistAppAdmin)
