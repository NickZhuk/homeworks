a = {'a': 1, 'b': 2, 'c': 3}
b = {'c': 3, 'd': 4, 'e': 5}
ab = dict()
a_keys = list(a.keys())
b_keys = list(b.keys())
a_set_keys = set(a_keys)
b_set_keys = set(b_keys)
common_keys = list(a_set_keys.union(b_set_keys))
for key in common_keys:
    ab[key] = [a.get(key), b.get(key)]
print(ab)
