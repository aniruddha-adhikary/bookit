from django.contrib import admin

from providers.models import ProviderService, Provider


@admin.register(Provider)
class ProviderAdmin(admin.ModelAdmin):
    list_display = ('name', 'area')


@admin.register(ProviderService)
class ProviderServiceAdmin(admin.ModelAdmin):
    list_display = ('name', 'provider', 'price')

    def get_queryset(self, request):
        return super().get_queryset(request).select_related('provider')


