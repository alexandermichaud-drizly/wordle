from urllib import request
from bs4 import BeautifulSoup

URL = 'https://www-cs-faculty.stanford.edu/~knuth/sgb-words.txt'

file = request.urlopen(URL)
doc = file.read()
text = BeautifulSoup(doc, 'html.parser').get_text()

WORD_BANK = text.split('\n')
