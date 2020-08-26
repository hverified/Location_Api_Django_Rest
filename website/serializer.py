from rest_framework import serializers
from .models import (
    LocationData, Region, State, City, Country
)


class RegionSerializer(serializers.ModelSerializer):
    def __init__(self, *args, **kwargs):
        super(RegionSerializer, self).__init__(*args, **kwargs)

    class Meta:
        model = Region
        fields = '__all__'


class CountrySerializer(serializers.ModelSerializer):
    def __init__(self, *args, **kwargs):
        super(CountrySerializer, self).__init__(*args, **kwargs)

    class Meta:
        model = Country
        fields = '__all__'
        depth = 1


class StateSerializer(serializers.ModelSerializer):
    def __init__(self, *args, **kwargs):
        super(StateSerializer, self).__init__(*args, **kwargs)

    class Meta:
        model = State
        fields = '__all__'
        depth = 1


class CitySerializer(serializers.ModelSerializer):
    def __init__(self, *args, **kwargs):
        super(CitySerializer, self).__init__(*args, **kwargs)

    class Meta:
        model = City
        fields = '__all__'
        depth = 1


class LocationDataSerializer(serializers.ModelSerializer):
    def __init__(self, *args, **kwargs):
        super(LocationDataSerializer, self).__init__(*args, **kwargs)

    class Meta:
        model = LocationData
        fields = '__all__'
        depth = 1
