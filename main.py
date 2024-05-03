from bs4 import BeautifulSoup
import requests

response = requests.get(
    'https://web.archive.org/web/20200518073855/https://www.empireonline.com/movies/features/best-movies-2/')
print("encoding is", response.encoding)  # prints: ISO-8859-1
response.encoding = "utf-8"
empire_website = response.text
soup = BeautifulSoup(empire_website, "html.parser")
top_100_movies = [movie.text for movie in soup.find_all(name="h3", class_="title")]
top_100_movies = top_100_movies[::-1]
with open('movies.txt', mode='w') as file:
    for i in top_100_movies:
        file.write(i+"\n")

