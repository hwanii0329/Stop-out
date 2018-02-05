from django.db import models
import requests
import re
from bs4 import BeautifulSoup as bs


class Webtoon(models.Model):
    webtoon_id = models.CharField(max_length=200)
    title = models.CharField(max_length=200)

    def get_episode_list(self):
        url = 'http://comic.naver.com/webtoon/list.nhn'
        i = 1
        while True:
            param = {
                'titleId': self.webtoon_id,
                'page': i,
            }
            response = requests.get(url, param)
            soup = bs(response.text, 'lxml')
            tr_list = soup.find('table', class_='viewList').findAll('tr')[1:]

            for tr in tr_list:
                if tr.get('class') and 'band_banner' in tr.get('class'):
                    continue
                p = re.compile(r'no=(.*?)&')
                episode_url = tr.find('td').find('a').get('href')
                episode_id = re.search(p, episode_url).group(1)
                if Episode.objects.filter(webtoon_id=self.pk).filter(episode_id=episode_id).exists():
                    continue
                title = tr.find('td', class_='title').find('a').text
                rating = tr.find('div', class_='rating_type').find('strong').text
                created_date = tr.find('td', class_='num').text
                # url_thumbnail = tr.find('td').find('img').get('src')
                Episode.objects.create(
                    episode_id=episode_id,
                    # url_thumbnail=url_thumbnail,
                    title=title,
                    rating=rating,
                    created_date=created_date,
                    webtoon_id=self.pk,
                )
            print(f'last epi: {episode_id}')
            print(f'page: {i}')
            if episode_id == '1':
                break
            i += 1


class Episode(models.Model):
    webtoon = models.ForeignKey(Webtoon, on_delete=models.CASCADE)
    episode_id = models.CharField(max_length=200)
    title = models.CharField(max_length=200)
    rating = models.CharField(max_length=200)
    created_date = models.CharField(max_length=200)

    def __str__(self):
        return f'Episode: {self.webtoon} | {self.title}'

    class Meta:
        ordering = ['-created_date']
