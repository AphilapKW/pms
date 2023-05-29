from rest_framework import generics
from .models import WorkOrder, MaidRequest, TechnicianRequest, AmenityRequest
from .serializers import WorkOrderSerializer, MaidRequestSerializer, TechnicianRequestSerializer, AmenityRequestSerializer


class WorkOrderList(generics.ListCreateAPIView):
    queryset = WorkOrder.objects.all()
    serializer_class = WorkOrderSerializer


class WorkOrderDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = WorkOrder.objects.all()
    serializer_class = WorkOrderSerializer


class MaidRequestList(generics.ListCreateAPIView):
    queryset = MaidRequest.objects.all()
    serializer_class = MaidRequestSerializer


class MaidRequestDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = MaidRequest.objects.all()
    serializer_class = MaidRequestSerializer


class TechnicianRequestList(generics.ListCreateAPIView):
    queryset = TechnicianRequest.objects.all()
    serializer_class = TechnicianRequestSerializer


class TechnicianRequestDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = TechnicianRequest.objects.all()
    serializer_class = TechnicianRequestSerializer


class AmenityRequestList(generics.ListCreateAPIView):
    queryset = AmenityRequest.objects.all()
    serializer_class = AmenityRequestSerializer


class AmenityRequestDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = AmenityRequest.objects.all()
    serializer_class = AmenityRequestSerializer
