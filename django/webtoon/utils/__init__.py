import requests
import re
from bs4 import BeautifulSoup as bs
def search_webtoon(keyword):
    url = 'http://comic.naver.com/search.nhn'
    i = 1
    result = []
    while True:
        param = {
            'm': 'webtoon',
            'keyword': keyword,
            'type': 'title',
            'page': i,
        }
        response = requests.get(url, param)
        soup = bs(response.text, 'lxml')
        div_result = soup.find('div', class_='resultBox')
        title_list = div_result.find('ul', class_='resultList').findAll('h5')
        if not title_list:
            break
        p = re.compile(r'titleId=(.*)')
        for title in title_list:
            id_href = title.find('a').get('href')
            webtoon_id = re.search(p, id_href).group(1)
            result.append({
                'webtoon_id': webtoon_id,
                'title': title.find('a').text,
            })

        i += 1
    return result