import types

# Доработать функцию flat_generator. Должен получиться генератор,
# который принимает список списков и возвращает их плоское представление.
# Функция test в коде ниже также должна отработать без ошибок.


def flat_generator(list_of_lists):

    inner_item = ''
    counter = 0
    inner_counter = 0

    while inner_item == '':
        while counter <= len(list_of_lists) - 1:
            item = list_of_lists[counter]
            while True:
                if inner_counter <= len(item) - 1:
                    inner_item = item[inner_counter]
                    inner_counter += 1
                    yield inner_item
                else:
                    inner_counter = 0
                    counter += 1
                    break


def test_2():

    list_of_lists_1 = [
        ['a', 'b', 'c'],
        ['d', 'e', 'f', 'h', False],
        [1, 2, None]
    ]

    for flat_iterator_item, check_item in zip(
            flat_generator(list_of_lists_1),
            ['a', 'b', 'c', 'd', 'e', 'f', 'h', False, 1, 2, None]
    ):

        assert flat_iterator_item == check_item

    assert list(flat_generator(list_of_lists_1)) == ['a', 'b', 'c', 'd', 'e',
                                                     'f', 'h', False, 1, 2,
                                                     None]

    assert isinstance(flat_generator(list_of_lists_1), types.GeneratorType)


if __name__ == '__main__':
    test_2()
