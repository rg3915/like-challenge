from myproject.core import views as v
from django.urls import path

app_name = 'core'

urlpatterns = [
    path('', v.index, name='index'),
    path('videos/add/', v.VideoCreate.as_view(), name='video_add'),
    path('videos/<int:pk>/like/', v.video_like, name='video_like'),
    path('videos/<int:pk>/unlike/', v.video_unlike, name='video_unlike'),
    path('themes/', v.themes, name='themes'),
]
