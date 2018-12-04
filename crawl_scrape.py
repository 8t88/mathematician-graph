from bs4 import BeautifulSoup
import scraper_utils as scraper

def get_indexes(url):

    index_home_html = scraper.plain_get(url)
    home_html = BeautifulSoup(index_home_html, 'html.parser')
    homes = home_html.select('a')

    index_list = []

    for ref in homes:
        if 'Index' in ref['href']:
            index_list.append(ref['href'])

    return index_list

def get_biographies(index):
    biographies_list = []
    index_url = 'http://www-groups.dcs.st-andrews.ac.uk/~history/'
    drill_url = index_url + index
    print(drill_url)

    drill_html = scraper.plain_get(drill_url)
    try:
        drill_html_parse = BeautifulSoup(drill_html, 'html.parser')
        drill_links = drill_html_parse.select('a')
        #format into list of dicts with {name:url} for easier iterating later
        if len(drill_links)>0:
            for ref in drill_links:
                if 'Biographies' in ref['href']:
                    bio_url = ref['href'][2:]#removing the ..

                    bio_name_html = bio_url.split('/')[-1]
                    bio_name = bio_name_html.split('.')[0]

                    biographies_list.append({"name":bio_name, "url": bio_url})
        else:
            print("no links")
    except Exception as e:
        print(e)
    return biographies_list



#for index in index_list:
#    biograhpies = get_biographies(index)

#home_url = "http://www-groups.dcs.st-andrews.ac.uk/~history/BiogIndex.html"

#index_list = get_indexes(home_url)
#print(index_list)

#lst = get_biographies(index_list[4])
#print(lst)
