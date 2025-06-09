from rest_framework import viewsets, permissions, filters, generics
from .models import Profile, Follow
from . serializers import ProfileSerializer, FollowSerializer, RegisterSerializer
from rest_framework.permissions import IsAuthenticatedOrReadOnly
from posts.permissions import IsOwnerOrReadOnly
from django.contrib.auth.models import User

class ProfileViewSet(viewsets.ModelViewSet):
    queryset = Profile.objects.select_related('user').all()
    serializer_class = ProfileSerializer
    permission_classes = [permissions.IsAuthenticated, IsOwnerOrReadOnly]
    filter_backends = [filters.SearchFilter]
    search_fields = ['user__username']

    def perform_update(self, serializer):
        serializer.save(user=self.request.user)

class FollowViewSet(viewsets.ModelViewSet):
    queryset = Follow.objects.all()
    serializer_class = FollowSerializer
    permission_classes = [permissions.IsAuthenticated]

    def perform_create(self, serializer):
        serializer.save(follower=self.request.user)


class RegisterView(generics.CreateAPIView):
    queryset = User.objects.all()
    serializer_class = RegisterSerializer