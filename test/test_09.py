if __name__ == "__main__":
    a = [12, 41, 45, 6]
    b = "qwdqwf"
    try:
        print(a.index(12))
    except ValueError:
        print('找不到该值')
    else:
        print("xx")
    finally:
        print("end")