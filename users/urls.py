from rest_framework.routers import DefaultRouter
from .views import ProfileViewSet, FollowViewSet, UserSearchViewSet

router = DefaultRouter()
router.register(r'profiles', ProfileViewSet, basename='profile')
router.register(r'follows', FollowViewSet, basename='follow')
router.register(r'search', UserSearchViewSet, basename='user-search')
urlpatterns = router.urls