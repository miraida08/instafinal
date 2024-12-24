from .views import *
from django.urls import path, include

urlpatterns = [
    path('user_list/', UserProfileListAPIView.as_view(), name='user_list'),
    path('user_create/', UserProfileCreateAPIView.as_view(), name='user_create'),
    path('follow/', FollowListAPIView.as_view(), name='store_list'),
    path('post_list/', PostListAPIView.as_view(), name='post_list'),
    path('post_create/', PostCreateAPIView.as_view(), name='post_create'),
    path('postlike_list/', PostLikeListAPIView.as_view(), name='postlike_list'),
    path('postlike_create/', PostLikeCreateAPIView.as_view(), name='postlike_create'),
    path('comment/', CommentListCreateAPIView.as_view(), name='comment'),
    path('comment_like/', CommentLikeCreateAPIView.as_view(), name='comment_like'),
    path('story_list/', StoryListAPIView.as_view(), name='story_list'),
    path('story_create/', StoryCreateAPIView.as_view(), name='story_create'),
    path('saved/', SavedViewSet.as_view({'get': 'list'}), name='saved'),
    path('saved/<int:pk>/', SaveItemViewSet.as_view({'put': 'update'}), name='save'),
    path('register/', RegisterView.as_view(), name='register'),
    path('login/', CustomLoginView.as_view(), name='login'),
    path('logout/', LogoutView.as_view(), name='logout'),
]