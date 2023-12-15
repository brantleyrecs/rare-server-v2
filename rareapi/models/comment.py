from django.db import models
from .user import User
from .post import Post

class Comment(models.Model):
  user = models.ForeignKey(User, on_delete=models.CASCADE)
  post = models.ForeignKey(Post, on_delete=models.CASCADE)
  content = models.TextField()
  created_on = models.DateField()
