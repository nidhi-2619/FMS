"""
Serializers for the files API view
"""
from django.contrib.auth import (
    get_user_model,
    authenticate,
)
from django.utils.translation import gettext as _
from rest_framework import serializers
from core.models import File

class FileSerializer(serializers.ModelSerializer):
    """Serializer for the file object."""

    class Meta:
        model = File
        fields = ['file', 'name', 'description']
        extra_kwargs = {'file': {'write_only': True}}

    def create(self, validated_data):
        """Create and return a file with encrypted password"""
        return File.objects.create(**validated_data)

    def update(self, instance, validated_data):
        """Update and return a file."""
        file = validated_data.pop('file', None)
        file = super().update(instance, validated_data)

        if file:
            file.set_file(file)
            file.save()

        return file

