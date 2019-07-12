from rest_framework import  serializers
from main.models import Property, Room,Image,Price
from accs.models import User


class PropertySerializer(serializers.ModelSerializer):
    owner = serializers.CharField(source='owner.full_name',read_only = True)
    rooms = serializers.StringRelatedField(many = True)
    price = serializers.StringRelatedField(many=True)
    images = serializers.StringRelatedField(many=True)
    class Meta:
        model = Property
        fields = ('owner','location', 'type','latitude','longitude','area','room_number',
                  'availability','slug', 'created_on', 'rooms','price','images')



class UserSerializer(serializers.ModelSerializer):
    property = serializers.PrimaryKeyRelatedField(many = True, queryset=Property.objects.all())
    class Meta:
        model = User
        fields = ('email','full_name', 'property')



class RoomSerializer(serializers.ModelSerializer):

    class Meta:
        model = Room
        fields = ('room_type','room_size','total')


class ImageSerializer(serializers.ModelSerializer):
    class Meta:
        model = Image
        fields = ('file','position')

class PriceSerializer(serializers.ModelSerializer):
    class Meta:
        model = Price
        fields = ('lease','price')





