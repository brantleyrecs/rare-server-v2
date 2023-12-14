from django.db import models

class Post(models.Model):
  rare_user = models.ForeignKey(User, on_delete=models.CASCADE)
  category = models.ForeignKey(Category, on_delete=models.CASCADE)
  title = models.CharField(max_length=50)
  publication_date = models.DateField(auto_now=True)
  image_url=models.CharField()
  content=models.CharField()
  approved=models.IntegerField()
