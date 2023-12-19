from django.db import models
from .user import User
from .category import Category

class Post(models.Model):
  rare_user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='user')
  category = models.ForeignKey(Category, on_delete=models.CASCADE)
  title = models.CharField(max_length=50)
  publication_date = models.DateField(auto_now=True)
  image_url=models.CharField(max_length=100)
  content=models.CharField(max_length=100)
