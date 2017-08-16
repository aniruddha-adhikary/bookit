from django.contrib import admin

from geo.models import Area


@admin.register(Area)
class AreaAdmin(admin.ModelAdmin):
    pass
