from rest_framework.decorators import api_view
from django.http import HttpResponseServerError
from rest_framework.decorators import action
from rest_framework.viewsets import ViewSet
from rest_framework.response import Response
from rest_framework import serializers, status
from rareapi.models import User

@api_view(['POST'])
def check_user(request):
    '''Checks to see if User has Associated User Account

    Method arguments:
      request -- The full HTTP request object
    '''
    uid = request.data['uid']

    # Use the built-in authenticate method to verify
    # authenticate returns the user object or None if no user is found
    user = User.objects.filter(uid=uid).first()

    # If authentication was successful, respond with their token
    if user is not None:
        data = {
            'id': user.id,
            'first_name': user.first_name,
            'last_name': user.last_name,
            'bio': user.bio,
            'profile_image_url': user.profile_image_url,
            'email': user.email,
            'created_on': user.created_on,
            'active': user.active,
            'is_staff': user.is_staff,
            'uid': user.uid
        }
        return Response(data)
    else:
        # Bad login details were provided. So we can't log the user in.
        data = { 'valid': False }
        return Response(data)


@api_view(['POST'])
def register_user(request):
    '''Handles the creation of a new user for authentication

    Method arguments:
      request -- The full HTTP request object
    '''

    user = User.objects.create(
        first_name=request.data["firstName"],
        last_name=request.data["lastName"],
        bio=request.data["bio"],
        profile_image_url=request.data["profileImageUrl"],
        email=request.data["email"],
        created_on=request.data["createdOn"],
        active=request.data["active"],
        is_staff=request.data["isStaff"],
        uid=request.data["uid"]
    )

    # Return the user info to the client
    data = {
        'id': user.id,
        'first_name': user.first_name,
        'last_name': user.last_name,
        'bio': user.bio,
        'profile_image_url': user.profile_image_url,
        'email': user.email,
        'created_on': user.created_on,
        'active': user.active,
        'is_staff': user.is_staff,
        'uid': user.uid
    }
    return Response(data)
  
class UserView(ViewSet):
  
  def retrieve(self, request, pk):
    
    try:
        user = User.objects.get(pk=pk)
        serializer = UserSerializer(user)
        return Response(serializer.data)
    except User.DoesNotExist as ex:
        return Response({'message': ex.args[0]}, status=status.HTTP_404_NOT_FOUND)

class UserSerializer(serializers.ModelSerializer):
    
  class Meta:
    model = User
    fields = ('id', 'first_name', 'last_name', 'bio', 'profile_image_url', 'email', 'created_on', 'active', 'is_staff', 'uid')
    depth = 1
