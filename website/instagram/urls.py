from .views import *
from rest_framework import routers
from django.urls import path, include

router = routers.SimpleRouter()
router.register(r'user', UserProfileViewSet, basename='users')
router.register(r'follow', FollowViewSet, basename='follows')
router.register(r'post', PostViewSet, basename='posts')
router.register(r'post_like', PostLikeViewSet, basename='post_like')
router.register(r'comment', CommentViewSet, basename='comment')
router.register(r'comment_like', CommentLikeViewSet, basename='comment_like')
router.register(r'story', StoryViewSet, basename='stories')
router.register(r'saved', SavedViewSet, basename='saved')
router.register(r'save_item', SaveItemViewSet, basename='save_item')

urlpatterns = [
    path('', include(router.urls)),
]