from django.db import models
from django.contrib.auth.models import AbstractUser


class UserProfile(AbstractUser):
    bio = models.TextField()
    image = models.ImageField(upload_to='user_image/', null=True, blank=True)
    website = models.URLField()


class Follow(models.Model):
    follower = models.ForeignKey(UserProfile, on_delete=models.CASCADE, related_name='follower')
    following = models.ForeignKey(UserProfile, on_delete=models.CASCADE, related_name='following')
    created_at = models.DateField(auto_now_add=True)


class Post(models.Model):
    user = models.ForeignKey(UserProfile, on_delete=models.CASCADE, related_name='user')
    image = models.ImageField(upload_to='post_image/', null=True, blank=True)
    video = models.FileField(upload_to='post_video/', null=True, blank=True)
    hashtag = models.TextField()
    created_at = models.DateField(auto_now_add=True)


class PostLike(models.Model):
    user = models.ForeignKey(UserProfile, on_delete=models.CASCADE, related_name='like_user')
    post = models.ForeignKey(Post, on_delete=models.CASCADE, related_name='post_like')
    like = models.BooleanField(default=False)
    created_at = models.DateTimeField(auto_now_add=True)


class Comment(models.Model):
    post = models.ForeignKey(Post, on_delete=models.CASCADE, related_name='post_comment')
    user = models.ForeignKey(UserProfile, on_delete=models.ForeignKey, related_name='user_comment')
    text = models.TextField()
    parent = models.ForeignKey('self', related_name='reviews', null=True, blank=True, on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)


class CommentLike(models.Model):
    user = models.ForeignKey(UserProfile, on_delete=models.ForeignKey, related_name='user_like')
    comment = models.ForeignKey(Comment, on_delete=models.ForeignKey, related_name='comment_like')
    like = models.BooleanField(default=False)
    created_at = models.DateTimeField(auto_now_add=True)


class Story(models.Model):
    user = models.ForeignKey(UserProfile, on_delete=models.ForeignKey, related_name='user_story')
    image = models.ImageField(upload_to='story_image/', null=True, blank=True)
    video = models.FileField(upload_to='story_video/', null=True, blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    like = models.BooleanField(default=False)


class Saved(models.Model):
    user = models.OneToOneField(UserProfile, on_delete=models.CASCADE, related_name='saved')


class SaveItem(models.Model):
    post = models.ForeignKey(Post, on_delete=models.CASCADE, related_name='saved_post')
    save = models.ForeignKey(Saved, on_delete=models.CASCADE, related_name='saved_item')
    created_date = models.DateField(auto_now_add=True)
