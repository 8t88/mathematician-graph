from bs4 import BeautifulSoup
import scraper

test_url = "http://www-groups.dcs.st-andrews.ac.uk/~history/Biographies/Lagrange.html"
main_url = "http://www-groups.dcs.st-andrews.ac.uk/~history/BiogIndex.html"

raw_html = scraper.plain_get(test_url)

index_home_html = scraper.plain_get(main_url)
home_html = BeautifulSoup(index_home_html, 'html.parser')
homes = home_html.select('a')#.select('center')#.select('table')

index_list = []

for ref in homes:
    if 'Index' in ref['href']:
        index_list.append(ref['href']
        print(ref['href']) 



biographies_list = []
for ref in drill:
    if 'Biographies' in ref['href']:
        biographies_list.append(ref['href']
        print(ref['href'])



#get h1, add to dict
#search through text for names of others, add them to dict info



#print(homes)
#html = BeautifulSoup(raw_html, 'html.parser')

#article = html.select('article')

#print(article)
#for 
#for p in html.select('p'):


