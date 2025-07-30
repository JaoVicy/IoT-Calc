from django import forms

from django import forms

class DistanceFrom(forms.Form):
    lat1 = forms.FloatField(
        label='Latitude 1',
        help_text='Enter the first latitude in decimal degrees.'
    )
    lon2 = forms.FloatField(
        label='Longitude 2',
        help_text='Enter the second longitude in decimal degrees.'
    )
    lat2 = forms.FloatField(
        label='Latitude 2',
        help_text='Enter the second latitude in decimal degrees.'
    )
    lon2 = forms.FloatField(
        label='Longitude 2',
        help_text='Enter the first longitude in decimal degrees.'
    )