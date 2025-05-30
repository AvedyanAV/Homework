import pytest

from src.masks import get_mask_account, get_mask_card_number


def test_get_mask_card_number_standard() -> None:
    """Тест правильности маскирования номера карты"""
    assert get_mask_card_number(1234567890123456) == "1234 56** **** 3456"


@pytest.fixture
def len_numbers() -> list:
    return [12345, 12345678901234567890, ""]


def test_get_mask_card_number_len(len_numbers: str) -> None:
    """Тест проверяющий правильность номера карты с длиной меньше или больше 16 символов"""
    assert get_mask_card_number(len_numbers) == "Некорректный номер карты"


@pytest.fixture
def type_numbers() -> list:
    return ["abcd567890123456", "1234 5678 9012 3456", "1234-5678-9012-3456"]


def test_get_mask_card_number_type(type_numbers: str) -> None:
    """Тест работы функции на различных входных форматах номеров карт"""
    assert get_mask_card_number(type_numbers) == "Некорректный номер карты"


def test_get_mask_account() -> None:
    """Тест правильности маскирования номера счета"""
    assert get_mask_account(12345678901234567892) == "**7892"


@pytest.fixture
def len_account() -> list:
    return [12345, 12345678901234567891561650, ""]


def test_get_mask_account_len(len_account: int) -> None:
    """Тест проверяющий правильность номера счета с длиной меньше или больше 20 символов"""
    assert get_mask_account(len_account) == "Некорректный номер счета"


@pytest.fixture
def type_account() -> list:
    return ["abcd5678901234567895", "123456789012 34564589", "123456789012-34561523"]


def test_get_mask_account_type(type_account: int) -> None:
    """Тест работы функции на различных входных форматах номеров счета"""
    assert get_mask_account(type_account) == "Некорректный номер счета"
