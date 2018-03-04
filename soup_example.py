from bs4 import BeautifulSoup

from link_crawler import download

url = 'http://example.webscraping.com/places/default/view/Afghanistan-1'
html = download(url)
soup = BeautifulSoup(html, "lxml")
tr = soup.find(attrs={'id':'places_area__row'})
td = tr.find(attrs={'class': 'w2p_fw'})  # locate the data element
area = td.text  # extract the text from the data element
print(area)