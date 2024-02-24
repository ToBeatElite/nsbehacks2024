from rest_framework import serializers

from .models import *

class SocialPostSerializer(serializers.ModelSerializer):
    class Meta:
        model = SocialPostModel
        fields = ["id", "author", "title", "content", "post_zone"]

class JobSerializer(serializers.ModelSerializer):
    class Meta:
        model = JobModel
        fields = ["title", "description", "city"]

class EventSerializer(serializers.ModelSerializer):
    class Meta:
        model = EventModel
        fields = ["title", "description", "city"]