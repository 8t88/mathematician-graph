import crawl_scrape as scrape
import parse_article as pa
import json

home_url = "http://www-groups.dcs.st-andrews.ac.uk/~history/BiogIndex.html"

index_list = scrape.get_indexes(home_url)
#print(index_list)

all_bios = []
for index in index_list[2]:
#for index in index_list[0:-3]: #last 3 entries are irrelevant
    lst = scrape.get_biographies(index)
    all_bios= all_bios + lst

#set up data structures for holding mathematician and all the links
mathematicians = set()#set #start with set, then change into list
links = []

#then iterate through the biographies
for bio_dict in all_bios:
    mathematicians.add(bio_dict['name'])
    links_list = pa.parse_article(bio_dict['url'])
    for names in links_list:
        links.append({"source": bio_dict['name'], "target": bio, "weight": 1})

nodes = [] #transform dict of names into list of dicts
for math in mathematicians:
    nodes.append({"name": math, "group": 1})

#then save to json file?
with open('links.json', 'w') as outfile:
    json.dump(links, outfile)
with open('nodes.json', 'w') as outfile:
    json.dump(nodes, outfile)
