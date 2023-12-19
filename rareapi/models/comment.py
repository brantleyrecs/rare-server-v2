from django.db import models
from .user import User
from .post import Post

class Comment(models.Model):
  user = models.ForeignKey(User, on_delete=models.CASCADE, related_name = 'comments')
  post = models.ForeignKey(Post, on_delete=models.CASCADE, related_name = 'comments')
  content = models.TextField()
  created_on = models.DateField(auto_now_add=True)
