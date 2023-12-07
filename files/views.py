"""
Views for the files app.
"""

from rest_framework import generics, authentication, permissions
from rest_framework.settings import api_settings
from drf_spectacular.utils import extend_schema
from .serializers import FileSerializer

@extend_schema(tags=["files"])
class CreateFileView(generics.CreateAPIView):
    """Create a new file in the system."""
    serializer_class = FileSerializer
    authentication_classes = [authentication.TokenAuthentication]
    permission_classes = [permissions.IsAuthenticated]

    def perform_create(self, serializer):
        """Create a new file."""
        serializer.save(user=self.request.user)
@extend_schema(tags=["files"])
class ListFileView(generics.ListAPIView):
    """List all files in the system."""
    serializer_class = FileSerializer
    authentication_classes = [authentication.TokenAuthentication]
    permission_classes = [permissions.IsAuthenticated]

    def get_queryset(self):
        """Retrieve the files for the authenticated user."""
        return self.request.files.all()

@extend_schema(tags=["files"])
class ManageFileView(generics.RetrieveUpdateDestroyAPIView):
    """Manage the authenticated file."""
    serializer_class = FileSerializer
    authentication_classes = [authentication.TokenAuthentication]
    permission_classes = [permissions.IsAuthenticated]

    def get_object(self):
        """Retrieve and return the authenticated file."""
        return self.request.files

