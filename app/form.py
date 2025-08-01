from django import forms

from django import forms


class DistanceForm(forms.Form):
    lat1 = forms.FloatField(
        label='Latitude 1',
        help_text='Coloque a primeira latitude em decimais.'
    )
    lon1 = forms.FloatField(
        label='Longitude 1',
        help_text='Coloque a primeira longitude em decimais.'
    )
    lat2 = forms.FloatField(
        label='Latitude 2',
        help_text='Coloque a segunda latitude em decimais.'
    )
    lon2 = forms.FloatField(
        label='Longitude 2',
        help_text='Coloque a segunda longitude em decimais.'
    )