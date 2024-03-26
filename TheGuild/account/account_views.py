from rest_framework import generics, permissions, status
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework.authtoken.models import Token
from django.contrib.auth.models import User
from django.contrib.auth import authenticate
from rest_framework.permissions import IsAuthenticated
from .serializer import UserSerializer
from django.http import HttpResponse
from django.template import loader

class UserLoginView(APIView):
    def post(self, request):
        user = authenticate(username=request.data['username'], password=request.data['password'])
        if user:
            token, created = Token.objects.get_or_create(user=user)
            return Response({'token': token.key, 'id':user.id}, status=status.HTTP_200_OK)
        else:
            print(user)
            return Response('Could not find user', status=status.HTTP_401_UNAUTHORIZED)
    
class UserRegisterView(APIView):
    def post(self, request):
        user = User.objects.create_user(request.data['username'], request.data['email'],request.data['password'])
        user.save()
        return Response('User created', status=status.HTTP_200_OK)

class UserDeleteView(APIView):
    permission_classes = [IsAuthenticated] 
    def delete(self, request):
        user = User.objects.get(id=request.user.id)
        user.delete()
        return Response('User Deleted ' + user.username)
    
class UserListView(generics.ListAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer
    permission_classes=[IsAuthenticated]
    
class UserDetailView(generics.RetrieveAPIView):
    serializer_class = UserSerializer
    permission_classes=[IsAuthenticated]
    queryset=User.objects.all()
    
    def get(self,request,*args, **kwargs):
        return self.retrieve(request,*args, **kwargs)
    
class LoginView(APIView):
    queryset= User.objects.all();
    
    def get(self, request, *args, **kwargs):
        template = loader.get_template("Accounts/login.html")
        context = {
            "login": "yes",
        }
        return HttpResponse(template.render(context, request))