from client import Client

c = Client()


def test1():
    # functions that don't return
    x = c.interface.functions.create(15, 'deset').transact()
    print(x)


def test2():
    x = c.interface.get_text(5)
    print(x)


def test3():
    i = 0
    while True:
        x = c.call.get_number(i)
        if x == 0:
            return
        print(i, x)
        i += 1


def test4():
    print(c.transaction('create', 20, 'ssss'))


test3()
