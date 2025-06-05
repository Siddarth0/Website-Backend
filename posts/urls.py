from rest_framework.routers import DefaultRouter
from .views import PostViewSet, CommentViewSet, LikeViewSet, StreamViewSet

router = DefaultRouter()
router.register(r'posts', PostViewSet, basename='post')
router.register(r'comments', CommentViewSet, basename='comment')
router.register(r'stream', StreamViewSet, basename='stream')
router.register(r'likes', LikeViewSet, basename='like')
urlpatterns = router.urls
