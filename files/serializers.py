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
import magic

class FileSerializer(serializers.ModelSerializer):
    """Serializer for the file object."""
    name = serializers.CharField(source='file.name', read_only=True)
    size = serializers.SerializerMethodField('get_size')
    file_type = serializers.SerializerMethodField('get_file_type')

    class Meta:
        model = File
        fields = ['file', 'size', 'user', 'created_at', 'name', 'file_type']
        extra_kwargs = {'file': {'write_only': True},'created_at': {'read_only': True}, 'size': {'read_only': True}, 'user': {'read_only': True}}

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

    @staticmethod
    def get_size(obj):
        return obj.file.size

    @staticmethod
    def get_file_type(obj):
        return magic.from_buffer(obj.file.read(1024), mime=True)

