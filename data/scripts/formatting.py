
links = []

main_name = ""
for name in mathematicians_list:
    entry = {
            "source": main_name,
            "target": name
            }
    links.append(entry)


#save links to json file
