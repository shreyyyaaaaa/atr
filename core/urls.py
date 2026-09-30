from django.urls import path
from . import views


urlpatterns = [

    path('', views.home, name='home'),

    path(
        'agriculture/',
        views.agriculture,
        name='agriculture'
    ),

    path(
        'tourism/',
        views.tourism,
        name='tourism'
    ),

    path(
        'resorts/',
        views.resorts,
        name='resorts'
    ),

    path(
        'hotels/',
        views.hotels,
        name='hotels'
    ),

    path(
        'hotel/<int:hotel_id>/',
        views.hotel_detail,
        name='hotel_detail'
    ),

    path(
        'booking/',
        views.booking,
        name='booking'
    ),

    path(
        'about/',
        views.about,
        name='about'
    ),

    path(
        'contact/',
        views.contact,
        name='contact'
    ),
    path('gallery/', views.gallery, name='gallery')
]