from myproject.core import views as v
from django.urls import path

app_name = 'core'

urlpatterns = [
    path('', v.index, name='index'),
    path('videos/add/', v.VideoCreate.as_view(), name='video_add'),
]
