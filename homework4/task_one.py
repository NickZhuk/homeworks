from collections import defaultdict
dict1 = {'a': 1, 'b': 2, 'c': 3}
dict2 = {'c': 3, 'd': 4, 'e': 5}
dict3 = defaultdict(list)
for key in set(list(dict1.keys())+list(dict2.keys())):
    if key in dict1:
        dict3[key].append(dict1[key])
        dict3[key].insert(0, None)
    if key in dict2:
        dict3[key].append(dict2[key])
        dict3[key].append(None)
print(dict3)
