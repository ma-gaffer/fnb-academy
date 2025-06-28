#sets
'''''
my_set ={1, 2, 3, 4, 5}

print(my_set)

my_set.add(6)
print(my_set)

my_set.remove(3)
print(my_set)
'''
set1 = {1, 2, 3}
set2 = {3, 4, 5}

#union
union_set=set1.union(set2)
print(union_set)

#intersection
inter_set = set1.intersection(set2)
print(inter_set)

#difference
diff_set = set1.difference(set2)
print(diff_set)