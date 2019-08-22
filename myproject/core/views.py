from django.db.models import Max
from django.http import JsonResponse
from django.shortcuts import render
from django.views.decorators.csrf import csrf_exempt
from django.views.generic import CreateView
from myproject.core.forms import VideoForm
from myproject.core.models import Video


def index(request):
    videos = Video.objects.all()
    context = {'videos': videos}
    return render(request, 'index.html', context)


class VideoCreate(CreateView):
    model = Video
    template_name = 'add.html'
    form_class = VideoForm
    success_url = '/'


@csrf_exempt
def video_like(request, pk):
    if request.method == 'POST' and request.is_ajax():
        data = request.POST
        like = data.get('like')
        video = Video.objects.get(pk=pk)
        video.like = like
        video.save()
        response = {'data': video.like}
        return JsonResponse(response)


@csrf_exempt
def video_unlike(request, pk):
    if request.method == 'POST' and request.is_ajax():
        data = request.POST
        unlike = data.get('unlike')
        video = Video.objects.get(pk=pk)
        video.unlike = unlike
        video.save()
        response = {'data': video.unlike}
        return JsonResponse(response)


def themes(request):
    template_name = 'themes.html'
    themes = Video.objects.values('theme__title').annotate(Max('score'))\
        .order_by('-score__max')
    context = {'themes': themes}
    return render(request, template_name, context)
