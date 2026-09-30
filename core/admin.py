from django.contrib import admin
from .models import Hotel, Room, BookingRequest

@admin.register(Hotel)
class HotelAdmin(admin.ModelAdmin):
    list_display = (
        'name',
        'location',
        'contact_email',
        'phone',
    )

@admin.register(Room)
class RoomAdmin(admin.ModelAdmin):
    list_display = (
        'hotel',
        'room_type',
        'room_number',
        'capacity',
        'price',
        'is_available',
    )

@admin.register(BookingRequest)
class BookingRequestAdmin(admin.ModelAdmin):
    list_display = (
        'customer_name',
        'hotel',
        'room',
        'check_in',
        'check_out',
        'status',
        'created_at',
    )

    list_filter = (
        'status',
        'hotel',
    )
