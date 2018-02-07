import requests
from bs4 import BeautifulSoup as bs
import re


class EpisodeData:
    def __init__(self, episode_id, url_thumbnail, title, rating, created_date):
        self.episode_id = episode_id
        self.url_thumbnail = url_thumbnail
        self.title = title
        self.rating = rating
        self.created_date = created_date

    def __str__(self):
        return f'episode_id: {self.episode_id} | title: {self.title} | rating: {self.rating} | created_date: {self.created_date} | url_thumbnail: {self.url_thumbnail}'


def get_episode_list(webtoon_id, page):
    url = 'http://comic.naver.com/webtoon/list.nhn'
    param = {
        'titleId': webtoon_id,
        'page': page,
    }
    response = requests.get(url, param)
    soup = bs(response.text, 'lxml')
    tr_list = soup.find('table', class_='viewList').findAll('tr')[1:]
    result = []
    for tr in tr_list:
        if tr.get('class') and 'band_banner' in tr.get('class'):
            continue
        title = tr.find('td', class_='title').find('a').text
        rating = tr.find('div', class_='rating_type').find('strong').text
        created_date = tr.find('td', class_='num').text
        url_thumbnail = tr.find('td').find('img').get('src')
        p = re.compile(r'no=(.*?)&')
        episode_url = tr.find('td').find('a').get('href')
        episode_id = re.search(p, episode_url).group(1)
        episode = EpisodeData(
            episode_id=episode_id,
            url_thumbnail=url_thumbnail,
            title=title,
            rating=rating,
            created_date=created_date,
        )
        result.append(episode)
    return result


if __name__ == '__main__':

    for toon in get_episode_list(183559, 1):
        print(toon)
