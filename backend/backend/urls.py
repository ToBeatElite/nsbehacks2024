from django.contrib import admin
from django.urls import path, include

from api.views import *

urlpatterns = [

    # admin access
    path('admin/', admin.site.urls),
    
    # endpoints for making social posts
    path('posts/create', CreateSocialPosts.as_view()),
    path('posts/', ListSocialPosts.as_view()),

    # TODO: fix these endpoints for full API functionality
    # path('posts/<int:id>/', DetailSocialPosts.as_view()),
    # path('posts/delete/<int:id>', DeleteSocialPosts.as_view())

]
