from django import forms


class ai_form(forms.Form):
    data = forms.CharField(label="", required=True, widget=forms.Textarea(attrs={'rows':5}))