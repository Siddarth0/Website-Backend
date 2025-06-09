from rest_framework.routers import DefaultRouter
from django.urls import path
from .views import ProfileViewSet, FollowViewSet, UserSearchViewSet, RegisterView

router = DefaultRouter()
router.register(r'profiles', ProfileViewSet, basename='profile')
router.register(r'follows', FollowViewSet, basename='follow')

urlpatterns = router.urls + [
    path('register/', RegisterView.as_view(), name='register'),
]

urlpatterns = router.urls