import pytest

from src.processing import filter_by_state, sort_by_date


@pytest.fixture
def state_standard() -> list:
    return [
        {"id": 41428829, "state": "EXECUTED", "date": "2019-07-03T18:35:29.512364"},
        {"id": 939719570, "state": "EXECUTED", "date": "2018-06-30T02:08:58.425572"},
    ]


def test_filter_by_state_standard(state_standard: list) -> None:
    """Тестирование фильтрации списка словарей по заданному статусу"""
    assert filter_by_state(state_standard) == state_standard


@pytest.fixture
def state_not_standard() -> list:
    return [
        {"id": 41428829, "state": "CANCELED", "date": "2019-07-03T18:35:29.512364"},
        {"id": 939719570, "state": "CANCELED", "date": "2018-06-30T02:08:58.425572"},
    ]


def test_filter_by_state_not_standard(state_not_standard: list) -> None:
    """Тестирование работы функции при отсутствии словарей с указанным статусом"""
    assert filter_by_state(state_not_standard) == []


@pytest.fixture
def state_zero() -> list:
    return [
        {"id": 41428829, "state": "", "date": "2019-07-03T18:35:29.512364"},
        {"id": 939719570, "date": "2018-06-30T02:08:58.425572"},
        {},
    ]


def test_filter_by_state_zero(state_zero: list) -> None:
    """Тестирование для различных возможных значений статуса"""
    assert filter_by_state(state_zero) == []


@pytest.fixture
def date_not_standard() -> list:
    return [
        {"id": 41428829, "state": "EXECUTED", "date": "2019-03T18:35:29.512364"},
        {"id": 41428860, "state": "EXECUTED", "date": "2022-07T18:35:29.512364"},
        {"id": 41428829, "state": "EXECUTED", "date": "-07-03T18:35:29.512364"},
    ]


def test_sort_by_date(date_not_standard: list) -> None:
    """Тесты на работу функции с некорректными или нестандартными форматами дат"""
    assert sort_by_date(date_not_standard) == [
        {"id": 41428860, "state": "EXECUTED", "date": "2022-07T18:35:29.512364"},
        {"id": 41428829, "state": "EXECUTED", "date": "2019-03T18:35:29.512364"},
        {"id": 41428829, "state": "EXECUTED", "date": "-07-03T18:35:29.512364"},
    ]


@pytest.fixture
def date_standard() -> list:
    return [
        {"id": 41428829, "state": "EXECUTED", "date": "2019-07-03T18:35:29.512364"},
        {"id": 41428860, "state": "EXECUTED", "date": "2022-07-03T18:35:29.512364"},
        {"id": 41428829, "state": "EXECUTED", "date": "2017-07-03T18:35:29.512364"},
    ]


def test_sort_by_date_standard(date_standard: list) -> None:
    """Тестирование сортировки списка словарей по датам в порядке убывания"""
    assert sort_by_date(date_standard) == [
        {"id": 41428860, "state": "EXECUTED", "date": "2022-07-03T18:35:29.512364"},
        {"id": 41428829, "state": "EXECUTED", "date": "2019-07-03T18:35:29.512364"},
        {"id": 41428829, "state": "EXECUTED", "date": "2017-07-03T18:35:29.512364"},
    ]


@pytest.mark.parametrize(
    "data, sorted, expected",
    [
        (
            [
                {"id": 41428860, "state": "EXECUTED", "date": "2022-07-03T18:35:29.512364"},
                {"id": 41428829, "state": "EXECUTED", "date": "2019-07-03T18:35:29.512364"},
                {"id": 41428829, "state": "EXECUTED", "date": "2017-07-03T18:35:29.512364"},
            ],
            True,
            [
                {"id": 41428860, "state": "EXECUTED", "date": "2022-07-03T18:35:29.512364"},
                {"id": 41428829, "state": "EXECUTED", "date": "2019-07-03T18:35:29.512364"},
                {"id": 41428829, "state": "EXECUTED", "date": "2017-07-03T18:35:29.512364"},
            ],
        ),
        (
            [
                {"id": 41428860, "state": "EXECUTED", "date": "2022-07-03T18:35:29.512364"},
                {"id": 41428829, "state": "EXECUTED", "date": "2019-07-03T18:35:29.512364"},
                {"id": 41428829, "state": "EXECUTED", "date": "2017-07-03T18:35:29.512364"},
            ],
            False,
            [
                {"id": 41428829, "state": "EXECUTED", "date": "2017-07-03T18:35:29.512364"},
                {"id": 41428829, "state": "EXECUTED", "date": "2019-07-03T18:35:29.512364"},
                {"id": 41428860, "state": "EXECUTED", "date": "2022-07-03T18:35:29.512364"},
            ],
        ),
    ],
)
def test_sort_by_date_reverse(data: list, sorted: bool, expected: list) -> None:
    """Тестирование сортировки списка словарей по датам в порядке убывания и возрастания"""
    assert sort_by_date(data, sorted) == expected
