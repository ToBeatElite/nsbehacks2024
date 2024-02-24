from rest_framework import generics

from .models import *
from .serializers import *

class ListSocialPosts(generics.ListAPIView):
    queryset = SocialPostModel.objects.all()
    serializer_class = SocialPostSerializer
class CreateSocialPosts(generics.CreateAPIView):
    queryset = SocialPostModel.objects.all()
    serializer_class = SocialPostSerializer

    
"""

# TODO: Fix these for full API functionality

class DetailSocialPosts(generics.RetrieveUpdateAPIView):
    queryset = SocialPostModel.objects.all()
    serializer_class = SocialPostSerializer

class DeleteSocialPosts(generics.DestroyAPIView):
    queryset = SocialPostModel.objects.all()
    serializer_class = SocialPostSerializer

"""
