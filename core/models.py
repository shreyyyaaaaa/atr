from django.db import models

class Hotel(models.Model):
    name = models.CharField(max_length=200)
    location = models.CharField(max_length=200)
    description = models.TextField()
    image = models.ImageField(
        upload_to='hotels/',
        blank=True,
        null=True
    )
    contact_email = models.EmailField(blank=True)
    phone = models.CharField(max_length=20, blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.name

class Room(models.Model):
    hotel = models.ForeignKey(
        Hotel,
        on_delete=models.CASCADE,
        related_name='rooms'
    )
    room_type = models.CharField(max_length=100)
    room_number = models.CharField(max_length=50)
    description = models.TextField(blank=True)
    capacity = models.PositiveIntegerField()
    price = models.DecimalField(
        max_digits=10,
        decimal_places=2
    )

    facilities = models.TextField(blank=True)
    image = models.ImageField(
        upload_to='rooms/',
        blank=True,
        null=True
    )
    is_available = models.BooleanField(default=True)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.hotel.name} - {self.room_type}"

class BookingRequest(models.Model):

    STATUS_CHOICES = [
        ('Pending', 'Pending'),
        ('Confirmed', 'Confirmed'),
        ('Rejected', 'Rejected'),
    ]

    customer_name = models.CharField(max_length=200)
    email = models.EmailField()
    phone = models.CharField(max_length=20)

    hotel = models.ForeignKey(
        Hotel,
        on_delete=models.CASCADE,
        related_name='booking_requests'
    )

    room = models.ForeignKey(
        Room,
        on_delete=models.CASCADE,
        related_name='booking_requests'
    )

    check_in = models.DateField()
    check_out = models.DateField()

    number_of_guests = models.PositiveIntegerField()

    message = models.TextField(blank=True)

    status = models.CharField(
        max_length=20,
        choices=STATUS_CHOICES,
        default='Pending'
    )

    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.customer_name} - {self.hotel.name}"