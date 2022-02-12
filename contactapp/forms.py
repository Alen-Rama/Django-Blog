from django import forms


class Contact(forms.Form):
    name=forms.CharField(label='Name', required=True)
    email=forms.EmailField(label='Email', required=True)
    subject=forms.CharField(label='Subject', required=True, widget=forms.Textarea)

