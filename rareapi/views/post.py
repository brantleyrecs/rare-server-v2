from django.http import HttpResponseServerError
from rest_framework.response import Response
from rest_framework.viewsets import ViewSet
from rest_framework import serializers, status
from rareapi.models import Post, User, Category

class PostView(ViewSet):
  def retrieve(self, request, pk):
    post = Post.objects.get(pk=pk)
    serializer = PostSerializer(post)
    return Response(serializer.data)
    
  def list(self, request):
    posts = Post.objects.all()
    serializer = PostSerializer(posts, many=True)
    return Response(serializer.data)
  
  def create(self, request):
    user_id = User.objects.get(pk=request.data["user_id"]) 
    category = Category.objects.get(pk=request.data["categoryId"])
    
    post = Post.objects.create(
      rare_user=user_id,
      category=category,
      title=request.data["title"],
      publication_date=request.data["publicationDate"],
      image_url=request.data["imageUrl"],
      content=request.data["content"],
      approved=request.data["approved"]
    )
    serializer = PostSerializer(post)
    return Response(serializer.data)
  
  def update(self, request, pk):
    post = Post.objects.get(pk=pk)
    post.title=request.data["title"]
    post.publication_date=request.data["publicationDate"]
    post.image_url=request.data["imageUrl"]
    post.content=request.data["content"]
    post.approved=request.data["approved"]
    
    rare_user=User.objects.get(uid=request.data["uid"]) 
    post.rare_user=rare_user
    
    category=Category.objects.get(pk=request.data["category"])
    post.category = category
    post.save()
    
    return Response(None, status=status.HTTP_204_NO_CONTENT)
    
  
  def destroy(self, request, pk):
    post = Post.objects.get(pk=pk)
    post.delete()
    return Response(None, status=status.HTTP_204_NO_CONTENT)
    
class PostSerializer(serializers.ModelSerializer):
  class Meta:
    model=Post
    fields = ('id', 'rare_user', 'category', 'title', 'publication_date', 'image_url', 'content', 'approved')
