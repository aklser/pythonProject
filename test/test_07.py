def decorator(aclass):
    class newClass:
        def __init__(self, age):
            self.total_display = 0
            self.wrapped = aclass(age)

        def display(self):
            self.total_display += 1
            print("total display:", self.total_display)
            self.wrapped.display()

    return newClass


@decorator
class Bird:
    def __init__(self, age):
        self.age = age

    def display(self):
        print("age:", self.age)


if __name__ == "__main__":
    bi = Bird(3)
    for i in range(3):
        bi.display()
    bi.display()
