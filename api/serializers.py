from rest_framework import serializers
from .models import Building, Floor, Room, Marker


class BuildingSerializer(serializers.ModelSerializer):
    class Meta:
        model = Building
        fields = '__all__'


class FloorSerializer(serializers.ModelSerializer):
    class Meta:
        model = Floor
        fields = '__all__'


class RoomSerializer(serializers.ModelSerializer):
    class Meta:
        model = Room
        fields = '__all__'


class MarkerSerializer(serializers.ModelSerializer):
    class Meta:
        model = Marker
        fields = '__all__'

        # depth = 2
