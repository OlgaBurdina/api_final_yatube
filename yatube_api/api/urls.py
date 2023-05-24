from django.urls import path, include
from rest_framework import routers

from .views import (
    PostViewSet,
    GroupViewSet,
    CommentViewSet,
    FollowView
)

router = routers.DefaultRouter()

router.register(
    r'posts/(?P<post_id>\d+)/comments',
    CommentViewSet,
    basename='comment'
)
router.register(r'posts', PostViewSet)
router.register(r'groups', GroupViewSet)

urlpatterns = [
    path('v1/', include('djoser.urls')),
    path('v1/', include('djoser.urls.jwt')),
    path('v1/', include(router.urls)),
    path('v1/follow/', FollowView.as_view()),
]
