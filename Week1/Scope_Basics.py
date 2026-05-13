x = 10   # global

def test():
    y = 5   # local
    print(x)  # can access global
    print(y)  # can access local

test()
