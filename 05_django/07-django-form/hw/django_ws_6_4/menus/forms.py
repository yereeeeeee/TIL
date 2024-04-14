from django import forms
from .models import Menu


class MenuForm(forms.ModelForm):
    name = forms.CharField(
        widget=forms.TextInput(
            attrs={
                'placeholder':'메뉴 이름을 작성해 주세요.',
                'class': 'form-control'
            }
        )
    )
    price = forms.IntegerField(
        widget=forms.TextInput(
            attrs={
                'class': 'form-control'
            }
        )
    )
    description = forms.CharField(
        widget=forms.Textarea(
            attrs={
                'placeholder':'메뉴 설명을 작성해 주세요.',
                'class': 'form-control'
            }
        )
    )
    
    class Meta:
        model = Menu
        fields = '__all__'