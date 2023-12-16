from rest_framework import serializers
from rareapi.models import Comment

class CommentSerializer(serializers.ModelSerializer):
    
  class Meta:
    model = Comment
    fields = ('id', 'user', 'post', 'content', 'created_on')
    depth = 0
