from django import forms
from .models import Restaurant, Menu


class RestaurantForm(forms.ModelForm):
    opening_time = forms.TimeField(widget=forms.TimeInput(format='%H:%M', attrs={'type': 'time'}))
    closing_time = forms.TimeField(widget=forms.TimeInput(format='%H:%M', attrs={'type': 'time'}))

    class Meta:
        model = Restaurant
        fields = '__all__'

class MenuForm(forms.ModelForm):
    
    class Meta:
        model = Menu
        exclude = ('restaurant', )

class MenuUpdateForm(forms.ModelForm):

    class Meta:
        model = Menu
        exclude = ('restaurant', 'name',)