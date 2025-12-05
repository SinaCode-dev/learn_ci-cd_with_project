from rest_framework import serializers

from .models import Application, Service, Comment


class ApplicationSerializer(serializers.ModelSerializer):
    class Meta:
        model = Application
        fields = ["title", "description", "top_service"]


class ServiceSerializer(serializers.ModelSerializer):
    class Meta:
        model = Service
        fields = ["name", "description", "price"]


class CommentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Comment
        fields = ["author", "body", "datetime_created"]