from django.shortcuts import render, redirect
from .models import Webtoon, Episode
from webtoon import utils


# Create your views here.

def webtoon_list(request):
    webtoons = Webtoon.objects.all()
    context = {
        'webtoons': webtoons,
    }
    return render(request, 'webtoon/webtoon_list.html', context)


def webtoon_detail(request, pk):
    episodes = Episode.objects.filter(webtoon_id=pk)
    context = {
        'episodes': episodes,
    }
    return render(request, 'webtoon/webtoon_detail.html', context)


def index(request):
    return render(request, 'webtoon/index.html')


def search_list(request):
    keyword = request.GET['keyword']
    context = {
        'search_list': utils.search_webtoon(keyword),
    }
    return render(request, 'webtoon/search_list.html', context)


def save_webtoon(request, webtoon_id, title):

    if not Webtoon.objects.filter(webtoon_id=webtoon_id).exists():
        webtoon = Webtoon.objects.create(
            webtoon_id=webtoon_id,
            title=title,
        )
        webtoon.get_episode_list()
        return redirect('webtoon:webtoon-detail', pk=webtoon.pk)
    else:
        toon = Webtoon.objects.get(webtoon_id=webtoon_id)
        print(toon)
        return redirect('webtoon:webtoon-detail', pk=toon.pk)
