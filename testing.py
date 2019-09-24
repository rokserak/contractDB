from client import Client
import unittest

c = Client()


class TestDatabase(unittest.TestCase):

    # insert
    def test1(self):
        c.interface.functions.create(15, 'deset').transact()
        db = c.get_all()
        is_in = False
        for i, num, text in db:
            if num == 15 and text == 'deset':
                is_in = True
                break
        self.assertTrue(is_in)

    # delete
    def test2(self):
        c.interface.functions.create(10, 'a').transact()
        db = c.get_all()
        id = 0
        for i, num, text in db:
            if num == 10 and text == 'a':
                id = i
                break
        c.transaction('deleted', id)

        num = c.call.get_number(id)
        text = c.call.get_text(id)
        self.assertTrue(num == -1 and text == 'deleted')

    # update
    def test3(self):
        c.transaction('create', 5, 'b')
        db = c.get_all()
        id = 0
        for i, num, text in db:
            if num == 5 and text == 'b':
                id = i
                break
        self.assertTrue(id > 0)

        c.transaction('set_number', id, 50)
        c.transaction('set_text', id, 'ola')

        num = c.call.get_number(id)
        text = c.call.get_text(id)

        self.assertTrue(num == 50 and text == 'ola')


if __name__ == '__main__':
    unittest.main()
