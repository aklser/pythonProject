def decorator(F):
    def new_F(a, b):
        print("input", a, b)
        return F(a, b)

    return new_F

@decorator
def my_sum(a, b):
    return a + b

@decorator
def my_diff(a, b):
    return a - b


if __name__ == "__main__":
    print(my_sum(1, 3))
    print(my_diff(32, 4))
