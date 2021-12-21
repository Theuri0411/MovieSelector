import random
import requests
from bs4 import BeautifulSoup



url = "https://www.imdb.com/chart/top"

def main(args):
    response = requests.get(url)
    html = response.text

    soup = BeautifulSoup(html, "html.parser")
    movietags = soup.select ("td.tittleColumn")
    movietags0 = movietags(0)
    


if __name__ == '__main__':
    main()
        