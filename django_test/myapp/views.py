from django.shortcuts import render
from django.http import HttpResponse

from rest_framework import generics
from .models import Post
from .serializers import PostSerializer

# Create your views here.
def home(request):
    return HttpResponse("Hello, Django")




# Create and List (GET and POST)
class PostListCreateView(generics.ListCreateAPIView):
    queryset = Post.objects.all()
    serializer_class = PostSerializer

# Read, Update, Delete (GET, PUT, DELETE)
class PostDetailView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Post.objects.all()
    serializer_class = PostSerializer