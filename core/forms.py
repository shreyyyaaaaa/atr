from django import forms
from .models import BookingRequest

class BookingRequestForm(forms.ModelForm):

    class Meta:
        model = BookingRequest

        fields =[
            'customer_name',
            'email',
            'phone',
            'hotel',
            'room',
            'check_in',
            'check_out',
            'number_of_guests',
            'message',
        ]

        widgets = {
            'check_in': forms.DateInput(
                attrs={'type': 'date'}
            ),
            'check_out': forms.DateInput(
                attrs={'type': 'date'}
            ),
            'message': forms.Textarea(
                attrs={'rows':4}
            ),
        }
    def clean(self):
        cleaned_data = super().clean()

        hotel = cleaned_data.get('hotel')
        room = cleaned_data.get('room')
        check_in = cleaned_data.get('check_in')
        check_out = cleaned_data.get('check_out')
        guests = cleaned_data.get('number_of_guests')

        if check_in and check_out:
            if check_out <= check_in:
                self.add_error(
                    'check_out',
                    'Check-out date must be after check-in date.'
                )

        if hotel and room:
            if room.hotel != hotel:
                self.add_error(
                    'room',
                    'The selected room does not belong to the selected hotel.'
                )

        if room and guests:
            if guests > room.capacity:
                self.add_error(
                    'number_of_guests',
                    f'This room can accommodate only {room.capacity} guests.'
                )

        if room and not room.is_available:
            self.add_error(
                'room',
                'This room is currently unavailable.'
            )

        return cleaned_data
