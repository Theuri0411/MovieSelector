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

    while trye


    # inner_movietag0 = innermovietags[0]
    # print (inner_movietag0)
    # actors = inner_movietag0['title']
    # title = inner_movietag0.text
    # print (actors)
    # print(title)
    ratin0 = rating_tags[0]
    print(ratin0 ['data-value'])
    
    
    
    
if __name__ == '__main__':
    main()
    