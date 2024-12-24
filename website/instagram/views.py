from rest_framework import viewsets, generics, status
from rest_framework.pagination import PageNumberPagination

from .models import UserProfile, Follow, Post, PostLike, Comment, CommentLike, Story, Saved, SaveItem
from .serializers import (UserSerializer, FollowSerializer, PostListSerializer, PostCreateSerializer,
                          PostLikeSerializer,
                          CommentLikeSerializer, CommentListCreateSerializer, SaveItemSerializer, SavedSerializer,
                          StorySerializer, LoginSerializer, UserProfileSerializer)
from rest_framework.filters import OrderingFilter, SearchFilter
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework.response import Response
from rest_framework_simplejwt.views import TokenObtainPairView
from rest_framework_simplejwt.tokens import RefreshToken


class RegisterView(generics.CreateAPIView):
    serializer_class = UserProfileSerializer

    def create(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        user = serializer.save()
        return Response(serializer.data, status=status.HTTP_201_CREATED)


class CustomLoginView(TokenObtainPairView):
    serializer_class = LoginSerializer

    def post(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        try:
            serializer.is_valid(raise_exception=True)
        except Exception:
            return Response({'detail': 'Неверные учетные данные'}, status=status.HTTP_401_UNAUTHORIZED)

        user = serializer.validated_data
        return Response(serializer.data, status=status.HTTP_200_OK)


class LogoutView(generics.GenericAPIView):
    def post(self, request, *args, **kwargs):
        try:
            refresh_token = request.data['refresh']
            token = RefreshToken(refresh_token)
            token.blacklist()
            return Response(status=status.HTTP_205_RESET_CONTENT)
        except Exception:
            return Response(status=status.HTTP_400_BAD_REQUEST)


class Pagination(PageNumberPagination):
    page_size = 2
    page_size_query_param = 'page_size'
    max_page_size = 100


class UserProfileListAPIView(generics.ListAPIView):
    queryset = UserProfile.objects.all()
    serializer_class = UserSerializer


class UserProfileCreateAPIView(generics.CreateAPIView):
    serializer_class = UserSerializer

    def get_queryset(self):
        return UserProfile.objects.filter(username=self.request.username)


class FollowListAPIView(generics.ListAPIView):
    queryset = Follow.objects.all()
    serializer_class = FollowSerializer


class PostListAPIView(generics.ListAPIView):
    queryset = Post.objects.all()
    serializer_class = PostListSerializer
    filter_backends = [SearchFilter, OrderingFilter, DjangoFilterBackend]
    filterset_fields = ['hashtag']
    search_fields = ['username', ]
    ordering_fields = ['created_at']
    ordering = ['-created_at']
    pagination_class = Pagination


class PostCreateAPIView(generics.CreateAPIView):
    serializer_class = PostCreateSerializer


class PostLikeListAPIView(generics.ListAPIView):
    queryset = PostLike.objects.all()
    serializer_class = PostLikeSerializer


class PostLikeCreateAPIView(generics.CreateAPIView):
    serializer_class = PostLikeSerializer


class CommentListCreateAPIView(generics.CreateAPIView):
    queryset = Comment.objects.all()
    serializer_class = CommentListCreateSerializer


class CommentLikeCreateAPIView(generics.CreateAPIView):
    serializer_class = CommentLikeSerializer


class StoryCreateAPIView(generics.CreateAPIView):
    serializer_class = StorySerializer


class StoryListAPIView(generics.ListAPIView):
    queryset = Story.objects.all()
    serializer_class = StorySerializer


class SavedViewSet(viewsets.ModelViewSet):
    queryset = Saved.objects.all()
    serializer_class = SavedSerializer


class SaveItemViewSet(viewsets.ModelViewSet):
    queryset = SaveItem.objects.all()
    serializer_class = SaveItemSerializer






