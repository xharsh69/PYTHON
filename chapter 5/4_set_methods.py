s= {34,56,67,45,34,45,23, "harsh","singh"}


s.add("raj") # add new eleament
s.remove(56) # remove eleament
s.pop() # remoeve random eleament

new_set = s.copy() # copy set
s.clear()

print(s, type(s))
print(new_set)


# More Set Operations

a = {1, 2, 3}
b = {3, 4, 5}

# Union
print(a.union(b))

# Intersection
print(a.intersection(b))

# Difference
print(a.difference(b))

print(len(new_set))