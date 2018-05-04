from rest_framework import serializers
from CarPositions.models import CarPosition

class CarPositionSerializer(serializers.ModelSerializer):
    class Meta:
        model = CarPosition
        field = ('carPosition_id', 'position_id', 'user_id', 'is_driveOut', 'time_created')

    def create(self, validate_data):
        return CarPosition.objects.create(**validate_data)

    def update(self, instance, validate_data):
        instance.is_driveOut = validate_data.get('is_driveOut',instance.is_driveOut)
        instance.save()
        
        return instance