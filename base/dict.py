my_dict = {"": "asd", "a": 1, "v": False}
print(my_dict)
print(my_dict[""])
# print(my_dict["1231dfa"])
my_dict[""] = 123
print(my_dict)
my_dict[321] = 12
print(my_dict)
print(len(my_dict))

a_list = [1, 3, 5, 7]
a_tuple = tuple(a_list)
print(a_tuple)
print({a_tuple[i] ** 2: a_list[i] for i in range(len(a_tuple))})
