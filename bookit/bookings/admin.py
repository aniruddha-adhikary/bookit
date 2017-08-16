from django.contrib import admin

from bookings.models import Booking


@admin.register(Booking)
class BookingAdmin(admin.ModelAdmin):
    pass
