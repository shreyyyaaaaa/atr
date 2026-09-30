from django.shortcuts import render
from .models import Hotel
from .forms import BookingRequestForm


def home(request):
    return render(request, 'core/home.html')


def agriculture(request):
    return render(request, 'core/agriculture.html')


def tourism(request):
    hotels = Hotel.objects.all()

    return render(
        request, 
        'core/tourism.html',
        {'hotels': hotels}
    )


def resorts(request):
    return render(request, 'core/resorts.html')


def hotels(request):
    return render(request, 'core/hotels.html')


def hotel_detail(request, hotel_id):
    hotel = Hotel.objects.get(id=hotel_id)
    rooms = hotel.rooms.all()

    return render(
        request,
          'core/hotel_detail.html',
          {
              'hotel': hotel,
              'rooms': rooms
          }
        )


def booking(request):

    if request.method == 'POST':
        form = BookingRequestForm(request.POST)

        if form.is_valid():
            form.save()

            return render(
                request,
                'core/booking_success.html'
            )

    else:
        form = BookingRequestForm()

    return render(
        request,
        'core/booking.html',
        {'form': form}
    )

def about(request):
    return render(request, 'core/about.html')


def contact(request):
    return render(request, 'core/contact.html')

def gallery(request):
    return render(request, 'core/gallery.html')