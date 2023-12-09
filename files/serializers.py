"""
Serializers for the files API view
"""
from django.contrib.auth import (
    get_user_model,
    authenticate,
)
from django.utils.translation import gettext as _
from django.core.files.uploadedfile import InMemoryUploadedFile
from rest_framework import serializers
from core.models import File
import os
USER = get_user_model()

class FileSerializer(serializers.ModelSerializer):
    """Serializer for the file object."""
    name = serializers.SerializerMethodField('get_name')
    size = serializers.SerializerMethodField('get_size')
    # file_type = serializers.SerializerMethodField('get_file_type')
    # filepath = serializers.SerializerMethodField('get_filepath')

    class Meta:
        model = File
        fields = ['file', 'size', 'created_at', 'name']
        extra_kwargs = {
            'file': {'write_only': True},
            'created_at': {'read_only': True},
            'size': {'read_only': True},
            'user': {'read_only': True}
        }

    def create(self, validated_data):
        """Set the user when creating a new File instance"""
        validated_data['user'] = self.context['request'].user
        return super().create(validated_data)

    def update(self, instance, validated_data):
        """Update and return a file."""
        file = validated_data.pop('file', None)
        file = super().update(instance, validated_data)

        if file:
            file.set_file(file)
            file.save()

        return file

    @staticmethod
    def get_size(obj):
        return obj.file.size

    @staticmethod
    def get_name(obj):
        return obj.file.name.split('\\')[-1]
    # @staticmethod
    # def get_file_type(obj):
    #     return magic.from_buffer(obj.file.read(1024), mime=True)
