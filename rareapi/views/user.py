from rest_framework.viewsets import ViewSet
from rest_framework import serializers, status
from rest_framework.response import Response
from rareapi.models import User

class UserView(ViewSet):
  
  def list(self, request):
    """GET request for a list of all registered users"""
    users = User.objects.all()
    serializer = UserSerializer(users, many=True)
    return Response(serializer.data)
  
  def retrieve(self, request, pk):
    
    try:
        user = User.objects.get(pk=pk)
        serializer = UserSerializer(user)
        return Response(serializer.data)
    except User.DoesNotExist as ex:
        return Response({'message': ex.args[0]}, status=status.HTTP_404_NOT_FOUND)
  
  def update(self, request, pk):
      """PUT request to update user"""
      user = User.objects.get(pk=pk)
      uid = request.META["HTTP_AUTHORIZATION"]
      user.first_name = request.data['firstName']
      user.last_name = request.data['lastName']
      user.bio = request.data['bio']
      user.profile_image_url = request.data['profileImageUrl']
      user.email = request.data['email']
      user.uid = uid
      user.save()
      return Response({'message': 'User Information Was Updated'}, status=status.HTTP_204_NO_CONTENT)

class UserSerializer(serializers.ModelSerializer):
    
  class Meta:
    model = User
    fields = ('id', 'first_name', 'last_name', 'bio', 'profile_image_url', 'email', 'created_on', 'uid')
    depth = 1
