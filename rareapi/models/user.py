from django.db import models

class User(models.Model):
  first_name = models.CharField(max_length=55)
  last_name = models.CharField(max_length=55)
  bio = models.CharField(max_length=55)
  profile_image_url = models.CharField(max_length=200)
  email = models.CharField(max_length=55)
  created_on = models.DateField()
  uid = models.CharField(max_length=55)
