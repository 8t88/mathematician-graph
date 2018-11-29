import scraping
import parse_article as pa


home_url = "http://www-groups.dcs.st-andrews.ac.uk/~history/BiogIndex.html"

index_list = scraping.get_indexes(home_url)
print(index_list)

all_bios = []
for index in index_list[0:-3]:
    lst = get_biographies(index)
    all_bios.append(lst)

#set up data structure for holding mathematician and all the links
#then iterate through the biograhpies
for bio in all_bios:
    pa.parse_article(bio)

#then save to json file?
