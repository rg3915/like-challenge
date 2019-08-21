from django.shortcuts import render
from myproject.core.models import Video
from myproject.core.forms import VideoForm
from django.views.generic import CreateView

def index(request):
    videos = Video.objects.all()
    context = {'videos': videos}
    return render(request, 'index.html', context)


class VideoCreate(CreateView):
    model = Video
    template_name = 'add.html'
    form_class = VideoForm
    success_url = '/'