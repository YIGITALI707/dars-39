from rest_framework import serializers
from .models import *




class CarSerializers(serializers.ModelSerializer):
    class Meta:
        model=Car
        fields='__all__'


class BrandSerializers(serializers.ModelSerializer):
    class Meta:
        model=Brand
        fields='__all__'


class ColorSerializers(serializers.ModelSerializer):
    class Meta:
        model=Color
        fields='__all__'