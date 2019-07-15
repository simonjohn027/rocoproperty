from django import forms
from .models import Property,Room,Image

class PropertyForm(forms.ModelForm):
    class Meta:
        model = Property
        fields = ('owner', 'location','type','latitude',
                  'longitude','area','room_number','shared','slug','availability')




class ImageForm(forms.ModelForm):

    class Meta:
        model = Image
        fields = ('file','position' )

class RoomForm(forms.ModelForm):

    class Meta:
        model = Room
        fields = ('property','room_type','room_size','total' )

