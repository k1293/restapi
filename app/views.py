from django.shortcuts import render
from .models import List
from .serializers import ListSerializer
from rest_framework import viewsets

# Create your views here.

class ListViewSet(viewsets.ModelViewSet):
    queryset = List.objects.all()
    serializer_class = ListSerializer
