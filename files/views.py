"""
Views for the files app.
"""
from drf_spectacular.utils import (
    extend_schema,
)

from rest_framework import generics, authentication, permissions, status, renderers
from rest_framework.parsers import MultiPartParser, JSONParser, FormParser, FileUploadParser
from rest_framework.response import Response
from django.http import FileResponse
from rest_framework.decorators import action
from rest_framework.settings import api_settings
from .serializers import FileSerializer
from core.models import (
    File,
)


class PassthroughRenderer(renderers.BaseRenderer):
    """
        Return data as-is. View should supply a Response.
    """
    media_type = ''
    format = ''

    def render(self, data, accepted_media_type=None, renderer_context=None):
        return data


@extend_schema(tags=["files"])
class ShowFilesView(generics.ListAPIView):
    """Show all files in the system."""
    serializer_class = FileSerializer
    authentication_classes = [authentication.TokenAuthentication]
    permission_classes = [permissions.IsAuthenticated]

    def get_queryset(self):
        """Return objects for the current authenticated user only."""
        return File.objects.filter(user=self.request.user).order_by('-created_at')

    @action(methods=['get'], detail=True, renderer_classes=[PassthroughRenderer])
    def download(self, *args, **kwargs):
        instance = self.get_object()
        file_handle = instance.file.open()

        response = FileResponse(file_handle, as_attachment=True, filename=instance.file.name.split('/')[-1])
        response['Content-Length'] = instance.file.size
        response['Content-Disposition'] = 'attachment; filename="%s"' % instance.file.name

        return response


@extend_schema(tags=["files"])
class UploadFileView(generics.CreateAPIView):
    """Upload a file in the system."""
    parser_classes = (MultiPartParser, JSONParser, FormParser, FileUploadParser)
    authentication_classes = [authentication.TokenAuthentication]
    permission_classes = [permissions.IsAuthenticated]
    serializer_class = FileSerializer

    def post(self, request, *args, **kwargs):
        file = request.data.get('file')

        if file:
            data = File.objects.create(
                user=request.user,
                file=file,
            )
            data.save()

        return Response(
            {'message': 'File uploaded successfully.',
             'data': {
                 data.file.name.split('/')[-1],
             },
             },

            content_type='application/json',
            status=status.HTTP_201_CREATED)


@extend_schema(tags=["files"])
class ManageFileView(generics.RetrieveUpdateDestroyAPIView):
    """Manage the authenticated user."""
    serializer_class = FileSerializer
    authentication_classes = [authentication.TokenAuthentication]
    permission_classes = [permissions.IsAuthenticated]

    def get_queryset(self):
        """Return objects for the current authenticated user only."""
        return self.queryset.filter(user=self.request.user).order_by('-created_at')

    def perform_update(self, serializer):
        """Update the file."""
        serializer.save(user=self.request.user, file=self.request.data.get('file'))

    def perform_destroy(self, instance):
        """Delete the file."""
        if instance.file:
            instance.file.delete()
            instance.delete()
            return Response(
                {'message': 'File deleted successfully.',
                 'data': {
                     instance.file.name.split('/')[-1],
                 },
                 },

                content_type='application/json',
                status=status.HTTP_200_OK)
        return Response(
            {'message': 'File not found.',
             'data': {
                 instance.file.name.split('/')[-1],
             },
             },

            content_type='application/json',
            status=status.HTTP_404_NOT_FOUND)


