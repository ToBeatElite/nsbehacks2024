from django.db import models

class SocialPostModel(models.Model):
    author = models.CharField(max_length = 180)
    title = models.CharField(max_length = 180)
    content = models.CharField(max_length = 180)
    city = models.CharField(max_length = 180)
    timestamp = models.DateTimeField(auto_now_add = True, auto_now = False, blank = True)

    def __str__(self):
        return self.task
    
class JobModel(models.Model):
    title = models.CharField(max_length = 180)
    description = models.CharField(max_length = 180)
    city = models.CharField(max_length = 180)
    timestamp = models.DateTimeField(auto_now_add = True, auto_now = False, blank = True)

    def __str__(self):
        return self.task
    
class EventModel(models.Model):
    title = models.CharField(max_length = 180)
    description = models.CharField(max_length = 180)
    city = models.CharField(max_length = 180)
    timestamp = models.DateTimeField(auto_now_add = True, auto_now = False, blank = True)

    def __str__(self):
        return self.task
    