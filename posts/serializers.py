from rest_framework import serializers
from .models import Post, Comment, Like, Stream

class CommentSerializer(serializers.ModelSerializer):
    user = serializers.StringRelatedField(read_only=True)

    class Meta:
        model = Comment
        fields = '__all__'
        read_only_fields = ['user', 'created_at']

class LikeSerializer(serializers.ModelSerializer):
    user = serializers.StringRelatedField(read_only=True)

    class Meta:
        model = Like
        fields = '__all__'
        read_only_fields = ['id', 'timestamp']

class PostSerializer(serializers.ModelSerializer):
    user = serializers.StringRelatedField(read_only=True)
    like_count = serializers.SerializerMethodField()
    comments = CommentSerializer(many=True, read_only=True)

    class Meta:
        model = Post
        fields = ['id', 'user', 'picture', 'caption', 'created_at', 'like_count', 'comments']

    def get_like_count(self, obj):
        return obj.likes.count()


class StreamSerializer(serializers.ModelSerializer):
    post = serializers.StringRelatedField()
    following = serializers.StringRelatedField()
    user = serializers.StringRelatedField()

    class Meta:
        model = Stream
        fields = ['id', 'user', 'following', 'post', 'date']
