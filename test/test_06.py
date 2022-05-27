def pre_str(pre=''):
    def dec(FUNC):
        def NEW_F(a, b):
            print(pre+" input:", a, b)
            return FUNC(a, b)

        return NEW_F
    return dec

@pre_str('aaa')
def MY_SUM(a, b):
    return a + b


if __name__ == "__main__":
    print(MY_SUM(123, 412))
