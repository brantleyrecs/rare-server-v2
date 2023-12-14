from django.db import models
from .user import User

class Comment(models.Model):
  user = models.ForeignKey(User, on_delete=models.CASCADE)
  content = models.TextField()
  created_on = models.DateField()
  time = models.TimeField()
  post = models.ForeignKey(Post, on_delete=models.CASCADE)
