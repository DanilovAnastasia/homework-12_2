import pytest


@pytest.fixture()
def get():
    def _get(array, index, default=None):
        """
        Извлекает из списка значение по указанному индексу, если индекс существует.
        Если индекс не существует, возвращает значение по умолчанию.
        Функция работает только с неотрицательными индексами.
        :param array: исходный список.
        :param index: индекс извлекаемого элемента.
        :param default: значение по-умолчанию.
        :return: значение по индексу или значение по-умолчанию.
        """

        if 0 <= index < len(array):
            return array[index]
        return default
    print('\n----------Start_test-------------')
    yield _get
    print('\n----------End_test---------------')


@pytest.fixture()
def my_slice():
    def _my_slice(coll, start=None, end=None):
        """
        Возвращает новый массив, содержащий копию части исходного массива.
        :param coll: исходный список.
        :param start: индекс, по которому начинается извлечение. Если индекс отрицательный,
        start указывает смещение от конца списка. По умолчанию равен нулю.
        :param end: индекс, по которому заканчивается извлечение (не включая элемент с индексом end).
        Если индекс отрицательный, end указывает смещение от конца списка. По умолчанию равен длине исходного списка.
        :return: массив элементов
        """

        length = len(coll)

        if length == 0:
            return []

        if start is None:
            normalized_start = 0
        else:
            normalized_start = start

        if end is None or end > length:
            normalized_end = length
        else:
            normalized_end = end

        return coll[normalized_start:normalized_end]
    print('\n----------Start_test-------------')
    yield _my_slice
    print('\n----------End_test---------------')


def test_get(get):
    assert get([1, 2, 3], 1, "test") == 2
    assert get([], 0, "test") == "test"


def test_slice(my_slice):
    assert my_slice([1, 2, 3, 4], 1, 3) == [2, 3]
    assert my_slice([1, 2, 3], 1) == [2, 3]
    assert my_slice([1, 2, 3], None) == [1, 2, 3]
    assert my_slice([], None) == []