class bird(object):
    feather = True


class chicken(bird):
    fly = False

    def __init__(self, age):
        self.age = age

    def getAge(self):
        return self.age

    def setAge(self, age):
        self.age = age

    def delAge(self):
        print("success")
        del self.age

    value = property(getAge, setAge, delAge, "value")


if __name__ == "__main__":
    summer = chicken(2)
    print(bird.__dict__)
    print(chicken.__dict__)
    print(summer.__dict__)
    print(summer.__class__.__base__)
    # print(summer.value.__doc__)
    del summer.value
