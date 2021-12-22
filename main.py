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
   
    
    def get_year (movie_tag):
        moviesplit = movie_tag.text.split()
        year = moviesplit[-1]
        return year
    years = [get_year(tag) for tag in movietags]
    actors_list = [tag['title'] for tag in innermovietags]
    titles = [tag.text for tag in innermovietags]


    inner_movietag0 = innermovietags[0]
    print (inner_movietag0)
    actors = inner_movietag0['title']
    title = inner_movietag0.text
    print (actors)
    print(title)
    
    
    
    
    
if __name__ == '__main__':
    main()
    