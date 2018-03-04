import time

FIELDS = ('area', 'population', 'iso', 'country', 'capital', 'continent',
'tld', 'currency_code', 'currency_name', 'phone', 'postal_code_format',
'postal_code_regex', 'languages', 'neighbours')

import re
def re_scraper(html):
 results = {}
 for field in FIELDS:
     results[field] = re.search('<tr id="places_%s__row">.*?<td class ="w2p_fw" > (.* ?) < / td > ' % field, html).groups()[0]
 return results


from bs4 import BeautifulSoup


def bs_scraper(html):
    soup = BeautifulSoup(html, 'html.parser')
    results = {}
    for field in FIELDS:
        results[field] = soup.find('table').find('tr', id='places_%s__row' %
                                                          field).find('td', class_='w2p_fw').text
    return results


from lxml.html import fromstring


def lxml_scraper(html):
    tree = fromstring(html)
    results = {}
    for field in FIELDS:
        results[field] = tree.cssselect('table > tr#places_%s__row > td.w2p_fw ' % field)[0].text_content()
    return results


def lxml_xpath_scraper(html):
    tree = fromstring(html)
    results = {}
    for field in FIELDS:
        results[field] = tree.xpath('//tr[@id="places_%s__row"]/td[@class="w2p_fw"]' %
           field)[0].text_content()
    return results


from link_crawler import download

NUM_ITERATIONS = 1000 # number of times to test each scraper
html = download('http://example.webscraping.com/places/default/view/Afghanistan-1')
from link_crawler import download
scrapers = [
 # ('Regular expressions', re_scraper),
 ('BeautifulSoup', bs_scraper),
 ('Lxml', lxml_scraper),
 ('Xpath', lxml_xpath_scraper)]
for name, scraper in scrapers:
 # record start time of scrape
 start = time.time()
 for i in range(NUM_ITERATIONS):
    if scraper == re_scraper:
        re.purge()
    result = scraper(html)
    # check scraped result is as expected
    assert result['area'] == '647,500 square kilometres'
 # record end time of scrape and output the total
 end = time.time()
 print('%s: %.2f seconds' % (name, end - start))
