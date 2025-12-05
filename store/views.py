from django.shortcuts import render

from rest_framework.viewsets import ModelViewSet

from .serializers import ApplicationSerializer, ServiceSerializer, CommentSerializer
from .models import Application, Service, Comment


class ApplicationViewSet(ModelViewSet):
    serializer_class = ApplicationSerializer
    queryset = Application.objects.all()


class ServiceViewSet(ModelViewSet):
    serializer_class = ServiceSerializer
    
    def get_queryset(self):
        application_pk = self.kwargs["application_pk"]
        return Service.objects.filter(application_id=application_pk).all()


class CommentViewSet(ModelViewSet):
    serializer_class = CommentSerializer
    
    def get_queryset(self):
        application_pk = self.kwargs["application_pk"]
        service_pk = self.kwargs["service_pk"]
        return Comment.objects.filter(service_id=service_pk, service__application_id=application_pk).all()