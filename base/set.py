my_set = {1, 3, 2, 3, 1, 1}
print(my_set)
print(type({}))
my_set.update({1, 32, 546}, {45, 65, 12, 12, 1, 546})
print(my_set)
my_set.add(123)
print(my_set)

my_set.discard(123)
print(my_set)
my_set.remove(45)
print(my_set)
my_set.pop()
print(my_set)

a_set = {1, 2, 3, 4}
b_set = {3, 4, 5, 6}
print("****")
print(a_set.union(b_set))
print(a_set.intersection(b_set))
print(a_set.difference(b_set))
print(a_set.symmetric_difference(b_set))
