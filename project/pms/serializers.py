from rest_framework import serializers
from .models import WorkOrder, MaidRequest, TechnicianRequest, AmenityRequest


class MaidRequestSerializer(serializers.ModelSerializer):
    class Meta:
        model = MaidRequest
        fields = '__all__'


class TechnicianRequestSerializer(serializers.ModelSerializer):
    class Meta:
        model = TechnicianRequest
        fields = '__all__'


class AmenityRequestSerializer(serializers.ModelSerializer):
    class Meta:
        model = AmenityRequest
        fields = '__all__'


class WorkOrderSerializer(serializers.ModelSerializer):
    maid_request = MaidRequestSerializer(read_only=True)
    technician_request = TechnicianRequestSerializer(read_only=True)
    amenity_request = AmenityRequestSerializer(read_only=True)

    class Meta:
        model = WorkOrder
        fields = '__all__'
