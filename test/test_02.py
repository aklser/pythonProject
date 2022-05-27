class VOM(object):
    def __init__(self, text):
        self.text = text

    def __enter__(self):
        self.text = "enter:" + self.text
        return self

    def __exit__(self, exc_type, exc_val, exc_tb):
        self.text = self.text + ">>" + "exit"


if __name__ == "__main__":
    with VOM("now") as myVom:
        print(myVom.text)
    print(myVom.text)
    # reiter = iter(range(5))
    # print(reiter)
    # try:
    #     for i in range(5):
    #         print(reiter.__next__())
    # except StopIteration:
    #     print('here is end,' + i)
    # def test_func():
    #
    #     try:
    #         raise NameError()
    #         m = 1 / 0
    #
    #     except NameError:
    #         print("Catch NameError in the sub-function")
    #
    #
    # try:
    #     test_func()
    # except ZeroDivisionError:
    #     print("Catch error in the main program")
    # a = 'asdasdf'
    # b = a
    # a = 0
    # print(b)
    # def ab(a):
    #     b = a[:]
    #     b[0] = 1
    #     print(b)
    #
    #
    # a = [123, 124, 5647, 1]
    # ab(a)
    # print(a)
    # with open('test01.txt', 'w') as f:
    #     print(f.closed)
    #     f.write('qwer')
    #     print(dir(f.__exit__()))
    # print(f.closed)
