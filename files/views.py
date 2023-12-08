"""
Views for the files app.
"""
from drf_spectacular.utils import (
    extend_schema,
)

from rest_framework import generics, authentication, permissions
from rest_framework.settings import api_settings
from .serializers import FileSerializer
from core.models import (
    File,
)


@extend_schema(tags=["files"])
class ShowFilesView(generics.ListAPIView):
    """Show all files in the system."""
    serializer_class = FileSerializer
    authentication_classes = [authentication.TokenAuthentication]
    permission_classes = [permissions.IsAuthenticated]

    def get_queryset(self):
        """Return objects for the current authenticated user only."""
        return File.objects.filter(user=self.request.user).order_by('-size')