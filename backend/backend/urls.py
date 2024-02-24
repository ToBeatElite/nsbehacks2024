from django.contrib import admin
from django.urls import path

from api.views import *

urlpatterns = [

    # admin access
    path('admin/', admin.site.urls),
    
    # endpoints for social posts
    path('posts/create', CreateSocialPosts.as_view()),
    path('posts/', ListSocialPosts.as_view()),
    path('posts/<int:pk>', DetailSocialPost.as_view()),
    path('posts/delete/<int:pk>', DeleteSocialPosts.as_view()),

    # endpoints for event entries
    path('events/create', CreateEvents.as_view()),
    path('events/', ListEvents.as_view()),
    path('events/<int:pk>', DetailEvents.as_view()),
    path('events/delete/<int:pk>', DeleteEvents.as_view()),

    # endpoints for job entries
    path('jobs/create', CreateJobs.as_view()),
    path('jobs/', ListJobs.as_view()),
    path('jobs/<int:pk>', DetailJobs.as_view()),
    path('jobs/delete/<int:pk>', DeleteJobs.as_view()),

]
