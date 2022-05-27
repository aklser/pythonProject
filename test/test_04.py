def line_conf():
    bil = 3

    def line(x):
        for i in range(x):
            print(i+bil)
    return line


def line_for():
    def line():
        for i in range(3):
            print(i)

    return line


if __name__ == "__main__":
    # t = line_conf()
    # line_conf()(3)
    # print(t.__closure__)
    # print(t.__closure__[0].cell_contents)
    line_for()()
