a = "name"
b = 2
print(f"I am {a},my age is {b:.3f}")
print(f"{a:10s}=>>>>{b:10d}")
print(f"{a:8s}=>>>>{b:8d}")
yes_votes = 42_572_654
no_votes = 43_132_495
percentage = yes_votes / (yes_votes + no_votes)
print('{:-9} YES votes  {:2.2%}'.format(yes_votes, percentage))

x = "2"
y = "x"
print(str(x))
print(repr(x))
print(repr((x, y, ('spam', 'eggs'))))
print(str((x, y, ('spam', 'eggs'))))
with open("../test/test.txt") as f:
    print(f.readline())
