from  rest_framework import serializers
from ..models import carlist
class CarSerlizers(serializers.Serializer):
    id=serializers.IntegerField(read_only=True)
    name=serializers.CharField()
    description=serializers.CharField()
    active=serializers.BooleanField(read_only=True)

    def create(self, validated_data):
        return carlist.objects.create(**validated_data)