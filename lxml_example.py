from lxml.html import fromstring, tostring
from link_crawler import download



url = 'http://example.webscraping.com/places/default/view/Afghanistan-1'
html = download(url)
tree = fromstring(html) # parse the HTML
td = tree.cssselect('tr#places_area__row > td.w2p_fw')[0]
area = td.text_content()
print(area)
