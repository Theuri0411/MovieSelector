import random
import requests
from bs4 import BeautifulSoup



url = 'https://www.imdb.com/chart/top'

def main():
    response = requests.get(url)
    html = response.text

    soup = BeautifulSoup(html, 'html.parser')
    movietags = soup.select ("td.titleColumn")
    inner_movietags = soup.select('td.titleColumn a')
   
    
    def get_year (movie_tag):
        moviesplit = movie_tag.text.split()
        year = moviesplit[-1]
        return year
    years = [get_year(tag) for tag in movietags]

    inner_movietag0 = inner_movietags[0]
    print (movietag0)
    # title = tag['title']
    
    
    
    
    
if __name__ == '__main__':
    main()
    