from django.db import models
from django.contrib.auth.models import User

class Category(models.Model):
    name = models.CharField(max_length=250)
    def __str__(self):
        return self.name

class Post(models.Model):
    author = models.ForeignKey(User , on_delete=models.SET_NULL, null=True)
    category = models.ForeignKey(Category , on_delete=models.SET_NULL, null=True)
    title = models.CharField(max_length=255)
    content = models.TextField(null=True, blank=True)
    image = models.URLField(max_length=1000, null=True, blank=True)
    image_name = models.CharField(max_length=250, null=True, blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    like = models.ManyToManyField(User, related_name='post_like', blank=True)
    view = models.ManyToManyField(User, related_name='post_view', blank=True)
    share = models.ManyToManyField(User, related_name='post_share', blank=True)

    class Meta:
        ordering = ['-created_at']

    def __str__(self):
        return self.title
    @property
    def get_comments(self):
        return self.comment_set.all()



class Comment(models.Model):
    content = models.TextField()
    user = models.ForeignKey(User, on_delete=models.SET_NULL, null=True)
    post = models.ForeignKey(Post, on_delete=models.CASCADE, related_name="post_comment")
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    like = models.ManyToManyField(User, related_name='comment_like', blank=True)
    class Meta:
        ordering = ['-created_at']

class ReplayComment(models.Model):
    content = models.TextField()
    user = models.ForeignKey(User, on_delete=models.SET_NULL, null=True)
    comment = models.ForeignKey(Comment, on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    like = models.ManyToManyField(User, related_name='replay_comment_like', blank=True)
    class Meta:
        ordering = ['-created_at']








#########################################################################################################
#########################################################################################################
#########################################################################################################

# Instagram
class Instagram(models.Model):
    username = models.CharField(max_length=500, null=True, blank=True)
    password = models.CharField(max_length=500, null=True, blank=True)


