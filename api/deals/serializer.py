from rest_framework import serializers
from .models import *


# Сериализация нашей модели в формат json

class DealsSerializer(serializers.ModelSerializer):
    def create(self, data):
        Deals.objects.create(**data)


    class Meta:
        model = Deals
        fields = '__all__'


