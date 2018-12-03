from bs4 import BeautifulSoup
import scraper_utils as scraper

test_url = "http://www-groups.dcs.st-andrews.ac.uk/~history/Biographies/Lagrange.html"

def parse_article(url):
    mathematicians_list = []

    raw_html = scraper.plain_get(url)
    raw_html_soup = BeautifulSoup(raw_html, 'html.parser')

    links = raw_html_soup.select('a')

    for ref in links:
        if 'Mathematicians' in ref['href']:
            name_html = ref['href'] .split('/')[-1]
            name = name_html.split('.')[0]
            mathematicians_list.append(name)
    
    return mathematicians_list


print(parse_article(test_url))
