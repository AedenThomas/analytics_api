from django.shortcuts import render

from rest_framework import viewsets
from .models import PageView
from .serializers import PageViewSerializer

class PageViewViewSet(viewsets.ModelViewSet):
    queryset = PageView.objects.all()
    serializer_class = PageViewSerializer
