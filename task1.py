
# Доработать класс FlatIterator в коде ниже. Должен получиться итератор,
# который принимает список списков и возвращает их плоское представление,
# т. е. последовательность, состоящую из вложенных элементов.
# Функция test в коде ниже также должна отработать без ошибок.

class FlatIterator:

    def __init__(self, list_of_list):
        self.list_of_list = list_of_list

    def __iter__(self):
        self.counter = 0
        self.inner_counter = 0
        return self

    def __next__(self):
        inner_item = ''
        while inner_item == '':
            if self.counter <= len(self.list_of_list) - 1:
                item = self.list_of_list[self.counter]
                if self.inner_counter <= len(item) - 1:
                    inner_item = item[self.inner_counter]
                    self.inner_counter += 1
                else:
                    self.inner_counter = 0
                    self.counter += 1
            else:
                raise StopIteration

        return inner_item


def test_1():

    list_of_lists_1 = [
        ['a', 'b', 'c'],
        ['d', 'e', 'f', 'h', False],
        [1, 2, None]
    ]

    for flat_iterator_item, check_item in zip(
            FlatIterator(list_of_lists_1),
            ['a', 'b', 'c', 'd', 'e', 'f', 'h', False, 1, 2, None]
    ):

        assert flat_iterator_item == check_item

    assert list(FlatIterator(list_of_lists_1)) == ['a', 'b', 'c', 'd', 'e',
                                                   'f', 'h', False, 1, 2, None]


if __name__ == '__main__':
    test_1()
