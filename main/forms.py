from django import forms
from .models import Property, Room, Image


class PropertyForm(forms.ModelForm):
    class Meta:
        model = Property
        fields = ('owner', 'location', 'type', 'latitude',
                  'longitude', 'area', 'room_number', 'shared', 'slug', 'availability')


class ImageForm(forms.ModelForm):
    class Meta:
        model = Image
        fields = ('file', 'position')


class RoomForm(forms.ModelForm):
    class Meta:
        model = Room
        fields = ('property', 'room_type', 'room_size', 'total')


class ContactForm(forms.Form):
    name = forms.CharField(max_length=250, widget=forms.TextInput(
        attrs={'size': 30,
               'title': 'Your Name',
               'required': "required",
               'name': "author",
               'aria-required': "true"}
    ))
    subject = forms.CharField(max_length=300, widget=forms.TextInput(
        attrs={
            'title': 'Subject',
            'required': "required",
            'name': "subject",
            'aria-required': "true"}
    ))
    email = forms.EmailField(widget=forms.EmailInput(
        attrs={'title': 'Email',
               'required': "required",
               'name': "email",
               'aria-required': "true"}
    ))
    message = forms.CharField(widget=forms.Textarea(
        attrs={'title': 'Your Message',
               'required': "required",
               'name': "comment",
               'cols': "45",
               'rows': "8",
               'aria-required': "true"}
    ))
