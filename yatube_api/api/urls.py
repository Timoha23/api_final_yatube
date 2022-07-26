from rest_framework import routers
from django.urls import path, include

from .views import PostViewSet, CommentViewSet, GroupViewSet, FollowViewSet

router = routers.DefaultRouter()
router.register(r'posts', PostViewSet)
router.register(r'groups', GroupViewSet)
router.register(r'posts/(?P<post_id>\d+)/comments', CommentViewSet, basename='comments')
router.register(r'follow', FollowViewSet, basename='following')

urlpatterns = [
    path('v1/', include(router.urls)),
    path('v1/auth/', include('djoser.urls')),
    path('v1/', include('djoser.urls.jwt')),
]
