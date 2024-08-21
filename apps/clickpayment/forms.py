from django import forms

from .models import Contacts, Booking


class ContactForm(forms.ModelForm):
    class Meta:
        model = Contacts
        fields = ['name', 'email', 'subject', 'message']


class BookingForm(forms.ModelForm):
    class Meta:
        model = Booking
        exclude = ()


from django import forms


class TripSearchForm(forms.Form):
    destination = forms.CharField(
        max_length=100,
        required=False,
        label='Package Name',
        widget=forms.TextInput(attrs={'placeholder': 'Enter package name'})
    )
    depart_time = forms.DateTimeField(
        required=False,
        widget=forms.TextInput(attrs={'type': 'datetime-local'}),
        label='Departure Time'
    )
    return_time = forms.DateTimeField(
        required=False,
        widget=forms.TextInput(attrs={'type': 'datetime-local'}),
        label='Return Time'
    )
    duration = forms.DurationField(
        required=False,
        widget=forms.TextInput(attrs={'placeholder': 'Enter duration (e.g., 2 days, 3:00:00)'}),
        label='Duration'
    )

    def clean(self):
        cleaned_data = super().clean()
        departure_time = cleaned_data.get('departure_time')
        return_time = cleaned_data.get('return_time')

        if departure_time and return_time and return_time <= departure_time:
            raise forms.ValidationError('Return time must be after departure time.')

        return cleaned_data
