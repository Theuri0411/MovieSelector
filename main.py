import random
import requests
from bs4 import BeautifulSoup



url = 'https://www.imdb.com/chart/top'

def main():
    response = requests.get(url)
    html = response.text
 
    soup = BeautifulSoup(html, 'html.parser')
    movietags = soup.select ("td.titleColumn")
    innermovietags = soup.select('td.titleColumn a')
    rating_tags = soup.select ('td.posterColumn span [name=ir]')
   
    
    def get_year (movie_tag):
        moviesplit = movie_tag.text.split()
        year = moviesplit[-1]
        return year
    years = [get_year(tag) for tag in movietags]
    actors_list = [tag['title'] for tag in innermovietags]
    titles = [tag.text for tag in innermovietags]
    ratings = [float(tag ['data-value']) for tag in rating_tags]



    n_movies = len(titles)
    print (n_movies)

    while (True):
        idx = random.randrange(0, n_movies)
        print(f'{titles[idx]} {years[idx]}, rating: {ratings[idx]:.1f}, starring: {actors_list[idx]}')


        user_input = input('Do You Want Another Movie (y/[n])? ')
        if user_input != 'y':
            break

if __name__ == '__main__':
    main()