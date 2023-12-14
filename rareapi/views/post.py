from django.http import HttpResponseServerError
from rest_framework.response import Response

class PostView(ViewSet):
  def retrieve(self, request, pk):
    post = Post.objects.get(pk=pk)
    serializer = PostSerializer(post)
    
  def list(self, request):
    games = Post.objects.all()
    serializer = PostSerializer(posts, many=True)
    return Response(serializer.data)
  
  def create(self, request):
    user = User.objects.get(uid=request.data["userId"]) #might need to change to "uid"
    category = Category.objects.get(pk=request.data["categoryId"])
    