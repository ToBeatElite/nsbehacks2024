from rest_framework import generics

from .models import *
from .serializers import *

class ListSocialPosts(generics.ListAPIView):
    queryset = SocialPostModel.objects.all()
    serializer_class = SocialPostSerializer
class CreateSocialPosts(generics.CreateAPIView):
    queryset = SocialPostModel.objects.all()
    serializer_class = SocialPostSerializer
class DetailSocialPost(generics.RetrieveUpdateAPIView):
    queryset = SocialPostModel.objects.all()
    serializer_class = SocialPostSerializer
class DeleteSocialPosts(generics.DestroyAPIView):
    queryset = SocialPostModel.objects.all()
    serializer_class = SocialPostSerializer

class ListEvents(generics.ListAPIView):
    queryset = EventModel.objects.all()
    serializer_class = EventSerializer
class CreateEvents(generics.CreateAPIView):
    queryset = EventModel.objects.all()
    serializer_class = EventSerializer
class DetailEvents(generics.RetrieveUpdateAPIView):
    queryset = EventModel.objects.all()
    serializer_class = EventSerializer
class DeleteEvents(generics.DestroyAPIView):
    queryset = EventModel.objects.all()
    serializer_class = EventSerializer

class ListJobs(generics.ListAPIView):
    queryset = JobModel.objects.all()
    serializer_class = JobSerializer
class CreateJobs(generics.CreateAPIView):
    queryset = JobModel.objects.all()
    serializer_class = JobSerializer
class DetailJobs(generics.RetrieveUpdateAPIView):
    queryset = JobModel.objects.all()
    serializer_class = JobSerializer
class DeleteJobs(generics.DestroyAPIView):
    queryset = JobModel.objects.all()
    serializer_class = JobSerializer

