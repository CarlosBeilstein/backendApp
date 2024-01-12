from rest_framework import serializers
from .models import FavStocks

class ListSerializer(serializers.ModelSerializer):
    class Meta:
        model = FavStocks
        fields = '__all__'