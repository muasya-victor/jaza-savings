from rest_framework import viewsets
from .models import CustomUser
from .serializers import CustomUserSerializer


class CustomUserViewSet(viewsets.ModelViewSet):
    queryset = CustomUser.objects.all()
    serializer_class = CustomUserSerializer

    def get_queryset(self):
        """Optionally restricts the returned users to a given user."""
        queryset = CustomUser.objects.all()
        # Implement filtering or other query modifications here if needed
        return queryset
