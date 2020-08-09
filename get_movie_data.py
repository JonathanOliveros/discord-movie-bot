#get_movie_data.py
from bs4 import BeautifulSoup
import requests
import os
from dotenv import load_dotenv

load_dotenv()

#keep sensitive information in .ENV
url=os.getenv('URL')

def getMovies(url):
    """use bs4 module to scrape data from desired website"""
    res = requests.get(url)
    res.raise_for_status() #  ensure status code is 200

    soup = BeautifulSoup(res.text, 'html.parser')
    elems = []
    for a in soup.findAll('blockquote'):
        elems.append(a.text)
    return elems



movies = getMovies(url)
file = open('movie_data.txt','w') # write data to .txt file
for line in movies:
    file.write(line)

