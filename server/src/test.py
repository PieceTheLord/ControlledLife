a=[(2006,1),(2007,4),(2008,9),(2006,5)]

new_dict={}

for item in a:
    if item[0] not in new_dict:
        new_dict[item[0]]=[item[1]]
    else:
        new_dict[item[0]].append(item[1])

print(new_dict)