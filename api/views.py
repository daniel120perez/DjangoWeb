from django.shortcuts import render
from .models import Worker
from .serializers import WorkerSerializer
from rest_framework import viewsets, views, filters, generics
# Create your views here.

class WorkerViewSet(viewsets.ModelViewSet):

    queryset = Worker.objects.all()
    serializer_class = WorkerSerializer

    filter_backends = [filters.SearchFilter, filters.OrderingFilter]
    search_fields = ['name']
    ordering_fields = ['id']

class WorkerDetail(generics.RetrieveUpdateDestroyAPIView):

    queryset = Worker.objects.all()
    serializer_class = WorkerSerializer