from django.http import HttpResponseServerError
from rest_framework.response import Response
from rest_framework.viewsets import ViewSet
from rest_framework import serializers, status
from rareapi.models import Post, User, Category, Comment
from rareapi.serializers import CommentSerializer
from rest_framework.decorators import action
from django.db.models import Count

class PostView(ViewSet):
  def retrieve(self, request, pk):
    post = Post.objects.annotate(comment_count=Count('comments')).get(pk=pk)
    serializer = PostSerializer(post)
    return Response(serializer.data)
    
  def list(self, request):
    posts = Post.objects.annotate(comment_count=Count('comments')).all()
    serializer = PostSerializer(posts, many=True)
    return Response(serializer.data)
  
  def create(self, request):
    uid = User.objects.get(pk=request.data["uid"]) 
    category = Category.objects.get(pk=request.data["categoryId"])
    
    post = Post.objects.create(
      rare_user=uid,
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
    
    rare_user=User.objects.get(pk=request.data["uid"]) 
    post.rare_user=rare_user
    
    category=Category.objects.get(pk=request.data["categoryId"])
    post.category = category
    post.save()
    
    return Response(None, status=status.HTTP_204_NO_CONTENT)
    
  
  def destroy(self, request, pk):
    post = Post.objects.get(pk=pk)
    post.delete()
    return Response(None, status=status.HTTP_204_NO_CONTENT)
  
  @action(methods=['post'], detail=True)
  def post_comment(self, request, pk):
    """Method to post a comment on a single post"""
    author_id = User.objects.get(pk=request.data["user"])
    post_id = Post.objects.get(pk=pk)
    user_comment = Comment.objects.create(
      user=author_id,
      post=post_id,
      content=request.data["content"],
      created_on=request.data["createdOn"]
    )
    return Response({'message': 'Comment posted!'}, status=status.HTTP_201_CREATED)
  
  @action(methods=['get'], detail=True)
  def comments(self, request, pk):
    """Method to get all the comments associated to a single post"""
    comments = Comment.objects.all()
    associated_post = comments.filter(post_id=pk)
    
    serializer = CommentSerializer(associated_post, many=True)
    return Response(serializer.data)
    
class PostSerializer(serializers.ModelSerializer):
  comment_count = serializers.IntegerField(default=None)
  class Meta:
    model=Post
    fields = ('id', 'rare_user', 'category', 'title', 'publication_date', 'image_url', 'content', 'approved', 'comment_count')
    depth = 1
