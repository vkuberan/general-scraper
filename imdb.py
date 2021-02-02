from gs_lib import general
from bs4 import BeautifulSoup

link_src = 'https://www.imdb.com/title/tt0407887/'
movie_data = general.fetch_data(
    link_src, 'data/imdb/tt0407887-the-departed.html')

soup = BeautifulSoup(movie_data, 'lxml')

data = {}
data['title'] = soup.find('div', class_='title_wrapper').find(
    'h1').get_text(strip=True).replace('(', ' (')
data['subtext'] = soup.find('div', class_='title_wrapper').find(
    'div', class_='subtext').get_text(strip=True)
data['ratings'] = soup.find(
    'div', class_='ratingValue').get_text(strip=True)
data['total_users_rated'] = soup.find(
    'span', itemprop='ratingCount').get_text(strip=True)

movie_poster = soup.find('div', class_='poster').find('img')
if movie_poster is not None:
    data['poster'] = [movie_poster.get('alt'), movie_poster.get('src')]

movie_trailer = soup.find('div', class_='')

print(data)
