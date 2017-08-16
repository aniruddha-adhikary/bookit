from django.contrib import admin

from bookings.models import Booking, Ticket


@admin.register(Booking)
class BookingAdmin(admin.ModelAdmin):
    pass


@admin.register(Ticket)
class TicketAdmin(admin.ModelAdmin):
    pass
