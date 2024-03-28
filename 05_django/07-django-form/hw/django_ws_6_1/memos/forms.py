from django import forms

class MemoForm(forms.Form):
  memo = forms.TextField()
  summary = forms.CharField(max_length=20)
  created_at = forms.DateTimeField(auto_now_add=True)
  updated_at = forms.DateTimeField(auto_now=True)