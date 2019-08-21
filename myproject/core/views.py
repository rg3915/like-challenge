from django.shortcuts import render
from myproject.core.models import Video

def index(request):
    return render(request, 'index.html')

def videos(request):
    videos = Video.objects.all()
    context = {'videos': videos}
    return render(request, 'listar.html', context)