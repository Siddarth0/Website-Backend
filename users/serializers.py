from rest_framework import serializers
from .models import Profile, Follow
from django.contrib.auth.models import User

class ProfileSerializer(serializers.ModelSerializer):
    username = serializers.CharField(source='user.username')

    class Meta:
        model = Profile
        fields = ['id', 'user', 'image', 'first_name', 'last_name', 'bio', 'location']


class FollowSerializer(serializers.ModelSerializer):
    follower = serializers.ReadOnlyField(source='follower.username')
    following = serializers.SlugRelatedField(slug_field='username', queryset=User.objects.all())

    class Meta:
        model = Follow
        fields = ['id', 'follower', 'following']


class RegisterSerializer(serializers.ModelSerializer):
    password = serializers.CharField(write_only=True)

    class Meta:
        model = User
        fields = ['id', 'username', 'email', 'password']

    def create(self, validated_data):
        user = User.objects.create_user(
            username=validated_data['username'],
            email=validated_data.get('email'),
            password=validated_data['password']
        )
        return user