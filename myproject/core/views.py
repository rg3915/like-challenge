from django.shortcuts import render
from myproject.core.models import Video

def index(request):
    videos = Video.objects.all()
    context = {'videos': videos}
    return render(request, 'index.html', context)
