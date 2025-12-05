from django.shortcuts import render

from rest_framework.viewsets import ModelViewSet

from .serializers import ApplicationSerializer
from .models import Application


class ApplicationViewSet(ModelViewSet):
    serializer_class = ApplicationSerializer
    queryset = Application.objects.all()