from rest_framework import serializers
from .models import Drink

class DrinkSerialzer(serializers.ModelSerializer):
    class Meta:
        model = Drink
        fields = ['id', 'name', 'description']