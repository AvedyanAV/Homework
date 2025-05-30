import pytest

from src.widget import get_date, mask_account_card


def test_get_date_standard() -> None:
    """Тестирование правильности преобразования даты"""
    assert get_date("2024-03-11T02:26:18.671407") == "11.03.2024"


@pytest.fixture
def date_type() -> list:
    return ["12024-03-11T02:26:18.671407",
            "2024-50-11T02:26:18.671407",
            "2024-03-50T02:26:18.671407",
            "",
            "0000-03-50T02:26:18.671407"]


def test_get_date_type(date_type: list) -> None:
    """Тест работы функции на некорректную дату"""
    for date in date_type:
        assert get_date(date) == "Некорректный формат даты"


@pytest.fixture
def date_day_in_month() -> list:
    return [
        "2024-02-30T02:26:18.671407",
        "2024-04-31T02:26:18.671407",
        "2024-06-31T02:26:18.671407",
        "2024-09-31T02:26:18.671407",
        "2024-11-31T02:26:18.671407",
    ]


def test_date_day_in_month(date_day_in_month: list) -> None:
    """Тест работы функции на количество дней в месяце"""
    for date in date_day_in_month:
        assert get_date(date) == "Некорректный формат даты"


@pytest.mark.parametrize(
    "account_card, expected",
    [
        ("Visa Platinum 7000792289606361", "Visa Platinum 7000 79** **** 6361"),
        ("Счет 73654108430135874305", "Счет **4305"),
    ],
)
def test_mask_account_card_standard(account_card: str, expected: str) -> None:
    """Тест правильности маскирования номера карты, счета"""
    assert mask_account_card(account_card) == expected


@pytest.mark.parametrize(
    "account_card, expected",
    [
        ("Maestro 1596837868705199", "Maestro 1596 83** **** 5199"),
        ("Счет 64686473678894779589", "Счет **9589"),
        ("MasterCard 7158300734726758", "MasterCard 7158 30** **** 6758"),
    ],
)
def test_mask_account_cards(account_card: str, expected: str) -> None:
    """Тесты с разными типами карт и счетов для проверки универсальности функции"""
    assert mask_account_card(account_card) == expected
