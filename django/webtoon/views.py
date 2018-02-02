from django.shortcuts import render
from .models import Webtoon, Episode


# Create your views here.

def webtoon_list(request):
    webtoons = Webtoon.objects.all()
    context = {
        'webtoons':webtoons,
    }
    return render(request, 'webtoon/webtoon_list.html',context)


def webtoon_detail(request, pk):
    episodes = Episode.objects.filter(webtoon_id=pk)
    context = {
        'episodes':episodes,
    }
    return render(request, 'webtoon/webtoon_detail.html', context)